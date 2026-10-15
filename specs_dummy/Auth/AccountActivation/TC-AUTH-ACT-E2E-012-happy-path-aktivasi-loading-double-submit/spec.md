---
id: TC-AUTH-ACT-E2E-012-happy-path-aktivasi-loading-double-submit
title: "Happy path Set Password: aktivasi sukses, boundary password valid, loading, dan klik ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-63
  - TC-AUTH-ACT-64
  - TC-AUTH-ACT-65
  - TC-AUTH-ACT-70
  - TC-AUTH-ACT-71
coverage:
  web: automated
---

# Happy path Set Password: aktivasi sukses, boundary password valid, loading, dan klik ganda

## Prerequisites

- Browser publik tanpa sesi login.
- `Mode: mock` — kemampuan menahan/delay respons submit via intercept jaringan (delay 5 detik untuk TC-AUTH-ACT-64) dan memantau jumlah request set password (TC-AUTH-ACT-65).
- 5 user seeding milik automation, masing-masing berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run): satu user untuk tiap blok TC-AUTH-ACT-63, TC-AUTH-ACT-64, TC-AUTH-ACT-65, TC-AUTH-ACT-70, dan TC-AUTH-ACT-71; hook `after` menghapus user serta menutup sesi.
- Akses API read-only untuk memverifikasi status user (Activated) dan token (Consumed) setelah tiap aktivasi.

## Test Steps

### Set Password dengan password valid mengaktifkan akun (TC-AUTH-ACT-63)

1. Buka link aktivasi user pertama → halaman `Auth > Account Activation > Set Password` tampil.
2. Ketik `Aman#Sandi8` pada field Password dan `Aman#Sandi8` pada field Confirm Password.
3. Klik button "Set Password" tanpa menahan respons.
4. Verifikasi halaman `Auth > Account Activation > Activation Success` tampil dengan Title "Account Activated", Body "Your account is now active. You can log in with your new password.", dan CTA "Go to Login".
5. Verifikasi tidak ada toast pada transisi ke halaman Activation Success.
6. Verifikasi via API bahwa token aktivasi user berstatus Consumed dan status user Activated.

### Password tepat 72 karakter diterima dan mengaktifkan akun (TC-AUTH-ACT-70)

7. Buka link aktivasi user kedua → halaman Set Password tampil.
8. Ketik `Aa1!` diikuti 68 karakter `x` (total 72 karakter) pada field Password dan field Confirm Password.
9. Klik button "Set Password".
10. Verifikasi halaman Activation Success tampil dengan Title "Account Activated", Body "Your account is now active. You can log in with your new password.", dan CTA "Go to Login".
11. Verifikasi via API bahwa status user Activated dan token Consumed.

### Password dengan karakter spesial `!@?&` diterima dan mengaktifkan akun (TC-AUTH-ACT-71)

12. Buka link aktivasi user ketiga → halaman Set Password tampil.
13. Ketik `Ab1!@?&xyz` pada field Password dan field Confirm Password.
14. Klik button "Set Password".
15. Verifikasi halaman Activation Success tampil dengan Title "Account Activated", Body "Your account is now active. You can log in with your new password.", dan CTA "Go to Login".
16. Verifikasi via API bahwa status user Activated dan token Consumed.

### Button Set Password Loading dan disabled selama request berjalan (TC-AUTH-ACT-64)

17. Buka link aktivasi user keempat → halaman Set Password tampil.
18. Ketik `Aman#Sandi8` pada field Password dan Confirm Password.
19. Atur intercept agar respons submit ditahan selama 5 detik, lalu klik button "Set Password".
20. Amati button selama 5 detik delay.
21. Verifikasi button "Set Password" berstatus Loading dan disabled (tidak dapat diklik kembali).
22. Lepaskan respons submit.
23. Verifikasi halaman Activation Success tampil.

### Klik ganda cepat hanya memproses satu request (TC-AUTH-ACT-65)

24. Buka link aktivasi user kelima → halaman Set Password tampil.
25. Ketik `Aman#Sandi8` pada field Password dan Confirm Password.
26. Pantau request jaringan, lalu klik button "Set Password" dua kali dengan cepat.
27. Verifikasi hanya satu request set password yang dikirim ke server.
28. Verifikasi halaman Activation Success tampil satu kali tanpa pesan error dan tanpa halaman Invalid Link.
29. Verifikasi via API bahwa token berstatus Consumed dan status user Activated tepat satu kali.

## Notes

- Semua blok mengaktifkan user masing-masing sehingga tiap TC memakai user seeding sendiri; urutan blok dari screening (aktivasi valid pertama) ke kasus edge (loading, klik ganda).
- Kebutuhan delay respons dan pemantauan jumlah request dicatat di Prerequisites.
