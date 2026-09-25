it("Mock and assert GET API requests using browser.intercept", async () => {
  // Navigate to API Fetch section
  await MatchersPage.open("api-fetch");

  // The app fetches the demo server's own self-hosted endpoint (/api/posts) — served by the
  // built-in demo app (started with `--demo`), so no external network is involved. Clear any mock
  // left registered by an earlier test in this same continuous session before adding this one,
  // since rules aren't scoped per-test and the first matching rule wins.
  Spectra.clearMocks();
  const mock = await Spectra.intercept(
    "api/posts",
    "GET",
    Fixture.apiData.mockPosts
  );

  // Trigger fetch button
  await MatchersPage.fetchApiButton.click();

  // Assert status and mocked elements
  await MatchersPage.fetchStatusBadge.shouldHaveText("200 OK");
  await MatchersPage.fetchedItems.shouldHaveLength(Fixture.apiData.mockPosts.length);
  await MatchersPage.fetchedItems.first().shouldContainText(Fixture.apiData.mockPosts[0].title);

  // Dynamically update fixture response
  await mock.respondWith([
    { id: 99, title: "Dynamic Updated Mock Title", body: "Updated on the fly" }
  ]);
  await MatchersPage.fetchApiButton.click();
  await MatchersPage.fetchedItems.shouldHaveLength(1);
  await MatchersPage.fetchedItems.first().shouldContainText("Dynamic Updated Mock Title");
});
