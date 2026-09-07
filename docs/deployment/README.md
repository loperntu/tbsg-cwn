# Publish the prepared CiWN website

Target: https://lopentu.github.io/sindia-site/buddhist/

Status on 2026-09-07: static site, bilingual project pages and navigation changes are ready. The GitHub integration returned `403 Resource not accessible by integration` when creating the site tree. No site commit or deployment was made. Research repository writes are separate.

## Review and apply

The patch was prepared against `lopentu/sindia-site` main commit `5ef5f0b9b46e8bfb7446608df8a407ce1540c819`. Use an authorized checkout and retain any newer work.

```bash
git switch main
git pull --ff-only
git apply --check /path/to/sindia-site.patch
git apply /path/to/sindia-site.patch
npm ci
npm run build
git diff --check
git diff --stat
```

After reviewing the result, commit the changes and push main. The repository’s existing `Deploy Next.js site to Pages` workflow builds and publishes `out/`. Confirm a successful workflow, then confirm the public project URL and `proposal.html`, `pnc-talk.html`, `release.html`, and `data/claims.json`. Do not describe the site as live until those checks pass.

## Scope

- Static assets under `public/buddhist/`, with no external JavaScript dependency.
- Desktop/mobile navigation entries and English/Traditional Chinese labels.
- 16 candidate claims, 6 evidence windows, 27 native CWN senses, original source headers and source terms.
- Full bilingual proposal, PNC talk guide and reproducibility notes.

HCC was not changed. Local JavaScript syntax and relative-resource links were checked. The Next.js production build and hosted behavior still require validation in the authorized deployment environment.
