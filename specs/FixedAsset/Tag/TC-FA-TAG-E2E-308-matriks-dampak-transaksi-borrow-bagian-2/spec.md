---
id: TC-FA-TAG-E2E-308-matriks-dampak-transaksi-borrow-bagian-2
title: "Matriks Dampak Transaksi Borrow: Extend Kondisi T4 dan Check-in Kondisi T1 sampai T4"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1174
  - TC-FA-TAG-1175
  - TC-FA-TAG-1176
  - TC-FA-TAG-1177
  - TC-FA-TAG-1178
coverage:
  web: automated
---

# Matriks Dampak Transaksi Borrow: Extend Kondisi T4 dan Check-in Kondisi T1 sampai T4

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Asset Admin (berhak menjalankan langkah ini di modul Borrow), `assetAdminBerhakMenjalankanLangkahIniDiModulBorrow_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_BRW_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Nama env password didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun aktor, lihat `suite.md`; spec ini tidak mengubahnya.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (kunci fixture ditandai untuk tim FE); data aset dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) yang dapat diatur membaca atau tidak membaca Tag aset tertentu; seed dan pemulihan aset, Tag Paired, laporan Tag, transaksi dan sesi opname lewat fixture backend; berkas gambar uji untuk bidang "Foto aset" (`Fixture.fixed-asset-tag.fotoAset`); pembacaan state backend (laporan Tag, status aset, flag Manual identification pada transaksi) dipakai hanya untuk butir Expected TC. Tidak ada endpoint yang dikarang di spec ini.
- Kondisi Tag: T1 = satu Tag RFID Paired yang dapat dipindai tanpa laporan terbuka; T2 = satu Tag RFID Paired yang dapat dipindai dengan laporan Damaged terbuka; T3 = satu Tag RFID Paired yang tidak dapat dipindai reader saat itu dan tanpa laporan terbuka; T4 = Asset Name ber-TAG Type RFID tanpa Tag Paired sama sekali (Without active tag). Simulator reader diatur membaca Tag aset T1 dan T2 serta tidak membaca Tag aset T3.
- Semua aset uji berada di Group Plant B (TC menyebut Plant B pada aset T3 dan T4; Group aset T1 dan T2 tidak disebut TC).
- Transaction Policy Borrow memakai nilai bawaan dan tidak diubah.

- Data aset uji (dibuat spec ini di hook `before`, nama bersuffix `{runId}-308`; dihapus atau dikembalikan di hook `after`):

  | Kunci fixture | Nama aset | Kondisi Tag | Status aset | TC |
  |---|---|---|---|---|
  | `asetExT4` | Aset Matriks Extend T4 {runId}-308 | T4 | Borrowed | 1174 |
  | `asetCiT1` | Aset Matriks Check-in T1 {runId}-308 | T1 | Borrowed | 1175 |
  | `asetCiT2` | Aset Matriks Check-in T2 {runId}-308 | T2 | Borrowed | 1176 |
  | `asetCiT3` | Aset Matriks Check-in T3 {runId}-308 | T3 | Borrowed | 1177 |
  | `asetCiT4` | Aset Matriks Check-in T4 {runId}-308 | T4 | Borrowed | 1178 |

- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus aset uji, Tag, laporan Tag, dan transaksi buatan spec; kembalikan status reader simulator.
- State global: tidak ada yang diubah selain data milik spec; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1174: Extend pada kondisi T4

1. Buka layar transaksi Borrow untuk aset `Aset Matriks Extend T4 {runId}-308`
2. Jalankan langkah "Extend" sampai selesai
3. Verifikasi langkah "Extend" pada Borrow berjalan normal sampai selesai
4. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil

### TC-FA-TAG-1175: Check-in pada kondisi T1

5. Buka layar transaksi Borrow untuk aset `Aset Matriks Check-in T1 {runId}-308`
6. Jalankan langkah "Check-in" sampai selesai
7. Verifikasi langkah "Check-in" pada Borrow berjalan normal sampai selesai
8. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil

### TC-FA-TAG-1176: Check-in pada kondisi T2

9. Buka layar transaksi Borrow untuk aset `Aset Matriks Check-in T2 {runId}-308`
10. Jalankan langkah "Check-in" sampai selesai
11. Verifikasi langkah "Check-in" pada Borrow berjalan normal sampai selesai
12. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil

### TC-FA-TAG-1177: Check-in pada kondisi T3

13. Buka layar transaksi Borrow untuk aset `Aset Matriks Check-in T3 {runId}-308`
14. Jalankan langkah "Check-in"
15. Verifikasi tombol `[I can't scan the TAG]` tersedia
16. Klik `[I can't scan the TAG]` untuk melanjutkan lewat identifikasi manual
17. Verifikasi bidang "Foto aset" bertanda wajib (*)
18. Unggah Foto aset dan selesaikan transaksi
19. Verifikasi transaksi dicatat dengan flag Manual identification beserta foto (dibaca lewat kemampuan baca state backend)
20. Verifikasi Report TAG "Unreadable" dibuat untuk Tag yang dipilih (Tag belum punya laporan terbuka) (dibaca lewat kemampuan baca state backend)
21. Verifikasi aset mendapat tambahan status "Tag Reported" (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1178: Check-in pada kondisi T4

22. Buka layar transaksi Borrow untuk aset `Aset Matriks Check-in T4 {runId}-308`
23. Jalankan langkah "Check-in"
24. Verifikasi tombol `[I can't scan the TAG]` tersedia
25. Klik `[I can't scan the TAG]` untuk melanjutkan lewat identifikasi manual
26. Verifikasi bidang "Foto aset" bertanda wajib (*)
27. Verifikasi tidak ada Tag untuk dipilih
28. Unggah Foto aset dan selesaikan transaksi
29. Verifikasi transaksi dicatat dengan flag Manual identification beserta foto (dibaca lewat kemampuan baca state backend)
30. Verifikasi tidak ada Report TAG yang dibuat; hanya flag Manual identification yang dicatat (dibaca lewat kemampuan baca state backend)

## Notes

- Mode: FE+BE.
- TC-FA-TAG-1167 sampai 1173 ada di spec 307.
- Temuan untuk QA:
  - Langkah "Jalankan langkah ..." di TC tidak menjabarkan layar, field, dan urutan klik transaksi; spec menulisnya sebagai satu langkah dan penjabarannya diserahkan ke tahap script.
  - TC tidak menyebut Group aset kondisi T1 dan T2; spec memakai Group Plant B seperti aset kondisi T3 dan T4.
  - TC tidak menyebut tempat teramatinya Report TAG, status "Tag Reported", dan flag Manual identification (kolom Expected tidak menunjuk layar); spec membacanya lewat kemampuan baca state backend (disediakan tim FE/BE) tanpa mengarang endpoint.
  - Kolom Post Condition semua TC di spec ini bernilai `-`; tidak ada Post Condition yang perlu diasersi.
  - TC-FA-TAG-1174 (Extend pada kondisi T4) menuliskan Expected "peringatan ... tidak tampil" tanpa alasan; spec mengikuti Expected TC apa adanya.
