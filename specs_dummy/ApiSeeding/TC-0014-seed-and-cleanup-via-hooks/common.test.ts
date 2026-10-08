// The `before` hook (hooks/before/common.hook.ts) already ran by the time this test body
// executes — it seeded a post via a real POST to the demo server's self-hosted API and stashed
// the result on globalThis for this test to read. Cleanup (hooks/after/common.hook.ts) runs
// after this whole suite finishes, so it can't be observed from inside the suite's own tests —
// a separate monitoring suite/run would be how a real project verifies cleanup actually happened.
//
// Suite-scoped hooks only run when a worker's whole batch is unambiguously scoped to this one
// suite (e.g. `spectra run specs/ApiSeeding` or targeting this TC directly) — hook functions are
// process-global singleton slots, not per-test-case, so a worker batch spanning multiple suites
// has no correct way to scope suite A's hooks to only run around suite A's own tests, and skips
// suite-level hooks entirely rather than risk applying the wrong suite's hooks to the wrong
// tests. Running the FULL default template (`spectra run -t web`/`android`, every suite at once)
// will legitimately fail this specific test for that reason — that's an inherent limitation of
// the current worker-batching model, not a bug in this demo.
it("Verify test data seeded by a before hook via the demo server's self-hosted API is available to the test", async () => {
  const seeding = (globalThis as any).__apiSeeding;

  if (!seeding?.seededPost) {
    throw new Error("Expected the before hook to have seeded a post onto globalThis.__apiSeeding, found none");
  }
  if (typeof seeding.seededPost.id !== "number") {
    throw new Error(`Expected seeded post to have a numeric id, got ${JSON.stringify(seeding.seededPost.id)}`);
  }
  if (seeding.seededPost.title !== "TestSpectra seeded post") {
    throw new Error(`Expected seeded post title to match, got "${seeding.seededPost.title}"`);
  }
  if (seeding.cleanedUp !== false) {
    throw new Error("Expected cleanedUp to still be false — the after hook hasn't run yet at this point");
  }
});
