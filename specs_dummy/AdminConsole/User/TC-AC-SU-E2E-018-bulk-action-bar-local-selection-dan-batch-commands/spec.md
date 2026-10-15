---
id: TC-AC-SU-E2E-018-bulk-action-bar-local-selection-dan-batch-commands
title: "Bulk Action Bar Interaksi Lokal, Counter Dinamis, dan Batch Commands"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-37
  - TC-AC-SU-38
  - TC-AC-SU-224
  - TC-AC-SU-225
  - TC-AC-SU-287
  - TC-AC-SU-288
coverage:
  web: automated
---

# Bulk Action Bar Interaksi Lokal, Counter Dinamis, dan Batch Commands

## Prerequisites

- Login sebagai Total Control
- Halaman User List memuat beberapa pengguna aktif dan inaktif

## Test Steps

### Pemilihan Baris dan Penampilan Bulk Action Bar
1. Buka `Admin Console > Settings > User`
2. Centang checkbox pada baris user 1
3. Verifikasi `Bulk Action Bar` melayang (floating dock) muncul di bagian bawah layar
4. Verifikasi teks counter menampilkan: `"1 User Selected"`
5. Centang checkbox pada baris user 2 dan baris user 3
6. Verifikasi teks counter berubah menjadi bentuk jamak: `"3 Users Selected"`

### Interaksi Tombol Batch dan Dismiss
7. Verifikasi tombol batch action yang tersedia: `[Assign to Group Role]`, `[Activate User]`, `[Deactivate User]`
8. Klik tombol `[Deactivate User]` pada Bulk Action Bar
9. Verifikasi muncul dialog konfirmasi bulk berisikan daftar nama user terpilih dalam bullet list
10. Klik tombol `[Cancel]` pada dialog; verifikasi dialog tertutup dan seleksi baris tetap terjaga
11. Klik tombol `✕` atau `[Deselect All]` pada Bulk Action Bar
12. Verifikasi seluruh centang checkbox terlepas dan Bulk Action Bar menghilang dari tampilan layar

## Notes

Menjamin kelancaran interaksi seleksi massal di tingkat halaman lokal.
