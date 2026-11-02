---
id: TC-FA-GRP-E2E-158-modal-changelog-pagination-default-navigasi-dan-reset-ke-halaman-1-saat-search-filter
title: "Modal Changelog Pagination: Default dan Page Size, Navigasi, serta Reset ke Halaman 1 Saat Search/Filter dari Halaman 2"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-517
  - TC-FA-GRP-518
  - TC-FA-GRP-1060
coverage:
  web: automated
---

# Modal Changelog Pagination: Default dan Page Size, Navigasi, serta Reset ke Halaman 1 Saat Search/Filter dari Halaman 2

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-158`, bagian 5), dibuat lewat API di `before` oleh akun aktor: group `Pg Log {runId}-158` (level 1) dengan 26 aksi Edit Description berturut-turut (`Pg Edit 01` sampai `Pg Edit 26`). Hasilnya adalah 27 entri Changelog terbaru (1 Create dan 26 Edit), sehingga Changelog client memuat >= 25 entri dengan >= 11 entri Action `Edit` dan tampilan aktif >= 26 baris. Total entri Changelog tidak diasersi sebagai angka absolut (audit trail permanen, S-12); halaman aktif diamati lewat indikator nomor halaman dan jumlah baris.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API group `Pg Log {runId}-158`. Entri Changelog permanen tidak dihapus.

## Test Steps

1. Klik icon Changelog

### TC-FA-GRP-517: Default dan pilihan page size

2. Verifikasi footer pagination tampil
3. Verifikasi default 10 baris per halaman
4. Buka dropdown page size
5. Verifikasi pilihan page size 10, 25, 50, dan 100
6. Pilih page size 25
7. Verifikasi tabel menampilkan 25 baris
8. Pilih page size 50
9. Verifikasi tabel menampilkan lebih dari 25 baris dan paling banyak 50 baris
10. Pilih page size 100
11. Verifikasi tabel menampilkan lebih dari 25 baris dan paling banyak 100 baris
12. Pilih page size 10
13. Verifikasi tabel menampilkan 10 baris

### TC-FA-GRP-518: Navigasi prev/next dan input nomor halaman

14. Klik tombol next
15. Verifikasi indikator halaman aktif menunjukkan halaman 2
16. Klik tombol prev
17. Verifikasi indikator halaman aktif menunjukkan halaman 1
18. Ketik nomor halaman `3` pada input halaman, tekan Enter
19. Verifikasi indikator halaman aktif menunjukkan halaman 3

### TC-FA-GRP-1060: Search dan Filter dari halaman 2 mereset ke halaman 1

20. Klik input halaman, ketik `1`, tekan Enter
21. Pindah ke halaman 2 lewat pagination
22. Klik icon Search
23. Ketik Search `Edit`, tekan Enter
24. Verifikasi indikator halaman aktif menunjukkan halaman 1 dari hasil search, bukan halaman 2
25. Pindah ke halaman 2 lewat pagination
26. Klik icon Filter
27. Pilih `Edit` pada dropdown Action
28. Klik [Apply]
29. Verifikasi indikator halaman aktif menunjukkan halaman 1 dari hasil filter, bukan halaman 2
30. Pindah ke halaman 2 lewat pagination
31. Klik icon Filter
32. Klik [Clear Field]
33. Klik [Apply]
34. Verifikasi indikator halaman aktif menunjukkan halaman 1 dengan seluruh data, bukan halaman 2
35. Klik `(←)` pada kotak Search
36. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka dan menutup Modal Changelog, kembali ke halaman 1 sebelum TC-FA-GRP-1060, berpindah halaman, dan `(←)` pada kotak Search (S-03, S-09, R-16).
- Seeding 26 aksi Edit pada `Pg Log` memenuhi syarat >= 25 entri dan >= 11 entri Edit pada TC-FA-GRP-1060 serta tampilan >= 26 baris pada TC-FA-GRP-517/518 tanpa mengubah data Pre-setup (S-06).
- Search `Edit` pada TC-FA-GRP-1060 sengaja tanpa batas suffix spec karena keyword adalah objek uji; hasilnya >= 26 baris sehingga halaman 2 tersedia.
- Spec 36 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - TC-FA-GRP-517 Expected b ("jumlah baris menyesuaikan pilihan") untuk page size 50 dan 100 bergantung pada total entri Changelog yang bertambah tiap run; spec mengasersi batas atas dan lebih dari 25 baris (S-12).
  - Total Changelog tidak dapat diasersi sebagai angka absolut (audit trail permanen).
