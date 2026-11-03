---
id: TC-AC-PF-E2E-198-setup-column-modal-changelog-global-settings-geser-pin
title: Setup Column modal Changelog Global Settings Reset to Default, Pin dan Unpin, dan geser urutan kolom
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-510
  - TC-AC-PF-511
  - TC-AC-PF-512
coverage:
  web: automated
---

# Setup Column modal Changelog Global Settings Reset to Default, Pin dan Unpin, dan geser urutan kolom

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log G, Changelog Global Settings lima entri Edit (`Max depreciation methods (Multi Depreciation tier)` dan `Max custom fields per asset name`, 02 Jun 26 sampai 30 Jun 26, John D dan Sarah T). Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Global Settings Principal tepat sama dengan Dataset Log G di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; pengatur lebar viewport browser; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: spec ini menyimpan preferensi kolom modal Changelog Global Settings (urutan kolom, Pin) di browser (localStorage, cache sendiri per modal) dan mengubah lebar viewport. Hook `after` menghapus preferensi kolom itu di browser, bukan lewat `[Reset to Default]` (kemampuan disediakan tim FE); lebar viewport dipulihkan di langkah terakhir blok Pin.

## Test Steps

### Reset to Default (TC-AC-PF-512)

1. Klik tab Global Settings
2. Klik ikon Changelog di pojok kanan atas Card
3. Buka Popup Setup Column dari header kolom Actions (`⋯`)
4. Uncheck kolom `Old Value`
5. Drag kolom `Modified By` ke posisi awal
6. Klik `[Save]`
7. Buka Popup Setup Column lagi
8. Klik `[Reset to Default]`
9. Verifikasi Live Preview menampilkan kolom dengan urutan default `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
10. Klik `[Save]`
11. Verifikasi tabel kembali ke urutan dan visibilitas default
12. Tekan F5
13. Klik tab Global Settings
14. Klik ikon Changelog di pojok kanan atas Card
15. Verifikasi tabel tetap dalam urutan dan visibilitas default

### Pin dan Unpin kolom (TC-AC-PF-511)

16. Perkecil lebar viewport sehingga tabel scroll horizontal
17. Buka Popup Setup Column
18. Klik icon Pin pada kolom `Date`
19. Klik `[Save]`
20. Scroll tabel ke kanan
21. Verifikasi kolom `Date` tetap terlihat di sisi kiri saat tabel di-scroll horizontal (freeze)
22. Tekan F5
23. Klik tab Global Settings
24. Klik ikon Changelog di pojok kanan atas Card
25. Scroll tabel ke kanan
26. Verifikasi kolom `Date` masih beku setelah F5
27. Buka Popup Setup Column
28. Klik icon Pin `Date` lagi (Unpin)
29. Klik `[Save]`
30. Scroll tabel ke kanan
31. Verifikasi kolom `Date` ikut bergeser saat tabel di-scroll
32. Pulihkan lebar viewport ke ukuran semula

### Geser urutan kolom (TC-AC-PF-510)

33. Buka Popup Setup Column
34. Drag kolom `Modified By` ke posisi paling awal
35. Verifikasi Live Preview menampilkan `Modified By` di posisi pertama sebelum Save
36. Klik `[Save]`
37. Tekan F5
38. Klik tab Global Settings
39. Klik ikon Changelog di pojok kanan atas Card
40. Verifikasi urutan header tabel dimulai dari `Modified By`

## Notes

- Urutan blok: TC-AC-PF-512 lebih dahulu, lalu TC-AC-PF-511, lalu TC-AC-PF-510, supaya tiap blok dimulai dari preferensi default; blok TC-AC-PF-510 menyimpan urutan yang diubah dan menjadi blok terakhir (S-09, S-10).
- Langkah 13, 14, 23, 24, 38, dan 39 membuka kembali modal karena F5 memuat ulang halaman.
- Spec ini melebihi sekitar 35 langkah (40 langkah). Alasan: ketiga blok TC berdiri sendiri pada satu kelas fungsional dan satu dataset; kegagalan satu blok tidak membuat blok lain kehilangan makna; ekspansi berasal dari Verifikasi per klausa (S-01) dan tiga kali F5 yang menuntut pembukaan ulang modal (S-14).- Temuan untuk QA:
  - TC-AC-PF-511 tidak menyatakan lebar viewport yang membuat tabel scroll horizontal; spec menulis "perkecil lebar viewport" mengikuti TC dan viewport dipulihkan di akhir blok.
  - TC menetapkan lima entri sebagai seluruh isi Changelog Global Settings. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
  - `suite.md` belum mendaftarkan pemulihan preferensi kolom di hook `after` (bagian 4 konvensi).
