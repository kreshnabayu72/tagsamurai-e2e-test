---
id: TC-GS-POS-E2E-031-filter-panel-last-updated-tabel-utama
title: "Filter Panel tabel utama: rentang Last Updated inklusif, single-day, Clear, cancel, dan kolom hidden"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-159
  - TC-GS-POS-160
  - TC-GS-POS-161
  - TC-GS-POS-162
  - TC-GS-POS-163
  - TC-GS-POS-164
coverage:
  web: automated
---

# Filter Panel tabel utama: rentang Last Updated inklusif, single-day, Clear, cancel, dan kolom hidden

## Prerequisites

- Login sebagai Total Control
- Data Position dengan rentang waktu Last Updated bervariasi

## Test Steps

### Screening Filter Panel & Rentang Tanggal

1. Klik ikon Filter pada Table Tools
2. Verifikasi Filter Panel terbuka menampilkan kontrol pemilihan tanggal untuk kolom Last Updated
3. Pilih rentang tanggal inklusif (Start Date s.d. End Date) yang mencakup sebagian record
4. Klik tombol "[Apply]"
5. Verifikasi hanya record dengan Last Updated di dalam rentang tersebut yang tampil di tabel

### Filter Single Day & Pembatalan Tanpa Apply

6. Buka kembali Filter Panel, pilih tanggal yang sama untuk Start Date dan End Date (1 hari)
7. Klik "[Apply]" dan verifikasi record pada hari tersebut berhasil difilter
8. Buka Filter Panel, ubah tanggal, tetapi klik ikon close `[✕]` tanpa klik Apply
9. Verifikasi perubahan tanggal dibuang dan filter sebelumnya tetap aktif

### Clear Field Filter & Kolom Hidden

10. Buka Filter Panel lalu klik tombol "[Clear Field]"
11. Verifikasi input tanggal dikosongkan dan seluruh data kembali tampil di tabel
12. Sembunyikan kolom Last Updated via Column Visibility, lalu terapkan filter tanggal
13. Verifikasi filter tetap berfungsi menyaring baris meskipun kolom Last Updated sedang disembunyikan

## Notes

- Menggabungkan TC-GS-POS-159 s.d. 164.
