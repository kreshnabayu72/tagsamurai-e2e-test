---
id: TC-AUTH-ACT-E2E-017-kondisi-data-target-user-dihapus
title: "Link milik user yang dihapus: saat dibuka maupun saat form terbuka"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-88
  - TC-AUTH-ACT-125
coverage:
  web: automated
---

# Link milik user yang dihapus: saat dibuka maupun saat form terbuka

## Prerequisites

- Browser publik tanpa sesi login (jendela privat) untuk alur aktivasi.
- Sesi login Role: Total Control (Global Settings) di browser admin, untuk menghapus user dari `Global Settings > User > Login User`.
- 2 user seeding milik automation, masing-masing berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run): user A (dihapus sebelum link dibuka) dan user B (dihapus saat form terbuka); keduanya sudah terhapus pada saat hook `after` berjalan.
- Akses API read-only untuk memastikan tidak ada akun yang teraktivasi.

## Test Steps

### Link milik user yang sudah dihapus menampilkan varian Expired (TC-AUTH-ACT-88)

1. Pada browser admin, hapus user A dari `Global Settings > User > Login User`.
2. Buka link aktivasi user A di jendela privat.
3. Verifikasi halaman Invalid Link varian Expired tampil: Title "Activation Link Expired" dan Body "This activation link has expired. Activation links are valid for 24 hours. Please contact your administrator to receive a new activation email."
4. Verifikasi tidak ada button CTA (tidak ada "Go to Login") dan form Set Password tidak ditampilkan.
5. Verifikasi tampilan identik dengan halaman link expired (tidak dibedakan dari penyebab lain).

### User dihapus saat form terbuka: submit diarahkan ke Invalid Link (TC-AUTH-ACT-125)

6. Buka link aktivasi user B di jendela privat → halaman `Auth > Account Activation > Set Password` tampil.
7. Ketik `Aman#Sandi8` pada field Password dan `Aman#Sandi8` pada field Confirm Password.
8. Pada browser admin, hapus user B dari `Global Settings > User > Login User`.
9. Kembali ke tab form dan klik button "Set Password".
10. Verifikasi tab form diarahkan ke halaman Invalid Link varian Expired dengan Title "Activation Link Expired".
11. Verifikasi tidak ada toast dan tidak ada akun yang teraktivasi.

## Notes

- Urutan dari kasus link sudah basi (non-destruktif terhadap sesi form) ke kasus perubahan state di tengah form; keduanya berakhir dengan data terhapus sehingga cocok sebagai penutup spec.
- Kebutuhan dua sesi browser (admin dan jendela privat) dicatat di Prerequisites.
