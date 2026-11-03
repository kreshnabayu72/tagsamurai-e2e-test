---
id: TC-AC-PF-E2E-183-filter-modal-changelog-default-opsi-and-tanpa-hasil
title: Filter modal Changelog Default opsi dropdown, kombinasi Filter AND Search, tanpa hasil, dan chip +N more Modified By
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-468
  - TC-AC-PF-469
  - TC-AC-PF-470
  - TC-AC-PF-784
  - TC-AC-PF-785
coverage:
  web: automated
---

# Filter modal Changelog Default opsi dropdown, kombinasi Filter AND Search, tanpa hasil, dan chip +N more Modified By

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup untuk blok TC-AC-PF-468 sampai TC-AC-PF-470: Dataset Log D, Changelog Default Principal lima entri, terbaru dahulu: `12 Aug 26, 09:00` Create `Enterprise` (Plan Name, Old `—`, New `Enterprise`, Jane S); `01 Aug 26, 08:00` Archive `Growth Plus (old)` (Status, Old `Active`, New `Archived`, Jane S); `20 Jul 26, 10:00` Push Update `PT Wahana Nusantara` (Plan Version, Old `v1`, New `v5`, Sarah T); `10 Jul 26, 12:00` Delete `Pilot Default` (Plan Name, Old `Pilot Default`, New `—`, John D); `05 Jun 26, 15:40` Edit `Growth` (Group count, Old `3`, New `5`, Jane S).
- Data Pre-setup untuk blok TC-AC-PF-784 dan TC-AC-PF-785: Dataset Log MB, Changelog Default Principal delapan entri Edit `Growth` Group count, masing-masing oleh satu user berbeda: `01 Jul 26, 10:00` Jane Smith (1 ke 3); `02 Jul 26, 10:00` John Doe (3 ke 25); `03 Jul 26, 10:00` Sarah Tan (25 ke Unlimited); `04 Jul 26, 10:00` Andi Wijaya (Unlimited ke 1); `05 Jul 26, 10:00` Rina Kusuma (1 ke 3); `06 Jul 26, 10:00` Budi Aditya (3 ke 25); `07 Jul 26, 10:00` Maya Putri (25 ke Unlimited); `08 Jul 26, 10:00` Eka Pratama (Unlimited ke 1); semua pengubah berhak Update. Viewport browser berlebar 1280 px untuk dua blok itu. Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Principal tepat sama dengan Dataset Log D di hook `before` dan memulihkannya ke baseline di hook `after`; penggantian ke Dataset Log MB dilakukan fixture yang sama sebagai langkah penghubung antar blok; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; pengatur lebar viewport browser; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: lebar viewport diubah di blok TC-AC-PF-784 dan dipulihkan di langkah terakhir spec ini.

## Test Steps

### Opsi dropdown Filter (TC-AC-PF-468)

1. Klik ikon Changelog pada toolbar tab Default
2. Buka Filter Panel
3. Buka dropdown Action
4. Verifikasi opsi Action: `Archive`, `Create`, `Delete`, `Edit`, `Push Update`
5. Buka dropdown Plan Name
6. Verifikasi opsi Plan Name: `Enterprise`, `Growth`, `Growth Plus (old)`, `Pilot Default`, `PT Wahana Nusantara`
7. Buka dropdown Field
8. Verifikasi opsi Field: `Group count`, `Plan Name`, `Plan Version`, `Status`
9. Buka dropdown Modified By
10. Verifikasi opsi Modified By: `Jane Smith`, `John Doe`, `Sarah Tan`

### Kombinasi Filter AND Search (TC-AC-PF-469)

11. Ketik Search `growth`, tekan Enter
12. Buka Filter Panel, pilih Modified By `Jane Smith` dan Action `Edit`, klik `[Apply]`
13. Verifikasi tabel menampilkan baris `Edit Growth` saja
14. Verifikasi Search tetap `growth`

### Filter tanpa hasil (TC-AC-PF-470)

15. Kosongkan isi kotak search, tekan Enter
16. Buka Filter Panel, klik `[Clear Field]`, pilih Action `Create` dan Modified By `Sarah Tan`, klik `[Apply]`
17. Verifikasi Illustration tampil
18. Verifikasi Title "No results found"
19. Verifikasi Description "Try adjusting your search or filter."

### Chip +N more pada delapan opsi Modified By (TC-AC-PF-784)

20. Ganti Dataset Log D dengan Dataset Log MB lewat fixture BE, lalu tekan F5
21. Atur lebar viewport browser menjadi 1280 px
22. Klik ikon Changelog pada toolbar tab Default
23. Klik ikon Filter, lalu buka dropdown Modified By
24. Centang kedelapan opsi (`Jane Smith`, `John Doe`, `Sarah Tan`, `Andi Wijaya`, `Rina Kusuma`, `Budi Aditya`, `Maya Putri`, `Eka Pratama`), lalu tutup dropdown
25. Verifikasi field Modified By menampilkan chip sebanyak yang muat pada lebar field dan satu chip `+N more` dengan N minimal 1 untuk sisanya
26. Verifikasi jumlah chip yang tampil ditambah N sama dengan 8
27. Verifikasi field Modified By tidak melebar keluar Filter Panel
28. Verifikasi isi field Modified By tidak digulir horizontal

### Chip +N more hilang saat opsi dikurangi (TC-AC-PF-785)

29. Buka dropdown Modified By lagi, hilangkan centang enam opsi hingga hanya `Jane Smith` dan `John Doe` terpilih, lalu tutup dropdown
30. Verifikasi field Modified By menampilkan dua chip `Jane Smith` dan `John Doe`
31. Verifikasi tidak ada chip `+N more`
32. Pulihkan lebar viewport browser ke ukuran semula

## Notes

- Langkah penghubung (S-03): langkah 15 mengosongkan Search sebelum blok TC-AC-PF-470; langkah 20 menukar dataset dan memuat ulang halaman; langkah 32 memulihkan viewport.
- Urutan blok: TC-AC-PF-784 dan TC-AC-PF-785 berdataset Log MB sehingga diletakkan sesudah blok berdataset Log D (S-10); TC-AC-PF-785 melanjutkan state dropdown dari TC-AC-PF-784 sesuai langkah 3 TC-nya.
- Verifikasi langkah 4, 6, 8, dan 10 membaca opsi dari dropdown yang dibuka pada langkah sebelumnya (opsi berasal dari data log saat ini).
- Temuan untuk QA:
  - TC menetapkan lima dan delapan entri sebagai seluruh isi Changelog Default. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
  - Opsi dropdown Modified By pada TC-AC-PF-784 mencantumkan `Andi Wijaya`, yaitu nama tampil akun aktor #1.
