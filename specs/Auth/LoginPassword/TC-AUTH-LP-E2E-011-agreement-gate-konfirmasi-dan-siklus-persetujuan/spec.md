---
id: TC-AUTH-LP-E2E-011-agreement-gate-konfirmasi-dan-siklus-persetujuan
title: Konfirmasi Agreement, validasi checkbox, idempotensi, dan lifecycle token pre-auth
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-82
  - TC-AUTH-LP-83
  - TC-AUTH-LP-84
  - TC-AUTH-LP-85
  - TC-AUTH-LP-86
  - TC-AUTH-LP-87
  - TC-AUTH-LP-88
  - TC-AUTH-LP-89
  - TC-AUTH-LP-90
  - TC-AUTH-LP-143
  - TC-AUTH-LP-148
  - TC-AUTH-LP-149
coverage:
  web: automated
---

# Konfirmasi Agreement, validasi checkbox, idempotensi, dan lifecycle token pre-auth

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `tonokurniawan@qwertysystem.net`, `hadigunawan@qwertysystem.net`, `sitirahmawati@qwertysystem.net`, `ninamarlina@qwertysystem.net`, `ikapertiwi@qwertysystem.net`, `jonoiskandar@qwertysystem.net`, `sriwahyuni@qwertysystem.net`, `rahmathidayat@qwertysystem.net`.
- Akun Principal tersedia untuk publikasi versi Privacy Policy baru di Admin Console.
- Manipulasi TTL token pra-autentikasi (10 menit) atau mocking waktu expirasi token.

## Test Steps

### Validasi penolakan submit tanpa centang checkbox

1. Buka halaman Login with Password di browser web
2. Login menggunakan email `tonokurniawan@qwertysystem.net` dan password `QaLogin#2026` sampai layar Confirm to Continue tampil
3. Biarkan checkbox unchecked lalu klik tombol [Continue ➔]
4. Verifikasi checkbox berada dalam status invalid (severity danger)
5. Verifikasi caption inline "You need to agree to the Privacy Policy to continue" tampil tepat di bawah checkbox
6. Verifikasi tombol [Continue ➔] tetap enabled dan browser tidak berpindah halaman

### Pemulihan: Centang checkbox dan submit berhasil

7. Centang checkbox persetujuan
8. Verifikasi caption inline "You need to agree to the Privacy Policy to continue" langsung hilang
9. Klik tombol [Continue ➔]
10. Verifikasi browser berpindah menuju Portal — Product Hub
11. Lakukan logout lalu login kembali dengan `tonokurniawan@qwertysystem.net`
12. Verifikasi layar Confirm to Continue tidak tampil lagi pada login berikutnya untuk versi policy yang sama

### Alur kombinasi Agreement dengan MFA handoff

13. Login menggunakan `sitirahmawati@qwertysystem.net` (login pertama) sampai layar Confirm to Continue tampil
14. Centang checkbox persetujuan lalu klik tombol [Continue ➔]
15. Verifikasi browser dialihkan ke halaman MFA (bukan langsung ke Portal) karena akun belum menyelesaikan MFA

### Perubahan versi Privacy Policy saat layar terbuka (Stale Document 409)

16. Login menggunakan `ninamarlina@qwertysystem.net` sampai layar Confirm to Continue (versi A) tampil
17. Centang checkbox persetujuan
18. Pada sesi terpisah, publikasikan versi Privacy Policy baru (versi B) dari Admin Console
19. Kembali ke layar Confirm to Continue dan klik tombol [Continue ➔]
20. Verifikasi layar Confirm to Continue dimuat ulang dengan dokumen versi B dan checkbox kembali berstatus unchecked
21. Centang kembali checkbox untuk versi B lalu klik tombol [Continue ➔]
22. Verifikasi login berhasil dan browser menuju Portal — Product Hub

### Lifecycle token pra-autentikasi (Kedaluwarsa dan Manipulasi)

23. Login menggunakan `hadigunawan@qwertysystem.net` sampai layar Confirm to Continue tampil
24. Biarkan layar terbuka hingga melebihi TTL token pra-autentikasi (10 menit)
25. Centang checkbox lalu klik tombol [Continue ➔]
26. Verifikasi browser kembali diarahkan ke halaman Login with Password tanpa pesan toast/alert dan field Email dalam keadaan kosong
27. Login menggunakan `ikapertiwi@qwertysystem.net` dan lakukan konfirmasi sebelum batas 10 menit (misal menit ke-9)
28. Verifikasi konfirmasi berhasil dan browser menuju Portal
29. Lakukan intersepsi request konfirmasi agreement untuk `wahyuhidayat@qwertysystem.net` dengan memodifikasi token pre-auth menjadi string acak
30. Verifikasi request ditolak server dan browser dialihkan kembali ke halaman Login awal

### Idempotensi: Double-click tombol Continue dan reuse token

31. Login menggunakan `sriwahyuni@qwertysystem.net` sampai layar Confirm to Continue tampil
32. Centang checkbox lalu lakukan klik ganda cepat pada tombol [Continue ➔]
33. Verifikasi request hanya diproses satu kali tanpa error duplikasi dan user masuk ke Portal
34. Login menggunakan `rahmathidayat@qwertysystem.net` dan selesaikan konfirmasi sampai masuk Portal
35. Lakukan logout, lalu tekan tombol Back browser hingga layar Confirm to Continue sebelumnya terbuka kembali
36. Klik tombol [Continue ➔]
37. Verifikasi token pre-auth yang sudah dikonsumsi ditolak dan browser dialihkan ke halaman Login utama

### Penutupan layar Confirm to Continue tanpa Continue

38. Login menggunakan `jonoiskandar@qwertysystem.net` sampai layar Confirm to Continue tampil
39. Tutup tab browser tanpa mencentang atau mengklik Continue
40. Buka kembali halaman Login with Password di tab baru
41. Verifikasi halaman Login tampil normal tanpa sesi aktif

## Notes

- Sesuai NC-17, ketika pre-auth token kedaluwarsa atau invalid, FE me-redirect ke halaman Login dengan field Email kosong dan tanpa pesan error.
- Double-submit guard pada tombol [Continue ➔] mencegah multi-request konfirmasi persetujuan (`TC-AUTH-LP-148`).
- Token pra-autentikasi hanya dapat dikonsumsi satu kali (`TC-AUTH-LP-149`).
