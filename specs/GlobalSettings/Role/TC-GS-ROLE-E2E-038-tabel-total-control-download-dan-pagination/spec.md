---
id: TC-GS-ROLE-E2E-038-tabel-total-control-download-dan-pagination
title: "Ekspor Download CSV/XLSX dan Navigasi Pagination Tab Total Control"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-74
  - TC-GS-ROLE-75
  - TC-GS-ROLE-76
  - TC-GS-ROLE-334
  - TC-GS-ROLE-346
coverage:
  web: automated
---

# Ekspor Download CSV/XLSX dan Navigasi Pagination Tab Total Control

## Prerequisites

- Login sebagai Role: Total Control
- Dataset Tab Total Control memiliki lebih dari 10 record user

## Test Steps

1. Buka Global Settings > Role & Permission > Tab Total Control
2. Klik tombol Download pada toolbar
3. Verifikasi menu popover download menampilkan opsi 'Download as CSV' dan 'Download as XLSX'
4. Pilih 'Download as CSV'
5. Verifikasi file bernama Role-Permission-Total-Control.csv berhasil diunduh tanpa memicu toast sukses
6. Verifikasi isi file mencakup seluruh record data dan header kolom data tanpa kolom kontrol Actions
7. Amati kontrol pagination di bagian footer tabel
8. Verifikasi dropdown page size menyediakan persis opsi 10, 25, 50, dan 100 tanpa opsi "All"
9. Pilih opsi 25 pada dropdown page size
10. Verifikasi jumlah baris yang dirender pada tabel berubah menjadi 25 record
11. Ketik nomor halaman '2' pada input lompat halaman lalu tekan Enter
12. Verifikasi tabel berpindah ke halaman ke-2
13. Lakukan refresh browser (F5) dan verifikasi preferensi page size dan posisi halaman tetap bertahan (persist)

## Notes

- Download ekspor file CSV/XLSX mengunduh seluruh baris dataset dan tidak memicu toast sukses (role.md §4.2a, §9.9).
