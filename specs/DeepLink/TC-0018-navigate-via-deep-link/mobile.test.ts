it("Navigate directly to a native route via Spectra.navigate() and an Android deep link", async () => {
  // The orchestrator's own bootstrap launches the app (fire-and-forget, ~1.5s wait) before any
  // test code runs at all — other tests never notice because their first action is a click()
  // with its own generous poll budget, which absorbs whatever's left of the cold start. This
  // test's first action is Spectra.navigate() itself, which is also fire-and-forget and has no
  // such budget, so without this it races the deep-link intent against the app's own still-in-
  // progress initial boot. Waiting for the home screen to actually be up first avoids that race.
  await Spectra.get("~toggle-sidebar-btn").waitForElement(30000);

  // No prior navigation, no button clicks — this jumps straight to the route via
  // `adb shell am start`, exactly like opening the app from a push notification or an
  // external link would.
  await Spectra.navigate("testspectra-demo://deeplink-target");
  await Spectra.get("~deeplink-target-marker").waitForElement(10000);

  await Spectra.get("~deeplink-target-marker").shouldHaveText("deeplink-target");
  await Spectra.get("~deeplink-received-message").shouldHaveText("(none)");

  await Spectra.get("~back-to-home-btn").click();

  // Deep links can carry query params — assert they survive the intent all the way to the screen.
  await Spectra.navigate("testspectra-demo://deeplink-target?message=hello-from-deep-link");

  await Spectra.get("~deeplink-received-message").waitForElement(10000);
  await Spectra.get("~deeplink-received-message").shouldHaveText("hello-from-deep-link");

  await Spectra.get("~back-to-home-btn").click();
});
