---
id: TC-GS-USER-E2E-036-bulk-activate-dan-bulk-deactivate-flow
title: "Bulk Actions: Eksekusi Bulk Activate dan Bulk Deactivate dengan penanganan baris skip"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-291
  - TC-GS-USER-292
  - TC-GS-USER-293
  - TC-GS-USER-294
  - TC-GS-USER-295
  - TC-GS-USER-296
  - TC-GS-USER-297
  - TC-GS-USER-298
  - TC-GS-USER-299
  - TC-GS-USER-300
  - TC-GS-USER-301
  - TC-GS-USER-302
  - TC-GS-USER-303
  - TC-GS-USER-304
  - TC-GS-USER-1016
  - TC-GS-USER-1027
  - TC-GS-USER-1035
  - TC-GS-USER-1036
  - TC-GS-USER-1045
  - TC-GS-USER-1048
  - TC-GS-USER-1049
  - TC-GS-USER-1050
coverage:
  web: automated
---

# Bulk Actions: Eksekusi Bulk Activate dan Bulk Deactivate dengan penanganan baris skip

## Prerequisites

- Login sebagai Role: Total Control
- Seleksi campuran user aktif dan inaktif tersedia

## Test Steps

### Bulk Deactivate dengan Baris Ter-skip

1. Pilih beberapa user yang terdiri dari user aktif dan user yang sudah inaktif
2. Klik tombol 'Deactivate' pada Bulk Bar
3. Verifikasi dialog konfirmasi menampilkan ringkasan user yang akan dinonaktifkan dan daftar user yang di-skip
4. Klik '[Continue]' / '[Deactivate]'
5. Verifikasi toast sukses/ringkasan T-13/T-39 tampil dan seluruh user target menjadi Inactive

### Bulk Activate

6. Pilih beberapa user inaktif, klik 'Activate' pada Bulk Bar, konfirmasi aksi
7. Verifikasi seluruh user target kembali berstatus Active

## Notes

- Menggabungkan 22 test case granular (TC-GS-USER-291 s.d. TC-GS-USER-1050).
