---
id: TC-GS-USER-E2E-050-konfirmasi-email-invalidate-reset-password
title: Konfirmasi ganti email membatalkan token Reset Password lama
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-544
  - TC-GS-USER-174
  - TC-GS-USER-113
coverage:
  web: automated
---

# Konfirmasi ganti email membatalkan token Reset Password lama

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- User "Rudi Reset" berstatus Activated, tanpa Pending Email Change
- Mailbox uji yang bisa dibaca skrip untuk alamat email lama "Rudi Reset" dan alamat email barunya
- Token Reset Password aktif untuk alamat email lama, diminta lewat fitur lupa kata sandi sebelum admin mengubah email, dan belum kedaluwarsa atau dipakai
- Link konfirmasi dan link reset bisa dibuka skrip di sesi browser terpisah
- Spec ini memindahkan email "Rudi Reset" ke alamat baru, jadi datanya dibuat ulang oleh seeding sebelum run berikutnya

## Test Steps

1. Di sesi terpisah, buka halaman lupa kata sandi dan minta link Reset Password untuk alamat email lama "Rudi Reset"
2. Verifikasi email Reset Password diterima di mailbox alamat lama dan linknya aktif (belum dipakai)
3. Di sesi admin, klik row action `Edit` pada baris "Rudi Reset", ganti Email dengan alamat baru, lalu klik `[Save]`
4. Verifikasi email konfirmasi diterima di alamat baru dan badge "Pending Email Confirmation" tampil pada baris "Rudi Reset"
5. Di sesi terpisah, buka link konfirmasi dari email di alamat baru
6. Verifikasi konfirmasi berhasil dan email "Rudi Reset" resmi berpindah ke alamat baru di User List
7. Di sesi terpisah, buka link Reset Password yang diterbitkan untuk alamat email lama
8. Verifikasi link itu membuka halaman 404 (bukan halaman Setup New Password)
9. Buka lagi link konfirmasi yang sudah dipakai di langkah 5
10. Verifikasi link itu menghasilkan respons 410 dengan pesan "This confirmation link has expired or was already used." (bukan error 500)
11. Buka Changelog "Rudi Reset"
12. Verifikasi ada baris Action "Email Confirmed", Field "Email", Old email lama (pending), New email baru, dan Modified By "Rudi Reset" sendiri (bukan admin), satu-satunya kasus self-actor karena ini aksi user dan bukan aksi admin

## Notes

- Sesuai PRD `user.md` [F-USER-03]: begitu link konfirmasi diklik, modul User wajib memanggil Auth > Reset Password untuk membatalkan semua token Reset Password aktif milik email lama dalam transaksi yang sama dengan pergantian email.
- Cascade Auth lain pada transaksi yang sama (OTP aktif, biometric_credential) dimiliki Auth dan diverifikasi dari sisi Auth (`TC-AUTH-RST-112`, `TC-AUTH-MFA-38`, `TC-AUTH-SES-99`).
- Langkah 9 dan 10 mencakup varian token yang sudah dipakai untuk `TC-GS-USER-174`. Varian dibatalkan dicakup spec 025, dan varian kedaluwarsa dicakup spec 028.
- Link konfirmasi yang sudah dipakai menghasilkan 410 (PRD [F-USER-03], `GAP-275` sudah ditutup), sedangkan link Reset Password lama yang dibatalkan membuka halaman 404 (aturan modul Auth).
- Butuh mailbox uji untuk dua alamat dan alur lupa kata sandi yang bisa dijalankan skrip. Kebutuhan itu ditulis di Prerequisites untuk tim FE.
