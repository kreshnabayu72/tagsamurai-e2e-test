---
id: TC-AC-SU-E2E-026-resend-emails-mail-catcher-payload-dan-token-inspection
title: "Verifikasi Payload Email Aktivasi dan Konfirmasi via Mail-Catcher API"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-217
  - TC-AC-SU-218
coverage:
  web: automated
---

# Verifikasi Payload Email Aktivasi dan Konfirmasi via Mail-Catcher API

## Prerequisites

- Service mock mail-catcher (MailHog / Inbucket) terhubung pada environment pengujian
- Login sebagai Total Control

## Test Steps

### Inspeksi Email Aktivasi Akun
1. Buka `Admin Console > Settings > User`
2. Lakukan Resend Activation Email pada user target `user.pending@example.com`
3. Panggil API mail-catcher untuk membaca pesan email masuk terbaru
4. Verifikasi subject email verbatim: `"[TAG Samurai] Activate Your Account"`
5. Verifikasi penerima email adalah `user.pending@example.com`
6. Verifikasi body email memuat tombol/tautan aktivasi dengan token URL kriptografis baru

### Inspeksi Email Konfirmasi Perubahan Email
7. Lakukan Resend Confirmation Email pada user `user.change@example.com`
8. Panggil API mail-catcher untuk membaca pesan terbaru
9. Verifikasi subject email verbatim: `"[TAG Samurai] Confirm Your New Email Address"`
10. Verifikasi body email memuat tautan konfirmasi dengan token verifikasi yang valid dan unik

## Notes

Menjamin kelengkapan isi konten komunikasi email resmi sistem ke pengguna.
