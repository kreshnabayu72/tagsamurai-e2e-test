---
id: TC-FA-TAG-E2E-290-notifikasi-lintas-modul-tag-replacement-needed-report-created-bagian-2
title: "Notifikasi Lintas Modul: tag_report_declined dan tag_report_canceled"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1250
  - TC-FA-TAG-1251
  - TC-FA-TAG-1252
  - TC-FA-TAG-1253
coverage:
  web: automated
---

# Notifikasi Lintas Modul: tag_report_declined dan tag_report_canceled

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG] `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Siti R. diasumsikan nama tampil akun ini (lihat Temuan untuk QA).
- Akun aktor: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Dipakai sebagai pelaku kedua lewat sesi API (Decline Report).
- Akun aktor: GM [GM] `gm_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_GM_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Dipakai sebagai pelaku kedua lewat sesi API (Cancel Report).
- Akun Budi S. (pemegang Update di group Plant B) tidak tertulis di Tabel Pre-setup TC; disediakan tim FE. Dipakai sebagai pengamat pada blok TC-FA-TAG-1252 dan 1251 (ganti akun eksplisit).
- Login di hook `before` spec ini sebagai akun aktor pertama; hook suite `beforeEach` tidak membuka halaman Fixed Asset > TAG untuk spec ini (akun pertama SA_NOTAG tidak punya akses halaman TAG; spec dikecualikan di `suite.md` bagian Hook): dropdown notifikasi akun aktor pertama dibuka pada halaman awal setelah login di hook `before`, tanpa langkah yang membuka halaman TAG. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE, lihat `suite.md`); langkah pemicunya tidak memuat asersi di sesi itu.
- Data (Pre-setup TC, tanpa suffix): aset AST-0020 ('Excavator 20 Ton - 20', Plant B) dengan Tag tunggal `RF-00130`; laporan terbuka Damaged dari Staff Auditor Siti R. dibuat fixture sebelum tiap pemicu (precondition TC, tidak diasersi).
- Kemampuan teknis (disediakan tim FE/BE): membaca dropdown notifikasi tiap akun, menghapus notifikasi in-app tertentu milik akun, dan membuat laporan Tag lewat fixture backend.
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 2, 9, 16); entri Changelog Tag dari Report `Unreadable` otomatis hasil identifikasi manual (langkah 27); entri Changelog `Decline Report` per Tag (langkah 3, 28); entri Changelog `Cancel Report` per Tag (langkah 10, 17).
- Notifikasi in-app bersifat persisten antar run: langkah 1 menghapus notifikasi "TAG report declined" dan "TAG report canceled" untuk RF-00130 milik Siti R. dan Budi S. lewat fixture backend sebelum pemicu pertama, sehingga `Verifikasi` notifikasi pada langkah 5, 13, 20, 25, dan 31 berasal dari run ini dan absence pada langkah 15 dan 33 tidak gagal oleh notifikasi run lama. Jeda "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 14 dan 32) sebelum asersi absence notifikasi adalah pilihan spec (bukan nilai TC atau PRD) sampai TC menyatakan durasinya (bagian 6).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan capability akun Budi S. (Update di group Plant B; diatur pada langkah 2) ke nilai awal yang dicatat fixture backend sebelum langkah 2 (dikoordinasikan tim FE/BE), serta TAG Type Asset Name, aset, Tag, laporan, notifikasi "TAG report declined" dan "TAG report canceled" untuk RF-00130 milik Siti R. dan Budi S. (dihapus), dan sesi ke akun default suite lewat fixture backend.
- State global yang diubah spec ini: status laporan Tag RF-00130 dan capability akun Budi S. (Update di group Plant B; langkah 2, dipulihkan di hook `after`, didaftarkan di `suite.md`; pengecualian S-06/S-12 butir A-15). Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1250: Decline Report mengirim tag_report_declined ke pelapor

1. Bersihkan lewat fixture backend: notifikasi "TAG report declined" dan "TAG report canceled" untuk RF-00130 milik Siti R. dan Budi S. dari run atau spec sebelumnya
2. Siapkan lewat fixture backend: laporan terbuka Damaged dari Siti R. pada Tag RF-00130 (AST-0020, Plant B); Budi S. memegang Update di group Plant B
3. Pelaku kedua (Total Control) lewat sesi API melakukan Decline Report pada laporan itu dengan Reason "Tag masih terbaca" hingga tersimpan
4. Buka dropdown notifikasi
5. Verifikasi notifikasi berjudul "TAG report declined" dengan isi "Your report on RF-00130 (AST-0020) was declined." tampil
6. Verifikasi notifikasi itu hanya memuat tombol [Mark as Read] (view-only)
7. Klik notifikasi "TAG report declined"
8. Verifikasi halaman tujuan notifikasi adalah Asset Detail aset AST-0020

### TC-FA-TAG-1253: pembatal laporan tidak menerima notifikasi pembatalannya sendiri

9. Siapkan lewat fixture backend: laporan terbuka Damaged dari Siti R. pada Tag RF-00130 (AST-0020)
10. Pelaku kedua (akun Siti R. lewat sesi API) membatalkan laporannya sendiri dengan Reason "Tag ternyata terbaca" hingga tersimpan
11. Muat ulang halaman
12. Buka dropdown notifikasi
13. Verifikasi dropdown notifikasi Siti R. memuat notifikasi "TAG report declined" dari TC-FA-TAG-1250
14. Tunggu 5 detik tanpa memuat ulang halaman
15. Verifikasi tidak ada notifikasi "TAG report canceled" untuk pelaku

### TC-FA-TAG-1252: Cancel Report mengirim tag_report_canceled ke pemegang Update dan pelapor

16. Siapkan lewat fixture backend: laporan terbuka Damaged dari Siti R. pada Tag RF-00130 (AST-0020)
17. Pelaku kedua (GM) lewat sesi API membatalkan laporan itu dengan Reason "Tag ternyata terbaca" hingga tersimpan
18. Muat ulang halaman
19. Buka dropdown notifikasi
20. Verifikasi Siti R. menerima notifikasi berjudul "TAG report canceled" dengan isi "The report on RF-00130 (AST-0020) was canceled by [User Name]." (nama GM pembatal)
21. Verifikasi notifikasi Siti R. itu hanya memuat tombol [Mark as Read] (view-only)
22. Ganti akun: logout dari akun Siti R.
23. Login dengan akun Budi S.
24. Buka dropdown notifikasi
25. Verifikasi Budi S. menerima notifikasi berjudul "TAG report canceled" dengan isi "The report on RF-00130 (AST-0020) was canceled by [User Name]." (nama GM pembatal)
26. Verifikasi notifikasi Budi S. itu hanya memuat tombol [Mark as Read] (view-only)

### TC-FA-TAG-1251: Decline pada laporan otomatis dari identifikasi manual tidak mengirim notifikasi

27. Siapkan lewat fixture backend: laporan terbuka Unreadable yang dibuat otomatis dari identifikasi manual (tanpa pelapor) pada AST-0020
28. Pelaku kedua (Total Control) lewat sesi API melakukan Decline Report pada laporan itu dengan Reason "Tag masih terbaca" hingga tersimpan
29. Muat ulang halaman
30. Buka dropdown notifikasi
31. Verifikasi dropdown notifikasi Budi S. terbuka dan memuat notifikasi "TAG report canceled" dari blok TC-FA-TAG-1252
32. Tunggu 5 detik tanpa memuat ulang halaman
33. Verifikasi tidak ada notifikasi "TAG report declined" baru yang dikirim

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 1, 2, 9, 11, 16, 18, 22, 23, 27 dan 29 (membersihkan notifikasi dan menyiapkan laporan lewat fixture, memuat ulang halaman, ganti akun eksplisit, S-07), serta 14 dan 32 (Tunggu 5 detik tanpa memuat ulang halaman, bagian 6).
- Pemicu memakai pelaku kedua lewat sesi API karena hanya memicu notifikasi dan tidak diasersi di sesinya (R-20). Urutan TC (S-10): blok Siti R. (TC-FA-TAG-1250, 1253, 1252) lebih dulu, lalu blok Budi S. (TC-FA-TAG-1252, 1251) agar ganti akun hanya sekali; TC-FA-TAG-1253 diletakkan sebelum TC-FA-TAG-1252 agar belum ada notifikasi pembatalan di dropdown Siti R.
- Absence TC-FA-TAG-1253 dan 1251: didahului `Verifikasi` notifikasi lain pada dropdown yang sama sebagai anchor positif (bagian 8b butir 2); asersi diletakkan sesudah pemicu dan muat ulang tanpa asersi artefak di antaranya (bagian 8b butir 11).
- Butir A-15: Budi S. adalah akun aktor TC yang tidak ada di Tabel Pre-setup TC dan disediakan tim FE/BE khusus untuk TC ini (Update di group Plant B menurut TC-FA-TAG-1252), sehingga pengaturan capability pada langkah 2 tidak menyentuh akun Pre-setup bersama (Total Control, Manage Read Update, Manage Read, dan akun grup khusus) yang tidak boleh diubah menurut A-15. Pemulihan dilakukan di hook `after` dan perubahan didaftarkan di `suite.md`. Bila QA memetakan nama itu ke akun Pre-setup bersama (pemetaan nama ke akun ditunda ke QA), spec ini perlu direvisi karena A-15 melarang mengubah capability akun bersama. Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 2, 9, 16); entri Changelog Tag dari Report `Unreadable` otomatis hasil identifikasi manual (langkah 27); entri Changelog `Decline Report` per Tag (langkah 3, 28); entri Changelog `Cancel Report` per Tag (langkah 10, 17).
- Temuan untuk QA:
  - TC-FA-TAG-1250 dan 1252 menyebut pelapor 'Staff Auditor Siti R.'; Tabel Pre-setup TC hanya memuat akun 'Staff Auditor (tidak memegang Manage asset & TAG)' [SA_NOTAG]. Spec mengasumsikan Siti R. adalah nama tampil akun itu.
  - TC-FA-TAG-1251 langkah TC ke-7 ('Periksa dropdown notifikasi seluruh pengguna terkait') tidak menyebut pengguna; laporan otomatis tanpa pelapor, sehingga spec memeriksa dropdown Budi S. (pemegang Update Plant B).
  - TC-FA-TAG-1250 dan 1252 memakai isi notifikasi dengan placeholder [User Name]; spec mengasersi nama tampil GM pembatal.
  - TC-FA-TAG-1250 langkah TC ke-7 ('Login sbg Siti R.') dan TC-FA-TAG-1252 memakai pemicu aksi UI oleh Total Control atau GM; spec memicunya lewat sesi API dan tidak menguji dialog Decline Report atau Cancel Report (diuji di spec lain).
