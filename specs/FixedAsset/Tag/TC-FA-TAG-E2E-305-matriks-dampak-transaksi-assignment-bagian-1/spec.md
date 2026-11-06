---
id: TC-FA-TAG-E2E-305-matriks-dampak-transaksi-assignment-bagian-1
title: "Matriks Dampak Transaksi Assignment: Assign Kondisi T2 sampai T4 dan Return Kondisi T1 sampai T3"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1156
  - TC-FA-TAG-1157
  - TC-FA-TAG-1158
  - TC-FA-TAG-1159
  - TC-FA-TAG-1160
  - TC-FA-TAG-1161
coverage:
  web: automated
---

# Matriks Dampak Transaksi Assignment: Assign Kondisi T2 sampai T4 dan Return Kondisi T1 sampai T3

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Asset Admin (berhak menjalankan langkah ini di modul Assignment), `assetAdminBerhakMenjalankanLangkahIniDiModulAssignment_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_ASG_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Nama env password didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun aktor, lihat `suite.md`; spec ini tidak mengubahnya.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (kunci fixture ditandai untuk tim FE); data aset dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) yang dapat diatur membaca atau tidak membaca Tag aset tertentu; seed dan pemulihan aset, Tag Paired, laporan Tag, transaksi dan sesi opname lewat fixture backend; berkas gambar uji untuk bidang "Foto aset" (`Fixture.fixed-asset-tag.fotoAset`); pembacaan state backend (laporan Tag, status aset, flag Manual identification pada transaksi) dipakai hanya untuk butir Expected TC. Tidak ada endpoint yang dikarang di spec ini.
- Kondisi Tag: T1 = satu Tag RFID Paired yang dapat dipindai tanpa laporan terbuka; T2 = satu Tag RFID Paired yang dapat dipindai dengan laporan Damaged terbuka; T3 = satu Tag RFID Paired yang tidak dapat dipindai reader saat itu dan tanpa laporan terbuka; T4 = Asset Name ber-TAG Type RFID tanpa Tag Paired sama sekali (Without active tag). Simulator reader diatur membaca Tag aset T1 dan T2 serta tidak membaca Tag aset T3.
- Semua aset uji berada di Group Plant B (TC menyebut Plant B pada aset T3 dan T4; Group aset T1 dan T2 tidak disebut TC).
- Pemegang aset `Rina T.` pada aset berstatus Assigned disediakan tim FE (tidak ada di Tabel Data Uji Pre-setup TC).

- Data aset uji (dibuat spec ini di hook `before`, nama bersuffix `{runId}-305`; dihapus atau dikembalikan di hook `after`):

  | Kunci fixture | Nama aset | Kondisi Tag | Status aset | TC |
  |---|---|---|---|---|
  | `asetAsgT2` | Aset Matriks Assign T2 {runId}-305 | T2 | Available | 1156 |
  | `asetAsgT3` | Aset Matriks Assign T3 {runId}-305 | T3 | Available | 1157 |
  | `asetAsgT4` | Aset Matriks Assign T4 {runId}-305 | T4 | Available | 1158 |
  | `asetRetT1` | Aset Matriks Return T1 {runId}-305 | T1 | Assigned kepada Rina T. | 1159 |
  | `asetRetT2` | Aset Matriks Return T2 {runId}-305 | T2 | Assigned kepada Rina T. | 1160 |
  | `asetRetT3` | Aset Matriks Return T3 {runId}-305 | T3 | Assigned kepada Rina T. | 1161 |

- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus aset uji, Tag, laporan Tag, dan transaksi buatan spec; kembalikan status reader simulator.
- State global: tidak ada yang diubah selain data milik spec; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1156: Assign / serah ke pemegang baru pada kondisi T2

1. Buka layar transaksi Assignment untuk aset `Aset Matriks Assign T2 {runId}-305`
2. Jalankan langkah "Assign / serah ke pemegang baru"
3. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tampil
4. Lanjutkan langkah "Assign / serah ke pemegang baru" sampai selesai
5. Verifikasi peringatan tidak memblokir: langkah "Assign / serah ke pemegang baru" dapat dilanjutkan sampai selesai

### TC-FA-TAG-1157: Assign / serah ke pemegang baru pada kondisi T3

6. Buka layar transaksi Assignment untuk aset `Aset Matriks Assign T3 {runId}-305`
7. Jalankan langkah "Assign / serah ke pemegang baru"
8. Verifikasi langkah "Assign / serah ke pemegang baru" diblokir dengan pesan "This asset can't be assigned until its TAG is replaced. Ask a TAG administrator of Plant B."
9. Verifikasi langkah tidak dapat dilanjutkan dan tidak tersedia identifikasi manual untuk memulai (Policy "Allow manual identification to start" bernilai bawaan OFF)
10. Verifikasi tombol `[Report TAG]` tampil karena Tag belum dilaporkan

### TC-FA-TAG-1158: Assign / serah ke pemegang baru pada kondisi T4

11. Buka layar transaksi Assignment untuk aset `Aset Matriks Assign T4 {runId}-305`
12. Jalankan langkah "Assign / serah ke pemegang baru"
13. Verifikasi langkah "Assign / serah ke pemegang baru" diblokir dengan pesan "This asset can't be assigned until its TAG is replaced. Ask a TAG administrator of Plant B."
14. Verifikasi langkah tidak dapat dilanjutkan dan tidak tersedia identifikasi manual untuk memulai (Policy "Allow manual identification to start" bernilai bawaan OFF)
15. Verifikasi tombol `[Report TAG]` dan tombol `[Replace TAG]` tidak tampil karena aset tanpa Tag Paired tidak punya Tag untuk dilaporkan atau diganti (S-26c, S-26d)

### TC-FA-TAG-1159: Return / unassign pada kondisi T1

16. Buka layar transaksi Assignment untuk aset `Aset Matriks Return T1 {runId}-305`
17. Jalankan langkah "Return / unassign"
18. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil
19. Lanjutkan langkah "Return / unassign" sampai selesai
20. Verifikasi langkah "Return / unassign" pada Assignment berjalan normal sampai selesai

### TC-FA-TAG-1160: Return / unassign pada kondisi T2

21. Buka layar transaksi Assignment untuk aset `Aset Matriks Return T2 {runId}-305`
22. Jalankan langkah "Return / unassign"
23. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil
24. Lanjutkan langkah "Return / unassign" sampai selesai
25. Verifikasi langkah "Return / unassign" pada Assignment berjalan normal sampai selesai

### TC-FA-TAG-1161: Return / unassign pada kondisi T3

26. Buka layar transaksi Assignment untuk aset `Aset Matriks Return T3 {runId}-305`
27. Jalankan langkah "Return / unassign"
28. Verifikasi tombol `[I can't scan the TAG]` tersedia
29. Klik `[I can't scan the TAG]` untuk melanjutkan lewat identifikasi manual
30. Verifikasi bidang "Foto aset" bertanda wajib (*)
31. Unggah Foto aset dan selesaikan transaksi
32. Verifikasi transaksi dicatat dengan flag Manual identification beserta foto (dibaca lewat kemampuan baca state backend)
33. Verifikasi Report TAG "Unreadable" dibuat untuk Tag yang dipilih (Tag belum punya laporan terbuka) (dibaca lewat kemampuan baca state backend)
34. Verifikasi aset mendapat tambahan status "Tag Reported" (dibaca lewat kemampuan baca state backend)

## Notes

- Mode: FE+BE.
- TC-FA-TAG-1155 (Assign pada kondisi T1) ada di spec 321. TC-FA-TAG-1162 sampai 1166 ada di spec 306.
- Temuan untuk QA:
  - Langkah "Jalankan langkah ..." di TC tidak menjabarkan layar, field, dan urutan klik transaksi; spec menulisnya sebagai satu langkah dan penjabarannya diserahkan ke tahap script.
  - TC tidak menyebut Group aset kondisi T1 dan T2; spec memakai Group Plant B seperti aset kondisi T3 dan T4.
  - TC tidak menyebut tempat teramatinya Report TAG, status "Tag Reported", dan flag Manual identification (kolom Expected tidak menunjuk layar); spec membacanya lewat kemampuan baca state backend (disediakan tim FE/BE) tanpa mengarang endpoint.
  - Kolom Post Condition semua TC di spec ini bernilai `-`; tidak ada Post Condition yang perlu diasersi.
