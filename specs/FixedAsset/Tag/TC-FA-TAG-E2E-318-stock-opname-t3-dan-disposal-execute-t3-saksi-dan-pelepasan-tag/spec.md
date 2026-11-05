---
id: TC-FA-TAG-E2E-318-stock-opname-t3-dan-disposal-execute-t3-saksi-dan-pelepasan-tag
title: "Stock Opname T3 dan Disposal Execute T3: Found (manual), Saksi, dan Pelepasan Tag"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1219
  - TC-FA-TAG-1220
  - TC-FA-TAG-1221
  - TC-FA-TAG-1222
coverage:
  web: automated
---

# Stock Opname T3 dan Disposal Execute T3: Found (manual), Saksi, dan Pelepasan Tag

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Asset Admin, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_AA_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Nama env password didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk akun aktor, lihat `suite.md`; spec ini tidak mengubahnya.
- Fixture `fixtures/fixed-asset-tag.json` belum ada (kunci fixture ditandai untuk tim FE); data aset dirujuk lewat `Fixture.fixed-asset-tag.<kunci>` setelah berkas itu dibuat. Seeding dan pemulihan idempotent lewat fixture backend (kemampuan disediakan tim FE/BE).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB (lihat `suite.md`) yang dapat diatur membaca atau tidak membaca Tag aset tertentu; seed dan pemulihan aset, Tag Paired, laporan Tag, transaksi dan sesi opname lewat fixture backend; berkas gambar uji untuk bidang "Foto aset" (`Fixture.fixed-asset-tag.fotoAset`); pembacaan state backend (laporan Tag, status aset, flag Manual identification pada transaksi) dipakai hanya untuk butir Expected TC. Tidak ada endpoint yang dikarang di spec ini.
- Data (Pre-setup TC, literal): aset `AST-0020` ('Excavator 20 Ton - 20', Group Plant B) dengan Tag RFID `RF-00130` berstatus Paired dan tidak terbaca (T3). Keadaan awal di hook `before`: sesi opname berjalan memuat `AST-0020`, `RF-00130` tanpa laporan terbuka. Langkah 7, 16, dan 22 menyiapkan ulang keadaan untuk TC berikutnya. Pengguna `Budi S.` (saksi) disediakan tim FE karena tidak ada di Tabel Data Uji Pre-setup TC.
- Nilai literal Pre-setup (ID aset AST-*, Asset Name, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog Tag dari Report `Unreadable` otomatis untuk `RF-00130` (langkah 4); entri TAG Log Global dari penyelesaian disposal (Tag masuk To Be Returned) (langkah 27). Penyelesaian sesi opname (langkah 4, 11) dan catatan identifikasi manual yang ditambahkan ke laporan Missing yang sudah ada (langkah 11) tidak dinyatakan PRD tag.md atau TC menimbulkan entri lain; jejak transaksi di modul Stock Opname tidak terpulihkan. Penyelesaian Execute disposal (langkah 27) tidak dinyatakan PRD tag.md atau TC menimbulkan entri lain di modul Disposal; jejak transaksi di modul Disposal tidak terpulihkan. Langkah Execute tanpa saksi (langkah 20) tidak dapat diselesaikan dan tidak menambah entri. Penyiapan ulang kondisi lewat fixture BE (langkah 7, 16, 22) menyiapkan atau memulihkan state; jejak log dari penyiapan itu tidak dinyatakan PRD tag.md atau TC.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset `AST-0020`, Tag `RF-00130`, laporan Tag, sesi opname, dan transaksi Disposal buatan spec ke keadaan awal, dan kembalikan status reader simulator.
- State global: tidak ada yang diubah selain data milik spec dan efek yang tidak terpulihkan yang tercatat di bawah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1219: Stock opname T3: aset dicatat Found (manual) dan Report Unreadable dibuat

1. Buka sesi opname yang berjalan
2. Pilih aset `Excavator 20 Ton - 20`
3. Klik `[I can't scan the TAG]`
4. Unggah Foto aset dan selesaikan
5. Verifikasi aset tercatat "Found (manual)" (dibaca lewat kemampuan baca state backend)
6. Verifikasi Report "Unreadable" dibuat untuk `RF-00130` (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1220: Stock opname T3 dengan laporan terbuka: catatan ditambahkan ke laporan yang ada

7. Siapkan ulang kondisi lewat fixture BE: sesi opname berjalan memuat aset `AST-0020`, Tag `RF-00130` tidak terbaca dan punya laporan terbuka Missing
8. Buka sesi opname yang berjalan
9. Pilih aset `Excavator 20 Ton - 20`
10. Klik `[I can't scan the TAG]`
11. Unggah Foto aset dan selesaikan
12. Verifikasi aset tercatat "Found (manual)" (dibaca lewat kemampuan baca state backend)
13. Verifikasi `RF-00130` tetap punya satu laporan terbuka "Missing" (dibaca lewat kemampuan baca state backend)
14. Verifikasi laporan "Missing" itu memuat catatan tambahan (dibaca lewat kemampuan baca state backend)
15. Verifikasi tidak ada laporan kedua untuk `RF-00130` (dibaca lewat kemampuan baca state backend)

### TC-FA-TAG-1221: Disposal Execute T3 tidak dapat diselesaikan tanpa saksi

16. Siapkan ulang kondisi lewat fixture BE: aset `AST-0020` berstatus In Disposal Process dengan Tag `RF-00130` tidak terbaca (T3)
17. Buka layar Disposal Execute untuk aset `AST-0020`
18. Klik `[I can't scan the TAG]`
19. Unggah Foto aset
20. Coba selesaikan langkah Execute tanpa memilih saksi
21. Verifikasi langkah Execute tidak dapat diselesaikan sampai saksi dipilih

### TC-FA-TAG-1222: Disposal Execute T3 dengan saksi selesai dan Tag dilepas

22. Siapkan ulang kondisi lewat fixture BE: aset `AST-0020` berstatus In Disposal Process dengan Tag RFID `RF-00130` tidak terbaca (T3); pengguna lain `Budi S.` berada dalam scope aset
23. Buka layar Disposal Execute untuk aset `AST-0020`
24. Klik `[I can't scan the TAG]`
25. Unggah Foto aset
26. Pilih `Budi S.` sebagai saksi
27. Selesaikan langkah Execute
28. Verifikasi Execute selesai dan nama saksi `Budi S.` dicatat bersama flag Manual identification (dibaca lewat kemampuan baca state backend)
29. Verifikasi waktu konfirmasi saksi dicatat bersama flag Manual identification (dibaca lewat kemampuan baca state backend)
30. Verifikasi Tag `RF-00130` dilepas dari aset saat disposal selesai (dibaca lewat kemampuan baca state backend)

## Notes

- Mode: FE+BE.
- Langkah penghubung (tanpa awalan `Verifikasi`): 7, 16, 22 (penyiapan ulang kondisi aset lewat fixture BE, penutupan popup, pembukaan menu, penggantian akun, dan penantian aksi selesai sesuai isi langkah).
- Verifikasi tidak ada laporan kedua (langkah 15) didahului `Verifikasi` laporan `Missing` tetap satu dan memuat catatan tambahan sebagai anchor positif.
- A-15: nilai literal Pre-setup (ID aset AST-*, Asset Name, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog Tag dari Report `Unreadable` otomatis untuk `RF-00130` (langkah 4); entri TAG Log Global dari penyelesaian disposal (Tag masuk To Be Returned) (langkah 27). Penyelesaian sesi opname (langkah 4, 11) dan catatan identifikasi manual yang ditambahkan ke laporan Missing yang sudah ada (langkah 11) tidak dinyatakan PRD tag.md atau TC menimbulkan entri lain; jejak transaksi di modul Stock Opname tidak terpulihkan. Penyelesaian Execute disposal (langkah 27) tidak dinyatakan PRD tag.md atau TC menimbulkan entri lain di modul Disposal; jejak transaksi di modul Disposal tidak terpulihkan. Langkah Execute tanpa saksi (langkah 20) tidak dapat diselesaikan dan tidak menambah entri. Penyiapan ulang kondisi lewat fixture BE (langkah 7, 16, 22) menyiapkan atau memulihkan state; jejak log dari penyiapan itu tidak dinyatakan PRD tag.md atau TC.
- Temuan untuk QA:
  - Langkah "Jalankan langkah ..." di TC tidak menjabarkan layar, field, dan urutan klik transaksi; spec menulisnya sebagai satu langkah dan penjabarannya diserahkan ke tahap script.
  - TC-FA-TAG-1219 sampai 1222 tidak menyebut tempat teramatinya status Found (manual), laporan Tag, catatan laporan, dan pelepasan Tag; spec membacanya lewat kemampuan baca state backend (disediakan tim FE/BE) tanpa mengarang endpoint.
  - TC-FA-TAG-1221 tidak menyebut tombol untuk menyelesaikan Execute tanpa saksi; spec menulis "Coba selesaikan langkah Execute tanpa memilih saksi" mengikuti TC.
  - TC-FA-TAG-1222 memakai pengguna `Budi S.` yang tidak ada di Tabel Data Uji Pre-setup; spec menulisnya sebagai pengguna yang disediakan tim FE.
  - Kolom Post Condition semua TC di spec ini bernilai `-`; tidak ada Post Condition yang perlu diasersi.
