---
id: TC-AC-PP-E2E-046-download-mengikuti-search-dan-filter
title: "Download Mengikuti Search dan Filter Aktif lintas Halaman (Riwayat B)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-143
  - TC-AC-PP-144
coverage:
  web: automated
---

# Download Mengikuti Search dan Filter Aktif lintas Halaman (Riwayat B)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, nama tampil Andi Wijaya, env var `AC_TC_PASSWORD`). Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Dataset: Riwayat B (Version 1 sampai 120; Published By bergantian, ganjil `John Doe` dan genap `Jane Smith`, sehingga 60 versi oleh `John Doe`; Version 120 Active). Hook `before` men-seed Riwayat B lewat Fixture BE (kemampuan teknis: membuat ulang dataset Riwayat; riwayat append-only sehingga tidak bisa dihapus lewat UI). Hook `after` mengembalikan dataset ke Riwayat A.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Kemampuan teknis: membaca file CSV yang terunduh (jumlah baris data, header, nilai kolom) dan membersihkan folder unduhan di hook `after` (kelas f, binary buffer).
- Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide; spec ini tidak membuat atau mengubah versi.
- Tidak ada fixture nilai tetap: halaman dibuka lewat sidebar (Settings > Privacy Policy).

## Test Steps

### TC-AC-PP-143: Export mengikuti Search aktif dan mencakup seluruh baris yang cocok lintas halaman

1. Buka Settings > Privacy Policy lewat sidebar
2. Klik icon Search, ketik "doe", lalu tekan Enter
3. Verifikasi footer menampilkan `1–10 of 60` (60 baris pada 6 halaman dengan page size 10)
4. Klik icon Download
5. Pilih "Download as CSV"
6. Buka file yang terunduh
7. Verifikasi file memuat 60 baris data (bukan hanya 10 baris halaman aktif dan bukan 120 baris)
8. Verifikasi seluruh baris pada kolom Published By bernilai `John Doe`
9. Verifikasi baris dengan Published By `Jane Smith` tidak ada

### TC-AC-PP-144: Export mengikuti Filter aktif

10. Klik icon `(←)` pada search bar untuk menutup dan mereset Search
11. Klik icon Filter di toolbar
12. Pada field `Published By` centang `John Doe`
13. Klik `[Apply]`
14. Klik icon Download
15. Pilih "Download as CSV"
16. Buka file yang terunduh
17. Verifikasi file memuat 60 baris data
18. Verifikasi seluruh nilai Published By adalah `John Doe`
19. Verifikasi baris header berisi `Version`, `Published At`, `Published By`
20. Buka panel Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: f (binary buffer, isi file CSV).
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): langkah 10 (tutup dan reset Search sebelum Filter agar TC-144 hanya memakai Filter, sesuai langkah 1 TC sumber) dan langkah 20 (bersihkan Filter); hook `after` menjadi cadangan pemulihan.
- Spec tidak membuat data dan tidak mengubah Pre-setup.
- Temuan untuk QA: tidak ada.
