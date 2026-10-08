---
id: TC-AUTH-RST-E2E-017-larangan-password-sama-dengan-lama
title: "Penolakan password baru sama dengan password aktif saat ini"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-79
  - TC-AUTH-RST-123
coverage:
  web: automated
---

# Penolakan password baru sama dengan password aktif saat ini

## Prerequisites

- User belum login (guest); form Setup New Password terbuka dengan token valid untuk `budisantoso@qwertysystem.net`.
- Password aktif user saat ini adalah `QaReset!2026`.
- Admin pemantau log `superAdminGlobalSettings_automated_qaTeam1@qwertysystem.net` dapat melihat log.

## Test Steps

### Submit password identik dengan password aktif

1. Buka halaman Setup New Password untuk user Budi Santoso
2. Masukkan password yang sedang aktif saat ini "QaReset!2026" pada field Password
3. Verifikasi seluruh 6 butir checklist Password Policy tercentang (ikon centang hitam)
4. Masukkan kembali "QaReset!2026" pada field Confirm Password
5. Klik tombol [Reset Password]
6. Verifikasi server menolak pembaruan password
7. Verifikasi pesan penolakan "Password must be different from your old password" tampil di layar
8. Verifikasi password akun di database TIDAK berubah (tetap `QaReset!2026`)
9. Verifikasi token reset di database TIDAK dikonsumsi (masih berstatus `active`)

### Pencatatan audit log kegagalan

10. Buka Activity Log Session dan User Log menggunakan sesi admin
11. Verifikasi tercatat entri log baru dengan Activity "Reset Password", Status "Failed", dan Note "Password does not meet requirements"

### Penegakan aturan oleh server (Bypass UI Prevention)

12. Kirimkan HTTP POST langsung ke endpoint `/confirm` dengan payload password yang sama dengan password aktif
13. Verifikasi server merespons dengan error HTTP 422 dan penolakan `PASSWORD_SAME_AS_OLD` / policy
14. Verifikasi aturan penolakan password lama ditegakkan secara ketat di layer backend

## Notes

- Sesuai PRD §6 V-AUTHRST-08, §9.4.2 baris 29, dan keputusan NC-03, submit password yang sama dengan password lama ditolak server dengan pesan error spesifik dan dicatat pada audit log sebagai Failed dengan Note `"Password does not meet requirements"`.
- Token reset tetap dapat digunakan kembali untuk memasukkan password baru yang berbeda (`TC-AUTH-RST-76`).
