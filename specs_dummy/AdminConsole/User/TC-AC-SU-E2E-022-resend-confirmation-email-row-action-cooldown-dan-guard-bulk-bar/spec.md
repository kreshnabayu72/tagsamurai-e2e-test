---
id: TC-AC-SU-E2E-022-resend-confirmation-email-row-action-cooldown-dan-guard-bulk-bar
title: "Row action Resend Confirmation Email, cooldown 60 detik, verifikasi template email baru, dan guard tidak muncul di Bulk Bar"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-48
  - TC-AC-SU-49
  - TC-AC-SU-50
  - TC-AC-SU-51
  - TC-AC-SU-218
  - TC-AC-SU-292
coverage:
  web: automated
---

# Row action Resend Confirmation Email, cooldown 60 detik, verifikasi template email baru, dan guard tidak muncul di Bulk Bar

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat target pengguna Activated dengan alamat email baru yang menunggu konfirmasi (`pending_email` terisi)

## Test Steps

### Akses Opsi Resend Confirmation Email dan Detail User Badge

1. Buka User List, temukan baris pengguna dengan status Pending Email Confirmation
2. Buka row action `[⋯]`, verifikasi opsi `Resend Confirmation Email` tersedia
3. Buka halaman Detail User untuk pengguna tersebut
4. Verifikasi field Email memuat badge kuning `"Pending Email Confirmation"` berstatus read-only tanpa tombol Cancel (pembatalan hanya dari Global Settings)

### Kirim Ulang Email Konfirmasi dan Cooldown

1. Klik opsi `Resend Confirmation Email`
2. Verifikasi toast sukses muncul: `"Success, email has been sent."`
3. Verifikasi tombol row action Disabled dengan tooltip cooldown `"Please wait {X} seconds before resending."` (countdown 60 detik)
4. Inspeksi email yang diterima di alamat email BARU pengguna:
5.   - Subject: `"Confirm your new email address"`
6.   - Greeting: `"Hi [First Name],"`
7.   - Body: `"We received a request to change the email address on your TAG Samurai account to this one. Click the button below to confirm the change."`
8.   - Tombol: `[Confirm Email Change]`
9.   - Penjelasan: `"Your current email address will remain active until this change is confirmed."`
10.   - Signoff: `"— TAG Samurai"`

### Guard Ketiadaan Resend Confirmation di Bulk Action Bar

1. Kembali ke halaman User List
2. Centang beberapa checkbox pengguna termasuk pengguna Pending Email Confirmation
3. Amati Bulk Action Bar, verifikasi opsi `Resend Confirmation Email` TIDAK PERNAH tampil di Bulk Action Bar (bersifat row-only)

## Notes

- Resend Confirmation Email eksklusif tersedia sebagai row action baris tunggal.
