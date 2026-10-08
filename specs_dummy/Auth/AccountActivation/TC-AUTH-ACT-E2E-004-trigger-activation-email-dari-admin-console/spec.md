---
id: TC-AUTH-ACT-E2E-004-trigger-activation-email-dari-admin-console
title: "Trigger Activation Email dari Admin Console lewat pembuatan Client + Default User"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-12
coverage:
  web: automated
---

# Trigger Activation Email dari Admin Console lewat pembuatan Client + Default User

## Prerequisites

- Login sebagai Total Control Admin Console (`Spectra.env.ADMIN_USERNAME` / `Spectra.env.ADMIN_PASSWORD`) — akun berbeda dari spec Global Settings.
- Mailbox uji / mail-catcher lingkungan automation dapat dibaca.
- Nama Client, nama Default User, dan email dibuat unik per run oleh fixture (`emailPrefix+<timestamp>+<rand>@qwertysystem.net`).
- Akses API read-only untuk memverifikasi token Active dan status Pending Activation pada Default User.
- Spec ini berdiri sendiri karena memakai akun dan entitas (Client) berbeda dari spec trigger via Global Settings > User.

## Test Steps

### Membuat Client dengan Default User memicu Activation Email (TC-AUTH-ACT-12)

1. Login sebagai Total Control Admin Console, lalu buka Admin Console.
2. Jalankan alur pembuatan Client baru dengan nama unik (hasil fixture) dan Default User Name serta Email unik (hasil fixture), lalu selesaikan submit.
3. Verifikasi Client baru dan Default User terbentuk.
4. Buka inbox email Default User.
5. Verifikasi email dengan Subject "Activate your TAG Samurai account" diterima.
6. Verifikasi isi email memakai template identik dengan jalur Global Settings > User: greeting "Hi <Full Name Default User>,", kalimat instruksi pembuatan akun, tombol [Activate Account], kalimat "This link is valid for 24 hours and can only be used once.", link teks mentah dengan URL yang sama, closing paragraph, dan signoff "— TAG Samurai".
7. Verifikasi raw token pada link email memiliki panjang 43 karakter dan hanya terdiri dari alfabet `A-Za-z0-9-_`.

### Klik [Activate Account] membuka Set Password (TC-AUTH-ACT-12)

8. Klik tombol [Activate Account] pada email Default User.
9. Verifikasi halaman `Auth > Account Activation > Set Password` tampil dengan subtitle "Set a password to log in for <email Default User>.".
10. Verifikasi alur aktivasi identik dengan user buatan Global Settings > User (tidak ada halaman Invalid Link dan tidak ada perbedaan tampilan).
11. Verifikasi status Default User tetap Pending Activation dengan token Active.

## Notes

- Pembuatan Client dipisah dari spec Global Settings > User karena memakai akun Admin Console dan entitas Client yang berbeda (aturan pemisahan beda akun/entity).
- Kebutuhan mailbox uji dan akses API dicatat di Prerequisites.
- Data uji Client bersifat dinamis dan dibuat unik per run; pembersihan Client beserta Default User dilakukan di hook `after`.
