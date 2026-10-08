// A single common.test.ts, not a web.test.ts/mobile.test.ts pair — the orchestrator's test-case
// discovery recognizes "common" as a platform stem for every target (web, android, ios, mobile),
// so this one file runs unmodified on all of them. This works here because every Spectra.*
// command below is genuinely platform-agnostic (the DSL layer has zero platform branching by
// design) and MatchersPage's selectors are already abstracted per-platform behind identically-
// named getters — nothing in this specific test depends on a page origin, a native-only gesture,
// or a browser-chrome-only assertion (see TC-0013's real-network test for a case that CAN'T be
// shared this way: Android has no implicit page origin to resolve a relative fetch URL against,
// so the URL itself has to differ per platform even though the commands stay identical).
it("Verify exact text, substring text, and input values", async () => {
  await MatchersPage.open("text");

  // Text assertions (positive and negative)
  await MatchersPage.exactText.shouldHaveText(Fixture.playgroundData.welcomeText);
  await MatchersPage.exactText.shouldNotHaveText("Unexpected Text");

  await MatchersPage.partialText.shouldContainText("Welcome");
  await MatchersPage.partialText.shouldNotContainText("Goodbye");

  // Value assertions (positive and negative)
  await MatchersPage.emailInput.shouldHaveValue(Fixture.playgroundData.defaultEmail);
  await MatchersPage.emailInput.shouldNotHaveValue("wrong.user@testspectra.dev");

  await MatchersPage.tokenInput.shouldContainValue("JWT_");
  await MatchersPage.tokenInput.shouldNotContainValue("EXPIRED_SESSION");
});
