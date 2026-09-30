---
id: TC-GS-USER-E2E-049-aktivasi-akun-dampak-user
title: Status user berubah menjadi Activated setelah user mengaktifkan akunnya
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-419
coverage:
  web: automated
---

# Status user berubah menjadi Activated setelah user mengaktifkan akunnya

## Prerequisites

- Login sebagai Role: Total Control, entity Client
- User "Contractor Baru" berstatus Pending Activation, dan link aktivasinya ada di mailbox uji yang bisa dibaca skrip
- Halaman aktivasi (Set Password) bisa dibuka skrip di sesi browser terpisah
- Spec ini mengaktifkan akun "Contractor Baru", jadi datanya dibuat ulang oleh seeding sebelum run berikutnya

## Test Steps

1. Di User List, cari "Contractor Baru"
2. Verifikasi baris menampilkan badge "Pending Activation"
3. Buka link aktivasi dari email "Contractor Baru" di sesi browser terpisah
4. Isi kata sandi baru yang valid pada halaman Set Password lalu kirim
5. Verifikasi aktivasi berhasil di sesi terpisah itu
6. Kembali ke User List dan muat ulang halaman
7. Verifikasi badge "Pending Activation" pada "Contractor Baru" tidak lagi tampil
8. Buka User Detail "Contractor Baru"
9. Verifikasi badge "Pending Activation" tidak tampil di Detail dan status menjadi Activated

## Notes

- Yang diuji adalah cerminan status di modul User setelah aktivasi selesai. Alur aktivasi dan gerbang login sendiri diuji di modul Account Activation (`TC-AUTH-ACT-94`) dan Login Password (`TC-AUTH-LP-91`), dan tidak diduplikasi di sini.
- Butuh mailbox uji dan halaman Set Password yang bisa dijalankan skrip. Kebutuhan itu ditulis di Prerequisites untuk tim FE.
