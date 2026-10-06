---
id: TC-AUTH-LP-E2E-004-evaluasi-status-akun-dan-email-unregistered
title: Evaluasi status akun (Pending Activation, Inactive) dan Email belum terdaftar
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-28
  - TC-AUTH-LP-31
  - TC-AUTH-LP-32
  - TC-AUTH-LP-33
  - TC-AUTH-LP-34
  - TC-AUTH-LP-35
  - TC-AUTH-LP-36
  - TC-AUTH-LP-37
coverage:
  web: automated
---

# Evaluasi status akun (Pending Activation, Inactive) dan Email belum terdaftar

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `dewilestari@qwertysystem.net` berstatus Pending Activation di database.
- User `agussetiawan@qwertysystem.net` berstatus Activated dengan Toggle Global OFF (Inactive).
- User `jokosusilo@qwertysystem.net` berstatus Activated dan Active.
- Email `tidakada@qwertysystem.net` tidak terdaftar di sistem.

## Test Steps

### Email belum terdaftar menghasilkan caption inline

1. Buka halaman Login with Password di browser web
2. Masukkan email `tidakada@qwertysystem.net` pada field Email
3. Masukkan password `QaLogin#2026` pada field Password
4. Selesaikan reCAPTCHA
5. Klik tombol [Log in]
6. Verifikasi caption inline "Email is not registered yet" tampil di bawah field Email
7. Verifikasi field Email tetap terisi `tidakada@qwertysystem.net`
8. Verifikasi field Password otomatis dikosongkan
9. Verifikasi widget reCAPTCHA kembali ke status Unsolved
10. Verifikasi tidak ada Alert pesan server di atas tombol [Log in]

### Akun belum diaktivasi (Pending Activation)

11. Masukkan email `dewilestari@qwertysystem.net` pada field Email
12. Masukkan password `QaLogin#2026` pada field Password
13. Selesaikan reCAPTCHA
14. Klik tombol [Log in]
15. Verifikasi Alert Danger "Your account has not been activated" tampil tepat di atas tombol [Log in]
16. Verifikasi field Password dikosongkan dan widget reCAPTCHA kembali Unsolved
17. Verifikasi browser tetap berada di halaman Login

### Akun dinonaktifkan (Inactive / Toggle Global OFF)

18. Masukkan email `agussetiawan@qwertysystem.net` pada field Email
19. Masukkan password `QaLogin#2026` pada field Password
20. Selesaikan reCAPTCHA
21. Klik tombol [Log in]
22. Verifikasi Alert Danger "Your account is inactive" tampil tepat di atas tombol [Log in]
23. Verifikasi field Password dikosongkan dan widget reCAPTCHA kembali Unsolved

### Percobaan salah pada akun Pending / Inactive tidak menambah lock counter

24. Masukkan kembali email `dewilestari@qwertysystem.net` dengan password salah `SalahPass#1`
25. Selesaikan reCAPTCHA lalu klik tombol [Log in]
26. Ulangi submit password salah untuk `dewilestari@qwertysystem.net` sebanyak dua kali lagi (total 3 kali)
27. Verifikasi pada ketiga percobaan pesan yang tampil selalu Alert Danger "Your account has not been activated"
28. Verifikasi caption lock 15 menit tidak pernah muncul, membuktikan akun Pending tidak dihitung counter gagalnya
29. Masukkan email `agussetiawan@qwertysystem.net` dengan password salah `SalahPass#1` sebanyak tiga kali berturut-turut
30. Verifikasi pada ketiga percobaan pesan yang tampil selalu Alert Danger "Your account is inactive"
31. Verifikasi caption lock tidak pernah muncul untuk akun Inactive

### Urutan evaluasi: Password kosong dan reCAPTCHA sebelum status akun

32. Masukkan email `dewilestari@qwertysystem.net`, kosongkan field Password, selesaikan reCAPTCHA, lalu klik [Log in]
33. Verifikasi caption inline "Password must not be empty" tampil di bawah field Password
34. Verifikasi Alert "Your account has not been activated" tidak tampil
35. Masukkan email `dewilestari@qwertysystem.net` dan password `QaLogin#2026` tanpa menyelesaikan reCAPTCHA, lalu klik [Log in]
36. Verifikasi caption "Please verify that you are not a robot" tampil di bawah widget reCAPTCHA
37. Verifikasi Alert "Your account has not been activated" tidak tampil

### Pembedaan pesan Email belum terdaftar dan kredensial salah

38. Masukkan email `tidakada@qwertysystem.net` dengan password `QaLogin#2026`, selesaikan reCAPTCHA, lalu klik [Log in]
39. Verifikasi pesan tampil berupa caption inline "Email is not registered yet" di bawah field Email
40. Masukkan email `jokosusilo@qwertysystem.net` dengan password salah `SalahPass#1`, selesaikan reCAPTCHA, lalu klik [Log in]
41. Verifikasi pesan tampil berupa Alert Danger "Incorrect email or password" di atas tombol [Log in]
42. Verifikasi kedua pesan dan letak posisinya dibedakan secara tegas sesuai ketentuan sistem

## Notes

- Sesuai NC-05, pesan "Email is not registered yet" tampil inline di bawah field Email (`AUTHLP-LOGIC-01`), sedangkan kredensial salah tampil sebagai Alert Danger di atas tombol [Log in].
- Urutan evaluasi menjamin penolakan field kosong dan captcha diproses sebelum pembacaan status akun (`NC-01`, `NC-02`).
