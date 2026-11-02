---
id: TC-FA-CAT-E2E-026-new-category-reserved-word-dan-validasi-code
title: "New Category: Reserved Word pada Category Name dan Validasi Code (Panjang, Whitelist, Duplikat)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-94
  - TC-FA-CAT-95
  - TC-FA-CAT-96
  - TC-FA-CAT-97
  - TC-FA-CAT-98
  - TC-FA-CAT-99
coverage:
  web: automated
---

# New Category: Reserved Word pada Category Name dan Validasi Code (Panjang, Whitelist, Duplikat)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang dipaksa lewat `Spectra.intercept()`.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settingsCategories.totalControl` (`totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`, client CatMain (Pre-setup #20). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan; keputusan tim).
- Data Pre-setup: client CatMain (Pre-setup #20); Code `ELEC-LT` milik `Laptop` (di parent berbeda) menjadi pembanding duplikat Code dan hanya dibaca.
- Data milik spec: kategori level 1 `Code Max new {runId}-026` dengan Code 15 karakter `A` (TC-FA-CAT-97) dan kategori `All  Categories` (dua spasi di tengah) dengan Code `ALLSP` (TC-FA-CAT-96). Nama `All  Categories` dan Code literal sesuai TC karena menjadi objek uji; hook `after` menghapus keduanya lewat API berdasarkan nama.
- Seed dan pemulihan lewat API, flag Guided Tooltip, dan hook suite lain: lihat `suite.md`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-94: Reserved word All Categories ditolak setelah Submit

1. Klik `[+] Category` pada sidebar
2. Isi Category Name `All Categories`
3. Klik `[Submit]`
4. Verifikasi pesan inline `'All Categories' is a reserved name and cannot be used` tampil setelah klik `[Submit]`
5. Verifikasi tidak ada kategori tersimpan (popup tetap terbuka, toast sukses tidak tampil)

### TC-FA-CAT-95: Reserved word dicocokkan tanpa membedakan huruf besar-kecil dan setelah trim

6. Ganti Category Name dengan `all categories ` (huruf kecil dengan spasi akhir)
7. Klik `[Submit]`
8. Verifikasi pesan `'All Categories' is a reserved name and cannot be used` tampil
9. Verifikasi tidak ada kategori tersimpan (popup tetap terbuka, toast sukses tidak tampil)

### TC-FA-CAT-98: Karakter di luar whitelist pada Code menampilkan error langsung (New Category)

10. Ganti Category Name dengan `Code Max new {runId}-026`
11. Ketik Code `AB C!`
12. Verifikasi pesan `Code contains invalid characters` tampil langsung saat mengetik (karakter tidak diblok)
13. Verifikasi helper text digantikan oleh pesan error selama error aktif

### TC-FA-CAT-99: Code duplikat di seluruh client ditolak real-time (New Category)

14. Ganti Code dengan `ELEC-LT` (milik `Laptop` di parent berbeda), lalu tunggu 500ms
15. Verifikasi pesan `Code already exists` tampil sekitar 500ms setelah berhenti mengetik (keunikan per client, bukan per parent)
16. Klik `[Submit]`
17. Verifikasi Submit diblok dan tidak ada kategori tersimpan (popup tetap terbuka, toast sukses tidak tampil)

### TC-FA-CAT-97: Code tepat 15 karakter diterima dan 16 karakter menampilkan error (New Category)

18. Ganti Code dengan 16 karakter `A`
19. Verifikasi pesan `Max. 15 characters` tampil langsung saat melebihi batas dan Submit diblok
20. Hapus satu karakter sehingga Code berisi 15 karakter `A`
21. Klik `[Submit]`
22. Verifikasi toast `Success, category has been created.` tampil
23. Verifikasi Code 15 karakter diterima dan kategori `Code Max new {runId}-026` tersimpan (Search `Code Max new {runId}-026`, tekan Enter, baris tampil)

### TC-FA-CAT-96: Dua spasi di tengah nama reserved tidak dinormalisasi sehingga diterima

24. Klik `[+] Category` pada sidebar
25. Isi Category Name `All  Categories` (dua spasi di tengah) dan Code `ALLSP`
26. Klik `[Submit]`
27. Verifikasi tidak ada error reserved word karena spasi di tengah tidak dinormalisasi
28. Verifikasi toast `Success, category has been created.` tampil dan kategori `All  Categories` tersimpan

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan dan penggabungan form (S-10, prinsip 6): validasi diblokir (TC-FA-CAT-94, 95, 98, 99, 97 bagian 16 karakter) sebelum aksi sukses (TC-FA-CAT-97 bagian 15 karakter dan TC-FA-CAT-96). TC-FA-CAT-97 menguji 15 karakter dulu lalu popup baru untuk 16; spec membalik urutan (16 lalu 15) dalam satu sesi popup agar tidak membuka popup dua kali. Jumlah buka form (langkah 1 dan 24) sama dengan jumlah kejadian menutup (Submit sukses langkah 21 dan 26).
- Langkah penghubung (S-03, R-12, R-16): langkah 6, 10, 14, dan 18 sekaligus mengganti nilai input sehingga error sebelumnya tidak terbawa; langkah 20 (hapus satu karakter) dan langkah 23 (Search untuk menemukan baris target).
- Penyimpangan data (S-06, S-12): Code 15 karakter `A` dan `ALLSP` literal sesuai TC; kolisi Code antar-run dicegah cleanup `after`.
- Temuan untuk QA:
  - TC-FA-CAT-97 Expected a ("kategori tersimpan") tidak menyebut toast; spec mengasersi toast sukses dan baris tersimpan lewat Search.
  - TC-FA-CAT-97 memberi Category Name `Code Max new` tanpa suffix; spec menambah suffix `{runId}-026` (S-12).
  - TC-FA-CAT-99 menyebut `ELEC-LT` milik `Laptop` tanpa Pre-setup eksplisit; spec memakai baris seed Pre-setup #20.
