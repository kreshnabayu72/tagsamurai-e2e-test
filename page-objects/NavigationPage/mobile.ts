class NavigationPage {
  get sidebarLinks() {
    return Spectra.getAll(
      "~nav-item-overview, ~nav-item-element-matchers, ~nav-item-visibility, ~nav-item-existence, ~nav-item-state, ~nav-item-value, ~nav-item-text, ~nav-item-class-attr, ~nav-item-browser-matchers, ~nav-item-url, ~nav-item-title, ~nav-item-collection-matchers, ~nav-item-length, ~nav-item-api-matchers, ~nav-item-api-fetch, ~nav-item-api-post, ~nav-item-playground"
    );
  }
  get toggleSidebarButton() { return Spectra.get("~toggle-sidebar-btn"); }
  get closeSidebarButton() { return Spectra.get("~close-sidebar-btn"); }
  get overviewLink() { return Spectra.get("~nav-item-overview"); }
  get visibilityLink() { return Spectra.get("~nav-item-visibility"); }
  get playgroundLink() { return Spectra.get("~nav-item-playground"); }
}

export default new NavigationPage();
