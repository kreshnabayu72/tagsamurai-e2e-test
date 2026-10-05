---
id: TC-AUTH-RST-E2E-016-navigasi-cta-halaman-404
title: Navigasi CTA pada halaman 404 link reset invalid
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-72
  - TC-AUTH-RST-73
coverage:
  web: automated
---

# Navigasi CTA pada halaman 404 link reset invalid

## Prerequisites

- Belum login dan session kosong.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE.
- Satu user berstatus Activated dan Active di Global Settings > User. Email-nya adalah
  `Fixture.authResetPassword.users.activated.email`.
- `Fixture.authResetPassword.tokens.seedExpiredToken` adalah cara membuat satu token reset yang
  sudah melewati masa berlaku milik user tersebut lewat API Global Settings > User.
- `Fixture.authResetPassword.tokens.seedConsumedToken` adalah cara membuat satu token reset yang
  statusnya sudah dipakai.
- `Fixture.authResetPassword.tokens.linkForToken` adalah cara menyusun tautan reset dari token
  tertentu tanpa menuliskan nilai token di file.
- `Fixture.authResetPassword.users.activated.email` sudah pernah melakukan request reset sebelumnya
  pada environment uji, sehingga form pada halaman tujuan bisa dibandingkan dengan keadaan setelah
  request. Kalau tidak, halaman tujuan tetap terbuka dengan form kosong dan itu kondisi yang valid.
- Nilai token hanya dibaca lewat helper dan tidak ditulis di spec maupun fixture.

## Test Steps

### CTA Request New Link pada varian Expired

1. Buat satu token reset milik user tersebut yang sudah expired memakai
   `Fixture.authResetPassword.tokens.seedExpiredToken`
2. Susun tautan reset dari token tersebut memakai `Fixture.authResetPassword.tokens.linkForToken`
3. Buka tautan reset tersebut di browser
4. Verifikasi CTA pada halaman adalah "Request New Link"
5. Klik "Request New Link"
6. Verifikasi navigasi ke halaman Reset Password terjadi
7. Verifikasi field Email pada halaman Reset Password tampil dalam keadaan kosong
8. Verifikasi widget reCAPTCHA tampil pada halaman tujuan
9. Verifikasi tombol "Reset Password" tampil dalam keadaan enabled
10. Verifikasi tidak ada toast error dan tidak ada halaman error yang tampil
11. Verifikasi tidak ada satu pun parameter token pada URL halaman tujuan

### CTA Go to Login pada varian Already Used

12. Buat satu token reset milik user tersebut yang statusnya sudah consumed memakai
    `Fixture.authResetPassword.tokens.seedConsumedToken`
13. Susun tautan reset dari token tersebut memakai `Fixture.authResetPassword.tokens.linkForToken`
14. Buka tautan reset tersebut di browser
15. Verifikasi CTA pada halaman adalah "Go to Login"
16. Klik "Go to Login"
17. Verifikasi navigasi ke halaman Login with Password terjadi
18. Verifikasi field Email pada halaman Login tampil dalam keadaan kosong
19. Verifikasi field Password pada halaman Login tampil
20. Verifikasi tidak ada toast error dan tidak ada halaman error yang tampil
21. Verifikasi tidak ada satu pun parameter token pada URL halaman tujuan

### Navigasi dari halaman Email Sent ke Login

22. Kembali ke halaman Email Sent lewat alur normal untuk mengisi kotak masuk dengan email reset
23. Verifikasi tombol "Resend" tampil pada halaman Email Sent
24. Verifikasi link "Log in with password" tampil pada halaman Email Sent
25. Klik link "Log in with password"
26. Verifikasi navigasi ke halaman Login with Password terjadi
27. Verifikasi halaman Login dengan Password tampil dengan field Email dan field Password
28. Verifikasi tidak ada halaman Email Sent yang masih terbuka setelah navigasi
29. Verifikasi tidak ada caption error dan tidak ada toast error yang tampil

## Notes

- Spec ini sengaja memakai token yang dibuat lewat API, bukan tautan dari email sungguhan, supaya tidak
  bergantung pada mailbox uji. Yang diuji murni navigasi dari halaman 404.
- Dua CTA diuji sebagai satu spec karena keduanya adalah topik yang sama, yaitu keluar dari halaman
  404, dan tidak ada state yang perlu diubah di antara keduanya.
- Navigasi dari halaman Email Sent ke Login sengaja ditambahkan di sini karena memakai label yang
  sama dengan CTA halaman 404, yaitu "Log in with password" atau "Go to Login", sehingga label yang
  sama terverifikasi konsisten di dua tempat sekaligus.
- Verifikasi URL halaman tujuan tidak membawa parameter token dilakukan supaya token tidak bocor
  lewat riwayat browser dan address bar.
- Label tombol mengikuti copy PRD apa adanya, yaitu "Request New Link" dan "Go to Login". Aturan
  `[Submit]` dan `[Save]` pada prd-conventions.md bagian 24.1 berlaku untuk form Create dan Edit
  entitas, bukan untuk halaman autentikasi.