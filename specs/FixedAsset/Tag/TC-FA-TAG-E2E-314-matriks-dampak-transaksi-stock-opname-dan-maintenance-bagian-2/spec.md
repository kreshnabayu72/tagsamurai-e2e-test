---
id: TC-FA-TAG-E2E-314-matriks-dampak-transaksi-stock-opname-dan-maintenance-bagian-2
title: "Matriks Dampak Transaksi Maintenance: Report Damage atau Complete Work Order Kondisi T1 sampai T4"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1201
  - TC-FA-TAG-1202
  - TC-FA-TAG-1203
  - TC-FA-TAG-1204
coverage:
  web: automated
---

# Matriks Dampak Transaksi Maintenance: Report Damage atau Complete Work Order Kondisi T1 sampai T4

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Asset Admin (berhak menjalankan langkah ini di modul Maintenance), `assetAdminBerhakMenjalankanLangkahIniDiModulMaintenance_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_MNT_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Nama env password didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun aktor, lihat `suite.md`; spec ini tidak mengubahnya.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (kunci fixture ditandai untuk tim FE); data aset dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) yang dapat diatur membaca atau tidak membaca Tag aset tertentu; seed dan pemulihan aset, Tag Paired, laporan Tag, transaksi dan sesi opname lewat fixture backend; berkas gambar uji untuk bidang "Foto aset" (`Fixture.fixed-asset-tag.fotoAset`); pembacaan state backend (laporan Tag, status aset, flag Manual identification pada transaksi) dipakai hanya untuk butir Expected TC. Tidak ada endpoint yang dikarang di spec ini.
- Kondisi Tag: T1 = satu Tag RFID Paired yang dapat dipindai tanpa laporan terbuka; T2 = satu Tag RFID Paired yang dapat dipindai dengan laporan Damaged terbuka; T3 = satu Tag RFID Paired yang tidak dapat dipindai reader saat itu dan tanpa laporan terbuka; T4 = Asset Name ber-TAG Type RFID tanpa Tag Paired sama sekali (Without active tag). Simulator reader diatur membaca Tag aset T1 dan T2 serta tidak membaca Tag aset T3.
- Semua aset uji berada di Group Plant B (TC menyebut Plant B pada aset T3 dan T4; Group aset T1 dan T2 tidak disebut TC).
- Work order Maintenance berjalan pada aset uji disiapkan lewat fixture backend.

- Data aset uji (dibuat spec ini di hook `before`, nama bersuffix `{runId}-314`; dihapus atau dikembalikan di hook `after`):

  | Kunci fixture | Nama aset | Kondisi Tag | Status aset | TC |
  |---|---|---|---|---|
  | `asetMntT1` | Aset Matriks Maintenance T1 {runId}-314 | T1 | Work order Maintenance berjalan | 1201 |
  | `asetMntT2` | Aset Matriks Maintenance T2 {runId}-314 | T2 | Work order Maintenance berjalan | 1202 |
  | `asetMntT3` | Aset Matriks Maintenance T3 {runId}-314 | T3 | Work order Maintenance berjalan | 1203 |
  | `asetMntT4` | Aset Matriks Maintenance T4 {runId}-314 | T4 | Work order Maintenance berjalan | 1204 |

- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus aset uji, Tag, laporan Tag, dan transaksi buatan spec; kembalikan status reader simulator. Work order buatan spec ditutup atau dihapus.
- State global: tidak ada yang diubah selain data milik spec; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1201: Report damage / Complete work order pada kondisi T1

1. Buka layar transaksi Maintenance untuk aset `Aset Matriks Maintenance T1 {runId}-314`
2. Jalankan langkah "Report damage / Complete work order"
3. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil
4. Lanjutkan langkah "Report damage / Complete work order" sampai selesai
5. Verifikasi langkah "Report damage / Complete work order" pada Maintenance berjalan normal sampai selesai

### TC-FA-TAG-1202: Report damage / Complete work order pada kondisi T2

6. Buka layar transaksi Maintenance untuk aset `Aset Matriks Maintenance T2 {runId}-314`
7. Jalankan langkah "Report damage / Complete work order"
8. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil
9. Lanjutkan langkah "Report damage / Complete work order" sampai selesai
10. Verifikasi langkah "Report damage / Complete work order" pada Maintenance berjalan normal sampai selesai

### TC-FA-TAG-1203: Report damage / Complete work order pada kondisi T3

11. Buka layar transaksi Maintenance untuk aset `Aset Matriks Maintenance T3 {runId}-314`
12. Jalankan langkah "Report damage / Complete work order"
13. Verifikasi tombol `[I can't scan the TAG]` tersedia
14. Klik `[I can't scan the TAG]` untuk melanjutkan lewat identifikasi manual
15. Verifikasi bidang "Foto aset" bertanda wajib (*)
16. Unggah Foto aset dan selesaikan transaksi
17. Verifikasi transaksi dicatat dengan flag Manual identification beserta foto (dibaca lewat kemampuan baca state backend)
18. Verifikasi Report TAG "Unreadable" dibuat untuk Tag yang dipilih (Tag belum punya laporan terbuka) (dibaca lewat kemampuan baca state backend)
19. Verifikasi aset mendapat tambahan status "Tag Reported" (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1204: Report damage / Complete work order pada kondisi T4

20. Buka layar transaksi Maintenance untuk aset `Aset Matriks Maintenance T4 {runId}-314`
21. Jalankan langkah "Report damage / Complete work order"
22. Verifikasi tombol `[I can't scan the TAG]` tersedia
23. Klik `[I can't scan the TAG]` untuk melanjutkan lewat identifikasi manual
24. Verifikasi bidang "Foto aset" bertanda wajib (*)
25. Verifikasi tidak ada Tag untuk dipilih
26. Unggah Foto aset dan selesaikan transaksi
27. Verifikasi transaksi dicatat dengan flag Manual identification beserta foto (dibaca lewat kemampuan baca state backend)
28. Verifikasi tidak ada Report TAG yang dibuat; hanya flag Manual identification yang dicatat (dibaca lewat kemampuan baca state backend)

## Notes

- Mode: FE+BE.
- TC-FA-TAG-1197 ada di spec 321. TC-FA-TAG-1198 sampai 1200 ada di spec 313.
- Temuan untuk QA:
  - Langkah "Jalankan langkah ..." di TC tidak menjabarkan layar, field, dan urutan klik transaksi; spec menulisnya sebagai satu langkah dan penjabarannya diserahkan ke tahap script.
  - TC tidak menyebut Group aset kondisi T1 dan T2; spec memakai Group Plant B seperti aset kondisi T3 dan T4.
  - TC tidak menyebut tempat teramatinya Report TAG, status "Tag Reported", dan flag Manual identification (kolom Expected tidak menunjuk layar); spec membacanya lewat kemampuan baca state backend (disediakan tim FE/BE) tanpa mengarang endpoint.
  - Kolom Post Condition semua TC di spec ini bernilai `-`; tidak ada Post Condition yang perlu diasersi.
  - TC-FA-TAG-1202 (kondisi T2) menuliskan Expected "peringatan ... tidak tampil" tanpa alasan; spec mengikuti Expected TC apa adanya.
