---
id: TC-FA-TAG-E2E-306-matriks-dampak-transaksi-assignment-bagian-2
title: "Matriks Dampak Transaksi Assignment: Return Kondisi T4 dan Offboarding Return Kondisi T1 sampai T4"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1162
  - TC-FA-TAG-1163
  - TC-FA-TAG-1164
  - TC-FA-TAG-1165
  - TC-FA-TAG-1166
coverage:
  web: automated
---

# Matriks Dampak Transaksi Assignment: Return Kondisi T4 dan Offboarding Return Kondisi T1 sampai T4

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Asset Admin (berhak menjalankan langkah ini di modul Assignment), `assetAdminBerhakMenjalankanLangkahIniDiModulAssignment_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_ASG_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Nama env password didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun aktor, lihat `suite.md`; spec ini tidak mengubahnya.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (kunci fixture ditandai untuk tim FE); data aset dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) yang dapat diatur membaca atau tidak membaca Tag aset tertentu; seed dan pemulihan aset, Tag Paired, laporan Tag, transaksi dan sesi opname lewat fixture backend; berkas gambar uji untuk bidang "Foto aset" (`Fixture.fixed-asset-tag.fotoAset`); pembacaan state backend (laporan Tag, status aset, flag Manual identification pada transaksi) dipakai hanya untuk butir Expected TC. Tidak ada endpoint yang dikarang di spec ini.
- Kondisi Tag: T1 = satu Tag RFID Paired yang dapat dipindai tanpa laporan terbuka; T2 = satu Tag RFID Paired yang dapat dipindai dengan laporan Damaged terbuka; T3 = satu Tag RFID Paired yang tidak dapat dipindai reader saat itu dan tanpa laporan terbuka; T4 = Asset Name ber-TAG Type RFID tanpa Tag Paired sama sekali (Without active tag). Simulator reader diatur membaca Tag aset T1 dan T2 serta tidak membaca Tag aset T3.
- Semua aset uji berada di Group Plant B (TC menyebut Plant B pada aset T3 dan T4; Group aset T1 dan T2 tidak disebut TC).
- Pemegang aset `Rina T.` dan karyawan yang di-offboard disediakan tim FE (tidak ada di Tabel Data Uji Pre-setup TC).

- Data aset uji (dibuat spec ini di hook `before`, nama bersuffix `{runId}-306`; dihapus atau dikembalikan di hook `after`):

  | Kunci fixture | Nama aset | Kondisi Tag | Status aset | TC |
  |---|---|---|---|---|
  | `asetRetT4` | Aset Matriks Return T4 {runId}-306 | T4 | Assigned kepada Rina T. | 1162 |
  | `asetOffT1` | Aset Matriks Offboarding T1 {runId}-306 | T1 | Assigned kepada karyawan yang di-offboard | 1163 |
  | `asetOffT2` | Aset Matriks Offboarding T2 {runId}-306 | T2 | Assigned kepada karyawan yang di-offboard | 1164 |
  | `asetOffT3` | Aset Matriks Offboarding T3 {runId}-306 | T3 | Assigned kepada karyawan yang di-offboard | 1165 |
  | `asetOffT4` | Aset Matriks Offboarding T4 {runId}-306 | T4 | Assigned kepada karyawan yang di-offboard | 1166 |

- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus aset uji, Tag, laporan Tag, dan transaksi buatan spec; kembalikan status reader simulator.
- State global: tidak ada yang diubah selain data milik spec; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1162: Return / unassign pada kondisi T4

1. Buka layar transaksi Assignment untuk aset `Aset Matriks Return T4 {runId}-306`
2. Jalankan langkah "Return / unassign"
3. Verifikasi tombol `[I can't scan the TAG]` tersedia
4. Klik `[I can't scan the TAG]` untuk melanjutkan lewat identifikasi manual
5. Verifikasi bidang "Foto aset" bertanda wajib (*)
6. Verifikasi tidak ada Tag untuk dipilih
7. Unggah Foto aset dan selesaikan transaksi
8. Verifikasi transaksi dicatat dengan flag Manual identification beserta foto (dibaca lewat kemampuan baca state backend)
9. Verifikasi tidak ada Report TAG yang dibuat; hanya flag Manual identification yang dicatat (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1163: Offboarding return (karyawan keluar) pada kondisi T1

10. Buka layar transaksi Assignment untuk aset `Aset Matriks Offboarding T1 {runId}-306`
11. Jalankan langkah "Offboarding return (karyawan keluar)" sampai selesai
12. Verifikasi langkah "Offboarding return (karyawan keluar)" pada Assignment berjalan normal sampai selesai
13. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil

### TC-FA-TAG-1164: Offboarding return (karyawan keluar) pada kondisi T2

14. Buka layar transaksi Assignment untuk aset `Aset Matriks Offboarding T2 {runId}-306`
15. Jalankan langkah "Offboarding return (karyawan keluar)" sampai selesai
16. Verifikasi langkah "Offboarding return (karyawan keluar)" pada Assignment berjalan normal sampai selesai
17. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil

### TC-FA-TAG-1165: Offboarding return (karyawan keluar) pada kondisi T3

18. Buka layar transaksi Assignment untuk aset `Aset Matriks Offboarding T3 {runId}-306`
19. Jalankan langkah "Offboarding return (karyawan keluar)"
20. Verifikasi tombol `[I can't scan the TAG]` tersedia
21. Klik `[I can't scan the TAG]` untuk melanjutkan lewat identifikasi manual
22. Verifikasi bidang "Foto aset" bertanda wajib (*)
23. Unggah Foto aset dan selesaikan transaksi
24. Verifikasi transaksi dicatat dengan flag Manual identification beserta foto (dibaca lewat kemampuan baca state backend)
25. Verifikasi Report TAG "Unreadable" dibuat untuk Tag yang dipilih (Tag belum punya laporan terbuka) (dibaca lewat kemampuan baca state backend)
26. Verifikasi aset mendapat tambahan status "Tag Reported" (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1166: Offboarding return (karyawan keluar) pada kondisi T4

27. Buka layar transaksi Assignment untuk aset `Aset Matriks Offboarding T4 {runId}-306`
28. Jalankan langkah "Offboarding return (karyawan keluar)"
29. Verifikasi tombol `[I can't scan the TAG]` tersedia
30. Klik `[I can't scan the TAG]` untuk melanjutkan lewat identifikasi manual
31. Verifikasi bidang "Foto aset" bertanda wajib (*)
32. Verifikasi tidak ada Tag untuk dipilih
33. Unggah Foto aset dan selesaikan transaksi
34. Verifikasi transaksi dicatat dengan flag Manual identification beserta foto (dibaca lewat kemampuan baca state backend)
35. Verifikasi tidak ada Report TAG yang dibuat; hanya flag Manual identification yang dicatat (dibaca lewat kemampuan baca state backend)

## Notes

- Mode: FE+BE.
- TC-FA-TAG-1155 sampai 1161 ada di spec 305 dan 321. TC-FA-TAG-1482 (Assign pada aset Non-TAG) ada di spec 321.
- Temuan untuk QA:
  - Langkah "Jalankan langkah ..." di TC tidak menjabarkan layar, field, dan urutan klik transaksi; spec menulisnya sebagai satu langkah dan penjabarannya diserahkan ke tahap script.
  - TC tidak menyebut Group aset kondisi T1 dan T2; spec memakai Group Plant B seperti aset kondisi T3 dan T4.
  - TC tidak menyebut tempat teramatinya Report TAG, status "Tag Reported", dan flag Manual identification (kolom Expected tidak menunjuk layar); spec membacanya lewat kemampuan baca state backend (disediakan tim FE/BE) tanpa mengarang endpoint.
  - Kolom Post Condition semua TC di spec ini bernilai `-`; tidak ada Post Condition yang perlu diasersi.
