---
id: TC-AUTH-ACT-E2E-003-trigger-activation-email-dari-gs-user
title: "Trigger Activation Email dari Global Settings > User, template email, snapshot nama, dan pembukaan link dari email"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-11
  - TC-AUTH-ACT-13
  - TC-AUTH-ACT-14
  - TC-AUTH-ACT-15
  - TC-AUTH-ACT-16
coverage:
  web: automated
---

# Trigger Activation Email dari Global Settings > User, template email, snapshot nama, dan pembukaan link dari email

## Prerequisites

- Login sebagai Total Control Global Settings (`Spectra.env.ADMIN_USERNAME` / `Spectra.env.ADMIN_PASSWORD`).
- Mailbox uji / mail-catcher lingkungan automation dapat dibaca untuk memverifikasi isi Activation Email.
- Nama dan email user dibuat unik per run oleh hook (`emailPrefix+<timestamp>+<rand>@qwertysystem.net`); data dibuat lewat UI Create User pada langkah pertama tiap blok.
- Akses API read-only untuk memverifikasi token Active, status Pending Activation, dan jumlah entri log.
- Tidak ada sesi lain yang memakai user target bersamaan dengan spec ini.

## Test Steps

### Membuat user memicu Activation Email dan link valid (TC-AUTH-ACT-11)

1. Buka `Global Settings > User > Login User`.
2. Klik button [+ User]; pada popup Create User isi First Name dan Last Name unik (hasil fixture), pilih Division, isi Email unik (hasil fixture), dan centang Access minimal satu produk, lalu klik [Submit].
3. Verifikasi user baru muncul pada tabel `Global Settings > User > Login User` dengan badge Pending Activation.
4. Buka inbox email user tersebut.
5. Verifikasi email dengan Subject "Activate your TAG Samurai account" diterima.
6. Verifikasi tidak ada entri pencatatan dari Auth untuk pembuatan token maupun pengiriman email.

### Isi email sesuai template platform (TC-AUTH-ACT-13)

7. Verifikasi body email menyapa "Hi <Full Name user>," dengan nama lengkap user.
8. Verifikasi body memuat kalimat "An account has been created for you on TAG Samurai. Click the button below to set your password and activate your account.".
9. Verifikasi tombol [Activate Account] tampil dengan link berformat `/activate?token={token}`.
10. Verifikasi body memuat kalimat "This link is valid for 24 hours and can only be used once.".
11. Verifikasi link teks mentah (versi URL mentah) tampil dengan URL yang sama dengan tombol [Activate Account] setelah kalimat "If the button doesn't work, click the link below or copy and paste it into your browser:".
12. Verifikasi body memuat kalimat "To keep your data secure, please don't forward this email to anyone. If you didn't create this account, just ignore this email." dan penutup "— TAG Samurai".

### Klik [Activate Account] membuka Set Password (TC-AUTH-ACT-14)

13. Klik tombol [Activate Account] pada email.
14. Verifikasi halaman `Auth > Account Activation > Set Password` tampil dengan subtitle "Set a password to log in for <email user>.".
15. Verifikasi halaman Invalid Link tidak tampil.

### Link teks mentah membuka Set Password (TC-AUTH-ACT-15)

16. Salin link teks mentah dari body email yang sama, lalu buka lewat address bar di tab baru.
17. Verifikasi halaman Set Password tampil dengan subtitle "Set a password to log in for <email user>.".

### Greeting memakai nama saat email dikirim (TC-AUTH-ACT-16)

18. Buat user kedua melalui popup Create User (nama dan email unik berbeda), lalu buka email aktivasi yang diterima.
19. Verifikasi greeting email berbunyi "Hi <Full Name user kedua>,".
20. Buka `Global Settings > User > Login User > Popup Edit User` untuk user kedua, ubah Last Name menjadi `Baru`, lalu klik [Save].
21. Buka kembali email aktivasi user kedua di inbox.
22. Verifikasi greeting email tetap "Hi <Full Name user kedua>," dan tidak berubah mengikuti nama baru.
23. Verifikasi user kedua pada Global Settings > User menampilkan nama yang sudah berubah, sedangkan statusnya tetap Pending Activation.

## Notes

- Kedua user dibuat lewat jalur yang sama (Global Settings > User), sehingga trigger, template, dan snapshot nama digabung dalam satu spec.
- Kebutuhan mailbox uji dan akses API dicatat di Prerequisites.
- Id TC disebut pada subjudul blok agar report per langkah dapat dipetakan ke TC granular.
