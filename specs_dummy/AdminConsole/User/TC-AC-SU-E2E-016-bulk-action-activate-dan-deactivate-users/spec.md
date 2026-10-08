---
id: TC-AC-SU-E2E-016-bulk-action-activate-dan-deactivate-users
title: "Bulk Action Bar, Server Select All lintas halaman, toggle Unselect All, Bulk Activate dan Deactivate"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-37
  - TC-AC-SU-38
  - TC-AC-SU-214
  - TC-AC-SU-224
  - TC-AC-SU-225
  - TC-AC-SU-249
  - TC-AC-SU-287
  - TC-AC-SU-288
coverage:
  web: automated
---

# Bulk Action Bar, Server Select All lintas halaman, toggle Unselect All, Bulk Activate dan Deactivate

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat dataset ≥10 pengguna tersebar di beberapa halaman dengan status campuran (Active, Inactive, dan isActiveGlobal=false)

## Test Steps

### Interaksi Bulk Action Bar dan Seleksi Server Select All

1. Centang 1 baris checkbox pengguna, verifikasi Bulk Action Bar muncul dengan counter singular `"1 user selected"`
2. Centang 1 baris checkbox tambahan, verifikasi counter berubah menjadi plural `"N users selected"`
3. Klik tombol `"Select All ({N} records)"` pada Bulk Action Bar
4. Verifikasi seluruh pengguna eligible terseleksi lintas halaman dan tombol bertransisi menjadi `"Unselect All"`
5. Hapus centang pada 1 baris data, verifikasi tombol kembali bertransisi menjadi `"Select All ({N} records)"`
6. Klik icon `(✕)` pada Bulk Action Bar, verifikasi seluruh seleksi dilepas dan bar tertutup

### Eksekusi Bulk Activate dan Bulk Deactivate

1. Pilih beberapa pengguna berstatus Inactive, klik tombol `[Activate]` pada Bulk Action Bar
2. Verifikasi dialog konfirmasi `"Activate Users"` terbuka memuat daftar bullet nama pengguna terpilih
3. Klik `[Cancel]`, verifikasi dialog tertutup dan tidak ada status yang berubah
4. Klik kembali `[Activate]`, klik konfirmasi `[Activate]`, verifikasi seluruh pengguna terpilih berhasil diaktifkan
5. Pilih beberapa pengguna berstatus Active (termasuk 1 pengguna dengan `isActiveGlobal=false`), klik tombol `[Deactivate]` pada Bulk Action Bar
6. Verifikasi dialog konfirmasi `"Deactivate Users"` terbuka memuat daftar nama pengguna terpilih
7. Klik konfirmasi `[Deactivate]`, verifikasi pengguna eligible berhasil dinonaktifkan, pengguna `isActiveGlobal=false` di-skip, dan toast partial muncul: `"N users updated, M failed."`

## Notes

- Bulk action mendukung eksekusi parsial dengan laporan ringkasan pada toast notification.
