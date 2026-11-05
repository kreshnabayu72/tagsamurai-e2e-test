---
id: TC-FA-TAG-E2E-322-replace-tag-saat-borrow-dan-sesi-opname-serta-identifikasi-manual-laporan-terbuka
title: "Identifikasi Manual pada Tag dengan Laporan Terbuka serta Replace TAG saat Borrow dan Sesi Opname"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1216
  - TC-FA-TAG-1225
  - TC-FA-TAG-1228
coverage:
  web: automated
---

# Identifikasi Manual pada Tag dengan Laporan Terbuka serta Replace TAG saat Borrow dan Sesi Opname

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Asset Admin, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun berikutnya (ganti akun eksplisit, login pada langkah 7): Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Nama env password didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun aktor, lihat `suite.md`; spec ini tidak mengubahnya.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (kunci fixture ditandai untuk tim FE); data aset dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) dengan satu reader tersambung, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin; seed dan pemulihan idempotent aset, Tag per status registri (Paired, Available), transaksi, dan sesi opname lewat fixture backend; pembacaan state backend (status aset dan data transaksi) dipakai hanya untuk butir Expected TC. Tidak ada endpoint yang dikarang di spec ini.
- Data (Pre-setup TC, literal): aset `AST-0020` ('Excavator 20 Ton - 20', Group Plant B) dengan Tag RFID `RF-00130` berstatus Paired; Tag RFID `RF-00500` berstatus Available di registri Global. Keadaan awal di hook `before` (TC-FA-TAG-1216): aset Borrowed, `RF-00130` tidak terbaca dan punya laporan terbuka Missing. Langkah 12 dan 23 menyiapkan ulang keadaan aset untuk TC berikutnya.
- Nilai literal Pre-setup (ID aset AST-*, Asset Name, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 16, 27); entri TAG Log Global (langkah 16, 27). Penyelesaian Check-in (langkah 4), catatan identifikasi manual yang ditambahkan ke laporan Missing yang sudah ada (langkah 4), dan pemindaian Tag baru pada sesi opname (langkah 30) tidak dinyatakan PRD tag.md atau TC menimbulkan entri lain; jejak transaksi di modul Borrow dan Stock Opname tidak terpulihkan. Penyiapan ulang kondisi lewat fixture BE (langkah 12, 23) menyiapkan atau memulihkan state; jejak log dari penyiapan itu tidak dinyatakan PRD tag.md atau TC.
- Transaction Policy Borrow memakai nilai bawaan dan tidak diubah.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset `AST-0020`, Tag `RF-00130` dan `RF-00500` (status registri Global), laporan Tag, transaksi Borrow, sesi opname, dan status reader simulator ke keadaan awal, dan kembalikan sesi ke akun default suite.
- State global: stok Tag RFID di registri Global dan status Tag pengganti diubah spec ini dan dipulihkan di hook `after`; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1216: Identifikasi manual pada Tag yang sudah punya laporan terbuka hanya menambah catatan

1. Buka layar Check-in Borrow untuk aset `AST-0020`
2. Jalankan langkah "Check-in"
3. Klik `[I can't scan the TAG]`
4. Unggah Foto aset dan lanjutkan sampai Check-in selesai
5. Tunggu Check-in selesai (transaksi tersimpan)
6. Ganti akun: Logout dari akun yang sedang aktif
7. Login sebagai Total Control dengan `totalControl_automated_{namaCompany}@qwertysystem.net` dan `Spectra.env.FA_TC_PASSWORD`
8. Buka menu Fixed Asset > TAG lewat sidebar, tab Paired
9. Verifikasi `RF-00130` tetap punya satu laporan terbuka dengan Report Type "Missing" (Report Type tidak berubah) (dibaca lewat kemampuan baca state backend)
10. Verifikasi catatan identifikasi manual ditambahkan ke laporan yang ada (dibaca lewat kemampuan baca state backend)
11. Verifikasi tidak ada laporan kedua untuk `RF-00130` (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1225: Replace TAG pada aset berstatus Borrowed diizinkan

12. Siapkan ulang kondisi lewat fixture BE: aset `AST-0020` dengan Tag `RF-00130` Paired berstatus Borrowed; Tag `RF-00500` Available di Global
13. Buka Popup Assets group Plant B
14. Pilih row action "Replace TAG" pada aset `Excavator 20 Ton - 20` (`AST-0020`)
15. Pindai Tag pengganti `RF-00500` (Available) dengan simulator reader
16. Klik `[Submit]`
17. Verifikasi toast "Success, TAG has been replaced." tampil
18. Buka layar Check-in Borrow untuk aset `AST-0020`
19. Pindai Tag baru `RF-00500` dengan simulator reader
20. Verifikasi Check-in aset ini memindai Tag baru `RF-00500`
21. Verifikasi data check-out tetap mencatat Tag lama `RF-00130` (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1228: Replace TAG pada aset berstatus Sesi opname berjalan diizinkan

22. Buka menu Fixed Asset > TAG lewat sidebar, tab Paired
23. Siapkan ulang kondisi lewat fixture BE: aset `AST-0020` dengan Tag `RF-00130` Paired berstatus Sesi opname berjalan; Tag `RF-00500` Available di Global
24. Buka Popup Assets group Plant B
25. Pilih row action "Replace TAG" pada aset `Excavator 20 Ton - 20` (`AST-0020`)
26. Pindai Tag pengganti `RF-00500` (Available) dengan simulator reader
27. Klik `[Submit]`
28. Verifikasi toast "Success, TAG has been replaced." tampil
29. Buka sesi opname yang berjalan
30. Pindai Tag baru `RF-00500` dengan simulator reader
31. Verifikasi scan Tag baru `RF-00500` pada sesi opname dihitung sebagai ditemukan

## Notes

- Mode: FE+BE.
- TC-FA-TAG-1211 sampai 1215 ada di spec 316, TC-FA-TAG-1217 dan 1218 di spec 317, dan TC-FA-TAG-1224, 1226, 1227, dan 1229 di spec 319.
- Langkah penghubung (tanpa awalan `Verifikasi`): 5, 6, 7, 8, 12, 22, 23 (penyiapan ulang kondisi aset lewat fixture BE, penutupan popup, pembukaan menu, penggantian akun, dan penantian aksi selesai sesuai isi langkah).
- Langkah 6 sampai 7 mengganti akun ke Total Control sesuai butir 4 pada kolom Langkah Uji TC-FA-TAG-1216 ("login Total Control"); akun Total Control tetap dipakai untuk TC-FA-TAG-1225 dan 1228. Langkah "Tunggu Check-in selesai" mengikuti bagian 8b butir 8 karena langkah berikutnya mengganti akun.
- Verifikasi tidak ada laporan kedua (langkah 11) didahului `Verifikasi` laporan `Missing` tetap satu sebagai anchor positif.
- A-15: nilai literal Pre-setup (ID aset AST-*, Asset Name, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 16, 27); entri TAG Log Global (langkah 16, 27). Penyelesaian Check-in (langkah 4), catatan identifikasi manual yang ditambahkan ke laporan Missing yang sudah ada (langkah 4), dan pemindaian Tag baru pada sesi opname (langkah 30) tidak dinyatakan PRD tag.md atau TC menimbulkan entri lain; jejak transaksi di modul Borrow dan Stock Opname tidak terpulihkan. Penyiapan ulang kondisi lewat fixture BE (langkah 12, 23) menyiapkan atau memulihkan state; jejak log dari penyiapan itu tidak dinyatakan PRD tag.md atau TC.
- Temuan untuk QA:
  - Langkah "Jalankan langkah ..." di TC tidak menjabarkan layar, field, dan urutan klik transaksi; spec menulisnya sebagai satu langkah dan penjabarannya diserahkan ke tahap script.
  - TC-FA-TAG-1216 tidak menyebut tempat teramatinya laporan Tag dan catatan identifikasi manual; spec membacanya lewat kemampuan baca state backend (disediakan tim FE/BE) tanpa mengarang endpoint.
  - TC-FA-TAG-1225 Expected b dan c (Check-in memindai Tag baru, data check-out mencatat Tag lama) tidak menyebut tempat teramatinya; sumber data check-out dibaca lewat kemampuan baca state backend.
  - TC-FA-TAG-1228 Expected b ("dihitung sebagai ditemukan") tidak menyebut tempat teramatinya hasil scan pada sesi opname; spec mengasersinya di sesi opname yang dibuka.
  - Kolom Post Condition semua TC di spec ini bernilai `-`; tidak ada Post Condition yang perlu diasersi.
