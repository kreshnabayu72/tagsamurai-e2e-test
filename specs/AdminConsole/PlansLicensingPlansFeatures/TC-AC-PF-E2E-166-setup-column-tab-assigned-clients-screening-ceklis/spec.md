---
id: TC-AC-PF-E2E-166-setup-column-tab-assigned-clients-screening-ceklis
title: "Setup Column Tab Assigned Clients: screening overlay dan popup, ceklis kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-429
  - TC-AC-PF-430
  - TC-AC-PF-431
coverage:
  web: automated
---

# Setup Column Tab Assigned Clients: screening overlay dan popup, ceklis kolom

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip mengikuti pernyataan di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE, sesuai `suite.md`): sesi API aktor, klien HTTP, dan fixture backend yang memulihkan Dataset Plan D ke keadaan awal secara idempoten; penghapusan preferensi kolom Tab Assigned Clients di browser (disediakan tim FE). Fixture `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis literal sesuai Pre-setup.
- Data Pre-setup: Dataset Plan D, default plan `Growth` v5 dengan 9 client: PT Sejahtera Abadi Active v5 17 Jun 26 John Doe; PT Wahana Nusantara Active v1 05 Jun 26 John Doe; PT Karya Abadi Active v1 03 Jun 26 Jane Smith; PT Cahaya Mandiri Grace v5 20 Jun 26 Jane Smith; PT Bumi Sentosa Active v1 11 Jun 26 Jane Smith; PT Timur Jaya Active v1 09 Jun 26 John Doe; PT Zona Nol Active v5 25 Jun 26 John Doe; PT Hak Parsial Satu Active v1 12 Jun 26 Jane Smith; PT Hak Parsial Dua Active v1 13 Jun 26 Jane Smith. Pengecualian S-06/S-12 butir A-14 (nama literal tanpa suffix; seeding idempoten dan pemulihan oleh fixture backend di hook `before` dan `after`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global dan pemulihan: spec menyimpan konfigurasi kolom Tab Assigned Clients (preferensi di browser); langkah 31 dan hook `after` menghapus preferensi itu. Last Updated dan Changelog plan tidak berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### Screening Overlay Column Visibility (TC-AC-PF-429)

1. Buka Plan Detail `Growth` (klik nama plan `Growth` pada tab Default, sub-tab Active).
2. Klik Tab Assigned Clients.
3. Hover header kolom Actions (`⋯`).
4. Verifikasi tooltip header kolom Actions `Column Visibility` tampil.
5. Klik header kolom Actions (`⋯`).
6. Verifikasi Overlay Column Visibility muncul.
7. Verifikasi Overlay Column Visibility memuat daftar kolom berurutan `Client Name`, `Subscription Status`, `Plan Version`, `Assigned Date`, `Assigned By`.
8. Verifikasi setiap kolom pada overlay memiliki checkbox tercentang yang enabled (Hideable).
9. Verifikasi setiap kolom pada overlay memiliki drag handle.
10. Verifikasi item `Setup Column...` ada di bagian bawah overlay.

### Screening Popup Setup Column (TC-AC-PF-430)

11. Klik `Setup Column...`.
12. Verifikasi Title `Setup Column` tampil di header popup.
13. Verifikasi deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns." tampil di header popup.
14. Verifikasi icon close `(X)` tampil di kanan atas popup.
15. Verifikasi daftar kolom `Client Name`, `Subscription Status`, `Plan Version`, `Assigned Date`, `Assigned By` tampil di body popup.
16. Verifikasi setiap kolom pada popup memiliki checkbox tercentang.
17. Verifikasi setiap kolom pada popup memiliki drag handle.
18. Verifikasi setiap kolom pada popup memiliki icon Pin.
19. Verifikasi Live Preview menampilkan urutan header kolom dan data sel yang sama dengan tabel.
20. Verifikasi footer popup memuat tombol `[Reset to Default]` (text, primary) dan `[Save]` (filled, success).
21. Verifikasi footer popup tidak memuat tombol `[Cancel]`.

### Ceklis kolom, Save, dan F5 (TC-AC-PF-431)

22. Uncheck kolom `Assigned By` pada popup.
23. Verifikasi Live Preview tidak lagi menampilkan kolom `Assigned By`.
24. Verifikasi tabel di belakang modal tidak lagi menampilkan kolom `Assigned By`.
25. Klik `[Save]`.
26. Verifikasi modal Setup Column tertutup.
27. Verifikasi tabel tanpa kolom `Assigned By`.
28. Tekan F5.
29. Verifikasi header tabel Tab Assigned Clients memuat `Client Name`, `Subscription Status`, `Plan Version`, dan `Assigned Date`.
30. Verifikasi kolom `Assigned By` tetap tidak tampil setelah F5.
31. Pulihkan konfigurasi kolom: hapus preferensi Setup Column Tab Assigned Clients di browser (kemampuan disediakan tim FE) lalu muat ulang halaman.

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 11 (membuka popup dari overlay yang terbuka) dan 31 (pemulihan konfigurasi kolom, bagian 4 konvensi).
- Langkah 24 mengasersi tabel di belakang modal pada state sementara sebelum `[Save]`; langkah 27 mengasersi tabel sesudah modal tertutup.
- Temuan untuk QA:
  - TC-AC-PF-431 Post Condition "Preferensi kolom tersimpan di localStorage" tidak punya langkah observasi di TC; persistensi hanya teramati lewat F5 (langkah 28 sampai 30) dan Post Condition tidak diasersi terpisah.
  - TC-AC-PF-429 tidak menyebut urutan penutupan overlay sebelum popup dibuka; popup dibuka langsung dari overlay yang terbuka (langkah 11).
  - TC-AC-PF-430 menyebut "Live Preview menampilkan ... data sel yang sama dengan tabel" tanpa menyebut sel yang dibandingkan; spec mengasersi urutan header dan data sel apa adanya.
  - `suite.md` belum mendaftarkan penghapusan preferensi Setup Column di hook `after` (bagian 4 konvensi), padahal spec ini menyimpan konfigurasi kolom.
