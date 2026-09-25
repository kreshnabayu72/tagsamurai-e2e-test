# CLAUDE.md - TestSpectra Framework Conventions

## Commands
- Run all Web tests: `pnpm test:web` (or `spectra run -t web`)
- Run all Mobile tests: `pnpm test:mobile` (or `spectra run -t mobile`)
- Run Android tests: `pnpm test:android` (or `spectra run -t android`)
- Run iOS tests: `pnpm test:ios` (or `spectra run -t ios`)
- Run specific spec: `spectra run "specs/Playground/TC-0001-form-controls/mobile.test.ts" -t mobile`
- Type checking: `pnpm type-check` (or `tsc -b`)
- Preflight doctor: `pnpm doctor` (or `spectra doctor`)
- Sync ambient types: `pnpm sync-types`

## Element Selectors
- `~name` → **accessibility id** (Android `content-desc`, RN `accessibilityLabel`, web `aria-label`) — the portable default.
- `#name` → **native id** (Android `resource-id`, RN `testID`, web CSS `id`).
- Each prefix maps to exactly one attribute (no silent cross-matching). Prefer `~` for user-perceivable elements, `#` for stable test ids. See `docs/v2/cli/selectors.md`.
