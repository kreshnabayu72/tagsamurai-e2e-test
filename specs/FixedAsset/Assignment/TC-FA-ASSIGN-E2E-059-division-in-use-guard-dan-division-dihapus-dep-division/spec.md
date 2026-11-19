---
id: TC-FA-ASSIGN-E2E-059-division-in-use-guard-dan-division-dihapus-dep-division
title: "Division yang dipakai ASG aktif tidak dapat dihapus"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EC-ASG-35, ASSIGN-LOGIC-16af, ASSIGN-LOGIC-16ag, ASSIGN-LOGIC-16ar, ASSIGN-LOGIC-16ah]
smoke: []
dependsOn: ["Division: hapus Division"]
trace:
  EC-ASG-35: [5, 10, 15]
  ASSIGN-LOGIC-16af: [5, 10, 15, 21, 27, 38]
  ASSIGN-LOGIC-16ag: [44, 45]
  ASSIGN-LOGIC-16ar: [47, 49]
  ASSIGN-LOGIC-16ah: 31
anchor: [17, 23, 34, 43]
coverage:
  web: automated
---
# Division yang dipakai ASG aktif tidak dapat dihapus

## Prerequisites
- Aktor: Total Control `Fajar Nugroho {runId}` (DU-059-1).
- Layar awal: Settings > Division.
- Data:
  - DU-059-1: Karyawan `Fajar Nugroho {runId}`, role Total Control, Status `Active`.
  - DU-059-2: Karyawan `Hendra Kusuma {runId}`, Status `Active`, Activation Status `Activated`, ber-akun login, PIC semua Division di bawah ini.
  - DU-059-3: Division `Logistik {runId}`, Code `LOGS`, dipakai satu ASG `Waiting for Approval` (DU-059-9).
  - DU-059-4: Division `Pemasaran {runId}`, Code `PEMS`, dipakai satu ASG `Waiting for Handover` (DU-059-10).
  - DU-059-5: Division `Keuangan {runId}`, Code `KEUS`, dipakai satu ASG `Assigned` (DU-059-11).
  - DU-059-6: Division `Arsip {runId}`, Code `ARSS`, tidak dipakai ASG maupun Draft mana pun.
  - DU-059-7: Division `Gudang {runId}`, Code `GUDS`, hanya dipakai satu ASG selesai berstatus `Unassigned` (DU-059-12).
  - DU-059-8: Division `Produksi {runId}`, Code `PRDS`, hanya menjadi Assignee satu Draft (DU-059-13).
  - DU-059-9: ASG `Waiting for Approval` untuk Assignee Division `Logistik {runId}`, PIC `Hendra Kusuma {runId}`, berisi aset `Rak Server Dell {runId}`.
  - DU-059-10: ASG `Waiting for Handover` untuk Assignee Division `Pemasaran {runId}`, PIC `Hendra Kusuma {runId}`, berisi aset `Kamera DSLR Nikon D750 {runId}`.
  - DU-059-11: ASG `Assigned` untuk Assignee Division `Keuangan {runId}`, PIC `Hendra Kusuma {runId}`, berisi aset `Mesin Hitung Uang Glory {runId}`.
  - DU-059-12: ASG `Unassigned` untuk Assignee Division `Gudang {runId}`, PIC `Hendra Kusuma {runId}`, berisi aset `Forklift Mini Toyota {runId}`.
  - DU-059-13: Draft Assignee Division `Produksi {runId}` dengan PIC `Hendra Kusuma {runId}`, berisi aset `Mesin Bor Bosch GSB {runId}` dengan Purpose `Perawatan lini produksi`.

## Test Steps

### Division yang dipakai ASG Waiting for Approval tidak dapat dihapus
1. Ketik Search `Logistik {runId}`, tekan Enter
2. Klik `⋯` pada baris Division `Logistik {runId}`
3. Klik `Delete`
4. Konfirmasi penghapusan pada dialog hapus Division
5. Verifikasi penghapusan Division `Logistik {runId}` ditolak oleh in-use guard dan Division tetap tampil di daftar karena dipakai ASG `Waiting for Approval`

### Division yang dipakai ASG Waiting for Handover tidak dapat dihapus
6. Ketik Search `Pemasaran {runId}`, tekan Enter
7. Klik `⋯` pada baris Division `Pemasaran {runId}`
8. Klik `Delete`
9. Konfirmasi penghapusan pada dialog hapus Division
10. Verifikasi penghapusan Division `Pemasaran {runId}` ditolak oleh in-use guard dan Division tetap tampil di daftar karena dipakai ASG `Waiting for Handover`

### Division yang dipakai ASG Assigned tidak dapat dihapus
11. Ketik Search `Keuangan {runId}`, tekan Enter
12. Klik `⋯` pada baris Division `Keuangan {runId}`
13. Klik `Delete`
14. Konfirmasi penghapusan pada dialog hapus Division
15. Verifikasi penghapusan Division `Keuangan {runId}` ditolak oleh in-use guard dan Division tetap tampil di daftar karena dipakai ASG `Assigned`

### Division yang tidak dipakai dapat dihapus
16. Ganti isi kotak search dengan `Arsip {runId}`, tekan Enter
17. Verifikasi baris Division `Arsip {runId}` tampil di daftar sebelum dihapus
18. Klik `⋯` pada baris Division `Arsip {runId}`
19. Klik `Delete`
20. Konfirmasi penghapusan pada dialog hapus Division
21. Verifikasi Division `Arsip {runId}` tidak tampil lagi di daftar

### Division yang hanya dipakai baris selesai dapat dihapus dan namanya tetap tampil dari log
22. Ganti isi kotak search dengan `Gudang {runId}`, tekan Enter
23. Verifikasi baris Division `Gudang {runId}` tampil di daftar sebelum dihapus
24. Klik `⋯` pada baris Division `Gudang {runId}`
25. Klik `Delete`
26. Konfirmasi penghapusan pada dialog hapus Division
27. Verifikasi Division `Gudang {runId}` tidak tampil lagi di daftar
28. Buka halaman Transactions > Assignment
29. Buka tab History
30. Ketik Search `Forklift Mini Toyota {runId}`, tekan Enter
31. Verifikasi baris riwayat aset `Forklift Mini Toyota {runId}` tetap menampilkan nama Division `Gudang {runId}` sebagai Assignee

### Division yang hanya menjadi Assignee Draft dapat dihapus dan Draft menunggu Assignee baru
32. Buka halaman Settings > Division
33. Ketik Search `Produksi {runId}`, tekan Enter
34. Verifikasi baris Division `Produksi {runId}` tampil di daftar sebelum dihapus
35. Klik `⋯` pada baris Division `Produksi {runId}`
36. Klik `Delete`
37. Konfirmasi penghapusan pada dialog hapus Division
38. Verifikasi Division `Produksi {runId}` tidak tampil lagi di daftar
39. Buka halaman Transactions > Assignment
40. Buka tab Drafts
41. Ketik Search `Mesin Bor Bosch GSB {runId}`, tekan Enter
42. Klik ikon `Edit` pada baris Draft untuk aset `Mesin Bor Bosch GSB {runId}`
43. Verifikasi aset `Mesin Bor Bosch GSB {runId}` ada di tabel aset Draft
44. Verifikasi field Assignee kosong dan tombol `[Select Assignee]` tampil pada Draft untuk aset `Mesin Bor Bosch GSB {runId}`
45. Verifikasi pesan `This division was deleted. Pick another assignee.` tampil pada field Assignee
46. Klik `[Save Draft]`
47. Verifikasi pesan `You must pick an assignee` tampil dan Draft belum tersimpan
48. Klik `[Submit]`
49. Verifikasi caption `Please fill in all required fields.` tampil dan pengajuan belum dikirim
50. Klik `[Cancel]` pada form Draft yang belum diubah
