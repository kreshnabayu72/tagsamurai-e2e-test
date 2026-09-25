---
name: lifecycle-hooks
description: TestSpectra lifecycle hooks — global-hooks/ (batch-run only) vs specs/<suite>/hooks/ (before, beforeEach, afterEach, after), their execution order in single-test vs global-batch runs, and the failure-cascade rules. Use whenever adding setup/teardown logic instead of duplicating it inside individual test cases.
---

# Skill: Suite & Global Lifecycle Hooks

Use this skill whenever you need setup/teardown logic (auth, DB seeding, cookie clearing, failure
screenshots) that shouldn't be duplicated inside every `it()` body.

---

## 1. Two Hook Levels — Know the Difference

| Hook                             | Level  | Scope              | When it runs                                                                                     |
| :------------------------------- | :----- | :----------------- | :----------------------------------------------------------------------------------------------- |
| `global-hooks/before`            | Global | Entire run session | **Once**, before all suites — **Global Batch Run / CI only**, never during single-test debugging |
| `global-hooks/after`             | Global | Entire run session | **Once**, after all suites — Global Batch Run only                                               |
| `specs/<suite>/hooks/before`     | Suite  | Test suite         | Once before the first test case in the suite                                                     |
| `specs/<suite>/hooks/beforeEach` | Suite  | Test case          | Before every test case in the suite                                                              |
| `specs/<suite>/hooks/afterEach`  | Suite  | Test case          | After every test case in the suite                                                               |
| `specs/<suite>/hooks/after`      | Suite  | Test suite         | Once after the last test case in the suite                                                       |

**Global hooks are skipped when running/debugging a single test case** — put anything a single
test genuinely depends on (navigating to `/login`, clearing storage) in a **suite** hook instead,
not a global one, or the test will fail/behave differently when run in isolation.

---

## 2. Directory Layout

```
workspace-root/
├── global-hooks/
│   ├── before/
│   │   ├── web.hook.ts
│   │   └── mobile.hook.ts
│   └── after/
│       ├── web.hook.ts
│       └── mobile.hook.ts
└── specs/
    └── authentication/
        ├── suite.md
        ├── hooks/
        │   ├── before/web.hook.ts
        │   ├── beforeEach/web.hook.ts   # e.g. clear cookies, navigate to /login
        │   ├── afterEach/web.hook.ts    # e.g. failure screenshot, clear storage
        │   └── after/web.hook.ts
        ├── TC-0001-valid-login/
        └── TC-0002-invalid-password/
```

---

## 3. Execution Order

### Single Test Case Run (VS Code CodeLens `▶ Run on <Target>`)

```
suite/hooks/before()
  └─► suite/hooks/beforeEach() ─► it('TC-0001') ─► suite/hooks/afterEach()
suite/hooks/after()
```

Global hooks do **not** run here.

### Global Batch Run (`▶ Global Run` / CI/CD)

```
global-hooks/before()                        (once, whole batch)
  ├─► Suite 1: before() → [beforeEach → TC → afterEach]* → after()
  ├─► Suite 2: before() → [beforeEach → TC → afterEach]* → after()
global-hooks/after()                         (once, whole batch)
```

---

## 4. Implementation: Anonymous Async Default Export

Same convention as steps/actions — one anonymous async function, default export, zero manual
imports:

```typescript
// specs/authentication/hooks/beforeEach/web.hook.ts
export default async function () {
  await Spectra.navigate('/auth/login');
  await Spectra.browser.clearLocalStorage();
  await Spectra.browser.clearCookies();
}
```

```typescript
// global-hooks/before/web.hook.ts
export default async function () {
  const response = await fetch(`${process.env.BASE_URL}/health`);
  if (!response.ok) {
    throw new Error(`Target environment is not healthy: ${response.statusText}`);
  }
}
```

---

## 5. Failure Cascade Rules

1. **`beforeEach` fails** → that test case is marked `failed` (Hook Failure), its `it()` body is
   skipped, but `afterEach` still runs for cleanup.
2. **Suite `before` fails** → every test case in that suite is marked `skipped`/`error`; suite
   `after` still runs to clean up partial resources.
3. **`global-hooks/before` fails** → the entire batch run aborts immediately; `global-hooks/after`
   still runs to finalize cleanup.

Write hook bodies defensively with this cascade in mind — teardown logic in `after`/`afterEach`
must not assume `before`/`beforeEach` fully succeeded.
