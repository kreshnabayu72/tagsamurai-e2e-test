---
id: TC-AC-PF-E2E-186-setup-column-modal-changelog-default-geser-pin-reset
title: Setup Column modal Changelog Default geser urutan, Pin dan Unpin, dan Reset to Default
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-478
  - TC-AC-PF-479
  - TC-AC-PF-480
coverage:
  web: automated
---

# Setup Column modal Changelog Default geser urutan, Pin dan Unpin, dan Reset to Default

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log D, Changelog Default Principal lima entri, terbaru dahulu: `12 Aug 26, 09:00` Create `Enterprise` (Plan Name, Old `—`, New `Enterprise`, Jane S); `01 Aug 26, 08:00` Archive `Growth Plus (old)` (Status, Old `Active`, New `Archived`, Jane S); `20 Jul 26, 10:00` Push Update `PT Wahana Nusantara` (Plan Version, Old `v1`, New `v5`, Sarah T); `10 Jul 26, 12:00` Delete `Pilot Default` (Plan Name, Old `Pilot Default`, New `—`, John D); `05 Jun 26, 15:40` Edit `Growth` (Group count, Old `3`, New `5`, Jane S). Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Principal tepat sama dengan Dataset Log D di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; pengatur lebar viewport browser; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: spec ini menyimpan preferensi kolom modal Changelog Default (urutan kolom, Pin) di browser (localStorage, cache sendiri per modal) dan mengubah lebar viewport. Hook `after` menghapus preferensi kolom itu di browser, bukan lewat `[Reset to Default]` (kemampuan disediakan tim FE); lebar viewport dipulihkan di langkah terakhir.

## Test Steps

### Reset to Default (TC-AC-PF-480)

1. Klik ikon Changelog pada toolbar tab Default
2. Buka Popup Setup Column dari header kolom Actions (`⋯`)
3. Uncheck kolom `Old Value`
4. Drag kolom `Modified By` ke posisi awal
5. Klik `[Save]`
6. Buka Popup Setup Column lagi
7. Klik `[Reset to Default]`
8. Verifikasi Live Preview menampilkan kolom dengan urutan default `Date`, `Action`, `Plan Name`, `Field`, `Old Value`, `New Value`, `Modified By`
9. Klik `[Save]`
10. Verifikasi tabel kembali ke urutan dan visibilitas default
11. Tekan F5
12. Klik ikon Changelog pada toolbar tab Default
13. Verifikasi tabel tetap dalam urutan dan visibilitas default

### Pin dan Unpin kolom (TC-AC-PF-479)

14. Perkecil lebar viewport sehingga tabel scroll horizontal
15. Buka Popup Setup Column
16. Klik icon Pin pada kolom `Date`
17. Klik `[Save]`
18. Scroll tabel ke kanan
19. Verifikasi kolom `Date` tetap terlihat di sisi kiri saat tabel di-scroll horizontal (freeze)
20. Tekan F5
21. Klik ikon Changelog pada toolbar tab Default
22. Scroll tabel ke kanan
23. Verifikasi kolom `Date` masih beku setelah F5
24. Buka Popup Setup Column
25. Klik icon Pin `Date` lagi (Unpin)
26. Klik `[Save]`
27. Scroll tabel ke kanan
28. Verifikasi kolom `Date` ikut bergeser saat tabel di-scroll
29. Pulihkan lebar viewport ke ukuran semula

### Geser urutan kolom (TC-AC-PF-478)

30. Buka Popup Setup Column
31. Drag kolom `Modified By` ke posisi paling awal
32. Verifikasi Live Preview menampilkan `Modified By` di posisi pertama sebelum Save
33. Klik `[Save]`
34. Tekan F5
35. Klik ikon Changelog pada toolbar tab Default
36. Verifikasi urutan header tabel dimulai dari `Modified By`

## Notes

- Urutan blok: TC-AC-PF-480 lebih dahulu, lalu TC-AC-PF-479, lalu TC-AC-PF-478, supaya tiap blok dimulai dari preferensi default (blok pertama berakhir di default dan blok Pin berakhir tanpa Pin); blok TC-AC-PF-478 menyimpan urutan yang diubah dan menjadi blok terakhir (S-09, S-10).
- Langkah 12, 21, dan 35 membuka kembali modal karena F5 memuat ulang halaman.
- Spec ini melebihi sekitar 35 langkah (36 langkah). Alasan: ketiga blok TC berdiri sendiri pada satu kelas fungsional dan satu dataset; kegagalan satu blok tidak membuat blok lain kehilangan makna; ekspansi berasal dari Verifikasi per klausa (S-01) dan tiga kali F5 yang menuntut pembukaan ulang modal (S-14).
- Temuan untuk QA:
  - TC-AC-PF-479 tidak menyatakan lebar viewport yang membuat tabel scroll horizontal; spec menulis "perkecil lebar viewport" mengikuti TC dan viewport dipulihkan di akhir blok.
  - TC menetapkan lima baris sebagai seluruh isi Changelog Default. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
  - `suite.md` belum mendaftarkan pemulihan preferensi kolom di hook `after` (bagian 4 konvensi).
