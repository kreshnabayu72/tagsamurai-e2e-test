---
id: TC-GS-USER-E2E-038-resend-activation-dan-confirmation-email-flow
title: "Resend Email: Kirim ulang email aktivasi dan konfirmasi single/bulk serta cooldown 60 detik"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-305
  - TC-GS-USER-306
  - TC-GS-USER-307
  - TC-GS-USER-308
  - TC-GS-USER-309
  - TC-GS-USER-310
  - TC-GS-USER-311
  - TC-GS-USER-312
  - TC-GS-USER-1046
coverage:
  web: automated
---

# Resend Email: Kirim ulang email aktivasi dan konfirmasi single/bulk serta cooldown 60 detik

## Prerequisites

- Login sebagai Role: Total Control
- User Lukman Hakim (Pending Activation) tersedia

## Test Steps

### Kirim Ulang Email dan Cooldown

1. Temukan baris Lukman Hakim, buka menu (⋯), klik 'Resend Activation Email'
2. Verifikasi toast sukses 'Activation email sent.' tampil
3. Coba klik 'Resend Activation Email' kembali seketika, verifikasi sistem memblokir pengiriman ulang dengan peringatan cooldown 60 detik
4. Pilih multiple user pending, verifikasi aksi Bulk Resend Email bekerja sesuai aturan kuota dan cooldown

## Notes

- Menggabungkan 9 test case granular (TC-GS-USER-305 s.d. TC-GS-USER-1046).
