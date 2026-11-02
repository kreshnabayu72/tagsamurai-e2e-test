---
id: TC-FA-GRP-E2E-017-role-matrix-negatif-menu-groups-hidden-dan-akses-url-langsung
title: "Role Matrix Negatif: Menu Settings > Groups Hidden dan Direct URL Ditolak untuk Role Tanpa Capability Manage Group"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-53
  - TC-FA-GRP-54
  - TC-FA-GRP-55
coverage:
  web: automated
---

# Role Matrix Negatif: Menu Settings > Groups Hidden dan Direct URL Ditolak untuk Role Tanpa Capability Manage Group

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun (Pre-setup) | Password | Blok langkah |
|---|---|---|---|
| Role Lain (tanpa Manage Group, bukan Total Control, Read Only, maupun Group Manager) | No 7 `otherRole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_OTHER_PASSWORD` | langkah 1 sampai 9 |
| Manage Group C+U+D tanpa R | No 6 `manageGroupNoRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGNR_PASSWORD` | langkah 10 sampai 15 |

- Login di hook `before` spec ini sebagai Role Lain. Hook `beforeEach` suite yang membuka Settings > Groups ditolak server untuk role ini; karena itu langkah 1 membuka Fixed Asset > Dashboard. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` tidak relevan untuk kedua role karena halaman Groups tidak dapat dibuka.
- Alamat URL halaman Settings > Groups (langkah 6) tidak ditulis TC; disediakan tim FE.
- Kemampuan teknis: fixture BE dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data maupun state global.

## Test Steps

### TC-FA-GRP-53: Menu Groups hidden untuk role tanpa capability Manage Group

1. Buka Fixed Asset > Dashboard
2. Buka sidebar menu Fixed Asset > Settings
3. Verifikasi sedikitnya satu item menu Settings lain tampil pada sidebar yang sama
4. Verifikasi item menu Groups tidak dirender

### TC-FA-GRP-55: Direct URL Settings > Groups oleh role tanpa akses

5. Tunggu toast lama hilang otomatis
6. Ketik URL halaman Settings > Groups langsung di address bar
7. Verifikasi toast error `You don't have permission to do this.`
8. Verifikasi data group tidak ditampilkan dan elemen tanpa hak (tombol [+] Group dan Table Tools Groups) tersembunyi
9. Buka Fixed Asset > Dashboard

### TC-FA-GRP-54: Menu Groups hidden untuk Manage Group tanpa R aktif

10. Logout dari akun Role Lain
11. Login sebagai Manage Group C+U+D tanpa R dengan `Spectra.env.FA_MGNR_PASSWORD`
12. Buka Fixed Asset > Settings
13. Verifikasi sedikitnya satu item menu Settings lain tampil pada sidebar yang sama
14. Verifikasi item menu Groups tidak dirender (menu membutuhkan R aktif)
15. Buka Fixed Asset > Dashboard

## Notes

- Langkah penghubung (S-03): langkah 1 (hook `beforeEach` suite tidak dapat membuka Groups untuk role ini), langkah 5 (menunggu toast penolakan dari hook `beforeEach` hilang agar langkah 7 tidak membaca toast lama, R-12), langkah 9 dan 15 (kembali ke Dashboard), langkah 10 sampai 12 (ganti akun eksplisit).
- `Verifikasi` langkah 3 dan 13 adalah anchor positif asersi absence item menu (8b butir 2) dan tidak ada di Expected TC.
- Urutan TC dalam spec: 53, 55, 54 (TC-FA-GRP-53 dan 55 memakai Role Lain; ganti akun hanya sekali untuk TC-FA-GRP-54).
- Temuan untuk QA:
  - Hook `beforeEach` suite membuka Settings > Groups; untuk spec ini hook perlu dilewati atau dibiarkan menghasilkan penolakan.
  - TC-FA-GRP-55 tidak menyebut URL; spec menyerahkan alamat ke tim FE (S-13).
  - TC-FA-GRP-55 butir b ("elemen tanpa hak tersembunyi") tidak menyebut elemen; spec mengasersi tombol [+] Group dan Table Tools Groups.
