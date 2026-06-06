---
title: "RISC-V Vector上下文调度框架"
date: "2025-11-11T10:00:57+08:00"
updated: "2025-11-11T02:37:27.420Z"
slug: "RISC-V-Vector上下文调度框架"
description: "riscv vector上下文追踪机制分析"
categories: 
  - "体系结构"
tags: 
  - "SIMD"
series: 
  - "RISC-V 笔记"
featured_image: "/images/covers/riscv-vector-context-scheduling.png"
pinned: false
---

<h1 id="1-背景">1 背景</h1><blockquote>
<p>基于<a target="_blank" rel="noopener" href="https://lore.kernel.org/linux-riscv/20240108035209.GA212605@sol.localdomain/T/#mda836061caf7a5db9b6994a58ec8e32721ae5038">[v9, 00/10] riscv: support kernel-mode Vector</a>，目前v6.7主线未合入。</p>
<hr>
<p>从多hart多task角度出发，返回用户态前，hart上装载的如果不是即将被调度task的vector_state是否能感知到？</p>
<ul>
<li>hart视角下：TIF_RISCV_V_DEFER_RESTORE没问题</li>
<li>task视角下：如果task还被调度到原hart上时，原hart的vector_state不变，原实现感知不到。</li>
</ul>
</blockquote>
<p><img src="https://cdn.jsdelivr.net/gh/MaskerDad/BlogImage@main/202401111027078.png" alt="image-20240111102727997"></p>
<h1 id="2-框架">2 框架</h1><p>为了减少不必要地保存和恢复vector状态的次数，内核需要跟踪两件事：</p>
<blockquote>
<p>a) 对于每个任务，内核需要记住最后一个将任务的vector状态加载到寄存器上的hart是哪一个；</p>
<p>b) 对于每个hart，内核需要记住最近加载到寄存器上的用户态vector状态属于哪个任务，或者在此期间是否已被用于执行内核模式vector操作。</p>
</blockquote>
<ul>
<li>对于a），向 <code>thread_struct</code> 添加了一个 <code>vector_cpu</code> 字段，每当vector状态被加载到hart上时，该字段会更新为当前hart的ID。</li>
<li>对于b），添加了per-hart变量 <code>vector_last_state</code>，其中包含最近加载到hart上的任务的用户空间vector状态的地址，如果在此之后执行了内核模式vector，则为NULL。</li>
</ul>
<hr>
<p>基于以上，我们在任务切换时就不再需要立即恢复下一个vector状态，可以将这个检查推迟到用户空间的恢复阶段，在这个阶段需要验证hart的 <code>vector_last_state</code> 和任务的 <code>vector_cpu</code> 是否仍然保持同步。如果同步，就可以省略vector的恢复操作。</p>
<p>为了更好地描述上述的 <code>task-hart</code> 的双向同步机制，使用统一线程标识 <code>TIF_FOREIGN_VSTATE</code> 来指示当前任务的用户态vector状态是否存在于hart中。如果当前hart的vetor寄存器包含当前任务的最新用户态vector状态，不设置该标志，否则设置。</p>
<p>对于某个任务，其可能的执行序列如下：</p>
<ul>
<li>**任务被调度：**如果任务的vector_cpu字段包含当前hart的ID，且hart的 <code>vector_last_state</code> per-cpu变量指向任务的vector_state，<code>TIF_FOREIGN_VSTATE</code> 标志位被清除，否则被设置；</li>
<li>**任务返回到用户空间：**如果设置了 <code>TIF_FOREIGN_VSTATE</code> 标志，任务的用户空间vector状态将从内存复制到寄存器中，任务的vector_cpu字段将设置为当前hart的ID，当前hart的 <code>vector_last_state</code> 指针将设置为该任务的vstate，并清除 <code>TIF_FOREIGN_VSTATE</code> 标志；</li>
<li>**该任务执行一个普通的系统调用：**当返回到用户空间时，<code>TIF_FOREIGN_VSTATE</code> 标志仍将被清除，因此不会恢复vector状态；</li>
<li>**该任务执行一个系统调用，该系统调用执行一些vector指令：**在此之前，调用 <code>kernel_vector_begin()</code> 函数，将任务的vector寄存器内容复制到内存中，清除vector_last_state变量，并设置 <code>TIF_FOREIGN_VSTATE</code> 标志；</li>
<li>**在调用kernel_vector_end()之后，任务被抢占：**由于我们还没有从第二个系统调用中返回，<code>TIF_FOREIGN_VSTATE</code>仍然被设置，因此vector寄存器中的内容不会被保存到内存中，而是被丢弃。</li>
</ul>
<p><img src="https://cdn.jsdelivr.net/gh/MaskerDad/BlogImage@main/202312201753572.png" alt="fpsimd_reduce_switch_times.drawio"></p>
<ol>
<li><p><strong>task0首次被调度：</strong></p>
<blockquote>
<p>判断是否保持同步:</p>
<p>TIF_FOREIGN_VSTATE = (task0-&gt;vector_cpu != hart0 || vector_last_state != task0)</p>
</blockquote>
</li>
<li><p><strong>task0返回用户态：</strong></p>
<blockquote>
<p>* 判断TIF_FOREIGN_VSTATE，这里为TRUE，<br>那就恢复vector_state到寄存器上；<br>* task0-&gt;vector_cpu = hart0;<br>* vector_last_state = task0;<br>* TIF_FOREIGN_VSTATE = false;</p>
</blockquote>
</li>
<li><p><strong>task0让出CPU控制权</strong></p>
</li>
<li><p><strong>task0再次被调度运行，目标CPU仍然为hart0：</strong></p>
<blockquote>
<p>还是判断和1）相同的两个变量，看是否同步，此时：<br>task0-&gt;vector_cpu = hart0；<br>vector_last_state = task0;<br>=&gt; TIF_FOREIGN_VSTATE = false;</p>
</blockquote>
</li>
<li><p><strong>task0再次返回用户态：</strong></p>
<blockquote>
<p>task0再次被调度运行，目标CPU仍然为hart0：</p>
</blockquote>
</li>
</ol>
<hr>
<p>后续工作：</p>
<ul>
<li><input disabled="" type="checkbox"> 考虑能否基于原 <code>DEFER</code> 进程标识实现；</li>
<li><input disabled="" type="checkbox"> 依次验证进程调度、内核模式vector操作、信号处理等非常虚拟化场景下的开销；</li>
<li><input disabled="" type="checkbox"> 接入KVM：<ul>
<li><input disabled="" type="checkbox"> 分析现有 <code>vcpu_load/restore</code> 路径上的vector切换是否存在问题； </li>
<li><input disabled="" type="checkbox"> 关于 <code>TIF_FOREIGN_VSTATE</code> 的设置时机；</li>
</ul>
</li>
</ul>
