---
id: TC-FA-FAAC-E2E-152-changelog-sort-3-state-dan-setup-column-screening
title: "Modal Changelog: Sort Tiga Tahap Kolom Date dan Kolom Campuran, serta Screening Column Visibility dan Setup Column"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-499
  - TC-FA-FAAC-501
  - TC-FA-FAAC-502
  - TC-FA-FAAC-503
sourceRules: ["§4.1.1#r26", "§4.1.1#r27", "§4.1.1#r28", "§4.1.1#r29", "§4.1.1#r30", "§4.1.1#r31", "§4.1.1#r32", "§4.4#r15", "§4.1#r10", "§4.1.1#p9", "§4.1.1#r33", "§4.4#r14", "§4.1.1#r51"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r26": [3, 4, 8, 9, 13, 15, 17, 20]
  "§4.1.1#r27": [3, 4, 8, 9]
  "§4.1.1#r28": [3, 4, 8, 9]
  "§4.1.1#r29": [3, 4, 8, 9]
  "§4.1.1#r30": [3, 4, 8, 9, 22, 24]
  "§4.1.1#r31": [3, 4, 8, 9, 28, 30]
  "§4.1.1#r32": [3, 4, 8, 9]
  "§4.4#r15": 5
  "§4.1#r10": 5
  "§4.1.1#p9": [13, 20]
  "§4.1.1#r33": [13, 17]
  "§4.4#r14": [15, 17, 19, 22, 24, 26, 28, 30, 32]
  "§4.1.1#r51": 15
anchor: [7, 10, 11]
coverage:
  web: automated
---

# Modal Changelog: Sort Tiga Tahap Kolom Date dan Kolom Campuran, serta Screening Column Visibility dan Setup Column

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data Changelog Pre-setup (hanya dibaca) mengikuti Example Data Modal Changelog PRD §4.1.1: 19 entri, tanggal format dd/mm/yy sesuai General Settings, dari Edit HEAVY-EQ Scheduled Version 28/10/26 14:30 sampai Create HEAVY-EQ Class Code 05/08/26 09:30. Kemampuan membaca dan memulihkan keadaan 19 entri itu lewat fixture BE disediakan tim FE/BE (suite.md).
- Syarat A-19 (S-12): TC mengasersi total absolut seed Changelog (19 entri); fixture BE mereset Changelog Asset Class ke 19 entri seed sebelum spec ini dan memulihkannya ke 19 entri di hook `after`; suite berjalan serial.
- Nama kode seed (`HEAVY-EQ`, `IT-EQ`, `TEMP-EQ`, dan lain-lain) dan pelaku (Rina P, Budi S, System) memakai nilai literal Example Data apa adanya karena asersi TC bergantung pada nilai itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Klik icon Changelog

### TC-FA-FAAC-502: Screening panel Column Visibility

2. Klik ikon `⋯` pada header kolom Actions modal
3. Verifikasi panel memuat daftar kolom berurutan Date, Action, Class Code, Field, Old Value, New Value, dan Modified By dengan drag handle
4. Verifikasi ketujuh checkbox tercentang dan Enabled
5. Verifikasi item `Setup Column...` tampil di bagian bawah panel

### TC-FA-FAAC-503: Screening modal Setup Column dari modal Changelog

6. Klik `Setup Column...`
7. Verifikasi header Setup Column berisi title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan tombol Close (X)
8. Verifikasi body memuat tujuh kolom tercentang dengan drag handle dan icon Pin
9. Verifikasi tabel Changelog di balik modal menampilkan ketujuh kolom
10. Verifikasi footer memuat `Reset to Default` dan `Save`
11. Verifikasi tidak ada tombol `Cancel` pada footer
12. Klik Close (X) pada Setup Column

### TC-FA-FAAC-499: Sort tiga tahap pada kolom Date

13. Verifikasi default Date Newest First dengan entri pertama 28/10/26 14:30
14. Klik header `Date` satu kali
15. Verifikasi klik 1 Oldest First dengan entri pertama Create HEAVY-EQ 05/08/26 09:30
16. Klik header `Date` kedua kali
17. Verifikasi klik 2 Newest First dengan entri pertama 28/10/26 14:30
18. Klik header `Date` ketiga kali
19. Verifikasi indikator sort `Date` netral
20. Verifikasi urutan kembali ke default Date Newest First

### TC-FA-FAAC-501: Sort tiga tahap pada kolom Old Value dan New Value bertipe campuran

21. Klik header `Old Value` satu kali
22. Verifikasi Old Value klik 1 (naik): nilai angka lebih dulu (48, 50, 96), lalu nilai teks, dan entri bernilai `—` di akhir
23. Klik header `Old Value` kedua kali
24. Verifikasi Old Value klik 2 (turun): entri `—` di awal
25. Klik header `Old Value` ketiga kali
26. Verifikasi indikator sort `Old Value` netral
27. Klik header `New Value` satu kali
28. Verifikasi New Value klik 1 (naik): nilai angka lebih dulu (40, 60, 84), lalu nilai teks, dan entri bernilai `—` di akhir
29. Klik header `New Value` kedua kali
30. Verifikasi New Value klik 2 (turun): entri `—` di awal
31. Klik header `New Value` ketiga kali
32. Verifikasi indikator sort `New Value` netral

## Notes

1. Pengecualian nama seed literal: asersi TC bergantung pada kode, tanggal, dan pelaku Example Data Changelog; data dipakai apa adanya dan hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Temuan untuk QA: TC mengasersi jumlah dan isi absolut dari seed Changelog (19 entri, lima entri System, tujuh entri Budi S, dan sejenisnya), sedangkan Changelog adalah audit trail permanen yang bertambah dari spec lain (S-12, bagian 8b butir 10). Spec mengikuti TC dan bergantung pada fixture BE yang menjamin keadaan 19 entri; usulan: TC ditulis relatif terhadap baseline.
3. Modal Changelog dibuka sekali per spec; state Search, Filter, Sort, dan ukuran halaman modal direset oleh TC (langkah penghubung) dan hilang saat modal ditutup (S-09).
4. TC-500 (sort tiga tahap kolom teks Action, Class Code, Field, dan Modified By) ada di spec 157. Klik 3 pada tiap kolom mengembalikan sort ke netral sehingga kolom berikutnya mulai dari default (S-09).
5. Urutan campuran Old Value dan New Value (TC-501) diasersi pada ukuran halaman bawaan 10 dengan nilai yang tampil pada halaman pertama; TC tidak menyebut halaman (Temuan untuk QA: asersi urutan lintas halaman perlu langkah pindah halaman, S-14).
6. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 12.
7. Urutan TC diubah dari urutan nomor: screening TC-502 dan TC-503 ditulis lebih dulu, lalu sort TC-499 dan TC-501 (S-10).
