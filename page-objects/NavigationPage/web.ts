class NavigationPage {
  get sidebarLinks() { return Spectra.getAll("aside a"); }
  get overviewLink() { return Spectra.get("aside a[href='#overview']"); }
  get visibilityLink() { return Spectra.get("aside a[href='#visibility']"); }
  get playgroundLink() { return Spectra.get("aside a[href='#playground']"); }
}

export default new NavigationPage();
