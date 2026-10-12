---
id: TC-GS-BRAND-E2E-003-retensi-state-search-filter-sort-dan-refresh
title: "Retensi State Tab Brand: Search, Filter, Sort, Halaman, Pindah Tab, dan Refresh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-4
  - TC-GS-BRAND-5
  - TC-GS-BRAND-153
coverage:
  web: automated
---

# Retensi State Tab Brand: Search, Filter, Sort, Halaman, Pindah Tab, dan Refresh

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (12 brand, data environment tetap), termasuk Vertex Labs dengan Used By (Items) = 5 (satu-satunya brand dengan Used By >= 5).
- Data Dinamis: Population D-01 (12 brand, Apex Tools sampai Linear Dynamics, nama literal tanpa suffix karena asersi jumlah dan halaman bergantung pada kumpulan nama ini) di-seed lewat API di hook `before` (setara TC-GS-BRAND-1) secara idempotent: nama yang sudah ada di Client A dilewati, sehingga total tetap 24 brand. Suite berjalan serial, jadi tidak ada spec lain yang men-seed atau menghapus Population bersamaan. Hook `after` hanya menghapus brand yang dibuat spec ini lewat API. Pembersihan tidak berasumsi seeding berhasil penuh.
- Guided Tooltip: hook `before` mencatat nilai awal flag `guided_tooltip_seen_gs-brand` lalu menyetelnya ke true lewat API; hook `after` memulihkan nilai awal.
- Kemampuan teknis: memuat ulang halaman dengan F5 dan menjaga Tab Measurement tidak membawa state Tab Brand (TC-GS-BRAND-4 dan TC-GS-BRAND-5).
- State global yang diubah: flag Guided Tooltip (dipulihkan seperti di atas). State Search/Filter/Sort/halaman tabel Brand dibersihkan lewat langkah pemulihan di tengah dan di akhir spec; hook `after` menjadi cadangan.

## Test Steps

### TC-GS-BRAND-4: Pindah Tab Measurement lalu kembali ke Brand mempertahankan Search dan halaman

1. Buka Global Settings > Master Reference dari sidebar → tab Brand tampil dengan 24 brand
2. Klik icon Search, ketik `o`, tekan Enter
3. Pindah ke halaman 2
4. Klik Tab Measurement
5. Verifikasi Tab Measurement tampil dengan state default miliknya: Search kosong, tanpa filter aktif, sort default, halaman 1
6. Verifikasi Tab Measurement tidak membawa keyword `o` atau halaman 2 dari Tab Brand
7. Klik Tab Brand kembali
8. Verifikasi keyword `o` tetap terisi dan tabel tetap tersaring
9. Verifikasi halaman 2 tetap aktif

### Pemulihan state antar TC

10. Hapus keyword Search dan kembalikan tabel ke halaman 1 dengan 24 brand tanpa filter dan tanpa sort

### TC-GS-BRAND-5: Pindah Tab mempertahankan Filter dan Sort tab Brand

11. Klik Filter, atur Used By (Items) Min `5`, klik [Apply]
12. Klik header Brand Name sampai urutan descending
13. Klik Tab Measurement
14. Verifikasi Tab Measurement tampil dengan state default miliknya: Search kosong, tanpa filter aktif, sort default, halaman 1
15. Verifikasi Tab Measurement tidak membawa Filter Used By (Items) atau Sort Brand Name dari Tab Brand
16. Klik Tab Brand kembali
17. Verifikasi Filter Used By (Items) Min `5` tetap aktif
18. Verifikasi hanya Vertex Labs yang tampil
19. Verifikasi Sort Brand Name descending tetap aktif

### Pemulihan state antar TC

20. Reset Filter Used By (Items) dan kembalikan Sort Brand Name ke urutan default (A-Z) sehingga tabel kembali menampilkan 24 brand di halaman 1

### TC-GS-BRAND-153: Refresh F5 mempertahankan Search, Filter, Sort, dan halaman

21. Klik icon Search, ketik `o`, tekan Enter
22. Klik header Brand Name sampai urutan descending
23. Pindah ke halaman 2
24. Tekan F5 untuk memuat ulang halaman
25. Verifikasi keyword `o` tetap terisi
26. Verifikasi Sort Brand Name descending tetap aktif
27. Verifikasi halaman 2 tetap aktif
28. Hapus keyword Search dan kembalikan Sort ke urutan default (A-Z) di halaman 1

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan; TC-GS-BRAND-153 (muat ulang F5) paling akhir.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 10, 20, dan 28 (pemulihan state tabel supaya TC berikutnya mulai dari tabel default 24 brand; subjudul "Pemulihan state antar TC" bukan TC sumber).
- Ketiga TC punya dependensi TC-GS-BRAND-1 (Population); di spec ini Population di-seed lewat API di hook `before`.
- Langkah 5 dan 14 mengikuti Expected Result c TC-GS-BRAND-4 dan TC-GS-BRAND-5 (state default Tab Measurement); langkah 6 dan 15 mengikuti klausa "tidak membawa" pada butir yang sama. Keduanya dijalankan saat Tab Measurement aktif (setelah langkah 4 dan 13).
