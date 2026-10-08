---
id: TC-AC-SU-E2E-023-row-action-resend-activation-mail-cooldown-timer-ui
title: "Row Action Resend Activation Email dan Cooldown Timer UI 60 Detik"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-42
  - TC-AC-SU-43
  - TC-AC-SU-44
  - TC-AC-SU-47
  - TC-AC-SU-286
coverage:
  web: automated
---

# Row Action Resend Activation Email dan Cooldown Timer UI 60 Detik

## Prerequisites

- Login sebagai Total Control
- Terdapat user dengan status Not Activated (Pending Activation)

## Test Steps

### Eksekusi Row Action Resend Activation
1. Buka `Admin Console > Settings > User`
2. Temukan user dengan badge status `Not Activated`
3. Klik tombol menu baris `[...]`
4. Verifikasi opsi menu `Resend Activation Email` dalam keadaan aktif (enabled)
5. Klik opsi `Resend Activation Email`
6. Verifikasi toast sukses muncul: `"Activation email has been resent successfully."`

### Verifikasi Cooldown Timer 60 Detik
7. Buka kembali menu baris `[...]` pada user yang sama seketika
8. Verifikasi opsi `Resend Activation Email` berada dalam kondisi `disabled`
9. Verifikasi terdapat teks hitung mundur atau tooltip: `"Please wait 60s before resending"`
10. Coba lakukan klik pada opsi yang disabled; verifikasi tidak ada request network baru yang dikirimkan (anti-spam)
11. Tunggu hingga timer 60 detik selesai; verifikasi opsi menu `Resend Activation Email` kembali berstatus aktif

## Notes

Memastikan guard anti-spam email aktivasi berjalan optimal di sisi UI.
