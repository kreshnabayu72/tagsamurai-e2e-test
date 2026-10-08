---
id: TC-GS-USER-E2E-030-resend-cooldown
title: Kirim ulang email diblokir selama cooldown 60 detik
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-55
  - TC-GS-USER-463
coverage:
  web: automated
---

# Kirim ulang email diblokir selama cooldown 60 detik

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- User "Lukman Hakim", "Maya Anggraini", dan "Nina Kartika" berstatus Pending Activation dan belum pernah dikirimi ulang email (tidak sedang cooldown)
- Kondisi cooldown dibuat oleh spec ini sendiri dengan mengirim ulang lalu langsung mencoba lagi
- Spec ini menunggu sekitar 60 detik untuk memastikan tombol aktif kembali. Bila tim FE menyediakan cara mempercepat cooldown, tuliskan di sini

## Test Steps

### Cooldown pada satu user

1. Klik row action `Resend Activation Email` pada baris "Lukman Hakim"
2. Verifikasi toast "Success, activation email has been sent." muncul
3. Segera hover tombol Resend pada baris "Lukman Hakim"
4. Verifikasi tombol tetap menampilkan label aslinya dalam state disabled
5. Verifikasi tooltip "Please wait {X} seconds before resending." muncul dan hitungannya menghitung mundur dari 60

### Cooldown pada kirim massal (partial success)

6. Klik row action `Resend Activation Email` pada baris "Maya Anggraini"
7. Verifikasi toast "Success, activation email has been sent." muncul
8. Segera pilih "Maya Anggraini" dan "Nina Kartika" (keduanya Pending Activation)
9. Klik `Resend Activation Email` pada bulk action bar
10. Verifikasi toast "1 email(s) sent. 1 skipped — conditions not met." muncul
11. Verifikasi checkbox seleksi otomatis dikosongkan
12. Verifikasi email aktivasi terkirim hanya ke "Nina Kartika" (tidak ada email kedua ke "Maya Anggraini")
13. Buka Changelog, System Log, dan Activity Log
14. Verifikasi ketiganya hanya mencatat entri kirim ulang untuk "Nina Kartika", dan tidak ada entri untuk "Maya Anggraini" dari kirim massal ini

### Cooldown berakhir

15. Tunggu sampai 60 detik sejak langkah 1 berlalu
16. Verifikasi tombol Resend pada baris "Lukman Hakim" aktif kembali dan tooltip cooldown hilang

## Notes

- Spec ini dipisah dari `TC-GS-USER-E2E-029-resend-email` karena butuh user yang sedang berada dalam kondisi cooldown (prinsip 12 di `docs/e2e-conventions.md` bagian 3).
- Kirim massal dengan sebagian user dalam cooldown menurut `TC-GS-USER-463`: user yang eligible diproses, yang dalam cooldown dilewati di sisi server, dan respons melaporkan jumlah terkirim dan dilewati.
- Langkah 15 dan 16 ditaruh paling akhir supaya waktu tunggu 60 detik berjalan sambil langkah 6 sampai 14 dikerjakan.
