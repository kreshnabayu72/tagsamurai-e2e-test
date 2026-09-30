---
id: TC-GS-USER-E2E-006-deactivate-force-logout-active-session
title: Deactivating a user force-logs-out their active session in real time
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-481
  - TC-GS-USER-251
coverage:
  web: automated
---

# Deactivating a user force-logs-out their active session in real time

## Prerequisites

- Login as Role: Total Control, entity is Client, in browser session A
- User "Rina Wijaya" is logged in and active in a separate browser session B, on any page of any licensed product
- The FE team requests a second, independently controllable browser session for this spec, since it needs two concurrent logged-in accounts
- In session B, the notification list of "Rina Wijaya" is captured before step 1 and again right after step 4

## Test Steps

1. In session A, click Toggle Active [Global] on the row of "Rina Wijaya" to turn it OFF
2. Click `[Deactivate]` on the dialog
3. Verify success toast "Success, user has been deactivated." appears in session A
4. In session B, verify a real-time message appears telling the user their session has been ended
5. In session B, perform any request or navigate to any page
6. Verify the request in session B returns 401 and the session is treated as invalid
7. In session B, attempt to log in again as "Rina Wijaya"
8. Verify a login-block dialog appears, consistent with the user being deactivated

### No separate notification

9. In session B, compare the notification list captured right after step 4 with the one captured before step 1
10. Verify no new notification entry exists for "Rina Wijaya" from this deactivation, and the only feedback she received is the real-time session-ended message and the login-block dialog "Account Deactivated"

## Notes

- This spec needs two browser sessions with two different accounts, which is why it is kept separate from TC-GS-USER-E2E-005, following `docs/e2e-conventions.md` section 3 (split for a different account).
- "Rina Wijaya" is Active with no other dependency before this spec runs, and is left Inactive afterward. No further cleanup is required, since no data is created.
- TC-GS-USER-251: Deactivate must not create a separate in-app notification. The session-ended message and the login-block dialog already cover it.
