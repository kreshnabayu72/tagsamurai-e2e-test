---
id: TC-AC-SU-E2E-020-resend-activation-email-row-action-cooldown-dan-template-email
title: "Row action Resend Activation Email, cooldown 60 detik, proteksi klik berulang, dan verifikasi template email"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-42
  - TC-AC-SU-43
  - TC-AC-SU-44
  - TC-AC-SU-47
  - TC-AC-SU-217
  - TC-AC-SU-286
coverage:
  web: automated
---

# Row action Resend Activation Email, cooldown 60 detik, proteksi klik berulang, dan verifikasi template email

## Prerequisites

- Login sebagai Role: Principal Total Control / Admin pemegang Update
- Terdapat target pengguna dengan status Pending Activation dan Default User Pending Activation

## Test Steps

### Akses Opsi Resend Activation Email dan Pengecualian Default User

1. Buka User List, temukan baris pengguna berstatus `Pending Activation`
2. Klik icon `[⋯]` pada kolom Actions, verifikasi opsi `Resend Activation Email` tersedia
3. Amati baris Default User yang berstatus Pending Activation
4. Buka row action Default User, verifikasi opsi `Resend Activation Email` tetap tampil dan DAPAT diklik (pengecualian dari guard Default User)

### Kirim Ulang Email dan Cooldown 60 Detik

1. Klik opsi `Resend Activation Email`
2. Verifikasi toast sukses muncul: `"Success, email has been sent."`
3. Verifikasi tombol row action tersebut otomatis berstatus Disabled dengan hover tooltip countdown `"Please wait {X} seconds before resending."` (menghitung mundur dari 60 detik ke 1 detik)
4. Coba klik kembali tombol tersebut selama masa cooldown <60 detik, verifikasi tombol tidak dapat diklik dan tidak ada request terkirim

### Verifikasi Konten Template Email dan Limit Harian

1. Inspeksi email aktivasi yang diterima di inbox penerima:
2.   - Subject: `"Activate your TAG Samurai account"`
3.   - Greeting: `"Hi [Full Name],"`
4.   - Body: `"An account has been created for you on TAG Samurai. Click the button below to set your password and activate your account."`
5.   - Tombol: `[Activate Account]`
6.   - Masa berlaku: `"This link is valid for 24 hours and can only be used once."`
7.   - Penutup: `"To keep your data secure, please don't forward this email to anyone..."` dan signoff `"— TAG Samurai"`
8. Tunggu hingga cooldown 60 detik habis, verifikasi tombol kembali Enabled dan email dapat dikirimkan ulang tanpa batasan kuota harian

## Notes

- Cooldown 60 detik mencegah spam pengiriman email aktivasi.
