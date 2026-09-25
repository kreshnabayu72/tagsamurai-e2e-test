class PlaygroundPage {
  get visibleElement() { return Spectra.get("#demo-visible-el-pg"); }
  get hiddenElement() { return Spectra.get("#demo-hidden-el-pg"); }
  get existingElement() { return Spectra.get("#demo-existing-el-pg"); }
  get removedElement() { return Spectra.get("#demo-removed-el-pg"); }
  get enabledButton() { return Spectra.get("#demo-enabled-btn"); }
  get disabledButton() { return Spectra.get("#demo-disabled-btn-pg"); }
  get termsCheckbox() { return Spectra.get("#demo-terms-checkbox"); }
  get modeRadio() { return Spectra.get("#demo-mode-radio"); }
  get emailInput() { return Spectra.get("#demo-email-input-pg"); }
  get tokenInput() { return Spectra.get("#demo-token-input-pg"); }
  get exactText() { return Spectra.get("#demo-exact-text-pg"); }
  get partialText() { return Spectra.get("#demo-partial-text-pg"); }
  get activeTab() { return Spectra.get("#demo-active-tab-pg"); }
  get navLink() { return Spectra.get("#demo-nav-link-pg"); }
  get styledElement() { return Spectra.get("#demo-styled-el-pg"); }
  get focusInput() { return Spectra.get("#demo-focus-input-pg"); }
  get productItems() { return Spectra.getAll(".demo-product-item"); }
  get emptyList() { return Spectra.getAll("#demo-empty-list-pg > *"); }
  get fileInput() { return Spectra.get("#demo-file-input-pg"); }
  get uploadedFilename() { return Spectra.get("#demo-uploaded-filename"); }

  async open() {
    await Spectra.navigate("/#playground");
  }

  async fillCredentials(email = Fixture.playgroundData.defaultEmail, token = Fixture.playgroundData.defaultToken) {
    await this.emailInput.type(email);
    await this.tokenInput.type(token);
  }
}

export default new PlaygroundPage();
