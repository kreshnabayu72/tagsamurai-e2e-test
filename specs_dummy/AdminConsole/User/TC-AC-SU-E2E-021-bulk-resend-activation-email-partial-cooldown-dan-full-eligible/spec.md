---
id: TC-AC-SU-E2E-021-bulk-resend-activation-email-partial-cooldown-dan-full-eligible
title: "Bulk Resend Activation Email: partial skip non-pending, partial skip cooldown, dan sukses homogen"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-46
  - TC-AC-SU-258
  - TC-AC-SU-289
coverage:
  web: automated
---

# Bulk Resend Activation Email: partial skip non-pending, partial skip cooldown, dan sukses homogen

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat kumpulan pengguna Pending Activation (sebagian dalam cooldown 60s) dan Activated

## Test Steps

### Bulk Resend Seleksi Campuran (Skip Non-Pending)

1. Pilih seleksi campuran baris pengguna Pending Activation dan Activated di User List
2. Klik tombol `[Resend Activation Email]` pada Bulk Action Bar
3. Verifikasi hanya pengguna Pending Activation yang diproses kirim email
4. Verifikasi toast partial muncul: `"Success, email has been sent. Some items were skipped."`

### Bulk Resend Seleksi Homogen dengan Pengguna dalam Cooldown

1. Pilih 2 pengguna Pending Activation di mana 1 pengguna baru saja dikirim email (<60 detik yang lalu)
2. Klik tombol `[Resend Activation Email]` pada Bulk Action Bar
3. Verifikasi pengguna yang berada dalam masa cooldown di-skip oleh server, dan toast partial muncul: `"Success, email has been sent. Some items were skipped."`

### Bulk Resend Seleksi Homogen Seluruhnya Eligible

1. Pilih beberapa pengguna Pending Activation yang seluruhnya berada di luar masa cooldown
2. Klik tombol `[Resend Activation Email]` pada Bulk Action Bar
3. Verifikasi seluruh email terkirim dan toast sukses standar muncul: `"Success, email has been sent."` (tanpa keterangan skipped)

## Notes

- Bulk resend activation email mengeksekusi pengiriman secara aman dengan mengabaikan data non-eligible.
