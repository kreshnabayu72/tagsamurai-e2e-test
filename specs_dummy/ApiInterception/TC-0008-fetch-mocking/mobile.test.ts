it("Mock and assert GET API requests using browser.intercept", async () => {
  // Navigate to API Fetch section
  await MatchersPage.open("api-fetch");

  // The app fetches the host demo server's self-hosted endpoint (http://localhost:5200/api/posts) —
  // the device's global HTTP proxy (set up transparently at bootstrap) routes it through the
  // worker's mock proxy without the app knowing or needing any special host/prefix, the same
  // way the CDP web driver intercepts traffic for free. Clear any mock left registered by an
  // earlier test in this same continuous session before adding this one.
  Spectra.clearMocks();
  const mock = await Spectra.intercept(
    "api/posts",
    "GET",
    Fixture.apiData.mockPosts
  );

  // Trigger fetch button in mobile demo app
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

  // Reset to the base mock and queue a single one-time response — asserts a transient state
  // (e.g. one retry attempt) without disturbing what every other call returns.
  Spectra.clearMocks();
  const queuedMock = await Spectra.intercept(
    "api/posts",
    "GET",
    Fixture.apiData.mockPosts
  );
  await queuedMock.respondOnce([
    { id: 777, title: "One-Time Queued Response", body: "Only served once" }
  ]);

  await MatchersPage.fetchApiButton.click();
  await MatchersPage.fetchedItems.shouldHaveLength(1);
  await MatchersPage.fetchedItems.first().shouldContainText("One-Time Queued Response");

  // The queued response is consumed by the call above — this one reverts to the base rule.
  await MatchersPage.fetchApiButton.click();
  await MatchersPage.fetchedItems.shouldHaveLength(Fixture.apiData.mockPosts.length);
  await MatchersPage.fetchedItems.first().shouldContainText(Fixture.apiData.mockPosts[0].title);
});
