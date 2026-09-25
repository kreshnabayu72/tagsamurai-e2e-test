---
name: shared-steps-and-actions
description: The difference between TestSpectra Shared Steps (Step.*, high-level business workflows, documented in spec.md via @step) and Spectra Actions (support/actions, low-level technical utilities) — directory layout, the mandatory anonymous async default export convention, and ambient type generation. Use whenever extracting reusable logic out of a test script.
---

# Skill: Shared Steps vs. Custom Actions

Use this skill when you're about to extract repeated logic (e.g. login, checkout) out of test
scripts, or when deciding whether new reusable logic belongs under `support/steps/` or
`support/actions/`.

---

## 1. Which One Do I Need?

| Attribute         | Shared Steps (`Step.*`)                        | Custom Actions (`Spectra.*` / on-element helpers)                             |
| :---------------- | :--------------------------------------------- | :---------------------------------------------------------------------------- |
| Abstraction level | High-level business workflow (login, checkout) | Low-level technical utility                                                   |
| Directory         | `support/steps/<stepName>/`                    | `support/actions/<actionName>/`                                               |
| Spec mapping      | Documented as `@step:<name>` in `spec.md`      | Just called inline, not listed in spec steps                                  |
| Metadata file     | `step.md` (YAML frontmatter + description)     | None — implementation file only                                               |
| Files             | `step.md` + `web.step.ts` [+ `mobile.step.ts`] | `web.action.ts` [+ `mobile.action.ts`]                                        |
| Invocation        | `await Step.loginAsAdmin(params)`              | Called as a helper bound to an element/page, e.g. inside a Page Object method |

Rule of thumb: if it's a multi-step _business_ flow a human would describe in one sentence
("log in as admin"), it's a **Step**. If it's a small technical helper reused across Page Objects
(a resilient click retry, filling a pair of fields), it's an **Action**.

---

## 2. Directory Layout

```
support/
├── steps/
│   └── loginAsAdmin/
│       ├── step.md            # Metadata, docs, parameter types
│       ├── web.step.ts
│       └── mobile.step.ts     # optional
└── actions/
    └── fillCredentials/
        ├── web.action.ts
        └── mobile.action.ts
```

Both use **camelCase** directory/function names (`loginAsAdmin`, `fillCredentials`,
`applyDiscount`, `verifyOtp`) — never kebab-case or snake_case.

---

## 3. `step.md` Metadata

```markdown
---
id: step-login-as-admin
name: loginAsAdmin
description: Authenticates as an administrator and asserts landing dashboard
platform:
  - web
  - mobile
tags:
  - auth
  - admin
parameters:
  - name: email
    type: string
    required: false
    description: Admin email address (defaults to Fixture.users.admin.email)
  - name: password
    type: string
    required: false
    description: Admin password (defaults to Fixture.users.admin.password)
---

# Login as Admin Step

## Purpose

Provides a standard, hardened administrative login sequence for web and mobile platforms.

## Prerequisites

- User fixture file exists at `fixtures/users.json`.
- Browser is navigated to the base URL or login route.
```

---

## 4. Implementation: Anonymous Async Default Export (Mandatory)

Every `*.step.ts` and `*.action.ts` file exports **one anonymous async function as its default
export** — no named exports, no `test()`/`it()` blocks. This is enforced by the linter
(`testspectra/require-anonymous-default-export`).

```typescript
// support/steps/loginAsAdmin/web.step.ts
export default async function (params?: { email?: string; password?: string }) {
  const email = params?.email ?? Fixture.users.admin.email;
  const password = params?.password ?? Fixture.users.admin.password;

  await Spectra.navigate('/auth/login');
  await LoginPage.emailInput.type(email, { clearFirst: true });
  await LoginPage.passwordInput.type(password);
  await LoginPage.submitButton.click();

  await DashboardPage.header.shouldBeVisible();
}
```

Custom Actions follow the same shape and are commonly written with a `this` receiver so they can
be attached/bound as element/page helpers:

```typescript
// support/actions/fillCredentials/web.action.ts
export default async function (this: any, email: string, token: string) {
  await this.get('#demo-email-input-pg').type(email);
  await this.get('#demo-token-input-pg').type(token);
}
```

```typescript
// support/actions/fillCredentials/mobile.action.ts
export default async function (this: any, email: string, token: string) {
  await this.get('~pg-email-input').type(email);
  await this.get('~pg-token-input').type(token);
}
```

Zero-import applies here too: never manually `import` a Page Object, `Fixture`, or `Spectra` — see
the `workspace-structure` skill.

---

## 5. Type Generation & Invocation

The `TypeGenerator` scans `support/steps/` and emits the `Step` ambient namespace automatically:

```typescript
declare global {
  namespace Step {
    function loginAsAdmin(params?: { email?: string; password?: string }): Promise<void>;
  }
}
```

### In `spec.md` (documents the step as part of the human-readable flow):

```markdown
## Test Steps

1. @step:loginAsAdmin
2. Navigate to user settings page
3. Update profile avatar
```

### In `web.test.ts` (invokes it with zero manual imports):

```typescript
it('should update admin profile avatar', async () => {
  await Step.loginAsAdmin();

  await SettingsPage.openProfile();
  await SettingsPage.avatarInput.type('avatar.png');
  await SettingsPage.successToast.shouldBeVisible();
});
```

Every `@step:<name>` in `spec.md` must have a matching `Step.<name>()` call in the paired test
script, or `spectra lint` reports `testspectra/missing-step-call`. See the
`spec-and-suite-authoring` skill for the full linter rule matrix.

---

## 6. Renaming a Step or Action

Never rename a step/action folder by hand. Use:

```
spectra refactor step loginAsAdmin authenticateAdmin
```

This atomically: renames `support/steps/loginAsAdmin/` → `support/steps/authenticateAdmin/`,
updates `name:` in `step.md`, rewrites every `@step:loginAsAdmin` in every `spec.md`, rewrites
every `Step.loginAsAdmin()` call site, and regenerates `.testspectra/types/steps.d.ts`.
