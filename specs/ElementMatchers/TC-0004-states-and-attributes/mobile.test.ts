it("Verify button state, checkbox, radio and attributes", async () => {
  await MatchersPage.open("state");

  // Interactivity & state assertions
  await MatchersPage.submitButton.shouldBeEnabled();
  await MatchersPage.submitButton.shouldBeClickable();

  await MatchersPage.disabledButton.shouldBeDisabled();
  await MatchersPage.disabledButton.shouldNotBeClickable();

  // Checked states
  await MatchersPage.checkbox.shouldNotBeChecked();
  await MatchersPage.radio.shouldBeChecked();

  // Focus & blur states (element API). On mobile `focus()` clicks the field and `blur()` is a
  // no-op (native apps have no DOM focus concept), so we only assert the focused transition.
  await MatchersPage.focusInput.shouldNotBeFocused();
  await MatchersPage.focusInput.focus();
  await MatchersPage.focusInput.shouldBeFocused();
  await MatchersPage.focusInput.blur();

  // Focus states (static Spectra API) mirror the element API on mobile.
  await Spectra.focus(MatchersPage.focusInput);
  await MatchersPage.focusInput.shouldBeFocused();
  await Spectra.blur(MatchersPage.focusInput);

  // Class, Attribute, and CSS assertions
  await MatchersPage.activeTab.shouldHaveClass("is-active");
  await MatchersPage.activeTab.shouldNotHaveClass("is-hidden");

  await MatchersPage.navLink.shouldHaveAttribute("accessibilityLabel", "nav-link");
  await MatchersPage.navLink.shouldNotHaveAttribute("disabled");

  await MatchersPage.styledElement.shouldHaveCss("color", "rgba(239,68,68,1)");
  await MatchersPage.styledElement.shouldNotHaveCss("color", "rgba(0,0,255,1)");
});
