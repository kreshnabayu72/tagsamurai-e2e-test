---
id: TC-FA-TAG-E2E-311-matriks-dampak-transaksi-disposal-bagian-1
title: "Matriks Dampak Transaksi Disposal: Request Kondisi T2 sampai T4 menurut Disposal Type"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1188
  - TC-FA-TAG-1189
  - TC-FA-TAG-1190
  - TC-FA-TAG-1191
  - TC-FA-TAG-1192
coverage:
  web: automated
---

# Matriks Dampak Transaksi Disposal: Request Kondisi T2 sampai T4 menurut Disposal Type

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Asset Admin (berhak menjalankan langkah ini di modul Disposal), `assetAdminBerhakMenjalankanLangkahIniDiModulDisposal_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_DSP_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Nama env password didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun aktor, lihat `suite.md`; spec ini tidak mengubahnya.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (kunci fixture ditandai untuk tim FE); data aset dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) yang dapat diatur membaca atau tidak membaca Tag aset tertentu; seed dan pemulihan aset, Tag Paired, laporan Tag, transaksi dan sesi opname lewat fixture backend; berkas gambar uji untuk bidang "Foto aset" (`Fixture.fixed-asset-tag.fotoAset`); pembacaan state backend (laporan Tag, status aset, flag Manual identification pada transaksi) dipakai hanya untuk butir Expected TC. Tidak ada endpoint yang dikarang di spec ini.
- Kondisi Tag: T1 = satu Tag RFID Paired yang dapat dipindai tanpa laporan terbuka; T2 = satu Tag RFID Paired yang dapat dipindai dengan laporan Damaged terbuka; T3 = satu Tag RFID Paired yang tidak dapat dipindai reader saat itu dan tanpa laporan terbuka; T4 = Asset Name ber-TAG Type RFID tanpa Tag Paired sama sekali (Without active tag). Simulator reader diatur membaca Tag aset T1 dan T2 serta tidak membaca Tag aset T3.
- Semua aset uji berada di Group Plant B (TC tidak menyebut Group aset T1 sampai T4).
- Transaction Policy Disposal memakai nilai bawaan (Allow manual identification to start OFF) dan tidak diubah.

- Data aset uji (dibuat spec ini di hook `before`, nama bersuffix `{runId}-311`; dihapus atau dikembalikan di hook `after`):

  | Kunci fixture | Nama aset | Kondisi Tag | Status aset | TC |
  |---|---|---|---|---|
  | `asetRqT2` | Aset Matriks Request T2 {runId}-311 | T2 | Available | 1188 |
  | `asetRqT3Lost` | Aset Matriks Request T3 Lost {runId}-311 | T3 | Missing (record Missing berstatus Missing) | 1189 |
  | `asetRqT3Sell` | Aset Matriks Request T3 Sell {runId}-311 | T3 | Available, Condition Normal | 1190 |
  | `asetRqT4WriteOff` | Aset Matriks Request T4 Write-off {runId}-311 | T4 | Missing (record Missing berstatus Missing) | 1191 |
  | `asetRqT4Scrap` | Aset Matriks Request T4 Scrap {runId}-311 | T4 | Available, Condition Normal | 1192 |

- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus aset uji, Tag, laporan Tag, dan transaksi buatan spec; kembalikan status reader simulator.
- State global: tidak ada yang diubah selain data milik spec; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1188: Request pada kondisi T2

1. Buka layar transaksi Disposal untuk aset `Aset Matriks Request T2 {runId}-311`
2. Jalankan langkah "Request"
3. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil
4. Lanjutkan langkah "Request" sampai selesai
5. Verifikasi langkah "Request" pada Disposal berjalan normal sampai selesai

### TC-FA-TAG-1189: Request kondisi T3 pada aset Missing (Lost) diizinkan tanpa identifikasi manual

6. Buka form Disposal Request dari tab Missing lewat Report Disposal untuk aset `Aset Matriks Request T3 Lost {runId}-311`
7. Pilih Disposal type Lost
8. Jalankan langkah "Request"
9. Verifikasi langkah "Request" pada Disposal berjalan normal tanpa pesan blok S-26
10. Verifikasi tombol `[I Can't Scan the TAG]` tidak diwajibkan
11. Verifikasi tidak ada Report TAG yang dibuat (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1190: Request kondisi T3 pada aset Normal (Sell) diizinkan tanpa identifikasi manual

12. Buka form Disposal Request untuk aset `Aset Matriks Request T3 Sell {runId}-311`
13. Pilih Disposal type Sell
14. Jalankan langkah "Request"
15. Verifikasi langkah "Request" pada Disposal berjalan normal tanpa pesan blok S-26
16. Verifikasi tidak ada kewajiban identifikasi manual pada langkah Request
17. Verifikasi transaksi tidak memiliki flag Manual identification (dibaca lewat kemampuan baca state backend)
18. Verifikasi transaksi tidak memiliki foto transaksi (dibaca lewat kemampuan baca state backend)
19. Verifikasi tidak ada Report TAG "Unreadable" yang dibuat (dibaca lewat kemampuan baca state backend)
20. Verifikasi aset tidak mendapat status "Tag Reported" (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1191: Request kondisi T4 pada aset Missing (Write-off) diizinkan tanpa identifikasi manual

21. Buka form Disposal Request dari tab Missing lewat Report Disposal untuk aset `Aset Matriks Request T4 Write-off {runId}-311`
22. Pilih Disposal type Write-off
23. Jalankan langkah "Request"
24. Verifikasi langkah "Request" pada Disposal berjalan normal tanpa pesan blok S-26
25. Verifikasi tombol `[I Can't Scan the TAG]` tidak diwajibkan
26. Verifikasi transaksi tidak memiliki flag Manual identification (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1192: Request kondisi T4 pada aset Normal (Scrap) diizinkan tanpa identifikasi manual

27. Buka form Disposal Request untuk aset `Aset Matriks Request T4 Scrap {runId}-311`
28. Pilih Disposal type Scrap
29. Jalankan langkah "Request"
30. Verifikasi langkah "Request" pada Disposal berjalan normal tanpa pesan blok S-26
31. Verifikasi tidak ada kewajiban identifikasi manual pada langkah Request
32. Verifikasi transaksi tidak memiliki flag Manual identification (dibaca lewat kemampuan baca state backend)
33. Verifikasi transaksi tidak memiliki foto transaksi (dibaca lewat kemampuan baca state backend)
34. Verifikasi tidak ada Report TAG yang dibuat (dibaca lewat kemampuan baca state backend)

## Notes

- Mode: FE+BE.
- TC-FA-TAG-1187 (Request pada kondisi T1) ada di spec 321. TC-FA-TAG-1193 sampai 1196 ada di spec 312.
- Temuan untuk QA:
  - Langkah "Jalankan langkah ..." di TC tidak menjabarkan layar, field, dan urutan klik transaksi; spec menulisnya sebagai satu langkah dan penjabarannya diserahkan ke tahap script.
  - TC tidak menyebut Group aset kondisi T1 dan T2; spec memakai Group Plant B seperti aset kondisi T3 dan T4.
  - TC tidak menyebut tempat teramatinya Report TAG, status "Tag Reported", dan flag Manual identification (kolom Expected tidak menunjuk layar); spec membacanya lewat kemampuan baca state backend (disediakan tim FE/BE) tanpa mengarang endpoint.
  - Kolom Post Condition semua TC di spec ini bernilai `-`; tidak ada Post Condition yang perlu diasersi.
  - TC-FA-TAG-1188 (Request pada kondisi T2) menuliskan Expected "peringatan ... tidak tampil" tanpa alasan; spec mengikuti Expected TC apa adanya.
  - TC-FA-TAG-1189 dan 1191 Expected c menegaskan ulang butir a (Disposal Request diizinkan pada kondisi T3 atau T4); spec tidak menulis `Verifikasi` terpisah untuk butir itu karena sudah dicakup langkah "berjalan normal tanpa pesan blok S-26" (S-01).
  - TC-FA-TAG-1189, 1190, 1191, dan 1192 tidak menyebut Group aset dan cara membuka tab Missing lewat Report Disposal secara rinci; spec memakai Group Plant B dan menuliskan alur apa adanya dari TC.
