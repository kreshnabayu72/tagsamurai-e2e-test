---
id: TC-FA-FATR-E2E-033-gating-mts-update
title: "Gating Manage transaction settings (Read + Update)"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [§2#r1, §2#r6, §4.1#r263, §4.8#r1, §4.8#r2, §4.8#r3, §4.8#r4, §4.8#r5, §4.8#r6, §4.8#r7, §4.8#r8, §4.8#r9, §4.8#r10, §4.8#r11, §4.8#r12, §4.8#p2, §9.11#r1, EB-AKS-5@save-changes, EB-AKS-5@add-override, EB-AKS-5@delete-override, §9.3#b1, §9.11#r7, §9.11#r10]
smoke: [§9.3#b1, §9.11#r7, §9.11#r10]
dependsOn: []
trace:
  §2#r1: [4, 7, 9, 21, 42]
  §2#r6: [2, 7, 21, 30, 31, 32, 42]
  §4.1#r263: [51, 56]
  §4.8#r1: [2, 4]
  §4.8#r2: [5, 7]
  §4.8#r3: 9
  §4.8#r4: 15
  §4.8#r5: [12, 16]
  §4.8#r6: 13
  §4.8#r7: 18
  §4.8#r8: 27
  §4.8#r9: 30
  §4.8#r10: 31
  §4.8#r11: 32
  §4.8#r12: [44, 51, 56, 60, 62, 63, 65, 69]
  §4.8#p2: [53, 58]
  §9.11#r1: 21
  EB-AKS-5@save-changes: [21, 26]
  EB-AKS-5@add-override: 42
  EB-AKS-5@delete-override: 49
  §9.3#b1: [21, 42]
  §9.11#r7: 42
  §9.11#r10: [30, 32]
anchor: [48]
coverage:
  web: automated
---
# Gating Manage transaction settings (Read + Update)

## Prerequisites
- Aktor: pemegang Global Role Manage transaction settings (Read, Update) `Maya Lestari {runId}`.
- Layar awal: Fixed Asset > Settings > Transaction Settings.
- Data:
  - DU-033-1: User `Maya Lestari {runId}`, Global Role Manage transaction settings dengan Read dan Update, bukan Total Control, tanpa Group Role Manage asset & TAG, tanpa tingkat akses Read Only, ada di entitas aktor.
  - DU-033-2: Category leaf `Alat Berat {runId}` di bawah Category induk `Aset Proyek {runId}`, semua field transaksi Inherit.
  - DU-033-3: Group `Proyek Subang {runId}`, ada di entitas aktor.
  - DU-033-4: Asset Name `Excavator PC200 {runId}`, aktif.
  - DU-033-5: Asset Name `Bulldozer D6 {runId}`, aktif.
  - DU-033-6: Aset `Bulldozer D6 - 1 {runId}` dengan Asset Name DU-033-5 dan Category `Alat Berat {runId}`, status bukan Disposed.
  - DU-033-7: override pada tab Borrow Category `Alat Berat {runId}` dengan Scope `Group`, Target `Proyek Subang {runId}`, Overridden `Max duration (30 days)`, dibuat oleh aktor lain.
  - DU-033-8: override pada tab Borrow Category `Alat Berat {runId}` dengan Scope `Asset`, Target aset DU-033-6, Overridden `Max duration (30 days)`, dibuat oleh aktor lain.
  - DU-033-11: Asset Name `Wheel Loader WA200 {runId}`, aktif.
  - DU-033-12: override pada tab Borrow Category `Alat Berat {runId}` dengan Scope `Asset Name`, Target `Wheel Loader WA200 {runId}`, Overridden `Max duration (20 days)`, dibuat oleh aktor lain.
- Kondisi:
  - Akun `Maya Lestari {runId}` aktif dan dapat dipakai masuk.

## Test Steps

### Pemegang Manage transaction settings (Read + Update) melihat halaman dan header
1. Ketik Search Sidebar Category Tree `Alat Berat {runId}`, tekan Enter
2. Verifikasi Sidebar Category Tree menampilkan `All categories` dan Category `Alat Berat {runId}`
3. Klik Category `Alat Berat {runId}`
4. Verifikasi tab `Borrow`, `Assign`, `Transfer`, dan `Disposal` tampil
5. Verifikasi tombol `[Export rules]` tampil dan aktif
6. Klik `[Export rules]`
7. Verifikasi berkas aturan terunduh langsung tanpa dialog
8. Klik ikon `Changelog` pada header halaman
9. Verifikasi dialog `Changelog: Transaction Settings` tampil
10. Klik `✕` pada dialog Changelog

### Pemegang Update mengubah dan menyimpan setting Category
11. Klik tab `Borrow`
12. Verifikasi tombol `[Set own value]` tampil pada field `Max duration`
13. Verifikasi tombol `[Reset to Default]` tampil dan aktif
14. Klik `[Set own value]` pada field `Max duration`
15. Verifikasi kontrol field `Max duration` aktif
16. Verifikasi tombol `[Reset to inherit]` tampil pada field `Max duration`
17. Ganti isi field `Max duration` dengan `16`
18. Verifikasi tombol `[Save]` tampil dan aktif
19. Klik `[Save]`
20. Klik `[Save]` pada dialog Save Changes
21. Verifikasi toast `Success, settings have been saved.` tampil
22. Muat ulang halaman
23. Ketik Search Sidebar Category Tree `Alat Berat {runId}`, tekan Enter
24. Klik Category `Alat Berat {runId}`
25. Klik tab `Borrow`
26. Verifikasi field `Max duration` bernilai `16`

### Pemegang Update menambah override Asset Name dan melihat Scope lain disabled
27. Verifikasi tombol `[+ Override]` tampil dan aktif
28. Klik `[+ Override]`
29. Klik pilihan Scope
30. Verifikasi opsi Scope `Group` disabled
31. Verifikasi opsi Scope `Asset Name` tampil dan aktif
32. Verifikasi opsi Scope `Asset` disabled
33. Pilih Scope `Asset Name`
34. Klik `[Select Asset Name]`
35. Ketik Search `Excavator PC200 {runId}`, tekan Enter
36. Centang baris `Excavator PC200 {runId}`
37. Klik `[Select]`
38. Pilih Field `Max duration`
39. Isi Value `10`
40. Klik `[Submit]`
41. Ketik Search tabel Overrides `Excavator PC200 {runId}`, tekan Enter
42. Verifikasi baris dengan Scope `Asset Name`, Target `Excavator PC200 {runId}`, dan Overridden `Max duration (10 days)` tampil

### Pemegang Update menghapus override Asset Name
43. Klik menu `⋯` pada baris `Excavator PC200 {runId}`
44. Verifikasi item `Delete` aktif untuk baris override dengan Scope `Asset Name`
45. Klik item `Delete`
46. Klik `[Delete]` pada dialog Delete Override
47. Ganti isi kotak search tabel Overrides dengan `{runId}`, tekan Enter
48. Verifikasi baris dengan Scope `Group` dan Target `Proyek Subang {runId}` tampil
49. Verifikasi baris dengan Target `Excavator PC200 {runId}` tidak tampil di tabel Overrides

### Delete override Group dan Asset di luar hak pemegang Update disabled
50. Klik menu `⋯` pada baris `Proyek Subang {runId}`
51. Verifikasi item `Delete` disabled untuk baris override dengan Scope `Group`
52. Arahkan kursor ke item `Delete`
53. Verifikasi alasan `This override is outside your scope.` tersampaikan pada item `Delete` yang disabled
54. Tekan Esc untuk menutup menu baris
55. Klik menu `⋯` pada baris `Bulldozer D6 - 1 {runId}`
56. Verifikasi item `Delete` disabled untuk baris override dengan Scope `Asset`
57. Arahkan kursor ke item `Delete`
58. Verifikasi alasan `This override is outside your scope.` tersampaikan pada item `Delete` yang disabled
59. Tekan Esc untuk menutup menu baris

### Checkbox seleksi baris di luar hak pemegang Update disabled dengan alasan
60. Verifikasi checkbox seleksi pada baris `Proyek Subang {runId}` disabled[^drift-1]
61. Arahkan kursor ke checkbox seleksi pada baris `Proyek Subang {runId}`
62. Verifikasi alasan `You don't have permission to do this.` tersampaikan pada checkbox seleksi yang disabled[^drift-1]
63. Verifikasi checkbox seleksi pada baris `Bulldozer D6 - 1 {runId}` disabled[^drift-1]
64. Arahkan kursor ke checkbox seleksi pada baris `Bulldozer D6 - 1 {runId}`
65. Verifikasi alasan `You don't have permission to do this.` tersampaikan pada checkbox seleksi yang disabled[^drift-1]

### Delete bulk untuk override Asset Name aktif bagi pemegang Update
66. Ketik Search tabel Overrides `Wheel Loader WA200 {runId}`, tekan Enter
67. Centang baris `Wheel Loader WA200 {runId}`
68. Klik tombol aksi bulk pada toolbar tabel Overrides
69. Verifikasi aksi bulk `Delete` aktif
70. Tekan Esc untuk menutup menu aksi bulk

[^drift-1]: Drift PRD vs foundation. PRD §4.8 (sel Delete baris dan bulk) dan §4.1 DO-15: baris di luar hak dapat dicentang lalu aksi bulk `Delete` disabled dengan tooltip tersendiri. foundation `functions/entity-isolation.md` §18.4 Aturan kolom 4: checkbox seleksi pada baris yang capability tulisnya tidak cukup Disabled 🔖 dengan tooltip `You don't have permission to do this.`, sehingga baris itu tidak bisa dicentang. Diasersi: foundation, karena checkbox seleksi tabel adalah pola bersama (SB-4).
