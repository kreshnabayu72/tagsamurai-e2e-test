it("Navigate browser history with Spectra.back(), forward(), and refresh()", async () => {
  await MatchersPage.open();

  // This demo app is single-page — its in-app "navigation" (Spectra.navigate("/#section")) only
  // ever sets window.location.hash, which this browser does not push as a traversable history
  // entry (history.length never grows), so there is nothing for back()/forward() to jump between.
  // Two distinct real paths give them something real: Vite's dev server serves the same SPA shell
  // for any path, but the browser still treats each as its own document and pushes a genuine
  // history entry — exactly like a real multi-page site would.
  await Spectra.navigate("/history-nav-a");
  await Spectra.browser.shouldContainUrl("/history-nav-a");

  await Spectra.navigate("/history-nav-b");
  await Spectra.browser.shouldContainUrl("/history-nav-b");

  await Spectra.back();
  await Spectra.browser.shouldContainUrl("/history-nav-a");

  await Spectra.forward();
  await Spectra.browser.shouldContainUrl("/history-nav-b");

  // The document reloads, but the current URL survives it.
  await Spectra.refresh();
  await Spectra.browser.shouldBeLoaded();
  await Spectra.browser.shouldContainUrl("/history-nav-b");
});
