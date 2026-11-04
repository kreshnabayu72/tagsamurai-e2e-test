---
id: TC-FA-TDC-E2E-249-popup-used-by-setup-column-geser-urutan-kolom
title: "Popup Used By Setup Column: Geser Urutan Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-598
coverage:
  web: automated
---

# Popup Used By Setup Column: Geser Urutan Kolom

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada), kunci `exampleData` ditambah pemakai NB-1: sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; NB-1 dipakai 5 Asset Class: `AC-01 – Mesin Produksi` (Straight Line, 12 Asset Name), `AC-02 – Peralatan Kantor` (Straight Line, 30), `AC-03 – Kendaraan Operasional` (Declining Balance, 7), `AC-04 – Komputer` (Declining Balance, 25), `AC-05 – Furnitur` (Straight Line, 18). Urutan awal kolom Popup Used By adalah default `Asset Class | Tax Method | Asset Names`.
- Tabel "Kolom yang diuji" (parameter langkah 2 sampai 10, dijalankan berurutan tanpa pemulihan di antara iterasi; kolom yang digeser pada iterasi berikutnya dimulai dari susunan hasil iterasi sebelumnya):

  | Iterasi | Kolom |
  |---|---|
  | 1 | Asset Class |
  | 2 | Tax Method |
  | 3 | Asset Names |

- Kemampuan teknis: Popup Setup Column pada Popup Used By; drag and drop kolom; konfigurasi kolom Popup Used By tersimpan di browser dan dibaca ulang setelah muat ulang halaman; pemulihan lewat langkah eksplisit (8b.14, R-24).
- State global yang diubah: urutan kolom Popup Used By digeser pada langkah 4 dan dikembalikan ke `Asset Class | Tax Method | Asset Names` pada langkah 13 sampai 15. Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### TC-FA-TDC-598: Geser urutan kolom di Popup Setup Column Popup Used By: 3 kolom default

1. Klik angka `5` pada baris NB-1 untuk membuka Popup Used By

Untuk setiap baris tabel "Kolom yang diuji" (langkah 2 sampai 10), dengan `{kolom}` = nilai kolom Kolom pada iterasi itu:

2. Klik icon `⋯` pada header kolom Actions
3. Klik `Setup Column...`
4. Drag kolom `{kolom}` ke posisi paling atas daftar
5. Verifikasi Live Preview menempatkan `{kolom}` sebagai kolom pertama
6. Klik `[Save]`
7. Verifikasi urutan tabel setelah Save menempatkan `{kolom}` sebagai kolom pertama
8. Muat ulang halaman (F5)
9. Klik angka `5` pada baris NB-1 untuk membuka kembali Popup Used By
10. Verifikasi urutan tabel tetap menempatkan `{kolom}` sebagai kolom pertama setelah F5

Pemulihan urutan kolom:

11. Klik icon `⋯` pada header kolom Actions
12. Klik `Setup Column...`
13. Drag kolom `Asset Class` ke posisi paling atas daftar
14. Drag kolom `Tax Method` ke posisi kedua daftar
15. Klik `[Save]`
16. Tutup Popup Used By lewat ikon Close `(X)`

## Notes

- Langkah berulang (8b.7): langkah 2 sampai 10 diulang tiga kali (satu iterasi per baris tabel "Kolom yang diuji"); parameter tiap iterasi hanya `{kolom}`, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa (S-01). Dengan ekspansi spec ini 34 langkah (1 langkah pembuka, 3 x 9 langkah berulang, dan 6 langkah pemulihan).
- Langkah penghubung (S-03): langkah 8 dan 9 (muat ulang dan membuka kembali popup), langkah 11 sampai 15 (pemulihan urutan kolom; 8b.14, R-24; hasilnya tidak diasersi), langkah 16 (menutup popup). Tabel utama memuat sembilan baris pada satu halaman; baris NB-1 tidak perlu dicari lewat Search (8b.13).
- Interpretasi TC-FA-TDC-598: langkah 4 TC dijalankan berurutan per kolom tanpa pemulihan di antara iterasi; susunan setelah iterasi 1 adalah `Asset Class | Tax Method | Asset Names`, setelah iterasi 2 `Tax Method | Asset Class | Asset Names`, dan setelah iterasi 3 `Asset Names | Tax Method | Asset Class`.
- Temuan untuk QA:
  - TC-FA-TDC-598: drag Asset Class ke posisi paling atas pada iterasi 1 tidak mengubah urutan karena Asset Class sudah di posisi atas; TC tidak menyebut hal ini dan Expected a hanya mengasersi Asset Class sebagai kolom pertama.
  - TC-FA-TDC-598 tidak menyatakan apakah susunan dipulihkan di antara iterasi; spec memulihkan hanya di akhir.
  - Email akun Total Control tidak tertulis di TC.
