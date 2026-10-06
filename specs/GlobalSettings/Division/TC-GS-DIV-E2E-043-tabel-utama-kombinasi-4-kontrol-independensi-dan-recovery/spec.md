---
id: TC-GS-DIV-E2E-043-tabel-utama-kombinasi-4-kontrol-independensi-dan-recovery
title: "Kombinasi Penuh Search, Filter, Sort, Pagination, Independensi Clear, dan Pemulihan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-64
  - TC-GS-DIV-65
  - TC-GS-DIV-66
  - TC-GS-DIV-67
  - TC-GS-DIV-68
  - TC-GS-DIV-69
coverage:
  web: automated
---

# Kombinasi Penuh Search, Filter, Sort, Pagination, Independensi Clear, dan Pemulihan

## Prerequisites

- Login sebagai Role: Total Control
- Dataset divisi berjumlah cukup untuk pagination (>10 record)

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Terapkan kriteria Search, Filter Last Updated, Sort kolom Name, dan pindah ke halaman 2 pada pagination
3. Verifikasi seluruh kontrol aktif secara simultan menampilkan data hasil irisan yang presisi
4. Buka Filter Panel lalu klik '[Clear Field]' dan '[Apply]'
5. Verifikasi filter tanggal terlepas sedangkan keyword Search, status Sort, dan seleksi pagination tetap bertahan
6. Hapus teks pencarian Search Box lalu tekan Enter
7. Verifikasi pencarian terlepas dan kontrol Sort tetap aktif
8. Klik header kolom lain untuk mengganti target sort
9. Verifikasi arah sort berpindah ke kolom baru secara independen
10. Terapkan kombinasi filter yang menghasilkan 0 data (No results found), lalu klik reset filter
11. Verifikasi tabel pulih (recovery) menampilkan data semula

## Notes

- Menguji interaksi independensi 4 kontrol tabel sesuai prd-conventions.md §9.
