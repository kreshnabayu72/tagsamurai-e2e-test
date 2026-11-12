---
id: TC-FA-TAG-E2E-313-matriks-dampak-transaksi-stock-opname-dan-maintenance-bagian-1
title: "Matriks Dampak Transaksi Stock Opname: Scan Aset Kondisi T2 sampai T4"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1198
  - TC-FA-TAG-1199
  - TC-FA-TAG-1200
coverage:
  web: automated
---

# Matriks Dampak Transaksi Stock Opname: Scan Aset Kondisi T2 sampai T4

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Asset Admin (berhak menjalankan langkah ini di modul Stock opname), `assetAdminBerhakMenjalankanLangkahIniDiModulStockOpname_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_OPN_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Nama env password didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun aktor, lihat `suite.md`; spec ini tidak mengubahnya.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (kunci fixture ditandai untuk tim FE); data aset dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) yang dapat diatur membaca atau tidak membaca Tag aset tertentu; seed dan pemulihan aset, Tag Paired, laporan Tag, transaksi dan sesi opname lewat fixture backend; berkas gambar uji untuk bidang "Foto aset" (`Fixture.fixed-asset-tag.fotoAset`); pembacaan state backend (laporan Tag, status aset, flag Manual identification pada transaksi) dipakai hanya untuk butir Expected TC. Tidak ada endpoint yang dikarang di spec ini.
- Kondisi Tag: T2 = satu Tag RFID Paired yang dapat dipindai dengan laporan Damaged terbuka; T3 = satu Tag RFID Paired yang tidak dapat dipindai reader saat itu dan tanpa laporan terbuka; T4 = Asset Name ber-TAG Type RFID tanpa Tag Paired sama sekali (Without active tag). Simulator reader diatur membaca Tag aset T2 serta tidak membaca Tag aset T3.
- Semua aset uji berada di Group Plant B (TC menyebut Plant B pada aset T3 dan T4; Group aset T2 tidak disebut TC).
- Sesi opname berjalan yang memuat aset uji disiapkan lewat fixture backend.

- Data aset uji (dibuat spec ini di hook `before`, nama bersuffix `{runId}-313`; dihapus atau dikembalikan di hook `after`):

  | Kunci fixture | Nama aset | Kondisi Tag | Status aset | TC |
  |---|---|---|---|---|
  | `asetOpnT2` | Aset Matriks Opname T2 {runId}-313 | T2 | Termuat di sesi opname berjalan | 1198 |
  | `asetOpnT3` | Aset Matriks Opname T3 {runId}-313 | T3 | Termuat di sesi opname berjalan | 1199 |
  | `asetOpnT4` | Aset Matriks Opname T4 {runId}-313 | T4 | Termuat di sesi opname berjalan | 1200 |

- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus aset uji, Tag, laporan Tag, dan transaksi buatan spec; kembalikan status reader simulator. Sesi opname buatan spec ditutup atau dihapus.
- State global: tidak ada yang diubah selain data milik spec; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1198: Scan aset (found) pada kondisi T2

1. Buka layar transaksi Stock opname untuk aset `Aset Matriks Opname T2 {runId}-313`
2. Jalankan langkah "Scan aset (found)"
3. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil
4. Lanjutkan langkah "Scan aset (found)" sampai selesai
5. Verifikasi langkah "Scan aset (found)" pada Stock opname berjalan normal sampai selesai

### TC-FA-TAG-1199: Scan aset (found) pada kondisi T3

6. Buka layar transaksi Stock opname untuk aset `Aset Matriks Opname T3 {runId}-313`
7. Jalankan langkah "Scan aset (found)"
8. Verifikasi tombol `[I can't scan the TAG]` tersedia
9. Klik `[I can't scan the TAG]` untuk melanjutkan lewat identifikasi manual
10. Verifikasi bidang "Foto aset" bertanda wajib (*)
11. Unggah Foto aset dan selesaikan transaksi
12. Verifikasi transaksi dicatat dengan flag Manual identification beserta foto (dibaca lewat kemampuan baca state backend)
13. Verifikasi Report TAG "Unreadable" dibuat untuk Tag yang dipilih (Tag belum punya laporan terbuka) (dibaca lewat kemampuan baca state backend)
14. Verifikasi aset mendapat tambahan status "Tag Reported" (dibaca lewat kemampuan baca state backend)
15. Verifikasi aset tercatat sebagai "Found (manual)" (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1200: Scan aset (found) pada kondisi T4

16. Buka layar transaksi Stock opname untuk aset `Aset Matriks Opname T4 {runId}-313`
17. Jalankan langkah "Scan aset (found)"
18. Verifikasi tombol `[I can't scan the TAG]` tersedia
19. Klik `[I can't scan the TAG]` untuk melanjutkan lewat identifikasi manual
20. Verifikasi bidang "Foto aset" bertanda wajib (*)
21. Verifikasi tidak ada Tag untuk dipilih
22. Unggah Foto aset dan selesaikan transaksi
23. Verifikasi transaksi dicatat dengan flag Manual identification beserta foto (dibaca lewat kemampuan baca state backend)
24. Verifikasi tidak ada Report TAG yang dibuat; hanya flag Manual identification yang dicatat (dibaca lewat kemampuan baca state backend)
25. Verifikasi aset tercatat sebagai "Found (manual)" (dibaca lewat kemampuan baca state backend)

## Notes

- Mode: FE+BE.
- TC-FA-TAG-1197 (Scan aset pada kondisi T1) ada di spec 321. TC-FA-TAG-1201 sampai 1204 ada di spec 314.
- Temuan untuk QA:
  - Langkah "Jalankan langkah ..." di TC tidak menjabarkan layar, field, dan urutan klik transaksi; spec menulisnya sebagai satu langkah dan penjabarannya diserahkan ke tahap script.
  - TC tidak menyebut Group aset kondisi T2; spec memakai Group Plant B seperti aset kondisi T3 dan T4.
  - TC tidak menyebut tempat teramatinya Report TAG, status "Tag Reported", dan flag Manual identification (kolom Expected tidak menunjuk layar); spec membacanya lewat kemampuan baca state backend (disediakan tim FE/BE) tanpa mengarang endpoint.
  - Kolom Post Condition semua TC di spec ini bernilai `-`; tidak ada Post Condition yang perlu diasersi.
  - TC-FA-TAG-1198 (kondisi T2) menuliskan Expected "peringatan ... tidak tampil" tanpa alasan; spec mengikuti Expected TC apa adanya.
