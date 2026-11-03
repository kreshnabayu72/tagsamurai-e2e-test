---
id: TC-AC-PF-E2E-160-screening-tab-assigned-clients-dan-format-sel
title: "Screening Tab Assigned Clients: toolbar, kolom, urutan default, footer, dan format sel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-410
  - TC-AC-PF-453
coverage:
  web: automated
---

# Screening Tab Assigned Clients: toolbar, kolom, urutan default, footer, dan format sel

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip mengikuti pernyataan di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE, sesuai `suite.md`): sesi API aktor, klien HTTP, dan fixture backend yang memulihkan Dataset Plan D ke keadaan awal secara idempoten. Fixture `fixtures/plans-licensing-plans-features.json` belum ada; nilai data di spec ini ditulis literal sesuai Pre-setup.
- Data Pre-setup: Dataset Plan D, default plan `Growth` v5 dengan 9 client: PT Sejahtera Abadi Active v5 17 Jun 26 John Doe; PT Wahana Nusantara Active v1 05 Jun 26 John Doe; PT Karya Abadi Active v1 03 Jun 26 Jane Smith; PT Cahaya Mandiri Grace v5 20 Jun 26 Jane Smith; PT Bumi Sentosa Active v1 11 Jun 26 Jane Smith; PT Timur Jaya Active v1 09 Jun 26 John Doe; PT Zona Nol Active v5 25 Jun 26 John Doe; PT Hak Parsial Satu Active v1 12 Jun 26 Jane Smith; PT Hak Parsial Dua Active v1 13 Jun 26 Jane Smith. Pengecualian S-06/S-12 butir A-14 (nama literal tanpa suffix; seeding idempoten dan pemulihan oleh fixture backend di hook `before` dan `after`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global dan pemulihan: spec hanya membaca; Last Updated dan Changelog plan tidak berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### Screening header, kolom, urutan default, dan footer (TC-AC-PF-410)

1. Buka Plan Detail `Growth` (klik nama plan `Growth` pada tab Default, sub-tab Active).
2. Klik Tab Assigned Clients.
3. Verifikasi Tab `Overview` dan `Assigned Clients` tampil, dengan Tab `Assigned Clients` aktif.
4. Verifikasi Table Tools `Search`, `Filter`, `Download` tampil.
5. Verifikasi teks "6 clients on an outdated version" tampil.
6. Verifikasi Table Tools tidak memuat ikon Changelog dan tidak memuat tombol create.
7. Verifikasi header kolom berurutan `Client Name`, `Subscription Status`, `Plan Version`, `Assigned Date`, `Assigned By`, `Column Visibility (⋯)`.
8. Verifikasi header `Client Name`, `Subscription Status`, `Plan Version`, `Assigned Date`, `Assigned By` bersifat sortable.
9. Verifikasi tidak ada kolom checkbox.
10. Klik header kolom `Column Visibility (⋯)`.
11. Verifikasi Overlay Column Visibility terbuka.
12. Verifikasi urutan baris tabel tidak berubah oleh klik header `Column Visibility (⋯)` (header tidak sortable).
13. Tutup Overlay Column Visibility (tekan Esc).
14. Verifikasi urutan baris default Client Name A-Z: `PT Bumi Sentosa`, `PT Cahaya Mandiri`, `PT Hak Parsial Dua`, `PT Hak Parsial Satu`, `PT Karya Abadi`, `PT Sejahtera Abadi`, `PT Timur Jaya`, `PT Wahana Nusantara`, `PT Zona Nol`.
15. Verifikasi baris `PT Wahana Nusantara` memuat `Active` | `v1` dengan badge `Outdated` | `05 Jun 26` | `John D`.
16. Klik ikon row action (⋯) pada baris `PT Wahana Nusantara`.
17. Verifikasi row action menu tampil pada baris tersebut.
18. Tutup row action menu (tekan Esc).
19. Verifikasi teks footer `Showing 1–9 of 9 entries`.
20. Verifikasi teks footer `Rows per page: 10`.

### Format sel Assigned By dan Client Name (TC-AC-PF-453)

21. Verifikasi sel Assigned By baris `PT Wahana Nusantara` berupa plain text `John D`.
22. Verifikasi sel Client Name baris `PT Wahana Nusantara` berupa link dengan warna netral.
23. Hover `John D` pada baris `PT Wahana Nusantara`.
24. Verifikasi tooltip `John Doe` tampil.
25. Hover link `PT Wahana Nusantara`.
26. Verifikasi warna link `PT Wahana Nusantara` berubah ke warna primary saat hover.
27. Verifikasi link `PT Wahana Nusantara` tidak memakai underline saat hover.

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 13 dan 18 (menutup overlay dan row action menu), 10 (klik header Column Visibility dipakai untuk mengamati bahwa header tidak sortable pada langkah 11 dan 12).
- Langkah 16 sampai 18 mengamati row action menu per baris sesuai Expected b TC-AC-PF-410; isi menunya tidak diasersi karena TC tidak menyebutnya.
- TC-AC-PF-453 bertipe UI Only dan dijalankan di backend nyata yang sama dengan TC-AC-PF-410 (Dataset Plan D).
- Temuan untuk QA:
  - TC-AC-PF-453 Expected b menyebut "warna netral" dan "warna primary" tanpa nilai warna atau token desain; asersi warna memakai gaya terhitung (computed style) yang nilainya perlu dikonfirmasi tim FE.
  - TC-AC-PF-410 Expected b menyebut kolom `Column Visibility (⋯)` "unsortable" tanpa menyebut cara mengamatinya; langkah 12 mengamati bahwa klik header tidak mengubah urutan baris.
