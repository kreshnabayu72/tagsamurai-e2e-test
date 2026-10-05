---
id: TC-AUTH-RST-E2E-019-submit-password-baris-batas-minimum-dan-maksimum
title: Submit password baru pada baris batas panjang minimum dan maksimum
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-RST-42
  - TC-AUTH-RST-44
coverage:
  web: automated
---

# Submit password baru pada baris batas panjang minimum dan maksimum

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Dua user berstatus Activated dan Active di Global Settings > User, dengan password lama yang
  diketahui dan tersedia lewat `Spectra.env.AUTH_PASSWORD`, tidak ditulis di file ini maupun di
  fixture. Kedua user bukan Default User dan bukan akun admin Total Control.
  - `Fixture.authResetPassword.users.activated.email` adalah user untuk kasus batas minimum.
  - `Fixture.authResetPassword.users.activatedSecondary.email` adalah user untuk kasus batas
    maksimum, dibedakan dari user pertama supaya password baru yang berhasil dipakai tidak
    saling berinteraksi.
- `Fixture.authResetPassword.tokens.seedActiveToken` adalah cara membuat satu token reset aktif
  milik user tertentu dengan masa berlaku 24 jam, lewat API Global Settings > User. Kemampuan ini
  disiapkan tim FE.
- `Fixture.authResetPassword.tokens.linkForToken` adalah cara menyusun tautan reset dari token
  tersebut tanpa menuliskan nilai token di file.
- `Fixture.authResetPassword.data.password8Chars` adalah password sepanjang tepat 8 karakter yang
  memenuhi seluruh Password Policy.
- `Fixture.authResetPassword.data.password72Chars` adalah password sepanjang tepat 72 karakter yang
  memenuhi seluruh Password Policy.
- `Fixture.authResetPassword.checklist` adalah daftar rule pada checklist beserta labelnya.
- Nilai token dan nilai password hanya dibaca lewat helper maupun environment variable dan tidak
  ditulis di spec maupun fixture.

## Test Steps

### Batas panjang minimum 8 karakter

1. Buat satu token reset aktif milik
   `Fixture.authResetPassword.users.activated.email` memakai
   `Fixture.authResetPassword.tokens.seedActiveToken`
2. Buka tautan reset dari token tersebut memakai `Fixture.authResetPassword.tokens.linkForToken`
3. Verifikasi halaman Setup New Password tampil
4. Isi field Password dengan `Fixture.authResetPassword.data.password8Chars`
5. Isi field Confirm Password dengan nilai yang sama
6. Verifikasi checklist Password Policy menampilkan keenam rule sebagai terpenuhi
7. Verifikasi caption "Maximum 72 characters" tidak tampil
8. Klik "Reset Password"
9. Verifikasi submit diterima, tidak diblokir oleh validasi FE
10. Verifikasi navigasi ke halaman Password Reset Successful terjadi
11. Verifikasi password baru user tersebut dapat dipakai untuk login
12. Verifikasi password lama user tersebut tidak lagi dapat dipakai untuk login

### Batas panjang maksimum 72 karakter

13. Buat satu token reset aktif milik
    `Fixture.authResetPassword.users.activatedSecondary.email` memakai
    `Fixture.authResetPassword.tokens.seedActiveToken`
14. Buka tautan reset dari token tersebut memakai `Fixture.authResetPassword.tokens.linkForToken`
15. Verifikasi halaman Setup New Password tampil
16. Isi field Password dengan `Fixture.authResetPassword.data.password72Chars`
17. Isi field Confirm Password dengan nilai yang sama
18. Verifikasi checklist Password Policy menampilkan keenam rule sebagai terpenuhi
19. Verifikasi caption "Maximum 72 characters" tidak tampil
20. Verifikasi caption batas panjang minimum juga tidak tampil
21. Klik "Reset Password"
22. Verifikasi submit diterima, tidak diblokir oleh validasi FE
23. Verifikasi navigasi ke halaman Password Reset Successful terjadi
24. Verifikasi password baru user tersebut dapat dipakai untuk login
25. Verifikasi password lama user tersebut tidak lagi dapat dipakai untuk login

## Notes

- Dua kasus dipisahkan oleh dua user berbeda supaya submit yang berhasil pada kasus pertama tidak
  memengaruhi kasus kedua, dan supaya nilai password baru yang dipakai tidak saling menggantikan.
- Yang diuji adalah penerimaan pada baris batas, sedangkan penolakan satu karakter di dalam dan di
  luar batas ada di spec 017.
- Panjang password dibaca dari fixture, bukan ditulis di spec ini, sesuai aturan e2e-conventions.md
  bagian 5.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password". Aturan `[Submit]` dan
  `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit entitas, bukan
  untuk halaman autentikasi.