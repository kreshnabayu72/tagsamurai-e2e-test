---
id: TC-FA-ASSIGN-E2E-053-assign-dari-asset-list-dan-quick-action-dep-asset-list
title: "Assign dari Asset List dan Quick Action membuka form dengan aset terisi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.2.13#b1", "§4.2.13#b2", "§4.1#r21"]
smoke: []
dependsOn: ["Asset List: aksi Assign, Add to Assignment Draft, dan Quick Action Assign"]
trace:
  "§4.2.13#b1": [4, 8, 9, 19, 28, 31, 35, 46, 47]
  "§4.2.13#b2": [39, 40]
  "§4.1#r21": 37
anchor: []
coverage:
  web: automated
---

# Assign dari Asset List dan Quick Action membuka form dengan aset terisi

## Prerequisites
- Aktor: Aktor Assignment (Asset Admin pada Group aset DU-053-1, DU-053-2, DU-053-5, dan DU-053-6).
- Layar awal: Asset List.
- Data:
  - DU-053-1: Aset `Laptop Lenovo ThinkPad T14 {runId}`, Custody `Available`, Condition `Normal`, Group `Head Office`.
  - DU-053-2: Aset `Monitor Dell P2422H {runId}`, Custody `Available`, Condition `Normal`, Group `Head Office`.
  - DU-053-3: Karyawan `Budi Santoso {runId}`, Email `budi.santoso053@example.com`, Status `Active`, Activation Status `Activated`, ber-akun login.
  - DU-053-4: Karyawan `Sari Dewi {runId}`, Email `sari.dewi053@example.com`, Status `Active`, Activation Status `Activated`, ber-akun login, belum punya Draft Assignment.
  - DU-053-5: Aset `Printer Epson L3250 {runId}`, Custody `Available`, Condition `Normal`, Group `Head Office`.
  - DU-053-6: Aset `Kursi Kerja Ergonomis {n} {runId}` sebanyak 4 aset, Custody `Available`, Condition `Normal`, Group `Head Office`.
- Kondisi:
  - Max assets per assignee bernilai `5`.

## Test Steps

### Assign dari baris Asset List membuka form dengan Assignee dan aset terisi
1. Ketik Search `Laptop Lenovo ThinkPad T14 {runId}`, tekan Enter
2. Klik `⋯` pada baris `Laptop Lenovo ThinkPad T14 {runId}`
3. Klik `Assign`
4. Verifikasi dialog Select Assignee tampil dengan baris `Budi Santoso {runId}` berstatus `Can be assigned`
5. Ketik Search `Budi Santoso {runId}`, tekan Enter
6. Pilih baris `Budi Santoso {runId}`
7. Klik `[Select]`
8. Verifikasi halaman Assignment Request terbuka dengan Assignee `Budi Santoso {runId}`
9. Verifikasi aset `Laptop Lenovo ThinkPad T14 {runId}` ada di tabel aset form
10. Klik `[Cancel]` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes

### Bulk Assign dari Asset List membawa semua aset terpilih ke form
11. Buka halaman Asset List
12. Ketik Search `{runId}`, tekan Enter
13. Centang baris `Laptop Lenovo ThinkPad T14 {runId}`
14. Centang baris `Monitor Dell P2422H {runId}`
15. Klik `Assign` pada menu aksi bulk
16. Ketik Search `Budi Santoso {runId}`, tekan Enter
17. Pilih baris `Budi Santoso {runId}`
18. Klik `[Select]`
19. Verifikasi form Assignment Request terbuka berisi aset `Laptop Lenovo ThinkPad T14 {runId}` dan `Monitor Dell P2422H {runId}` dengan Assignee `Budi Santoso {runId}`
20. Klik `[Cancel]` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes

### Add to Assignment Draft untuk Assignee tanpa Draft langsung membuat Draft baru
21. Buka halaman Asset List
22. Ketik Search `Printer Epson L3250 {runId}`, tekan Enter
23. Klik `⋯` pada baris `Printer Epson L3250 {runId}`
24. Klik `Add to Assignment Draft`
25. Ketik Search `Sari Dewi {runId}`, tekan Enter
26. Pilih baris `Sari Dewi {runId}`
27. Klik `[Select]`
28. Verifikasi toast `Success, 1 asset has been added to the draft.` tampil setelah Assignee dipilih
29. Buka tab Drafts di halaman Transactions > Assignment
30. Ketik Search `Sari Dewi {runId}`, tekan Enter
31. Verifikasi baris Draft untuk Assignee `Sari Dewi {runId}` tampil
32. Buka halaman Asset List
33. Ketik Search `Printer Epson L3250 {runId}`, tekan Enter
34. Klik `⋯` pada baris `Printer Epson L3250 {runId}`
35. Verifikasi opsi `Assign` tetap tampil pada menu baris aset yang sudah masuk Draft

### Quick Action Assign membuka form Assignment Request kosong
36. Klik `Quick Action` pada navbar
37. Verifikasi item `Assign` tampil pada menu Quick Action
38. Klik `Assign`
39. Verifikasi tombol `[Select Assignee]` tampil pada form Assignment Request karena Assignee belum dipilih
40. Verifikasi tabel aset form menampilkan empty state `No assets added`

### Bulk Assign melebihi Max assets per assignee menandai Assignee Blocked di Select Assignee
41. Buka halaman Asset List
42. Ketik Search `{runId}`, tekan Enter
43. Centang checkbox header kolom Checkbox
44. Klik `Assign` pada menu aksi bulk
45. Ketik Search `Budi Santoso {runId}`, tekan Enter
46. Verifikasi baris `Budi Santoso {runId}` berstatus `Blocked` pada dialog Select Assignee
47. Verifikasi alasan `[Assignee] can hold up to 5 assets at a time.` tersampaikan pada baris `Budi Santoso {runId}` dengan `[Assignee]` berisi `Budi Santoso {runId}`
48. Klik `[Cancel]` pada dialog Select Assignee
