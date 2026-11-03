---
id: TC-FA-TAG-E2E-307-matriks-dampak-transaksi-borrow-bagian-1
title: "Matriks Dampak Transaksi Borrow: Check-out Kondisi T1 sampai T4 dan Extend Kondisi T1 sampai T3"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1167
  - TC-FA-TAG-1168
  - TC-FA-TAG-1169
  - TC-FA-TAG-1170
  - TC-FA-TAG-1171
  - TC-FA-TAG-1172
  - TC-FA-TAG-1173
coverage:
  web: automated
---

# Matriks Dampak Transaksi Borrow: Check-out Kondisi T1 sampai T4 dan Extend Kondisi T1 sampai T3

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Asset Admin (berhak menjalankan langkah ini di modul Borrow), `assetAdminBerhakMenjalankanLangkahIniDiModulBorrow_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_BRW_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Nama env password didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun aktor, lihat `suite.md`; spec ini tidak mengubahnya.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (kunci fixture ditandai untuk tim FE); data aset dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) yang dapat diatur membaca atau tidak membaca Tag aset tertentu; seed dan pemulihan aset, Tag Paired, laporan Tag, transaksi dan sesi opname lewat fixture backend; berkas gambar uji untuk bidang "Foto aset" (`Fixture.fixed-asset-tag.fotoAset`); pembacaan state backend (laporan Tag, status aset, flag Manual identification pada transaksi) dipakai hanya untuk butir Expected TC. Tidak ada endpoint yang dikarang di spec ini.
- Kondisi Tag: T1 = satu Tag RFID Paired yang dapat dipindai tanpa laporan terbuka; T2 = satu Tag RFID Paired yang dapat dipindai dengan laporan Damaged terbuka; T3 = satu Tag RFID Paired yang tidak dapat dipindai reader saat itu dan tanpa laporan terbuka; T4 = Asset Name ber-TAG Type RFID tanpa Tag Paired sama sekali (Without active tag). Simulator reader diatur membaca Tag aset T1 dan T2 serta tidak membaca Tag aset T3.
- Semua aset uji berada di Group Plant B (TC menyebut Plant B pada aset T3 dan T4; Group aset T1 dan T2 tidak disebut TC).
- Policy Borrow On pada aset yang berstatus Available diatur lewat fixture backend; Transaction Policy Borrow memakai nilai bawaan (Allow manual identification to start OFF) dan tidak diubah.

- Data aset uji (dibuat spec ini di hook `before`, nama bersuffix `{runId}-307`; dihapus atau dikembalikan di hook `after`):

  | Kunci fixture | Nama aset | Kondisi Tag | Status aset | TC |
  |---|---|---|---|---|
  | `asetCoT1` | Aset Matriks Check-out T1 {runId}-307 | T1 | Available, policy Borrow On | 1167 |
  | `asetCoT2` | Aset Matriks Check-out T2 {runId}-307 | T2 | Available, policy Borrow On | 1168 |
  | `asetCoT3` | Aset Matriks Check-out T3 {runId}-307 | T3 | Available, policy Borrow On | 1169 |
  | `asetCoT4` | Aset Matriks Check-out T4 {runId}-307 | T4 | Available, policy Borrow On | 1170 |
  | `asetExT1` | Aset Matriks Extend T1 {runId}-307 | T1 | Borrowed | 1171 |
  | `asetExT2` | Aset Matriks Extend T2 {runId}-307 | T2 | Borrowed | 1172 |
  | `asetExT3` | Aset Matriks Extend T3 {runId}-307 | T3 | Borrowed | 1173 |

- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus aset uji, Tag, laporan Tag, dan transaksi buatan spec; kembalikan status reader simulator.
- State global: tidak ada yang diubah selain data milik spec; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1167: Check-out pada kondisi T1

1. Buka layar transaksi Borrow untuk aset `Aset Matriks Check-out T1 {runId}-307`
2. Jalankan langkah "Check-out" sampai selesai
3. Verifikasi langkah "Check-out" pada Borrow berjalan normal sampai selesai
4. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil

### TC-FA-TAG-1168: Check-out pada kondisi T2

5. Buka layar transaksi Borrow untuk aset `Aset Matriks Check-out T2 {runId}-307`
6. Jalankan langkah "Check-out"
7. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tampil
8. Lanjutkan langkah "Check-out" sampai selesai
9. Verifikasi peringatan tidak memblokir: langkah "Check-out" dapat dilanjutkan sampai selesai

### TC-FA-TAG-1169: Check-out pada kondisi T3

10. Buka layar transaksi Borrow untuk aset `Aset Matriks Check-out T3 {runId}-307`
11. Jalankan langkah "Check-out"
12. Verifikasi langkah "Check-out" diblokir dengan pesan "This asset can't be borrowed until its TAG is replaced. Ask a TAG administrator of Plant B."
13. Verifikasi langkah tidak dapat dilanjutkan dan tidak tersedia identifikasi manual untuk memulai (Policy "Allow manual identification to start" bernilai bawaan OFF)
14. Verifikasi tombol `[Report TAG]` tampil karena Tag belum dilaporkan

### TC-FA-TAG-1170: Check-out pada kondisi T4

15. Buka layar transaksi Borrow untuk aset `Aset Matriks Check-out T4 {runId}-307`
16. Jalankan langkah "Check-out"
17. Verifikasi langkah "Check-out" diblokir dengan pesan "This asset can't be borrowed until its TAG is replaced. Ask a TAG administrator of Plant B."
18. Verifikasi langkah tidak dapat dilanjutkan dan tidak tersedia identifikasi manual untuk memulai (Policy "Allow manual identification to start" bernilai bawaan OFF)
19. Verifikasi tombol `[Report TAG]` dan tombol `[Replace TAG]` tidak tampil karena aset tanpa Tag Paired tidak punya Tag untuk dilaporkan atau diganti (S-26c, S-26d)

### TC-FA-TAG-1171: Extend pada kondisi T1

20. Buka layar transaksi Borrow untuk aset `Aset Matriks Extend T1 {runId}-307`
21. Jalankan langkah "Extend" sampai selesai
22. Verifikasi langkah "Extend" pada Borrow berjalan normal sampai selesai
23. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil

### TC-FA-TAG-1172: Extend pada kondisi T2

24. Buka layar transaksi Borrow untuk aset `Aset Matriks Extend T2 {runId}-307`
25. Jalankan langkah "Extend" sampai selesai
26. Verifikasi langkah "Extend" pada Borrow berjalan normal sampai selesai
27. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil

### TC-FA-TAG-1173: Extend pada kondisi T3

28. Buka layar transaksi Borrow untuk aset `Aset Matriks Extend T3 {runId}-307`
29. Jalankan langkah "Extend" sampai selesai
30. Verifikasi langkah "Extend" pada Borrow berjalan normal sampai selesai
31. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil

## Notes

- Mode: FE+BE.
- TC-FA-TAG-1174 sampai 1178 ada di spec 308.
- Temuan untuk QA:
  - Langkah "Jalankan langkah ..." di TC tidak menjabarkan layar, field, dan urutan klik transaksi; spec menulisnya sebagai satu langkah dan penjabarannya diserahkan ke tahap script.
  - TC tidak menyebut Group aset kondisi T1 dan T2; spec memakai Group Plant B seperti aset kondisi T3 dan T4.
  - Kolom Post Condition semua TC di spec ini bernilai `-`; tidak ada Post Condition yang perlu diasersi.
  - TC-FA-TAG-1172 dan 1173 (Extend pada kondisi T2 dan T3) menuliskan Expected "peringatan ... tidak tampil" tanpa alasan; spec mengikuti Expected TC apa adanya.
