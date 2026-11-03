---
id: TC-AC-DC-E2E-031-add-validasi-trim-dan-karakter
title: "Add Subcategory: Batas 120 Karakter, Auto-trim Spasi Tepi, dan Emoji Diblok"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DC-80
  - TC-AC-DC-82
  - TC-AC-DC-83
  - TC-AC-DC-84
coverage:
  web: automated
---

# Add Subcategory: Batas 120 Karakter, Auto-trim Spasi Tepi, dan Emoji Diblok

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1, Budi Santoso, tampil di kolom Modified By sebagai `Budi S`): `totalControlDevCat_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar).
- Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor dan pemulihan pohon Pre-setup #14 oleh fixture BE (disediakan tim FE/BE); suite berjalan serial (`parallel: false`).
- Data Pre-setup #14 hanya dibaca dan tidak diubah: node `Hardware` dan `Handheld Reader`. Nama node Pre-setup dibaca dari fixture `Fixture.settingsDeviceCategory.*` (fixture belum ada; disediakan tim FE).
- Data Dinamis milik spec (dibuat lewat sesi API aktor di hook `before`, nama bersuffix `{runId}-031`): `Induk A {runId}-031` dan `Induk B {runId}-031` (leaf di bawah `Handheld Reader`). Hook `after` menghapus keduanya beserta seluruh anaknya lewat sesi API. Entri Changelog hasil seeding dan cleanup bersifat permanen dan tidak dihapus.
- Nilai uji: `N80` = awal teks `Fixture.settingsDeviceCategory.name120` dipotong lalu diakhiri ` {runId}-031a` sehingga panjang total tepat 120 karakter termasuk suffix (TC-80, di bawah `Induk A`); `N82` = hal yang sama dengan akhiran ` {runId}-031b` (TC-82, di bawah `Induk B`, diketik dengan 3 spasi di awal dan di akhir); `Mobile Terminal {runId}-031` (TC-83, diketik dengan 3 spasi di awal dan di akhir, di bawah `Induk A`); `Scanner 😊` dan `🔥` (TC-84).
- Kemampuan teknis: menempel teks dari clipboard ke input (TC-84) disediakan tim FE. Search pada modal Changelog dipakai untuk menemukan entri berdasarkan nama bersuffix unik.

## Test Steps

### Emoji diblok saat diketik atau ditempel (TC-84)

1. Expand `Hardware` lalu `Handheld Reader`
2. Hover node `Induk A {runId}-031`, klik aksi `+ Subcategory`
3. Ketik `Scanner 😊` pada input, lalu tempel `🔥` ke input
4. Verifikasi nilai input hanya `Scanner `
5. Verifikasi tidak ada pesan error
6. Klik `[Clear Field]`, tekan Esc

### Nama tepat 120 karakter diterima (TC-80)

7. Hover node `Induk A {runId}-031`, klik aksi `+ Subcategory`
8. Ketik `N80` pada input, klik `[Submit]`
9. Verifikasi tidak ada error inline
10. Verifikasi toast sukses "Success, category has been created."
11. Verifikasi node `N80` tersimpan dengan nama utuh 120 karakter di bawah `Induk A {runId}-031`

### Auto-trim spasi tepi (TC-83)

12. Tunggu toast sukses dari blok sebelumnya hilang otomatis
13. Hover node `Induk A {runId}-031`, klik aksi `+ Subcategory`
14. Ketik `   Mobile Terminal {runId}-031   ` pada input, klik `[Submit]`
15. Verifikasi toast sukses "Success, category has been created."
16. Verifikasi node tampil dengan nama `Mobile Terminal {runId}-031` tanpa spasi tepi
17. Klik ikon Changelog pada header Sidebar Category
18. Ketik Search `Mobile Terminal {runId}-031`, tekan Enter
19. Verifikasi entri `Create` dengan New Value `Mobile Terminal {runId}-031` tanpa spasi tepi
20. Klik `[×]` pada modal Changelog

### Spasi tepi tidak dihitung pada batas 120 karakter (TC-82)

21. Hover node `Induk B {runId}-031`, klik aksi `+ Subcategory`
22. Ketik 3 spasi, `N82`, lalu 3 spasi pada input, klik `[Submit]`
23. Verifikasi tidak ada error "Max. 120 characters"
24. Verifikasi node `N82` tersimpan dengan nama 120 karakter tanpa spasi tepi di bawah `Induk B {runId}-031`
25. Klik ikon Changelog pada header Sidebar Category
26. Ketik Search `{runId}-031b`, tekan Enter
27. Verifikasi entri `Create` dengan New Value `N82` tanpa spasi tepi
28. Klik `[×]` pada modal Changelog

## Notes

- S-03, langkah penghubung: langkah 1 (membuka cabang tree), langkah 6 (memulihkan input ke keadaan bersih lalu menutupnya tanpa dialog), langkah 12 (menunggu toast lama hilang), langkah 20 dan 28 (menutup modal Changelog). Search pada modal Changelog (langkah 18, 26) menemukan entri berdasarkan nama bersuffix unik.
- Urutan TC dalam spec: TC-84 (diblokir) lebih dulu, lalu TC-80, TC-83, TC-82 agar kedua kasus 120 karakter memakai parent berbeda (S-10).
- Temuan untuk QA:
  - TC memakai nama literal 120 karakter (`Pemindai Kode Batang ...`) dan induk literal `Rugged Scanner`. Spec membuat nama 120 karakter termasuk suffix ` {runId}-031a` dan ` {runId}-031b` (suffix berbeda agar TC-80 dan TC-82 tidak bentrok pada pencarian Changelog) dan memakai induk milik spec; teks 120 karakter tidak persis sama dengan Data Uji TC karena sebagian karakter akhir diganti suffix.
  - Pada TC-84 hasil ketik `Scanner 😊` ditulis TC sebagai nilai `Scanner ` (dengan spasi akhir); spec mengasersi nilai itu apa adanya.
  - Post Condition atau Expected TC-80 tidak menyebut entri Changelog; spec tidak mengasersinya.
