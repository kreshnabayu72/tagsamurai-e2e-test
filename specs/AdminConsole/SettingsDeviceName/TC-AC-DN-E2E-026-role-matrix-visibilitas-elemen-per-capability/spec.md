---
id: TC-AC-DN-E2E-026-role-matrix-visibilitas-elemen-per-capability
title: "Role Matrix: Visibilitas Kontrol List per Capability (Total Control, Read Only, Create-Only)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-64
  - TC-AC-DN-65
  - TC-AC-DN-63
  - TC-AC-DN-66
coverage:
  web: automated
---

# Role Matrix: Visibilitas Kontrol List per Capability (Total Control, Read Only, Create-Only)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Principal, Default User) (Pre-setup #1); halaman dibuka hook `beforeEach` suite. Jaring pengaman S-09 hook `beforeEach` dan penyetelan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.AC_TC_PASSWORD`).
- Suite berjalan serial (`parallel: false`).
- Akun yang dipakai (email dirujuk lewat `Fixture.settings-device-name.<kunci>`; fixture belum ada, disediakan tim FE):

| Pre-setup | Role | Nama user | Email | Kunci fixture | Env var password | Dipakai di TC |
|---|---|---|---|---|---|---|
| #1 | Total Control (Principal, Default User) | Budi Santoso | `totalControlDevName_automated_{namaCompany}@qwertysystem.net` | `akunTotalControl` | `Spectra.env.AC_TC_PASSWORD` | TC-AC-DN-64 |
| #3 | Read Only (Principal) | Rina Wijaya | `readOnlyDevName_automated_{namaCompany}@qwertysystem.net` | `akunReadOnly` | `Spectra.env.AC_DN_RO_PASSWORD` | TC-AC-DN-65 |
| #4 | Create-Only (Manage device master data: Create + Read) | (tanpa nama di TC) | `manageDeviceC_automated_{namaCompany}@qwertysystem.net` | `akunCreateOnly` | `Spectra.env.AC_DN_CREATE_PASSWORD` | TC-AC-DN-63, TC-AC-DN-66 |

- Env var password: `Spectra.env.AC_DN_CREATE_PASSWORD`, `Spectra.env.AC_DN_RO_PASSWORD`, `Spectra.env.AC_TC_PASSWORD`. `AC_DN_CREATE_PASSWORD`, `AC_DN_RO_PASSWORD` belum terdaftar dan didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; `AC_TC_PASSWORD` sudah terdaftar. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Device Name inti (#16) dibaca saja (baris `Cable Tester` hanya dicentang lalu dicentang ulang tanpa aksi hapus; baris `Barcode Station` hanya dibuka row action-nya).
- Spec tidak mengubah data dan tidak mengubah state global.

## Test Steps

### TC-AC-DN-64: Total Control Default User melihat semua kontrol Device Name

1. Verifikasi Table Tools menampilkan `Search | Filter | Download | Changelog | [+ Device Name]`
2. Centang kotak seleksi pada baris `Cable Tester`
3. Verifikasi kolom checkbox seleksi tampil di sisi kiri tabel
4. Klik tombol `Bulk Action` pada Bulk Action Bar
5. Verifikasi Bulk Action Bar menampilkan tombol `Bulk Action` dengan aksi `Delete`
6. Tutup overlay Bulk Action
7. Hilangkan centang pada baris `Cable Tester`
8. Klik ikon `⋯` pada baris `Barcode Station`
9. Verifikasi Overlay Row Action memuat `Detail | Edit | Delete`
10. Tutup overlay Row Action

### TC-AC-DN-65: Read Only hanya melihat List, Detail, Download, dan Changelog

11. Logout dari akun Total Control
12. Login sebagai Read Only (`Fixture.settings-device-name.akunReadOnly`, password dari `Spectra.env.AC_DN_RO_PASSWORD`)
13. Buka halaman `Settings > Device > Device Name`
14. Verifikasi Table Tools menampilkan `Search | Filter | Download | Changelog`
15. Verifikasi tombol `[+ Device Name]` Hidden
16. Verifikasi kolom checkbox seleksi Hidden sehingga Bulk Action Bar tidak tersedia
17. Klik ikon `⋯` pada baris `Barcode Station`
18. Verifikasi Overlay Row Action hanya memuat `Detail`
19. Verifikasi `Edit` dan `Delete` Hidden
20. Tutup overlay Row Action

### TC-AC-DN-63: Create-Only tetap melihat List, Detail, Download, dan Changelog karena Read menjadi baseline

21. Logout dari akun Read Only
22. Login sebagai Create-Only (`Fixture.settings-device-name.akunCreateOnly`, password dari `Spectra.env.AC_DN_CREATE_PASSWORD`)
23. Buka halaman `Settings > Device > Device Name`
24. Verifikasi List Device Name tampil
25. Verifikasi Table Tools menampilkan `Search | Filter | Download | Changelog | [+ Device Name]`
26. Klik ikon `⋯` pada baris `Barcode Station`
27. Verifikasi Overlay Row Action memuat `Detail`
28. Tutup overlay Row Action

### TC-AC-DN-66: Create-Only melihat tombol tambah tanpa Edit, Delete, dan seleksi massal

29. Verifikasi Table Tools menampilkan `Search | Filter | Download | Changelog | [+ Device Name]`
30. Verifikasi kolom checkbox seleksi Hidden
31. Klik ikon `⋯` pada baris `Barcode Station`
32. Verifikasi Overlay Row Action hanya memuat `Detail`
33. Verifikasi `Edit` dan `Delete` Hidden
34. Tutup overlay Row Action

## Notes

- Spec Role Matrix matriks visibilitas (bagian 3a konvensi): satu daftar elemen List, banyak capability, hasil berbeda per role; title tanpa kata Positif atau Negatif. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan (S-10): TC sumber diurutkan 64, 65, 63, 66 agar TC-AC-DN-63 dan TC-AC-DN-66 (akun Create-Only yang sama) berurutan. Langkah "Buka halaman" tidak diulang untuk TC-AC-DN-66 karena halaman yang sama dipakai berulang tanpa alasan state; halaman untuk TC-AC-DN-64 dibuka hook `beforeEach` suite.
- Langkah penghubung (S-03): ganti akun eksplisit; menutup overlay Row Action dan Bulk Action; menghilangkan centang baris `Cable Tester` (S-09); langkah klik `Bulk Action` ditambahkan karena Expected TC-AC-DN-64 menuntut aksi `Delete` pada Bulk Action diamati; langkah "Buka halaman" setelah login. Anchor asersi Hidden adalah Table Tools dan List yang sudah termuat (bagian 8b butir 2).
- Ukuran spec (34 langkah, mendekati batas sekitar 35 langkah; alasan R2): tiap blok capability berdiri sendiri dengan langkah ganti akun eksplisit (bagian 3 prinsip 13, "Beda akun"); semuanya satu kelas fungsional tanpa aksi tulis. Capability Update-Only, Delete-Only, dan Full CRUD ada di spec 040.
- Temuan untuk QA:
  - TC-AC-DN-63 dan TC-AC-DN-66 sama-sama akun Create-Only dengan Expected yang tumpang tindih (Table Tools dan overlay hanya `Detail`); tiap TC tetap satu spec dan keduanya ditulis lengkap.
  - TC-AC-DN-64 Expected b menyebut aksi `Delete` pada tombol `Bulk Action` tanpa langkah yang mengklik tombol itu.
