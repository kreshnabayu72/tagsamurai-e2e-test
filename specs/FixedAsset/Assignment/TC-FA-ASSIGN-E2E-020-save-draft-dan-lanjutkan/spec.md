---
id: TC-FA-ASSIGN-E2E-020-save-draft-dan-lanjutkan
title: "Save Draft, edit Draft, dan Submit Draft"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["F-ASSIGN-01", "TS-ASG-01", "TS-ASG-28", "EB-FRM-9", "§4.4#r4"]
smoke: []
dependsOn: []
trace:
  "F-ASSIGN-01": [17, 22]
  "TS-ASG-01": [14, 35]
  "TS-ASG-28": 29
  "EB-FRM-9": [37, 38, 41, 42, 43, 44, 49]
  "§4.4#r4": [14, 22]
anchor: []
coverage:
  web: automated
---

# Save Draft, edit Draft, dan Submit Draft

## Prerequisites
- Aktor: Asset Admin (Aktor Assignment) dengan cakupan Group `Head Office`.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-020-1: Aset `Laptop Dell Latitude 5420 {runId}`, Category `Laptop`, Group `Head Office`, Custody `Available`, Condition `Normal`.
  - DU-020-2: Aset `Monitor LG 24 {runId}`, Category `Monitor`, Group `Head Office`, Custody `Available`, Condition `Normal`.
  - DU-020-3: Assignee Employee `Budi Santoso` (email `budi.santoso@example.com`, Position `Staff`, Division `IT`, Home Group `Head Office`), karyawan aktif dengan akun login.
  - DU-020-4: Draft yang disimpan spec ini untuk Assignee `Budi Santoso`, Assignee Type `Employee`, Group `Head Office`, berisi `Laptop Dell Latitude 5420 {runId}` dengan Purpose `Kerja harian` dan `Monitor LG 24 {runId}` dengan Purpose `Presentasi`.
  - DU-020-5: Purpose pengganti baris `Laptop Dell Latitude 5420 {runId}` adalah `Kerja lapangan`.
  - Draft berisi `2` aset.
- Kondisi:
  - Feature Suite Assignment bernilai `Full`.

## Test Steps

### Save Draft menyimpan tanpa mengunci aset
1. Klik `[+ Assign]`
2. Klik pilihan `Employee`
3. Klik `[Select Assignee]`
4. Pilih baris `Budi Santoso` pada dialog Select Assignee
5. Klik `[Select]`
6. Klik `[+ Asset]`
7. Ketik Search `{runId}`, tekan Enter
8. Centang baris `Laptop Dell Latitude 5420 {runId}`
9. Centang baris `Monitor LG 24 {runId}`
10. Klik `[Select]`
11. Isi Purpose baris `Laptop Dell Latitude 5420 {runId}` dengan `Kerja harian`
12. Isi Purpose baris `Monitor LG 24 {runId}` dengan `Presentasi`
13. Klik `[Save Draft]`
14. Verifikasi toast `Success, assignment has been saved as draft.` tampil setelah Draft baru disimpan

### Draft tampil di tab Drafts dan aset belum terkunci
15. Klik tab `Drafts`
16. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
17. Verifikasi baris Draft dengan Assignee `Budi Santoso`, Total Asset `2`, dan Origin `New` tampil di tab Drafts
18. Klik `[+ Assign]`
19. Klik pilihan `Employee`
20. Klik `[+ Asset]`
21. Ketik Search `{runId}`, tekan Enter
22. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` dan `Monitor LG 24 {runId}` tetap tampil pada dialog Select Asset
23. Klik `[Cancel]` pada dialog Select Asset
24. Klik `[Cancel]` pada form (form belum diubah, tanpa dialog Unsaved Changes)

### Edit Draft: simpan tanpa perubahan lalu ubah satu Purpose
25. Klik tab `Drafts`
26. Ganti isi kotak search dengan `Laptop Dell Latitude 5420 {runId}`, tekan Enter
27. Klik Assignee `Budi Santoso` pada baris Draft
28. Klik `[Save Draft]`
29. Verifikasi toast `No changes to save.` tampil
30. Klik tab `Drafts`
31. Ganti isi kotak search dengan `Laptop Dell Latitude 5420 {runId}`, tekan Enter
32. Klik Assignee `Budi Santoso` pada baris Draft
33. Ganti isi Purpose baris `Laptop Dell Latitude 5420 {runId}` dengan `Kerja lapangan`
34. Klik `[Save Draft]`
35. Verifikasi toast `Success, assignment has been saved as draft.` tampil setelah perubahan Purpose disimpan
36. Muat ulang halaman
37. Verifikasi Purpose baris `Laptop Dell Latitude 5420 {runId}` `Kerja lapangan`
38. Verifikasi Purpose baris `Monitor LG 24 {runId}` tetap `Presentasi`

### Validasi Submit gagal tidak mengubah Draft tersimpan
39. Kosongkan Purpose baris `Monitor LG 24 {runId}`
40. Klik `[Submit]`
41. Verifikasi caption `Please fill in all required fields.` tampil di atas deretan tombol
42. Verifikasi error `Purpose must not be empty` tampil di bawah Purpose baris `Monitor LG 24 {runId}`
43. Verifikasi form Assignment Request tetap terbuka
44. Verifikasi tidak ada toast sukses yang tampil
45. Klik `[Cancel]` pada form
46. Klik `[Leave]` pada dialog Unsaved Changes
47. Ganti isi kotak search dengan `Laptop Dell Latitude 5420 {runId}`, tekan Enter
48. Klik Assignee `Budi Santoso` pada baris Draft
49. Verifikasi Purpose baris `Monitor LG 24 {runId}` tetap `Presentasi`
