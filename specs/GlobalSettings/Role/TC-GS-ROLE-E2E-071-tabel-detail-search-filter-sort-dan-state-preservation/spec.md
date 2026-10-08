---
id: TC-GS-ROLE-E2E-071-tabel-detail-search-filter-sort-dan-state-preservation
title: "Tabel Halaman Detail: Pencarian, Filter Panel, Pengurutan Kolom Data, dan State Preservation Back"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-186
  - TC-GS-ROLE-187
  - TC-GS-ROLE-188
  - TC-GS-ROLE-189
  - TC-GS-ROLE-190
  - TC-GS-ROLE-191
  - TC-GS-ROLE-195
coverage:
  web: automated
---

# Tabel Halaman Detail: Pencarian, Filter Panel, Pengurutan Kolom Data, dan State Preservation Back

## Prerequisites

- Login sebagai Total Control
- Data Uji: Detail Manage user and role
- Setup Hook: beforeEach: navigateTo(Detail)
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > System > Detail "Manage TAG"
- Detail berisi ≥4 user dengan Position/Division berbeda
- User berada di Global Settings > Role & Permission > System

## Test Steps

### Search Detail berdasarkan Name, Position, Division (TC-GS-ROLE-186)

1. Klik Search: amati placeholder
2. Search "PRATAMA" + Enter
3. Search "staf" + Enter
4. Search "it" + Enter
5. Verifikasi Placeholder "Search name..."
6. Verifikasi Name: Doni Pratama cocok
7. Verifikasi Position: baris Staff/Finance Staff cocok
8. Verifikasi Division: baris Division IT cocok

### Search Detail tidak mencocokkan kolom CRUD dan Temporary Until (TC-GS-ROLE-187)

9. Search "Update" + Enter
10. Search tanggal Temporary Until salah satu user + Enter
11. Verifikasi "No results found" untuk kedua keyword

### Search Detail kolom Activation Status, Temporary User, TAG, dan Custom Field (TC-GS-ROLE-188)

12. Search "TG-00451" + Enter (kolom TAG default Hidden)
13. Tampilkan kolom Activation Status, Temporary User, TAG, Region via Setup Column > Save
14. Search "Pending" + Enter
15. Search "Yes" + Enter
16. Search "TG-00451" + Enter
17. Search "Bandung" + Enter
18. Verifikasi Langkah 1: "No results found"
19. Verifikasi Activation Status: keyword "Pending" menampilkan Rudi Hartono (Pending Activation)
20. Verifikasi Temporary User: keyword "Yes" menampilkan user temporary
21. Verifikasi TAG: baris Ahmad Fauzi cocok
22. Verifikasi [Custom Field aktif] Region: baris user Region Bandung cocok

### Screening Filter Panel Detail (TC-GS-ROLE-189)

23. Klik Filter
24. Screening field
25. Verifikasi Position → "All positions"; Division → "All divisions"; Activation Status → "All statuses"; Temporary User → "All options" (multi-select searchable); Temporary Until → "Select date" (date range picker); [Custom Field aktif] sesuai tipe
26. Verifikasi Tidak ada field Status, Modified By, Last Updated

### Filter Detail per field dan kombinasi (TC-GS-ROLE-190)

27. Filter Position "Staff" → Apply → catat → Clear
28. Filter Division "IT" → Apply → Clear
29. Filter Activation Status "Activated" → Apply → Clear
30. Filter Temporary User "No" → Apply → Clear
31. Filter Temporary Until rentang tertentu → Apply → Clear
32. Filter Division IT + Activation Status Activated → Apply → Clear
33. Filter [Custom Field aktif] Region "Bandung" → Apply
34. Verifikasi Position: hanya Staff
35. Verifikasi Division: hanya IT
36. Verifikasi Activation Status: hanya Activated
37. Verifikasi Temporary User: hanya No
38. Verifikasi Temporary Until: hanya tanggal di rentang
39. Verifikasi Kombinasi: irisan IT ∩ Activated
40. Verifikasi Region: hanya user Region Bandung

### Sort Detail per kolom data dan kolom CRUD tidak sortable (TC-GS-ROLE-191)

41. Klik header Name 3 kali
42. Klik header Position 3 kali
43. Klik header Division 3 kali
44. Tampilkan Activation Status, Temporary User, Temporary Until, TAG, Region via Setup Column > Save; klik header tiap kolom itu 3 kali
45. Hover header Read dan Update
46. Buka Detail "Manage user and role", hover header Create dan Delete
47. Verifikasi Name: A-Z / Z-A / default
48. Verifikasi Position: A-Z / Z-A / default; Default User (—) selalu di akhir untuk kedua arah
49. Verifikasi Division: A-Z / Z-A / default; Default User (—) selalu di akhir untuk kedua arah
50. Verifikasi Activation Status: A-Z / Z-A / default
51. Verifikasi Temporary User: Yes First / No First / default
52. Verifikasi Temporary Until: klik 1 Oldest First, klik 2 Newest First, klik 3 default; kosong selalu di akhir untuk kedua arah
53. Verifikasi TAG: A-Z by TAG code / Z-A / default; kosong selalu di akhir untuk kedua arah
54. Verifikasi Region: A-Z by badge label / Z-A / default
55. Verifikasi Header kolom CRUD tanpa ikon sort: Read dan Update (Manage TAG), Create dan Delete (Manage user and role)

### Back dari Detail mempertahankan Search Tab System (TC-GS-ROLE-195)

56. Search "manage" + Enter
57. Klik Role Name "Manage TAG"
58. Klik browser Back
59. Verifikasi Tab System masih menampilkan keyword "manage" dan hasilnya

## Notes

- Memvalidasi alur skenario "Tabel Halaman Detail: Pencarian, Filter Panel, Pengurutan Kolom Data, dan State Preservation Back".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.1.4; global-settings/role/PRD/role.md §4.2 Page: Detail; global-settings/role/PRD/role.md §5; foundation/process/prd-process/prd-conventions.md §27.1c.
- Sumber pemetaan test case granular: TC-GS-ROLE-186, TC-GS-ROLE-187, TC-GS-ROLE-188, TC-GS-ROLE-189, TC-GS-ROLE-190, TC-GS-ROLE-191, TC-GS-ROLE-195.
