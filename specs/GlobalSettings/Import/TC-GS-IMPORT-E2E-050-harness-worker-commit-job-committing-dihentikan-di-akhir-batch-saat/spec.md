---
id: TC-GS-IMPORT-E2E-050-harness-worker-commit-job-committing-dihentikan-di-akhir-batch-saat
title: "Harness Worker Commit: Job Committing Dihentikan di Akhir Batch saat Entitas Suspended atau Organisasi Turun ke Plan Free"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-IMPORT-49
  - TC-GS-IMPORT-50
coverage:
  web: automated
---

# Harness Worker Commit: Job Committing Dihentikan di Akhir Batch saat Entitas Suspended atau Organisasi Turun ke Plan Free

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Akun: Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`, `Spectra.env.GS_CLIENTE_TC_PASSWORD`; login di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (Client E, dibuat ulang lewat skrip fixture sebelum tiap TC): D-34 draft Brand 250 baris `pending` (`Brand 001` sampai `Brand 250`, `brand-250.csv`; volume hanya seed, bukan objek uji). D-76 varian 1 untuk TC-GS-IMPORT-49: `created_at` dimundurkan 25 jam sehingga Unsaved Banner tampil (hanya seed backdate).
- Kemampuan teknis yang disediakan tim FE/BE (lingkungan non-produksi):
  - Kontrol worker commit D-47 mode (2): dijeda di dalam batch pertama setelah uji ulang late-binding baris batch itu dan sebelum batch selesai; jeda dilepas lewat langkah eksplisit.
  - Fixture Admin Console: ubah status Client E ke Suspended dan pulihkan ke Active; turunkan plan Client E ke Free dan pulihkan ke Growth.
  - Pembaca notifikasi lonceng dan Changelog Import.
- State global yang diubah dan dipulihkan: status dan plan Client E, kontrol worker, hasil commit (hapus Brand `Brand 001` sampai `Brand 100` hasil commit sebagian, hapus draft, reset hasil commit terakhir dan penanda Banner Hasil Commit, sesuai D-47). Hook `after` memulihkan semuanya walau spec gagal di tengah.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Menunggu: polling muat ulang tiap 5 detik dengan batas tunggu 2 menit, sesuai TC.

## Test Steps

### TC-GS-IMPORT-49: Job committing dihentikan di akhir batch saat entitas menjadi Suspended

1. Atur kontrol worker commit ke mode (2) Data Dinamis D-47
2. Klik [Import (250)]
3. Ubah status Client E menjadi Suspended lewat fixture
4. Lepaskan jeda worker commit
5. Muat ulang halaman Import setiap 5 detik sampai Staging Metric Cards menampilkan Total Rows 150 dan `[Discard]` Enabled (batas tunggu 2 menit)
6. Buka notifikasi lonceng
7. Verifikasi notifikasi beralih ke judul "Import Brand stopped"
8. Verifikasi isi notifikasi "100 records imported. 150 rows remain."
9. Verifikasi tombol `[Detail]` pada notifikasi tampil
10. Verifikasi Staging Metric Cards Total Rows 150 dan Ready to Import 150
11. Verifikasi Pagination `Showing 1 - 10 of 150 items`
12. Verifikasi footer `[Import (150)]` dan `[Discard]` Enabled
13. Verifikasi baris pertama Staging Table bernama `Brand 101`
14. Verifikasi tidak ada baris `Brand 001` sampai `Brand 100`
15. Klik tombol `[Changelog]` di header halaman
16. Verifikasi satu entri `Import Brand` teratas tercatat dengan Data "100 records imported, 0 duplicates ignored, 150 rows remaining"
17. Tutup modal Changelog
18. Pulihkan Client E ke status Active lewat fixture; reset Client E sesuai D-47 dan buat ulang draft D-34
19. Muat ulang halaman Import > Brand

### TC-GS-IMPORT-50: Job committing dihentikan di akhir batch saat organisasi turun ke plan Free

20. Atur kontrol worker commit ke mode (2) Data Dinamis D-47
21. Klik [Import (250)]
22. Turunkan plan Client E ke Free lewat fixture
23. Lepaskan jeda worker commit
24. Buka notifikasi lonceng dan buka ulang setiap 5 detik sampai notifikasi "Import Brand stopped" tampil (batas tunggu 2 menit)
25. Verifikasi notifikasi "Import Brand stopped" berisi "100 records imported. 150 rows remain."
26. Verifikasi tombol `[Detail]` pada notifikasi tampil
27. Buka menu Import dari sidebar
28. Verifikasi halaman Import tampil Disabled 🔒 dengan chip "Upgrade"
29. Verifikasi draft tersimpan tidak dapat diakses: tidak ada baris staging yang dapat dibuka
30. Pulihkan plan Client E ke Growth lewat fixture; reset Client E sesuai D-47

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (kelas d, prinsip 13d; objek uji kontrol worker commit D-47). Perubahan status dan plan Client E adalah pemicu state (P-2/P-5), bukan objek uji.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5, 24 (polling muat ulang tiap 5 detik); langkah 6, 15, 27 (membuka notifikasi, Changelog, menu Import); langkah 17 (menutup modal Changelog); langkah 18 dan 30 (pemulihan state sebelum TC berikutnya); langkah 19 (muat ulang halaman Import > Brand agar draft yang diganti fixture terbaca).
- Langkah 14 (absence baris `Brand 001` sampai `Brand 100`) memakai baris `Brand 101` langkah 13 sebagai anchor positif pada surface yang sama; langkah 29 memakai chip "Upgrade" langkah 28 sebagai anchor.
- Pembersihan state antar blok (S-03): langkah 17 menutup modal Changelog dan langkah 19 memuat ulang halaman sesudah fixture mengganti draft (langkah 18), sehingga blok TC-GS-IMPORT-50 mulai dari halaman yang memuat draft D-34 dengan 250 baris sebelum langkah 21 ([Import (250)]).
- Temuan untuk QA:
  - TC-GS-IMPORT-49 dan 50 merujuk D-47 tetapi tidak menyebut mekanisme pembacaan jumlah percobaan pelanjutan; tidak diasersi.
  - Batas tunggu 2 menit untuk polling bukan jeda ±30 detik yang dibolehkan konvensi bagian 6; spec mengikuti TC dan menuliskannya di Prerequisites.
