export default async function (this: any) {
  // Host-side (Bun) fetch — not the browser's — so there's no CORS/credentials restriction on
  // reading the raw Set-Cookie header, HttpOnly included.
  const res = await fetch("http://localhost:5200/api/login", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ email: "demo@testspectra.dev", password: "demo-password" }),
  });
  if (!res.ok) {
    throw new Error(`seedSession: login failed (${res.status})`);
  }
  await this.browser.setCookies(res.headers.getSetCookie(), res.url);
}
