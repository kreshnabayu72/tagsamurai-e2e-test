it("element.get()/getAll() resolves a child scoped to its parent's own subtree", async () => {
  await MatchersPage.open();
  await MatchersPage.overviewSection.shouldBeVisible();

  // Positive: the subtitle is a real descendant of the overview section, so the scoped lookup
  // resolves it.
  await MatchersPage.overviewSubtitle().shouldExist();

  // Negative (the actual scoping proof): the submit button lives in a different section
  // entirely. If .get() weren't genuinely scoped (e.g. silently fell back to a page-wide
  // lookup), this would incorrectly resolve to the globally-existing element instead of
  // correctly not finding it.
  await MatchersPage.overviewOutsideElement().shouldNotExist();
});
