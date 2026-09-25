it("Make a genuine (non-intercepted) network call and verify it is recorded", async () => {
  await MatchersPage.open("api-fetch");

  // Deliberately no Spectra.intercept() call — this is a genuine request that actually leaves
  // the app and hits a real server, not a mock. It targets the demo server's own self-hosted
  // endpoint (started with `--demo`) instead of an external public API, so it's deterministic
  // and fast everywhere. On web the browser reaches localhost directly; on Android it's
  // transparently routed through the device's global HTTP proxy with no matching mock rule, so
  // the worker's proxy just forwards it for real. Clear any mock a previous test in this suite
  // left registered (e.g. against /api/posts) so it can't accidentally catch this request too —
  // this test uses a different resource (/api/todos/1) specifically to avoid that collision,
  // plus a cache-busting query param so a repeat run doesn't get a 304 Not Modified from the
  // device/browser's own HTTP cache.
  Spectra.clearMocks();
  const cacheBuster = Date.now();
  await MatchersPage.fetchCustomUrlInput.type(`http://localhost:5200/api/todos/1?cb=${cacheBuster}`);
  await MatchersPage.fetchApiButton.click();
  await MatchersPage.fetchStatusBadge.shouldHaveText("200 OK");

  const entry = Spectra.browser.recordedNetwork.find((e) => e.url.includes(`todos/1?cb=${cacheBuster}`));
  if (!entry) {
    throw new Error("Expected a recorded network entry for the real demo-server call, found none");
  }
  if (entry.status !== 200) {
    throw new Error(`Expected recorded entry status 200, got ${entry.status}`);
  }
});
