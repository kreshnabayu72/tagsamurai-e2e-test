---
id: TC-GS-USER-E2E-028-email-token-kedaluwarsa
title: Token konfirmasi perubahan email kedaluwarsa
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-28
  - TC-GS-USER-174
coverage:
  web: automated
---

# Token konfirmasi perubahan email kedaluwarsa

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- Mailbox uji untuk alamat baru "Yuni Lestari" yang bisa dibaca skrip, dan linknya bisa dibuka
- User "Yuni Lestari" berstatus Activated, tanpa Pending Email Change, dan alamat email baru yang belum dipakai user lain
- Pemicu waktu yang disediakan tim FE: masa berlaku token konfirmasi perubahan email dipendekkan di environment ini, atau jam sistem bisa dimajukan, sehingga token bisa kedaluwarsa dalam waktu run
- Spec ini membuat Pending Email Change pada "Yuni Lestari" yang tidak dibatalkan, jadi datanya dibuat ulang oleh seeding sebelum run berikutnya

## Test Steps

1. Klik `Edit` pada baris "Yuni Lestari", ganti Email dengan alamat baru, lalu klik `[Save]`
2. Verifikasi badge "Pending Email Confirmation" muncul pada baris "Yuni Lestari" dan kolom Email masih menampilkan email lama
3. Picu kedaluwarsa token konfirmasi sesuai kebutuhan di Prerequisites
4. Buka link konfirmasi dari email di alamat baru
5. Verifikasi respons 410 dengan pesan "This confirmation link has expired or was already used." muncul (bukan 500 dan bukan konfirmasi sukses)
6. Muat ulang User List
7. Verifikasi badge "Pending Email Confirmation" pada baris "Yuni Lestari" tetap ada dan kolom Email tetap email lama
8. Klik row action `Resend Confirmation Email` pada baris "Yuni Lestari"
9. Verifikasi toast "Success, confirmation email has been sent to Yuni Lestari." muncul dan email konfirmasi baru diterima di alamat baru
10. Buka link dari email yang baru dan verifikasi link itu berlaku

## Notes

- Spec ini dipisah dari `TC-GS-USER-E2E-025-edit-email-pending-change` karena butuh pemicu waktu dan data Pending yang hanya sekali pakai.
- Setelah token kedaluwarsa, pending dan badge tetap ada sampai dikonfirmasi atau dibatalkan admin. Resend Confirmation memakai ulang baris pending yang sama dan memperpanjang masa berlaku 24 jam (PRD `user.md` [F-USER-03], `GAP-275` sudah ditutup). Link yang tidak lagi live menghasilkan 410, dan 404 hanya untuk token tak dikenal.
- Toast Resend Confirmation mengikuti `TC-GS-USER-57`.
- `TC-GS-USER-174` (link kedaluwarsa membuka halaman token tidak valid, bukan error 500) dicakup pada langkah 4 dan 5. Varian token yang sudah dipakai dicakup spec konfirmasi email berikutnya.
