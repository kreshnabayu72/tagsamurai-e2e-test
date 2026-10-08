---
id: TC-GS-USER-E2E-034-bulk-action-bar-protokol-seleksi-dan-retensi
title: "Bulk Action Bar: Protokol seleksi checkbox header, baris, dan retensi filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-274
  - TC-GS-USER-275
  - TC-GS-USER-276
  - TC-GS-USER-277
  - TC-GS-USER-278
  - TC-GS-USER-279
  - TC-GS-USER-280
  - TC-GS-USER-281
  - TC-GS-USER-282
  - TC-GS-USER-283
  - TC-GS-USER-284
  - TC-GS-USER-285
coverage:
  web: automated
---

# Bulk Action Bar: Protokol seleksi checkbox header, baris, dan retensi filter

## Prerequisites

- Login sebagai Role: Total Control
- Tabel User List memuat banyak baris data

## Test Steps

### Seleksi Baris dan Tampilan Bulk Bar

1. Centang salah satu baris user, verifikasi Bulk Action Bar melayang muncul di bawah/atas tabel
2. Verifikasi Bulk Bar menampilkan counter '1 user selected' dan tombol aksi 'Activate', 'Deactivate', 'Delete'
3. Centang checkbox di header tabel, verifikasi seluruh baris pada halaman aktif tercentang
4. Klik teks 'Select all {N} users across all pages', verifikasi counter terupdate mencakup seluruh data
5. Klik 'Unselect All', verifikasi seluruh centang bersih dan Bulk Bar menghilang

## Notes

- Menggabungkan 12 test case granular (TC-GS-USER-274 s.d. TC-GS-USER-285).
