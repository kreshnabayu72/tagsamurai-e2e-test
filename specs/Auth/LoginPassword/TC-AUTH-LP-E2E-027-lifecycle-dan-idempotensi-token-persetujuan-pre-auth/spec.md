---
id: TC-AUTH-LP-E2E-027-lifecycle-dan-idempotensi-token-persetujuan-pre-auth
title: Lifecycle dan idempotensi token persetujuan pre-auth
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-87
  - TC-AUTH-LP-88
  - TC-AUTH-LP-89
  - TC-AUTH-LP-143
  - TC-AUTH-LP-148
  - TC-AUTH-LP-149
coverage:
  web: automated
---

# Lifecycle dan idempotensi token persetujuan pre-auth

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `ninamarlina@qwertysystem.net`, `hadigunawan@qwertysystem.net`, `ikapertiwi@qwertysystem.net`, `wahyuhidayat@qwertysystem.net`, `sriwahyuni@qwertysystem.net`, `rahmathidayat@qwertysystem.net`.
- Akun Principal tersedia untuk publikasi versi Privacy Policy baru di Admin Console.
- Manipulasi TTL token pra-autentikasi (10 menit) atau mocking waktu expirasi token.

## Test Steps

### Perubahan versi Privacy Policy saat layar terbuka (Stale Document 409)

1. Buka halaman Login with Password di browser web
2. Login menggunakan `ninamarlina@qwertysystem.net` sampai layar Confirm to Continue (versi A) tampil
3. Centang checkbox persetujuan
4. Pada sesi terpisah, publikasikan versi Privacy Policy baru (versi B) dari Admin Console
5. Kembali ke layar Confirm to Continue dan klik tombol [Continue ➔]
6. Verifikasi layar Confirm to Continue dimuat ulang dengan dokumen versi B dan checkbox kembali berstatus unchecked
7. Centang kembali checkbox untuk versi B lalu klik tombol [Continue ➔]
8. Verifikasi login berhasil dan browser menuju Portal — Product Hub

### Lifecycle token pra-autentikasi (Kedaluwarsa dan Manipulasi)

9. Login menggunakan `hadigunawan@qwertysystem.net` sampai layar Confirm to Continue tampil
10. Biarkan layar terbuka hingga melebihi TTL token pra-autentikasi (10 menit)
11. Centang checkbox lalu klik tombol [Continue ➔]
12. Verifikasi browser kembali diarahkan ke halaman Login with Password tanpa pesan toast/alert dan field Email dalam keadaan kosong
13. Login menggunakan `ikapertiwi@qwertysystem.net` dan lakukan konfirmasi sebelum batas 10 menit (misal menit ke-9)
14. Verifikasi konfirmasi berhasil dan browser menuju Portal
15. Lakukan intersepsi request konfirmasi agreement untuk `wahyuhidayat@qwertysystem.net` dengan memodifikasi token pre-auth menjadi string acak
16. Verifikasi request ditolak server dan browser dialihkan kembali ke halaman Login awal

### Idempotensi: Double-click tombol Continue dan reuse token

17. Login menggunakan `sriwahyuni@qwertysystem.net` sampai layar Confirm to Continue tampil
18. Centang checkbox lalu lakukan klik ganda cepat pada tombol [Continue ➔]
19. Verifikasi request hanya diproses satu kali tanpa error duplikasi dan user masuk ke Portal
20. Login menggunakan `rahmathidayat@qwertysystem.net` dan selesaikan konfirmasi sampai masuk Portal
21. Lakukan logout, lalu tekan tombol Back browser hingga layar Confirm to Continue sebelumnya terbuka kembali
22. Klik tombol [Continue ➔]
23. Verifikasi token pre-auth yang sudah dikonsumsi ditolak dan browser dialihkan ke halaman Login utama

## Notes

- Sesuai NC-17, ketika pre-auth token kedaluwarsa, dimodifikasi, atau sudah dikonsumsi, FE me-redirect ke halaman Login dengan field Email kosong dan tanpa pesan error (`TC-AUTH-LP-88`, `TC-AUTH-LP-143`, `TC-AUTH-LP-149`).
- Perubahan versi Privacy Policy saat layar terbuka memuat ulang layar Confirm to Continue dengan checkbox baru unchecked dan tidak menciptakan sesi (`TC-AUTH-LP-87`, §9.6 Confirm Agreement 409).
- Double-submit guard pada tombol [Continue ➔] mencegah multi-request konfirmasi persetujuan (`TC-AUTH-LP-148`); token pra-autentikasi hanya dapat dikonsumsi satu kali (`TC-AUTH-LP-149`).
- Spec ini dipecah dari E2E-011 agar uji konfirmasi dasar (checkbox, pemulihan, handoff MFA) terpisah dari lifecycle token, perkalian versi dokumen, dan idempotensi (lihat `gap-spec/gap-spec.md` GAP-LP-E2E-009).