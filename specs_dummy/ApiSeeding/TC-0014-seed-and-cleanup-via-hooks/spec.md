---
id: TC-0014-seed-and-cleanup-via-hooks
title: Verify test data seeded by a before hook via the demo server's self-hosted API is available to the test
priority: Medium
caseType: Positive
status: ready-for-automation
coverage:
  web: automated
  mobile: automated
---

# Verify test data seeded by a before hook via the demo server's self-hosted API is available to the test

The before hook seeds against the demo server's self-hosted `/api/posts` (POST), and the after
hook cleans up via DELETE. Because the hooks run on the host worker (not on the device), the demo
server must be up on the host — run this suite with `--demo` on any platform, e.g.
`spectra run "specs/ApiSeeding/TC-0014-seed-and-cleanup-via-hooks/common.test.ts" -t android --demo`.

## Test Steps
1. Before hook seeds a post via a real POST to the demo server's self-hosted API and stashes it on globalThis
2. Verify the seeded post is present on globalThis
3. Assert the seeded post has a numeric id and the expected title
4. Assert cleanup has not yet run (the after hook runs after this suite finishes)
