class MatchersPage {
  get visibleElement() { return Spectra.get("#demo-visible-el"); }
  get hiddenElement() { return Spectra.get("#demo-hidden-el"); }
  get existingElement() { return Spectra.get("#demo-existing-el"); }
  get submitButton() { return Spectra.get("#demo-submit-btn"); }
  get disabledButton() { return Spectra.get("#demo-disabled-btn"); }
  get checkbox() { return Spectra.get("#demo-checkbox"); }
  get radio() { return Spectra.get("#demo-radio"); }
  get emailInput() { return Spectra.get("#demo-email-input"); }
  get tokenInput() { return Spectra.get("#demo-token-input"); }
  get exactText() { return Spectra.get("#demo-exact-text"); }
  get partialText() { return Spectra.get("#demo-partial-text"); }
  get activeTab() { return Spectra.get("#demo-active-tab"); }
  get navLink() { return Spectra.get("#demo-nav-link"); }
  get styledElement() { return Spectra.get("#demo-styled-el"); }
  get focusInput() { return Spectra.get("#demo-focus-input"); }
  get productCards() { return Spectra.getAll(".demo-product-card"); }
  get emptyList() { return Spectra.getAll("#demo-empty-list > *"); }
  get overviewSection() { return Spectra.get("#overview"); }
  // Scoped lookups via element.get() — resolved within overview-section's own subtree, not
  // document-wide.
  overviewSubtitle() { return this.overviewSection.get("#demo-page-subtitle"); }
  overviewOutsideElement() { return this.overviewSection.get("#demo-submit-btn"); }

  // API Interception & Mocking elements
  get fetchApiButton() { return Spectra.get("#fetch-api-btn"); }
  get fetchStatusBadge() { return Spectra.get("#fetch-status-badge"); }
  get fetchedItems() { return Spectra.getAll(".api-fetched-item"); }
  get fetchLoadingIndicator() { return Spectra.get("#fetch-loading-indicator"); }
  get fetchCustomUrlInput() { return Spectra.get("#fetch-custom-url-input"); }
  get postTitleInput() { return Spectra.get("#post-input-title"); }
  get postBodyInput() { return Spectra.get("#post-input-body"); }
  get submitPostButton() { return Spectra.get("#submit-post-btn"); }
  get postStatusBadge() { return Spectra.get("#post-status-badge"); }
  get postSuccessBanner() { return Spectra.get("#post-success-banner"); }
  get postResponseJson() { return Spectra.get("#post-response-json"); }

  async open(section = "") {
    await Spectra.navigate("/" + (section ? "#" + section : ""));
  }
}

export default new MatchersPage();
