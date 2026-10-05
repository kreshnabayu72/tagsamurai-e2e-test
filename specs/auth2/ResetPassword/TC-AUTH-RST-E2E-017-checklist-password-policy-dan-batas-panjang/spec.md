---
id: TC-AUTH-RST-E2E-017-checklist-password-policy-dan-batas-panjang
title: Checklist Password Policy real-time, batas panjang, dan show/hide password
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-RST-43
  - TC-AUTH-RST-45
  - TC-AUTH-RST-46
  - TC-AUTH-RST-47
  - TC-AUTH-RST-48
  - TC-AUTH-RST-49
  - TC-AUTH-RST-50
  - TC-AUTH-RST-51
  - TC-AUTH-RST-56
  - TC-AUTH-RST-57
coverage:
  web: automated
---

# Checklist Password Policy real-time, batas panjang, dan show/hide password

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- `Fixture.authResetPassword.tokens.seedActiveToken` adalah cara membuat satu token reset aktif
  milik satu user dengan masa berlaku 24 jam, lewat API Global Settings > User. Kemampuan ini
  disiapkan tim FE.
- `Fixture.authResetPassword.tokens.linkForToken` adalah cara menyusun tautan reset dari token
  tersebut tanpa menuliskan nilai token di file.
- `Fixture.authResetPassword.users.activated.email` adalah email user pemilik token tersebut. User ini
  bukan Default User dan bukan akun admin Total Control.
- `Fixture.authResetPassword.tokens.readTokenState` adalah cara membaca status token reset, dipakai
  untuk memastikan submit yang diblokir tidak mengonsumsi token.
- `Fixture.authResetPassword.data.password7Chars` adalah password sepanjang 7 karakter yang sudah
  memenuhi seluruh rule selain panjang minimum.
- `Fixture.authResetPassword.data.password73Chars` adalah password sepanjang 73 karakter yang sudah
  memenuhi seluruh rule selain panjang maksimum.
- `Fixture.authResetPassword.data.passwordNoUppercase` adalah password tanpa huruf besar.
- `Fixture.authResetPassword.data.passwordNoLowercase` adalah password tanpa huruf kecil.
- `Fixture.authResetPassword.data.passwordNoNumber` adalah password tanpa angka.
- `Fixture.authResetPassword.data.passwordNoSpecial` adalah password tanpa special character.
- `Fixture.authResetPassword.data.passwordWithSpace` adalah password yang memuat spasi di tengah.
- `Fixture.authResetPassword.data.passwordProgressive` adalah password yang dibuat bertahap sehingga
  semua rule terpenuhi satu per satu, dipakai untuk menguji pembaruan checklist per keystroke.
- `Fixture.authResetPassword.checklist` adalah daftar rule pada checklist beserta labelnya, supaya
  label tidak diketik ulang di spec ini.
- `Fixture.authResetPassword.captions` adalah sumber caption panjang maksimum dan caption spasi.
- Nilai token hanya dibaca lewat helper dan tidak ditulis di spec maupun fixture.

## Test Steps

### Checklist tampil dan pembaruan real-time

1. Buat satu token reset aktif milik
   `Fixture.authResetPassword.users.activated.email` memakai
   `Fixture.authResetPassword.tokens.seedActiveToken`
2. Buka tautan reset dari token tersebut memakai `Fixture.authResetPassword.tokens.linkForToken`
3. Verifikasi halaman Setup New Password tampil
4. Verifikasi checklist Password Policy tampil dan memuat keenam rule dari
    `Fixture.authResetPassword.checklist`
5. Verifikasi semua baris checklist berada dalam keadaan belum terpenuhi saat kedua field masih
    kosong
6. Ketik `Fixture.authResetPassword.data.passwordProgressive` pada field Password satu per satu
7. Verifikasi setiap baris checklist berubah dari belum terpenuhi menjadi terpenuhi tepat saat rule
    terkait terpenuhi, tanpa perlu menekan tombol submit
8. Verifikasi tidak ada kedipan, muat ulang, atau penundaan pada pembaruan checklist
9. Verifikasi baris checklist yang belum terpenuhi tetap tampil, bukan ikut hilang

### Batas panjang minimum

10. Isi field Password dengan `Fixture.authResetPassword.data.password7Chars`
11. Isi field Confirm Password dengan nilai yang sama
12. Verifikasi baris checklist "Minimum 8 characters" tetap berada dalam keadaan belum terpenuhi
13. Klik "Reset Password"
14. Verifikasi submit diblokir dan tidak ada navigasi dari halaman Setup New Password
15. Verifikasi caption yang tampil sesuai dengan caption panjang minimum dari
    `Fixture.authResetPassword.captions`
16. Verifikasi status token reset milik user tersebut tetap "active"
17. Verifikasi tidak ada navigasi ke halaman Password Reset Successful

### Batas panjang maksimum

18. Kosongkan kedua field dengan tombol "Clear Field"
19. Isi field Password dengan `Fixture.authResetPassword.data.password73Chars`
20. Verifikasi caption terpisah yang berbunyi "Maximum 72 characters" muncul
21. Verifikasi caption tersebut tampil di luar checklist enam baris, bukan sebagai baris checklist
22. Verifikasi caption tersebut tidak menggantikan atau menggeser baris checklist
23. Klik "Reset Password"
24. Verifikasi submit diblokir dan tidak ada navigasi dari halaman Setup New Password
25. Verifikasi status token reset milik user tersebut tetap "active"

### Setiap rule Password Policy

26. Kosongkan kedua field dengan tombol "Clear Field"
27. Isi field Password dengan `Fixture.authResetPassword.data.passwordNoUppercase`, lalu isi Confirm
    Password dengan nilai yang sama
28. Verifikasi baris checklist "One uppercase (A-Z)" berada dalam keadaan belum terpenuhi
29. Kosongkan kedua field dengan tombol "Clear Field"
30. Isi field Password dengan `Fixture.authResetPassword.data.passwordNoLowercase`, lalu isi Confirm
    Password dengan nilai yang sama
31. Verifikasi baris checklist "One lowercase (a-z)" berada dalam keadaan belum terpenuhi
32. Kosongkan kedua field dengan tombol "Clear Field"
33. Isi field Password dengan `Fixture.authResetPassword.data.passwordNoNumber`, lalu isi Confirm
    Password dengan nilai yang sama
34. Verifikasi baris checklist "One number (0-9)" berada dalam keadaan belum terpenuhi
35. Kosongkan kedua field dengan tombol "Clear Field"
36. Isi field Password dengan `Fixture.authResetPassword.data.passwordNoSpecial`, lalu isi Confirm
    Password dengan nilai yang sama
37. Verifikasi baris checklist "One special character" berada dalam keadaan belum terpenuhi
38. Verifikasi baris checklist yang lain tetap menunjukkan keadaan sebenarnya untuk nilai tersebut

### Password yang memuat spasi

39. Kosongkan kedua field dengan tombol "Clear Field"
40. Isi field Password dengan `Fixture.authResetPassword.data.passwordWithSpace`, lalu isi Confirm
    Password dengan nilai yang sama
41. Verifikasi baris checklist "Password cannot contain spaces" berada dalam keadaan belum terpenuhi
42. Verifikasi baris checklist "Minimum 8 characters" tetap terpenuhi, sehingga panjang yang dihitung
    memasukkan spasi
43. Klik "Reset Password"
44. Verifikasi submit diblokir dan tidak ada navigasi dari halaman Setup New Password
45. Verifikasi caption yang tampil sesuai dengan caption spasi dari
    `Fixture.authResetPassword.captions`
46. Verifikasi nilai pada field Password tetap memuat spasi setelah submit diblokir, sehingga spasi
    tidak di-trim otomatis oleh FE
47. Verifikasi status token reset milik user tersebut tetap "active"

### Tampilkan dan sembunyikan password

48. Isi field Password dengan satu nilai yang memenuhi seluruh rule
49. Verifikasi teks pada field Password tersembunyi secara default
50. Verifikasi teks pada field Confirm Password tersembunyi secara default
51. Klik ikon mata pada field Password
52. Verifikasi teks pada field Password terlihat
53. Verifikasi tooltip pada ikon adalah "Show password" sebelum diklik, dan berubah menjadi
    "Hide password" setelah diklik
54. Verifikasi teks pada field Confirm Password tetap tersembunyi
55. Verifikasi nilai pada field Password tidak hilang saat ikon diklik
56. Klik lagi ikon mata pada field Password
57. Verifikasi teks pada field Password kembali tersembunyi
58. Klik ikon mata pada field Confirm Password
59. Verifikasi teks pada field Confirm Password terlihat
60. Verifikasi teks pada field Password tetap tersembunyi

### Tidak ada reCAPTCHA di halaman Setup New Password

61. Verifikasi tidak ada widget reCAPTCHA di halaman ini
62. Verifikasi tidak ada elemen mock atau spacers kosong yang sebelumnya menampung reCAPTCHA
63. Verifikasi ketiadaan reCAPTCHA tidak bergantung pada status token atau kondisi lain, sehingga
    tetap tidak tampil setelah submit yang diblokir pada langkah 14 dan 23
64. Verifikasi tombol "Reset Password" tetap dapat diklik tanpa menyelesaikan captcha apa pun

## Notes

- Semua submit pada spec ini diblokir oleh validasi FE, sehingga status token dipakai sebagai
  pembuktian bahwa submit yang diblokir tidak mengonsumsi token. Nilai itu dibaca di beberapa
  titik dan dibandingkan dengan nilai awal.
- Baris checklist dibaca dari `Fixture.authResetPassword.checklist`, sesuai aturan
  e2e-conventions.md bagian 9, supaya label tidak diketik ulang di banyak spec.
- Subbagian batas panjang maksimum sengaja memverifikasi bahwa caption "Maximum 72 characters"
  terpisah dari checklist, karena PRD menempatkan caption itu sebagai informasi tambahan, bukan
  sebagai rule ketujuh.
- Password yang memuat spasi diuji bersama konsekuensinya pada panjang minimum, supaya terlihat
  bahwa spasi ikut terhitung pada panjang dan bukan sekadar ditolak terpisah.
- Ketiadaan reCAPTCHA di halaman ini dibandingkan dengan halaman permintaan yang menampilkannya,
  sesuai aturan proteksi di auth-foundation.md. Perbedaannya disengaja.
- Password uji pada spec ini adalah nilai contoh yang memang ditolak, bukan kredensial sungguhan,
  dan tetap diambil dari fixture.