---
id: TC-GS-USER-E2E-005-delete-bulk-toggle-active-remove-access
title: Delete, bulk selection, Toggle Active, and Remove Access on the User List and Edit modal
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-36
  - TC-GS-USER-44
  - TC-GS-USER-52
  - TC-GS-USER-37
  - TC-GS-USER-45
  - TC-GS-USER-433
  - TC-GS-USER-33
  - TC-GS-USER-353
  - TC-GS-USER-453
  - TC-GS-USER-34
  - TC-GS-USER-35
  - TC-GS-USER-42
  - TC-GS-USER-435
  - TC-GS-USER-41
  - TC-GS-USER-447
  - TC-GS-USER-43
  - TC-GS-USER-446
  - TC-GS-USER-46
  - TC-GS-USER-480
  - TC-GS-USER-443
  - TC-GS-USER-47
  - TC-GS-USER-445
  - TC-GS-USER-444
  - TC-GS-USER-449
  - TC-GS-USER-49
  - TC-GS-USER-352
  - TC-GS-USER-425
  - TC-GS-USER-351
  - TC-GS-USER-387
  - TC-GS-USER-50
  - TC-GS-USER-258
  - TC-GS-USER-38
  - TC-GS-USER-434
coverage:
  web: automated
---

# Delete, bulk selection, Toggle Active, and Remove Access on the User List and Edit modal

## Prerequisites

- Login as Role: Total Control, entity is Client
- The environment is an automation-dedicated environment prepared and isolated by the FE team, so Select All and bulk actions may act on the full result set
- More than 10 users exist, spread across at least 2 pages of the User List, with mixed Active and Inactive status, so Select All is exercised against a realistic mixed dataset
- User "Budi Santoso" exists, has no borrowed asset, no pending approval, and no uploaded photo
- User "Doni Pratama" exists and has an active Borrowed Asset in Fixed Asset (FAMS)
- User "Wulan Setiawan" has an uploaded custom photo (not the default avatar)
- User "Siti Rahmawati" is Active in every licensed product, including FAMS
- User "Fajar Ramadhan" has status Pending Activation and has never logged in
- User "Yanti Kusuma" is Active and has a pending approval task in progress
- User "Zainal Arifin" is Active and has no pending approval
- User "Umar Fauzi" is Active and has a pending approval task in progress
- Users "Agus Salim", "Bayu Permana", and "Candra Wijaya" are all Active
- User "Denny Kurniawan" has Access `[Global Settings, FAMS]`, an active Borrowed Asset, and a pending approval task, both in FAMS
- User "Eka Wijaya" has Access `[Global Settings, FAMS]`, with no asset or approval in FAMS
- User "Rendi Saputra" has Access `[Global Settings]` and currently has `access_level = Total Control` in Role & Permission
- Every listed user other than the logged-in admin is a Login User created by automation seeding

## Test Steps

### Screening: Default User and Self guards

1. Verify the `[Delete]` action is disabled on the Default User row, with tooltip "Default User cannot be modified."
2. Verify the Toggle Active control is disabled on the Default User row, with tooltip "Default User cannot be modified."
3. Open the Edit modal on the Default User row
4. Verify the Access checkboxes are disabled, with tooltip "Default User cannot be modified."
5. Click `✕` to close the modal
6. Verify the `[Delete]` action is disabled on the row of the logged-in admin, with tooltip "You can't manage your own account from here."
7. Verify the Toggle Active control is disabled on the row of the logged-in admin, with tooltip "You can't manage your own account from here."

### Delete on a single row

8. Click `[Delete]` on the row of "Budi Santoso"
9. Verify dialog title "Delete User" with body "• Budi Santoso\nHistorical transaction data will be preserved.\nThis action cannot be undone. Are you sure you want to delete it?" and buttons `[Cancel]` and `[Delete]`
10. Click `[Cancel]` on the dialog
11. Verify the dialog closes and the row "Budi Santoso" still appears
12. Click `[Delete]` on the row of "Budi Santoso" again
13. Double-click `[Delete]` on the dialog in quick succession
14. Verify `[Delete]` becomes disabled and shows a loading state immediately after the first click, and the second click triggers no additional request
15. Verify success toast "Success, user has been deleted." appears and exactly one delete happens, with no duplicate error or effect
16. Verify the row "Budi Santoso" no longer appears in the User List
17. Click `[Delete]` on the row of "Doni Pratama"
18. Verify the dialog shows an additional warning that "Doni Pratama" still has a related asset and recommends returning it first, while `[Delete]` stays enabled
19. Click `[Delete]` on the dialog
20. Verify success toast "Success, user has been deleted." appears and the row "Doni Pratama" no longer appears in the User List
21. Click `[Delete]` on the row of "Wulan Setiawan" and confirm on the dialog
22. Verify success toast "Success, user has been deleted." appears
23. Verify the uploaded photo of "Wulan Setiawan" is permanently removed from storage, not merely hidden from the list

### Toggle Active

24. On the User Detail of "Siti Rahmawati", turn the per-product Toggle Active `FAMS` OFF
25. Verify only the `FAMS` toggle turns OFF, the Toggle Active [Global] stays ON, and every other product toggle stays ON
26. On the User List, click Toggle Active [Global] on the row of "Siti Rahmawati" to turn it OFF
27. Verify dialog "Deactivate User" appears with body "• Siti Rahmawati\nThis will deactivate user across all products. Are you sure you want to deactivate it?"
28. Click `[Cancel]` on the dialog
29. Verify the dialog closes and the Toggle Active [Global] on "Siti Rahmawati" returns to ON
30. Click Toggle Active [Global] on the row of "Siti Rahmawati" to turn it OFF again
31. Click `[Deactivate]` on the dialog
32. Verify success toast "Success, user has been deactivated." appears and every per-product toggle of "Siti Rahmawati", including `FAMS`, is OFF
33. Click Toggle Active [Global] on the row of "Siti Rahmawati" to turn it ON
34. Verify dialog "Activate User" appears with body "• Siti Rahmawati\nThis will activate user across all products. Are you sure you want to activate it?"
35. Click `[Cancel]` on the dialog
36. Verify the dialog closes and the Toggle Active [Global] on "Siti Rahmawati" stays OFF
37. Click Toggle Active [Global] on the row of "Siti Rahmawati" to turn it ON again
38. Click `[Activate]` on the dialog
39. Verify success toast "Success, user has been activated." appears
40. Verify the per-product toggle `FAMS` of "Siti Rahmawati" stays OFF, because it was turned off manually before Global went OFF, while every other product toggle returns to ON
41. Click Toggle Active [Global] on the row of "Fajar Ramadhan" to turn it OFF and confirm on the dialog
42. Verify success toast "Success, user has been deactivated." appears, and badge "Pending Activation" still shows together with status Inactive
43. Click Toggle Active [Global] on the row of "Yanti Kusuma" to turn it OFF
44. Verify the dialog shows an additional line that "Yanti Kusuma" has an approval task in progress that will need to be resolved by a Total Control admin
45. Click `[Deactivate]` on the dialog
46. Verify success toast "Success, user has been deactivated." appears

### Bulk Deactivate and Bulk Activate

47. Select the checkboxes of "Agus Salim", "Bayu Permana", and "Candra Wijaya"
48. Click the bulk action `Deactivate`
49. Verify dialog "Deactivate Users" with body bullets of the 3 selected names and "They will be deactivated across all products. Are you sure you want to deactivate them?"
50. Click `[Cancel]` on the dialog
51. Verify the dialog closes and all 3 users stay Active
52. Click the bulk action `Deactivate` again and click `[Deactivate]` on the dialog
53. Verify success toast "Success, user has been deactivated." appears and all 3 users become Inactive
54. Select the checkboxes of "Agus Salim", "Bayu Permana", and "Candra Wijaya" again
55. Click the bulk action `Activate`
56. Verify dialog "Activate Users" with body bullets of the 3 selected names and "They will be activated across all products. Are you sure you want to activate them?"
57. Click `[Cancel]` on the dialog
58. Verify the dialog closes and all 3 users stay Inactive
59. Click the bulk action `Activate` again and click `[Activate]` on the dialog
60. Verify success toast "Success, user has been activated." appears and all 3 users become Active
61. Select the checkboxes of "Zainal Arifin" and "Umar Fauzi", then click the bulk action `Deactivate`
62. Verify the dialog shows an additional line that some of the selected users have an approval task in progress that will need to be resolved by a Total Control admin
63. Click `[Deactivate]` on the dialog and verify success toast "Success, user has been deactivated." appears

### Remove Access via Edit modal

64. Open the Edit modal on "Eka Wijaya"
65. Uncheck `FAMS` in the Access field
66. Click `[Save]`
67. Verify no additional dialog appears and success toast "Success, user has been updated." appears
68. Verify the Access of "Eka Wijaya" becomes `[Global Settings]` only
69. Open the Edit modal on "Denny Kurniawan"
70. Uncheck `FAMS` in the Access field
71. Click `[Save]`
72. Verify a warning dialog appears mentioning that removing access to Fixed Asset will affect the borrowed asset and pending approval of "Denny Kurniawan", historical data will be preserved, but the user will lose functional access
73. Click `[Cancel]` on the dialog
74. Verify the Edit modal stays open and `FAMS` in the Access field is still unchecked, unsaved
75. Click `[Save]` again
76. Verify the same warning dialog appears
77. Confirm the dialog
78. Verify success toast "Success, user has been updated." appears and the Access of "Denny Kurniawan" becomes `[Global Settings]` only
79. Open the Edit modal on "Rendi Saputra"
80. Uncheck `Global Settings` in the Access field
81. Click `[Save]`
82. Verify a warning dialog appears explicitly mentioning "• Rendi Saputra\nThis user currently has Total Control in Role & Permission. Removing Global Settings access will also revoke it. Are you sure you want to remove it?"
83. Confirm the dialog
84. Verify success toast "Success, user has been updated." appears, the Access of "Rendi Saputra" becomes empty, and `access_level` is no longer Total Control

### Select All and Bulk Delete

85. Verify the button "Select All ({N} records)" shows `{N}` equal to the total user count matching the current filter
86. Click "Select All ({N} records)"
87. Verify every row across every page becomes checked, except the Default User row and the logged-in admin row, which stay unchecked
88. Verify the button toggles to "Unselect All"
89. Click the bulk action `Delete`
90. Verify the confirmation dialog lists the selected users
91. Click `[Cancel]` on the dialog
92. Verify the dialog closes, every previously selected row is still checked, and the bulk action bar is still visible
93. Click the bulk action `Delete` again
94. Click `[Delete]` on the dialog
95. Verify success toast "Success, user has been deleted." appears
96. Verify every row that was selected, except the Default User and the logged-in admin, no longer appears in the User List

## Notes

- One spec covers many independent actions on the User List and the Edit modal, all under the same Role Total Control and the same Client entity. They are combined because none of them depends on a different account, entity, hardware, or a mix of data creators, following `docs/e2e-conventions.md` section 3.
- Select All and Bulk Delete (steps 85–96) run last on purpose, because they act on every remaining row except the Default User and the logged-in admin. Running this earlier would delete the seeded users that the Delete single, Toggle Active, Bulk Deactivate/Activate, and Remove Access sections still need. Placed last, it also cleans up every seeded user still present (Siti, Fajar, Yanti, Zainal, Umar, Agus, Bayu, Candra, Denny, Eka, and Rendi), so no separate cleanup step is needed for them. Budi, Doni, and Wulan are already gone by then from the Delete single section.
- Step 61 uses "Umar Fauzi" instead of "Yanti Kusuma" for the pending-approval half of TC-GS-USER-449's mixed selection, because "Yanti Kusuma" is already Inactive by then (from steps 43–46).
- TC-GS-USER-38's exclusion of Default User and Self from Select All is verified together with TC-GS-USER-258's Select All mechanic in steps 85–88, since both describe the same click.
- TC-GS-USER-51 (Remove Access leaving 0 Access) is not covered here. Its expected result is ambiguous in the source TC ("blocked OR allowed"), so it is logged in `prd-gap-registry.md` instead of being guessed in this spec.
- TC-GS-USER-352 (no dialog when the removed product has no asset or approval) and TC-GS-USER-49 describe the same outcome and are verified together in steps 64–68.
- TC-GS-USER-387 and TC-GS-USER-50 describe the same Global Settings removal warning and are verified together in steps 79–84.
- If the spec fails before reaching step 85, Select All and Bulk Delete does not run, so every seeded user must still be cleaned up individually in that case.
- TC-GS-USER-39, 40, 451, 452, 48, and 53 (mid-action 500/403/404 races that can only be triggered by mocking the server) are not covered here; they are the frontend layer's responsibility (TC-GS-USER-FE-082, 083, 084, 085, 104, 110).
- TC-GS-USER-448, 458, 459, and 398 (bulk bar collapse to singular dialog, and Activate/Deactivate hidden when the whole selection is already uniform) are pure UI/state behavior with no backend effect and are not covered here (TC-GS-USER-FE-102, 098, 099, 105).
