---
id: TC-AC-DS-E2E-008-state-list-loading-empty-no-result-stok-nol
title: "State List: Loading, Empty State Principal Tanpa SKU, No Result, dan SKU Stok 0 Tetap Tampil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-29
  - TC-AC-DS-30
  - TC-AC-DS-31
  - TC-AC-DS-33
coverage:
  web: automated
---

# State List: Loading, Empty State Principal Tanpa SKU, No Result, dan SKU Stok 0 Tetap Tampil

## Prerequisites

- Mode: FE+BE (respons API list ditahan lewat `Spectra.intercept()` di atas backend nyata pada TC-29).
- Akun aktor: Total Control Principal PT Arunika Prima `totalControlSku_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Jane Setiawan`), password `Spectra.env.AC_DS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (ganti akun pada TC-30): Total Control Principal Tanpa SKU `totalControlFresh_automated_{namaCompany}@qwertysystem.net` (Pre-setup #21; belum ada SKU dan belum ada entri Changelog), password `Spectra.env.AC_DS_FRESH_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): SKU inti #29 (`HHR-ARC-200` dan `TAG-ARC-OBJ` stok 0, `HHR-ARC-100` stok lebih dari 0) dan seed #30 (total 129 SKU Principal, dari seeding). Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).
- Kemampuan teknis: `Spectra.intercept()` untuk menahan lalu melepas respons API list Device SKU (path endpoint dibuka tim FE karena TC tidak menyebutnya); intercept dilepas dalam langkah spec dan oleh hook `after` bila spec gagal di tengah.
- Env var `AC_DS_TC_PASSWORD` dan `AC_DS_FRESH_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Tidak ada seeding dan tidak ada state global yang diubah.

## Test Steps

### TC-AC-DS-29: State loading

1. Tahan respons API list Device SKU dengan `Spectra.intercept()`
2. Muat ulang halaman `Settings > Device > Device SKU`
3. Verifikasi area tabel menampilkan Loading component
4. Verifikasi area tabel tidak menampilkan empty state
5. Verifikasi area tabel tidak menampilkan pesan error
6. Lepas tahanan respons API list Device SKU
7. Verifikasi baris SKU tampil setelah respons diterima

### TC-AC-DS-31: Empty state saat Search tidak menghasilkan baris

8. Ketik Search `tidak-ada-sku`, tekan Enter
9. Verifikasi tabel menampilkan ilustrasi dengan judul "No results found" dan deskripsi "Try adjusting your search or filter."
10. Verifikasi tampilan tidak memuat judul "No SKU yet"
11. Verifikasi tampilan tidak memuat pesan "Unable to load this data."
12. Klik `(←)` pada kotak Search

### TC-AC-DS-33: SKU stok 0 tidak disembunyikan

13. Ketik Search `HHR-ARC-200`, tekan Enter
14. Verifikasi baris `HHR-ARC-200` tampil dengan Current Stock `0`
15. Ganti isi kotak search dengan `TAG-ARC-OBJ`, tekan Enter
16. Verifikasi baris `TAG-ARC-OBJ` tampil dengan Current Stock `0`
17. Klik `(←)` pada kotak Search
18. Verifikasi total baris List Principal 129 SKU, mencakup SKU berstok 0 dan SKU berstok lebih dari 0

### TC-AC-DS-30: Empty state saat belum ada SKU sama sekali

19. Ganti akun: Logout dari akun Total Control Principal PT Arunika Prima
20. Login sebagai Total Control Principal Tanpa SKU `totalControlFresh_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DS_FRESH_PASSWORD`
21. Buka halaman `Settings > Device > Device SKU`
22. Verifikasi tabel menampilkan ilustrasi dengan judul "No SKU yet" dan deskripsi "Get started by creating your first SKU."
23. Verifikasi toolbar tetap tampil
24. Verifikasi tombol `[+ SKU]` tampil
25. Verifikasi tidak ada tombol `[Try Again]`
26. Verifikasi tidak ada pesan error

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-29, TC-31, TC-33, TC-30. TC-30 diletakkan terakhir karena memerlukan ganti akun ke Principal Tanpa SKU (S-07); TC lain memakai akun default spec.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 2, 6 (menahan, memuat ulang, melepas respons; hasilnya diasersi pada langkah 3 sampai 5 dan 7), 8, 13, 15 (Search; langkah 13 dan 15 menemukan baris target, R-16), 12 dan 17 (mengosongkan Search, S-09), 19 sampai 21 (ganti akun dan membuka halaman; hook `beforeEach` suite hanya membuka halaman untuk akun pertama).
- Asersi absence langkah 4 dan 5 mengikuti langkah 3 (Loading component menjadi anchor positif); langkah 10 dan 11 mengikuti langkah 9 ("No results found" menjadi anchor positif); langkah 25 dan 26 mengikuti langkah 22 sampai 24 (empty state, toolbar, dan `[+ SKU]` menjadi anchor positif).
- Temuan untuk QA:
  - S-12: asersi memakai nama literal Pre-setup #29/#30 (`HHR-ARC-200`, `TAG-ARC-OBJ`, total 129) karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan).
  - Fixture rancangan: ketersediaan Pre-setup #21 (Principal Tanpa SKU) dan #29/#30 di environment belum diverifikasi.
  - TC-33 Expected b tidak menyebut cara membaca total baris List; langkah 18 membaca total dari Pagination dan nilai 129 berasal dari seeding Pre-setup #30 (8b butir 10).
  - TC-29 dan TC-30 tidak menyebut path endpoint API list; path disediakan tim FE.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
