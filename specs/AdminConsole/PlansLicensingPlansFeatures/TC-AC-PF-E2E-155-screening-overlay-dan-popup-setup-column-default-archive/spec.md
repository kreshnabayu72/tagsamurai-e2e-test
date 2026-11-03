---
id: TC-AC-PF-E2E-155-screening-overlay-dan-popup-setup-column-default-archive
title: Screening Overlay Column Visibility dan Popup Setup Column Default Archive, Custom Archive, dan Modal Changelog Custom
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-630
  - TC-AC-PF-631
coverage:
  web: automated
---

# Screening Overlay Column Visibility dan Popup Setup Column Default Archive, Custom Archive, dan Modal Changelog Custom

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan A (Pre-setup #21; Default Archive `Growth Plus (old)`, custom archived `Enterprise Reseller`), Dataset Plan R (Pre-setup #30; Default Archive `Plan Arsip Lama`, `Plan Arsip Tengah`, `Plan Arsip Baru`), dan Dataset Log C (Pre-setup #41; Changelog Custom Principal 6 entri).
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Tabel "Surface yang diuji" (langkah berulang untuk tiap baris):

| Kode | Surface | Cara membuka | Daftar kolom |
|---|---|---|---|
| DR | Default > Archive | klik tab Default, lalu sub-tab Archive | `Plan Name | Product | Pricing Type | Version | Clients | Last Modified` |
| CR | Custom > Archive | klik tab Custom, lalu sub-tab Archive | `Plan Name | Product | Pricing Type | Version | Clients | Last Modified` |
| MC | Modal Changelog Custom | klik tab Custom, lalu klik ikon Changelog | `Date | Action | Plan Name | Field | Old Value | New Value | Modified By` |

- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12).
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup dan tidak menyimpan konfigurasi kolom.
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

### TC-AC-PF-630 Screening Overlay Column Visibility

Untuk setiap baris tabel "Surface yang diuji" (langkah 1 sampai 8):

1. Buka surface sesuai kolom "Cara membuka".
2. Klik header kolom Actions (`⋯`).
3. Hover header kolom Actions.
4. Verifikasi tooltip header kolom Actions adalah `Column Visibility`.
5. Verifikasi overlay memuat daftar kolom sesuai kolom "Daftar kolom" dengan checkbox tercentang.
6. Verifikasi tiap kolom pada daftar memiliki drag handle.
7. Verifikasi item `Setup Column...` ada di bawah daftar kolom.
8. Tekan Esc untuk menutup overlay.

Tambahan Custom Archive:

9. Buka tab Custom, lalu sub-tab Archive, lalu klik header kolom Actions (`⋯`).
10. Verifikasi baris `Created By` (Curated) tidak tercentang dan enabled.
11. Verifikasi kolom Created By tidak tampil pada tabel.
12. Tekan Esc untuk menutup overlay.

### TC-AC-PF-631 Screening Popup Setup Column

Untuk setiap baris tabel "Surface yang diuji" (langkah 13 sampai 26):

13. Buka surface sesuai kolom "Cara membuka".
14. Klik header kolom Actions (`⋯`), lalu klik `Setup Column...`.
15. Verifikasi Title Popup adalah `Setup Column`.
16. Verifikasi deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.".
17. Verifikasi icon close `(X)` tampil.
18. Verifikasi daftar kolom sesuai kolom "Daftar kolom".
19. Verifikasi tiap kolom memiliki checkbox.
20. Verifikasi tiap kolom memiliki drag handle.
21. Verifikasi tiap kolom memiliki icon Pin.
22. Verifikasi Live Preview menampilkan urutan header kolom yang sama dengan tabel.
23. Verifikasi Live Preview menampilkan data sel yang sama dengan tabel.
24. Verifikasi footer memuat tombol `[Reset to Default]` (text, primary) dan `[Save]` (filled, success).
25. Verifikasi tidak ada tombol `[Cancel]`.
26. Klik icon close `(X)`.

Tambahan Custom Archive:

27. Buka tab Custom, lalu sub-tab Archive, lalu buka Popup Setup Column (header kolom Actions `⋯`, lalu `Setup Column...`).
28. Verifikasi baris `Created By` (Curated) tidak tercentang dan enabled.
29. Verifikasi Live Preview tidak menampilkan kolom Created By.
30. Klik icon close `(X)`.

## Notes

- Langkah berulang: "Untuk setiap baris tabel" mengulang langkah 1 sampai 8 dan 13 sampai 26 untuk baris DR, CR, dan MC; parameter tiap iterasi ada di tabel "Surface yang diuji", tanpa langkah bersyarat, dan tiap `Verifikasi` tetap satu per klausa. Langkah 9 sampai 12 dan 27 sampai 30 ditulis terpisah karena asersi baris `Created By` hanya berlaku untuk Custom Archive (TC-AC-PF-630 butir b, TC-AC-PF-631 butir b).
- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 8, 12, 26, dan 30 menutup overlay atau popup tanpa Save.
- Alasan di atas sekitar 35 langkah: TC sumber masing-masing mencakup tiga surface dalam satu TC dengan langkah identik dan parameter berbeda; hasil ekspansi iterasi sekitar 70 langkah, dan semua blok adalah screening Setup Column dengan dataset yang sama. Estimasi langkah semula lebih rendah karena tiap TC menghitung satu surface.
- Temuan untuk QA: TC-AC-PF-631 butir c menulis "struktur sama" untuk modal Changelog Custom tanpa merinci footer dan Live Preview; spec mengasersi struktur yang sama dengan dua surface lain.
