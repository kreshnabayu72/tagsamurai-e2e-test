---
id: TC-FA-FAAC-E2E-033-role-matrix-positif-manage-update-asset-name-dan-versi
title: "Role Matrix Positif: Manage Accounting (Read, Update) Assign, Move, Unassign Asset Name dan Cancel Scheduled Version Berhasil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-82
  - TC-FA-FAAC-83
  - TC-FA-FAAC-84
  - TC-FA-FAAC-85
coverage:
  web: automated
---

# Role Matrix Positif: Manage Accounting (Read, Update) Assign, Move, Unassign Asset Name dan Cancel Scheduled Version Berhasil

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Manage accounting (Read, Update)) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Role yang diuji (tiap role memakai akunnya sendiri):

| Role | Akun | Env var password | TC |
|---|---|---|---|
| Manage accounting (Read, Update) | `manageAccountingReadUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_RU_PASSWORD` | TC-FA-FAAC-82, TC-FA-FAAC-83, TC-FA-FAAC-84, TC-FA-FAAC-85 |

- Env var: `FA_AC_MA_RU_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Rujukan suite: seed dan pemulihan data lewat API/fixture BE, flag Guided Tooltip, dan sesi akun mengikuti `suite.md` (butir Hook suite). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: sembilan Asset Class contoh (Tabel Data Uji Pre-setup; nilai mengikuti Example Data PRD §4.1.1): HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Identitasnya dirujuk lewat `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada; nama kunci ditetapkan tim FE); langkah memakai nama seed literal sesuai TC. Asset Name Forklift 3T belum ter-assign ke Asset Class mana pun; Asset Name Crane Rental Unit (0 aset aktif) ter-assign ke OFFICE-NEW; HEAVY-EQ memiliki versi Scheduled dengan Effective From bulan berjalan + 2 (M+2, format MMM yyyy; seed Scheduled relatif tanggal run, fixture disediakan tim FE/BE) dan Asset Name ter-assign Excavator PC200 dan Wheel Loader (Pre-setup seed, NC-16).
- Tabel Asset Class memuat baris lain di luar sembilan Asset Class contoh (seed B-*, TEMP-EQ, dan sejenisnya); baris yang dipakai langkah dicari lewat Search kode Class Code karena tidak dijamin berada di halaman 1.
- Data yang diubah spec: Forklift 3T ter-assign ke BLDG, Crane Rental Unit dipindah lalu di-unassign, dan versi Scheduled HEAVY-EQ dibatalkan. Target aksi tulis memakai baris seed literal sesuai TC (nama seed dipakai apa adanya, pengecualian beralasan atas S-06 dan S-12 untuk modul ini); fixture BE (disediakan tim FE/BE) menyiapkan baris itu di hook `before` dan memulihkannya ke keadaan awal di hook `after`, termasuk bila spec gagal di tengah. Pemulihan juga dilakukan sebagai langkah penghubung antar blok (langkah 18 dan 26).
- Sesi API aktor (login API dengan password) dipakai sebagai pelaku pemulihan; kemampuan ini disediakan tim BE/FE dan dinyatakan di `suite.md`.
- Data Dinamis: tidak ada data bersuffix `{runId}`; target aksi tulis adalah baris seed literal di atas (pengecualian beralasan, lihat butir sebelumnya).
- State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite).
- Kemampuan teknis: dialog Assign, Move, Unassign, dan Cancel Scheduled Version, fixture BE untuk seed dan pemulihan, muat ulang halaman.

## Test Steps

### TC-FA-FAAC-82

1. Ketik Search `BLDG`, tekan Enter
2. Klik Class Code BLDG
3. Klik tab Asset Names
4. Klik [+ Assign Asset Names]
5. Verifikasi dialog bertitle "Assign Asset Names to Buildings" terbuka
6. Centang Forklift 3T
7. Klik [Assign]
8. Verifikasi toast "Success, asset name has been assigned." tampil
9. Kembali ke tabel Asset Class lewat Breadcrumb Asset Class (form tidak diubah)

### TC-FA-FAAC-83

10. Ganti isi kotak search dengan `OFFICE-NEW`, tekan Enter
11. Klik Class Code OFFICE-NEW
12. Klik tab Asset Names
13. Klik tombol ⋯ baris Crane Rental Unit lalu klik Move
14. Verifikasi dialog "Move Asset Names" terbuka
15. Pilih Destination Asset Class VEHICLES – Vehicles
16. Klik [Move]
17. Verifikasi toast "Success, asset name has been moved." tampil
18. Pulihkan Crane Rental Unit ke OFFICE-NEW lewat fixture BE hingga penempatannya tersimpan, lalu kembali ke tabel Asset Class lewat Breadcrumb Asset Class dan muat ulang halaman (F5)

### TC-FA-FAAC-84

19. Ketik Search `OFFICE-NEW`, tekan Enter
20. Klik Class Code OFFICE-NEW
21. Klik tab Asset Names
22. Klik tombol ⋯ baris Crane Rental Unit lalu klik Unassign
23. Verifikasi dialog Konfirmasi tampil dengan title "Unassign Asset Name", bullet "Crane Rental Unit", teks "It will have no asset class and its assets will not be depreciated. Are you sure you want to unassign it?", tombol [Cancel] dan [Unassign]
24. Klik [Unassign] pada dialog
25. Verifikasi toast "Success, asset name has been unassigned." tampil
26. Pulihkan Crane Rental Unit ke OFFICE-NEW lewat fixture BE hingga penempatannya tersimpan, lalu kembali ke tabel Asset Class lewat Breadcrumb Asset Class dan muat ulang halaman (F5)

### TC-FA-FAAC-85

27. Ketik Search `HEAVY-EQ`, tekan Enter
28. Klik Class Code HEAVY-EQ
29. Klik [Cancel scheduled version] pada Alert
30. Verifikasi dialog tampil dengan title "Cancel Scheduled Version", baris "HEAVY-EQ – Heavy Equipment", "Effective From <M+2 dalam format MMM yyyy>", "Are you sure you want to cancel this scheduled version?", tombol [Back] dan [Cancel version]
31. Klik [Cancel version] pada dialog
32. Verifikasi toast "Success, scheduled version has been cancelled." tampil
33. Verifikasi Alert versi Scheduled hilang

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix positif (bagian 3a): aksi tulis Assign, Move, Unassign, dan Cancel Scheduled Version berhasil bagi role dengan huruf Update; satu role, tanpa ganti akun. Beberapa aksi dalam satu spec dengan polaritas seragam positif.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 9 (kembali ke tabel tanpa mengubah form, S-09), langkah 18 dan 26 (Crane Rental Unit dipulihkan ke OFFICE-NEW karena TC-FA-FAAC-83 memindahkannya dan TC-FA-FAAC-84 memerlukannya ter-assign ke OFFICE-NEW; pelaku pemulihan memakai sesi API aktor, lihat `suite.md`).
- Asersi Alert versi Scheduled hilang memakai toast sukses Cancel version yang sudah diasersi sebagai anchor positif (bagian 8b butir 2).
- Post Condition TC-FA-FAAC-82 sampai 85 tidak punya langkah observasi di TC dan tidak diasersi.
- Temuan untuk QA:
  - TC-FA-FAAC-83 dan TC-FA-FAAC-84 memakai Crane Rental Unit yang ter-assign ke OFFICE-NEW tanpa menyebut pemulihan di antaranya; spec menambah langkah 18 dan 26.
  - TC-FA-FAAC-85 menyebut tombol [Cancel scheduled version] tanpa menyebut Class Code yang dibuka selain HEAVY-EQ; spec memakai HEAVY-EQ sesuai data Pre-setup.
