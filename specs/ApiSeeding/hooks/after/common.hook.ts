// Suite-level `after` hook — runs once after this suite's tests complete, regardless of whether
// they passed, so seeded data is always cleaned up rather than leaking into later runs.
export default async function () {
  const seeding = (globalThis as any).__apiSeeding;
  if (!seeding?.seededPost?.id) return;

  const res = await fetch(`http://localhost:5200/api/posts/${seeding.seededPost.id}`, {
    method: "DELETE",
  });

  if (!res.ok) {
    throw new Error(`ApiSeeding after hook: failed to clean up seeded post ${seeding.seededPost.id} (${res.status})`);
  }

  seeding.cleanedUp = true;
}
