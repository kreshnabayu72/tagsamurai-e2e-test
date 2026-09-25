---
name: matchers-and-assertions
description: Full reference of the TestSpectra element action/assertion API (shouldBeVisible, click, type...), collection matchers (shouldHaveLength...), and global Spectra.* / Spectra.browser.* commands. Use whenever writing or reviewing the body of an it() test script, step, or action.
---

# Skill: Matchers, Actions & the Global `Spectra` API

Use this skill as the canonical vocabulary reference whenever you write the body of a test script
(`it()`), a shared step, or a custom action. TestSpectra never uses raw WebdriverIO/Jest matcher
names (`toBeDisplayed`, `setValue`, `$`) in authored code — always use the TestSpectra syntax below.
Every call is automatically traced (`trackCommand()`) and emitted as one natural-English log line
per action/assertion in `.testspectra/reports/`.

---

## 1. Element Action Commands (called on a Page Object getter)

| TestSpectra syntax                   | Semantic log output                     |
| :----------------------------------- | :-------------------------------------- |
| `await el.click()`                   | `Click on element "{el}"`               |
| `await el.doubleClick()`             | `Double-click on {el}`                  |
| `await el.rightClick()`              | `Right-click on {el}`                   |
| `await el.type(text, options?)`      | `Type "{text}" into element "{el}"`     |
| `await el.clear()`                   | `Clear text in {el}`                    |
| `await el.select(option)`            | `Select option "{option}" in {el}`      |
| `await el.hover()`                   | `Hover over {el}`                       |
| `await source.dragDrop(dest)`        | `Drag {source} and drop onto {dest}`    |
| `await el.scrollIntoView()`          | `Scroll {el} into view`                 |
| `await el.longPress(durationMs)`     | `Long-press on {el} for {durationMs}ms` |
| `await el.waitForElement(timeoutMs)` | `Wait for {el} to be displayed`         |

`type()` accepts an options object, e.g. `{ clearFirst: true }` to clear the field before typing.

---

## 2. Element Assertions (called on a Page Object getter)

| TestSpectra syntax                        | Semantic log output                                      |
| :---------------------------------------- | :------------------------------------------------------- |
| `await el.shouldBeVisible()`              | `Expect element "{el}" to be visible`                    |
| `await el.shouldNotBeVisible()`           | `Expect element "{el}" not to be visible`                |
| `await el.shouldExist()`                  | `Expect element "{el}" to exist in DOM`                  |
| `await el.shouldNotExist()`               | `Expect element "{el}" not to exist in DOM`              |
| `await el.shouldBeClickable()`            | `Expect element "{el}" to be clickable`                  |
| `await el.shouldNotBeClickable()`         | `Expect element "{el}" not to be clickable`              |
| `await el.shouldBeEnabled()`              | `Expect element "{el}" to be enabled`                    |
| `await el.shouldBeDisabled()`             | `Expect element "{el}" to be disabled`                   |
| `await el.shouldBeChecked()`              | `Expect element "{el}" to be checked`                    |
| `await el.shouldNotBeChecked()`           | `Expect element "{el}" not to be checked`                |
| `await el.shouldHaveText(text)`           | `Expect element "{el}" to have text "{text}"`            |
| `await el.shouldContainText(substr)`      | `Expect element "{el}" to contain text "{substr}"`       |
| `await el.shouldHaveValue(val)`           | `Expect element "{el}" to have value "{val}"`            |
| `await el.shouldHaveAttribute(attr, val)` | `Expect element "{el}" attribute "{attr}" to be "{val}"` |
| `await el.shouldBeFocused()`              | `Expect element "{el}" to be focused`                    |

Every assertion above (and every collection matcher in section 3) accepts a trailing
`options?: { timeoutMs }` to override the adaptive fail-fast timeout for that one call, without
raising it for every other assertion in the test — use this when a specific assertion is known to
need longer, e.g. right after a deliberately delayed `Spectra.intercept(..., { delayMs })` mock:

```typescript
await ReportPage.statusBadge.shouldHaveText('Ready', { timeoutMs: 5000 });
```

---

## 3. Collection Matchers (on `Spectra.getAll(selector)` getters)

| TestSpectra syntax                           | Semantic log output                                     |
| :------------------------------------------- | :------------------------------------------------------ |
| `await col.shouldHaveLength(n)`              | `Expect collection "{selector}" count to equal {n}`     |
| `await col.shouldNotHaveLength(n)`           | `Expect collection "{selector}" count not to equal {n}` |
| `await col.shouldHaveLengthGreaterThan(min)` | `count to be greater than {min}`                        |
| `await col.shouldHaveLengthLessThan(max)`    | `count to be less than {max}`                           |
| `await col.shouldBeEmpty()`                  | `Expect collection "{selector}" to be empty`            |
| `await col.shouldNotBeEmpty()`               | `Expect collection "{selector}" not to be empty`        |

---

## 4. Scoped Element Lookups: `.get()` / `.getAll()`

Any resolved element also has `.get(childSelector)` / `.getAll(childSelector)`, chaining a lookup
scoped to that element's own subtree — Playwright's `locator.locator()` model. **Prefer this over
a hand-written compound selector** whenever disambiguating repeated markup that shares one
selector across rows (a list of cards, a table's rows):

```typescript
// WRONG: `.buy-btn` is the same selector on every card — this always resolves the first one.
await Spectra.get('.buy-btn').click();

// RIGHT: scoped to the specific card first.
const thirdCard = Spectra.getAll('.product-card').nth(2);
await thirdCard.get('.buy-btn').click();
await thirdCard.getAll('.badge').shouldHaveLength(2);
```

Works identically from a Page Object property, since it's already a resolved element:
`await SettingsPage.modal.get('#save-btn').click()`. `.first()`/`.last()`/`.nth(i)` on a scoped
collection carry the scope forward too. No behavior difference on web vs. Android — resolution
(real DOM query vs. bounds-containment) is handled transparently underneath.

---

## 5. Global `Spectra.*` Commands

| Category       | Syntax                                                                                                                           |
| :------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| Navigation     | `await Spectra.navigate("/login")` / `.back()` / `.forward()` / `.refresh()`                                                     |
| Element query  | `Spectra.get(selector)` / `Spectra.getAll(selector)` — chain `.get()`/`.getAll()` on the result to scope a lookup, see section 4 |
| Window         | `await Spectra.setViewport(1920, 1080)`                                                                                          |
| Timing         | `await Spectra.wait(1000)`                                                                                                       |
| Keyboard       | `await Spectra.pressKey("Enter")`                                                                                                |
| Scroll         | `await Spectra.scroll({ direction: "down", pixels: 400 })`                                                                       |
| Mobile gesture | `await Spectra.swipe({ direction: "left", distance: 300 })`                                                                      |
| Network mock   | `const mock = await Spectra.intercept({ url, method, response })` — see the `network-interception` skill                         |

## 6. `Spectra.browser.*` — Browser/Context Level

| Syntax                                              | Purpose                         |
| :-------------------------------------------------- | :------------------------------ |
| `await Spectra.browser.clearCookies()`              | Clear all cookies               |
| `await Spectra.browser.clearLocalStorage()`         | Clear localStorage              |
| `await Spectra.browser.shouldHaveUrl(url)`          | Assert exact URL                |
| `await Spectra.browser.shouldContainUrl(substr)`    | Assert URL contains substring   |
| `await Spectra.browser.shouldHaveTitle(title)`      | Assert exact document title     |
| `await Spectra.browser.shouldContainTitle(substr)`  | Assert title contains substring |
| `await Spectra.browser.shouldBeLoaded()`            | Assert page fully loaded        |
| `await Spectra.browser.shouldHaveNoConsoleErrors()` | Assert zero console errors      |

---

## 7. Full Example

```typescript
it('should login as administrator and assert dashboard metrics', async () => {
  await Spectra.navigate('/auth/login');
  await Spectra.browser.clearCookies();

  await LoginPage.emailInput.type(Fixture.users.admin.email, { clearFirst: true });
  await LoginPage.passwordInput.type(Fixture.users.admin.password);
  await LoginPage.submitButton.click();

  await DashboardPage.header.shouldBeVisible();
  await DashboardPage.welcomeMsg.shouldHaveText('Welcome back, Admin');
  await DashboardPage.statCards.shouldHaveLength(4);
  await LoginPage.loadingSpinner.shouldNotBeVisible();

  await Spectra.browser.shouldHaveUrl('https://app.testspectra.dev/dashboard');
  await Spectra.browser.shouldHaveNoConsoleErrors();
});
```

This is engine-agnostic: the exact same syntax dispatches to Chrome CDP on `web.test.ts` and to the
native Android TCP driver on `android.test.ts` — never branch authoring code per platform inside a
shared file; instead put platform-specific implementations in the correctly-suffixed file (see the
`workspace-structure` skill).
