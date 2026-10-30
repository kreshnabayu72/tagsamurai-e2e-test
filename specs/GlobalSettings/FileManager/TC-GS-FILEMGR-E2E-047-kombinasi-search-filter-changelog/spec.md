---
id: TC-GS-FILEMGR-E2E-047-kombinasi-search-filter-changelog
title: "Kombinasi Search dan Filter Modal Changelog: Irisan, Independensi Clear, dan Pemulihan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-164
  - TC-GS-FILEMGR-165
  - TC-GS-FILEMGR-166
  - TC-GS-FILEMGR-167
coverage:
  web: automated
---

# Kombinasi Search dan Filter Modal Changelog: Irisan, Independensi Clear, dan Pemulihan Empty State

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sinta Maharani (Tabel A1 TC) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Tabel A4 (14 entri Changelog File Manager; format tanggal General Settings default `dd/MM/yy HH:mm`). Dataset disiapkan lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme dan endpoint seeding tidak didefinisikan di TC, lihat Temuan untuk QA). Entri literal sesuai Tabel A4 karena asersi Search, Filter, dan Sort bergantung pada nilainya (pengecualian setara S-12: seeding idempotent, suite serial). Spec hanya membaca data; tidak ada aksi tulis dan tidak ada data dinamis.
- Suite serial (`parallel: false`). Changelog adalah audit trail permanen yang tidak dapat di-seed ulang atau dibersihkan dan spec lain menambah entri (S-12), sehingga hitungan entri tidak diasersi sebagai total absolut: hitungan dibatasi dengan Filter Date rentang Date Tabel A4 (`23/08/26` sampai `14/09/26`, inklusif; entri terlama 23/08/26 08:00 dan terbaru 14/09/26 02:00) yang hanya memuat populasi Tabel A4. Pilihan Date ini ikut dipilih pada langkah 5, 10, 16, dan 29 (langkah 21 mempertahankannya).
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan: tidak ada.
- Kemampuan teknis: memilih rentang Date `23/08/26` sampai `14/09/26` pada date range picker Filter Panel Changelog (Date entri Tabel A4 tetap, bukan relatif); membaca indikator sort pada header kolom, isi input Search, dan pilihan terpilih pada Filter Panel.

## Test Steps

1. Klik ikon Changelog di toolbar

### TC-GS-FILEMGR-164: Search lebih dulu lalu Filter menghasilkan irisan

2. Ketik Search `archive`, tekan Enter
3. Verifikasi tabel memuat 9 entri `archive-photo-01.jpg` s.d. `archive-photo-09.jpg`
4. Klik ikon Filter di toolbar modal
5. Pilih Date `23/08/26` sampai `14/09/26` dan `System` pada Modified By, klik `[Apply]`
6. Verifikasi tabel memuat 3 entri: `archive-photo-03.jpg`, `archive-photo-06.jpg`, `archive-photo-09.jpg`
7. Verifikasi kata kunci `archive` tetap terisi di input Search

### TC-GS-FILEMGR-165: Filter lebih dulu lalu Search menghasilkan irisan yang sama

8. Klik `[Clear Field]`, klik `[Apply]`
9. Klik ikon panah (←) di kiri input Search
10. Pilih Date `23/08/26` sampai `14/09/26` dan `System` pada Modified By, klik `[Apply]`
11. Verifikasi tabel memuat 5 entri dalam rentang Date Tabel A4
12. Ketik Search `archive`, tekan Enter
13. Verifikasi tabel memuat 3 entri: `archive-photo-03.jpg`, `archive-photo-06.jpg`, `archive-photo-09.jpg`
14. Verifikasi pilihan `System` pada Modified By tetap terpilih di Filter Panel

### TC-GS-FILEMGR-166: Clear Filter dan Clear Search saling independen dengan Sort aktif

15. Klik header Date sekali
16. Klik `[Clear Field]` pada Filter, pilih Date `23/08/26` sampai `14/09/26`, klik `[Apply]`
17. Verifikasi kata kunci `archive` tetap terisi di input Search
18. Verifikasi sort Date Oldest First tetap aktif
19. Verifikasi tabel memuat 9 entri
20. Verifikasi `archive-photo-09.jpg` berada di baris pertama
21. Pilih `System` pada Modified By (Date tetap terpilih dari langkah 16), klik `[Apply]`
22. Klik ikon (✕) di input Search, tekan Enter
23. Verifikasi pilihan `System` pada Modified By tetap terpilih di Filter Panel
24. Verifikasi sort Date Oldest First tetap aktif
25. Verifikasi tabel memuat 5 entri dalam rentang Date Tabel A4
26. Verifikasi `archive-photo-09.jpg` berada di baris pertama

### TC-GS-FILEMGR-167: Pemulihan dari empty state saat salah satu kontrol dilepas

27. Klik `[Clear Field]`, klik `[Apply]`
28. Klik header Date dua kali (Newest First lalu indikator sort hilang)
29. Pilih Date `23/08/26` sampai `14/09/26` dan `Delete` pada Action, klik `[Apply]`
30. Ketik Search `archive`, tekan Enter
31. Verifikasi tampil `No results found`
32. Klik ikon (✕) di input Search, tekan Enter
33. Verifikasi tabel memuat 2 entri Delete: C04 dan C05

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber dipertahankan (164 sampai 167). TC-GS-FILEMGR-166 memakai state Search `archive` dan Filter `System` yang sama dengan akhir TC-GS-FILEMGR-165, sehingga hanya perlu menambah sort (langkah 15). TC-GS-FILEMGR-167 di akhir karena menghasilkan empty state.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8 dan 9 (membersihkan filter dan Search sisa TC-GS-FILEMGR-164 sebelum TC-GS-FILEMGR-165), langkah 27 dan 28 (membersihkan filter dan sort sisa TC-GS-FILEMGR-166 sebelum TC-GS-FILEMGR-167). Langkah 5, 10, 16, dan 29 menyertakan pilihan Date rentang Tabel A4 sebagai penghubung (tidak ada di TC; dicatat per S-03) supaya hitungan entri hanya dari populasi Tabel A4. Langkah 15 (satu klik header Date menghasilkan Oldest First) menjabarkan "urutkan Date Oldest First".
- Langkah 3 (Search `archive` tanpa Filter) menyebut 9 entri bernama `archive-photo-01.jpg` s.d. `archive-photo-09.jpg`; hitungan itu hanya valid selama tidak ada entri spec lain yang memuat kata `archive` (belum dibatasi Filter Date karena TC-GS-FILEMGR-164 mewajibkan Search lebih dulu).
- Anchor: langkah 3, 11, dan 19 membuktikan tabel termuat dengan entri sebelum asersi jumlah; empty state "No results found" (langkah 31) adalah anchor positif sah untuk absence hasil.
- Filter Panel diasumsikan tetap terbuka setelah `[Apply]` mengikuti langkah TC.
- Temuan untuk QA:
  - TC tidak menyatakan apakah Filter Panel tetap terbuka setelah `[Apply]`; spec mengikuti langkah TC dan memakai `[Clear Field]`/`[Apply]` berurutan. Perlu konfirmasi perilaku panel.
  - TC tidak menyebut indikator tempat "filter tetap aktif" teramati; spec mengasersi pilihan `System` pada Modified By tetap terpilih di Filter Panel (langkah 14 dan 23).
  - Mekanisme dan endpoint seeding Tabel A4 tidak didefinisikan di TC (Q-4).
  - TC sumber (mis. TC-GS-FILEMGR-172 dan TC Changelog sejenis) menyatakan hitungan entri absolut ("14 entri", "5 baris") yang bertentangan dengan S-12 (Changelog tidak dapat di-seed ulang atau dibersihkan). Spec membatasi dengan Filter Date rentang Tabel A4 sebagai langkah penghubung; pemilik TC perlu menulis ulang Data Uji sebagai Filter Date rentang Tabel A4 atau hitungan relatif.
