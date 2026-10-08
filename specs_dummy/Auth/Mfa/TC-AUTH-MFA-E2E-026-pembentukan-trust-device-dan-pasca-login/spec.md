---
id: TC-AUTH-MFA-E2E-026-pembentukan-trust-device-dan-pasca-login
title: "Pembentukan Trust Device, Multi-Device Recognition, dan Redirect Product Hub"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-143
  - TC-AUTH-MFA-144
  - TC-AUTH-MFA-145
  - TC-AUTH-MFA-146
  - TC-AUTH-MFA-147
  - TC-AUTH-MFA-150
  - TC-AUTH-MFA-151
coverage:
  web: automated
---
# Pembentukan Trust Device, Multi-Device Recognition, dan Redirect Product Hub

## Prerequisites

- Browser uji A (dikenali) dan browser uji B (device baru).
- Perangkat mobile TAG Samurai Android terpasang.
- User `Grace Natalia` (`gracenatalia@qwertysystem.net`) profil NEWDEVE.
- User `Haikal Azzam` (`haikalazzam@qwertysystem.net`) profil NEWDEVE.
- User `Ines Maharani` (`inesmaharani@qwertysystem.net`) profil NEWDEVE.
- User `Jaya Kusuma` (`jayakusuma@qwertysystem.net`) profil MOB (trusted di web, belum di mobile).
- User `Kartika Sari` (`kartikasari@qwertysystem.net`) profil NEWDEVE.

## Test Steps

### Pembentukan trust device pasca-MFA sukses dan single-step pada login berikutnya

1. Buka browser uji B pada halaman login dengan user `gracenatalia@qwertysystem.net`
2. Selesaikan alur verifikasi faktor-2 Authenticator dengan kode valid hingga selesai
3. Verifikasi browser mendarat langsung di Portal — Product Hub (`/product-hub`, bukan Dashboard aplikasi)
4. Lakukan logout dari akun tersebut
5. Pada browser uji B yang sama dan lokasi yang sama, lakukan login kembali dengan kredensial yang sama
6. Verifikasi login langsung berakhir single-step ke Portal — Product Hub tanpa memicu halaman MFA (device telah berstatus Trusted)
7. Verifikasi tidak ada email alert baru pada login kedua ini

### Device tidak di-trust sebelum login final berhasil tuntas

8. Buka browser uji B dengan user `haikalazzam@qwertysystem.net`
9. Pada halaman Authenticator Verification, masukkan kode yang salah
10. Biarkan halaman tanpa menyelesaikan faktor-2, lalu buka tab baru dan coba login ulang dari awal
11. Verifikasi login pada tab baru tetap memicu halaman MFA (perangkat belum di-trust karena login final belum pernah tuntas)

### Kegagalan faktor-2 tidak memperbarui daftar trusted device

12. Buka form verifikasi untuk user `inesmaharani@qwertysystem.net` pada browser uji B
13. Masukkan 5 kode salah berturut-turut hingga sesi pre-auth hangus
14. Login ulang dari faktor-1 dengan password valid
15. Verifikasi sistem tetap menampilkan halaman MFA (daftar trusted device tidak bertambah)

### Trust device bersifat independen per platform (Web trust tidak membebaskan Mobile)

16. Gunakan user `jayakusuma@qwertysystem.net` yang telah memiliki status trusted device di web
17. Buka aplikasi mobile TAG Samurai Android dan login dengan akun tersebut
18. Verifikasi aplikasi mobile tetap menampilkan tantangan MFA (trust web tidak mengabaikan pemeriksaan perangkat di mobile)

### Dukungan multi-device: Kedua perangkat dikenali secara simultan

19. Pada user `kartikasari@qwertysystem.net`, selesaikan MFA sukses di browser uji A lalu di browser uji B
20. Lakukan login ulang di browser uji A dan verifikasi berakhir single-step
21. Lakukan login ulang di browser uji B dan verifikasi juga berakhir single-step (kedua device tercatat sebagai trusted device aktif)

## Notes

- Sesuai `AUTHMFA-LOGIC-04b`, device trust dibentuk secara permanen setelah verifikasi faktor-2 tuntas.
- Sesuai PRD §4.2, tujuan redirect login sukses adalah Portal — Product Hub.
