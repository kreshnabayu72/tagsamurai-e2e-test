it("Verify page title and sidebar navigation links", async () => {
  await MatchersPage.open();

  // Open sidebar drawer to view navigation links
  await NavigationPage.toggleSidebarButton.click();

  // Navigation sidebar collection verification
  await NavigationPage.sidebarLinks.shouldHaveLengthGreaterThan(0);

  // Close sidebar drawer
  await NavigationPage.closeSidebarButton.click();
});
