---
name: spec-and-suite-authoring
description: How to write suite.md, spec.md, and the paired *.test.ts execution script for a TestSpectra test case — frontmatter schema, the @step directive convention, and every spec-schema-linter rule that must pass (single it(), no describe/test, zero-import, title parity). Use whenever creating or editing a test case.
---

# Skill: Spec & Suite Authoring (`spec.md`, `suite.md`, `*.test.ts`)

Use this skill whenever you create a new test case, add a new suite, or edit an existing
`spec.md` / `*.test.ts` pair. TestSpectra treats the Markdown spec as the human-readable source of
truth and the TypeScript file as its execution — the CLI linter (`spectra lint`) enforces that the
two never drift apart.

---

## 1. Directory Convention

```
specs/<SuiteName>/suite.md
specs/<SuiteName>/hooks/{before,beforeEach,afterEach,after}/web.hook.ts
specs/<SuiteName>/TC-<NNNN>-<kebab-slug>/spec.md
specs/<SuiteName>/TC-<NNNN>-<kebab-slug>/web.test.ts   # + android/ios/mobile/common variants
```

`SuiteName` is a directory (no `describe()` block ever exists in code — the suite boundary is
purely the folder). The test case id (`TC-0001-valid-login`) is both the directory name and the
`id` in `spec.md`'s frontmatter, and must be unique across the entire workspace
(`testspectra/duplicate-spec-id`).

---

## 2. `suite.md` Frontmatter

```markdown
---
name: Untitled Suite
id: suite-element-matchers
description: Element visibility, existence, form states and attributes
executionOrder: 1.0
parallel: true
---

# Suite: ElementMatchers
```

---

## 3. `spec.md` Frontmatter & Body

```markdown
---
id: TC-0003-visibility-and-dom
title: Verify element visibility and existence matchers
priority: High
caseType: Positive
status: ready-for-automation
coverage:
  web: automated
  mobile: automated
---

# Verify element visibility and existence matchers

## Test Steps

1. Open visibility section in matchers page
2. Assert visible element has be.visible state
3. Assert existing element exists in DOM
```

Required frontmatter: `id`, `title`, `priority`, `caseType`, `status` — missing any of these, or
missing the `# <Title>` / `## Test Steps` headings, triggers `testspectra/missing-frontmatter`.
Invalid enum values (an unrecognized `priority`, `caseType`, or `status`) trigger
`testspectra/invalid-frontmatter-enum`.

If the test case invokes a shared step (see the `shared-steps-and-actions` skill), reference it in
the `## Test Steps` list as `@step:<stepName>` — the linter cross-checks this against
`Step.<stepName>()` calls in the paired `*.test.ts`.

---

## 4. The Paired Test Script (`web.test.ts`)

```typescript
it('Verify element visibility and existence matchers', async () => {
  await MatchersPage.open('visibility');

  await MatchersPage.visibleElement.shouldBeVisible();
  await MatchersPage.hiddenElement.shouldNotBeVisible();

  await MatchersPage.existingElement.shouldExist();
  await Spectra.get('#demo-non-existent-el').shouldNotExist();
});
```

### Hard rules (each is a `spectra lint` error unless noted):

1. **Exactly one `it(...)` block, nothing else at the top level.** Zero or multiple `it()` blocks
   → `testspectra/single-it-required`.
2. **Never `test(...)`.** Only `it(...)` is allowed → `testspectra/no-test-block`.
3. **Never `describe(...)`.** Suite grouping is the directory, not code →
   `testspectra/no-describe-block`.
4. **Zero manual `import`s.** See the `workspace-structure` skill →
   `testspectra/no-manual-import`.
5. **`it()`'s title should read the same as `spec.md`'s `title`** (case-insensitive semantic
   match). A mismatch is a warning, not an error → `testspectra/title-mismatch`.
6. **Every `@step:<name>` in `spec.md` must have a matching `Step.<name>()` call** in the test
   script → `testspectra/missing-step-call` (error) if absent, and conversely a `Step.<name>()`
   call not documented with `@step:<name>` in `spec.md` is
   `testspectra/undocumented-step` (warning).

### Platform variants

A test case directory may contain any combination of `web.test.ts`, `android.test.ts`,
`ios.test.ts`, `mobile.test.ts`, `common.test.ts` — each is linted and can be run independently.
Reuse a shared step for the parts of the flow that are identical across platforms rather than
duplicating the `it()` body per platform.

---

## 5. Running the Linter

- `spectra lint` — scan the whole workspace, human-readable output.
- `spectra lint --strict` — treat warnings as errors, exit code `1` on any diagnostic (use this in
  CI).
- `spectra lint --json` — machine-readable diagnostics (what an AI agent should parse to
  self-correct after generating a spec).
- `spectra lint <path>` — scan a single suite or test case folder.

Exit codes: `0` valid, `1` violations found, `2` fatal (malformed YAML/JSON).

After authoring or editing a `spec.md`/`*.test.ts` pair, run `spectra lint <path-to-that-case>`
before considering the task done.
