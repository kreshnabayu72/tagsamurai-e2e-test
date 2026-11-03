---
id: TC-AC-DN-E2E-024-role-matrix-visibilitas-menu-per-entitas
title: "Role Matrix: Visibilitas Menu Device Name per Entitas dan Capability, serta Dropdown Distributor"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DN-58
  - TC-AC-DN-62
  - TC-AC-DN-60
  - TC-AC-DN-61
  - TC-AC-DN-59
  - TC-AC-DN-526
coverage:
  web: automated
---

# Role Matrix: Visibilitas Menu Device Name per Entitas dan Capability, serta Dropdown Distributor

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal, Default User) (Pre-setup #1); halaman dibuka hook `beforeEach` suite. Jaring pengaman S-09 hook `beforeEach` dan penyetelan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.AC_TC_PASSWORD`).
- Suite berjalan serial (`parallel: false`).
- Akun yang dipakai (email dirujuk lewat `Fixture.settings-device-name.<kunci>`; fixture belum ada, disediakan tim FE):

| Pre-setup | Role | Nama user | Email | Kunci fixture | Env var password | Dipakai di TC |
|---|---|---|---|---|---|---|
| #1 | Total Control (Principal, Default User) | Budi Santoso | `totalControlDevName_automated_{namaCompany}@qwertysystem.net` | `akunTotalControl` | `Spectra.env.AC_TC_PASSWORD` | TC-AC-DN-58 |
| #8 | Principal tanpa capability Manage device master data | (tanpa nama di TC) | `noCapabilityDevName_automated_{namaCompany}@qwertysystem.net` | `akunTanpaCapability` | `Spectra.env.AC_DN_NOCAP_PASSWORD` | TC-AC-DN-62 |
| #10 | Total Control pada entitas Partner `Partner Jaringan` | (tanpa nama di TC) | `totalControlPartner_automated_{namaCompany}@qwertysystem.net` | `akunPartner` | `Spectra.env.AC_DN_PARTNER_PASSWORD` | TC-AC-DN-60 |
| #11 | Total Control pada entitas Client `Client Jaringan` | (tanpa nama di TC) | `totalControlClient_automated_{namaCompany}@qwertysystem.net` | `akunClient` | `Spectra.env.AC_DN_CLIENT_PASSWORD` | TC-AC-DN-61 |
| #9 | Total Control pada entitas Distributor `Distributor Jaringan` | (tanpa nama di TC) | `totalControlDistributor_automated_{namaCompany}@qwertysystem.net` | `akunDistributor` | `Spectra.env.AC_DN_DISTRIBUTOR_PASSWORD` | TC-AC-DN-59, TC-AC-DN-526 |

- Env var password: `Spectra.env.AC_DN_CLIENT_PASSWORD`, `Spectra.env.AC_DN_DISTRIBUTOR_PASSWORD`, `Spectra.env.AC_DN_NOCAP_PASSWORD`, `Spectra.env.AC_DN_PARTNER_PASSWORD`, `Spectra.env.AC_TC_PASSWORD`. `AC_DN_CLIENT_PASSWORD`, `AC_DN_DISTRIBUTOR_PASSWORD`, `AC_DN_NOCAP_PASSWORD`, `AC_DN_PARTNER_PASSWORD` belum terdaftar dan didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; `AC_TC_PASSWORD` sudah terdaftar. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Device Name inti (#16) dibaca saja; entitas uji `Distributor Jaringan`, `Partner Jaringan`, dan `Client Jaringan` (#9, #10, #11).
- Kondisi TC-AC-DN-526: Local Registration aktif untuk `Distributor Jaringan` dan Device Name inti (`Gate Antenna`, `RFID Reader`) tersedia sebagai opsi dropdown; Local Registration Distributor disediakan tim FE (tidak ada di tabel Pre-setup TC; lihat Temuan untuk QA).
- Spec tidak mengubah data dan tidak mengubah state global.

## Test Steps

### TC-AC-DN-58: Principal dengan capability Read melihat menu Device Name dan membuka List

1. Buka navigasi sidebar lalu pilih `Settings > Device`
2. Verifikasi menu `Settings > Device` tampil pada navigasi
3. Verifikasi sub-tab `Device Name` tampil
4. Klik sub-tab `Device Name`
5. Verifikasi List Device Name tampil di `Settings > Device > Device Name`

### TC-AC-DN-62: Principal tanpa capability Manage device master data tidak melihat menu Device Name

6. Logout dari akun Total Control
7. Login sebagai Principal tanpa capability Manage device master data (`Fixture.settings-device-name.akunTanpaCapability`, password dari `Spectra.env.AC_DN_NOCAP_PASSWORD`)
8. Buka navigasi sidebar lalu pilih `Settings`
9. Verifikasi daftar menu Settings tampil
10. Verifikasi menu Device Name tidak tampil (Hidden) karena tanpa akses Read
11. Verifikasi tidak ada akses UI ke List Device Name

### TC-AC-DN-60: Partner ber-role Total Control tidak memiliki menu Device Name

12. Logout dari akun Principal tanpa capability
13. Login sebagai Total Control pada entitas Partner (`Fixture.settings-device-name.akunPartner`, password dari `Spectra.env.AC_DN_PARTNER_PASSWORD`)
14. Buka navigasi sidebar lalu pilih menu `Settings`
15. Verifikasi daftar menu Settings tampil
16. Verifikasi item menu dan sub-tab `Device Name` tidak tampil (Hidden)
17. Verifikasi tidak ada akses UI ke List Device Name

### TC-AC-DN-61: Client ber-role Total Control tidak memiliki menu Device Name

18. Logout dari akun Partner
19. Login sebagai Total Control pada entitas Client (`Fixture.settings-device-name.akunClient`, password dari `Spectra.env.AC_DN_CLIENT_PASSWORD`)
20. Buka navigasi produk yang tersedia bagi Client
21. Verifikasi navigasi produk yang tersedia bagi Client tampil
22. Verifikasi menu Admin Console termasuk `Settings > Device > Device Name` tidak tersedia
23. Verifikasi tidak ada akses UI ke List Device Name

### TC-AC-DN-59: Distributor ber-role Total Control tidak memiliki menu Device Name

24. Logout dari akun Client
25. Login sebagai Total Control pada entitas Distributor (`Fixture.settings-device-name.akunDistributor`, password dari `Spectra.env.AC_DN_DISTRIBUTOR_PASSWORD`)
26. Buka navigasi sidebar lalu pilih `Settings > Device`
27. Verifikasi halaman `Settings > Device` terbuka
28. Verifikasi sub-tab `Device Name` tidak tampil (Hidden) meskipun user ber-role Total Control
29. Verifikasi tidak ada akses UI ke List Device Name

### TC-AC-DN-526: Distributor memilih Device Name lewat dropdown form Create Device SKU sementara menu Device Name tidak tersedia

30. Buka halaman `Settings > Device > Device SKU`
31. Verifikasi List Device SKU tampil
32. Verifikasi sub-tab `Device Name` tidak tampil pada halaman Device SKU
33. Klik `[+ SKU]`
34. Buka dropdown field Device Name
35. Verifikasi dropdown Device Name memuat opsi "Gate Antenna" dan "RFID Reader" untuk dibaca dan dipilih
36. Pilih opsi "Gate Antenna"
37. Verifikasi field Device Name menampilkan "Gate Antenna"
38. Ketik URL halaman `Settings > Device > Device Name` pada address bar, tekan Enter
39. Verifikasi toast error "You don't have permission to do this."
40. Verifikasi tidak ada pengalihan halaman
41. Verifikasi area halaman tidak menampilkan data Device Name, tombol `+ Device Name`, maupun aksi baris
42. Tutup form Create Device SKU lewat `✕`
43. Verifikasi dialog `Unsaved Changes` tampil
44. Klik `[Leave]`

## Notes

- Spec Role Matrix visibilitas (bagian 3a konvensi): satu daftar elemen (menu Device Name), banyak role, hasil Hidden dan tampil dicampur. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan (S-10): TC sumber diurutkan 58, 62, 60, 61, 59, 526 (bukan 58, 59, 60, 61, 62, 526) agar akun Distributor dipakai berurutan dengan TC-AC-DN-526 dan jumlah ganti akun minimum.
- Langkah penghubung (S-03): ganti akun eksplisit (logout lalu login) pada awal tiap blok akun. Langkah 1 tidak melakukan login karena akun aktor pertama (Total Control) sudah login di hook `before` (S-07). Verifikasi anchor ditambahkan agar asersi Hidden punya anchor positif (bagian 8b butir 2): daftar menu Settings tampil (langkah 9 dan 15), navigasi produk Client tampil (langkah 21), halaman `Settings > Device` terbuka (langkah 27). Langkah 42 sampai 44 menutup form Create Device SKU yang dirty (S-08, S-09).
- Ukuran spec (44 langkah, di atas 35 langkah; alasan R2): tiap blok akun berdiri sendiri dengan langkah ganti akun eksplisit (bagian 3 prinsip 13, "Beda akun") dan semuanya satu kelas fungsional tanpa aksi tulis; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-DN-526 mensyaratkan Local Registration aktif untuk Distributor Jaringan yang tidak ada di tabel Data Uji Pre-setup; ditulis sebagai disediakan tim FE.
  - TC-AC-DN-526 tidak menyatakan apakah form Create Device SKU tetap terbuka setelah URL halaman Device Name diminta; spec menutup form dengan langkah 42 sampai 44 sesuai S-08.
  - TC-AC-DN-58 berjudul Principal dengan capability Read tetapi login sebagai Total Control; tidak ada akun Read-only-capability terpisah di TC ini (kasus Read Only ada di spec 025 dan 026).
  - TC-AC-DN-61 Langkah 1 "Buka navigasi produk yang tersedia bagi Client" tidak menyebut halaman yang dituju; Verifikasi navigasi tampil (langkah 21) ditambahkan sebagai anchor.
