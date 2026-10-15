---
id: TC-GS-POS-E2E-021-delete-single-position-happy-path-dan-satu-satunya-jabatan
title: "Delete single Position bebas relasi berhasil, Cancel dialog, guard double-click, dan delete record terakhir"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-111
  - TC-GS-POS-112
  - TC-GS-POS-113
  - TC-GS-POS-120
  - TC-GS-POS-122
  - TC-GS-POS-299
coverage:
  web: automated
---

# Delete single Position bebas relasi berhasil, Cancel dialog, guard double-click, dan delete record terakhir

## Prerequisites

- Login sebagai Role: Total Control
- Record Position "Temporary Staff" (bebas relasi) tersedia
- Entitas dengan 1 record tunggal tersedia untuk pengujian batas

## Test Steps

### Screening Dialog Delete & Cancel

1. Buka menu ⋯ pada baris "Temporary Staff", klik "Delete"
2. Verifikasi dialog konfirmasi Delete Position muncul menampilkan nama "Temporary Staff", tombol "[Cancel]", dan tombol "[Delete]"
3. Verifikasi focus trap aktif di dalam dialog dan tombol Esc menutup dialog
4. Buka kembali dialog Delete, lalu klik tombol "[Cancel]"
5. Verifikasi dialog tertutup dan record "Temporary Staff" tetap ada di tabel

### Delete Sukses & Guard Double-Click

6. Buka kembali dialog Delete untuk "Temporary Staff"
7. Klik tombol "[Delete]" secara cepat dua kali berturut-turut
8. Verifikasi tombol masuk ke loading state dan permintaan hanya diproses satu kali
9. Verifikasi toast sukses "Success, position has been deleted." muncul dan record hilang dari tabel

### Delete Record Terakhir di Entitas

10. Buka entitas yang hanya memiliki tepat 1 record Position tersisa
11. Buka dialog Delete dan konfirmasi hapus record tersebut
12. Verifikasi penghapusan diizinkan (tidak diblokir oleh guard last-item) dan tabel kini menampilkan empty state

## Notes

- Menggabungkan TC-GS-POS-111, 112, 113, 120, 122, dan 299.
