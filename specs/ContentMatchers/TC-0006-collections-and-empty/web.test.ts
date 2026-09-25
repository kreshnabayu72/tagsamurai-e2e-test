it("Verify collection lengths, counts, and empty lists", async () => {
  await MatchersPage.open("length");

  // Receiver assertion methods
  await MatchersPage.productCards.shouldHaveLength(4);
  await MatchersPage.productCards.shouldNotHaveLength(0);
  await MatchersPage.productCards.shouldHaveLengthGreaterThan(0);
  await MatchersPage.productCards.shouldHaveLengthLessThan(10);
  await MatchersPage.emptyList.shouldBeEmpty();
  await MatchersPage.productCards.shouldNotBeEmpty();
});
