---
id: TC-AUTH-LP-E2E-011-account-status-gate
title: Account status gate untuk akun belum aktivasi, akun inactive, akun dihapus, dan akun baru diaktivasi
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-28
  - TC-AUTH-LP-29
  - TC-AUTH-LP-85
  - TC-AUTH-LP-86
  - TC-AUTH-LP-91
coverage:
  web: automated
---

# Account status gate untuk akun belum aktivasi, akun inactive, akun dihapus, dan akun baru diaktivasi

## Prerequisites

- Environment run adalah environment terisolasi khusus otomasi yang menyiapkan mailbox uji.
- Belum login dan session kosong. Halaman `/login` terbuka di browser.
- Hook `before` menyediakan tiga user uji, dibuat lewat API Global Settings > User dan direstore di `afterEach`:
  - `Fixture.authLoginPassword.users.pendingActivation` dengan status Pending Activation, kredensial sudah diset, dan email diketahui
  - `Fixture.authLoginPassword.users.inactiveTarget` dengan status Activated tetapi Toggle Global Inactive, kredensial benar, dan email diketahui
  - `Fixture.authLoginPassword.users.deletedTarget` dengan status yang pernah Activated lalu user dihapus dari Global Settings > User, dan emailnya diketahui
- `Fixture.authLoginPassword.users.activationTarget` berisi user Pending Activation yang akan menyelesaikan alur aktivasi akun pada langkah akhir, dengan tautan aktivasi dari mailbox uji sudah diketahui hook.
- Ketiga user uji bukan Default User. Password asli masing-masing tersedia lewat `Spectra.env.AUTH_PASSWORD`.
- `Fixture.authLoginPassword.captions.notActivated` berisi caption akun belum diaktivasi.
- `Fixture.authLoginPassword.captions.inactive` berisi caption akun inactive.
- `Fixture.authLoginPassword.captions.unregistered` berisi caption email belum terdaftar.
- `Fixture.authLoginPassword.captions.notes` berisi enum Note kanon.
- `Fixture.authLoginPassword.log.userLogPath` berisi rute halaman Global Settings > User > User Detail > tab User Log.
- Hook `before` mengembalikan Toggle Global user uji ke keadaan semula di `afterEach`, supaya spec ini tidak bergantung pada spec lain.

## Test Steps

### Akun belum aktivasi

1. Buka `/login`
2. Isi Email dengan `Fixture.authLoginPassword.users.pendingActivation.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`
3. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
4. Verifikasi caption yang tampil adalah "Your account has not been activated"
5. Verifikasi caption tersebut muncul sebagai banner atau alert, bukan inline di bawah field
6. Verifikasi browser tidak berpindah ke Portal maupun ke layar mana pun
7. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Failed" dan Note "Account is not activated"

### Akun inactive

8. Isi Email dengan `Fixture.authLoginPassword.users.inactiveTarget.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`
9. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
10. Verifikasi caption yang tampil adalah "Your account is inactive"
11. Verifikasi caption tersebut berbeda dari caption akun belum diaktivasi, sehingga status kedua kondisi tidak tercampur
12. Verifikasi browser tidak berpindah ke halaman mana pun
13. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Failed" dan Note "Account is inactive"

### Akun yang baru saja dinonaktifkan di Global Settings

14. Login sebagai user dengan role Total Control pada entity Client
15. Buka Global Settings > User, cari `Fixture.authLoginPassword.users.inactiveTarget`, ubah Toggle Global menjadi Inactive, lalu simpan
16. Verifikasi status user berubah menjadi Inactive di User List
17. Logout dari akun admin sehingga session kosong
18. Buka `/login` lalu isi Email dengan `Fixture.authLoginPassword.users.inactiveTarget.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`
19. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
20. Verifikasi caption yang tampil adalah "Your account is inactive", sehingga status dibaca real-time dari Global Settings > User, bukan dari cache lama
21. Verifikasi jumlah entri di User Log bertambah satu dengan Status "Failed" dan Note "Account is inactive"

### Akun yang dihapus di Global Settings

22. Kembali ke Global Settings > User, ubah Toggle Global `Fixture.authLoginPassword.users.inactiveTarget` menjadi Active, lalu hapus user `Fixture.authLoginPassword.users.deletedTarget`
23. Verifikasi user tersebut hilang dari User List
24. Logout dari akun admin sehingga session kosong
25. Catat jumlah entri di User Log user yang lain sebagai pembanding
26. Buka `/login` lalu isi Email dengan `Fixture.authLoginPassword.users.deletedTarget.email` dan Password dengan `Spectra.env.AUTH_PASSWORD`
27. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
28. Verifikasi caption yang tampil adalah "Email is not registered yet"
29. Verifikasi caption tersebut sama dengan caption untuk email yang memang belum pernah terdaftar
30. Verifikasi tidak ada caption lain yang membocorkan bahwa akun tersebut pernah ada lalu dihapus
31. Verifikasi jumlah entri di User Log tetap sama dengan pembanding, sehingga akun yang dihapus tidak menghasilkan entri log karena tidak ada subjek user

### Akun yang baru saja diaktivasi

32. Isi Email dengan `Fixture.authLoginPassword.users.activationTarget.email` dan Password dengan satu nilai lalu klik "Log in"
33. Verifikasi caption "Your account has not been activated" muncul, sehingga kondisi awal spec ini memang terkonfirmasi
34. Jalankan alur aktivasi akun lengkap untuk user tersebut lewat tautan aktivasi dari mailbox uji, lalu selesaikan Set Password
35. Verifikasi alur aktivasi selesai dengan sukses
36. Buka `/login` lalu isi Email dengan `Fixture.authLoginPassword.users.activationTarget.email` dan Password dengan password hasil Set Password
37. Verifikasi reCAPTCHA diselesaikan sampai tercentang, lalu klik "Log in"
38. Verifikasi caption "Your account has not been activated" tidak muncul lagi
39. Verifikasi browser berpindah ke layar "Confirm to Continue" atau ke Portal — Product Hub, sehingga login diproses lanjut normal
40. Verifikasi entri yang baru muncul di User Log bukan Note "Account is not activated", sehingga gerbang status tidak lagi menolak
41. Logout dari Portal sehingga session kosong

## Notes

- Status user adalah stored di Global Settings > User dan Auth hanya membacanya secara real-time. Verifikasi status dilakukan lewat UI Global Settings, bukan lewat database.
- Caption akun belum aktivasi dan akun inactive sengaja dipisahkan. Kalau keduanya memakai caption yang sama, langkah 11 tidak bisa dibedakan.
- Akun yang dihapus menghasilkan caption yang sama dengan email yang belum pernah terdaftar, dan justru itu yang diuji pada langkah 28 sampai 30. Ini mencegah kebocoran bahwa sebuah akun pernah ada.
- Langkah 15 sampai 21 mengubah Toggle Global lewat UI Global Settings. Perubahan itu dikembalikan oleh hook `afterEach`, jadi spec ini tidak meninggalkan user dalam keadaan tidak aktif untuk spec lain.
- Alur aktivasi akun pada langkah 34 adalah milik modul `auth/account-activation`. Yang diuji di sini efeknya terhadap gerbang status login, yaitu caption gate yang hilang.
- Kebutuhan mailbox uji untuk tautan aktivasi dicatat di Prerequisites sebagai sumber resmi bagi tim FE.
- Delete user pada langkah 22 adalah aksi yang menghapus data. Letaknya di bagian akhir spec karena baris yang dipakai pada langkah 26 memang harus sudah tidak ada.
- Verifikasi entri log memakai User Log milik user uji masing-masing, bukan log gabungan, supaya tidak saling tertimpa penghitungannya.