it("Mock a Server-Sent Events (EventSource) stream via the existing network-intercept engine", async () => {
  await MatchersPage.open("sse");

  // EventSource's initial request is a plain HTTP GET under the hood — CDP's Fetch domain
  // intercepts it exactly like any other fetch()/XHR request. Fulfilling it with a
  // text/event-stream body delivers every "data: ...\n\n" block at once; the browser's own
  // EventSource parser still splits that into individual "message" events and dispatches them
  // just as it would for a real stream, which is the part this demo actually cares about.
  //
  // What this can't fake: `Fetch.fulfillRequest` delivers a complete, connection-closing
  // response (there's no way to keep it open indefinitely the way a real SSE endpoint would), so
  // the browser's EventSource treats that closure as a connection error shortly after — the
  // events still arrive and get processed first, but the app's own "CONNECTED" status flips back
  // to disconnected right after, same as it would after a real server unexpectedly closed the
  // connection. So this test verifies the events were received, not that the connection stayed
  // open — genuinely-persistent SSE isn't something a request/response-shaped mock can simulate.
  await Spectra.intercept("/api/sse-feed", "GET", {
    body: 'data: {"text":"hello from mock SSE"}\n\ndata: {"text":"second event"}\n\n',
    headers: { "Content-Type": "text/event-stream" },
  });

  await Spectra.get("#sse-connect-btn").click();
  await Spectra.getAll(".sse-message-item").shouldHaveLength(2);
  await Spectra.getAll(".sse-message-item").first().shouldContainText("hello from mock SSE");
  await Spectra.getAll(".sse-message-item").last().shouldContainText("second event");
});
