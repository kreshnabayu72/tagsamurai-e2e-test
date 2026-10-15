---
id: TC-AC-PP-E2E-047-download-volume-5001-baris
title: "Download CSV Lebih dari 5.000 Baris Diproses Sinkron (Riwayat D)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PP-207
coverage:
  web: automated
---

# Download CSV Lebih dari 5.000 Baris Diproses Sinkron (Riwayat D)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, nama tampil Andi Wijaya, env var `AC_TC_PASSWORD`). Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Dataset: Riwayat D (Version 1 sampai 5.001; Published By bergantian `John Doe` dan `Jane Smith`; Version 5.001 Active). Hook `before` men-seed Riwayat D lewat Fixture BE (kemampuan teknis: membuat ulang dataset Riwayat dalam volume besar; riwayat append-only sehingga tidak bisa dihapus lewat UI). Hook `after` mengembalikan dataset ke Riwayat A.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Kemampuan teknis: membaca file CSV yang terunduh (jumlah baris) dan membersihkan folder unduhan di hook `after` (kelas e volume data dan kelas f binary buffer).
- Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide; spec ini tidak membuat atau mengubah versi.
- Tidak ada fixture nilai tetap: halaman dibuka lewat sidebar (Settings > Privacy Policy).

## Test Steps

### TC-AC-PP-207: Download lebih dari 5.000 baris diproses sinkron dan seluruh baris ada pada file

1. Buka Settings > Privacy Policy lewat sidebar
2. Klik icon Download
3. Pilih "Download as CSV"
4. Verifikasi file `Privacy-Policy-Version-History.csv` terunduh langsung dari aksi yang sama
5. Verifikasi tidak ada langkah menunggu atau job background (file terunduh tanpa proses lanjutan)
6. Verifikasi tidak ada toast pemberitahuan lanjutan
7. Buka file yang terunduh
8. Verifikasi file memuat baris header
9. Verifikasi file memuat 5.001 baris data
10. Verifikasi tidak ada toast sukses

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: e (volume data khusus, 5.001 versi) dan f (isi file); satu spec sendiri karena dataset Riwayat D hanya dipakai TC ini.
- Langkah 4 sampai 6 memecah Expected a TC menjadi tiga klausa yang dapat gagal sendiri (terunduh langsung, tanpa job background atau menunggu, tanpa toast lanjutan).
- Spec tidak membuat data dan tidak mengubah Pre-setup.
- Temuan untuk QA: tidak ada.
