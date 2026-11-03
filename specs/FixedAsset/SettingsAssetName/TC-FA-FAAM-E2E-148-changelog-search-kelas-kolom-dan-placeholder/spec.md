---
id: TC-FA-FAAM-E2E-148-changelog-search-kelas-kolom-dan-placeholder
title: "Modal Changelog: Search Kelas Kolom, Modified By Nama Lengkap, Tanpa Kolom Date, dan Kolom Hidden"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-470
  - TC-FA-FAAM-471
  - TC-FA-FAAM-472
  - TC-FA-FAAM-473
  - TC-FA-FAAM-745
coverage:
  web: automated
---

# Modal Changelog: Search Kelas Kolom, Modified By Nama Lengkap, Tanpa Kolom Date, dan Kolom Hidden

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.changelogSeed`): Changelog contoh PRD §4.1 (Pre-setup #28) pada Asset Name `Dell Latitude` berisi entri Create, Edit, dan Delete oleh Sarah Johnson, David Kurniawan, dan Michael Wijaya, termasuk entri Edit Field `Category` (Old Value `Hardware`, New Value `IT Equipment`) dan entri Field `TAG Type`. Jumlah total entri tidak diasersi sebagai angka absolut (S-12).
- Kemampuan teknis: hapus preferensi kolom Changelog di browser (disediakan tim FE).
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`; seed API per TC dan sesi API aktor disediakan tim BE/FE).
- State global: konfigurasi kolom Changelog (preferensi di browser) diubah langkah 23 dan dikembalikan langkah 26. Hook `after` menghapus preferensi kolom di browser sebagai cadangan (bukan `[Reset to Default]`; spec ini terdaftar di `suite.md`). Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik icon Changelog

### TC-FA-FAAM-473: Placeholder Search Modal Changelog

2. Klik icon Search di toolbar modal
3. Verifikasi placeholder `Search asset name, field, action...`

### TC-FA-FAAM-470: Search Changelog kelas Action, Asset Name, Field, Old Value, New Value

4. Ketik `Edit` di kotak Search, tekan Enter
5. Verifikasi sedikitnya satu baris ber-Action `Edit` tampil (tanpa membedakan huruf besar-kecil)
6. Ganti isi kotak search dengan `latitude`, tekan Enter
7. Verifikasi baris Asset Name `Dell Latitude` tampil
8. Ganti isi kotak search dengan `category`, tekan Enter
9. Verifikasi baris Field `Category` tampil
10. Ganti isi kotak search dengan `Hardware`, tekan Enter
11. Verifikasi baris Old Value `Hardware` tampil
12. Ganti isi kotak search dengan `IT Equipment`, tekan Enter
13. Verifikasi baris New Value `IT Equipment` tampil

### TC-FA-FAAM-471: Search Changelog pada Modified By mencocokkan nama lengkap

14. Ganti isi kotak search dengan `johnson`, tekan Enter
15. Verifikasi baris entri dengan Modified By `Sarah J` tampil
16. Ganti isi kotak search dengan `sarah j`, tekan Enter
17. Verifikasi baris entri dengan Modified By `Sarah J` tampil

### TC-FA-FAAM-472: Search Changelog tidak mencari kolom Date

18. Klik `(←)` pada kotak Search
19. Baca teks kolom Date pada baris pertama tabel Changelog
20. Ketik teks Date yang dibaca pada langkah 19 di kotak Search, tekan Enter
21. Verifikasi tidak ada baris yang cocok: tabel menampilkan empty state `No results found`

### TC-FA-FAAM-745: Search Changelog tidak mencari kolom Field yang di-hide dan kembali mencari saat di-unhide

22. Klik `(←)` pada kotak Search
23. Klik header Actions (⋯), uncheck `Field` pada overlay Column Visibility, lalu tutup overlay dengan klik header Actions (⋯) lagi
24. Ketik Search `tag type`, tekan Enter
25. Verifikasi saat Field di-hide, keyword `tag type` tidak menemukan baris dan tabel menampilkan `No results found`
26. Klik header Actions (⋯), check `Field` pada overlay Column Visibility, lalu tutup overlay dengan klik header Actions (⋯) lagi
27. Ganti isi kotak search dengan `tag type`, tekan Enter
28. Verifikasi setelah di-unhide baris dengan Field `TAG Type` tampil

## Notes

- Urutan di spec: TC-FA-FAAM-473 lebih dulu karena mengamati placeholder pada kotak Search yang masih kosong; TC-FA-FAAM-745 terakhir karena mengubah konfigurasi kolom (S-10). Langkah 23 menyembunyikan Field dan langkah 26 menampilkannya kembali sehingga spec berakhir pada konfigurasi bawaan.
- Langkah penghubung (aksi tanpa `Verifikasi`): mengosongkan Search lewat `(←)` (langkah 18 dan 22), membaca teks Date baris pertama sebagai keyword (langkah 19), serta menutup overlay Column Visibility (langkah 23 dan 26).
- Asersi tidak ada kecocokan pada langkah 21 dan 25 memakai empty state `No results found` hasil Search sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAM-472 Expected "Tidak ada kecocokan" tidak menyebut tampilannya; spec mengasersi empty state `No results found` (teks dari TC-FA-FAAM-467).
  - TC-FA-FAAM-745 membutuhkan entri Changelog dengan Field `TAG Type`, dan TC-FA-FAAM-470 entri Edit Category `Hardware` ke `IT Equipment`; Pre-setup #28 tidak merinci keduanya. Spec mengandalkan seed dari tim BE.
  - TC-FA-FAAM-471 Expected menyebut baris `Sarah Johnson`, sedangkan kolom Modified By menampilkan `Sarah J`; spec mengasersi `Sarah J`.
