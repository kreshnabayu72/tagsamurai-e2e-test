---
id: TC-AUTH-RST-E2E-014-token-valid-render-halaman-setup
title: Token valid merender halaman Setup New Password dan validasi read-only
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-35
  - TC-AUTH-RST-40
  - TC-AUTH-RST-87
coverage:
  web: automated
---

# Token valid merender halaman Setup New Password dan validasi read-only

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Satu user berstatus Activated dan Active di Global Settings > User. Email-nya adalah
  `Fixture.authResetPassword.users.activated.email`. User ini bukan Default User dan bukan akun
  admin Total Control.
- `Fixture.authResetPassword.tokens.seedActiveToken` adalah cara membuat satu token reset aktif
  milik user tersebut lewat API Global Settings > User, dengan masa berlaku 24 jam dan belum
  pernah dipakai. Kemampuan ini disiapkan tim FE.
- `Fixture.authResetPassword.tokens.readTokenState` adalah cara membaca status token reset milik
  user tersebut.
- `Fixture.authResetPassword.tokens.linkForActiveToken` adalah cara menyusun tautan reset dari
  token aktif milik user tersebut tanpa menuliskan nilai token di file.
- `Fixture.authResetPassword.users.activated.email` adalah email yang tampil pada subtitle halaman
  Setup New Password.
- Dua tab browser tersedia pada environment uji untuk subbagian pembuka link yang sama di dua tab.
- Nilai token hanya dibaca lewat helper dan tidak ditulis di spec maupun fixture.

## Test Steps

### Token valid merender halaman Setup New Password

1. Buat satu token reset aktif milik
   `Fixture.authResetPassword.users.activated.email` memakai
   `Fixture.authResetPassword.tokens.seedActiveToken`
2. Susun tautan reset dari token tersebut memakai
   `Fixture.authResetPassword.tokens.linkForActiveToken`
3. Buka tautan reset tersebut di browser
4. Verifikasi halaman Setup New Password tampil
5. Verifikasi judul halaman adalah "Setup New Password"
6. Verifikasi subtitle di bawah judul menyebut email lengkap user tersebut pada kalimat
    "Set a new password to log in for [email]."
7. Verifikasi field Password dan field Confirm Password tampil dalam keadaan kosong
8. Verifikasi tombol "Reset Password" tampil dalam keadaan enabled
9. Verifikasi checklist Password Policy tampil di halaman
10. Verifikasi tidak ada navigasi ke halaman 404 maupun halaman lain

### Validasi link bersifat read-only

11. Catat status token reset milik user tersebut
12. Muat ulang halaman Setup New Password
13. Verifikasi halaman Setup New Password tetap tampil setelah muat ulang
14. Verifikasi field Password dan field Confirm Password tetap kosong setelah muat ulang
15. Muat ulang halaman Setup New Password beberapa kali berturut-turut
16. Verifikasi halaman Setup New Password tetap tampil pada setiap muat ulang
17. Verifikasi status token reset milik user tersebut tetap "active" setelah semua muat ulang
18. Verifikasi token tidak berubah status menjadi "consumed" oleh proses validasi link
19. Verifikasi tidak ada email reset baru yang dibuat oleh proses validasi link

### Dua tab membuka link yang sama

20. Susun ulang tautan reset dari token aktif tersebut memakai
    `Fixture.authResetPassword.tokens.linkForActiveToken`
21. Buka tautan reset tersebut di tab pertama
22. Buka tautan reset yang sama di tab kedua hampir bersamaan
23. Verifikasi tab pertama merender halaman Setup New Password
24. Verifikasi tab kedua merender halaman Setup New Password
25. Verifikasi tidak ada tab yang merender halaman 404
26. Verifikasi tidak ada caption error dan tidak ada toast error yang muncul di kedua tab
27. Verifikasi status token reset milik user tersebut tetap "active"
28. Verifikasi tidak ada request yang mengubah state, sehingga kedua tab hanya melakukan pembacaan

## Notes

- Yang diuji pada subbagian kedua adalah bahwa memuat ulang halaman tidak mengonsumsi token. Kalau
  validasi link tidak read-only, muat ulang pertama saja sudah membuat token tidak berlaku lagi.
- Subbagian ketiga memakai token yang sama untuk dua tab, dan hasilnya normal pada kedua tab
  karena pada tahap ini belum ada aksi yang mengubah state. Perilaku berbeda muncul pada tahap
  submit dan diuji di spec 022 serta spec 024.
- Subtitle halaman diambil dari `Fixture.authResetPassword.captions` sesuai aturan
  e2e-conventions.md bagian 9, dengan email user disisipkan oleh test.
- Nilai token hanya dibaca lewat helper dan tidak ditulis di file, sesuai aturan
  e2e-conventions.md bagian 5.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Reset Password". Aturan `[Submit]` dan
  `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit entitas, bukan
  untuk halaman autentikasi.