---
id: TC-AC-SU-E2E-013-user-list-state-preservation-dan-pagination-controls
title: "Persistensi state filter dan search saat tab switching dan refresh F5, pagination page size, serta Clear Filter"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-232
  - TC-AC-SU-233
  - TC-AC-SU-281
  - TC-AC-SU-282
  - TC-AC-SU-283
  - TC-AC-SU-284
coverage:
  web: automated
---

# Persistensi state filter dan search saat tab switching dan refresh F5, pagination page size, serta Clear Filter

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat > 50 data pengguna untuk pengujian paginasi

## Test Steps

### Persistensi State Search & Filter (Tab Switching & Refresh)
1. Buka halaman `Settings > User`
2. Ketik `"John"` pada kotak Search toolbar dan terapkan filter status `"Active"`
3. Klik salah satu nama pengguna untuk berpindah ke halaman Detail User
4. Klik tombol navigasi Back pada browser atau breadcrumb untuk kembali ke User List
5. Verifikasi keyword `"John"` dan filter status `"Active"` tetap tersimpan dan tabel tetap menampilkan hasil saringan yang sama
6. Tekan tombol `F5` untuk me-refresh halaman browser
7. Verifikasi keyword Search dan kriteria Filter tetap dipertahankan dari sessionStorage

### Tombol Clear Filter
8. Klik tombol `[Clear Filter]` pada toolbar
9. Verifikasi seluruh kriteria saringan direset dan tabel kembali menampilkan daftar lengkap seluruh pengguna

### Kontrol Paginasi & Page Size
10. Amati kontrol paginasi di bawah tabel User List
11. Verifikasi default page size adalah 25 baris per halaman
12. Ubah page size dari 25 menjadi 50 baris per halaman
13. Verifikasi tabel me-reload data dan menampilkan 50 baris
14. Navigasi ke halaman ke-2 via kontrol pagination
15. Verifikasi data halaman ke-2 dimuat dengan nomor urut yang sesuai
16. Refresh halaman browser dan verifikasi posisi page size 50 tetap dipertahankan

## Notes

- State pencarian dan saringan disimpan di sessionStorage per tab per halaman.
