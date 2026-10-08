it("Verify a custom environmentVariables entry is readable via Spectra.env", async () => {
  if (Spectra.env.DEMO_API_MODE !== "sandbox") {
    throw new Error(`Expected Spectra.env.DEMO_API_MODE to be "sandbox", got "${Spectra.env.DEMO_API_MODE}"`);
  }
});
