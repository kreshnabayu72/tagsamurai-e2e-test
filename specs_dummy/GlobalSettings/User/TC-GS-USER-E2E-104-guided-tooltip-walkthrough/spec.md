---
id: TC-GS-USER-E2E-104-guided-tooltip-walkthrough
title: 'Guided Tooltip User List: auto-trigger pertama, replay, navigasi, dan keluar tanpa selesai'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-185
  - TC-GS-USER-186
  - TC-GS-USER-187
  - TC-GS-USER-188
  - TC-GS-USER-189
  - TC-GS-USER-190
coverage:
  web: automated
---

# Guided Tooltip User List: auto-trigger pertama, replay, navigasi, dan keluar tanpa selesai

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client, akun yang belum pernah membuka halaman User (flag seen `gs-user` belum ada)
- Akun kedua dengan flag seen belum ada untuk uji keluar tanpa selesai
- Flag seen di-reset oleh seeding untuk kedua akun sebelum run
- Spec ini menetapkan flag seen akun pertama, jadi flag di-reset lagi oleh seeding sebelum run berikutnya

## Test Steps

### Kunjungan pertama

1. Login dengan akun pertama dan buka halaman User untuk pertama kali
2. Verifikasi walkthrough muncul otomatis dengan lima langkah: "Search & Filters" (target toolbar Search dan Filter), "Create User" (target `[+ User]`), "Active Toggle" (target kolom Toggle Active), "Access" (target kolom Access), "User Actions" (target kolom Row Action `[⋯]`)
3. Klik `Next` sampai langkah terakhir, lalu `Back` satu kali
4. Verifikasi `Back` dan `Next` berpindah langkah sesuai arah
5. Klik `Next` hingga langkah terakhir lalu klik `Done`
6. Verifikasi walkthrough tertutup dan flag seen ter-set

### Kunjungan berikutnya dan replay

7. Refresh halaman
8. Verifikasi walkthrough tidak muncul otomatis lagi
9. Klik ikon `[?]` untuk replay lalu klik `Skip` di langkah pertama
10. Verifikasi walkthrough tertutup kapan pun `Skip` diklik, dan refresh halaman tidak memunculkan walkthrough otomatis (replay tidak mereset flag seen)

### Keyboard

11. Klik `[?]` untuk memulai walkthrough, lalu tekan `Enter`, `Arrow Right`, dan `Arrow Left`
12. Verifikasi `Enter` dan `Arrow Right` maju ke langkah berikutnya dan `Arrow Left` mundur
13. Tekan `Esc`
14. Verifikasi walkthrough tertutup seperti `Skip`

### Keluar tanpa selesai

15. Login dengan akun kedua dan buka halaman User sehingga walkthrough muncul
16. Ubah ukuran jendela atau navigasi ke halaman lain tanpa menekan `Done` atau `Skip`
17. Kembali ke halaman User
18. Verifikasi walkthrough muncul otomatis lagi karena flag seen tidak ter-set oleh keluar tanpa selesai

## Notes

- Sumber `user.md` bagian 4.4 dan `foundation/functions/guided-tooltip.md`. Isi deskripsi tiap langkah mengikuti PRD; spec ini memverifikasi judul dan target.
- Pemulihan flag seen lewat seeding disediakan tim FE.
