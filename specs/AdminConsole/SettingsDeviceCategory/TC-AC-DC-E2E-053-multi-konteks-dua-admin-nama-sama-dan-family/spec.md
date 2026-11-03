---
id: TC-AC-DC-E2E-053-multi-konteks-dua-admin-nama-sama-dan-family
title: "Dua Admin: Nama Sama pada Parent yang Sama dan Family Dihapus saat Edit Descendant"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-255
  - TC-AC-DC-256
coverage:
  web: automated
---

# Dua Admin: Nama Sama pada Parent yang Sama dan Family Dihapus saat Edit Descendant

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Admin kedua (Pre-setup #9, Maya Putri, Total Control Principal): `totalControlDevCat2_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DC_TC2_PASSWORD` (nama env baru; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`, satu arti: password Total Control kedua Admin Console Settings Device Category). Pada TC-255 admin kedua memakai konteks browser kedua karena toast hasil di sesi itu diasersi; pada TC-256 admin kedua bertindak lewat sesi API aktor (hanya memicu perubahan state).
- Login akun aktor pertama di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` menutup konteks browser kedua bila masih terbuka dan mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, di bawah `Handheld Reader`; nama bersuffix `{runId}-053`): `Induk {runId}-053` (leaf; TC-255, tempat admin kedua dan aktor menambah `Nama Serentak {runId}-053`) dan family `Keluarga Fam {runId}-053F` dengan anak `Anak A Fam {runId}-053F` (leaf) dan `Anak B Fam {runId}-053F`, serta cucu `Cucu Fam {runId}-053F` di bawah `Anak B Fam {runId}-053F` (TC-256, dihapus admin kedua). Hook `after` menghapus sisa node milik spec lewat sesi API. Entri Changelog hasil seeding, aksi admin kedua, dan cleanup bersifat permanen dan tidak dihapus.
- Kemampuan teknis: Search pada modal Changelog dipakai untuk menemukan entri berdasarkan nama bersuffix unik.

## Test Steps

### Dua admin membuat nama sama di parent yang sama (TC-255)

1. Expand `Hardware` lalu `Handheld Reader`
2. Hover node `Induk {runId}-053`, klik aksi `+ Subcategory`
3. Ketik `Nama Serentak {runId}-053` tetapi belum klik `[Submit]`
4. Buka konteks browser kedua, login sebagai admin kedua (`totalControlDevCat2_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DC_TC2_PASSWORD`), lalu buka Settings > Device > Device Name
5. Pada konteks kedua, expand `Hardware` lalu `Handheld Reader`
6. Pada konteks kedua, hover node `Induk {runId}-053`, klik aksi `+ Subcategory`, ketik `Nama Serentak {runId}-053`, klik `[Submit]`
7. Verifikasi toast sukses "Success, category has been created." pada konteks kedua
8. Tutup konteks browser kedua dan kembali ke konteks pertama
9. Klik `[Submit]`
10. Verifikasi pesan error inline "Category name already exists"
11. Verifikasi input tetap terbuka
12. Klik `[Clear Field]`, tekan Esc
13. Verifikasi hanya satu node `Nama Serentak {runId}-053` ada di bawah `Induk {runId}-053`
14. Klik ikon Changelog pada header Sidebar Category
15. Ketik Search `Nama Serentak {runId}-053`, tekan Enter
16. Verifikasi hanya satu entri `Create` untuk Category `Nama Serentak {runId}-053`
17. Klik `[×]` pada modal Changelog

### Family dihapus saat admin lain membuka Edit pada descendant (TC-256)

18. Expand `Keluarga Fam {runId}-053F` dan `Anak B Fam {runId}-053F`
19. Hover node `Cucu Fam {runId}-053F`, klik aksi Edit
20. Admin kedua (sesi API) menghapus family `Keluarga Fam {runId}-053F` hingga terhapus
21. Tunggu aksi admin kedua selesai
22. Ubah nilai menjadi `Cucu Baru {runId}-053F`, klik `[Save]`
23. Verifikasi toast netral "This category is no longer available."
24. Verifikasi tidak ada toast error terpisah
25. Verifikasi input ditutup
26. Verifikasi tree di-refresh tanpa family `Keluarga Fam {runId}-053F`
27. Klik ikon Changelog pada header Sidebar Category
28. Ketik Search `Cucu Baru {runId}-053F`, tekan Enter
29. Verifikasi empty state "No results found" (tidak ada entri `Edit` untuk `Cucu Fam {runId}-053F` menjadi `Cucu Baru {runId}-053F`)
30. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 dan 18 (membuka cabang tree), langkah 4 sampai 6 dan 8 (membuka, memakai, dan menutup konteks browser kedua untuk TC-255), langkah 12 (membersihkan input sebelum jumlah node diverifikasi; input kosong bersih sehingga Esc tanpa dialog), langkah 17 dan 30 (menutup modal Changelog), langkah 21 (menunggu aksi admin kedua selesai sebelum aksi sesi pertama). Search pada modal Changelog (langkah 15, 28) menemukan entri berdasarkan nama bersuffix unik.
- Pelaku kedua memakai sesi API pada langkah 20 karena hanya memicu perubahan state dan hasil di sesi itu tidak diasersi; pada TC-255 konteks browser kedua dipakai karena toast di sesi itu menjadi Expected (langkah 7).
- S-05: klausa "tidak ada entri Edit untuk Cucu" pada TC-256 dinyatakan sebagai asersi nama bersuffix unik dengan baseline nol (langkah 29), bukan asersi absence kelas g.
- Temuan untuk QA:
  - TC memakai node literal Pre-setup #14 `Handheld Reader`, `Hapus Keluarga`, dan `Hapus Keluarga Cucu`. Spec memakai node milik spec bersuffix `{runId}-053`; family milik spec dihapus admin kedua dan sisanya dibersihkan di hook `after`.
  - TC-255 dan TC-256 ditandai `Manual Only (d)`; dua pelaku tidak menghambat penulisan.
