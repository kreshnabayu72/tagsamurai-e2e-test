---
id: TC-GS-POS-E2E-004-pagination-dan-page-size-tabel-utama
title: "Pagination default 10 baris, navigasi halaman, dan opsi page size 10/25/50/100"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-10
  - TC-GS-POS-11
  - TC-GS-POS-12
coverage:
  web: automated
---

# Pagination default 10 baris, navigasi halaman, dan opsi page size 10/25/50/100

## Prerequisites

- Login sebagai Role: Total Control
- Tabel Position berisi antara 11 hingga 20 record aktif

## Test Steps

### Navigasi Halaman

1. Buka Global Settings > User > Position
2. Verifikasi halaman 1 menampilkan tepat 10 baris data
3. Klik tombol navigasi Next (>) pada kontrol pagination
4. Verifikasi tabel berpindah ke halaman 2 dan menampilkan sisa record (N - 10 baris) dengan urutan terusan A-Z
5. Klik tombol navigasi Prev (<) dan verifikasi tabel kembali ke halaman 1 dengan 10 record yang sama

### Input Langsung Nomor Halaman

6. Ketik angka "2" ke dalam input nomor halaman lalu tekan Enter
7. Verifikasi tabel langsung berpindah ke halaman 2

### Opsi Page Size

8. Buka dropdown pilihan ukuran halaman pada footer tabel
9. Verifikasi opsi dropdown berisi tepat "10 | 25 | 50 | 100" tanpa opsi "All"
10. Pilih opsi "25"
11. Verifikasi seluruh baris data (N record) kini tampil sekaligus dalam 1 halaman tunggal

## Notes

- Menggabungkan TC-GS-POS-10, 11, dan 12.
