---
id: TC-AC-SU-E2E-025-row-action-resend-confirmation-mail-cooldown-timer-ui
title: "Row Action Resend Confirmation Email, Cooldown 60 Detik, dan Guard Ketiadaan di Bulk Bar"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-48
  - TC-AC-SU-49
  - TC-AC-SU-50
  - TC-AC-SU-51
  - TC-AC-SU-292
coverage:
  web: automated
---

# Row Action Resend Confirmation Email, Cooldown 60 Detik, dan Guard Ketiadaan di Bulk Bar

## Prerequisites

- Login sebagai Total Control
- Terdapat user dengan status Waiting for Confirmation (perubahan email pending verifikasi)

## Test Steps

### Eksekusi Row Action Resend Confirmation Email
1. Buka `Admin Console > Settings > User`
2. Temukan user berstatus `Waiting for Confirmation`
3. Klik tombol menu baris `[...]`
4. Verifikasi opsi menu `Resend Confirmation Email` tersedia dan aktif
5. Klik opsi `Resend Confirmation Email`
6. Verifikasi toast sukses muncul: `"Confirmation email has been resent successfully."`

### Verifikasi Cooldown dan Guard Bulk Action Bar
7. Buka kembali menu baris `[...]`; verifikasi opsi `Resend Confirmation Email` disabled dengan indikator cooldown 60 detik
8. Centang checkbox baris user tsb untuk memunculkan Bulk Action Bar
9. Periksa seluruh tombol aksi pada Bulk Action Bar
10. Verifikasi tombol "Resend Confirmation Email" TIDAK PERNAH muncul di Bulk Action Bar (hanya didukung via row action perorangan sesuai PRD)

## Notes

Memverifikasi batas fungsionalitas email konfirmasi perubahan identitas.
