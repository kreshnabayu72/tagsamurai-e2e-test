---
id: TC-AUTH-ACT-E2E-018-pengaruh-toggle-active-off
title: "Toggle Active user dalam kondisi OFF: link tetap valid dan aktivasi tetap berhasil"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-ACT-72
  - TC-AUTH-ACT-89
  - TC-AUTH-ACT-126
coverage:
  web: automated
---

# Toggle Active user dalam kondisi OFF: link tetap valid dan aktivasi tetap berhasil

## Prerequisites

- Browser publik tanpa sesi login (jendela privat) untuk alur aktivasi.
- Sesi login Role: Total Control (Global Settings) di browser admin, untuk menyetel dan mematikan toggle Active di `Global Settings > User > Login User`.
- 3 user seeding milik automation, masing-masing berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run), dengan toggle Active sudah berstatus OFF (status Activation tetap Pending Activation): user A (kasus buka link saja), user B (kasus aktifkan akun), user C (toggle dimatikan saat form terbuka); hook `after` membersihkan user.
- Akses API read-only untuk memverifikasi status Activation, status token, dan nilai toggle Active.

## Test Steps

### Link user dengan toggle Active OFF tetap menampilkan form Set Password (TC-AUTH-ACT-89)

1. Buka link aktivasi user A di jendela privat.
2. Verifikasi halaman `Auth > Account Activation > Set Password` tampil dengan Subtitle "Set a password to log in for <email user A>."
3. Verifikasi halaman Invalid Link tidak tampil.

### User Pending Activation dengan toggle OFF tetap bisa mengaktifkan akun (TC-AUTH-ACT-72)

4. Buka link aktivasi user B → halaman Set Password tampil normal (tidak ada halaman Invalid Link).
5. Ketik `Aman#Sandi8` pada field Password dan `Aman#Sandi8` pada field Confirm Password.
6. Klik button "Set Password".
7. Verifikasi halaman Activation Success tampil dengan Title "Account Activated".
8. Verifikasi via API bahwa status Activation user B berubah menjadi Activated dan token berstatus Consumed.
9. Verifikasi nilai toggle Active user B tetap pada nilai sebelum aktivasi (OFF).

### User dinonaktifkan saat form terbuka: submit tetap berhasil (TC-AUTH-ACT-126)

10. Buka link aktivasi user C → halaman Set Password tampil.
11. Ketik `Aman#Sandi8` pada field Password dan `Aman#Sandi8` pada field Confirm Password.
12. Pada browser admin, matikan toggle Active user C di `Global Settings > User > Login User` dan klik [Deactivate] pada dialog konfirmasi.
13. Kembali ke tab form dan klik button "Set Password".
14. Verifikasi halaman Activation Success tampil dengan Title "Account Activated".
15. Verifikasi tidak ada halaman Invalid Link dan tidak ada toast error.
16. Verifikasi via API bahwa status Activation user C berubah menjadi Activated, token berstatus Consumed, dan toggle Active tetap OFF.

## Notes

- Kasus baca saja (TC-AUTH-ACT-89) didahulukan; dua kasus aktivasi menyusul karena mengonsumsi token, dengan kasus perubahan state di tengah form sebagai penutup.
- Kebutuhan dua sesi browser (admin dan jendela privat) dicatat di Prerequisites.
