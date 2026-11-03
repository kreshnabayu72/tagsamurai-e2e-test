---
id: TC-GS-NLU-E2E-035-popup-select-user-ikon-edit-badge-klik-badge-dan
title: "Popup Select User: ikon edit badge, klik badge, dan Represented By Inactive"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-108
  - TC-GS-NLU-109
  - TC-GS-NLU-496
coverage:
  web: automated
---

# Popup Select User: ikon edit badge, klik badge, dan Represented By Inactive

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/nonLoginUser.json` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): pool Login User Represented By No. 10 (Dewi Anggraini, Fajar Nugroho, Jane Smith Inactive) dan Non-Login User `Nonaktif Wakil` dengan Represented By Jane Smith yang Inactive (No. 11). Popup Edit `Nonaktif Wakil` hanya dibuka lalu ditutup tanpa Save sehingga data tidak berubah. Popup Create tidak pernah di-Submit; spec tidak membuat atau mengubah data backend.
- State global: tidak ada yang diubah.

## Test Steps

1. Klik `[+ Non-Login User]` sehingga Popup Create Non-Login User terbuka
2. Klik `[+ Select User]` pada field Represented By sehingga Popup Select User terbuka

### TC-GS-NLU-108: Ikon edit pada badge membuka ulang popup dengan user terpilih saat ini dan memungkinkan ganti user

3. Klik baris Dewi Anggraini
4. Klik `[Select]`
5. Klik ikon `✎` pada badge
6. Verifikasi Popup Select User terbuka dengan baris Dewi Anggraini sudah tersorot (pre-selected)
7. Klik baris Fajar Nugroho
8. Klik `[Select]`
9. Verifikasi badge berganti menjadi `Fajar Nugroho`
10. Verifikasi tidak ada ikon hapus atau remove pada badge

### TC-GS-NLU-109: Klik badge di luar ikon edit tidak melakukan apa pun

11. Klik ikon `✎` pada badge
12. Klik baris Dewi Anggraini
13. Klik `[Select]`
14. Klik teks `Dewi Anggraini` pada badge (bukan ikon `✎`)
15. Verifikasi tidak ada popup dan tidak ada navigasi
16. Verifikasi badge tidak berubah dan tetap `Dewi Anggraini`
17. Klik `✕` pada Popup Create Non-Login User
18. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan tombol `[Cancel]` dan `[Leave]`
19. Klik `[Leave]`

### TC-GS-NLU-496: Popup Select User tanpa baris ter-pre-select saat Represented By tersimpan sudah Inactive

20. Ketik Search `Nonaktif Wakil`, tekan Enter
21. Klik `⋯` pada baris Nonaktif Wakil > `Edit` sehingga Popup Edit Non-Login User terbuka
22. Klik icon edit `✎` pada badge Represented By sehingga Popup Select User terbuka
23. Verifikasi tabel Popup Select User menampilkan sedikitnya satu baris Login User
24. Verifikasi tidak ada baris yang tersorot di Popup Select User (Jane Smith tidak ada di pool)
25. Klik `[Cancel]`
26. Verifikasi badge Represented By di form tetap `Jane Smith`
27. Klik `✕` pada Popup Edit Non-Login User

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung tanpa `Verifikasi`: langkah 11 sampai 13 (memilih kembali Dewi Anggraini sebagai precondition TC-GS-NLU-109 karena TC-GS-NLU-108 meninggalkan badge Fajar Nugroho), langkah 17 sampai 19 (menutup Popup Create yang dirty secara deterministik, S-08), dan langkah 27 (menutup Popup Edit yang tidak berubah sehingga tanpa dialog). Langkah 20 mencari baris target (R-16).
- Urutan: TC-GS-NLU-496 dijalankan terakhir karena memakai Popup Edit, bukan Popup Create.
- Temuan untuk QA:
  - TC-GS-NLU-109 menyatakan badge Dewi Anggraini lewat langkah "Pilih Dewi Anggraini lalu `[Select]`"; karena spec ini menjalankan TC-GS-NLU-108 lebih dulu, badge sudah Fajar Nugroho dan spec memilih ulang Dewi Anggraini lewat ikon `✎`.
