---
id: TC-GS-DIV-E2E-029-delete-single-happy-path-record-aman
title: "Penghapusan Divisi Tunggal Bebas Relasi Berhasil"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-42
coverage:
  web: automated
---

# Penghapusan Divisi Tunggal Bebas Relasi Berhasil

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat data divisi aman 'Finance' yang tidak direferensikan oleh pengguna manapun

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Klik menu row action (⋯) pada baris 'Finance' lalu klik 'Delete'
3. Pada dialog konfirmasi 'Delete Division', klik tombol '[Delete]'
4. Verifikasi toast sukses muncul: 'Success, division has been deleted.'
5. Verifikasi baris 'Finance' hilang dari tabel utama
6. Buka form Create User pada tab User List dan periksa opsi dropdown Division
7. Verifikasi opsi 'Finance' sudah tidak tersedia lagi di dropdown

## Notes

- Membuktikan alur hapus divisi bebas relasi sukses sesuai division.md §9.2 [F-DIV-04].
