class AuthPage {
  get checkStatusButton() { return Spectra.get("#check-auth-status-btn"); }
  get statusBadge() { return Spectra.get("#auth-status-badge"); }

  async open() {
    await Spectra.navigate("/#auth");
  }
}

export default new AuthPage();
