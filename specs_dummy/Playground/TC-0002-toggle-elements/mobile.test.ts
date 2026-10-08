it("Verify typing credentials and updating playground inputs", async () => {
  await PlaygroundPage.open();
  await PlaygroundPage.fillCredentials("qa.expert@testspectra.dev", "JWT_custom_session_token");
  await PlaygroundPage.emailInput.shouldHaveValue("qa.expert@testspectra.dev");
  await PlaygroundPage.tokenInput.shouldContainValue("JWT_custom_session_token");
});
