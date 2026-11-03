---
id: TC-AC-PF-E2E-150-setup-column-tab-custom-active-screening-ceklis-geser
title: Setup Column Tab Custom Active Screening, Ceklis, dan Geser Urutan
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-384
  - TC-AC-PF-385
  - TC-AC-PF-386
  - TC-AC-PF-387
coverage:
  web: automated
---

# Setup Column Tab Custom Active Screening, Ceklis, dan Geser Urutan

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active (langkah 1 pindah ke tab Custom).
- Data Pre-setup: Dataset Plan C (Pre-setup #23): custom Principal aktif `alpha Tier`, `Beta Pro`, `Growth Tier`, `Zeta Max`; semuanya Paid. Kolom curated `Created By` tersembunyi secara default.
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- State sementara: spec menyimpan konfigurasi kolom lewat `[Save]` (cache browser tab Custom Active); preferensi dihapus di hook `after` (kemampuan menghapus preferensi kolom di browser disediakan tim FE, bagian 4).
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

1. Klik tab Custom, lalu sub-tab Active.

### TC-AC-PF-384 Screening Overlay Column Visibility

2. Klik header kolom Actions (`⋯`).
3. Verifikasi Overlay Column Visibility muncul.
4. Hover header kolom Actions.
5. Verifikasi tooltip header kolom Actions adalah `Column Visibility`.
6. Verifikasi overlay memuat daftar kolom berurutan `Plan Name | Product | Pricing Type | Version | Clients | Last Modified`.
7. Verifikasi tiap kolom pada daftar memiliki checkbox tercentang (Hideable, enabled).
8. Verifikasi tiap kolom pada daftar memiliki drag handle.
9. Verifikasi baris `Created By` (Curated) tidak tercentang dan enabled.
10. Verifikasi kolom Created By tidak tampil pada tabel.
11. Verifikasi item `Setup Column...` ada di bagian bawah overlay.

### TC-AC-PF-385 Screening Popup Setup Column

12. Klik `Setup Column...`.
13. Verifikasi Title Popup adalah `Setup Column`.
14. Verifikasi deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.".
15. Verifikasi icon close `(X)` di kanan atas.
16. Verifikasi daftar kolom `Plan Name | Product | Pricing Type | Version | Clients | Last Modified`.
17. Verifikasi tiap kolom memiliki checkbox tercentang.
18. Verifikasi tiap kolom memiliki drag handle.
19. Verifikasi tiap kolom memiliki icon Pin.
20. Verifikasi baris `Created By` (Curated) tidak tercentang dan enabled.
21. Verifikasi Live Preview tidak menampilkan kolom Created By.
22. Verifikasi Live Preview menampilkan urutan header kolom yang sama dengan tabel.
23. Verifikasi Live Preview menampilkan data sel yang sama dengan tabel.
24. Verifikasi footer memuat tombol `[Reset to Default]` (text, primary) dan `[Save]` (filled, success).
25. Verifikasi tidak ada tombol `[Cancel]`.

### TC-AC-PF-386 Ceklis dan unceklis kolom

26. Uncheck kolom `Clients`.
27. Verifikasi Live Preview tidak lagi menampilkan kolom `Clients`.
28. Verifikasi tabel di belakang modal tidak lagi menampilkan kolom `Clients`.
29. Klik `[Save]`.
30. Verifikasi modal tertutup.
31. Verifikasi tabel tanpa kolom `Clients`.
32. Tekan F5.
33. Verifikasi kolom `Clients` tetap tidak tampil (tersimpan di cache browser).

### TC-AC-PF-387 Geser urutan kolom

34. Buka Popup Setup Column.
35. Drag kolom `Last Modified` ke posisi paling awal.
36. Verifikasi Live Preview menampilkan `Last Modified` di posisi pertama sebelum Save.
37. Klik `[Save]`.
38. Tekan F5.
39. Verifikasi urutan header tabel dimulai dari `Last Modified`.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 1 membuka tab Custom.
- Screening (langkah 2 sampai 25) ditempatkan di awal (bagian 3 prinsip 1).
- Alasan di atas sekitar 35 langkah (39): seluruh blok memakai satu surface (Popup Setup Column tab Custom Active), satu dataset, dan satu cache kolom; tiap butir Expected screening harus dipecah per klausa (S-01: checkbox, drag handle, dan Pin tidak digabung). Estimasi langkah semula lebih rendah karena pemecahan itu.
- Temuan untuk QA: TC-AC-PF-387 tidak menyebut kondisi kolom awal; langkah 34 sampai 39 dijalankan sesudah kolom `Clients` disembunyikan oleh TC-AC-PF-386 (tidak memengaruhi asersi urutan).
