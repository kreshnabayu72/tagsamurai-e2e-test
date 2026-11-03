---
id: TC-FA-TAG-E2E-313-matriks-dampak-transaksi-stock-opname-dan-maintenance-bagian-1
title: "Matriks Dampak Transaksi Stock Opname dan Maintenance: Scan Aset Kondisi T2 sampai T4 dan Maintenance Kondisi T1 dan T2"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1198
  - TC-FA-TAG-1199
  - TC-FA-TAG-1200
  - TC-FA-TAG-1201
  - TC-FA-TAG-1202
coverage:
  web: automated
---

# Matriks Dampak Transaksi Stock Opname dan Maintenance: Scan Aset Kondisi T2 sampai T4 dan Maintenance Kondisi T1 dan T2

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Asset Admin (berhak menjalankan langkah ini di modul Stock opname), `assetAdminBerhakMenjalankanLangkahIniDiModulStockOpname_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_OPN_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun berikutnya (ganti akun eksplisit, login pada langkah 26): Asset Admin (berhak menjalankan langkah ini di modul Maintenance), `assetAdminBerhakMenjalankanLangkahIniDiModulMaintenance_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_MNT_PASSWORD`.
- Nama env password didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun aktor, lihat `suite.md`; spec ini tidak mengubahnya.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (kunci fixture ditandai untuk tim FE); data aset dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) yang dapat diatur membaca atau tidak membaca Tag aset tertentu; seed dan pemulihan aset, Tag Paired, laporan Tag, transaksi dan sesi opname lewat fixture backend; berkas gambar uji untuk bidang "Foto aset" (`Fixture.fixed-asset-tag.fotoAset`); pembacaan state backend (laporan Tag, status aset, flag Manual identification pada transaksi) dipakai hanya untuk butir Expected TC. Tidak ada endpoint yang dikarang di spec ini.
- Kondisi Tag: T1 = satu Tag RFID Paired yang dapat dipindai tanpa laporan terbuka; T2 = satu Tag RFID Paired yang dapat dipindai dengan laporan Damaged terbuka; T3 = satu Tag RFID Paired yang tidak dapat dipindai reader saat itu dan tanpa laporan terbuka; T4 = Asset Name ber-TAG Type RFID tanpa Tag Paired sama sekali (Without active tag). Simulator reader diatur membaca Tag aset T1 dan T2 serta tidak membaca Tag aset T3.
- Semua aset uji berada di Group Plant B (TC menyebut Plant B pada aset T3 dan T4; Group aset T1 dan T2 tidak disebut TC).
- Sesi opname berjalan yang memuat aset uji dan work order Maintenance berjalan disiapkan lewat fixture backend.

- Data aset uji (dibuat spec ini di hook `before`, nama bersuffix `{runId}-313`; dihapus atau dikembalikan di hook `after`):

  | Kunci fixture | Nama aset | Kondisi Tag | Status aset | TC |
  |---|---|---|---|---|
  | `asetOpnT2` | Aset Matriks Opname T2 {runId}-313 | T2 | Termuat di sesi opname berjalan | 1198 |
  | `asetOpnT3` | Aset Matriks Opname T3 {runId}-313 | T3 | Termuat di sesi opname berjalan | 1199 |
  | `asetOpnT4` | Aset Matriks Opname T4 {runId}-313 | T4 | Termuat di sesi opname berjalan | 1200 |
  | `asetMntT1` | Aset Matriks Maintenance T1 {runId}-313 | T1 | Work order Maintenance berjalan | 1201 |
  | `asetMntT2` | Aset Matriks Maintenance T2 {runId}-313 | T2 | Work order Maintenance berjalan | 1202 |

- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus aset uji, Tag, laporan Tag, dan transaksi buatan spec; kembalikan status reader simulator. Sesi opname dan work order buatan spec ditutup atau dihapus.
- State global: tidak ada yang diubah selain data milik spec; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1198: Scan aset (found) pada kondisi T2

1. Buka layar transaksi Stock opname untuk aset `Aset Matriks Opname T2 {runId}-313`
2. Jalankan langkah "Scan aset (found)" sampai selesai
3. Verifikasi langkah "Scan aset (found)" pada Stock opname berjalan normal sampai selesai
4. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil

### TC-FA-TAG-1199: Scan aset (found) pada kondisi T3

5. Buka layar transaksi Stock opname untuk aset `Aset Matriks Opname T3 {runId}-313`
6. Jalankan langkah "Scan aset (found)"
7. Verifikasi tombol `[I can't scan the TAG]` tersedia
8. Klik `[I can't scan the TAG]` untuk melanjutkan lewat identifikasi manual
9. Verifikasi bidang "Foto aset" bertanda wajib (*)
10. Unggah Foto aset dan selesaikan transaksi
11. Verifikasi transaksi dicatat dengan flag Manual identification beserta foto (dibaca lewat kemampuan baca state backend)
12. Verifikasi Report TAG "Unreadable" dibuat untuk Tag yang dipilih (Tag belum punya laporan terbuka) (dibaca lewat kemampuan baca state backend)
13. Verifikasi aset mendapat tambahan status "Tag Reported" (dibaca lewat kemampuan baca state backend)
14. Verifikasi aset tercatat sebagai "Found (manual)" (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1200: Scan aset (found) pada kondisi T4

15. Buka layar transaksi Stock opname untuk aset `Aset Matriks Opname T4 {runId}-313`
16. Jalankan langkah "Scan aset (found)"
17. Verifikasi tombol `[I can't scan the TAG]` tersedia
18. Klik `[I can't scan the TAG]` untuk melanjutkan lewat identifikasi manual
19. Verifikasi bidang "Foto aset" bertanda wajib (*)
20. Verifikasi tidak ada Tag untuk dipilih
21. Unggah Foto aset dan selesaikan transaksi
22. Verifikasi transaksi dicatat dengan flag Manual identification beserta foto (dibaca lewat kemampuan baca state backend)
23. Verifikasi tidak ada Report TAG yang dibuat; hanya flag Manual identification yang dicatat (dibaca lewat kemampuan baca state backend)
24. Verifikasi aset tercatat sebagai "Found (manual)" (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1201: Report damage / Complete work order pada kondisi T1

25. Ganti akun: Logout dari akun yang sedang aktif
26. Login sebagai Asset Admin (berhak menjalankan langkah ini di modul Maintenance) dengan `assetAdminBerhakMenjalankanLangkahIniDiModulMaintenance_automated_{namaCompany}@qwertysystem.net` dan `Spectra.env.FA_TAG_AA_MNT_PASSWORD`
27. Buka layar transaksi Maintenance untuk aset `Aset Matriks Maintenance T1 {runId}-313`
28. Jalankan langkah "Report damage / Complete work order" sampai selesai
29. Verifikasi langkah "Report damage / Complete work order" pada Maintenance berjalan normal sampai selesai
30. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil

### TC-FA-TAG-1202: Report damage / Complete work order pada kondisi T2

31. Buka layar transaksi Maintenance untuk aset `Aset Matriks Maintenance T2 {runId}-313`
32. Jalankan langkah "Report damage / Complete work order" sampai selesai
33. Verifikasi langkah "Report damage / Complete work order" pada Maintenance berjalan normal sampai selesai
34. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil

## Notes

- Mode: FE+BE.
- TC-FA-TAG-1197 (Scan aset pada kondisi T1) ada di spec 321. TC-FA-TAG-1203 dan 1204 ada di spec 314.
- Langkah penghubung (tanpa awalan `Verifikasi`): 25, 26 (penyiapan ulang kondisi aset lewat fixture BE, penutupan popup, pembukaan menu, penggantian akun, dan penantian aksi selesai sesuai isi langkah).
- Ganti akun pada langkah 25 sampai 26 berlaku untuk TC-FA-TAG-1201 dan 1202 yang memakai akun Asset Admin modul Maintenance; akun pertama (modul Stock opname) login di hook `before`.
- Temuan untuk QA:
  - Langkah "Jalankan langkah ..." di TC tidak menjabarkan layar, field, dan urutan klik transaksi; spec menulisnya sebagai satu langkah dan penjabarannya diserahkan ke tahap script.
  - TC tidak menyebut Group aset kondisi T1 dan T2; spec memakai Group Plant B seperti aset kondisi T3 dan T4.
  - TC tidak menyebut tempat teramatinya Report TAG, status "Tag Reported", dan flag Manual identification (kolom Expected tidak menunjuk layar); spec membacanya lewat kemampuan baca state backend (disediakan tim FE/BE) tanpa mengarang endpoint.
  - Kolom Post Condition semua TC di spec ini bernilai `-`; tidak ada Post Condition yang perlu diasersi.
  - TC-FA-TAG-1198 dan 1202 (kondisi T2) menuliskan Expected "peringatan ... tidak tampil" tanpa alasan; spec mengikuti Expected TC apa adanya.
