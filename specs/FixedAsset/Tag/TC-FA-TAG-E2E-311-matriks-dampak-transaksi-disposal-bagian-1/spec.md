---
id: TC-FA-TAG-E2E-311-matriks-dampak-transaksi-disposal-bagian-1
title: "Matriks Dampak Transaksi Disposal: Request Kondisi T2 sampai T4 menurut Metode Disposal"
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

# Matriks Dampak Transaksi Disposal: Request Kondisi T2 sampai T4 menurut Metode Disposal

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Asset Admin (berhak menjalankan langkah ini di modul Disposal), `assetAdminBerhakMenjalankanLangkahIniDiModulDisposal_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_DSP_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Nama env password didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun aktor, lihat `suite.md`; spec ini tidak mengubahnya.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (kunci fixture ditandai untuk tim FE); data aset dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) yang dapat diatur membaca atau tidak membaca Tag aset tertentu; seed dan pemulihan aset, Tag Paired, laporan Tag, transaksi dan sesi opname lewat fixture backend; berkas gambar uji untuk bidang "Foto aset" (`Fixture.fixed-asset-tag.fotoAset`); pembacaan state backend (laporan Tag, status aset, flag Manual identification pada transaksi) dipakai hanya untuk butir Expected TC. Tidak ada endpoint yang dikarang di spec ini.
- Kondisi Tag: T1 = satu Tag RFID Paired yang dapat dipindai tanpa laporan terbuka; T2 = satu Tag RFID Paired yang dapat dipindai dengan laporan Damaged terbuka; T3 = satu Tag RFID Paired yang tidak dapat dipindai reader saat itu dan tanpa laporan terbuka; T4 = Asset Name ber-TAG Type RFID tanpa Tag Paired sama sekali (Without active tag). Simulator reader diatur membaca Tag aset T1 dan T2 serta tidak membaca Tag aset T3.
- Semua aset uji berada di Group Plant B (TC menyebut Plant B pada aset T3 dan T4; Group aset T1 dan T2 tidak disebut TC).
- Transaction Policy Disposal memakai nilai bawaan (Allow manual identification to start OFF) dan tidak diubah.

- Data aset uji (dibuat spec ini di hook `before`, nama bersuffix `{runId}-311`; dihapus atau dikembalikan di hook `after`):

  | Kunci fixture | Nama aset | Kondisi Tag | Status aset | TC |
  |---|---|---|---|---|
  | `asetRqT2` | Aset Matriks Request T2 {runId}-311 | T2 | Available | 1188 |
  | `asetRqT3Clr` | Aset Matriks Request T3 Clearance {runId}-311 | T3 | Permanently Missing | 1189 |
  | `asetRqT3Sale` | Aset Matriks Request T3 Sale {runId}-311 | T3 | Available | 1190 |
  | `asetRqT4Clr` | Aset Matriks Request T4 Clearance {runId}-311 | T4 | Available | 1191 |
  | `asetRqT4Sale` | Aset Matriks Request T4 Sale {runId}-311 | T4 | Available | 1192 |

- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus aset uji, Tag, laporan Tag, dan transaksi buatan spec; kembalikan status reader simulator.
- State global: tidak ada yang diubah selain data milik spec; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1188: Request pada kondisi T2

1. Buka layar transaksi Disposal untuk aset `Aset Matriks Request T2 {runId}-311`
2. Jalankan langkah "Request"
3. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil
4. Lanjutkan langkah "Request" sampai selesai
5. Verifikasi langkah "Request" pada Disposal berjalan normal sampai selesai

### TC-FA-TAG-1189: Request kondisi T3 dengan metode Clearance

6. Buka layar transaksi Disposal untuk aset `Aset Matriks Request T3 Clearance {runId}-311`
7. Jalankan langkah "Request"
8. Pilih metode disposal Clearance
9. Verifikasi langkah "Request" pada Disposal berjalan normal untuk metode Clearance tanpa pesan blok
10. Verifikasi Disposal Request metode Clearance diizinkan pada aset Permanently Missing kondisi T3

### TC-FA-TAG-1190: Request kondisi T3 dengan metode selain Clearance

11. Buka layar transaksi Disposal untuk aset `Aset Matriks Request T3 Sale {runId}-311`
12. Jalankan langkah "Request"
13. Pilih metode disposal Sale (selain Clearance)
14. Verifikasi tombol `[I can't scan the TAG]` tersedia
15. Klik `[I can't scan the TAG]` untuk melanjutkan lewat identifikasi manual
16. Verifikasi bidang "Foto aset" bertanda wajib (*)
17. Unggah Foto aset dan selesaikan transaksi
18. Verifikasi transaksi dicatat dengan flag Manual identification beserta foto (dibaca lewat kemampuan baca state backend)
19. Verifikasi Report TAG "Unreadable" dibuat untuk Tag yang dipilih (Tag belum punya laporan terbuka) (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1191: Request kondisi T4 dengan metode Clearance

20. Buka layar transaksi Disposal untuk aset `Aset Matriks Request T4 Clearance {runId}-311`
21. Jalankan langkah "Request"
22. Pilih metode disposal Clearance
23. Verifikasi langkah "Request" pada Disposal berjalan normal untuk metode Clearance tanpa pesan blok
24. Verifikasi Disposal Request metode Clearance diizinkan pada kondisi T4

### TC-FA-TAG-1192: Request kondisi T4 dengan metode selain Clearance

25. Buka layar transaksi Disposal untuk aset `Aset Matriks Request T4 Sale {runId}-311`
26. Jalankan langkah "Request"
27. Pilih metode disposal Sale (selain Clearance)
28. Verifikasi tombol `[I can't scan the TAG]` tersedia
29. Klik `[I can't scan the TAG]` untuk melanjutkan lewat identifikasi manual
30. Verifikasi bidang "Foto aset" bertanda wajib (*)
31. Verifikasi tidak ada Tag untuk dipilih
32. Unggah Foto aset dan selesaikan transaksi
33. Verifikasi transaksi dicatat dengan flag Manual identification beserta foto (dibaca lewat kemampuan baca state backend)
34. Verifikasi tidak ada Report TAG yang dibuat; hanya flag Manual identification yang dicatat (dibaca lewat kemampuan baca state backend)

## Notes

- Mode: FE+BE.
- TC-FA-TAG-1187 (Request pada kondisi T1) ada di spec 321. TC-FA-TAG-1193 sampai 1196 ada di spec 312.
- Temuan untuk QA:
  - Langkah "Jalankan langkah ..." di TC tidak menjabarkan layar, field, dan urutan klik transaksi; spec menulisnya sebagai satu langkah dan penjabarannya diserahkan ke tahap script.
  - TC tidak menyebut Group aset kondisi T1 dan T2; spec memakai Group Plant B seperti aset kondisi T3 dan T4.
  - TC tidak menyebut tempat teramatinya Report TAG, status "Tag Reported", dan flag Manual identification (kolom Expected tidak menunjuk layar); spec membacanya lewat kemampuan baca state backend (disediakan tim FE/BE) tanpa mengarang endpoint.
  - Kolom Post Condition semua TC di spec ini bernilai `-`; tidak ada Post Condition yang perlu diasersi.
  - TC-FA-TAG-1188 (Request pada kondisi T2) menuliskan Expected "peringatan ... tidak tampil" tanpa alasan; spec mengikuti Expected TC apa adanya.
  - TC-FA-TAG-1189 dan 1191 Expected b hanya menegaskan ulang butir a (diizinkan untuk metode Clearance); spec tetap menulis satu `Verifikasi` untuk tiap butir.
