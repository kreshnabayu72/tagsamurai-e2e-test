---
id: TC-AC-SU-E2E-014-row-action-deactivate-user-dialog-konfirmasi-force-logout-dan-a11y
title: "Deaktivasi user baris tunggal (ON ke OFF), dialog konfirmasi danger, focus trap a11y, Cancel path, dan force logout"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-27
  - TC-AC-SU-28
  - TC-AC-SU-29
  - TC-AC-SU-291
coverage:
  web: automated
---

# Deaktivasi user baris tunggal (ON ke OFF), dialog konfirmasi danger, focus trap a11y, Cancel path, dan force logout

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat target pengguna dengan status Active yang sedang memiliki sesi login aktif di peramban lain

## Test Steps

### Buka Dialog Konfirmasi Deaktivasi dan Uji Aksesibilitas

1. Buka halaman User List dan temukan baris pengguna yang berstatus Active (switch ON)
2. Klik switch Active baris tersebut untuk mematikannya (ON → OFF)
3. Verifikasi dialog konfirmasi terbuka dengan:
4.   - Title: `"Deactivate User"`
5.   - Body: bullet `[User Name]` serta kalimat `"This user will lose portal access immediately. Any active sessions will be ended. Are you sure you want to deactivate it?"`
6.   - Tombol: `[Cancel]` dan `[Deactivate]` (`severity="danger"`, `confirmSeverity="danger"`)
7. Tekan tombol `Tab` pada keyboard secara berulang, verifikasi fokus keyboard tetap terkunci (focus trap) di dalam elemen dialog
8. Tekan tombol `Esc` pada keyboard
9. Verifikasi dialog tertutup setara klik `[Cancel]`, switch tetap ON, dan tidak ada perubahan data

### Konfirmasi Deaktivasi dan Force Logout Target Sesi

1. Klik kembali switch Active baris tersebut (ON → OFF)
2. Klik tombol `[Deactivate]` pada dialog konfirmasi
3. Verifikasi status pengguna berubah menjadi `is_active = false` dan switch Active berubah menjadi OFF
4. Verifikasi toast sukses muncul: `"Success, user has been deactivated."`
5. Amati sesi login peramban target pengguna tersebut
6. Verifikasi sesi login target pengguna seketika diterminasi (force logout) dan diarahkan ke halaman login dengan notifikasi `"Your session has been ended..."`

## Notes

- Deaktivasi akun seketika memutus seluruh sesi aktif pengguna demi keamanan akses.
