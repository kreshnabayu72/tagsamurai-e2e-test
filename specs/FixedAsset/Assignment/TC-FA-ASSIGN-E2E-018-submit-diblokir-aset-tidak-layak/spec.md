---
id: TC-FA-ASSIGN-E2E-018-submit-diblokir-aset-tidak-layak
title: "Submit ditolak karena aset tidak layak dan tanda di baris"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["EC-ASG-05", "EC-ASG-50", "S-ASG-13"]
smoke: []
dependsOn: []
trace:
  "EC-ASG-05": [4, 9]
  "EC-ASG-50": [14, 16, 20, 23, 25, 29]
  "S-ASG-13": [4, 6]
anchor: []
coverage:
  web: automated
---

# Submit ditolak karena aset tidak layak dan tanda di baris

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office`.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-018-1: Aset `Laptop Dell Latitude 5420 {runId}`, Category `Laptop`, Group `Head Office`, Condition `Damaged`.
  - DU-018-2: Aset `Monitor LG 24 {runId}`, Category `Monitor`, Group `Head Office`, Custody `Available`, Condition `Normal`.
  - DU-018-3: Aset `Printer HP M404 {runId}`, Category `Printer`, Group `Head Office`, Lifecycle `Deleted`.
  - DU-018-4: Draft Assignee `Budi Setiawan`, Assignee Type `Employee`, Group `Head Office`, berisi `Laptop Dell Latitude 5420 {runId}` dan `Monitor LG 24 {runId}` dengan Purpose `Kerja harian`.
  - DU-018-5: Draft Assignee `Budi Setiawan`, Assignee Type `Employee`, Group `Head Office`, berisi `Printer HP M404 {runId}` dengan Purpose `Kerja harian`.
  - DU-018-6: Assignee Employee `Budi Setiawan` (email `budi.setiawan@example.com`, Position `Analyst`, Division `Finance`, Home Group `Branch Surabaya`), karyawan aktif dengan akun login.
  - DU-018-7: Aset `Scanner Zebra DS2208 {runId}`, Category `Scanner`, Group `Head Office`, Lifecycle `Disposed`.
  - DU-018-8: Draft Assignee `Budi Setiawan`, Assignee Type `Employee`, Group `Head Office`, berisi `Scanner Zebra DS2208 {runId}` dengan Purpose `Kerja harian`.
- Kondisi:
  - Feature Suite Assignment bernilai `Full`.
  - Aset `Laptop Dell Latitude 5420 {runId}` berkondisi Damaged dan aset `Printer HP M404 {runId}` sudah dihapus (Deleted) sesudah masing-masing Draft disimpan, dan aset `Scanner Zebra DS2208 {runId}` berstatus Disposed sesudah Draft-nya disimpan.

## Test Steps

### Aset Damaged di Draft ditandai dan Submit diblokir
1. Klik tab `Drafts`
2. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
3. Klik Assignee `Budi Setiawan` pada baris Draft
4. Verifikasi baris aset `Laptop Dell Latitude 5420 {runId}` ditandai ikon ⚠ dengan caption `This asset can no longer be assigned.`
5. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
6. Verifikasi menu baris menyediakan aksi `Remove from List`
7. Tekan Esc untuk menutup menu baris
8. Klik `[Submit]`
9. Verifikasi caption `Remove the unavailable assets to continue.` tampil di atas deretan tombol
10. Klik `[Cancel]` (form belum diubah, tanpa dialog Unsaved Changes)

### Aset dihapus di Draft ditandai dan Draft tetap tersimpan
11. Klik tab `Drafts`
12. Ganti isi kotak search dengan `Printer HP M404 {runId}`, tekan Enter
13. Klik Assignee `Budi Setiawan` pada baris Draft
14. Verifikasi baris aset `Printer HP M404 {runId}` ditandai ikon ⚠ dengan caption `This asset can no longer be assigned.`
15. Klik `⋯` pada baris `Printer HP M404 {runId}`
16. Verifikasi menu baris menyediakan aksi `Remove from List`
17. Tekan Esc untuk menutup menu baris
18. Klik `[Cancel]` (form belum diubah, tanpa dialog Unsaved Changes)
19. Klik tab `Drafts`
20. Verifikasi Draft berisi `Printer HP M404 {runId}` tetap tampil di tab Drafts

### Aset Disposed di Draft ditandai dan Draft tetap tersimpan
21. Ganti isi kotak search dengan `Scanner Zebra DS2208 {runId}`, tekan Enter
22. Klik Assignee `Budi Setiawan` pada baris Draft
23. Verifikasi baris aset `Scanner Zebra DS2208 {runId}` ditandai ikon ⚠ dengan caption `This asset can no longer be assigned.`
24. Klik `⋯` pada baris `Scanner Zebra DS2208 {runId}`
25. Verifikasi menu baris menyediakan aksi `Remove from List`
26. Tekan Esc untuk menutup menu baris
27. Klik `[Cancel]` (form belum diubah, tanpa dialog Unsaved Changes)
28. Klik tab `Drafts`
29. Verifikasi Draft berisi `Scanner Zebra DS2208 {runId}` tetap tampil di tab Drafts
