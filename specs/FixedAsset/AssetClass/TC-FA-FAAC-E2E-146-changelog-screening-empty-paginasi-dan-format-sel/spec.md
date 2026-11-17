---
id: TC-FA-FAAC-E2E-146-changelog-screening-empty-paginasi-dan-format-sel
title: "Modal Changelog: Screening, Empty State, Hasil Search Kosong, Paginasi, dan Format Sel"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-472
  - TC-FA-FAAC-473
  - TC-FA-FAAC-474
  - TC-FA-FAAC-475
  - TC-FA-FAAC-476
sourceRules: ["§4.7#r8", "§4.1#r9", "§8#r1", "§4.1.1#p10", "§4.1.1#r26", "§4.1.1#r27", "§4.1.1#r28", "§4.1.1#r29", "§4.1.1#r30", "§4.1.1#r31", "§4.1.1#r32", "§4.1#r10", "§4.1.1#r33", "§5#b5", "§9.5#r5", "ST-27", "§4.1.1#r34", "§4.1.1#r35", "§4.1.1#r36", "§4.1.1#r37", "§4.1.1#r38", "§4.1.1#r39", "§4.1.1#r40", "§4.1.1#r41", "§4.1.1#r42", "§4.1.1#r43", "§4.1.1#r44", "§4.1.1#r45", "§4.1.1#r46", "§4.1.1#r47", "§4.1.1#r48", "§4.1.1#r49", "§4.1.1#r50", "§4.1.1#r51", "J-01"]
smoke: []
dependsOn: []
trace:
  "§4.7#r8": 2
  "§4.1#r9": 4
  "§8#r1": 4
  "§4.1.1#p10": 5
  "§4.1.1#r26": [6, 7]
  "§4.1.1#r27": 6
  "§4.1.1#r28": 6
  "§4.1.1#r29": 6
  "§4.1.1#r30": 6
  "§4.1.1#r31": 6
  "§4.1.1#r32": [6, 22, 25]
  "§4.1#r10": 6
  "§4.1.1#r33": [8, 19]
  "§5#b5": [9, 13, 14, 16]
  "§9.5#r5": [9, 13, 14]
  "ST-27": [11, 31]
  "§4.1.1#r34": [19, 21]
  "§4.1.1#r35": 19
  "§4.1.1#r36": 19
  "§4.1.1#r37": 19
  "§4.1.1#r38": 19
  "§4.1.1#r39": 19
  "§4.1.1#r40": 19
  "§4.1.1#r41": 19
  "§4.1.1#r42": 19
  "§4.1.1#r43": 19
  "§4.1.1#r44": 19
  "§4.1.1#r45": 19
  "§4.1.1#r46": 19
  "§4.1.1#r47": 19
  "§4.1.1#r48": 19
  "§4.1.1#r49": 19
  "§4.1.1#r50": 19
  "§4.1.1#r51": [19, 27]
  "J-01": 23
anchor: [18]
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
