# Blog Card Layout Fix

- [x] Add a regression check for mobile post card cover width.
- [x] Verify the regression check fails on the current CSS.
- [x] Fix the mobile post card image rule in `scss/modern.min.css`.
- [x] Run build and automated verification.
- [x] Inspect the homepage at 901px width.
- [x] Record review notes.
- [x] Commit and push to `origin/gh-pages`.

## Review

- Root cause: `modern.min.css` loaded after `journal.min.css` and reset `.post-item-image` to `width: 220px`; the later mobile override only changed height and border radius.
- Fix: set mobile `.post-item-image` to `width: 100%` inside the existing `max-width: 1020px` rule.
- Verification: `node tests/check-mobile-card-css.mjs`, `npm run build`, and a 901x857 Chromium screenshot of `http://127.0.0.1:4173/`.
