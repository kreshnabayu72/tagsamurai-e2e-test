---
name: workspace-structure
description: TestSpectra workspace layout, zero-import ambient type architecture, platform file suffixes (web/android/ios/mobile/common), spectra.config.ts, and the core spectra CLI commands. Use before scaffolding any new TestSpectra project or file so it lands in the right directory with the right suffix.
---

# Skill: TestSpectra Workspace Structure & Zero-Import Architecture

Use this skill whenever you scaffold a new TestSpectra workspace, add a new file to an existing
one, or need to decide where a Page Object / Step / Action / Hook / Fixture belongs.

---

## 1. Core Philosophy: Git-First, Spec-as-Code

Every test case, shared step, Page Object, fixture, and config file is a plain TypeScript or
Markdown file tracked in git — there is no proprietary binary project format. TestSpectra supports
two workspace paradigms:

1. **Default Project Mode** (`spectra init`, single-root repo) — one app, one `spectra.config.ts`.
2. **Monorepo / Nx Project Mode** (`spectra init --template nx`) — multiple `packages/*` test
   projects sharing a library under `shared/testing` (or a custom path), wired into
   `pnpm-workspace.yaml`.

Never guess which mode a repo uses — check for `nx.json` / `pnpm-workspace.yaml` with a
`packages:` list first.

---

## 2. Default Workspace Directory Layout

```
my-test-project/
├── .testspectra/                # Auto-managed. NEVER hand-edit these files.
│   ├── tsconfig/                 # web.json, mobile.json, android.json, ios.json, common.json
│   ├── types/                    # web.d.ts, mobile.d.ts, android.d.ts, ios.d.ts, common.d.ts,
│   │                              # fixtures.d.ts — ambient globals (Spectra, Step, Fixture, POs)
│   └── reports/                  # report.json, network-resources.json, last-run.json
│
├── specs/                        # Test suites & test cases (Spec-as-Code)
│   └── <SuiteName>/
│       ├── suite.md              # Suite metadata (id, name, executionOrder, parallel)
│       ├── hooks/                 # Suite-level lifecycle hooks (before/beforeEach/afterEach/after)
│       └── TC-<NNNN>-<slug>/     # One directory per test case
│           ├── spec.md            # Frontmatter + "## Test Steps" with @step:<name> directives
│           ├── web.test.ts        # and/or android.test.ts / ios.test.ts / mobile.test.ts / common.test.ts
│
├── page-objects/                 # Page Object Model singletons
│   └── <PageName>/
│       ├── web.ts
│       └── mobile.ts             # (or android.ts / ios.ts)
│
├── support/
│   ├── steps/                    # High-level reusable business workflows (Step.*)
│   │   └── <stepName>/
│   │       ├── step.md
│   │       ├── web.step.ts
│   │       └── mobile.step.ts
│   └── actions/                  # Low-level technical utilities (Spectra.<action>())
│       └── <actionName>/
│           ├── web.action.ts
│           └── mobile.action.ts
│
├── fixtures/                     # JSON/CSV test data, auto-typed under Fixture.*
│   └── users.json
│
├── global-hooks/                 # Workspace-wide hooks, run once per Global Batch Run only
│   ├── before/
│   └── after/
│
├── spectra.config.ts             # Single source of truth for execution settings
├── tsconfig.json                 # References ./.testspectra/tsconfig.json — do not add "include"
└── package.json                  # Has "postinstall": "spectra sync-types"
```

For the Nx/monorepo variant, each `packages/<project>/` is its own self-contained workspace
(`specs/`, `page-objects/`, `spectra.config.ts`, `package.json`), and a shared library
(default `shared/testing/`) holds cross-project Page Objects/Steps/Actions/Fixtures. **Never** put
a `specs/` directory or a `spec.md`/`suite.md` file inside the shared library — the linter rejects
it (`testspectra/no-specs-in-shared-lib`).

---

## 3. Zero-Import Rule (Non-Negotiable)

TestSpectra scripts **never** contain a manual `import` statement for framework entities. Page
Objects, `Step.*`, `Fixture.*`, and the global `Spectra` object are all injected as ambient
globals via `.testspectra/types/*.d.ts`, which the CLI regenerates automatically (sub-60ms) when
you add/rename files under `page-objects/`, `support/`, or `fixtures/`.

- ❌ `import LoginPage from '../../page-objects/LoginPage';`
- ✅ Just reference `LoginPage` directly — it resolves globally.

Adding an `import` in a `*.test.ts`, `*.step.ts`, `*.action.ts`, `*.hook.ts`, or Page Object file
triggers linter rule `testspectra/no-manual-import` (error). If a file's types look stale after you
add a new Page Object/Step/Fixture, run `spectra sync-types` rather than importing manually.

---

## 4. Platform File Suffixes

| Suffix        | Target                      | Can access                                    |
| :------------ | :-------------------------- | :-------------------------------------------- |
| `*.web.*`     | Web (Chrome CDP)            | web + common                                  |
| `*.android.*` | Android (native TCP driver) | android + mobile + common                     |
| `*.ios.*`     | iOS (XCUITest)              | ios + mobile + common                         |
| `*.mobile.*`  | Shared Android & iOS        | mobile + common only (no web, no android/ios) |
| `*.common.*`  | Universal (web + mobile)    | common only (strictest isolation)             |

This applies to test scripts (`web.test.ts`), Page Objects (`web.ts`), steps (`web.step.ts`),
actions (`web.action.ts`), and hooks (`web.hook.ts`). Pick the narrowest suffix that fits — don't
write a `mobile.test.ts` for something that is actually web-only.

---

## 5. `spectra.config.ts`

```typescript
import { defineConfig } from '@testspectra/cli';

export default defineConfig({
  webConfig: {
    baseUrl: 'http://localhost:5173',
    maxConcurrentSessions: '1',
    headless: true,
    implicitWait: '5000',
    parallelizationMode: 'testcase', // "testcase" | "suite"
  },
  androidConfig: {
    driverServer: 'tcp://127.0.0.1:8200',
    appPackage: 'dev.example.app',
    appActivity: 'dev.example.app.MainActivity',
    noReset: false,
    implicitWait: '10000',
    parallelizationMode: 'suite',
    devices: [{ id: 'emulator-5554', name: 'Pixel 8a Emulator', version: '14.0', systemPort: 8200 }],
  },
  iosConfig: {
    appiumServer: 'http://127.0.0.1:4723',
    automationName: 'XCUITest',
    bundleId: '',
    autoAcceptAlerts: true,
    noReset: false,
    implicitWait: '10000',
    parallelizationMode: 'suite',
    devices: [
      { id: 'iphone-15-pro', name: 'iPhone 15 Pro Simulator', version: '17.0', udid: 'auto', wdaLocalPort: 8100 },
    ],
  },
  executionConfig: {
    networkMonitoringEnabled: true,
    fastResponseTime: '200',
    normalResponseTime: '1000',
    monitoredDomains: [{ domain: 'api.example.com', enabled: true }],
    environmentVariables: { API_MODE: 'sandbox' },
  },
});
```

Numeric-looking fields (timeouts, ports, session counts) accept either a `number` or a numeric
`string` — stay consistent with whatever the rest of the file already uses.

`executionConfig` notes:

- **`monitoredDomains`**: empty/absent = record every domain; non-empty = only requests matching
  an `enabled: true` entry (exact hostname or leading-`*` wildcard) get recorded/streamed to the
  Network panel. `networkMonitoringEnabled: false` disables recording outright regardless of this
  list.
- **`fastResponseTime`/`normalResponseTime`**: millisecond thresholds the VS Code Network panel
  uses to color each request's Duration cell (fast/normal/slow). No effect on test execution
  itself.
- **`environmentVariables`**: a flat `Record<string, string>` (not an array, not nested
  key/value pairs) — every key becomes both a typed `Spectra.env.KEY` entry (generated into
  `.testspectra/types/env.d.ts`, autocompleted, zero-import — **prefer this over `process.env`**,
  which is untyped `string | undefined`) and a plain `process.env.KEY` string for code that must
  consume the untyped standard API.

---

## 6. Core `spectra` CLI Commands

| Command                                              | Purpose                                                                                                 |
| :--------------------------------------------------- | :------------------------------------------------------------------------------------------------------ |
| `spectra init [--template nx]`                       | Scaffold a new workspace                                                                                |
| `spectra sync-types`                                 | Regenerate `.testspectra/types` and `.testspectra/tsconfig` (also runs on `postinstall` and file-watch) |
| `spectra run [path] -t <web\|mobile\|android\|ios>`  | Execute tests                                                                                           |
| `spectra lint [path] [--strict] [--json]`            | Validate `spec.md`/`suite.md` schema + code parity (see the `spec-and-suite-authoring` skill)           |
| `spectra doctor`                                     | Preflight dependency/environment health check                                                           |
| `spectra refactor step\|action\|fixture <old> <new>` | Atomically rename across folder, metadata, and all call sites                                           |
| `spectra watch`                                      | Background file watcher driving `sync-types`                                                            |

After scaffolding or renaming any file under `page-objects/`, `support/`, or `fixtures/`, assume
the ambient types are stale until `sync-types` (or the watcher) has run — don't hand-write
`.testspectra/types/*.d.ts` yourself.
