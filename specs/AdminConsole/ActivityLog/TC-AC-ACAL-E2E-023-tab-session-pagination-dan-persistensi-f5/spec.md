---
id: TC-AC-ACAL-E2E-023-tab-session-pagination-dan-persistensi-f5
title: "Tab Session — Penggantian Page Size, navigasi Next/Prev, dan retensi state filter saat reload F5"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-16
  - TC-AC-ACAL-124
  - TC-AC-ACAL-125
  - TC-AC-ACAL-126
  - TC-AC-ACAL-127
  - TC-AC-ACAL-265
coverage:
  web: automated
---

# Tab Session — Penggantian Page Size, navigasi Next/Prev, dan retensi state filter saat reload F5

## Prerequisites

- Login sebagai Role: Principal Total Control
- Tab Session terisi minimal 26 baris data

## Test Steps

### Pagination Default & Page Size

1. Buka menu `Admin Console > Activity Log` (Tab Session)
2. Verifikasi komponen pagination di bawah tabel aktif menampilkan default 10 baris per halaman
3. Verifikasi opsi dropdown rows-per-page memuat: `10`, `25`, `50`, `100`
4. Pilih opsi `25` baris per halaman
5. Verifikasi tabel me-render hingga 25 baris secara bersamaan

### Navigasi Next & Prev

6. Pilih kembali opsi `10` baris per halaman
7. Klik tombol `[Next →]`
8. Verifikasi tabel berpindah ke halaman 2 menampilkan data urutan ke 11-20
9. Klik tombol `[← Prev]`
10. Verifikasi tabel kembali ke halaman 1

### Retensi State Filter & Reset Page Saat F5

11. Masukkan keyword search `"john"` dan pilih filter Division `"Finance"`
12. Klik tombol `[Next →]` untuk berpindah ke halaman 2 hasil pencarian
13. Lakukan refresh halaman browser (F5)
14. Verifikasi keyword Search `"john"` dan filter Division `"Finance"` tetap terpasang aktif di input (state tersimpan di sessionStorage)
15. Verifikasi tabel tetap menampilkan data tersaring yang cocok, namun nomor halaman otomatis reset kembali ke halaman 1

## Notes

- Sesuai konvensi platform, state pencarian dan filter dipertahankan saat refresh, sedangkan posisi nomor halaman selalu di-reset ke 1.
