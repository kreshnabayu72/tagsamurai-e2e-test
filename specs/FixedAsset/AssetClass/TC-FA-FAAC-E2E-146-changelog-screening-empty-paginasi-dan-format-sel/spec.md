---
id: TC-FA-FAAC-E2E-146-changelog-screening-empty-paginasi-dan-format-sel
title: "Modal Changelog: Screening, Empty State, Hasil Search Kosong, Paginasi, dan Format Sel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-472
  - TC-FA-FAAC-473
  - TC-FA-FAAC-474
  - TC-FA-FAAC-475
  - TC-FA-FAAC-476
coverage:
  web: automated
---

# Modal Changelog: Screening, Empty State, Hasil Search Kosong, Paginasi, dan Format Sel

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Changelog Pre-setup (hanya dibaca) mengikuti Example Data Modal Changelog PRD §4.1.1: 19 entri, tanggal format dd/mm/yy sesuai General Settings, dari Edit HEAVY-EQ Scheduled Version 28/10/26 14:30 sampai Create HEAVY-EQ Class Code 05/08/26 09:30. Kemampuan membaca dan memulihkan keadaan 19 entri itu lewat fixture BE disediakan tim FE/BE (suite.md).
- Kemampuan teknis: fixture BE yang mengubah isi Changelog Asset Class client hingga tersimpan dan memulihkannya ke 19 entri Pre-setup disediakan tim FE/BE; pemulihan juga dijalankan di hook `after`. Suite berjalan serial karena spec ini mengubah state Changelog bersama.
- Seed relatif terhadap tanggal run: entri Edit HEAVY-EQ Scheduled Version 28/10/26 14:30 memakai New Value bulan M+2 (bulan berjalan ditambah dua bulan, format MMM yyyy); fixture BE membuat seed ini relatif terhadap tanggal run, dan spec tidak menulis nama bulan literal.
- Nama kode seed (`HEAVY-EQ`, `IT-EQ`, `TEMP-EQ`, dan lain-lain) dan pelaku (Rina P, Budi S, System) memakai nilai literal Example Data apa adanya karena asersi TC bergantung pada nilai itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-472: Screening modal Changelog: Asset Class

1. Arahkan kursor ke icon Changelog
2. Verifikasi tooltip icon Changelog berbunyi `Changelog`
3. Klik icon Changelog
4. Verifikasi header modal berisi title `Changelog: Asset Class` dan tombol Close (X)
5. Verifikasi toolbar modal memuat Search, Filter, dan Download
6. Verifikasi kolom tabel berurutan Date (sortable), Action (sortable), Class Code (sortable), Field (sortable), Old Value (sortable), New Value (sortable), Modified By (sortable), dan Column Visibility `⋯` (unsortable, klik header membuka panel Column Visibility)
7. Verifikasi default sort Date Newest First
8. Verifikasi baris pertama adalah entri 28/10/26 14:30 (Edit, HEAVY-EQ, Scheduled Version, `—`, bulan M+2 dalam format MMM yyyy, Rina P)
9. Verifikasi footer memuat paginasi dengan ukuran halaman 10 dan pilihan 10 / 25 / 50 / 100

### TC-FA-FAAC-474: Empty state hasil Search tidak ditemukan

10. Ketik Search `zzzzzz` di modal, tekan Enter
11. Verifikasi empty state menampilkan illustration, title `No results found`, dan description `Try adjusting your search or filter.`
12. Klik `✕` pada kotak Search di modal, tekan Enter

### TC-FA-FAAC-475: Paginasi modal Changelog

13. Verifikasi halaman 1 menampilkan 10 entri
14. Verifikasi pilihan ukuran halaman 10 / 25 / 50 / 100
15. Klik halaman 2
16. Verifikasi halaman 2 menampilkan 9 entri sisa
17. Ganti ukuran halaman ke 25
18. Verifikasi tabel kembali ke halaman 1
19. Verifikasi tabel menampilkan 19 entri
20. Ganti ukuran halaman kembali ke 10

### TC-FA-FAAC-476: Format sel Old Value, New Value, dan Modified By

21. Verifikasi baris Delete TEMP-EQ (28/10/26 09:15) menampilkan New Value `—`
22. Verifikasi Modified By ditulis dalam format nama depan dan inisial belakang, mis. `Rina P`
23. Verifikasi Modified By `System` untuk entri tanpa user aktor
24. Arahkan kursor ke nama `Rina P` pada salah satu baris
25. Verifikasi hover pada `Rina P` menampilkan nama lengkap `Rina Pratiwi`
26. Klik halaman 2
27. Verifikasi baris Create HEAVY-EQ (05/08/26 09:30) menampilkan Old Value `—`

### TC-FA-FAAC-473: Empty state modal Changelog belum ada riwayat

28. Tutup modal Changelog dengan Close (X)
29. Kondisikan client tanpa entri Changelog Asset Class lewat fixture BE hingga tersimpan
30. Klik icon Changelog
31. Verifikasi empty state menampilkan illustration, title `No changelog yet`, dan description `Activities and changes will appear here.`
32. Tutup modal Changelog dengan Close (X)
33. Pulihkan 19 entri Changelog Pre-setup lewat fixture BE hingga tersimpan

## Notes

1. Pengecualian nama seed literal: asersi TC bergantung pada kode, tanggal, dan pelaku Example Data Changelog; data dipakai apa adanya dan hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Pengecualian total absolut Changelog (A-19, S-12): TC mengasersi total absolut seed Changelog (19 entri, lima entri System, tujuh entri Budi S, dan sejenisnya); spec 146 sampai 157 mengikuti pengecualian modul A-19 karena fixture BE mereset Changelog ke 19 entri seed sebelum blok dan memulihkannya sesudahnya, dan suite berjalan serial.
3. Perubahan urutan TC: TC-473 ditulis paling akhir karena membutuhkan client tanpa entri Changelog (state berat lewat fixture BE) dan keadaan 19 entri dipulihkan sesudahnya; TC-474 ditulis sebelum TC-475 supaya Search dikosongkan sebelum paginasi.
4. Langkah TC 'Arahkan kursor ke icon Changelog sebelum klik' ditulis sebelum klik icon karena tooltip diasersi sebelum langkah yang mengubah state (bagian 8b butir 5).
5. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 12, 20, 28, 29, 32, 33.
