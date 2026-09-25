class PlaygroundPage {
  get visibleElement() { return Spectra.get("~playground-visible"); }
  get hiddenElement() { return Spectra.get("~playground-hidden"); }
  get existingElement() { return Spectra.get("~playground-existing"); }
  get removedElement() { return Spectra.get("~playground-removable"); }
  get enabledButton() { return Spectra.get("~enabled-button"); }
  get disabledButton() { return Spectra.get("~pg-disabled-button"); }
  get termsCheckbox() { return Spectra.get("~pg-terms-checkbox"); }
  get modeRadio() { return Spectra.get("~pg-mode-radio"); }
  get emailInput() { return Spectra.get("~pg-email-input"); }
  get tokenInput() { return Spectra.get("~pg-token-input"); }
  get exactText() { return Spectra.get("~exact-text-el"); }
  get partialText() { return Spectra.get("~partial-text-el"); }
  get activeTab() { return Spectra.get("~active-tab-el"); }
  get navLink() { return Spectra.get("~nav-link-el"); }
  get styledElement() { return Spectra.get("~playground-styled-element"); }
  get focusInput() { return Spectra.get("~playground-focus-input"); }
  get productItems() { return Spectra.getAll("~product-item-1, ~product-item-2, ~product-item-3, ~product-item-4"); }
  get emptyList() { return Spectra.getAll("~empty-list-el-item"); }

  async open() {
    try {
      // If a previous test or deep link left the app on a sub-screen, return to home first
      const hasBackBtn = await Spectra.get("~back-to-home-btn").isDisplayed().catch(() => false);
      if (hasBackBtn) {
        await Spectra.get("~back-to-home-btn").click();
      }

      // See MatchersPage.open()'s equivalent comment: waits for the cold-start home screen, then
      // for the drawer Modal to actually finish materializing before clicking a nav item inside
      // it — both races that otherwise surface as an occasional ~10s stall on the next click.
      await Spectra.get("~toggle-sidebar-btn").waitForElement(30000);

      const isDrawerOpen = await Spectra.get("~close-sidebar-btn").isDisplayed().catch(() => false);
      if (!isDrawerOpen) {
        await Spectra.get("~toggle-sidebar-btn").click();
        await Spectra.get("~close-sidebar-btn").waitForElement(10000);
      }
      await Spectra.get("~nav-item-playground").click();
    } catch {}
  }
  async fillCredentials(email = Fixture.playgroundData.defaultEmail, token = Fixture.playgroundData.defaultToken) {
    await this.emailInput.type(email);
    await this.tokenInput.type(token);
  }
}

export default new PlaygroundPage();
