---
id: TC-FA-GRP-E2E-094-wizard-cancel-unsaved-klik-total-asset-user-dan-server-menolak-seleksi-d-23
title: "Wizard: [Cancel] Tanpa dan Dengan Perubahan (Unsaved Changes), Klik Total Asset/Total User Membuka Detail Group, dan Server Menolak Seleksi Melebihi Cap atau Kosong (Dialog D-23)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-308
  - TC-FA-GRP-309
  - TC-FA-GRP-948
  - TC-FA-GRP-965
  - TC-FA-GRP-966
coverage:
  web: automated
---

# Wizard: [Cancel] Tanpa dan Dengan Perubahan (Unsaved Changes), Klik Total Asset/Total User Membuka Detail Group, dan Server Menolak Seleksi Melebihi Cap atau Kosong (Dialog D-23)

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control client Wizard (Pre-setup No 8: plan dijadwalkan downgrade Professional ke Growth, cap 3, T-30 berjalan, client punya 6 group; email dan `Spectra.env.FA_WIZ_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`): enam group `Head Office`, `Warehouse A` (24 aset aktif), `Branch Office` (0 aset), `Warehouse B`, `Disposal Yard`, dan `Global HQ`, dibuat berurutan (urutan pembuatan tercatat). Seleksi Wizard tersimpan dikosongkan dan status belum pernah submit direset oleh hook `before` lewat fixture BE (disediakan tim FE/BE).
- State tenant (kelas h): plan dijadwalkan downgrade. Hook `after` memulihkan plan terjadwal, seleksi tersimpan, dan status Excess lewat fixture BE (disediakan tim FE/BE). Hook uji handler plan-efektif pada T-0 (pemicu, bukan objek uji) disediakan tim FE/BE tanpa endpoint karangan. Suite berjalan serial.
- Intercept request [Save Selection] (TC-965 dan TC-966): isi request diubah di atas backend nyata supaya server menerima seleksi melebihi cap (4 group) atau kosong (0 group) dan membalas 422; ini pemicu state UI (P-2), bukan objek uji. Nama endpoint tidak disebut TC, PRD, atau LLD (APISpec kosong); ditentukan tim FE. Intercept dilepas segera setelah pemicu selesai (S-09).
- Pembacaan seleksi tersimpan (kosong) lewat fixture BE (disediakan tim FE/BE).

## Test Steps

### TC-FA-GRP-308: [Cancel] tanpa perubahan

1. Buka Wizard Reconciliation > Step Group Consolidation
2. Klik [Cancel] tanpa mencentang apa pun
3. Verifikasi step langsung tertutup tanpa dialog
4. Buka Wizard Reconciliation > Step Group Consolidation
5. Verifikasi seluruh checkbox unchecked (tidak ada seleksi tersimpan atau berubah)

### TC-FA-GRP-309: [Cancel] setelah mencentang memunculkan dialog Unsaved changes; perubahan bersih nol menutup step langsung

6. Centang 2 group
7. Klik [Cancel]
8. Verifikasi dialog tanpa title: "You have unsaved changes. Are you sure you want to leave?" dengan [Cancel] dan [Leave]
9. Klik [Cancel] pada dialog
10. Verifikasi dialog tertutup dan step tetap terbuka dengan 2 centang dipertahankan
11. Klik [Cancel] lagi
12. Verifikasi dialog `Unsaved changes` `You have unsaved changes. Are you sure you want to leave?` tampil kembali
13. Klik [Leave]
14. Verifikasi step tertutup
15. Buka Wizard Reconciliation > Step Group Consolidation
16. Verifikasi centang yang belum disimpan dibuang (seluruh checkbox unchecked; tidak ada seleksi tersimpan)
17. Centang 1 group
18. Uncheck group yang sama (kembali ke keadaan saat step dibuka)
19. Klik [Cancel]
20. Verifikasi step langsung tertutup tanpa dialog Unsaved changes

### TC-FA-GRP-948: Klik Total Asset dan Total User membuka Detail Group

21. Buka Wizard Reconciliation > Step Group Consolidation
22. Centang `Branch Office`
23. Klik angka Total Asset baris `Warehouse A` (24)
24. Verifikasi popup Detail Group `Warehouse A` terbuka pada tab Assets (24 aset)
25. Tutup popup
26. Klik angka Total User baris `Warehouse A`
27. Verifikasi popup Detail Group `Warehouse A` terbuka pada tab Users
28. Tutup popup
29. Klik angka Total Asset baris `Branch Office` (0)
30. Verifikasi popup Detail Group `Branch Office` terbuka pada tab Assets dengan ilustrasi, title "No assets assigned", dan body "No assets are currently assigned to this group."
31. Tutup popup
32. Verifikasi centang `Branch Office` pada kolom Keep usable tidak berubah
33. Klik [Cancel]
34. Verifikasi dialog `Unsaved changes` `You have unsaved changes. Are you sure you want to leave?` tampil
35. Klik [Leave]

### TC-FA-GRP-965: Server menolak seleksi melebihi cap

36. Buka Wizard Reconciliation > Step Group Consolidation
37. Pasang intercept: isi request [Save Selection] diubah menjadi 4 group
38. Centang 3 group
39. Klik [Save Selection]
40. Verifikasi dialog blok "Cannot Save Selection" dengan isi "The selection exceeds the group limit of your new plan. Deselect some groups and try again." dan satu tombol [OK]
41. Verifikasi tidak ada toast Error T-10
42. Klik [OK]
43. Lepas intercept
44. Verifikasi dialog tertutup dan step tetap terbuka
45. Verifikasi centang yang sedang dipilih (3 group) tidak hilang
46. Verifikasi seleksi tersimpan sebelumnya tidak berubah (kosong, dibaca lewat fixture BE)
47. Klik [Cancel] (3 group tetap tercentang)
48. Verifikasi dialog tanpa title "You have unsaved changes. Are you sure you want to leave?" dengan [Cancel] dan [Leave]
49. Klik [Leave]

### TC-FA-GRP-966: Server menolak seleksi kosong

50. Buka Wizard Reconciliation > Step Group Consolidation
51. Pasang intercept: isi request [Save Selection] diubah menjadi 0 group
52. Centang 1 group
53. Klik [Save Selection]
54. Verifikasi dialog blok "Cannot Save Selection" dengan isi "At least one group must be kept usable. Select at least one group and try again." dan satu tombol [OK]
55. Verifikasi tidak ada toast Error T-10
56. Klik [OK]
57. Lepas intercept
58. Verifikasi dialog tertutup dan step tetap terbuka
59. Verifikasi seleksi tersimpan sebelumnya tidak berubah (kosong, dibaca lewat fixture BE)
60. Klik [Cancel] (1 group tetap tercentang)
61. Verifikasi dialog tanpa title "You have unsaved changes. Are you sure you want to leave?" dengan [Cancel] dan [Leave]
62. Klik [Leave]

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 4, 15, 17 sampai 19, 21, 25, 28, 31, 33, 35 sampai 37, 43, 47, 49 sampai 51, 57, 60, 62: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- P-2: intercept pada TC-965 dan TC-966 hanya pemicu state UI (server menolak seleksi) dan bukan objek asersi; yang diasersi adalah dialog D-23 dan state step. Asersi absence toast Error T-10 (langkah sesudah 37 dan 51) berpangkal pada dialog yang tampil (anchor positif, 8b butir 2).
- Langkah "Centang `Branch Office`" pada TC-948 ditambahkan supaya asersi Expected d (centang tidak berubah setelah popup ditutup) bermakna (S-03); TC tidak menyebut centang awal.
- Penutupan step yang dirty pada TC-965 dan TC-966 (langkah 47, 60) ditulis [Cancel], `Verifikasi` dialog Unsaved changes, lalu [Leave] (S-08) dengan centang dipertahankan supaya form dirty nyata; Wizard dibuka lagi di langkah 50 untuk TC-966 karena langkah 49 menutup step (S-04). Pada TC-309 langkah 17 sampai 20 perubahan centang bersih nol sehingga step langsung tertutup tanpa dialog (FI-06); Wizard dibuka lagi di langkah 21 untuk TC-948 karena langkah 19 menutup step.
- Spec berisi lebih dari 35 langkah. Alasan: seluruh blok pada satu surface (step Group Consolidation) dan satu dataset; tiap blok berdiri sendiri; sebagian besar langkah adalah penghubung buka atau tutup step dan popup.
- Temuan untuk QA:
  - TC-965 Langkah 4 ("Klik [OK] pada dialog") dan TC-966 Langkah 3 menyebut pencegahan sisi klien dilewati lewat mis. intercept request tanpa mekanisme tertentu; spec memakai intercept yang mengubah isi request (kemampuan disediakan tim FE).
  - TC-966 Langkah tidak memuat centang awal; spec mencentang 1 group supaya [Save Selection] enabled sebelum isi request diubah menjadi kosong.
  - TC-308 Expected b "tidak ada seleksi tersimpan/berubah" tidak menyebut cara observasi; spec mengasersi isi Wizard pada pembukaan ulang.
