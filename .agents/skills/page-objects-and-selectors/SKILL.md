---
name: page-objects-and-selectors
description: How to write a TestSpectra Page Object (Spectra.get / Spectra.getAll singleton pattern) and how the ~accessibility-id vs #native-id selector contract resolves identically across Web, Android, and iOS. Use whenever declaring element locators or a new Page Object.
---

# Skill: Page Objects & the Selector Contract

Use this skill whenever you add a new Page Object, add a getter to an existing one, or need to
pick a selector string.

---

## 1. Page Object Pattern

A Page Object is a class with getter properties that return `Spectra.get(selector)` /
`Spectra.getAll(selector)`, exported as a singleton default export, and consumed with **zero
imports** anywhere else in the workspace (see the `workspace-structure` skill).

```typescript
// page-objects/MatchersPage/web.ts
class MatchersPage {
  get visibleElement() {
    return Spectra.get('#demo-visible-el');
  }
  get hiddenElement() {
    return Spectra.get('#demo-hidden-el');
  }
  get existingElement() {
    return Spectra.get('#demo-existing-el');
  }
  get productCards() {
    return Spectra.getAll('.demo-product-card');
  } // collection

  async open(section = '') {
    await Spectra.navigate('/' + (section ? '#' + section : ''));
  }
}

export default new MatchersPage();
```

Rules:

- One getter per element/collection; name the getter for what the element _is_ (`submitButton`,
  `statCards`), not for the selector string.
- `Spectra.get(selector)` → single element; `Spectra.getAll(selector)` → collection (used with
  collection matchers like `.shouldHaveLength(n)`).
- Add reusable navigation/composite helpers as regular `async` methods on the same class (e.g.
  `open()` above), not as standalone actions, when they are specific to that one page.
- File suffix follows the platform-suffix rule: `web.ts` for CSS selectors, `mobile.ts` /
  `android.ts` / `ios.ts` for native selectors targeting the same logical page.

---

## 2. Selector Contract: `~name` vs `#name`

TestSpectra resolves selectors identically across every platform — a selector written once means
the same thing everywhere. Each prefix maps to **exactly one** attribute; there is no silent
cross-matching.

| Selector           | Meaning              | Web                     | Android                          | iOS                      |
| :----------------- | :------------------- | :---------------------- | :------------------------------- | :----------------------- |
| `~name`            | **accessibility id** | `[aria-label="name"]`   | `content-desc`                   | accessibility identifier |
| `#name`            | **native id**        | CSS `#name`             | `resource-id`                    | — (n/a)                  |
| `//xpath`          | raw XPath            | delegated to the driver | delegated to the on-device agent | n/a                      |
| `name` (no prefix) | lenient fallback     | n/a                     | native id, then accessibility id | n/a                      |

### Which one to use

- **Prefer `~name`** for anything a user can perceive — it's the portable, semantic, recommended
  default across all platforms.
- **Use `#name`** only when the element has a stable test/native id and no accessibility label
  (React Native `testID`, Android `resource-id`, CSS `id`).
- Set the _matching_ attribute on the app/page element so the selector actually resolves:

```tsx
// React Native — these resolve DIFFERENT selectors:
<Pressable accessibilityLabel="submit-button" />   // → Spectra.get('~submit-button')
<Pressable testID="submit-button" />                // → Spectra.get('#submit-button')
```

```html
<!-- Web -->
<button aria-label="submit-button">…</button>
<!-- → Spectra.get('~submit-button') -->
<button id="submit-button">…</button>
<!-- → Spectra.get('#submit-button') -->
```

- When `testID` and `accessibilityLabel` are set to the same value, `~name` and `#name` are
  interchangeable; they diverge the moment the two attributes differ.
- Avoid the unprefixed lenient form (`name`) in new tests — it's Android-only leniency kept for
  backwards compatibility, not part of the cross-platform contract. Always write an explicit `~`
  or `#`.
- Avoid raw `//xpath` unless there is genuinely no stable id/label to hook into — it's brittle and
  bypasses the fast, cached full-hierarchy snapshot lookup that `~`/`#` selectors use on Android.

---

## 3. Scoping a Lookup Instead of Writing a Compound Selector

When the same selector repeats across rows (a list of cards, a table), **do not** reach for a
compound CSS selector (`.card:nth-child(3) .buy-btn`) or an index baked into an xpath — those are
brittle and don't have a cross-platform equivalent (Android has no CSS nth-child). Chain
`.get(childSelector)` / `.getAll(childSelector)` off an already-resolved element instead; it
scopes the lookup to that element's own subtree:

```typescript
class ProductsPage {
  get cards() {
    return Spectra.getAll('.product-card');
  }
  cardBuyButton(index: number) {
    return this.cards.nth(index).get('.buy-btn');
  }
}
```

This is a Page Object concern, not a new selector prefix — `~`/`#`/xpath all still apply as the
child selector, resolved within the parent's subtree instead of the whole document/screen. See the
`matchers-and-assertions` skill for the full `.get()`/`.getAll()` chaining behavior.

---

## 4. Never Use Raw `$` / `$$` / `browser` / `driver`

TestSpectra encapsulates the entire runtime into a single global `Spectra` object. There is no raw
WebdriverIO `$`, `$$`, `browser`, or `driver` in test-authoring code — always go through
`Spectra.get()` / `Spectra.getAll()` for locators and `Spectra.*` / `Spectra.browser.*` for
everything else (navigation, gestures, storage, network). See the `matchers-and-assertions` skill
for the full command surface.
