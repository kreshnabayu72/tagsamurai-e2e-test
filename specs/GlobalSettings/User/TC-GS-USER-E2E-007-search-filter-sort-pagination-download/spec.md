---
id: TC-GS-USER-E2E-007-search-filter-sort-pagination-download
title: Search, filter, sort, pagination, and download reflect real data on the User List
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-358
  - TC-GS-USER-359
  - TC-GS-USER-360
  - TC-GS-USER-361
  - TC-GS-USER-362
  - TC-GS-USER-554
  - TC-GS-USER-555
  - TC-GS-USER-556
  - TC-GS-USER-557
  - TC-GS-USER-357
  - TC-GS-USER-127
  - TC-GS-USER-197
  - TC-GS-USER-198
  - TC-GS-USER-199
  - TC-GS-USER-200
  - TC-GS-USER-201
  - TC-GS-USER-202
  - TC-GS-USER-207
  - TC-GS-USER-208
  - TC-GS-USER-364
  - TC-GS-USER-128
  - TC-GS-USER-218
  - TC-GS-USER-219
  - TC-GS-USER-220
  - TC-GS-USER-221
  - TC-GS-USER-222
  - TC-GS-USER-223
  - TC-GS-USER-224
  - TC-GS-USER-225
  - TC-GS-USER-227
  - TC-GS-USER-228
  - TC-GS-USER-229
  - TC-GS-USER-230
  - TC-GS-USER-210
  - TC-GS-USER-211
  - TC-GS-USER-212
  - TC-GS-USER-216
  - TC-GS-USER-132
  - TC-GS-USER-131
  - TC-GS-USER-490
  - TC-GS-USER-491
  - TC-GS-USER-492
  - TC-GS-USER-493
  - TC-GS-USER-496
  - TC-GS-USER-497
coverage:
  web: automated
---

# Search, filter, sort, pagination, and download reflect real data on the User List

## Prerequisites

- Login as Role: Total Control, entity is Client
- More than 25 users exist in total, spread across at least 2 pages, on top of the users listed below
- User "Andi Saputra" has First Name starting with an uppercase letter
- User "budi Iskandar" has First Name starting with a lowercase letter, so Name sort can be checked against ICU collation `en-US-x-icu` instead of binary/ASCII order
- User "Budi Santoso" is Active, Position "Staff", Division "Finance", a known unique Email, Employee ID "EMP-002", 1 Access, and was last modified by admin "Rina Kartika"
- User "Citra Wulandari" is Active, Position "Manager", Division "Marketing", and was last modified by admin "Doni Admin"
- User "Doni Pratama" has Access `[Fixed Asset, Global Settings]` (2 Access) and TAG "RFID-00321"
- User "Eka Prasetyo" is Inactive
- User "Fajar Nugroho" has status Pending Activation and has never logged in
- User "Gita Ayu" is Activated normally, with no pending email change
- User "Hana Melati" is Activated and has a pending email change (`pendingEmail` filled), so its Activation Status is "Pending Email Confirmation"
- User "Indra Kusuma" has Position and Employee ID both empty
- User "Joko Prasetyo" has Access `[Global Settings, Fixed Asset, Admin Console]` (3 Access)
- User "Kirana Dewi" has Temporary User Yes with Temporary Until 3 days from today
- User "Laras Ayu" has Temporary User Yes with Temporary Until 10 days from today
- Columns Activation Status, Temporary User, Temporary Until, and TAG are curated (hidden by default) and are enabled via Setup Column before this spec's steps run
- The FE team is asked to provide a way for the script to read the actual downloaded file's content (not just its filename), since several steps verify real file bytes

## Test Steps

### Search across columns

1. Search "budi.santoso" (part of the known email of "Budi Santoso")
2. Verify "Budi Santoso" appears in the result, even though the keyword does not match its Name
3. Clear the search
4. Search "Manager" (Position of "Citra Wulandari")
5. Verify "Citra Wulandari" appears in the result, even though the keyword does not match its Name or Email
6. Clear the search
7. Search "Finance" (Division of "Budi Santoso")
8. Verify "Budi Santoso" appears in the result
9. Clear the search
10. Search "EMP-002" (Employee ID of "Budi Santoso")
11. Verify "Budi Santoso" appears in the result
12. Clear the search
13. Search "Rina Kartika" (the admin who last modified "Budi Santoso")
14. Verify "Budi Santoso" appears in the result
15. Clear the search
16. Search "Fixed" (part of the Access product name "Fixed Asset")
17. Verify "Doni Pratama" appears in the result and a user without Fixed Asset access does not
18. Clear the search
19. Search "Pending"
20. Verify "Fajar Nugroho" and "Hana Melati" appear in the result, and "Gita Ayu" (Activated, no pending change) does not
21. Clear the search
22. Search "Yes"
23. Verify "Kirana Dewi" and "Laras Ayu" appear in the result
24. Clear the search
25. Search "00321" (part of the TAG code of "Doni Pratama")
26. Verify only "Doni Pratama" appears in the result
27. Clear the search

### Name sort and locale collation

28. Click the `Name` column header once
29. Verify the order is ascending alphabetically under ICU collation `en-US-x-icu`, so "budi Iskandar" can appear before "Andi Saputra" according to locale rules, not strictly after every uppercase-starting name as a binary sort would place it
30. Click the `Name` column header again
31. Verify the order becomes descending
32. Click the `Name` column header a third time
33. Verify the order returns to the default

### Filter per field

34. Open the Filter Panel, select Status "Inactive", click `[Apply Filter]`
35. Verify only rows with Status Inactive appear, including "Eka Prasetyo"
36. Click `[Clear Field]` and verify the filter resets to the default placeholder "All statuses"
37. Select Position of "Budi Santoso" ("Staff"), click `[Apply Filter]`
38. Verify only rows with that Position appear
39. Clear the filter
40. Select Division of "Budi Santoso" ("Finance"), click `[Apply Filter]`
41. Verify only rows with that Division appear
42. Clear the filter
43. Select Modified By "Rina Kartika" and "Doni Admin" together, click `[Apply Filter]`
44. Verify both "Budi Santoso" and "Citra Wulandari" appear, since Modified By combines the selected admins with OR
45. Clear the filter
46. Select a Last Update date that matches an existing change, click `[Apply Filter]`
47. Verify only rows with that Last Update date appear
48. Clear the filter
49. Select Activation "Pending Activation", click `[Apply Filter]`
50. Verify only "Fajar Nugroho" appears
51. Clear the filter
52. Select Activation "Pending Email Confirmation", click `[Apply Filter]`
53. Verify only "Hana Melati" appears, and neither "Gita Ayu" nor "Fajar Nugroho" appear
54. Clear the filter
55. Select Access "Global Settings", click `[Apply Filter]`
56. Verify only rows whose Access includes "Global Settings" appear
57. Clear the filter
58. Select Temporary User "Yes", click `[Apply Filter]`
59. Verify only "Kirana Dewi" and "Laras Ayu" appear
60. Clear the filter
61. Select the Temporary Until date of "Kirana Dewi", click `[Apply Filter]`
62. Verify only "Kirana Dewi" appears, not "Laras Ayu"
63. Clear the filter

### Sort per column

64. Click the `Active` column header once, then again, then a third time
65. Verify the 3-state cycle: Active first, then Inactive first, then the default order
66. Click the `Email` column header once, then again, then a third time
67. Verify the 3-state cycle sorts alphabetically both ways, then returns to default
68. Click the `Position` column header once
69. Verify rows with an empty Position, including "Indra Kusuma", appear at the end of the ascending order
70. Click the `Division` column header once, then again, then a third time
71. Verify the 3-state cycle sorts alphabetically both ways, then returns to default
72. Click the `Access` column header once
73. Verify "Budi Santoso" (1 Access) appears before "Doni Pratama" (2 Access), which appears before "Joko Prasetyo" (3 Access), and that users with the same Access count are tie-broken alphabetically by their first product name
74. Click the `Employee ID` column header once
75. Verify rows with an empty Employee ID, including "Indra Kusuma", appear at the end
76. Click the `Modified By` column header once
77. Verify the order follows each actor's full underlying name, not the short form shown on screen
78. Click the `Last Update` column header once
79. Verify the order is Newest First
80. Click the `Activation Status` column header once
81. Verify the order is alphabetical ("Activated", "Pending Activation", "Pending Email Confirmation")
82. Click the `Temporary User` column header once
83. Verify the order is Yes First
84. Click the `Temporary Until` column header once
85. Verify "Kirana Dewi" appears before "Laras Ayu" (closer expiry first), and rows that are not Temporary appear at the end
86. Click the `TAG` column header once
87. Verify the order is alphabetical by TAG code, and rows without a paired TAG appear at the end

### Combined Search, Filter, Sort, and Pagination

88. Search "Finance", then select Position of "Budi Santoso" ("Staff") and click `[Apply Filter]`
89. Verify the result is the precise intersection of the search and the filter, and the search keyword is not reset by applying the filter
90. Clear the filter and the search
91. Select Position "Staff" and click `[Apply Filter]`, then search "Finance"
92. Verify the filter criteria stays active in the background and the result is the precise intersection
93. Clear the filter and the search
94. With more than 15 users available, search a keyword, apply a filter, click a sort column header, and change the page size, all at once
95. Verify all 4 conditions apply together without overriding each other
96. Change the search or filter so the result becomes "No results found"
97. Release one of the active criteria
98. Verify the table automatically recovers and shows the matching data again

### Pagination

99. Change the page size to 25
100. Verify the number of rows per page matches the selected size
101. Navigate to page 2
102. Verify page 2 shows the next set of rows

### Download

103. Clear every active search and filter, click Download and select CSV
104. Verify the downloaded file is named "User-List.csv" and contains every row (fetchAll), not only the currently displayed page
105. Apply Filter Division "Finance", click Download and select CSV
106. Verify the downloaded file contains only rows with Division "Finance", matching the active filter, not the full user list
107. Clear the filter, click Download and select CSV again
108. Verify the file downloads successfully and no success toast appears
109. Click Download and select XLSX
110. Verify the downloaded file is named "User-List.xlsx"
111. Open a downloaded CSV file and inspect its cell values
112. Verify the `Active` column shows the literal text "Active" or "Inactive" (not a boolean or icon), the `Access` column shows plain product names separated by ", " without badge coloring, and an empty field (such as Position for "Indra Kusuma") shows a single hyphen "-"
113. Hide column `Email` via Setup Column, click Download and select CSV
114. Verify the downloaded file does not contain the `Email` column
115. Unhide column `Email` via Setup Column, click Download and select CSV
116. Verify the downloaded file contains the `Email` column again

## Notes

- One spec covers the whole List toolbar (Search, Filter, Sort, Pagination, Download) on the User List, all under the same Role Total Control and the same Client entity, with no modal involved, following `docs/e2e-conventions.md` section 3.
- These TC were re-selected under the hybrid rule (`docs/e2e-conventions.md` section 2): even though most of them already have frontend test case coverage with a mocked API, that mocked coverage only proves the UI renders whatever the mock returns. It cannot prove that Search, Filter, Sort, and Download actually query and return the correct rows from real data. This spec exists specifically to prove that effect against a real backend, so the overlap with the frontend layer here is intentional, not redundant.
- Setup Column itself (checking/unchecking a column, drag-reordering, pin/unpin, Reset to Default) is not covered here, because it is pure client-side rendering state that does not depend on real data and is already covered by the frontend layer. Steps 113–116 use Setup Column only as a means to reach a Download state, not as something being verified for its own sake.
- TC-GS-USER-129, 130, 202 are not part of this spec's TC yet appear to have no frontend test case coverage either (checked against `tc-user-frontend.md`, no match found). This spec does not cover them, since 202 (Filter Access single value) is exercised indirectly through step 55, and 129/130 are pure UI state. This is reported to QA as a possible frontend backlog gap, not an e2e gap.
- TC-GS-USER-466 (Access badge order inside one cell is always alphabetical) also has no frontend mapping, but it is pure rendering with no data-correctness concern, so it stays out of this spec for the same reason as Setup Column.
- TC-GS-USER-213, 214, 215, 217 (state retention: does the search box keep its text, does the sort arrow stay visible, does a checkbox selection survive) are UI memory concerns, not query-correctness concerns, and are left to the frontend layer.
- TC-GS-USER-363 (Download failing on a simulated server error) needs a mocked failure and is the frontend layer's responsibility.
- TC-GS-USER-494 is a duplicate of TC-GS-USER-496 (per `GAP-161`, already closed in the source PRD); step 113–114 cover both under TC-496's wording.
- Reading actual downloaded file bytes (steps 104, 106, 108, 110, 112, 114, 116) needs tooling support from the FE team, noted in Prerequisites.
- No data is created or destroyed by this spec. Every named user must exist before the run; none of them need cleanup beyond what the automation-dedicated environment already handles.
