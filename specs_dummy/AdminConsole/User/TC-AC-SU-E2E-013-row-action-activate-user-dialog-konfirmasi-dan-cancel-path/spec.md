---
id: TC-AC-SU-E2E-013-row-action-activate-user-dialog-konfirmasi-dan-cancel-path
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

- Login sebagai Role: Principal Total Control
- Terdapat pengguna dengan status Inactive (switch Active OFF)

## Test Steps

### Buka Dialog Konfirmasi dan Cancel Path

1. Buka halaman User List dan temukan baris pengguna yang berstatus Inactive (switch OFF)
2. Klik switch Active baris tersebut untuk menyalakannya (OFF → ON)
3. Verifikasi dialog konfirmasi terbuka dengan:
4.   - Title: `"Activate User"`
5.   - Body: bullet `[User Name]` serta kalimat `"This user will regain access to the portal. Are you sure you want to activate it?"`
6.   - Tombol: `[Cancel]` dan `[Activate]` (`severity="info"`, `confirmSeverity="primary"`)
7. Klik tombol `[Cancel]` pada dialog konfirmasi
8. Verifikasi dialog tertutup, switch Active tetap berada pada posisi OFF (Inactive), dan tidak ada request PATCH yang dikirimkan ke server

### Konfirmasi Aktivasi Sukses

1. Klik kembali switch Active baris tersebut (OFF → ON)
2. Klik tombol `[Activate]` pada dialog konfirmasi
3. Verifikasi request PATCH terkirim ke server dan status pengguna berubah menjadi `is_active = true`
4. Verifikasi switch Active berubah posisi menjadi ON (Active)
5. Verifikasi toast sukses muncul: `"Success, user has been activated."`

## Notes

- Aktivasi mengembalikan hak akses pengguna ke portal Admin Console.
