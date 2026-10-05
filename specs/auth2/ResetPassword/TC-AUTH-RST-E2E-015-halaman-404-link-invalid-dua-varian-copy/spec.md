---
id: TC-AUTH-RST-E2E-015-halaman-404-link-invalid-dua-varian-copy
title: Halaman 404 untuk link reset invalid dengan dua varian copy
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-36
  - TC-AUTH-RST-37
  - TC-AUTH-RST-38
  - TC-AUTH-RST-39
  - TC-AUTH-RST-70
  - TC-AUTH-RST-71
  - TC-AUTH-RST-74
coverage:
  web: automated
---

# Halaman 404 untuk link reset invalid dengan dua varian copy

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Satu user berstatus Activated dan Active di Global Settings > User. Email-nya adalah
  `Fixture.authResetPassword.users.activated.email`.
- `Fixture.authResetPassword.tokens.seedExpiredToken` adalah cara membuat satu token reset yang
  statusnya masih aktif tapi sudah melewati masa berlaku lewat API Global Settings > User.
- `Fixture.authResetPassword.tokens.seedConsumedToken` adalah cara membuat satu token reset yang
  statusnya sudah dipakai, dengan simulates kondisi submit yang pernah berhasil.
- `Fixture.authResetPassword.tokens.seedInvalidatedToken` adalah cara membuat satu token reset yang
  statusnya sudah di-invalidasi karena ada request atau resend baru.
- `Fixture.authResetPassword.tokens.seedActiveToken` adalah cara membuat satu token reset aktif
  yang dipakai sebagai pemicu token lain menjadi tidak berlaku.
- `Fixture.authResetPassword.tokens.linkForToken` adalah cara menyusun tautan reset dari token
  tertentu tanpa menuliskan nilai token di file.
- `Fixture.authResetPassword.data.garbageToken` adalah string token yang tidak dikenal dan tidak
  pernah dibuat server, dipakai untuk menguji link yang dimanipulasi.
- Copy halaman 404 untuk kedua varian diambil dari `Fixture.authResetPassword.captions`, sehingga
  teks panjangnya tidak diketik ulang di spec ini.
- Nilai token hanya dibaca lewat helper dan tidak ditulis di spec maupun fixture.

## Test Steps

### Token expired

1. Buat satu token reset milik `Fixture.authResetPassword.users.activated.email` yang statusnya
   sudah expired memakai `Fixture.authResetPassword.tokens.seedExpiredToken`
2. Susun tautan reset dari token tersebut memakai `Fixture.authResetPassword.tokens.linkForToken`
3. Buka tautan reset tersebut di browser
4. Verifikasi halaman 404 tampil
5. Verifikasi Title pada halaman adalah "Reset Link Expired"
6. Verifikasi Body pada halaman adalah
    "This password reset link has expired. Reset links are valid for 24 hours."
7. Verifikasi CTA pada halaman adalah "Request New Link"
8. Verifikasi tidak ada field Email dan tidak ada form pada halaman ini
9. Verifikasi tidak ada Password Policy dan tidak ada field Password pada halaman ini

### Token already used

10. Buat satu token reset milik `Fixture.authResetPassword.users.activated.email` yang statusnya
    sudah consumed memakai `Fixture.authResetPassword.tokens.seedConsumedToken`
11. Susun tautan reset dari token tersebut memakai `Fixture.authResetPassword.tokens.linkForToken`
12. Buka tautan reset tersebut di browser
13. Verifikasi halaman 404 tampil
14. Verifikasi Title pada halaman adalah "Reset Link Already Used"
15. Verifikasi Body pada halaman adalah
    "This password reset link has already been used. Your password has been updated."
16. Verifikasi CTA pada halaman adalah "Go to Login"
17. Verifikasi tidak ada field Email dan tidak ada form pada halaman ini
18. Verifikasi tidak ada Password Policy dan tidak ada field Password pada halaman ini

### Token invalidasi oleh request atau resend baru

19. Buat satu token reset aktif milik user tersebut memakai
    `Fixture.authResetPassword.tokens.seedActiveToken`
20. Simpan tautan reset dari token tersebut sebagai tautan lama
21. Buat request reset baru untuk user tersebut sehingga token lama di-invalidasi
22. Buka tautan lama pada langkah 20 di browser
23. Verifikasi halaman 404 tampil
24. Verifikasi Title pada halaman adalah "Reset Link Expired", sehingga token invalidasi dipetakan
    ke varian Expired dan bukan ke varian Already Used
25. Verifikasi CTA pada halaman adalah "Request New Link"
26. Verifikasi tidak ada teks yang menyebut bahwa token pernah di-invalidasi karena ada request
    atau resend baru

### Token tidak dikenal atau dimanipulasi

27. Susun tautan reset memakai `Fixture.authResetPassword.data.garbageToken`
28. Buka tautan reset tersebut di browser
29. Verifikasi halaman 404 tampil
30. Verifikasi Title pada halaman adalah "Reset Link Expired"
31. Verifikasi CTA pada halaman adalah "Request New Link"
32. Verifikasi tidak ada teks yang menyebut bahwa token tidak dikenal atau tidak ada di database

### Tidak ada kebocoran penyebab teknis

33. Bandingkan seluruh teks yang tampil pada keempat kondisi tadi
34. Verifikasi hanya ada dua Title yang berbeda, yaitu "Reset Link Expired" dan
    "Reset Link Already Used"
35. Verifikasi tidak ada varian ketiga yang muncul pada kondisi mana pun
36. Verifikasi tidak ada teks yang menyebut status internal token seperti "invalidated", "consumed",
    "expired", atau "unknown"
37. Verifikasi tidak ada kode status HTTP, kode error, atau nama field teknis yang tampil di halaman
38. Verifikasi respons dan payload yang dikembalikan tidak membocorkan penyebab spesifik, sehingga
    tidak ada informasi yang bisa dipakai memperjelas status token di luar halaman

## Notes

- Empat kondisi diuji sebagai satu spec karena semuanya menghasilkan satu dari dua varian copy yang
  sama, dan yang diuji justru bahwa tidak ada varian ketiga.
- Token invalidasi sengaja dipetakan ke varian Expired. Kalau dipetakan ke Already Used, user
  akan mengira password-nya sudah berubah padahal belum, dan itu informasi yang menyesatkan.
- Copy Body yang panjang diambil dari fixture, bukan diketik ulang, supaya perubahan copy di PRD
  tidak membuat spec ini Rusak.
- Verifikasi payload jaringan dilakukan pada langkah 38 untuk memastikan penyebab teknis tidak
  bocor lewat jalur selain tampilan halaman.
- Nilai token hanya dibaca lewat helper dan tidak ditulis di file, sesuai aturan
  e2e-conventions.md bagian 5.