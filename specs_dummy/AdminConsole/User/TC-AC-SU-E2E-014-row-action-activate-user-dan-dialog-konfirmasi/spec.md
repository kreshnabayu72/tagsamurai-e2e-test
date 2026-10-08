---
id: TC-AC-SU-E2E-014-row-action-activate-user-dan-dialog-konfirmasi
title: "Aktivasi user baris tunggal (OFF ke ON), dialog konfirmasi info, Cancel path, dan aktivasi sukses"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-26
  - TC-AC-SU-223
coverage:
  web: automated
---

# Aktivasi user baris tunggal (OFF ke ON), dialog konfirmasi info, Cancel path, dan aktivasi sukses

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat target pengguna bernama `"User Inactive Target"` dengan switch Active berstatus OFF (Inactive)

## Test Steps

### Trigger Dialog Konfirmasi Aktivasi & Jalur Batal
1. Buka halaman `Settings > User`
2. Temukan baris `"User Inactive Target"` dengan switch Active posisi OFF
3. Klik switch Active untuk menyalakan akses (OFF → ON)
4. Verifikasi muncul modal konfirmasi aktivasi dengan `severity="info"`
5. Verifikasi teks judul dialog adalah `"Activate User"` dan body dialog memuat pertanyaan eksplisit: `"Are you sure you want to activate User Inactive Target?"`
6. Klik tombol `[Cancel]` pada dialog konfirmasi
7. Verifikasi dialog tertutup, switch Active tetap berada di posisi OFF, dan status pengguna tidak berubah di backend

### Eksekusi Konfirmasi Aktivasi Sukses
8. Klik kembali switch Active pada baris tersebut (OFF → ON)
9. Pada dialog konfirmasi yang muncul, klik tombol konfirmasi primer `[Activate]`
10. Verifikasi switch Active beralih visual ke posisi ON
11. Verifikasi muncul toast sukses dengan pesan literal: `"Success, User Inactive Target has been activated."`
12. Refresh halaman dan verifikasi switch Active tetap berada di posisi ON

## Notes

- Aktivasi baris tunggal selalu memunculkan dialog konfirmasi sebelum mutasi dijalankan.
