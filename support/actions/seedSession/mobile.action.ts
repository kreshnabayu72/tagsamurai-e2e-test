export default async function (this: any) {
  // Android has no cookie jar to write into — the deep link asks the app to log itself in
  // (a known, sanctioned test account, server-side) and persist the result through its own
  // secure storage (e.g. react-native-keychain), the same way a real login would. See
  // docs/v2/features/authentication-and-session-seeding.md for why this doesn't accept an
  // externally-supplied session value the way the web action does.
  await this.navigate("testspectra-demo://seed-session");
  await this.get("~auth-status-badge").waitForElement(10000);
}
