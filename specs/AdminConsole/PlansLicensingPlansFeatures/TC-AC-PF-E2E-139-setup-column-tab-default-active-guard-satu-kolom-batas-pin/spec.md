---
id: TC-AC-PF-E2E-139-setup-column-tab-default-active-guard-satu-kolom-batas-pin
title: Setup Column Tab Default Active Guard Satu Kolom, Batas Pin, dan Independensi Cache
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-342
  - TC-AC-PF-343
  - TC-AC-PF-344
coverage:
  web: automated
---

# Setup Column Tab Default Active Guard Satu Kolom, Batas Pin, dan Independensi Cache

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active.
- Data Pre-setup: Dataset Plan A (Pre-setup #21), default aktif `Starter`, `Growth`, `Professional`, `Enterprise`, `SIEM`; sub-tab Default Archive dan tab Custom Active memuat data Dataset Plan A (Growth Plus (old), Growth Tier).
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup.
- State sementara: langkah 19 menyimpan kolom `Clients` tersembunyi pada tab Default Active; preferensi dihapus di hook `after` (kemampuan menghapus preferensi kolom di browser disediakan tim FE, bagian 4).
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

### TC-AC-PF-342 Guard satu kolom tersisa

1. Buka Popup Setup Column dan uncheck semua kolom kecuali `Clients`.
2. Hover checkbox kolom `Clients`.
3. Verifikasi checkbox `Clients` Disabled (tetap tampil).
4. Verifikasi tooltip "At least one column must remain visible.".
5. Coba uncheck kolom `Clients`.
6. Verifikasi checkbox `Clients` tidak bisa di-uncheck (tetap tercentang).
7. Centang kembali satu kolom lain.
8. Verifikasi semua checkbox enabled.

### TC-AC-PF-343 Batas pin tiga kolom

9. Klik `[Reset to Default]`.
10. Pin kolom `Plan Name`, `Product`, `Pricing Type`.
11. Hover icon Pin kolom `Version`.
12. Verifikasi icon Pin `Version` Disabled.
13. Verifikasi tooltip "Maximum 3 columns can be pinned at once. Unpin another column first.".
14. Klik icon Pin kolom `Version`.
15. Verifikasi klik tidak membekukan kolom `Version`.
16. Unpin kolom `Pricing Type`.
17. Verifikasi icon Pin kolom lain kembali aktif.
18. Klik icon close `(X)`.

### TC-AC-PF-344 Independensi cache Setup Column

19. Buka Popup Setup Column, sembunyikan kolom `Clients`, klik `[Save]`.
20. Klik sub-tab Archive.
21. Verifikasi Default Archive tetap menampilkan kolom `Clients`.
22. Klik tab Custom, lalu sub-tab Active.
23. Verifikasi Custom Active tetap menampilkan kolom `Clients`.
24. Klik tab Default, lalu sub-tab Active.
25. Verifikasi kolom `Clients` tetap tersembunyi pada Default Active.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 9 mengembalikan konfigurasi kolom ke default sebelum TC-AC-PF-343 (langkah 1 sampai 8 meninggalkan kolom tidak lengkap); langkah 18 menutup popup tanpa Save.
- Temuan untuk QA: TC-AC-PF-342 Expected b ("Setelah satu kolom lain dicentang kembali semua checkbox enabled") tidak punya langkah pada Langkah Uji; spec menambah langkah 7 (centang kembali satu kolom) tanpa menentukan kolom. TC-AC-PF-343 langkah 4 "Unpin satu kolom" tidak menyebut kolom; spec memakai `Pricing Type`.
- Jumlah langkah 25: di bawah ambang sekitar 35.
