---
id: TC-AC-PF-E2E-169-pagination-tab-assigned-clients-default-dan-navigasi
title: "Pagination Tab Assigned Clients: default 10 baris, opsi page size, dan navigasi halaman"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-439
  - TC-AC-PF-440
coverage:
  web: automated
---

# Pagination Tab Assigned Clients: default 10 baris, opsi page size, dan navigasi halaman

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip mengikuti pernyataan di `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE, sesuai `suite.md`): sesi API aktor, klien HTTP, dan fixture backend yang melakukan seeding volume besar serta memulihkan Dataset Plan Q ke keadaan awal secara idempoten. Fixture `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis literal sesuai Pre-setup.
- Data Pre-setup: Dataset Plan Q, custom plan `Paket Banyak Client` dengan 120 client bernama `PT Massal 001` sampai `PT Massal 120`. Pengecualian S-06/S-12 butir A-14 (nama literal tanpa suffix; seeding idempoten dan pemulihan oleh fixture backend di hook `before` dan `after`). Volume 100 baris atau lebih: kelas e (volume data).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC.
- State global dan pemulihan: spec hanya membaca; Last Updated dan Changelog plan tidak berubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### Default dan opsi page size (TC-AC-PF-439)

1. Klik tab `Custom`, sub-tab `Active`.
2. Buka Plan Detail `Paket Banyak Client` (klik nama plan `Paket Banyak Client`).
3. Klik Tab Assigned Clients.
4. Verifikasi halaman 1 menampilkan 10 baris.
5. Verifikasi teks footer `Showing 1–10 of 120 entries`.
6. Verifikasi teks footer `Rows per page: 10`.
7. Klik Overlay Page Size.
8. Verifikasi Overlay Page Size memuat opsi `10`, `25`, `50`, `100`.
9. Verifikasi Overlay Page Size tidak memuat opsi All.
10. Verifikasi tombol `Prev` Disabled pada halaman 1.
11. Tutup Overlay Page Size (tekan Esc).

### Navigasi halaman (TC-AC-PF-440)

12. Klik `Next`.
13. Verifikasi tabel menampilkan baris 11 sampai 20.
14. Verifikasi teks footer `Showing 11–20 of 120 entries`.
15. Klik `Prev`.
16. Verifikasi tabel kembali ke halaman 1 (teks footer `Showing 1–10 of 120 entries`).
17. Ketik `2` pada input nomor halaman, tekan Enter.
18. Verifikasi tabel langsung membuka halaman 2 (teks footer `Showing 11–20 of 120 entries`).

## Notes

- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 11 (menutup Overlay Page Size).
- Spec ini memakai kelas e (volume data, 120 baris) sebagai satu-satunya kelas harness; tidak ada pengecualian `P-n`.
- Temuan untuk QA:
  - TC-AC-PF-440 Expected a menyebut "baris 11 sampai 20" tanpa menuliskan nama baris; spec mengasersi rentang lewat teks footer dan jumlah baris tanpa menyebut nama `PT Massal NNN`, karena urutan default tidak disebut TC untuk plan ini.
