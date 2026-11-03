---
id: TC-AC-DN-E2E-040-role-matrix-visibilitas-elemen-per-capability-bagian-2
title: "Role Matrix: Visibilitas Kontrol List per Capability (Update-Only, Delete-Only, Full CRUD)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-67
  - TC-AC-DN-68
  - TC-AC-DN-69
coverage:
  web: automated
---

# Role Matrix: Visibilitas Kontrol List per Capability (Update-Only, Delete-Only, Full CRUD)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Update-Only (Manage device master data: Update + Read) (Pre-setup #5); halaman dibuka hook `beforeEach` suite. Jaring pengaman S-09 hook `beforeEach` dan penyetelan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.AC_TC_PASSWORD`).
- Suite berjalan serial (`parallel: false`).
- Akun yang dipakai (email dirujuk lewat `Fixture.settings-device-name.<kunci>`; fixture belum ada, disediakan tim FE):

| Pre-setup | Role | Nama user | Email | Kunci fixture | Env var password | Dipakai di TC |
|---|---|---|---|---|---|---|
| #5 | Update-Only (Manage device master data: Update + Read) | (tanpa nama di TC) | `manageDeviceU_automated_{namaCompany}@qwertysystem.net` | `akunUpdateOnly` | `Spectra.env.AC_DN_UPDATE_PASSWORD` | TC-AC-DN-67 |
| #6 | Delete-Only (Manage device master data: Delete + Read) | (tanpa nama di TC) | `manageDeviceD_automated_{namaCompany}@qwertysystem.net` | `akunDeleteOnly` | `Spectra.env.AC_DN_DELETE_PASSWORD` | TC-AC-DN-68 |
| #7 | Full CRUD non-Total Control (Create + Update + Delete + Read, role custom) | (tanpa nama di TC) | `manageDeviceCUD_automated_{namaCompany}@qwertysystem.net` | `akunFullCrud` | `Spectra.env.AC_DN_CRUD_PASSWORD` | TC-AC-DN-69 |

- Env var password: `Spectra.env.AC_DN_CRUD_PASSWORD`, `Spectra.env.AC_DN_DELETE_PASSWORD`, `Spectra.env.AC_DN_UPDATE_PASSWORD`. `AC_DN_CRUD_PASSWORD`, `AC_DN_DELETE_PASSWORD`, `AC_DN_UPDATE_PASSWORD` belum terdaftar dan didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; `AC_TC_PASSWORD` sudah terdaftar. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: Device Name inti (#16) dibaca saja (baris `Cable Tester` hanya dicentang lalu dicentang ulang tanpa aksi hapus; baris `Barcode Station` hanya dibuka row action-nya).
- Spec tidak mengubah data dan tidak mengubah state global.

## Test Steps

### TC-AC-DN-67: Update-Only melihat Edit tanpa tombol tambah, Delete, dan seleksi massal

1. Verifikasi Table Tools menampilkan `Search | Filter | Download | Changelog`
2. Verifikasi tombol `[+ Device Name]` Hidden
3. Verifikasi kolom checkbox seleksi Hidden
4. Klik ikon `⋯` pada baris `Barcode Station`
5. Verifikasi Overlay Row Action memuat `Detail | Edit`
6. Verifikasi `Delete` Hidden
7. Tutup overlay Row Action

### TC-AC-DN-68: Delete-Only melihat Delete dan seleksi massal tanpa tombol tambah dan Edit

8. Logout dari akun Update-Only
9. Login sebagai Delete-Only (`Fixture.settings-device-name.akunDeleteOnly`, password dari `Spectra.env.AC_DN_DELETE_PASSWORD`)
10. Buka halaman `Settings > Device > Device Name`
11. Verifikasi Table Tools menampilkan `Search | Filter | Download | Changelog`
12. Verifikasi tombol `[+ Device Name]` Hidden
13. Centang kotak seleksi pada baris `Cable Tester`
14. Verifikasi kolom checkbox seleksi tampil
15. Klik tombol `Bulk Action` pada Bulk Action Bar
16. Verifikasi Bulk Action Bar menampilkan tombol `Bulk Action` dengan aksi `Delete`
17. Tutup overlay Bulk Action
18. Hilangkan centang pada baris `Cable Tester`
19. Klik ikon `⋯` pada baris `Barcode Station`
20. Verifikasi Overlay Row Action memuat `Detail | Delete`
21. Verifikasi `Edit` Hidden
22. Tutup overlay Row Action

### TC-AC-DN-69: Full CRUD non-Total Control melihat semua kontrol Device Name

23. Logout dari akun Delete-Only
24. Login sebagai Full CRUD non-Total Control (`Fixture.settings-device-name.akunFullCrud`, password dari `Spectra.env.AC_DN_CRUD_PASSWORD`)
25. Buka halaman `Settings > Device > Device Name`
26. Verifikasi Table Tools menampilkan `Search | Filter | Download | Changelog | [+ Device Name]`
27. Centang kotak seleksi pada baris `Cable Tester`
28. Verifikasi kolom checkbox seleksi tampil
29. Klik tombol `Bulk Action` pada Bulk Action Bar
30. Verifikasi Bulk Action Bar menampilkan tombol `Bulk Action` dengan aksi `Delete`
31. Tutup overlay Bulk Action
32. Hilangkan centang pada baris `Cable Tester`
33. Klik ikon `⋯` pada baris `Barcode Station`
34. Verifikasi Overlay Row Action memuat `Detail | Edit | Delete`
35. Tutup overlay Row Action

## Notes

- Spec Role Matrix matriks visibilitas (bagian 3a konvensi): satu daftar elemen List, banyak capability; title tanpa kata Positif atau Negatif. Subjudul `###` memetakan langkah ke id TC granular.
- Pembagian TC lintas spec: TC-AC-DN-64, 65, 63, dan 66 (Total Control, Read Only, Create-Only) ada di spec 026.
- Langkah penghubung (S-03): ganti akun eksplisit (akun aktor pertama Update-Only login di hook `before`, S-07); menutup overlay Row Action dan Bulk Action; menghilangkan centang baris `Cable Tester` (S-09); langkah klik `Bulk Action` ditambahkan karena Expected menuntut aksi `Delete` diamati; langkah "Buka halaman" setelah login. Anchor asersi Hidden adalah Table Tools dan List yang sudah termuat (bagian 8b butir 2).
- Ukuran spec (35 langkah, sekitar 35 langkah; alasan R2): tiap blok capability berdiri sendiri dengan langkah ganti akun eksplisit (bagian 3 prinsip 13, "Beda akun"); semuanya satu kelas fungsional tanpa aksi tulis.
- Temuan untuk QA:
  - TC-AC-DN-68 dan TC-AC-DN-69 Expected b menyebut aksi `Delete` pada tombol `Bulk Action` tanpa langkah yang mengklik tombol itu; langkah penghubung ditambahkan.
