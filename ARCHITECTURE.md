# TestSpectra Project Architecture

This project is built with the TestSpectra testing framework.

## Structure & File Map
- `./spectra.config.ts`: Typed runner configuration.
- `./specs/`: Layered test cases (`specs/<Suite>/<CaseId>/` with `web.test.ts`, `android.test.ts`, `ios.test.ts`).
- `./page-objects/`: Page Object models per platform.
- `./support/steps/`: Business flows accessible globally via `Step.*`.
- `./support/actions/`: Atomic actions accessible globally via `Spectra.*`.
- `./fixtures/`: JSON fixtures accessible globally via `Fixture.*`.
- `./global-hooks/`: Global suite lifecycle hooks.
- `./.testspectra/`: Auto-generated ambient typings and local runtime cache.

## Execution
```bash
# Run web test suite
pnpm test

# Run Android / iOS
pnpm spectra run --target android
pnpm spectra run --target ios

# Type check
pnpm type-check
```
