it("Verify element visibility and existence matchers", async () => {
  await MatchersPage.open("visibility");

  // Element visibility (positive and negative)
  await MatchersPage.visibleElement.shouldBeVisible();
  await MatchersPage.hiddenElement.shouldNotBeVisible();

  // DOM existence (positive and negative)
  await MatchersPage.existingElement.shouldExist();
  await Spectra.get("#demo-non-existent-el").shouldNotExist();
});
