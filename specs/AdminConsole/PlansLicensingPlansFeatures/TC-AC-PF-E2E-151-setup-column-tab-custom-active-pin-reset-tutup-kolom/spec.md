---
id: TC-AC-PF-E2E-151-setup-column-tab-custom-active-pin-reset-tutup-kolom
title: Setup Column Tab Custom Active Pin, Reset to Default, Tutup Popup, dan Kolom Created By
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-388
  - TC-AC-PF-389
  - TC-AC-PF-390
  - TC-AC-PF-393
  - TC-AC-PF-394
coverage:
  web: automated
---

# Setup Column Tab Custom Active Pin, Reset to Default, Tutup Popup, dan Kolom Created By

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active (langkah 1 pindah ke tab Custom).
- Data Pre-setup: Dataset Plan C (Pre-setup #23): custom Principal aktif `alpha Tier` (Created By Andi Wijaya), `Beta Pro` (Created By Rina Kusuma), `Growth Tier` (Andi Wijaya), `Zeta Max` (Budi Aditya); semuanya Paid. Kolom curated `Created By` tersembunyi secara default.
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup. Mengubah lebar viewport browser (diperkecil lalu dipulihkan).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- State sementara: konfigurasi kolom yang disimpan (pin, visibilitas, urutan, kolom Created By) tersimpan di cache browser tab Custom Active; preferensi dihapus di hook `after` (kemampuan disediakan tim FE, bagian 4).
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

1. Klik tab Custom, lalu sub-tab Active.

### TC-AC-PF-388 Pin dan Unpin

2. Perkecil lebar viewport sehingga tabel scroll horizontal.
3. Buka Popup Setup Column dan klik icon Pin pada kolom `Plan Name`.
4. Klik `[Save]`, lalu scroll tabel ke kanan.
5. Verifikasi kolom `Plan Name` tetap terlihat di sisi kiri saat tabel di-scroll horizontal (freeze).
6. Tekan F5.
7. Verifikasi kolom `Plan Name` masih beku setelah F5.
8. Buka Popup Setup Column, klik icon Pin `Plan Name` lagi (Unpin), klik `[Save]`.
9. Scroll tabel ke kanan.
10. Verifikasi kolom `Plan Name` ikut bergeser saat scroll.
11. Pulihkan lebar viewport ke ukuran semula.

### TC-AC-PF-389 Reset to Default

12. Buka Popup Setup Column, uncheck `Clients`, drag `Last Modified` ke posisi awal, klik `[Save]`.
13. Buka Popup Setup Column lagi, klik `[Reset to Default]`.
14. Verifikasi Live Preview menampilkan kolom dengan urutan default `Plan Name | Product | Pricing Type | Version | Clients | Last Modified`.
15. Klik `[Save]`.
16. Verifikasi tabel kembali ke default.
17. Tekan F5.
18. Verifikasi tabel default bertahan setelah F5.

### TC-AC-PF-390 Tutup popup tanpa Save

19. Buka Popup Setup Column, uncheck `Clients`.
20. Klik icon close `(X)`.
21. Verifikasi modal tertutup.
22. Verifikasi tabel tetap menampilkan kolom `Clients`.
23. Buka Popup Setup Column lagi, uncheck `Clients`, tekan Esc.
24. Verifikasi modal tertutup.
25. Verifikasi tabel tetap menampilkan kolom `Clients`.

### TC-AC-PF-393 Kolom curated Created By

26. Buka Popup Setup Column.
27. Verifikasi checkbox `Created By` tidak tercentang (Curated) dan enabled pada kondisi awal.
28. Centang `Created By`, klik `[Save]`.
29. Verifikasi kolom `Created By` tampil pada tabel.
30. Verifikasi isi kolom `Created By` berformat `Andi W`.
31. Tekan F5.
32. Verifikasi kolom `Created By` tetap tampil setelah F5.

### TC-AC-PF-394 Tooltip Created By

33. Hover sel `Rina K`.
34. Verifikasi tooltip menampilkan `Rina Kusuma`.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 1 membuka tab Custom; langkah 2 dan 11 mengubah serta memulihkan lebar viewport; langkah 9 menggulir ulang tabel sebelum mengamati hasil Unpin.
- TC-AC-PF-393 dan TC-AC-PF-394 diletakkan di akhir karena menyimpan kolom `Created By` yang mengubah susunan tabel (bagian 3 prinsip 1).
- Jumlah langkah 34: di bawah ambang sekitar 35.
