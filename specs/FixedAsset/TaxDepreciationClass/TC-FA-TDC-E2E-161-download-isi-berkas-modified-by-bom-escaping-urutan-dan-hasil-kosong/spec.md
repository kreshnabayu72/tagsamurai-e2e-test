---
id: TC-FA-TDC-E2E-161-download-isi-berkas-modified-by-bom-escaping-urutan-dan-hasil-kosong
title: "Download Isi Berkas: Modified By, BOM, Escaping, Urutan, dan Hasil Kosong"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-574
  - TC-FA-TDC-575
  - TC-FA-TDC-576
  - TC-FA-TDC-577
sourceRules: ["§4.1.1#r12", "§3.9#r13", "T-11a", "F-FATDC-12.k2", "§5#b7"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r12": 6
  "§3.9#r13": 16
  "T-11a": 19
  "F-FATDC-12.k2": [20, 21]
  "§5#b7": 20
anchor: [13, 27, 28, 29]
coverage:
  web: automated
---

# Download Isi Berkas: Modified By, BOM, Escaping, Urutan, dan Hasil Kosong

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada), kunci `exampleData`: sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; NB-SL terakhir diubah oleh user bernama lengkap `Rina Putri` (user penyunting disediakan tim FE). Nilai Used By untuk urutan: NB-1 5, NB-SL 4, NB-2 3, BLD-P 1, dan BLD-NP, LAND, NB-4, NB-KHS, NB-OLD masing-masing 0.
- Data Dinamis (milik spec, dipakai TC-FA-TDC-575 pada langkah 23): satu class tambahan dengan Class Name literal `Kelompok "A", khusus` dan Class Code `KHS-ESC-{runId}-161`; nilai field wajib lain (Asset Type, Useful Life, Allowed Methods) tidak disebut TC dan diisi seeding minimal oleh tim FE (lihat Temuan untuk QA). Class dihapus lewat seeding API pada langkah 30 dan di hook `after`.
- Kemampuan teknis: seeding class lewat API; membuka berkas unduhan CSV dengan editor teks (encoding, BOM, pemisah, escaping) disediakan tim FE; Overlay Column Visibility; Overlay Download; sort header; Search; pemulihan Setup Column dengan langkah eksplisit (8b.14, R-24).
- State global yang diubah: kolom Modified By ditampilkan lalu disembunyikan kembali (langkah 1 sampai 3 dan 7 sampai 9), sort Used By dikembalikan ke default (langkah 14), Search dikosongkan (langkah 22). Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### TC-FA-TDC-574: Download menulis Modified By sebagai nama lengkap

1. Klik header Actions `⋯`
2. Centang kolom Modified By
3. Tutup Overlay Column Visibility
4. Klik icon Download
5. Klik `Download as CSV` lalu buka berkas
6. Verifikasi kolom Modified By baris NB-SL berisi `Rina Putri` (bukan `Rina P`)
7. Klik header Actions `⋯`
8. Hapus centang kolom Modified By
9. Tutup Overlay Column Visibility

### TC-FA-TDC-576: Urutan baris berkas mengikuti sort aktif

10. Klik header Used By dua kali (Descending)
11. Klik icon Download
12. Klik `Download as CSV` lalu buka berkas
13. Verifikasi baris berkas berurutan NB-1, NB-SL, NB-2, BLD-P, lalu BLD-NP, LAND, NB-4, NB-KHS, NB-OLD
14. Klik header Used By sekali lagi hingga urutan kembali ke default Class Code A-Z

### TC-FA-TDC-577: Download saat hasil Search kosong menghasilkan berkas berisi header saja

15. Ketik Search `zzzz`, tekan Enter
16. Verifikasi tombol Download tetap aktif
17. Klik icon Download
18. Klik `Download as CSV` lalu buka berkas
19. Verifikasi tidak ada toast
20. Verifikasi berkas berisi baris header kolom yang tampil
21. Verifikasi berkas tidak memuat baris data
22. Klik `(←)` pada kotak Search

### TC-FA-TDC-575: Download CSV: encoding UTF-8 dengan BOM dan escaping nilai

23. Tambahkan class dengan Class Name `Kelompok "A", khusus` lewat seeding API (Class Code `KHS-ESC-{runId}-161`), lalu muat ulang halaman
24. Klik icon Download
25. Klik `Download as CSV`
26. Buka berkas dengan editor teks
27. Verifikasi berkas berencoding UTF-8 dengan BOM
28. Verifikasi berkas memakai pemisah koma
29. Verifikasi nilai Class Name dibungkus tanda kutip ganda dan tanda kutip di dalamnya digandakan: `"Kelompok ""A"", khusus"`
30. Hapus class `KHS-ESC-{runId}-161` lewat seeding API, lalu muat ulang halaman

## Notes

- Urutan TC dalam spec: TC-FA-TDC-574, 576, 577, 575. TC-FA-TDC-575 membutuhkan satu class tambahan sehingga diletakkan paling akhir dan class dihapus di akhir spec (langkah 30); TC lain memakai sembilan class Example Data.
- Langkah penghubung (S-03): langkah 3 dan 9 (menutup Overlay), langkah 7 sampai 9 (menyembunyikan kembali kolom Modified By; pemulihan Setup Column 8b.14, R-24; TC tidak menyebut `[Save]`), langkah 14 (mengembalikan sort ke default), langkah 22 (mengosongkan Search; 8b.9), langkah 23 dan 30 (seeding API).
- Asersi absence langkah 19 diletakkan segera setelah pemicu sebelum asersi berkas (8b.11); anchor positif: hasil Search kosong dan tombol Download aktif (langkah 16), serta berkas yang dibuka pada langkah 18.
- Pada langkah 6, 13, 20, 21, dan 27 sampai 29 isi berkas (kelas f) dibaca dari berkas yang diunduh pada langkah sebelumnya dalam TC yang sama.
- Temuan untuk QA:
  - TC-FA-TDC-574 tidak menyebut cara menampilkan kolom Modified By dan nama lengkap user penyunting selain `Rina Putri`; spec memakai Overlay Column Visibility.
  - TC-FA-TDC-575 hanya menyebut Class Name `Kelompok "A", khusus` tanpa Class Code, Asset Type, Useful Life, dan Allowed Methods; kode `KHS-ESC-{runId}-161` ditetapkan penulis spec dan nilai field lain diisi seeding minimal. TC juga tidak menyebut apakah class itu termasuk sembilan class Example Data; spec menambahkannya sebagai class kesepuluh.
  - TC-FA-TDC-576 tidak menyebut cara mengembalikan sort ke default; spec menekan header Used By sekali lagi (asumsi siklus tiga klik seperti TC-FA-TDC-587).
  - TC-FA-TDC-577 butir b "tanpa toast" tidak memberi langkah observasi spesifik; spec mengasersinya segera setelah pemicu.
  - Email akun Total Control tidak tertulis di TC.
