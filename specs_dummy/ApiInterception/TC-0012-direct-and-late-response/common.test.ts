it("Intercept a direct (immediate) response and a late (delayed) response using Fixture data", async () => {
  await MatchersPage.open("api-fetch");

  // The app fetches the self-hosted demo endpoint (/api/posts on web, the same path served by
  // the demo server and reached through the device proxy on mobile) — no external network, so
  // there's no upstream latency leaking into the "immediate" assertion below. On web, CDP's
  // Fetch domain intercepts it; on Android, the device's global HTTP proxy routes it through the
  // same worker-side mock engine. Neither platform needs the app, or this test, to know anything
  // special about being under test.
  Spectra.clearMocks();

  // Direct (immediate) response — Fixture data returned with no artificial latency.
  const mock = await Spectra.intercept("api/posts", "GET", Fixture.apiData.mockPosts);
  await MatchersPage.fetchApiButton.click();
  await MatchersPage.fetchStatusBadge.shouldHaveText("200 OK");
  await MatchersPage.fetchedItems.shouldHaveLength(Fixture.apiData.mockPosts.length);
  await MatchersPage.fetchedItems.first().shouldContainText(Fixture.apiData.mockPosts[0].title);

  // Late (delayed) response — same mock rule, switched to hold the response back via `delayMs`.
  // The loading indicator must still be visible right after the click, proving this is real
  // network-level latency (the request genuinely stays pending) rather than a client-side-only
  // spinner timer. The delay is set past the default assertion timeout on purpose, to demonstrate
  // the per-assertion `{ timeoutMs }` override below — without it, these assertions would fail-fast
  // before the delayed response ever arrives.
  await mock.respondWith(Fixture.apiData.mockPosts, { delayMs: 2500 });
  await MatchersPage.fetchApiButton.click();
  await MatchersPage.fetchLoadingIndicator.shouldBeVisible();
  await MatchersPage.fetchStatusBadge.shouldHaveText("200 OK", { timeoutMs: 3500 });
  await MatchersPage.fetchedItems.shouldHaveLength(Fixture.apiData.mockPosts.length, { timeoutMs: 3500 });
});
