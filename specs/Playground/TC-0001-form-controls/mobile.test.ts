it("Verify playground form inputs and default states", async () => {
  await Step.verifyPlaygroundState();
  await PlaygroundPage.emailInput.shouldHaveValue(Fixture.playgroundData.defaultEmail);
  await PlaygroundPage.tokenInput.shouldContainValue("JWT_");
  await PlaygroundPage.exactText.shouldHaveText(Fixture.playgroundData.welcomeText);
});
