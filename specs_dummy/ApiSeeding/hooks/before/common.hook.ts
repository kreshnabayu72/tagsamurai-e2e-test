// Suite-level `before` hook — runs once before this suite's tests. Hooks run in the same worker
// process/global scope as the test files, so data seeded here is handed to tests via a plain
// `globalThis` namespace rather than a return value (hooks don't have a return channel).
//
// Seeds against the demo server's own self-hosted API (started with `--demo`) instead of an
// external public API, so the round trip is deterministic and offline-safe — same seed-in-
// `before`, clean-up-in-`after` hook mechanics, with a REAL network round trip, just against a
// server we control. Because the hook runs on the HOST (not the device), this suite needs the
// demo server up on the host: run it with `--demo` (e.g. `spectra run ... -t android --demo`).
// Swap the base URL for a real backend's seeding endpoint in an actual project.
export default async function () {
  const res = await fetch("http://localhost:5200/api/posts", {
    method: "POST",
    headers: { "Content-Type": "application/json; charset=UTF-8" },
    body: JSON.stringify({
      title: "TestSpectra seeded post",
      body: "Created by ApiSeeding's before hook for TC-0014.",
      userId: 1,
    }),
  });

  if (!res.ok) {
    throw new Error(`ApiSeeding before hook: failed to seed post (${res.status} ${res.statusText})`);
  }

  const seeded = await res.json();
  (globalThis as any).__apiSeeding = { seededPost: seeded, cleanedUp: false };
}
