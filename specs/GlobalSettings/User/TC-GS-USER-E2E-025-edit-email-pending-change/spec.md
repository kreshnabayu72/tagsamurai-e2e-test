---
id: TC-GS-USER-E2E-025-edit-email-pending-change
title: Ubah email user dan alur Pending Email Change
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-403
  - TC-GS-USER-350
  - TC-GS-USER-27
  - TC-GS-USER-404
  - TC-GS-USER-349
  - TC-GS-USER-479
  - TC-GS-USER-421
  - TC-GS-USER-430
  - TC-GS-USER-477
coverage:
  web: automated
---

# Ubah email user dan alur Pending Email Change

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- Mailbox uji yang bisa dibaca otomatis oleh skrip (subject, isi, dan link di email), dengan alamat berikut yang semuanya milik automation:
  - alamat awal "Eka Prasetyo"
  - alamat baru "Eka Prasetyo"
  - alamat awal "Lina Marlina"
  - alamat baru pertama dan alamat baru kedua "Lina Marlina"
- Link konfirmasi di email bisa dibuka oleh skrip
- User "Eka Prasetyo" berstatus Pending Activation dan dibuat lewat seeding sebelum spec, sehingga Activation Email sudah terkirim ke alamat awalnya
- User "Lina Marlina" berstatus Activated, tanpa Pending Email Change
- Spec ini mengubah email kedua user, jadi datanya dibuat ulang oleh seeding sebelum run berikutnya

## Test Steps

### Isi Activation Email

1. Buka Activation Email di mailbox "Eka Prasetyo"
2. Verifikasi subject "Activate your TAG Samurai account"
3. Verifikasi isi memuat greeting "Hi Eka Prasetyo,", kalimat "An account has been created for you on TAG Samurai. Click the button below to set your password and activate your account.", tombol `[Activate Account]`, kalimat "This link is valid for 24 hours and can only be used once.", fallback link mentah, paragraf penutup "To keep your data secure, please don't forward this email to anyone. If you didn't create this account, just ignore this email.", dan penutup "— TAG Samurai"

### Ubah email user Pending Activation

4. Klik `Edit` pada baris "Eka Prasetyo", ganti Email dengan alamat baru "Eka Prasetyo", lalu klik `[Save]`
5. Verifikasi email langsung berubah di baris "Eka Prasetyo" tanpa alur konfirmasi
6. Verifikasi tidak ada badge "Pending Email Confirmation" pada baris tersebut
7. Verifikasi Activation Email (bukan Confirmation Email) diterima di alamat baru "Eka Prasetyo"

### Ubah email user Activated

8. Klik `Edit` pada baris "Lina Marlina", ganti Email dengan alamat baru pertama, lalu klik `[Save]`
9. Verifikasi toast "Confirmation email sent to new address." muncul
10. Verifikasi badge "Pending Email Confirmation" muncul pada baris "Lina Marlina" dan kolom Email masih menampilkan alamat awal
11. Buka Confirmation Email di alamat baru pertama
12. Verifikasi subject "Confirm your new email address"
13. Verifikasi isi memuat greeting "Hi Lina,", kalimat "We received a request to change the email address on your TAG Samurai account to this one. Click the button below to confirm the change.", tombol `[Confirm Email Change]`, kalimat "Your current email address will remain active until this change is confirmed.", paragraf penutup "If you didn't request this change, you can safely ignore this email — no changes will be made.", dan penutup "— TAG Samurai"

### Email diubah lagi sebelum konfirmasi

14. Klik `Edit` pada "Lina Marlina", ganti Email dengan alamat baru kedua, lalu klik `[Save]`
15. Buka link konfirmasi lama (dari email di alamat baru pertama)
16. Verifikasi link lama membuka halaman 404 (tidak valid)
17. Verifikasi badge "Pending Email Confirmation" masih ada dan hanya link dari alamat baru kedua yang berlaku

### Menutup modal saat Pending Email Change

18. Klik `Edit` pada "Lina Marlina" dan ubah satu field lain
19. Klik `✕`, lalu klik `[Leave]` pada dialog "You have unsaved changes. Are you sure you want to leave?"
20. Verifikasi modal tertutup dan badge "Pending Email Confirmation" masih ada
21. Klik `Edit` pada "Lina Marlina" lagi
22. Verifikasi label "Pending email change to [alamat baru kedua]" dan tombol `[Cancel]` inline tampil di bawah field Email

### Membatalkan Pending Email Change

23. Klik `[Cancel]` inline di sebelah label
24. Verifikasi dialog "Cancel pending email change? The email will revert to [alamat awal]." muncul dengan tombol `[Go Back]` dan `[Cancel Change]`
25. Klik `[Go Back]`
26. Verifikasi dialog tertutup, label dan tombol `[Cancel]` inline tetap tampil, tidak ada toast, dan tidak ada entri Changelog baru
27. Klik `[Cancel]` inline lagi, lalu klik `[Cancel Change]`
28. Verifikasi toast "Success, pending email change has been canceled." muncul, dialog tertutup, modal Edit tetap terbuka, label dan tombol `[Cancel]` inline hilang, dan field Email kembali normal
29. Buka link konfirmasi dari email di alamat baru kedua
30. Verifikasi link membuka halaman 404 token tidak valid (bukan 500 dan bukan konfirmasi sukses)
31. Verifikasi Changelog, System Log, dan Activity Log masing-masing mencatat "Cancel Email Change" dengan Modified By admin yang login

## Notes

- Kasus pembatalan (langkah 23 sampai 31) ditaruh paling akhir karena setelah dibatalkan state Pending Email Change hilang dan tidak bisa dipakai kasus lain.
- Isi Activation Email (`TC-GS-USER-403`) diperiksa dari email user seeding yang dibuat lewat API, supaya tidak menumpang pada spec Create. Template email yang sama juga dikirim ulang pada langkah 7.
- Kedaluwarsa token (`TC-GS-USER-28`) butuh pemicu waktu dan dicakup `TC-GS-USER-E2E-028-email-token-kedaluwarsa`.
- Kegagalan server saat membatalkan Pending Email Change (`TC-GS-USER-559`) dicakup spec hanya-FE (`Mode: mock`) yang dibuat kemudian.
- Teks badge di baris adalah "Pending Email Confirmation" dan label di bawah field Email pada modal Edit adalah "Pending email change to [new email]", keduanya sesuai PRD (`user.md` bagian 4.1 dan 4.2). `tc-user.md` sudah diselaraskan pada 2026-09-30.
- Toast di langkah 9 mengikuti `TC-GS-USER-27`. PRD hanya mendefinisikan toast Edit standar "Success, user has been updated." dan tidak menyebut toast khusus untuk perubahan email, sehingga dicatat sebagai `GAP-276`. Langkah 9 disesuaikan bila PRD diputuskan.
- Klik link di email dan pembacaan mailbox butuh kemampuan teknis dari tim FE (dicatat di Prerequisites).
