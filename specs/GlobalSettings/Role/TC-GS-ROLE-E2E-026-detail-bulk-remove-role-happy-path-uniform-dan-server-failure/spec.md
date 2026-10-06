---
id: TC-GS-ROLE-E2E-026-detail-bulk-remove-role-happy-path-uniform-dan-server-failure
title: "Pencabutan Massal Role Assignment Sukses (Homogen Semua Aman) dan Ketahanan Terhadap Gagal Server"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-48
  - TC-GS-ROLE-51
coverage:
  web: automated
---

# Pencabutan Massal Role Assignment Sukses (Homogen Semua Aman) dan Ketahanan Terhadap Gagal Server

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia minimal 2 user target reguler ter-assign pada Detail role

## Test Steps

1. Buka Detail role pada Tab System
2. Centang 2 user target reguler yang aman (bebas status TC/RO)
3. Klik tombol [Remove] pada Bulk Action Bar
4. Pada dialog konfirmasi, klik tombol [Remove]
5. Verifikasi toast sukses muncul: "Success, users have been removed."
6. Verifikasi kedua user terpilih terhapus dari tabel Detail
7. Verifikasi Bulk Action Bar otomatis tertutup
8. Pilih user lain lalu lakukan Bulk Remove saat server disimulasikan gagal 500 (mode mock)
9. Verifikasi toast error muncul: "Error, failed to remove users." dan data tidak berubah

## Notes

- Pencabutan massal yang sukses memicu toast plural "Success, users have been removed." (toast-copy §10).
