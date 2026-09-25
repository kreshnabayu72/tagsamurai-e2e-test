class MatchersPage {
  get visibleElement() { return Spectra.get("~visible-element"); }
  get hiddenElement() { return Spectra.get("~hidden-element"); }
  get existingElement() { return Spectra.get("~existing-element"); }
  get removableElement() { return Spectra.get("~removable-element"); }
  get submitButton() { return Spectra.get("~submit-button"); }
  get disabledButton() { return Spectra.get("~disabled-button"); }
  get checkbox() { return Spectra.get("~terms-checkbox"); }
  get radio() { return Spectra.get("~mode-radio"); }
  get emailInput() { return Spectra.get("~email-input"); }
  get tokenInput() { return Spectra.get("~token-input"); }
  get exactText() { return Spectra.get("~exact-text"); }
  get partialText() { return Spectra.get("~partial-text"); }
  // `#` = native id (RN testID → resource-id). Its accessibility label deliberately reads
  // "active-tab is-active" (RN exposes no CSS classes, so the class is carried in the a11y label
  // for `shouldHaveClass`), so it isn't addressable by the a11y-id form `~active-tab`.
  get activeTab() { return Spectra.get("#active-tab"); }
  get navLink() { return Spectra.get("~nav-link"); }
  get styledElement() { return Spectra.get("~styled-element"); }
  get focusInput() { return Spectra.get("~focus-input"); }
  get productCards() { return Spectra.getAll("~product-item-1, ~product-item-2, ~product-item-3, ~product-item-4"); }
  get emptyList() { return Spectra.getAll("~empty-list-item"); }
  get overviewSection() { return Spectra.get("#overview-section"); }
  // Scoped lookups via element.get() — resolved within overview-section's own bounds (Android
  // has no ancestor API, so this is a bounds-containment lookup), not screen-wide.
  overviewSubtitle() { return this.overviewSection.get("#demo-page-subtitle"); }
  overviewOutsideElement() { return this.overviewSection.get("~submit-button"); }

  // API Demo elements
  get fetchApiButton() { return Spectra.get("~fetch-api-btn"); }
  get fetchStatusBadge() { return Spectra.get("~fetch-status-badge"); }
  get fetchedItems() { return Spectra.getAll("~api-post-item"); }
  get fetchLoadingIndicator() { return Spectra.get("~fetch-loading-indicator"); }
  get fetchCustomUrlInput() { return Spectra.get("~fetch-custom-url"); }
  get postTitleInput() { return Spectra.get("~post-title-input"); }
  get postBodyInput() { return Spectra.get("~post-body-input"); }
  get submitPostButton() { return Spectra.get("~submit-post-btn"); }
  get postStatusBadge() { return Spectra.get("~post-status-badge"); }
  get postSuccessBanner() { return Spectra.get("~post-success-banner"); }
  get postResponseJson() { return Spectra.get("~post-response-json"); }

  async open(section = "") {
    try {
      // If a previous test or deep link left the app on a sub-screen, return to home first
      const hasBackBtn = await Spectra.get("~back-to-home-btn").isDisplayed().catch(() => false);
      if (hasBackBtn) {
        await Spectra.get("~back-to-home-btn").click();
      }

      // A fresh app process (relaunched by the orchestrator's bootstrap before every suite) has to
      // fetch, parse, and execute the RN JS bundle from Metro before anything is on screen — on a
      // cold start this can take well past a normal action's poll budget. Wait for the home screen
      // itself first so that timing doesn't silently swallow the sidebar click below and leave the
      // real failure to surface confusingly on whatever element the test touches next.
      await Spectra.get("~toggle-sidebar-btn").waitForElement(30000);

      const target = section || "overview";
      const isDrawerOpen = await Spectra.get("~close-sidebar-btn").isDisplayed().catch(() => false);
      if (!isDrawerOpen) {
        await Spectra.get("~toggle-sidebar-btn").click();
        // The mobile drawer is a React Native `<Modal>` — a separate OS-level window with its own
        // slide-in animation, not a plain re-rendered View — so its content (including every
        // nav-item below) isn't in the accessibility tree at all until Android actually finishes
        // creating that window, which is async and occasionally slow under load. Without this
        // wait, clicking a nav item right after the toggle relies entirely on click()'s own
        // poll-retry to bridge that gap, which can eat most of the ~10s implicit-wait budget when
        // the Modal is slow to materialize.
        await Spectra.get("~close-sidebar-btn").waitForElement(10000);
      }
      await Spectra.get(`~nav-item-${target}`).click();
    } catch {}
  }
}

export default new MatchersPage();
