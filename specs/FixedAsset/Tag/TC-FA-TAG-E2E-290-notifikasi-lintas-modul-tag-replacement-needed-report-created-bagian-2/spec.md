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
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE, lihat `suite.md`); langkah pemicunya tidak memuat asersi di sesi itu.
- Data (Pre-setup TC, tanpa suffix): aset AST-0020 ('Excavator 20 Ton - 20', Plant B) dengan Tag tunggal `RF-00130`; laporan terbuka Damaged dari Staff Auditor Siti R. dibuat fixture sebelum tiap pemicu (precondition TC, tidak diasersi).
- Kemampuan teknis (disediakan tim FE/BE): membaca dropdown notifikasi tiap akun dan membuat laporan Tag lewat fixture backend.
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan TAG Type Asset Name, aset, Tag, laporan, dan sesi ke akun default suite lewat fixture backend.
- State global yang diubah spec ini: status laporan Tag RF-00130. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1250: Decline Report mengirim tag_report_declined ke pelapor

1. Siapkan lewat fixture backend: laporan terbuka Damaged dari Siti R. pada Tag RF-00130 (AST-0020, Plant B); Budi S. memegang Update di group Plant B
2. Pelaku kedua (Total Control) lewat sesi API melakukan Decline Report pada laporan itu dengan Reason "Tag masih terbaca" hingga tersimpan
3. Buka dropdown notifikasi
4. Verifikasi notifikasi berjudul "TAG report declined" dengan isi "Your report on RF-00130 (AST-0020) was declined." tampil
5. Verifikasi notifikasi itu hanya memuat tombol [Mark as Read] (view-only)
6. Klik notifikasi "TAG report declined"
7. Verifikasi halaman tujuan notifikasi adalah Asset Detail aset AST-0020

### TC-FA-TAG-1253: pembatal laporan tidak menerima notifikasi pembatalannya sendiri

8. Siapkan lewat fixture backend: laporan terbuka Damaged dari Siti R. pada Tag RF-00130 (AST-0020)
9. Pelaku kedua (akun Siti R. lewat sesi API) membatalkan laporannya sendiri dengan Reason "Tag ternyata terbaca" hingga tersimpan
10. Muat ulang halaman
11. Buka dropdown notifikasi
12. Verifikasi dropdown notifikasi Siti R. memuat notifikasi "TAG report declined" dari TC-FA-TAG-1250
13. Verifikasi tidak ada notifikasi "TAG report canceled" untuk pelaku

### TC-FA-TAG-1252: Cancel Report mengirim tag_report_canceled ke pemegang Update dan pelapor

14. Siapkan lewat fixture backend: laporan terbuka Damaged dari Siti R. pada Tag RF-00130 (AST-0020)
15. Pelaku kedua (GM) lewat sesi API membatalkan laporan itu dengan Reason "Tag ternyata terbaca" hingga tersimpan
16. Muat ulang halaman
17. Buka dropdown notifikasi
18. Verifikasi Siti R. menerima notifikasi berjudul "TAG report canceled" dengan isi "The report on RF-00130 (AST-0020) was canceled by [User Name]." (nama GM pembatal)
19. Verifikasi notifikasi Siti R. itu hanya memuat tombol [Mark as Read] (view-only)
20. Ganti akun: logout dari akun Siti R.
21. Login dengan akun Budi S.
22. Buka dropdown notifikasi
23. Verifikasi Budi S. menerima notifikasi berjudul "TAG report canceled" dengan isi "The report on RF-00130 (AST-0020) was canceled by [User Name]." (nama GM pembatal)
24. Verifikasi notifikasi Budi S. itu hanya memuat tombol [Mark as Read] (view-only)

### TC-FA-TAG-1251: Decline pada laporan otomatis dari identifikasi manual tidak mengirim notifikasi

25. Siapkan lewat fixture backend: laporan terbuka Unreadable yang dibuat otomatis dari identifikasi manual (tanpa pelapor) pada AST-0020
26. Pelaku kedua (Total Control) lewat sesi API melakukan Decline Report pada laporan itu dengan Reason "Tag masih terbaca" hingga tersimpan
27. Muat ulang halaman
28. Buka dropdown notifikasi
29. Verifikasi dropdown notifikasi Budi S. terbuka dan memuat notifikasi "TAG report canceled" dari blok TC-FA-TAG-1252
30. Verifikasi tidak ada notifikasi "TAG report declined" baru yang dikirim

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 1, 8, 10, 14, 16, 20, 21, 25 dan 27 (menyiapkan laporan lewat fixture, memuat ulang halaman, ganti akun eksplisit, S-07).
- Pemicu memakai pelaku kedua lewat sesi API karena hanya memicu notifikasi dan tidak diasersi di sesinya (R-20). Urutan TC (S-10): blok Siti R. (TC-FA-TAG-1250, 1253, 1252) lebih dulu, lalu blok Budi S. (TC-FA-TAG-1252, 1251) agar ganti akun hanya sekali; TC-FA-TAG-1253 diletakkan sebelum TC-FA-TAG-1252 agar belum ada notifikasi pembatalan di dropdown Siti R.
- Absence TC-FA-TAG-1253 dan 1251: didahului `Verifikasi` notifikasi lain pada dropdown yang sama sebagai anchor positif (bagian 8b butir 2); asersi diletakkan sesudah pemicu dan muat ulang tanpa asersi artefak di antaranya (bagian 8b butir 11).
- Temuan untuk QA:
  - TC-FA-TAG-1250 dan 1252 menyebut pelapor 'Staff Auditor Siti R.'; Tabel Pre-setup TC hanya memuat akun 'Staff Auditor (tidak memegang Manage asset & TAG)' [SA_NOTAG]. Spec mengasumsikan Siti R. adalah nama tampil akun itu.
  - TC-FA-TAG-1251 langkah TC ke-7 ('Periksa dropdown notifikasi seluruh pengguna terkait') tidak menyebut pengguna; laporan otomatis tanpa pelapor, sehingga spec memeriksa dropdown Budi S. (pemegang Update Plant B).
  - TC-FA-TAG-1250 dan 1252 memakai isi notifikasi dengan placeholder [User Name]; spec mengasersi nama tampil GM pembatal.
  - TC-FA-TAG-1250 langkah TC ke-7 ('Login sbg Siti R.') dan TC-FA-TAG-1252 memakai pemicu aksi UI oleh Total Control atau GM; spec memicunya lewat sesi API dan tidak menguji dialog Decline Report atau Cancel Report (diuji di spec lain).
