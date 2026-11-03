---
id: TC-AC-DN-E2E-025-role-matrix-akses-url-langsung
title: "Role Matrix: Akses URL Langsung Halaman Device Name per Entitas dan Role"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-600
  - TC-AC-DN-601
  - TC-AC-DN-257
  - TC-AC-DN-549
  - TC-AC-DN-548
  - TC-AC-DN-547
coverage:
  web: automated
---

# Role Matrix: Akses URL Langsung Halaman Device Name per Entitas dan Role

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal, Default User) (Pre-setup #1); halaman dibuka hook `beforeEach` suite. Jaring pengaman S-09 hook `beforeEach` dan penyetelan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.AC_TC_PASSWORD`).
- Suite berjalan serial (`parallel: false`).
- Akun yang dipakai (email dirujuk lewat `Fixture.settings-device-name.<kunci>`; fixture belum ada, disediakan tim FE):

| Pre-setup | Role | Nama user | Email | Kunci fixture | Env var password | Dipakai di TC |
|---|---|---|---|---|---|---|
| #1 | Total Control (Principal, Default User) | Budi Santoso | `totalControlDevName_automated_{namaCompany}@qwertysystem.net` | `akunTotalControl` | `Spectra.env.AC_TC_PASSWORD` | TC-AC-DN-600 |
| #3 | Read Only (Principal) | Rina Wijaya | `readOnlyDevName_automated_{namaCompany}@qwertysystem.net` | `akunReadOnly` | `Spectra.env.AC_DN_RO_PASSWORD` | TC-AC-DN-601, TC-AC-DN-257 |
| #8 | Principal tanpa capability Manage device master data | (tanpa nama di TC) | `noCapabilityDevName_automated_{namaCompany}@qwertysystem.net` | `akunTanpaCapability` | `Spectra.env.AC_DN_NOCAP_PASSWORD` | TC-AC-DN-549 |
| #10 | Total Control pada entitas Partner `Partner Jaringan` | (tanpa nama di TC) | `totalControlPartner_automated_{namaCompany}@qwertysystem.net` | `akunPartner` | `Spectra.env.AC_DN_PARTNER_PASSWORD` | TC-AC-DN-548 |
| #9 | Total Control pada entitas Distributor `Distributor Jaringan` | (tanpa nama di TC) | `totalControlDistributor_automated_{namaCompany}@qwertysystem.net` | `akunDistributor` | `Spectra.env.AC_DN_DISTRIBUTOR_PASSWORD` | TC-AC-DN-547 |

- Env var password: `Spectra.env.AC_DN_DISTRIBUTOR_PASSWORD`, `Spectra.env.AC_DN_NOCAP_PASSWORD`, `Spectra.env.AC_DN_PARTNER_PASSWORD`, `Spectra.env.AC_DN_RO_PASSWORD`, `Spectra.env.AC_TC_PASSWORD`. `AC_DN_DISTRIBUTOR_PASSWORD`, `AC_DN_NOCAP_PASSWORD`, `AC_DN_PARTNER_PASSWORD`, `AC_DN_RO_PASSWORD` belum terdaftar dan didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; `AC_TC_PASSWORD` sudah terdaftar. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Device Name inti (#16) dibaca saja; Usage by Company `Gate Antenna` (#18) dibaca saja (lima baris Usage Company A sampai Company E).
- Spec tidak mengubah data dan tidak mengubah state global.

## Test Steps

### TC-AC-DN-600: Total Control membuka halaman Device Name lewat URL langsung

1. Buka navigasi sidebar lalu pilih `Settings > Device > Device Name` dan salin URL dari address bar
2. Buka tab baru dan tempel URL
3. Verifikasi halaman `Settings > Device > Device Name` termuat dengan List
4. Verifikasi toolbar `Search | Filter | Download | Changelog | [+ Device Name]` tampil
5. Verifikasi row action tersedia
6. Tutup tab baru

### TC-AC-DN-601: Read Only membuka halaman Device Name lewat URL langsung tanpa kontrol tulis

7. Logout dari akun Total Control
8. Login sebagai Read Only (`Fixture.settings-device-name.akunReadOnly`, password dari `Spectra.env.AC_DN_RO_PASSWORD`)
9. Buka navigasi sidebar lalu pilih `Settings > Device > Device Name` dan salin URL dari address bar
10. Buka tab baru dan tempel URL
11. Verifikasi halaman `Settings > Device > Device Name` termuat dengan List
12. Klik ikon `⋯` pada baris `Barcode Station`
13. Verifikasi tombol `+ Device Name`, row action `Edit` dan `Delete`, serta kolom checkbox tidak tampil
14. Tutup overlay Row Action

### TC-AC-DN-257: Aktor Read Only dapat membuka dialog Detail

15. Klik nama `Gate Antenna`
16. Verifikasi dialog dengan judul "Device Name Detail" terbuka
17. Verifikasi dialog menampilkan lima baris Usage
18. Tutup dialog Detail dan tab baru

### TC-AC-DN-549: Principal tanpa capability Manage device master data mengakses URL halaman Device Name

19. Logout dari akun Read Only
20. Login sebagai Principal tanpa capability Manage device master data (`Fixture.settings-device-name.akunTanpaCapability`, password dari `Spectra.env.AC_DN_NOCAP_PASSWORD`)
21. Ketik URL halaman `Settings > Device > Device Name` pada address bar, tekan Enter
22. Verifikasi toast error "You don't have permission to do this."
23. Verifikasi tidak ada pengalihan ke halaman lain
24. Verifikasi area halaman tidak menampilkan data Device Name, tombol `+ Device Name`, maupun aksi baris

### TC-AC-DN-548: Partner mengakses URL halaman Device Name

25. Logout dari akun Principal tanpa capability
26. Login sebagai Total Control pada entitas Partner (`Fixture.settings-device-name.akunPartner`, password dari `Spectra.env.AC_DN_PARTNER_PASSWORD`)
27. Ketik URL halaman `Settings > Device > Device Name` pada address bar, tekan Enter
28. Verifikasi toast error "You don't have permission to do this."
29. Verifikasi tidak ada pengalihan ke halaman lain
30. Verifikasi area halaman tidak menampilkan data Device Name, tombol `+ Device Name`, maupun aksi baris

### TC-AC-DN-547: Distributor mengakses URL halaman Device Name

31. Logout dari akun Partner
32. Login sebagai Total Control pada entitas Distributor (`Fixture.settings-device-name.akunDistributor`, password dari `Spectra.env.AC_DN_DISTRIBUTOR_PASSWORD`)
33. Ketik URL halaman `Settings > Device > Device Name` pada address bar, tekan Enter
34. Verifikasi toast error "You don't have permission to do this."
35. Verifikasi tidak ada pengalihan ke halaman lain
36. Verifikasi area halaman tidak menampilkan data Device Name, tombol `+ Device Name`, maupun aksi baris

## Notes

- Spec Role Matrix akses URL (bagian 3a konvensi): topik direct URL per entitas dan role dikelompokkan sebagai spec negatif tersendiri. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan (S-10): TC sumber diurutkan 600, 601, 257, 549, 548, 547 agar akun Read Only dipakai berurutan untuk TC-AC-DN-601 dan TC-AC-DN-257 dan jumlah ganti akun minimum.
- Langkah penghubung (S-03): ganti akun eksplisit; langkah 6 (tutup tab baru) dan langkah 14 (tutup overlay Row Action) serta penutupan dialog Detail dan tab baru. Langkah 12 (klik `⋯`) ditambahkan karena Expected TC-AC-DN-601 butir b menuntut row action `Edit` dan `Delete` diamati. Langkah 1 TC-AC-DN-600 tidak login karena akun aktor pertama login di hook `before` (S-07).
- Ukuran spec (36 langkah, sedikit di atas 35 langkah; alasan R2): tiap blok akun berdiri sendiri dengan langkah ganti akun eksplisit (bagian 3 prinsip 13, "Beda akun") dan semuanya satu kelas fungsional tanpa aksi tulis.
- Temuan untuk QA:
  - TC-AC-DN-601 Expected b menyebut row action `Edit` dan `Delete` tidak tampil tanpa langkah yang membuka overlay Row Action; langkah 12 ditambahkan.
  - TC-AC-DN-257 Expected menyebut "lima baris Usage" tanpa menyebut nama Company; spec memverifikasi jumlah lima baris.
