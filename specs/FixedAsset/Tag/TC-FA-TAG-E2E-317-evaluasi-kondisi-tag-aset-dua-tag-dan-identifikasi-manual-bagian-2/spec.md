---
id: TC-FA-TAG-E2E-317-evaluasi-kondisi-tag-aset-dua-tag-dan-identifikasi-manual-bagian-2
title: "Identifikasi Manual: Hanya Tag yang Dipilih Dilaporkan dan Aset T4 Tanpa Report"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1217
  - TC-FA-TAG-1218
coverage:
  web: automated
---

# Identifikasi Manual: Hanya Tag yang Dipilih Dilaporkan dan Aset T4 Tanpa Report

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Asset Admin, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Nama env password didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun aktor, lihat `suite.md`; spec ini tidak mengubahnya.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (kunci fixture ditandai untuk tim FE); data aset dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) yang dapat diatur membaca atau tidak membaca Tag aset tertentu; seed dan pemulihan aset, Tag Paired, laporan Tag, transaksi dan sesi opname lewat fixture backend; berkas gambar uji untuk bidang "Foto aset" (`Fixture.fixed-asset-tag.fotoAset`); pembacaan state backend (laporan Tag, status aset, flag Manual identification pada transaksi) dipakai hanya untuk butir Expected TC. Tidak ada endpoint yang dikarang di spec ini.
- Data (Pre-setup TC, literal): aset `AST-0044` (Group Plant B) dengan Tag `RF-00132` dan `QR-00232` berstatus Paired; aset `AST-0600` (TAG Type Asset Name RFID, tanpa Tag Paired). Keadaan awal di hook `before`: `AST-0044` Borrowed, kedua Tag tidak terbaca dan tanpa laporan terbuka. Langkah 8 menyiapkan ulang keadaan untuk TC-FA-TAG-1218.
- Nilai literal Pre-setup (ID aset AST-*, Asset Name, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog Tag dari Report `Unreadable` otomatis untuk `RF-00132` saja (langkah 5). Penyelesaian Check-in pada langkah 5 dan 14 tidak dinyatakan PRD tag.md atau TC menimbulkan efek lain; jejak transaksi di modul Borrow tidak terpulihkan. Langkah 14 hanya mencatat flag Manual identification dan tidak membuat laporan Tag (TC-FA-TAG-1218). Penyiapan ulang kondisi lewat fixture BE (langkah 8) menyiapkan atau memulihkan state; jejak log dari penyiapan itu tidak dinyatakan PRD tag.md atau TC.
- Transaction Policy Borrow memakai nilai bawaan dan tidak diubah.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset `AST-0044` dan `AST-0600`, Tag, dan laporan Tag ke keadaan awal, tutup transaksi Borrow buatan spec, dan kembalikan status reader simulator.
- State global: tidak ada yang diubah selain data milik spec dan efek yang tidak terpulihkan yang tercatat di bawah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1217: Identifikasi manual hanya melaporkan Tag yang dipilih

1. Buka layar Check-in Borrow untuk aset `AST-0044`
2. Jalankan langkah "Check-in"
3. Klik `[I can't scan the TAG]`
4. Hilangkan centang `QR-00232` sehingga hanya `RF-00132` tercentang
5. Unggah Foto aset dan lanjutkan sampai Check-in selesai
6. Verifikasi laporan terbuka "Unreadable" dibuat hanya untuk `RF-00132` (dibaca lewat kemampuan baca state backend)
7. Verifikasi `QR-00232` tidak punya laporan (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1218: Identifikasi manual pada aset T4 hanya mencatat flag tanpa Report

8. Siapkan ulang kondisi lewat fixture BE: aset `AST-0600` Borrowed dengan TAG Type Asset Name RFID tetapi tanpa Tag Paired (T4)
9. Buka layar Check-in Borrow untuk aset `AST-0600`
10. Jalankan langkah "Check-in"
11. Klik `[I can't scan the TAG]`
12. Verifikasi bidang "Foto aset" tampil pada formulir identifikasi manual
13. Verifikasi tidak ada checkbox Tag untuk dipilih
14. Unggah Foto aset dan lanjutkan sampai Check-in selesai
15. Verifikasi transaksi dicatat dengan flag Manual identification (dibaca lewat kemampuan baca state backend)
16. Verifikasi tidak ada laporan Tag yang dibuat (dibaca lewat kemampuan baca state backend)

## Notes

- Mode: FE+BE.
- TC-FA-TAG-1211 sampai 1215 ada di spec 316. TC-FA-TAG-1216 ada di spec 322.
- Langkah penghubung (tanpa awalan `Verifikasi`): 8 (penyiapan ulang kondisi aset lewat fixture BE, penutupan popup, pembukaan menu, penggantian akun, dan penantian aksi selesai sesuai isi langkah).
- Langkah 12 (bidang "Foto aset" tampil) adalah asersi tambahan di luar Expected TC-FA-TAG-1218 (S-03), dipakai sebagai anchor positif bagi langkah tidak ada checkbox Tag dan harus berada sebelum unggah foto karena formulir tertutup sesudahnya.
- A-15: nilai literal Pre-setup (ID aset AST-*, Asset Name, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog Tag dari Report `Unreadable` otomatis untuk `RF-00132` saja (langkah 5). Penyelesaian Check-in pada langkah 5 dan 14 tidak dinyatakan PRD tag.md atau TC menimbulkan efek lain; jejak transaksi di modul Borrow tidak terpulihkan. Langkah 14 hanya mencatat flag Manual identification dan tidak membuat laporan Tag (TC-FA-TAG-1218). Penyiapan ulang kondisi lewat fixture BE (langkah 8) menyiapkan atau memulihkan state; jejak log dari penyiapan itu tidak dinyatakan PRD tag.md atau TC.
- Temuan untuk QA:
  - Langkah "Jalankan langkah ..." di TC tidak menjabarkan layar, field, dan urutan klik transaksi; spec menulisnya sebagai satu langkah dan penjabarannya diserahkan ke tahap script.
  - TC-FA-TAG-1217 dan 1218 tidak menyebut tempat teramatinya laporan Tag dan flag Manual identification; spec membacanya lewat kemampuan baca state backend (disediakan tim FE/BE) tanpa mengarang endpoint.
