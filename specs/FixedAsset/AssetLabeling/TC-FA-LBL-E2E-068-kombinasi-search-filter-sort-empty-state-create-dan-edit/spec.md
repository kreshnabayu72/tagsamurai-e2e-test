---
id: TC-FA-LBL-E2E-068-kombinasi-search-filter-sort-empty-state-create-dan-edit
title: "Kombinasi Search dan Filter Labels List: Empty State, Create, dan Edit saat Search Aktif"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-252
  - TC-FA-LBL-253
  - TC-FA-LBL-254
coverage:
  web: automated
---

# Kombinasi Search dan Filter Labels List: Empty State, Create, dan Edit saat Search Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 (katalog Company Alpha, 9 label; hanya dibaca, tidak diubah; Total Asset berasal dari Pre-setup #13):

  | Label | Modified By |
  |---|---|
  | `High Priority` | `Sarah J` |
  | `Finance Department` | `David K` |
  | `Audit Ready` | `Sarah J` |
  | `Executive Asset` | `Michael W` |
  | `Maintenance Due` | `David K` |
  | `Seasonal Event` | `Michael W` |
  | `Night Shift` | `Sarah J` |
  | `Warehouse Priority` | `Sarah J` |
  | `Field Kit` | `David K` |

- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor Total Control untuk membuat label; fixture BE untuk menghapus label.
- Data Dinamis (sufiks `{runId}-068`, `{runId}` hanya digit): label `Filtered Create 253 {runId}-068` (dibuat lewat UI di blok TC-FA-LBL-253) dan label `Finance Edit 254 {runId}-068` (seed lewat sesi API, diubah namanya lewat UI menjadi `Treasury Edit 254 {runId}-068`); keduanya dihapus di hook `after` lewat fixture BE (tidak berasumsi aksi berhasil penuh).
- State global: tidak ada yang diubah selain label Data Dinamis di atas.

## Test Steps

### TC-FA-LBL-252: Pemulihan dari empty state setelah melepas salah satu saringan

1. Ketik Search `Finance`, tekan Enter
2. Klik icon Filter di Table Tools
3. Pilih `Modified By` = `Michael W`
4. Klik `[Apply]`
5. Verifikasi empty state `No results found`
6. Kosongkan isi kotak search, tekan Enter
7. Verifikasi dua baris `Michael W` tampil kembali: `Executive Asset`, `Seasonal Event`
8. Pulihkan: klik `[Clear Field]`, klik `[Apply]`, klik area di luar panel, lalu klik `(←)` pada kotak Search

### TC-FA-LBL-253: Create label yang tidak cocok dengan Search aktif tidak muncul di tabel tersaring

9. Ketik Search `Finance`, tekan Enter
10. Verifikasi tabel memuat `Finance Department`
11. Klik `[+ Label]`
12. Ketik `Filtered Create 253 {runId}-068` di Label Name
13. Klik `[Submit]`
14. Tunggu aksi `[Submit]` selesai (modal Create tertutup)
15. Verifikasi tabel tetap hanya memuat `Finance Department`
16. Klik `(←)` pada kotak Search
17. Verifikasi baris `Filtered Create 253 {runId}-068` tampil setelah Search dikosongkan

### TC-FA-LBL-254: Edit yang membuat nama tidak cocok dengan Search aktif menghilangkan baris dari view

18. Lewat sesi API akun Total Control, buat label `Finance Edit 254 {runId}-068` hingga label tersimpan
19. Ketik Search `Finance`, tekan Enter
20. Verifikasi tabel memuat `Finance Department` dan `Finance Edit 254 {runId}-068`
21. Klik `⋯` pada baris `Finance Edit 254 {runId}-068`, lalu klik `Edit`
22. Ganti isi Label Name dengan `Treasury Edit 254 {runId}-068`
23. Klik `[Save]`
24. Tunggu aksi `[Save]` selesai (modal Edit tertutup)
25. Verifikasi tabel masih memuat `Finance Department`
26. Verifikasi baris `Treasury Edit 254 {runId}-068` hilang dari tabel tersaring karena tidak cocok dengan keyword

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4a dan 3a/3b (alur Create dan Edit label).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 8 memulihkan Search, Filter, dan panel; langkah 14 dan 24 menunggu aksi tulis selesai sebelum asersi absence (bagian 8b butir 8 dan butir 2); langkah 18 menyiapkan label seed `Finance Edit 254` tepat sebelum blok TC-FA-LBL-254 agar Search `Finance` pada TC-FA-LBL-252 dan TC-FA-LBL-253 tetap hanya menemukan `Finance Department`.
- Verifikasi `Finance Department` pada langkah 10, 20, dan 25 adalah anchor positif bahwa tabel tersaring sudah dimuat sebelum asersi absence (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-LBL-253 dan TC-FA-LBL-254 tidak menyebut toast hasil Create dan Edit; spec tidak mengasersi toast dan memakai penutupan modal sebagai penanda aksi selesai.
  - TC-FA-LBL-253 Expected "tidak tampil sampai Search dikosongkan" menyiratkan baris muncul sesudah Search dikosongkan; spec mengasersinya di langkah akhir blok.
