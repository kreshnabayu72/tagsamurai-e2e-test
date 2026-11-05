---
id: TC-FA-TAG-E2E-316-evaluasi-kondisi-tag-aset-dua-tag-dan-identifikasi-manual-bagian-1
title: "Evaluasi Kondisi Tag Aset Dua Tag dan Identifikasi Manual: Penilaian T1 sampai T3, Checkbox Bawaan, dan Report Unreadable Otomatis"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-1211
  - TC-FA-TAG-1212
  - TC-FA-TAG-1213
  - TC-FA-TAG-1214
  - TC-FA-TAG-1215
coverage:
  web: automated
---

# Evaluasi Kondisi Tag Aset Dua Tag dan Identifikasi Manual: Penilaian T1 sampai T3, Checkbox Bawaan, dan Report Unreadable Otomatis

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Asset Admin, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun berikutnya (ganti akun eksplisit, login pada langkah 30): Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Nama env password didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun aktor, lihat `suite.md`; spec ini tidak mengubahnya.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (kunci fixture ditandai untuk tim FE); data aset dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) yang dapat diatur membaca atau tidak membaca Tag aset tertentu; seed dan pemulihan aset, Tag Paired, laporan Tag, transaksi dan sesi opname lewat fixture backend; berkas gambar uji untuk bidang "Foto aset" (`Fixture.fixed-asset-tag.fotoAset`); pembacaan state backend (laporan Tag, status aset, flag Manual identification pada transaksi) dipakai hanya untuk butir Expected TC. Tidak ada endpoint yang dikarang di spec ini.
- Data (Pre-setup TC, literal): aset `AST-0044` (Group Plant B) dengan Tag `RF-00132` (RFID) dan `QR-00232` (QR) berstatus Paired; aset `AST-0020` (Group Plant B) dengan Tag `RF-00130` Paired. Keadaan awal di hook `before`: `AST-0044` Available, `RF-00132` terbaca tanpa laporan, `QR-00232` punya laporan Missing terbuka. Langkah 6, 12, 16, dan 23 menyiapkan ulang keadaan aset untuk TC berikutnya.
- Nilai literal Pre-setup (ID aset AST-*, Asset Name, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog Tag dari Report `Unreadable` otomatis hasil identifikasi manual (langkah 27). Penyelesaian Check-out (langkah 10) dan Check-in (langkah 27) tidak dinyatakan PRD tag.md atau TC menimbulkan efek lain; jejak transaksi di modul Borrow tidak terpulihkan. Langkah "Check-out" pada langkah 14 diblokir dan tidak menambah entri. Penyiapan ulang kondisi lewat fixture BE (langkah 6, 12, 16, 23) menyiapkan atau memulihkan state; jejak log dari penyiapan itu tidak dinyatakan PRD tag.md atau TC.
- Transaction Policy Borrow memakai nilai bawaan dan tidak diubah. Baseline kartu `Reported` dibaca sebelum Check-in langkah 24, lewat kemampuan baca state backend (disediakan tim FE/BE).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset `AST-0044` dan `AST-0020`, Tag, dan laporan Tag ke keadaan awal, tutup transaksi Borrow buatan spec, kembalikan status reader simulator, dan kembalikan sesi ke akun default suite.
- State global: tidak ada yang diubah selain data milik spec dan efek yang tidak terpulihkan yang tercatat di bawah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1211: Aset dua Tag: satu terbaca tanpa laporan dinilai T1 walau Tag lain punya laporan terbuka

1. Buka layar Check-out Borrow untuk aset `AST-0044`
2. Jalankan langkah "Check-out"
3. Verifikasi langkah berjalan normal
4. Verifikasi langkah berjalan tanpa peringatan dan tanpa blok
5. Verifikasi identifikasi manual tidak diperlukan: opsi `[I can't scan the TAG]` tidak ditawarkan

### TC-FA-TAG-1212: Aset dua Tag: tidak ada Tag bersih tetapi ada Tag terbaca dengan laporan Damaged dinilai T2

6. Siapkan ulang kondisi lewat fixture BE: aset `AST-0044` Available, Tag `RF-00132` terbaca dan punya laporan Damaged terbuka, Tag `QR-00232` tidak terbaca
7. Buka layar Check-out Borrow untuk aset `AST-0044`
8. Jalankan langkah "Check-out"
9. Verifikasi peringatan "This asset's TAG has been reported as damaged. Consider replacing it before handing over." tampil
10. Lanjutkan langkah "Check-out" sampai selesai
11. Verifikasi langkah dapat dilanjutkan sampai selesai

### TC-FA-TAG-1213: Aset dua Tag: tidak ada Tag yang dapat dipindai dinilai T3

12. Siapkan ulang kondisi lewat fixture BE: aset `AST-0044` Available di Group Plant B, Tag `RF-00132` dan `QR-00232` keduanya tidak dapat dipindai
13. Buka layar Check-out Borrow untuk aset `AST-0044`
14. Jalankan langkah "Check-out"
15. Verifikasi langkah "Check-out" diblokir dengan pesan "This asset can't be borrowed until its TAG is replaced. Ask a TAG administrator of Plant B."

### TC-FA-TAG-1214: Identifikasi manual: semua Tag Paired aset tercentang secara bawaan

16. Siapkan ulang kondisi lewat fixture BE: aset `AST-0044` Borrowed, Tag `RF-00132` dan `QR-00232` tidak terbaca dan tanpa laporan terbuka
17. Buka layar Check-in Borrow untuk aset `AST-0044`
18. Jalankan langkah "Check-in"
19. Klik `[I can't scan the TAG]`
20. Verifikasi checkbox per Tag Paired tampil untuk `RF-00132` dan `QR-00232`
21. Verifikasi kedua checkbox tercentang secara bawaan
22. Verifikasi bidang "Foto aset" bertanda wajib (*) dengan keterangan plat atau label identitas terlihat

### TC-FA-TAG-1215: Identifikasi manual membuat Report Unreadable otomatis bila Tag belum punya laporan terbuka

23. Siapkan ulang kondisi lewat fixture BE: aset `AST-0020` Borrowed, Tag `RF-00130` tidak terbaca dan tanpa laporan terbuka; catat jumlah pada kartu `Reported` sebagai baseline (dibaca lewat kemampuan baca state backend)
24. Buka layar Check-in Borrow untuk aset `AST-0020`
25. Jalankan langkah "Check-in"
26. Klik `[I can't scan the TAG]`
27. Unggah Foto aset dan lanjutkan sampai Check-in selesai
28. Tunggu Check-in selesai (transaksi tersimpan)
29. Ganti akun: Logout dari akun yang sedang aktif
30. Login sebagai Total Control dengan `totalControl_automated_{namaCompany}@qwertysystem.net` dan `Spectra.env.FA_TC_PASSWORD`
31. Buka menu Fixed Asset > TAG lewat sidebar, tab Paired
32. Verifikasi satu laporan terbuka Report Type "Unreadable" dibuat untuk `RF-00130` (dibaca lewat kemampuan baca state backend)
33. Verifikasi aset `AST-0020` mendapat status "Tag Reported" (dibaca lewat kemampuan baca state backend)
34. Verifikasi kartu `Reported` bertambah satu dari baseline

## Notes

- Mode: FE+BE.
- TC-FA-TAG-1216 ada di spec 322. TC-FA-TAG-1217 dan 1218 ada di spec 317.
- Langkah penghubung (tanpa awalan `Verifikasi`): 6, 12, 16, 23, 28, 29, 30, 31 (penyiapan ulang kondisi aset lewat fixture BE, penutupan popup, pembukaan menu, penggantian akun, dan penantian aksi selesai sesuai isi langkah).
- Langkah 29 sampai 30 mengganti akun ke Total Control sesuai butir 4 pada kolom Langkah Uji TC-FA-TAG-1215 ("login Total Control"); langkah "Tunggu Check-in selesai" mengikuti bagian 8b butir 8 karena langkah berikutnya mengganti akun.
- Verifikasi langkah 4 (tanpa peringatan dan tanpa blok) didahului langkah berjalan normal sebagai anchor positif.
- A-15: nilai literal Pre-setup (ID aset AST-*, Asset Name, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog Tag dari Report `Unreadable` otomatis hasil identifikasi manual (langkah 27). Penyelesaian Check-out (langkah 10) dan Check-in (langkah 27) tidak dinyatakan PRD tag.md atau TC menimbulkan efek lain; jejak transaksi di modul Borrow tidak terpulihkan. Langkah "Check-out" pada langkah 14 diblokir dan tidak menambah entri. Penyiapan ulang kondisi lewat fixture BE (langkah 6, 12, 16, 23) menyiapkan atau memulihkan state; jejak log dari penyiapan itu tidak dinyatakan PRD tag.md atau TC.
- Temuan untuk QA:
  - Langkah "Jalankan langkah ..." di TC tidak menjabarkan layar, field, dan urutan klik transaksi; spec menulisnya sebagai satu langkah dan penjabarannya diserahkan ke tahap script.
  - TC-FA-TAG-1211 sampai 1213 tidak menyebut Group aset `AST-0044` untuk kondisi normal; Group Plant B dipakai karena pesan blok TC-FA-TAG-1213 menyebut Plant B.
  - TC-FA-TAG-1215 Expected a tidak menyebut tempat teramatinya laporan Unreadable; butir 4 pada kolom Langkah Uji hanya menyebut membuka Fixed Asset > TAG > Paired. Spec membaca laporan dan status "Tag Reported" lewat kemampuan baca state backend (disediakan tim FE/BE) dan hanya kartu `Reported` yang diasersi di UI.
  - TC-FA-TAG-1215 Post Condition (modul terdampak Borrow dan notification tag_report_created) tanpa langkah observasi; tidak diasersi.
  - TC-FA-TAG-1214 Expected b menyebut keterangan plat atau label identitas terlihat tanpa menyebut teksnya; spec mengasersi bahwa keterangan itu terlihat.
