---
id: TC-AC-PF-E2E-137-setup-column-tab-default-active-screening-ceklis-geser
title: Setup Column Tab Default Active Screening, Ceklis, dan Geser Urutan
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-335
  - TC-AC-PF-336
  - TC-AC-PF-337
  - TC-AC-PF-338
coverage:
  web: automated
---

# Setup Column Tab Default Active Screening, Ceklis, dan Geser Urutan

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan A (Pre-setup #21), default aktif `Starter`, `Growth`, `Professional`, `Enterprise`, `SIEM`.
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- State sementara: spec menyimpan konfigurasi kolom lewat `[Save]` (disimpan di cache browser tab Default Active); preferensi dihapus di hook `after` (kemampuan menghapus preferensi kolom di browser disediakan tim FE, bagian 4).
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

### TC-AC-PF-335 Screening Overlay Column Visibility

1. Klik header kolom Actions (`⋯`).
2. Verifikasi Overlay Column Visibility muncul.
3. Hover header kolom Actions.
4. Verifikasi tooltip header kolom Actions adalah `Column Visibility`.
5. Verifikasi overlay memuat daftar kolom berurutan `Plan Name | Product | Pricing Type | Version | Clients | Last Modified`.
6. Verifikasi tiap kolom pada daftar memiliki checkbox tercentang (Hideable, enabled).
7. Verifikasi tiap kolom pada daftar memiliki drag handle.
8. Verifikasi item `Setup Column...` ada di bagian bawah overlay.

### TC-AC-PF-336 Screening Popup Setup Column

9. Klik `Setup Column...`.
10. Verifikasi Title Popup adalah `Setup Column`.
11. Verifikasi deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.".
12. Verifikasi icon close `(X)` di kanan atas.
13. Verifikasi daftar kolom `Plan Name | Product | Pricing Type | Version | Clients | Last Modified`.
14. Verifikasi tiap kolom memiliki checkbox tercentang.
15. Verifikasi tiap kolom memiliki drag handle.
16. Verifikasi tiap kolom memiliki icon Pin.
17. Verifikasi Live Preview menampilkan urutan header kolom yang sama dengan tabel.
18. Verifikasi Live Preview menampilkan data sel yang sama dengan tabel.
19. Verifikasi footer memuat tombol `[Reset to Default]` (text, primary) dan `[Save]` (filled, success).
20. Verifikasi tidak ada tombol `[Cancel]`.

### TC-AC-PF-337 Ceklis dan unceklis kolom

21. Uncheck kolom `Clients`.
22. Verifikasi Live Preview tidak lagi menampilkan kolom `Clients`.
23. Verifikasi tabel di belakang modal tidak lagi menampilkan kolom `Clients`.
24. Klik `[Save]`.
25. Verifikasi modal tertutup.
26. Verifikasi tabel tanpa kolom `Clients`.
27. Tekan F5.
28. Verifikasi kolom `Clients` tetap tidak tampil (tersimpan di cache browser).

### TC-AC-PF-338 Geser urutan kolom

29. Buka Popup Setup Column.
30. Drag kolom `Last Modified` ke posisi paling awal.
31. Verifikasi Live Preview menampilkan `Last Modified` di posisi pertama sebelum Save.
32. Klik `[Save]`.
33. Tekan F5.
34. Verifikasi urutan header tabel dimulai dari `Last Modified`.

## Notes

- Langkah 1 sampai 8 dan 9 sampai 20 adalah screening dan ditempatkan di awal (bagian 3 prinsip 1).
- Jumlah langkah 34: di bawah ambang sekitar 35.
- Temuan untuk QA: TC-AC-PF-338 tidak menyebut kondisi kolom awal; langkah 29 sampai 34 dijalankan sesudah kolom `Clients` disembunyikan oleh TC-AC-PF-337 (tidak memengaruhi asersi urutan).
