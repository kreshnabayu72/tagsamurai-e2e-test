---
id: TC-AC-PF-E2E-173-tab-assigned-clients-term-terminal-term-campuran-term
title: "Tab Assigned Clients: client yang hanya punya term terminal tidak dirender dan tidak dihitung"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-633
  - TC-AC-PF-634
coverage:
  web: automated
---

# Tab Assigned Clients: client yang hanya punya term terminal tidak dirender dan tidak dihitung

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip mengikuti pernyataan di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE, sesuai `suite.md`): sesi API aktor, klien HTTP, dan fixture backend yang melakukan seeding term terminal (Renewed, Rejected, Canceled, Converted, Deleted) serta memulihkan Dataset Plan TM ke keadaan awal secara idempoten. Fixture `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis literal sesuai Pre-setup.
- Data Pre-setup: Dataset Plan TM (pengecualian S-06/S-12 butir A-14: nama literal tanpa suffix; seeding idempoten dan pemulihan oleh fixture backend di hook `before` dan `after`):
  - Custom plan `Paket Terminal Aktif` v2 dengan `PT Term Aktif` Active v2; lima client yang hanya punya satu term terminal: `PT Term Renewed` Renewed, `PT Term Rejected` Rejected, `PT Term Canceled` Canceled, `PT Term Converted` Converted, `PT Term Deleted` Deleted.
  - Custom plan `Paket Terminal Arsip` archived v1 dengan lima client yang hanya punya satu term terminal: `PT Arsip Renewed`, `PT Arsip Rejected`, `PT Arsip Canceled`, `PT Arsip Converted`, `PT Arsip Deleted` (terhapus permanen).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global dan pemulihan: spec hanya membaca; Last Updated dan Changelog plan tidak berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### Plan aktif dengan client berterm terminal (TC-AC-PF-633)

1. Klik tab `Custom`, sub-tab `Active`.
2. Verifikasi kolom Clients baris `Paket Terminal Aktif` bernilai `1` (hanya subscription Active atau Grace yang dihitung).
3. Klik `Paket Terminal Aktif`.
4. Klik Tab Assigned Clients.
5. Verifikasi Tab Assigned Clients memuat satu baris: `PT Term Aktif` | `Active` | `v2`.
6. Verifikasi teks footer `Showing 1–1 of 1 entries`.
7. Verifikasi tidak ada baris `PT Term Renewed`, `PT Term Rejected`, `PT Term Canceled`, `PT Term Converted`, maupun `PT Term Deleted`.
8. Klik ikon Filter.
9. Buka dropdown Subscription Status.
10. Verifikasi dropdown Subscription Status memuat opsi `Active`.
11. Verifikasi dropdown Subscription Status tidak memuat opsi `Renewed`, `Rejected`, `Canceled`, `Converted`, maupun `Deleted`.
12. Tutup dropdown Subscription Status dan Filter Panel tanpa menerapkan filter.

### Plan archived dengan client berterm terminal (TC-AC-PF-634)

13. Kembali ke Plans & Licensing > Plans & Features > Custom.
14. Klik sub-tab `Archive`.
15. Verifikasi kolom Clients baris `Paket Terminal Arsip` bernilai `4` (historical count lintas status subscription: `PT Arsip Renewed`, `PT Arsip Rejected`, `PT Arsip Canceled`, `PT Arsip Converted` terhitung; `PT Arsip Deleted` tidak terhitung karena terhapus permanen).
16. Klik ikon row action (⋯) baris `Paket Terminal Arsip`.
17. Verifikasi menu row action hanya memuat `Detail`; `Delete` tidak tersedia karena Clients bernilai `4`, artinya masih ada record subscription yang merujuk plan (`PT Arsip Deleted` tidak terhitung karena sudah terhapus permanen).
18. Klik `Detail`.
19. Klik Tab Assigned Clients.
20. Verifikasi Table Tools `Search`, `Filter`, `Download` tampil.
21. Verifikasi Tab Assigned Clients tidak memuat baris untuk `PT Arsip Renewed`, `PT Arsip Rejected`, `PT Arsip Canceled`, `PT Arsip Converted`, maupun `PT Arsip Deleted`.

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 12 (menutup dropdown dan Filter Panel), 13 dan 14 (berpindah ke sub-tab Archive).
- Langkah 20 menjadi anchor positif bagi asersi absence baris pada langkah 21 (halaman Plan Detail dan Tab Assigned Clients sudah termuat; bagian 8b butir 2). Langkah 5 menjadi anchor bagi langkah 7, dan langkah 10 bagi langkah 11.
- Langkah 17 memuat kesimpulan ("`Delete` tidak tersedia karena Clients bernilai `4`") sebagai satu `Verifikasi` karena tidak teramati terpisah dari isi menu (S-03).
- TC-AC-PF-640, TC-AC-PF-747, dan TC-AC-PF-748 (term campuran dan term Trial) ada di spec 177.
- Temuan untuk QA:
  - TC-AC-PF-634 Expected c mengasersi absensi baris tanpa menyebut tampilan Tab Assigned Clients (empty state atau tabel lain); spec hanya mengasersi absensi baris dengan anchor Table Tools.
