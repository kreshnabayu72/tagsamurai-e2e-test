---
id: TC-AC-PF-E2E-152-setup-column-tab-custom-active-guard-satu-kolom-dan-batas
title: Setup Column Tab Custom Active Guard Satu Kolom dan Batas Pin
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-391
  - TC-AC-PF-392
coverage:
  web: automated
---

# Setup Column Tab Custom Active Guard Satu Kolom dan Batas Pin

## Prerequisites

- Mode: FE+BE
- Akun: `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, Total Control, Principal), password dari env `AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Halaman awal: Plans & Licensing > Plans & Features > Default > Active (langkah 1 pindah ke tab Custom).
- Data Pre-setup: Dataset Plan C (Pre-setup #23): custom Principal aktif `alpha Tier`, `Beta Pro`, `Growth Tier`, `Zeta Max`; semuanya Paid.
- General Settings (Pre-setup #44): Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- Kemampuan teknis: fixture BE idempoten untuk memulihkan Dataset Pre-setup ke keadaan awal (disediakan tim FE/BE, dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` spec ini. Fixture `fixtures/plans-licensing-plans-features.json` belum ada (S-12); nilai data ditulis literal dari Pre-setup.
- Pengecualian S-06/S-12 butir A-14: nama literal Pre-setup tanpa suffix; suite serial. Spec ini tidak mengubah data Pre-setup dan tidak menyimpan konfigurasi kolom (popup ditutup tanpa Save).
- Flag Guided Tooltip: sesuai pernyataan di `suite.md` (hook suite `before` dan `after`).

## Test Steps

1. Klik tab Custom, lalu sub-tab Active.

### TC-AC-PF-391 Guard satu kolom tersisa

2. Buka Popup Setup Column dan uncheck semua kolom kecuali `Clients`.
3. Hover checkbox kolom `Clients`.
4. Verifikasi checkbox `Clients` Disabled (tetap tampil).
5. Verifikasi tooltip "At least one column must remain visible.".
6. Coba uncheck kolom `Clients`.
7. Verifikasi checkbox `Clients` tidak bisa di-uncheck (tetap tercentang).
8. Centang kembali satu kolom lain.
9. Verifikasi semua checkbox enabled.

### TC-AC-PF-392 Batas pin tiga kolom

10. Klik `[Reset to Default]`.
11. Pin kolom `Plan Name`, `Product`, `Pricing Type`.
12. Hover icon Pin kolom `Version`.
13. Verifikasi icon Pin `Version` Disabled.
14. Verifikasi tooltip "Maximum 3 columns can be pinned at once. Unpin another column first.".
15. Klik icon Pin kolom `Version`.
16. Verifikasi klik tidak membekukan kolom `Version`.
17. Unpin kolom `Pricing Type`.
18. Verifikasi icon Pin kolom lain kembali aktif.
19. Klik icon close `(X)`.

## Notes

- Langkah penghubung (S-03), ditulis tanpa `Verifikasi`: langkah 1 membuka tab Custom; langkah 10 mengembalikan konfigurasi kolom ke default sebelum TC-AC-PF-392; langkah 19 menutup popup tanpa Save.
- Temuan untuk QA: TC-AC-PF-391 Expected b ("Setelah satu kolom lain dicentang kembali semua checkbox enabled") tidak punya langkah pada Langkah Uji; spec menambah langkah 8 tanpa menentukan kolom. TC-AC-PF-392 langkah 4 "Unpin satu kolom" tidak menyebut kolom; spec memakai `Pricing Type`.
- Jumlah langkah 19: di bawah ambang sekitar 35.
