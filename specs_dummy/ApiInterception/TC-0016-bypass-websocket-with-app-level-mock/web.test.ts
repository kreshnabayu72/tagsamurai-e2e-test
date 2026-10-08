it("Bypass a real WebSocket connection via an app-level test-only mock flag", async () => {
  await MatchersPage.open("websocket");

  // Set BEFORE the app opens its connection — the component checks this flag inside its own
  // connect() handler and, if present, uses an in-memory fake socket instead of a real
  // `new WebSocket(...)`. This is necessarily app-level, not network-level: see this TC's
  // spec.md for why CDP has no way to intercept/mock a WebSocket handshake or its frames the
  // way Spectra.intercept() does for fetch()/XHR/EventSource.
  await Spectra.browser.evaluate(
    "window.__mockWebSocketMessages = ['hello from mock WS', 'second frame']",
  );

  await Spectra.get("#ws-connect-btn").click();
  await Spectra.get("#ws-connection-status").shouldHaveText("CONNECTED");
  await Spectra.getAll(".ws-message-item").shouldHaveLength(2);
  await Spectra.getAll(".ws-message-item").first().shouldContainText("hello from mock WS");
  await Spectra.getAll(".ws-message-item").last().shouldContainText("second frame");

  await Spectra.get("#ws-disconnect-btn").click();
  await Spectra.get("#ws-connection-status").shouldHaveText("DISCONNECTED");
});
