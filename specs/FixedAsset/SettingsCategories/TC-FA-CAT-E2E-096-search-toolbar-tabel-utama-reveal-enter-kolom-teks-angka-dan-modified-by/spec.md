---
id: TC-FA-CAT-E2E-096-search-toolbar-tabel-utama-reveal-enter-kolom-teks-angka-dan-modified-by
title: "Search Toolbar Tabel Utama: Reveal, Enter, Kolom Teks, dan Kolom Angka"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-321
  - TC-FA-CAT-322
  - TC-FA-CAT-323
  - TC-FA-CAT-324
  - TC-FA-CAT-325
coverage:
  web: automated
---

# Search Toolbar Tabel Utama: Reveal, Enter, Kolom Teks, dan Kolom Angka

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMany (Pre-setup #24), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #24 (CatMany): 30 kategori L1 `Seed Cat 01` sampai `Seed Cat 30` dengan Code `SC01` sampai `SC30`; N total baris = 30 dari seeding. Kategori `Seed Cat 07` bercode `SC07`. Satu baris bernilai Total Asset `17`. Spec hanya membaca data; tidak ada state yang diubah.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-321: Search toolbar, reveal, auto-focus, placeholder, dan tooltip

1. Hover icon Search pada toolbar
2. Verifikasi tooltip icon `Search`
3. Klik icon Search
4. Verifikasi input melebar (reveal)
5. Verifikasi kursor langsung fokus di input
6. Verifikasi placeholder `Search category, code, total asset, modified by...`

### TC-FA-CAT-322: Search tidak live-as-you-type, tabel tersaring saat Enter, dan (✕) mengosongkan input tanpa reset tabel

7. Ketik `Seed Cat 1` pada input Search tanpa menekan Enter
8. Verifikasi icon (✕) muncul pada input
9. Verifikasi tabel belum tersaring (jumlah total baris tetap 30)
10. Tekan `Enter`
11. Verifikasi tabel memuat sedikitnya satu baris
12. Verifikasi tabel hanya memuat `Seed Cat 10` sampai `Seed Cat 19`
13. Klik icon (✕)
14. Verifikasi input Search kosong
15. Verifikasi hasil search terakhir dipertahankan (tabel belum di-reset)
16. Tekan `Enter` pada input kosong
17. Verifikasi tabel kembali memuat seluruh data (jumlah total baris 30)

### TC-FA-CAT-323: Menutup Search lewat icon panah mengosongkan keyword dan langsung me-reset tabel

18. Ketik Search `Seed Cat 2`, tekan Enter
19. Klik icon panah (←) di kiri toolbar
20. Verifikasi kotak pencarian menutup menjadi icon Search biasa
21. Verifikasi keyword kosong
22. Verifikasi tabel langsung memuat seluruh data (jumlah total baris 30) tanpa menekan `Enter`

### TC-FA-CAT-324: Search kolom teks identitas, Category dan Code (substring, case-insensitive, empty state)

23. Ketik Search `seed cat 07`, tekan Enter
24. Verifikasi baris `Seed Cat 07` ditemukan (kolom Category)
25. Ganti isi kotak search dengan `sc07`, tekan Enter
26. Verifikasi baris `Seed Cat 07` ditemukan (kolom Code)
27. Ganti isi kotak search dengan `tidak-ada-xyz`, tekan Enter
28. Verifikasi Title `No results found` tampil
29. Verifikasi Description `Try adjusting your search or filter.` tampil

### TC-FA-CAT-325: Search kolom Total Asset mencocokkan nilai angka

30. Ganti isi kotak search dengan `17`, tekan Enter
31. Verifikasi baris dengan Total Asset `17` ditemukan (substring pada nilai angka)
32. Klik icon panah (←) di kiri toolbar

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Urutan TC: TC-FA-CAT-321 sampai TC-FA-CAT-325 mengikuti urutan TC; Search tidak mengubah data sehingga satu pembukaan halaman dipakai berulang. Langkah 32 mereset Search sebelum hook `afterEach` (S-09).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 3 (membuka input untuk TC-FA-CAT-321), 19 (menutup Search), 32 (pemulihan akhir).
- Spec 097 memuat TC-FA-CAT-326 sampai TC-FA-CAT-331 (Search lanjutan); spec 098 dan 099 memuat Filter.
- Temuan untuk QA:
  - TC-FA-CAT-322 menyebut hasil `Seed Cat 1` dan `Seed Cat 10` sampai `Seed Cat 19`, sedangkan TC-FA-CAT-324 memakai nama berformat dua digit (`Seed Cat 07`); bila seed berformat dua digit, `Seed Cat 1` tidak ada sehingga hasil hanya `Seed Cat 10` sampai `Seed Cat 19`. Spec mengasersi `Seed Cat 10` sampai `Seed Cat 19` saja.
  - TC-FA-CAT-322 Expected a menyebut "tabel belum tersaring" tanpa angka; spec memakai jumlah total 30 dari seeding (8b.10).
  - TC-FA-CAT-325 tidak menyebut kategori yang bernilai Total Asset `17`; spec mengasersi baris bernilai `17` dari seed Pre-setup #24 dan tidak menyebut namanya.
  - TC-FA-CAT-324 Expected c menyebut Description `Try adjusting your search or filter.` sebagai bagian empty state; spec mengasersinya sebagai Verifikasi terpisah (S-01).
