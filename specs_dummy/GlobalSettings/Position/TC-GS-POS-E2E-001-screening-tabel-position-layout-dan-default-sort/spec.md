---
id: TC-GS-POS-E2E-001-screening-tabel-position-layout-dan-default-sort
title: "Screening tab Position, breadcrumb, visual styling, dan default sort Name A-Z"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-1
  - TC-GS-POS-2
  - TC-GS-POS-3
  - TC-GS-POS-4
  - TC-GS-POS-5
  - TC-GS-POS-9
  - TC-GS-POS-291
  - TC-GS-POS-293
coverage:
  web: automated
---

# Screening tab Position, breadcrumb, visual styling, dan default sort Name A-Z

## Prerequisites

- Login sebagai Role: Total Control (Budi Santoso)
- Entity Client aktif
- Tabel Position berisi ≥11 record (memuat record pre-setup IT Manager, Finance Analyst, Warehouse Supervisor, serta record seed 'Head of Operations' dan hasil Import 'Field Technician')
- Record Position dengan panjang 120 karakter sudah dibuat di environment

## Test Steps

### Screening Layout dan Breadcrumb

1. Buka sidebar Global Settings > User, lalu klik sub-tab "Position"
2. Verifikasi breadcrumb menampilkan teks "User > Position" dengan tombol "[?]" di sampingnya
3. Verifikasi segmen "User" dan "Position" tidak dapat diklik (bukan tautan link yang berpindah halaman)
4. Verifikasi sub-tab menampilkan "User List | Position (aktif) | Division | Custom Field"
5. Verifikasi area Table Tools rata kanan menampilkan ikon Search, Filter, Download, Changelog, dan tombol primary "[+ Position]" dengan ikon AddLine
6. Hover ikon Search, Filter, Download, Changelog, dan header kolom Actions (⋯), verifikasi tooltip masing-masing menampilkan "Search", "Filter", "Download", "Changelog", dan "Column Visibility"

### Default Sort dan Data Rendering

7. Verifikasi baris tabel otomatis terurut berdasarkan kolom Name A-Z (ascending case-insensitive) tanpa ada indikator panah sort aktif
8. Verifikasi record seed "Head of Operations" dan record hasil Import "Field Technician" memiliki kolom Last Updated yang terisi tanggal-waktu valid (tidak kosong atau "—")
9. Temukan baris dengan nama Position 120 karakter, verifikasi nama tampil utuh tanpa terpotong ellipsis (...) dan wrap natural

### Visual State

10. Hover salah satu baris tabel, verifikasi latar belakang baris berubah menjadi highlight hover
11. Centang checkbox pada baris tersebut, verifikasi baris memiliki status visual selected
12. Hover dan fokuskan keyboard pada tombol "[+ Position]", verifikasi perubahan background hover dan kemunculan focus ring

## Notes

- Menggabungkan TC-GS-POS-1, 2, 3, 4, 5, 9, 291, dan 293 dalam satu alur screening tanpa mutasi data.
- TC-GS-POS-9 menguji batas tampilan 120 karakter pada tabel.
