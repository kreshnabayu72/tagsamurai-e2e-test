---
id: TC-FA-TAG-E2E-312-matriks-dampak-transaksi-disposal-bagian-2
title: "Matriks Dampak Transaksi Disposal: Execute Kondisi T1 sampai T4 dan Konfirmasi Saksi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1193
  - TC-FA-TAG-1194
  - TC-FA-TAG-1195
  - TC-FA-TAG-1196
coverage:
  web: automated
---

# Matriks Dampak Transaksi Disposal: Execute Kondisi T1 sampai T4 dan Konfirmasi Saksi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Asset Admin (berhak menjalankan langkah ini di modul Disposal), `assetAdminBerhakMenjalankanLangkahIniDiModulDisposal_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_DSP_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Nama env password didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun aktor, lihat `suite.md`; spec ini tidak mengubahnya.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (kunci fixture ditandai untuk tim FE); data aset dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) yang dapat diatur membaca atau tidak membaca Tag aset tertentu; seed dan pemulihan aset, Tag Paired, laporan Tag, transaksi dan sesi opname lewat fixture backend; berkas gambar uji untuk bidang "Foto aset" (`Fixture.fixed-asset-tag.fotoAset`); pembacaan state backend (laporan Tag, status aset, flag Manual identification pada transaksi) dipakai hanya untuk butir Expected TC. Tidak ada endpoint yang dikarang di spec ini.
- Kondisi Tag: T1 = satu Tag RFID Paired yang dapat dipindai tanpa laporan terbuka; T2 = satu Tag RFID Paired yang dapat dipindai dengan laporan Damaged terbuka; T3 = satu Tag RFID Paired yang tidak dapat dipindai reader saat itu dan tanpa laporan terbuka; T4 = Asset Name ber-TAG Type RFID tanpa Tag Paired sama sekali (Without active tag). Simulator reader diatur membaca Tag aset T1 dan T2 serta tidak membaca Tag aset T3.
- Semua aset uji berada di Group Plant B (TC menyebut Plant B pada aset T3 dan T4; Group aset T1 dan T2 tidak disebut TC).
- Saksi: satu pengguna lain dalam scope aset disediakan tim FE (TC tidak menyebut akunnya). Transaction Policy Disposal memakai nilai bawaan dan tidak diubah.

- Data aset uji (dibuat spec ini di hook `before`, nama bersuffix `{runId}-312`; dihapus atau dikembalikan di hook `after`):

  | Kunci fixture | Nama aset | Kondisi Tag | Status aset | TC |
  |---|---|---|---|---|
  | `asetExeT1` | Aset Matriks Execute T1 {runId}-312 | T1 | In Disposal Process, Disposal Request disetujui | 1193 |
  | `asetExeT2` | Aset Matriks Execute T2 {runId}-312 | T2 | In Disposal Process, Disposal Request disetujui | 1194 |
  | `asetExeT3` | Aset Matriks Execute T3 {runId}-312 | T3 | In Disposal Process, Disposal Request disetujui | 1195 |
  | `asetExeT4` | Aset Matriks Execute T4 {runId}-312 | T4 | In Disposal Process, Disposal Request disetujui | 1196 |

- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus aset uji, Tag, laporan Tag, dan transaksi buatan spec; kembalikan status reader simulator.
- State global: tidak ada yang diubah selain data milik spec; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1193: Execute pada kondisi T1

1. Buka layar transaksi Disposal untuk aset `Aset Matriks Execute T1 {runId}-312`
2. Jalankan langkah "Execute" sampai selesai
3. Verifikasi langkah "Execute" pada Disposal berjalan normal sampai selesai
4. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil

### TC-FA-TAG-1194: Execute pada kondisi T2

5. Buka layar transaksi Disposal untuk aset `Aset Matriks Execute T2 {runId}-312`
6. Jalankan langkah "Execute" sampai selesai
7. Verifikasi langkah "Execute" pada Disposal berjalan normal sampai selesai
8. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil

### TC-FA-TAG-1195: Execute pada kondisi T3

9. Buka layar transaksi Disposal untuk aset `Aset Matriks Execute T3 {runId}-312`
10. Jalankan langkah "Execute"
11. Verifikasi tombol `[I can't scan the TAG]` tersedia
12. Klik `[I can't scan the TAG]` untuk melanjutkan lewat identifikasi manual
13. Verifikasi bidang "Foto aset" bertanda wajib (*)
14. Unggah Foto aset
15. Verifikasi konfirmasi saksi wajib: Execute belum dapat diselesaikan sebelum saksi (pengguna lain dalam scope aset) dipilih
16. Pilih satu pengguna lain dalam scope aset sebagai saksi dan selesaikan langkah Execute
17. Verifikasi transaksi dicatat dengan flag Manual identification beserta foto (dibaca lewat kemampuan baca state backend)
18. Verifikasi Report TAG "Unreadable" dibuat untuk Tag yang dipilih (Tag belum punya laporan terbuka) (dibaca lewat kemampuan baca state backend)
19. Verifikasi aset mendapat tambahan status "Tag Reported" (dibaca lewat kemampuan baca state backend)
20. Verifikasi nama saksi dan waktu konfirmasi dicatat bersama flag Manual identification (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1196: Execute pada kondisi T4

21. Buka layar transaksi Disposal untuk aset `Aset Matriks Execute T4 {runId}-312`
22. Jalankan langkah "Execute"
23. Verifikasi tombol `[I can't scan the TAG]` tersedia
24. Klik `[I can't scan the TAG]` untuk melanjutkan lewat identifikasi manual
25. Verifikasi bidang "Foto aset" bertanda wajib (*)
26. Verifikasi tidak ada Tag untuk dipilih
27. Unggah Foto aset
28. Verifikasi konfirmasi saksi wajib: Execute belum dapat diselesaikan sebelum saksi (pengguna lain dalam scope aset) dipilih
29. Pilih satu pengguna lain dalam scope aset sebagai saksi dan selesaikan langkah Execute
30. Verifikasi transaksi dicatat dengan flag Manual identification beserta foto (dibaca lewat kemampuan baca state backend)
31. Verifikasi tidak ada Report TAG yang dibuat; hanya flag Manual identification yang dicatat (dibaca lewat kemampuan baca state backend)
32. Verifikasi nama saksi dan waktu konfirmasi dicatat bersama flag Manual identification (dibaca lewat kemampuan baca state backend)

## Notes

- Mode: FE+BE.
- TC-FA-TAG-1187 sampai 1192 ada di spec 311 dan 321.
- Expected d TC-FA-TAG-1195 dan 1196 memuat dua klausa yang berkaitan (saksi wajib dan Execute tidak dapat diselesaikan tanpa saksi); keduanya ditulis sebagai satu `Verifikasi` (langkah 15 untuk TC-FA-TAG-1195 dan langkah 28 untuk TC-FA-TAG-1196) karena tidak teramati terpisah, sedangkan nama saksi dan waktu konfirmasi diasersi sendiri sesudah Execute selesai.
- Temuan untuk QA:
  - Langkah "Jalankan langkah ..." di TC tidak menjabarkan layar, field, dan urutan klik transaksi; spec menulisnya sebagai satu langkah dan penjabarannya diserahkan ke tahap script.
  - TC tidak menyebut Group aset kondisi T1 dan T2; spec memakai Group Plant B seperti aset kondisi T3 dan T4.
  - TC tidak menyebut tempat teramatinya Report TAG, status "Tag Reported", dan flag Manual identification (kolom Expected tidak menunjuk layar); spec membacanya lewat kemampuan baca state backend (disediakan tim FE/BE) tanpa mengarang endpoint.
  - Kolom Post Condition semua TC di spec ini bernilai `-`; tidak ada Post Condition yang perlu diasersi.
  - TC-FA-TAG-1195 dan 1196 tidak menyebut akun saksi; spec memakai satu pengguna lain dalam scope aset yang disediakan tim FE.
  - TC-FA-TAG-1194 (Execute pada kondisi T2) menuliskan Expected "peringatan ... tidak tampil" tanpa alasan; spec mengikuti Expected TC apa adanya.
