it("Verify page title and sidebar navigation links", async () => {
  await MatchersPage.open();

  // Browser title assertions
  await Spectra.browser.shouldHaveTitle("TestSpectra — Matchers API Reference");
  await Spectra.browser.shouldContainTitle("TestSpectra");

  // Browser URL assertions
  const currentUrl = await browser.getUrl();
  await Spectra.browser.shouldHaveUrl(currentUrl);
  await Spectra.browser.shouldContainUrl("localhost");

  // Page lifecycle and console error diagnostics
  await Spectra.browser.shouldBeLoaded();
  await Spectra.browser.shouldHaveNoConsoleErrors();

  // Navigation sidebar collection verification
  await NavigationPage.sidebarLinks.shouldHaveLengthGreaterThan(0);
});
