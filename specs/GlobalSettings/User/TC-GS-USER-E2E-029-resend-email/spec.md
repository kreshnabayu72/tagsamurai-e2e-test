---
id: TC-GS-USER-E2E-029-resend-email
title: Kirim ulang email aktivasi dan konfirmasi
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-56
  - TC-GS-USER-439
  - TC-GS-USER-95
  - TC-GS-USER-54
  - TC-GS-USER-57
  - TC-GS-USER-438
coverage:
  web: automated
---

# Kirim ulang email aktivasi dan konfirmasi

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- Mailbox uji yang bisa dibaca skrip untuk alamat email semua user di bawah
- User "Fajar Nugroho" berstatus Pending Activation
- User "Gita Permata" dan "Hadi Susanto" berstatus Pending Activation
- User "Lestari Dewi" berstatus Activated, tanpa Pending Email Change
- User "Kiki Amelia" berstatus Activated dengan Pending Email Change
- User "Indah Sari" dan "Joko Widodo" berstatus Activated dengan Pending Email Change
- Belum ada resend sebelumnya untuk user di atas, jadi tidak ada yang sedang dalam cooldown 60 detik
- Setiap user hanya dikirim sekali oleh spec ini, karena kirim ulang memasukkan user ke cooldown

## Test Steps

### Screening: kapan tombol Resend tampil

1. Buka menu row action pada baris "Lestari Dewi"
2. Verifikasi row action `Resend Activation Email` dan `Resend Confirmation Email` tidak tampil
3. Pilih baris "Hadi Susanto" (Pending Activation) dan "Lestari Dewi" (Activated) bersamaan
4. Verifikasi bulk action bar tidak menampilkan `Resend Activation Email`
5. Hapus seleksi lalu pilih baris "Indah Sari" dan "Joko Widodo" (keduanya Activated dengan Pending Email Change)
6. Verifikasi bulk action bar tidak menampilkan opsi kirim ulang konfirmasi email sama sekali
7. Hapus seleksi

### Resend aktivasi satu user

8. Klik row action `Resend Activation Email` pada baris "Fajar Nugroho"
9. Verifikasi request kirim ulang email terkirim
10. Verifikasi toast "Success, activation email has been sent." muncul
11. Verifikasi Activation Email diterima di mailbox "Fajar Nugroho"

### Resend konfirmasi satu user

12. Klik row action `Resend Confirmation Email` pada baris "Kiki Amelia"
13. Verifikasi toast "Success, confirmation email has been sent to Kiki Amelia." muncul
14. Verifikasi email konfirmasi baru diterima di alamat email baru "Kiki Amelia"

### Resend aktivasi massal

15. Pilih baris "Gita Permata" dan "Hadi Susanto" (keduanya Pending Activation)
16. Verifikasi bulk action bar menampilkan `Resend Activation Email`
17. Klik `Resend Activation Email` pada bulk action bar
18. Verifikasi toast "Success, activation email has been sent." muncul
19. Verifikasi Activation Email diterima di mailbox kedua user

## Notes

- Screening (langkah 1 sampai 7) ditaruh di awal karena tidak mengubah data. Tombol yang tersembunyi diuji sebelum kirim, supaya kondisi user belum berubah.
- Kirim ulang dalam masa cooldown 60 detik dicakup `TC-GS-USER-E2E-030-resend-cooldown`.
- Kegagalan server pada Resend (`TC-GS-USER-58`) dicakup spec hanya-FE (`Mode: mock`) yang dibuat kemudian.
- Nama row action mengikuti PRD `user.md` bagian 4.2 ("Resend Activation Email" dan "Resend Confirmation Email").
