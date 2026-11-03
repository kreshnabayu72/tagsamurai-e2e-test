---
id: TC-AC-PF-E2E-138-setup-column-tab-default-active-pin-reset-to-default-tutup
title: Setup Column Tab Default Active Pin, Reset to Default, dan Tutup Popup
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-339
  - TC-AC-PF-340
  - TC-AC-PF-341
coverage:
  web: automated
---

# Setup Column Tab Default Active Pin, Reset to Default, dan Tutup Popup

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan A (Pre-setup #21), default aktif `Starter`, `Growth`, `Professional`, `Enterprise`, `SIEM`.
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup. Mengubah lebar viewport browser (diperkecil lalu dipulihkan).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- State sementara: konfigurasi kolom yang disimpan (pin, visibilitas, urutan) tersimpan di cache browser tab Default Active; preferensi dihapus di hook `after` (kemampuan disediakan tim FE, bagian 4).
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

### TC-AC-PF-339 Pin dan Unpin

1. Perkecil lebar viewport sehingga tabel scroll horizontal.
2. Buka Popup Setup Column dan klik icon Pin pada kolom `Plan Name`.
3. Klik `[Save]`, lalu scroll tabel ke kanan.
4. Verifikasi kolom `Plan Name` tetap terlihat di sisi kiri saat tabel di-scroll horizontal (freeze).
5. Tekan F5.
6. Verifikasi kolom `Plan Name` masih beku setelah F5.
7. Buka Popup Setup Column, klik icon Pin `Plan Name` lagi (Unpin), klik `[Save]`.
8. Scroll tabel ke kanan.
9. Verifikasi kolom `Plan Name` ikut bergeser saat scroll.

### TC-AC-PF-340 Reset to Default

10. Buka Popup Setup Column, uncheck `Clients`, drag `Last Modified` ke posisi awal, klik `[Save]`.
11. Buka Popup Setup Column lagi, klik `[Reset to Default]`.
12. Verifikasi Live Preview menampilkan kolom dengan urutan default `Plan Name | Product | Pricing Type | Version | Clients | Last Modified`.
13. Klik `[Save]`.
14. Verifikasi tabel kembali ke default.
15. Tekan F5.
16. Verifikasi tabel default bertahan setelah F5.

### TC-AC-PF-341 Tutup popup tanpa Save

17. Buka Popup Setup Column, uncheck `Clients`.
18. Klik icon close `(X)`.
19. Verifikasi modal tertutup.
20. Verifikasi tabel tetap menampilkan kolom `Clients`.
21. Buka Popup Setup Column lagi, uncheck `Clients`, tekan Esc.
22. Verifikasi modal tertutup.
23. Verifikasi tabel tetap menampilkan kolom `Clients`.
24. Pulihkan lebar viewport ke ukuran semula.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 1 dan 24 mengubah serta memulihkan lebar viewport; langkah 8 menggulir ulang tabel sebelum mengamati hasil Unpin.
- Jumlah langkah 24: di bawah ambang sekitar 35.
