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
- Data Dinamis (Client E, disiapkan lewat skrip fixture oleh langkah 1 untuk TC-GS-IMPORT-49 dan dibuat ulang oleh langkah 30 untuk TC-GS-IMPORT-50): D-34 draft Brand 250 baris `pending` (`Brand 001` sampai `Brand 250`, `brand-250.csv`; volume hanya seed, bukan objek uji). D-76 varian 1 untuk TC-GS-IMPORT-49: `created_at` dimundurkan 25 jam sehingga Unsaved Banner tampil (hanya seed backdate).
- Kemampuan teknis yang disediakan tim FE/BE (lingkungan non-produksi):
  - Kontrol worker commit D-47 mode (2): dijeda di dalam batch pertama setelah uji ulang late-binding baris batch itu dan sebelum batch selesai; jeda dilepas lewat langkah eksplisit.
  - Fixture Admin Console: ubah status Client E ke Suspended dan pulihkan ke Active; turunkan plan Client E ke Free dan pulihkan ke Growth.
  - Pembaca notifikasi lonceng dan Changelog Import.
- State global yang diubah dan dipulihkan: status dan plan Client E, kontrol worker, hasil commit (hapus Brand `Brand 001` sampai `Brand 100` hasil commit sebagian, hapus draft, reset hasil commit terakhir dan penanda Banner Hasil Commit, sesuai D-47). Hook `after` memulihkan semuanya walau spec gagal di tengah.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk akun aktor diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Menunggu: polling muat ulang tiap 5 detik dengan batas tunggu 2 menit, sesuai TC.

## Test Steps

### TC-GS-IMPORT-49: Job committing dihentikan di akhir batch saat entitas menjadi Suspended

1. Siapkan lewat skrip fixture draft Brand D-34 pada Client E (250 baris `pending`, `brand-250.csv`) dan mundurkan `created_at` draft 25 jam (D-76 varian 1), lalu muat ulang halaman Import > Brand
2. Atur kontrol worker commit ke mode (2) Data Dinamis D-47
3. Klik tombol `[Changelog]` di header halaman
4. Klik icon Filter
5. Pilih Action `Import Brand` pada dropdown Action
6. Klik `[Apply]`
7. Catat angka total pada teks Pagination (Showing [From] - [To] of [N] items; 0 bila yang tampil adalah empty state) sebagai baseline Changelog Import
8. Tutup modal Changelog
9. Klik [Import (250)]
10. Tunggu aksi selesai (permintaan mendapat respons)
11. Ubah status Client E menjadi Suspended lewat fixture
12. Lepaskan jeda worker commit
13. Muat ulang halaman Import setiap 5 detik sampai Staging Metric Cards menampilkan Total Rows 150 dan `[Discard]` Enabled (batas tunggu 2 menit)
14. Buka notifikasi lonceng
15. Verifikasi notifikasi beralih ke judul "Import Brand stopped"
16. Verifikasi isi notifikasi "100 records imported. 150 rows remain."
17. Verifikasi tombol `[Detail]` pada notifikasi tampil
18. Verifikasi Staging Metric Cards Total Rows 150 dan Ready to Import 150
19. Verifikasi Pagination `Showing 1 - 10 of 150 items`
20. Verifikasi footer `[Import (150)]` dan `[Discard]` Enabled
21. Verifikasi baris pertama Staging Table bernama `Brand 101`
22. Verifikasi tidak ada baris `Brand 001` sampai `Brand 100`
23. Klik tombol `[Changelog]` di header halaman
24. Klik icon Filter
25. Pilih Action `Import Brand` pada dropdown Action
26. Klik `[Apply]`
27. Verifikasi total pada Pagination Changelog Import dengan Filter Action `Import Brand` bertambah tepat satu dibanding baseline langkah 7
28. Verifikasi satu entri `Import Brand` teratas tercatat dengan Data "100 records imported, 0 duplicates ignored, 150 rows remaining"
29. Tutup modal Changelog
30. Pulihkan Client E ke status Active lewat fixture; reset Client E sesuai D-47 dan buat ulang draft D-34
31. Muat ulang halaman Import > Brand
32. Buka notifikasi lonceng
33. Catat jumlah notifikasi "Import Brand stopped" pada lonceng sebagai baseline
34. Tutup lonceng notifikasi

### TC-GS-IMPORT-50: Job committing dihentikan di akhir batch saat organisasi turun ke plan Free

35. Atur kontrol worker commit ke mode (2) Data Dinamis D-47
36. Klik [Import (250)]
37. Tunggu aksi selesai (permintaan mendapat respons)
38. Turunkan plan Client E ke Free lewat fixture
39. Lepaskan jeda worker commit
40. Buka notifikasi lonceng dan buka ulang setiap 5 detik sampai jumlah notifikasi "Import Brand stopped" bertambah dibanding baseline langkah 33 (batas tunggu 2 menit)
41. Verifikasi notifikasi "Import Brand stopped" yang baru berisi "100 records imported. 150 rows remain."
42. Verifikasi tombol `[Detail]` pada notifikasi tampil
43. Muat ulang halaman Import
44. Verifikasi halaman Import tampil Disabled 🔒 dengan chip "Upgrade"
45. Verifikasi draft tersimpan tidak dapat diakses: tidak ada baris staging yang dapat dibuka
46. Pulihkan plan Client E ke Growth lewat fixture; reset Client E sesuai D-47

## Notes

- Spec melewati sekitar 35 langkah (46 langkah). Seluruhnya satu topik dengan akun dan client yang sama; memecahnya hanya menambah login, hook, dan pembersihan tanpa menambah daya deteksi.
- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (kelas d, prinsip 13d; objek uji kontrol worker commit D-47). Perubahan status dan plan Client E adalah pemicu state (P-2/P-5), bukan objek uji.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (seed draft D-34 dan D-76 varian 1); langkah 13, 40 (polling muat ulang tiap 5 detik); langkah 14 dan 23 (membuka notifikasi dan Changelog); langkah 43 (muat ulang halaman Import); langkah 3 sampai 6 dan 24 sampai 26 (membuka Changelog Import dan memfilter Action `Import Brand`); langkah 7 (baseline Changelog Import, S-12); langkah 8 dan 29 (menutup modal Changelog); langkah 32 sampai 34 (baseline notifikasi "Import Brand stopped" sebelum Import TC-GS-IMPORT-50, S-12); langkah 30 dan 46 (pemulihan state sebelum TC berikutnya); langkah 31 (muat ulang halaman Import > Brand agar draft yang diganti fixture terbaca). Langkah 10, 37 (Tunggu aksi selesai: menunggu aksi tanpa `Verifikasi` selesai sebelum perubahan status atau plan Client E lewat fixture; penanda permintaan mendapat respons).
- Langkah 22 (absence baris `Brand 001` sampai `Brand 100`) memakai baris `Brand 101` langkah 21 sebagai anchor positif pada surface yang sama; langkah 45 memakai chip "Upgrade" langkah 44 sebagai anchor.
- Langkah 24 sampai 27 dan langkah 3 sampai 8 (D-14): jumlah entri Changelog Import dibaca dengan Filter Action `Import Brand` sebelum `[Import (250)]` dan dibandingkan sesudahnya; langkah 28 (entri teratas) menjadi asersi tambahan pada hasil terfilter. Langkah 32 sampai 34 mencatat jumlah notifikasi "Import Brand stopped" sebelum pemicu TC-GS-IMPORT-50 supaya polling langkah 40 tidak berhenti pada notifikasi lama dari TC-GS-IMPORT-49. Asersi baseline ini di luar Expected TC (S-03).
- Pembersihan state antar blok (S-03): langkah 29 menutup modal Changelog dan langkah 31 memuat ulang halaman sesudah fixture mengganti draft (langkah 30), sehingga blok TC-GS-IMPORT-50 mulai dari halaman yang memuat draft D-34 dengan 250 baris sebelum langkah 36 ([Import (250)]).
- Temuan untuk QA:
  - TC-GS-IMPORT-49 dan 50 merujuk D-47 tetapi tidak menyebut mekanisme pembacaan jumlah percobaan pelanjutan; tidak diasersi.
  - Batas tunggu 2 menit untuk polling bukan jeda ±30 detik yang dibolehkan konvensi bagian 6; spec mengikuti TC dan menuliskannya di Prerequisites.
  - Penanda selesai untuk langkah 10 dan 37 (klik `[Import (250)]` sebelum fixture mengubah status atau plan Client E) tidak disebut di TC, PRD, atau spec ini; langkah "Tunggu aksi selesai" memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati di surface Total Control Client E.
