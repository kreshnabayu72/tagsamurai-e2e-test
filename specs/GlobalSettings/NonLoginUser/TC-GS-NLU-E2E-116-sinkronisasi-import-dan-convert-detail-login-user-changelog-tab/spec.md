---
id: TC-GS-NLU-E2E-116-sinkronisasi-import-dan-convert-detail-login-user-changelog-tab
title: "Sinkronisasi Import dan Convert: Detail Login User, Changelog, tab Non-Login User"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-NLU-424
  - TC-GS-NLU-426
  - TC-GS-NLU-427
  - TC-GS-NLU-428
  - TC-GS-NLU-429
coverage:
  web: automated
---

# Sinkronisasi Import dan Convert: Detail Login User, Changelog, tab Non-Login User

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup No. 9 sampai 13 (Position `Driver` dan `Manager`; Division `Operations`, `Warehouse`, `Logistics`, `Finance`; Login User `Ahmad Fauzi` dan `Dewi Anggraini`; Custom Field dasar) hanya dibaca, tidak diubah atau dihapus.
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding, Import, Convert, dan transaksi FAMS disediakan tim FE/BE; Division `Operations`, Email `<nama>+{runId}-116@qwertysystem.net`):
  - TC-GS-NLU-424: Non-Login User `Impor Satu {runId}-116` (Position `Driver`, Represented By `Ahmad Fauzi`, Active) dibuat lewat Import "User Non Login".
  - TC-GS-NLU-426: Non-Login User `Budi Kurniawan {runId}-116` (Active, Represented By `Ahmad Fauzi`) dengan transaksi Borrowed `BRW-20260610-0001` (Laptop - 1) dan `BRW-20260702-0003` (Proyektor) serta Assigned `ASG-20260505-0001` (Company Vehicle B1234XY) dan `ASG-20260610-0002` (Mesin Bor), sesuai Tabel Data Uji Pre-setup No. 14.
  - TC-GS-NLU-427: Login User `Konversi Aset {runId}-116` hasil Convert dengan Borrowed `BRW-20260801-0009` (Kamera Uji) dan Assigned `ASG-20260801-0004` (Tripod Uji), PIC Siti Rahma; thread Changelog memuat entri era Non-Login (`Create` sampai `Convert to Login User`) dan sedikitnya satu entri lanjutan Login User (First Name diubah lewat API oleh hook `before` sesudah Convert).
  - TC-GS-NLU-428: Login User `Sudah Konversi Satu {runId}-116` (First Name `Sudah`, Last Name `Konversi Satu {runId}-116`) hasil Convert dengan entri `Convert to Login User` di Changelog.
  - TC-GS-NLU-429: Login User `Ahmad Rujuk {runId}-116` (First Name `Ahmad`, Last Name `Rujuk {runId}-116`, Active); Non-Login User `Sudah Konversi Dua {runId}-116` hasil Convert dengan Represented By lama `Ahmad Rujuk {runId}-116`; Non-Login User `Sisa Aktif {runId}-116` (Active) dan `Sisa Inaktif {runId}-116` (Inactive) dengan Represented By `Ahmad Rujuk {runId}-116`. N dari seeding = 2 (label `Non-Login User (2)`).
- Pemulihan: hook `after` menghapus lewat API semua data `{runId}-116` yang tersisa (Non-Login User dan Login User hasil Convert).
- Suite berjalan serial (`parallel: false`).
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

### TC-GS-NLU-424: Import User Non Login, record hasil Import dapat di-Edit sama seperti hasil Create manual

1. Ketik Search `Impor Satu {runId}-116`, tekan Enter, klik `⋯` baris `Impor Satu {runId}-116` > `Edit`
2. Ubah Position dari `Driver` menjadi `Manager`, lalu klik `[Save]`
3. Verifikasi Toast sukses `Success, non-login user has been updated.`
4. Verifikasi sel Position baris `Impor Satu {runId}-116` menampilkan `Manager`
5. Klik Name baris `Impor Satu {runId}-116` untuk membuka Detail, lalu klik tab `Changelog`
6. Verifikasi Changelog memuat entri `Edit` Field `Position`, Old Value `Driver`, New Value `Manager`, Modified By `Siti N`, sama seperti record yang dibuat manual

### TC-GS-NLU-426: Deactivate Non-Login User tidak mempengaruhi riwayat transaksi berjalan

7. Buka sub-tab Non-Login User, ketik Search `Budi Kurniawan {runId}-116`, tekan Enter, klik Name baris tersebut untuk membuka Detail
8. Klik tab `Responsibilities`, sub-tab `Borrowed Assets`, dan catat daftar transaksi sebagai baseline
9. Klik sub-tab `Assigned Assets` dan catat daftar transaksi sebagai baseline
10. Klik switch Active di header Detail (ON), lalu konfirmasi dengan `[Deactivate]`
11. Tunggu aksi selesai (dialog Deactivate menutup)
12. Klik tab `Responsibilities`, sub-tab `Borrowed Assets`
13. Verifikasi daftar Borrowed Assets tetap menampilkan transaksi yang sama dengan baseline
14. Klik sub-tab `Assigned Assets`
15. Verifikasi daftar Assigned Assets tetap menampilkan transaksi yang sama dengan baseline

### TC-GS-NLU-427: Setelah Convert, Detail Login User memuat Responsibilities dan thread Changelog yang sama

16. Buka sub-tab Login User, ketik Search `Konversi Aset {runId}-116`, tekan Enter, klik Name baris tersebut untuk membuka Detail Login User
17. Klik tab `Responsibilities`
18. Verifikasi Borrowed Assets lama `BRW-20260801-0009` (Kamera Uji) tetap tampil
19. Klik sub-tab `Assigned Assets`
20. Verifikasi Assigned Assets lama `ASG-20260801-0004` (Tripod Uji) tetap tampil
21. Klik tab `Changelog`
22. Verifikasi Changelog memuat entri era Non-Login User dari `Create` sampai `Convert to Login User`
23. Verifikasi Changelog memuat entri lanjutan Login User dalam thread yang sama

### TC-GS-NLU-428: Setelah Convert, entri lanjutan tidak lagi muncul di Modal Changelog agregat Non-Login User

24. Buka sub-tab Login User, ketik Search `Konversi Satu {runId}-116`, tekan Enter, klik `⋯` baris `Sudah Konversi Satu {runId}-116` > `Edit`
25. Ubah First Name `Sudah` menjadi `Sudahx`, lalu klik `[Save]`
26. Tunggu aksi selesai (popup Edit menutup)
27. Buka sub-tab Non-Login User, klik icon `Changelog` pada Table Tools sehingga Modal Changelog terbuka, lalu ketik Search `Konversi Satu {runId}-116`, tekan Enter
28. Verifikasi entri `Convert to Login User` untuk record tersebut tetap tampil sebagai baris terakhir
29. Verifikasi tidak ada entri `Edit` baru untuk record tersebut di Modal Changelog agregat
30. Tutup Modal Changelog dengan `✕`

### TC-GS-NLU-429: Setelah Convert, baris hilang dari Tab Non-Login User milik Represented By lama

31. Buka sub-tab Login User, ketik Search `Rujuk {runId}-116`, tekan Enter, klik Name baris `Ahmad Rujuk {runId}-116` untuk membuka Detail, lalu klik tab `Non-Login User`
32. Verifikasi baris `Sisa Aktif {runId}-116` dan `Sisa Inaktif {runId}-116` tampil di tab
33. Verifikasi `Sudah Konversi Dua {runId}-116` tidak muncul di tab
34. Verifikasi label tab `Non-Login User (2)` sama dengan jumlah Non-Login User Active atau Inactive yang belum dihapus dengan Represented By `Ahmad Rujuk {runId}-116`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1, 7, 16, 24, 27, 31 (membuka sub-tab dan Search record yang dicari), langkah 5 (membuka Detail), langkah 11, 26 (Tunggu aksi selesai), dan langkah 30 (menutup modal).
- N pada TC-GS-NLU-429 berasal dari seeding (dua Non-Login User tersisa), bukan dibaca dari tabel (bagian 8b butir 10).
- Temuan untuk QA:
  - TC-GS-NLU-424 tidak menyebut Position awal dan nilai pengganti record hasil Import, serta cara hook membuat record lewat Import; spec memakai `Driver` menjadi `Manager` dan seeding Import disediakan tim FE/BE.
  - TC-GS-NLU-426 menyebut Budi Kurniawan (Pre-setup) sebagai target Deactivate; spec memakai record milik spec dengan transaksi FAMS yang sama dengan Pre-setup No. 14 supaya Deactivate tidak mengubah data bersama (S-06). Pemasangan transaksi FAMS ke record milik spec disediakan tim FE/BE.
  - TC-GS-NLU-427 Expected b menyebut "entri lanjutan Login User" tanpa menyebut entri itu; spec memakai satu entri perubahan First Name yang dibuat hook `before` sesudah Convert (disediakan tim FE/BE).
  - TC-GS-NLU-428 menyebut "baris terakhir" untuk entri `Convert to Login User` pada Modal Changelog yang entri teratasnya adalah entri terbaru (TC-GS-NLU-394); spec mengikuti TC dan mengasersi entri itu pada baris terakhir hasil Search, urutan tampil perlu dikonfirmasi QA.
  - TC-GS-NLU-428 dan 429 memakai Login User hasil Convert Pre-setup (`Sudah Konversi Satu`, `Sudah Konversi Dua`); spec memakai akun milik spec dengan nama bersuffix.
