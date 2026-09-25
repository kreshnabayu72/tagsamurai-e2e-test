it("Verify plugin-registered custom Spectra commands", async () => {
  await Spectra.navigate("/#playground");

  // Button-specific command registered by @testspectra/plugin-demo (common platform stem).
  const enabledButton = Spectra.findButton("#demo-enabled-btn");
  await enabledButton.shouldBeVisible();
  await enabledButton.assertLabel("Enabled Button");
  await enabledButton.press();

  // Universal component command registered by the same plugin (common platform stem).
  await Spectra.findComponent("#demo-email-input-pg").shouldExist();

  // Web-only command registered by the plugin (web platform stem).
  await Spectra.findByCss("#demo-email-input-pg").shouldExist();
});
