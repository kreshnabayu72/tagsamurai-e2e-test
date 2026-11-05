---
id: TC-FA-TAG-E2E-321-matriks-dampak-transaksi-kondisi-t1-dan-aset-non-tag-lintas-modul
title: "Matriks Dampak Transaksi Kondisi T1 dan Aset Non-TAG: Assign, Load, Request, dan Scan Aset Berjalan Normal"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1155
  - TC-FA-TAG-1482
  - TC-FA-TAG-1179
  - TC-FA-TAG-1187
  - TC-FA-TAG-1197
coverage:
  web: automated
---

# Matriks Dampak Transaksi Kondisi T1 dan Aset Non-TAG: Assign, Load, Request, dan Scan Aset Berjalan Normal

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Asset Admin (berhak menjalankan langkah ini di modul Assignment), `assetAdminBerhakMenjalankanLangkahIniDiModulAssignment_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_ASG_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun berikutnya (ganti akun eksplisit, login pada langkah 12): Asset Admin (berhak menjalankan langkah ini di modul Transfer), `assetAdminBerhakMenjalankanLangkahIniDiModulTransfer_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_TRF_PASSWORD`.
- Akun berikutnya (ganti akun eksplisit, login pada langkah 19): Asset Admin (berhak menjalankan langkah ini di modul Disposal), `assetAdminBerhakMenjalankanLangkahIniDiModulDisposal_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_DSP_PASSWORD`.
- Akun berikutnya (ganti akun eksplisit, login pada langkah 26): Asset Admin (berhak menjalankan langkah ini di modul Stock opname), `assetAdminBerhakMenjalankanLangkahIniDiModulStockOpname_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_OPN_PASSWORD`.
- Nama env password didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun aktor, lihat `suite.md`; spec ini tidak mengubahnya.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (kunci fixture ditandai untuk tim FE); data aset dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) yang dapat diatur membaca atau tidak membaca Tag aset tertentu; seed dan pemulihan aset, Tag Paired, laporan Tag, transaksi dan sesi opname lewat fixture backend; berkas gambar uji untuk bidang "Foto aset" (`Fixture.fixed-asset-tag.fotoAset`); pembacaan state backend (laporan Tag, status aset, flag Manual identification pada transaksi) dipakai hanya untuk butir Expected TC. Tidak ada endpoint yang dikarang di spec ini.
- Kondisi Tag: T1 = satu Tag RFID Paired yang dapat dipindai tanpa laporan terbuka. Simulator reader diatur membaca Tag aset T1. Aset TC-FA-TAG-1482 tidak punya Tag Paired sama sekali dan Asset Name-nya Non-TAG.
- Aset TC-FA-TAG-1482 ('Forklift Manual - 74', AST-0074) pada TC diganti aset Non-TAG milik spec dengan atribut yang sama (Group Plant A, tanpa Tag Paired) agar target aksi tulis tidak memakai data Pre-setup bersama; asersi tidak bergantung pada nama aset.
- Transaction Policy tiap modul memakai nilai bawaan dan tidak diubah. Sesi opname berjalan yang memuat aset uji disiapkan lewat fixture backend.

- Data aset uji (dibuat spec ini di hook `before`, nama bersuffix `{runId}-321`; dihapus atau dikembalikan di hook `after`):

  | Kunci fixture | Nama aset | Kondisi Tag | Status aset | TC |
  |---|---|---|---|---|
  | `asetAsgT1` | Aset Matriks Assign T1 {runId}-321 | T1 | Available (Group Plant B) | 1155 |
  | `asetAsgNonTag` | Aset Matriks Assign Non-TAG {runId}-321 | Tanpa Tag Paired (Asset Name Non-TAG) | Available (Group Plant A) | 1482 |
  | `asetLdT1` | Aset Matriks Load T1 {runId}-321 | T1 | Available, Transfer Request disetujui (Group Plant B) | 1179 |
  | `asetRqT1` | Aset Matriks Request T1 {runId}-321 | T1 | Available (Group Plant B) | 1187 |
  | `asetOpnT1` | Aset Matriks Opname T1 {runId}-321 | T1 | Termuat di sesi opname berjalan (Group Plant B) | 1197 |

- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus aset uji, Tag, laporan Tag, dan transaksi buatan spec; kembalikan status reader simulator. Sesi opname buatan spec ditutup atau dihapus.
- State global: tidak ada yang diubah selain data milik spec; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1155: Assign / serah ke pemegang baru pada kondisi T1

1. Buka layar transaksi Assignment untuk aset `Aset Matriks Assign T1 {runId}-321`
2. Jalankan langkah "Assign / serah ke pemegang baru"
3. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil
4. Lanjutkan langkah "Assign / serah ke pemegang baru" sampai selesai
5. Verifikasi langkah "Assign / serah ke pemegang baru" pada Assignment berjalan normal sampai selesai

### TC-FA-TAG-1482: Assign pada aset Asset Name Non-TAG tanpa Tag Paired berjalan normal dan bukan kondisi T4

6. Buka layar transaksi Assignment untuk aset `Aset Matriks Assign Non-TAG {runId}-321`
7. Jalankan langkah "Assign / serah ke pemegang baru"
8. Verifikasi langkah "Assign / serah ke pemegang baru" berjalan normal sampai selesai
9. Verifikasi pesan blok "This asset can't be assigned until its TAG is replaced. Ask a TAG administrator of Plant A." tidak tampil karena aset bukan T4 (Asset Name Non-TAG tidak menuntut Tag yang dikelola menu TAG)
10. Verifikasi tombol `[Report TAG]` dan tombol `[Replace TAG]` tidak tampil

### TC-FA-TAG-1179: Load (mulai In Transfer Process) pada kondisi T1

11. Ganti akun: Logout dari akun yang sedang aktif
12. Login sebagai Asset Admin (berhak menjalankan langkah ini di modul Transfer) dengan `assetAdminBerhakMenjalankanLangkahIniDiModulTransfer_automated_{namaCompany}@qwertysystem.net` dan `Spectra.env.FA_TAG_AA_TRF_PASSWORD`
13. Buka layar transaksi Transfer untuk aset `Aset Matriks Load T1 {runId}-321`
14. Jalankan langkah "Load (mulai In Transfer Process)"
15. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil
16. Lanjutkan langkah "Load (mulai In Transfer Process)" sampai selesai
17. Verifikasi langkah "Load (mulai In Transfer Process)" pada Transfer berjalan normal sampai selesai

### TC-FA-TAG-1187: Request pada kondisi T1

18. Ganti akun: Logout dari akun yang sedang aktif
19. Login sebagai Asset Admin (berhak menjalankan langkah ini di modul Disposal) dengan `assetAdminBerhakMenjalankanLangkahIniDiModulDisposal_automated_{namaCompany}@qwertysystem.net` dan `Spectra.env.FA_TAG_AA_DSP_PASSWORD`
20. Buka layar transaksi Disposal untuk aset `Aset Matriks Request T1 {runId}-321`
21. Jalankan langkah "Request"
22. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil
23. Lanjutkan langkah "Request" sampai selesai
24. Verifikasi langkah "Request" pada Disposal berjalan normal sampai selesai

### TC-FA-TAG-1197: Scan aset (found) pada kondisi T1

25. Ganti akun: Logout dari akun yang sedang aktif
26. Login sebagai Asset Admin (berhak menjalankan langkah ini di modul Stock opname) dengan `assetAdminBerhakMenjalankanLangkahIniDiModulStockOpname_automated_{namaCompany}@qwertysystem.net` dan `Spectra.env.FA_TAG_AA_OPN_PASSWORD`
27. Buka layar transaksi Stock opname untuk aset `Aset Matriks Opname T1 {runId}-321`
28. Jalankan langkah "Scan aset (found)"
29. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tidak tampil dan pesan blok "This asset can't be ..." tidak tampil
30. Lanjutkan langkah "Scan aset (found)" sampai selesai
31. Verifikasi langkah "Scan aset (found)" pada Stock opname berjalan normal sampai selesai

## Notes

- Mode: FE+BE.
- TC-FA-TAG-1156 sampai 1161 ada di spec 305, TC-FA-TAG-1180 sampai 1185 di spec 309, TC-FA-TAG-1188 sampai 1192 di spec 311, dan TC-FA-TAG-1198 sampai 1202 di spec 313.
- Langkah penghubung (tanpa awalan `Verifikasi`): 11, 12, 18, 19, 25, 26 (penyiapan ulang kondisi aset lewat fixture BE, penutupan popup, pembukaan menu, penggantian akun, dan penantian aksi selesai sesuai isi langkah).
- Ganti akun pada langkah 11 sampai 12, 18 sampai 19, dan 25 sampai 26 mengikuti Role di precondition TC masing-masing (Asset Admin per modul); akun pertama (Assignment) login di hook `before`.
- Temuan untuk QA:
  - Langkah "Jalankan langkah ..." di TC tidak menjabarkan layar, field, dan urutan klik transaksi; spec menulisnya sebagai satu langkah dan penjabarannya diserahkan ke tahap script.
  - TC tidak menyebut Group aset kondisi T1 dan T2; spec memakai Group Plant B seperti aset kondisi T3 dan T4.
  - TC-FA-TAG-1155, 1179, 1187, dan 1197 (kondisi T1) menuliskan peringatan dan pesan blok "tidak tampil"; peringatan muncul pada Langkah Mulai (PRD tag.md §7 S-25), sehingga spec mengasersi ketiadaannya tepat sesudah langkah dijalankan dan sebelum dilanjutkan sampai selesai (bagian 8b butir 5 dan 11); pemicunya menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berjalan normal sampai selesai.
  - Kolom Post Condition semua TC di spec ini bernilai `-`; tidak ada Post Condition yang perlu diasersi.
