---
id: TC-AC-SU-E2E-040-role-matrix-negatif-penolakan-menu-read-only-dan-direct-url-403
title: "Role Matrix Negatif: penolakan sidebar menu dan Direct URL 403 untuk Client, Group Manager, role lain, dan mode Read Only"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-21
  - TC-AC-SU-153
  - TC-AC-SU-154
  - TC-AC-SU-239
coverage:
  web: automated
---

# Role Matrix Negatif: penolakan sidebar menu dan Direct URL 403 untuk Client, Group Manager, role lain, dan mode Read Only

## Prerequisites

- Terdapat akun login untuk: Client User, Group Manager (tanpa Manage user and role), User tanpa role user management, dan Read Only User

## Test Steps

### Penolakan Menu dan Direct URL untuk Client, Group Manager, dan Role Lain

1. Login sebagai pengguna dengan entitas Client:
2.   - Verifikasi menu `Settings > User` TIDAK TAMPIL di sidebar
3.   - Akses langsung URL `.../settings/user` dan `.../settings/user/[id]` dari address bar peramban
4.   - Verifikasi akses ditolak sistem (403 Forbidden / diarahkan ke halaman unauthorized)
5. Login sebagai pengguna berstatus Group Manager (tanpa Global Role "Manage user and role"):
6.   - Verifikasi menu `Settings > User` tidak tampil di sidebar
7.   - Akses langsung URL User List, verifikasi akses ditolak 403 Forbidden
8. Login sebagai pengguna dengan role lain (bukan user management):
9.   - Verifikasi menu disembunyikan dan direct URL ditolak

### Mode Read Only: Visibilitas Terbatas Tanpa Kontrol Write

1. Login sebagai pengguna dengan tier Read Only
2. Buka menu `Settings > User`, verifikasi halaman terbuka dalam mode baca murni:
3.   - Checkbox bulk dan Bulk Action Bar tersembunyi (hidden)
4.   - Row action Resend Activation / Confirmation Email tersembunyi
5.   - Switch Active berstatus Disabled dengan tooltip Read Only
6.   - Tombol `Assign Group` pada Tab Role tersembunyi

## Notes

- Role matrix negatif memastikan perlindungan defense-in-depth pada UI dan URL routing.
