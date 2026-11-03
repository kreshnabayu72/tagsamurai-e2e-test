---
id: TC-FA-RP-E2E-128-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-4
title: "Popup Assign per jenis: alert tanpa seleksi, stale, dan tidak eligible (4/4)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-440
  - TC-FA-RP-1089
  - TC-FA-RP-1090
  - TC-FA-RP-1091
coverage:
  web: automated
---

# Popup Assign per jenis: alert tanpa seleksi, stale, dan tidak eligible (4/4)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya. "Sesi lain" pada TC sumber hanya memicu perubahan state (menghapus identitas pengguna, menetapkan role pada user) dan memakai sesi API Total Control kedua (Rina Wulandari, Pre-setup #3, `Spectra.env.FA_TC2_PASSWORD`); kemampuan sesi API disediakan tim BE/FE. TC sumber menyebut `Manual Only (d) dua sesi paralel`; sesi lain bukan objek asersi.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #15 (kolam pengguna Standard: Ahmad Fauzi, Budi Santoso, Dimas Pranata, Endah Susanti), #18 (pohon group), #19 (Role Transaksi `IT Infrastructure` sub-tab `Disposal`: Asset Admin Nadia Putri, Monitoring & Report Oscar Pratama, Staff Putri Wulandari, Approver Pandu Wijaya). Kolam #15 disiapkan ulang lewat seeding API di awal TC yang menghapus identitas atau menetapkan penugasan (Pre-setup #32).
- Parameter iterasi (langkah 13 sampai 18, 20 sampai 27, dan 29 sampai 36):

  | Section | User stale (TC-FA-RP-1090) | User tidak lagi eligible dan role yang ditetapkan sesi lain (TC-FA-RP-1091) | User valid yang ikut tercentang |
  |---|---|---|---|
  | Asset Admin | Ahmad Fauzi | Ahmad Fauzi (Asset Admin) | Budi Santoso |
  | Monitoring & Report | Dimas Pranata | Dimas Pranata (Monitoring & Report) | Budi Santoso |
  | Staff | Endah Susanti | Endah Susanti (Staff) | Budi Santoso |

- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: menghapus identitas pengguna, menetapkan Approver, Asset Admin, Monitoring & Report, dan Staff, serta membaca penugasan lewat sesi API (disediakan tim FE/BE tanpa endpoint karangan).
- State yang diubah dan pemulihannya: identitas Ahmad Fauzi, Dimas Pranata, dan Endah Susanti dihapus (TC-FA-RP-1090) dan ditetapkan pada role section (TC-FA-RP-440 dan TC-FA-RP-1091) lewat langkah sesi API. Hook `after` memulihkan kolam Pre-setup #15 dan Pre-setup #19 lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` pada Sidebar Group Tree
3. Klik sub-tab `Disposal`

### TC-FA-RP-440: Assign Approver, user tidak lagi eligible menolak seluruh submit dengan alert

4. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan
5. Klik `[+ Assign]` pada section Approver
6. Centang Ahmad Fauzi dan Budi Santoso
7. Tetapkan Ahmad Fauzi sebagai Approver pada `IT Infrastructure` sub-tab `Disposal` lewat sesi API hingga tersimpan
8. Klik `[Assign]`
9. Verifikasi alert inline `Ahmad Fauzi is no longer eligible. Please select another.`
10. Verifikasi tidak ada penugasan dibuat untuk Budi Santoso lewat kemampuan baca
11. Verifikasi Budi Santoso tetap tercentang
12. Klik `[Cancel]`

### TC-FA-RP-1089: Assign Asset Admin, Monitoring & Report, dan Staff, klik `[Assign]` tanpa seleksi menampilkan alert inline

Untuk setiap section pada tabel "Parameter iterasi" (langkah 13 sampai 18):

13. Klik `[+ Assign]` pada section
14. Klik `[Assign]` tanpa memilih user
15. Verifikasi alert inline rata kanan di atas footer `You must pick a user`
16. Verifikasi popup tetap terbuka
17. Verifikasi tidak ada penugasan tersimpan pada section itu lewat kemampuan baca
18. Klik `[Cancel]`

### TC-FA-RP-1090: Assign Asset Admin, Monitoring & Report, dan Staff, user stale menolak seluruh submit dengan alert

19. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan

Untuk setiap section pada tabel "Parameter iterasi" (langkah 20 sampai 27):

20. Klik `[+ Assign]` pada section
21. Centang user stale pada tabel dan Budi Santoso
22. Hapus identitas user stale lewat sesi API hingga terhapus
23. Klik `[Assign]`
24. Verifikasi alert inline `[user stale] no longer exists. Please select another.`
25. Verifikasi tidak ada penugasan dibuat pada section itu lewat kemampuan baca
26. Verifikasi Budi Santoso tetap tercentang
27. Klik `[Cancel]`

### TC-FA-RP-1091: Assign Asset Admin, Monitoring & Report, dan Staff, user tidak lagi eligible menolak seluruh submit dengan alert

28. Siapkan kolam pengguna Pre-setup #15 lewat sesi API hingga tersimpan

Untuk setiap section pada tabel "Parameter iterasi" (langkah 29 sampai 36):

29. Klik `[+ Assign]` pada section
30. Centang user stale pada tabel dan Budi Santoso
31. Tetapkan user stale pada role section itu di `IT Infrastructure` sub-tab `Disposal` lewat sesi API hingga tersimpan
32. Klik `[Assign]`
33. Verifikasi alert inline `[user stale] is no longer eligible. Please select another.`
34. Verifikasi tidak ada penugasan dibuat pada section itu lewat kemampuan baca
35. Verifikasi Budi Santoso tetap tercentang
36. Klik `[Cancel]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 4, 19, dan 28 (menyiapkan kolam pengguna per TC lewat sesi API, Pre-setup #32), langkah 12 dan 18 (menutup popup Assign dengan `[Cancel]`). Langkah 27 dan 36 adalah langkah `[Cancel]` dari TC-FA-RP-1090 dan TC-FA-RP-1091.
- Langkah 13 sampai 18, 20 sampai 27, dan 29 sampai 36 diulang per section sesuai tabel "Parameter iterasi" (bagian 8b butir 7); `Verifikasi` tetap satu per klausa pada tiap iterasi. Teks `[user stale]` pada langkah 24 dan 33 diganti nama user pada tabel untuk iterasi itu.
- Langkah 10, 17, 25, dan 34 ("tidak ada penugasan dibuat atau tersimpan") memakai kemampuan baca penugasan karena TC tidak menyebut indikator UI.
- Alasan di atas sekitar 35 langkah (36 langkah nominal, 80 langkah efektif sesudah ekspansi tiga section): empat TC satu topik (alert popup Assign Role Transaksi) dengan iterasi per section yang parameternya ada di tabel Prerequisites dan tanpa langkah bersyarat. Kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-RP-440 menyebut "mengubah kelayakan Ahmad Fauzi (sudah memegang penugasan yang sama)" tanpa menyebut cara; spec menetapkan penugasan yang sama lewat sesi API (langkah 7).
  - TC-FA-RP-1089 menyebut `UI Only` pada kolom FE Test tetapi Expected "tidak ada penugasan tersimpan" menyentuh state server; spec memakai FE+BE dan kemampuan baca.
