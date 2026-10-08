---
id: TC-GS-USER-E2E-001-screening-tabel-user-list-layout-dan-default-sort
title: "Screening tabel User List layout, breadcrumb, Table Tools, dan default sort Name A-Z"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-1
  - TC-GS-USER-2
  - TC-GS-USER-7
  - TC-GS-USER-11
  - TC-GS-USER-13
  - TC-GS-USER-25
coverage:
  web: automated
---

# Screening tabel User List layout, breadcrumb, Table Tools, dan default sort Name A-Z

## Prerequisites

- Login sebagai Role: Total Control
- Entity Client aktif
- Data pre-setup User (Tabel Data Uji Pre-setup No. 10–22) tersedia di environment

## Test Steps

### Screening Layout dan Breadcrumb

1. Buka menu Global Settings > User melalui sidebar
2. Verifikasi breadcrumb menampilkan 'User > User List' tanpa Page Title Header
3. Verifikasi tab 'User List' aktif dan sub-tab 'Login User' aktif secara default
4. Verifikasi area Table Tools rata kanan menampilkan ikon Search, Filter, Download, Changelog, dan tombol primary '[+ User]'
5. Hover setiap ikon di Table Tools, verifikasi tooltip masing-masing menampilkan 'Search', 'Filter', 'Download', dan 'Changelog'
6. Verifikasi header tabel menampilkan kolom Checkbox, Active, Name, Email, Position, Division, Access, Employee ID, Modified By, Last Update, dan Column Visibility (⋯)

### Default Sort dan Interaksi Baris

7. Verifikasi baris tabel otomatis terurut berdasarkan kolom Name A-Z case-insensitive
8. Verifikasi tidak ada indikator panah sort aktif di header kolom selain default Name
9. Hover teks Name pada salah satu baris, verifikasi warna teks berubah ke warna primary Global Settings tanpa underline
10. Klik sel Email atau Division pada baris yang sama, verifikasi tidak terjadi navigasi atau seleksi baris (area bukan primary identifier tidak memicu aksi)

## Notes

- Menggabungkan 6 test case granular (TC-GS-USER-1 s.d. TC-GS-USER-25).
