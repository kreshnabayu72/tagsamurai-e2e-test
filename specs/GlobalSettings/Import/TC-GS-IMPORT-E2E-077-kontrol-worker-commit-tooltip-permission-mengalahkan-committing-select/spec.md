---
id: TC-GS-IMPORT-E2E-077-kontrol-worker-commit-tooltip-permission-mengalahkan-committing-select
title: "Kontrol Worker Commit: Tooltip Permission Mengalahkan Committing, Select All Mengecualikan Baris Batch Aktif, dan Import In Progress Ditolak Tanpa Take Over"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-208
  - TC-GS-IMPORT-692
  - TC-GS-IMPORT-869@L1078
coverage:
  web: automated
---

# Kontrol Worker Commit: Tooltip Permission Mengalahkan Committing, Select All Mengecualikan Baris Batch Aktif, dan Import In Progress Ditolak Tanpa Take Over

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`) karena spec mengubah kontrol worker commit; lihat `suite.md`.
- Akun, password lewat env:
  - Client E: Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`, `Spectra.env.GS_CLIENTE_TC_PASSWORD` (login di hook `before`); Import data (Read Only) Client E (Indra Gunawan) `importRead_automated_qaTeam5@qwertysystem.net`, `Spectra.env.GS_CLIENTE_IMPORTRO_PASSWORD` (sesi browser terpisah untuk TC-GS-IMPORT-208).
  - Pelaku kedua TC-GS-IMPORT-869@L1078: Admin kedua Client E (Dimas Anggoro) `totalControlSecond_automated_qaTeam5@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTE_TC2_PASSWORD`, hanya lewat sesi API untuk permintaan Import fixture (memulai commit); tidak ada sesi UI kedua karena hasil di sesi itu tidak diasersi. Sesi UI TC-GS-IMPORT-869@L1078 memakai Total Control Client E (login di hook `before`).
  - Password tidak ditulis di spec atau fixture. Hook `after` menutup konteks kedua, melanjutkan worker, dan mengembalikan sesi ke akun default suite.
- Data Dinamis: Client E D-34 draft Brand 250 baris `pending` (`Brand 001` sampai `Brand 250`, `brand-250.csv`), disiapkan oleh langkah 1 dan dibuat ulang oleh langkah 10; D-76 varian 1 (`created_at` dimundurkan 25 jam, hanya seed backdate) sehingga Unsaved Banner tampil pada TC-GS-IMPORT-208, disiapkan oleh langkah 1. Client E D-50 draft Brand 12 baris `pending` dari `brand-12.csv` untuk TC-GS-IMPORT-869@L1078, disiapkan oleh langkah 28.
- Kemampuan teknis yang disediakan tim FE/BE (lingkungan non-produksi): kontrol worker commit D-47 mode (1) (dijeda sebelum job mulai sehingga job tetap `committing`) untuk ketiga TC.
- State global yang diubah dan dipulihkan: kontrol worker (dilanjutkan), hasil commit dan draft Client E sesuai D-47 (termasuk 12 Brand hasil commit draft D-50 pada TC-GS-IMPORT-869@L1078). Hook `after` memulihkan walau spec gagal di tengah.
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > Brand untuk akun aktor pertama. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk semua akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.

## Test Steps

### TC-GS-IMPORT-208: Prioritas tooltip, permission mengalahkan committing pada [Discard]

1. Reset Client E ke tanpa draft; seed draft D-34 dan D-76 varian 1 (mundurkan `created_at` 25 jam) lewat skrip fixture
2. [Sesi TC Client E] Muat ulang halaman Import > Brand
3. [Sesi TC Client E] Jeda worker commit (kontrol worker D-47)
4. [Sesi TC Client E] Klik `[Import (250)]`
5. [Sesi TC Client E] Tunggu aksi selesai (permintaan mendapat respons)
6. [Sesi Import data (Read Only) Client E] Muat ulang halaman Import > Brand
7. [Sesi Import data (Read Only) Client E] Hover `[Discard]` pada Unsaved Banner
8. [Sesi Import data (Read Only) Client E] Verifikasi tooltip yang tampil "You don't have permission to do this."
9. [Sesi Import data (Read Only) Client E] Verifikasi tooltip "Can't discard while an import is in progress." tidak tampil
10. Lanjutkan worker commit; reset Client E sesuai D-47 dan buat ulang draft D-34

### TC-GS-IMPORT-692: Select All tidak menyertakan baris di dalam batch aktif

11. Muat ulang halaman Import > Brand
12. Jeda worker commit (kontrol worker D-47)
13. Klik `[Import (250)]`
14. Tunggu aksi selesai (permintaan mendapat respons)
15. Muat ulang halaman Import > Brand
16. Hover checkbox baris #1
17. Verifikasi checkbox baris #1 tampil Disabled
18. Verifikasi hover menampilkan tooltip "Can't do this while an import is in progress."
19. Set Rows per page menjadi 100
20. Klik tombol halaman 2 pada paginator
21. Centang baris #101
22. Verifikasi tombol `[Select All (150 records)]` tampil
23. Klik tombol Select All
24. Verifikasi Bulk Action Bar menampilkan "150 Rows selected"
25. Klik tombol halaman 1 pada paginator
26. Verifikasi checkbox baris #1 tidak tercentang
27. Lanjutkan worker commit; reset Client E sesuai D-47

### TC-GS-IMPORT-869 (baris L1078): Memulai sesi edit saat job committing ditolak

28. Reset Client E (D-47) ke tanpa draft dan siapkan draft Brand 12 baris dari brand-12.csv (D-50) lewat fixture, lalu muat ulang halaman Import > Brand
29. Tahan commit pada status `committing` (kontrol worker D-47 mode 1)
30. Mulai commit draft Brand Client E atas nama Admin kedua Client E lewat permintaan Import fixture (sesi API; setara klik `[Import (12)]`)
31. Tunggu aksi selesai (permintaan mendapat respons)
32. Pada halaman langkah 28 (tanpa muat ulang) klik `⋯` pada baris #1
33. Pilih Edit
34. Verifikasi dialog Title "Import In Progress" dengan Body "An import is currently running for this draft. Please try again after it finishes." dan tombol `[OK]` saja (tanpa `[Take Over Session]`)
35. Klik `[OK]` pada dialog
36. Verifikasi baris #1 tidak menjadi input
37. Lanjutkan worker commit; reset Client E sesuai D-47 (hapus Brand hasil commit dan draft)

## Notes

- Spec melewati sekitar 35 langkah (37 langkah). Seluruhnya satu topik dengan akun dan client yang sama; memecahnya hanya menambah login, hook, dan pembersihan tanpa menambah daya deteksi.
- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: harness eksternal (kelas d, prinsip 13d; objek uji kontrol worker commit D-47 mode jeda).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (reset dan seed fixture), langkah 2 (muat ulang sesudah seed), langkah 3, 4, 12, 13, 29, 30 (menahan job pada status `committing`), langkah 6, 11, 15 (muat ulang; langkah 11 memuat ulang halaman Import > Brand setelah reset fixture langkah 10 sebelum klik `[Import (250)]`), langkah 10, 27, 37 (pemulihan), langkah 19 sampai 21, 23, 25 (aksi menuju keadaan yang diasersi), langkah 28 (reset dan penyiapan draft), langkah 5, 14, dan 31 (menunggu permintaan commit mendapat respons sebelum sesi atau halaman lain bertindak; langkah 14 mencegah muat ulang langkah 15 berlomba dengan permintaan `[Import (250)]` langkah 13). Langkah 30 adalah pemicu sesi API Admin kedua Client E tanpa pembukaan halaman; langkah TC "Admin kedua Client E: klik `[Import (12)]`" digantikan pemicu itu karena hasil di sesi tersebut tidak diasersi.
- Konteks kedua beraksi: belum ada id pengecualian untuk Sesi Import data (Read Only) Client E yang memuat ulang halaman dan melakukan hover lalu diasersi (TC-GS-IMPORT-208) di spec kelas d; `P-6` hanya untuk pengamat read-only tanpa interaksi dan `P-2` hanya untuk konteks yang bukan objek asersi. Spec tidak dipecah (satu kelas harness, blok berdiri sendiri); usulan aturan baru menunggu batch konvensi.
- Langkah 9 (absence tooltip) memakai tooltip izin langkah 8 sebagai anchor positif pada elemen yang sama.
- Pembagian TC lintas spec: nomor TC-GS-IMPORT-869 dipakai dua baris; spec ini memuat baris L1078 (Import In Progress) dan baris L937 (duplicate Email vs email baru menunggu konfirmasi) berada di spec lain.
- Temuan untuk QA:
  - TC-GS-IMPORT-208: langkah 6 dan Expected tunggal tanpa huruf; Pre-setup memakai dua akun (Import data Read Only dan Total Control Client E) dan butuh D-47 dan D-76; tidak ada langkah yang memastikan akun Read Only tidak punya capability Create selama commit berjalan.
  - ID ganda TC-GS-IMPORT-868 (L738 dan L1077), 869 (L937 dan L1078), 870 (L1020 dan L1079), 871 (L938 dan L1080) dengan isi berbeda; `sourceTc` dan `check-suite.py` tidak dapat membedakannya. Usulan: QA memberi nomor baru pada empat baris di L1077-L1080.
  - Penanda selesai untuk langkah 5 (klik `[Import (250)]`), langkah 14 (klik `[Import (250)]` pada TC-GS-IMPORT-692), dan langkah 31 (permintaan Import fixture) tidak disebut di TC, PRD, atau spec ini; langkah "Tunggu aksi selesai" memakai "permintaan mendapat respons" sampai QA menetapkan penanda yang teramati di surface aktor pertama.
