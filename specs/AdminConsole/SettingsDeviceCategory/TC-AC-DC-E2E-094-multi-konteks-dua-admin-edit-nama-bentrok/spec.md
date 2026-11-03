---
id: TC-AC-DC-E2E-094-multi-konteks-dua-admin-edit-nama-bentrok
title: "Dua Admin: Edit ke Nama yang Baru Dibuat Admin Lain di Parent yang Sama"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-281
coverage:
  web: automated
---

# Dua Admin: Edit ke Nama yang Baru Dibuat Admin Lain di Parent yang Sama

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Admin kedua (Pre-setup #9, Maya Putri, Total Control Principal): `totalControlDevCat2_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DC_TC2_PASSWORD` (nama env baru; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`, satu arti: password Total Control kedua Admin Console Settings Device Category). Admin kedua memakai konteks browser kedua karena toast hasil di sesi itu diasersi.
- Login akun aktor pertama di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` menutup konteks browser kedua bila masih terbuka dan mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-094`): `Target {runId}-094` (leaf, namanya tidak berubah selama spec). Node `Nama Bentrok {runId}-094` dibuat admin kedua di bawah `Handheld Reader`. Hook `after` menghapus kedua node itu lewat sesi API. Entri Changelog hasil seeding, aksi admin kedua, dan cleanup bersifat permanen dan tidak dihapus; entri hasil seeding tidak diasersi.
- Kemampuan teknis (disediakan tim FE/BE; tanpa endpoint karangan): membaca jumlah total entri Changelog Category sebelum dan sesudah aksi (B281, langkah 9 dan 19) karena Changelog adalah audit trail permanen (S-12). Search pada modal Changelog dipakai untuk menemukan entri berdasarkan nama bersuffix unik.

## Test Steps

1. Expand `Hardware` lalu `Handheld Reader`
2. Hover node `Target {runId}-094`, klik aksi Edit
3. Ubah nilai menjadi `Nama Bentrok {runId}-094` tetapi belum klik `[Save]`
4. Buka konteks browser kedua, login sebagai admin kedua (`totalControlDevCat2_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DC_TC2_PASSWORD`), lalu buka Settings > Device > Device Name
5. Pada konteks kedua, expand `Hardware` lalu `Handheld Reader`
6. Pada konteks kedua, hover node `Handheld Reader`, klik aksi `+ Subcategory`, ketik `Nama Bentrok {runId}-094`, klik `[Submit]`
7. Verifikasi toast sukses "Success, category has been created." pada konteks kedua
8. Tutup konteks browser kedua dan kembali ke konteks pertama
9. Baca dan catat jumlah entri Changelog Category sebagai B281 (kemampuan baca)
10. Klik `[Save]`
11. Verifikasi pesan error inline "Category name already exists"
12. Verifikasi input Edit tetap terbuka
13. Klik `[Clear Field]`, ketik ulang `Target {runId}-094`, tekan Esc
14. Verifikasi nama node tetap `Target {runId}-094`
15. Klik ikon Changelog pada header Sidebar Category
16. Ketik Search `Nama Bentrok {runId}-094`, tekan Enter
17. Verifikasi hasil Search memuat satu entri `Create` untuk Category `Nama Bentrok {runId}-094` dari admin kedua
18. Verifikasi hasil Search tidak memuat entri `Edit`
19. Verifikasi jumlah entri Changelog Category sama dengan B281 (kemampuan baca)
20. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 (membuka cabang tree), langkah 4 sampai 6 dan 8 (membuka, memakai, dan menutup konteks browser kedua), langkah 13 (mengembalikan input ke nilai tersimpan sehingga bersih lalu menutupnya tanpa dialog, S-09), langkah 20 (menutup modal Changelog). Search pada modal Changelog (langkah 16) menemukan entri berdasarkan nama bersuffix unik (R-16).
- S-05: klausa "tidak ada entri Edit di Changelog" dinyatakan sebagai asersi hasil Search nama bersuffix unik dengan anchor entri `Create` admin kedua (langkah 17 mendahului langkah 18) dan sebagai selisih jumlah total entri terhadap B281 (langkah 9 dan 19), bukan asersi absence kelas g. B281 dicatat sesudah aksi admin kedua (langkah 6) dan sebelum `[Save]` (langkah 10), sehingga selisih nol membuktikan `[Save]` yang ditolak tidak menulis entri apa pun, termasuk entri `Edit` bernama lain.
- P-1: asersi "tidak ada entri Edit" (TC-281 Expected c, kelas g) tetap berada di spec ini karena bergantung pada state yang dibangun langkah sebelumnya di spec asal (form Edit yang dirty di konteks pertama dan nama bentrok yang dibuat admin kedua di konteks kedua), dan state itu tidak dapat dibentuk ulang di spec absence tanpa biaya dua konteks yang sama.
- Pembagian TC lintas spec: TC-122 dan TC-123 (pelaku kedua lewat sesi API) ada di spec 052.
- Temuan untuk QA:
  - TC-281 memakai node literal Pre-setup #14 `Rugged Scanner` sebagai target Edit. Spec memakai `Target {runId}-094` milik spec.
  - TC-281 ditandai `Manual Only (d)`; dua pelaku tidak menghambat penulisan.
