---
id: TC-GS-UOM-E2E-012-retensi-state-search-halaman-dan-refresh
title: "Retensi State Tab Measurement: Pindah Tab Brand, Search, Sort, Filter, Halaman, dan F5"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-3
  - TC-GS-UOM-156
coverage:
  web: automated
---

# Retensi State Tab Measurement: Pindah Tab Brand, Search, Sort, Filter, Halaman, dan F5

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables`.
- Data (hanya dibaca, spec tidak membuat atau mengubah data): Pre-setup Client A (8 unit) dan Population D-01 (12 unit), total N = 20 unit (diturunkan dari seeding; hook `before` men-seed Population secara idempotent sesuai "Data bersama" di `suite.md`). Dependensi TC-GS-UOM-36 (Population) dipenuhi oleh seeding itu; 20 unit dipakai sebagai precondition TC-GS-UOM-3 dan TC-GS-UOM-156, tidak diasersi.
- Guided Tooltip: flag halaman Measurement mengikuti pernyataan hook suite di `suite.md`. Flag `guided_tooltip_seen_gs-brand` (spec ini berpindah ke Tab Brand) juga mengikuti hook suite.
- Layar awal (Global Settings > Master Reference > Measurement) dibuka hook `beforeEach` suite.
- Kemampuan teknis: memuat ulang halaman dengan F5 (TC-GS-UOM-156).
- State global yang diubah: hanya flag Guided Tooltip Brand (dipulihkan seperti di atas). State Search dan Sort tabel Measurement dibersihkan lewat langkah pemulihan di tengah dan di akhir spec; hook `after` sebagai cadangan.

## Test Steps

### TC-GS-UOM-3: Pindah Tab Brand lalu kembali ke Measurement tidak mereset Search dan halaman

1. Ketik Search `m`, tekan Enter
2. Catat halaman aktif pada Pagination
3. Klik Tab Brand
4. Verifikasi Tab Brand tampil
5. Verifikasi Search Tab Brand kosong
6. Verifikasi Tab Brand tanpa filter aktif
7. Verifikasi sort Tab Brand pada urutan default
8. Verifikasi Tab Brand pada halaman 1
9. Klik Tab Measurement kembali
10. Verifikasi sedikitnya satu baris unit tampil pada tabel
11. Verifikasi keyword `m` tetap terisi pada kotak Search
12. Verifikasi hasil tabel tetap tersaring
13. Verifikasi halaman pagination yang aktif sama dengan halaman yang dicatat pada langkah 2

### Pemulihan state antar TC

14. Klik `(←)` pada kotak Search

### TC-GS-UOM-156: Muat ulang (F5) mempertahankan Search, Sort, Filter, dan halaman

15. Ketik Search `m`, tekan Enter
16. Klik header Symbol sekali (ascending)
17. Catat halaman aktif pada Pagination
18. Tekan F5 untuk memuat ulang halaman
19. Verifikasi sedikitnya satu baris unit tampil pada tabel
20. Verifikasi keyword `m` tetap terisi pada kotak Search
21. Verifikasi hasil tabel tetap tersaring
22. Verifikasi Sort Symbol tetap aktif dengan arah yang sama seperti sebelum muat ulang
23. Verifikasi halaman pagination yang aktif sama dengan halaman yang dicatat pada langkah 17
24. Klik `(←)` pada kotak Search dan kembalikan Sort Symbol ke urutan default (klik header Symbol dua kali lagi sampai netral)

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan; TC-GS-UOM-156 (muat ulang F5) paling akhir.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 14 dan 24 (pemulihan state tabel supaya bagian berikutnya dan spec lain mulai dari tabel default; subjudul "Pemulihan state antar TC" bukan TC sumber).
- Langkah 4 sampai 8 mewujudkan Expected c TC-GS-UOM-3 ("State Tab Brand tidak berubah oleh aksi di Tab Measurement"): Tab Brand tidak diubah oleh spec ini, sehingga state Tab Brand yang diharapkan adalah state default.
- Langkah 10 dan 19 adalah baris pembanding bagi asersi "tabel tetap tersaring" (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-GS-UOM-3 langkah uji 2 menulis "Pindah ke halaman 2 pagination (bila ada) atau catat halaman aktif" dan TC-GS-UOM-156 langkah uji 1 menulis "pindah halaman bila ada": langkah bersyarat tidak diizinkan di spec (S-08), dan Search `m` pada 20 unit diperkirakan menghasilkan kurang dari 11 baris sehingga halaman 2 tidak ada. Spec mencatat halaman aktif tanpa berpindah halaman. QA diminta menyebut keyword yang menghasilkan lebih dari satu halaman bila retensi halaman 2 memang ingin diuji.
  - TC-GS-UOM-156 pada judul menyebut Filter, tetapi langkah dan Expected tidak menerapkan Filter; spec tidak menambah Filter.
  - TC-GS-UOM-156 langkah uji 1 tidak menyebut arah Sort Symbol; spec memakai klik sekali (ascending).
