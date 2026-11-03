---
id: TC-AC-PF-E2E-168-setup-column-tab-assigned-clients-tutup-guard-batas-pin
title: "Setup Column Tab Assigned Clients: tutup tanpa Save, guard satu kolom, dan batas pin tiga kolom"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-435
  - TC-AC-PF-436
  - TC-AC-PF-437
coverage:
  web: automated
---

# Setup Column Tab Assigned Clients: tutup tanpa Save, guard satu kolom, dan batas pin tiga kolom

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip mengikuti pernyataan di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE, sesuai `suite.md`): sesi API aktor, klien HTTP, dan fixture backend yang memulihkan Dataset Plan D ke keadaan awal secara idempoten; penghapusan preferensi kolom Tab Assigned Clients di browser (disediakan tim FE). Fixture `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis literal sesuai Pre-setup.
- Data Pre-setup: Dataset Plan D, default plan `Growth` v5 dengan 9 client: PT Sejahtera Abadi Active v5 17 Jun 26 John Doe; PT Wahana Nusantara Active v1 05 Jun 26 John Doe; PT Karya Abadi Active v1 03 Jun 26 Jane Smith; PT Cahaya Mandiri Grace v5 20 Jun 26 Jane Smith; PT Bumi Sentosa Active v1 11 Jun 26 Jane Smith; PT Timur Jaya Active v1 09 Jun 26 John Doe; PT Zona Nol Active v5 25 Jun 26 John Doe; PT Hak Parsial Satu Active v1 12 Jun 26 Jane Smith; PT Hak Parsial Dua Active v1 13 Jun 26 Jane Smith. Pengecualian S-06/S-12 butir A-14 (nama literal tanpa suffix; seeding idempoten dan pemulihan oleh fixture backend di hook `before` dan `after`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global dan pemulihan: spec tidak pernah menekan `[Save]`, sehingga preferensi kolom tidak berubah; hook `after` tetap menghapus preferensi kolom Tab Assigned Clients. Last Updated dan Changelog plan tidak berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### Tutup tanpa Save (TC-AC-PF-435)

1. Buka Plan Detail `Growth` (klik nama plan `Growth` pada tab Default, sub-tab Active).
2. Klik Tab Assigned Clients.
3. Buka Popup Setup Column (klik header kolom Actions (`⋯`), lalu `Setup Column...`).
4. Uncheck kolom `Assigned By`.
5. Klik icon close `(X)`.
6. Verifikasi modal Setup Column tertutup.
7. Verifikasi tabel tetap menampilkan kolom `Assigned By` (perubahan preview dibuang).
8. Buka Popup Setup Column lagi.
9. Uncheck kolom `Assigned By`.
10. Tekan Esc.
11. Verifikasi modal Setup Column tertutup.
12. Verifikasi tabel tetap menampilkan kolom `Assigned By` (perubahan preview dibuang).

### Guard satu kolom tersisa (TC-AC-PF-436)

13. Buka Popup Setup Column.
14. Uncheck kolom `Client Name`, `Subscription Status`, `Plan Version`, dan `Assigned Date` hingga hanya `Assigned By` tercentang.
15. Hover checkbox kolom `Assigned By`.
16. Verifikasi checkbox `Assigned By` Disabled dan tetap tampil.
17. Verifikasi tooltip "At least one column must remain visible." tampil.
18. Klik checkbox kolom `Assigned By` untuk mencoba meng-uncheck.
19. Verifikasi checkbox `Assigned By` tetap tercentang.
20. Centang kembali kolom `Client Name`.
21. Verifikasi semua checkbox kolom enabled.
22. Klik icon close `(X)`.

### Batas pin tiga kolom (TC-AC-PF-437)

23. Buka Popup Setup Column.
24. Klik icon Pin kolom `Client Name`.
25. Klik icon Pin kolom `Subscription Status`.
26. Klik icon Pin kolom `Plan Version`.
27. Hover icon Pin kolom `Assigned Date`.
28. Verifikasi icon Pin kolom `Assigned Date` Disabled.
29. Verifikasi tooltip "Maximum 3 columns can be pinned at once. Unpin another column first." tampil.
30. Klik icon Pin kolom `Assigned Date`.
31. Verifikasi kolom `Assigned Date` tidak ter-pin (klik tidak membekukan kolom).
32. Unpin kolom `Plan Version`.
33. Verifikasi icon Pin kolom lain kembali aktif.
34. Klik icon close `(X)`.

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 22 dan 34 (menutup popup tanpa Save sehingga perubahan preview dibuang dan state bersih untuk blok berikutnya, S-09).
- TC-AC-PF-438 (independensi cache Setup Column terhadap tabel Plans List) ada di spec 176.
- Temuan untuk QA:
  - TC-AC-PF-436 Expected b ("Setelah satu kolom lain dicentang kembali semua checkbox enabled") tidak menyebut kolom yang dicentang; spec memakai `Client Name`.
  - TC-AC-PF-437 langkah 6 ("Unpin satu kolom") tidak menyebut kolom yang di-unpin; spec memakai `Plan Version`.
