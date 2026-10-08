---
id: TC-AUTH-RST-E2E-013-halaman-404-token-expired
title: "Halaman 404 varian Expired: token kedaluwarsa 24 jam, akun nonaktif/dihapus, dan navigasi Request New Link"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-52
  - TC-AUTH-RST-53
  - TC-AUTH-RST-55
  - TC-AUTH-RST-60
  - TC-AUTH-RST-61
coverage:
  web: automated
---

# Halaman 404 varian Expired: token kedaluwarsa 24 jam, akun nonaktif/dihapus, dan navigasi Request New Link

## Prerequisites

- User belum login (guest); browser web siap mengakses tautan reset.
- Environment uji terisolasi khusus pengujian otomatis.
- Admin `superAdminGlobalSettings_automated_qaTeam1@qwertysystem.net` dapat mengubah status user dan membaca log.

## Test Steps

### Screening elemen Halaman 404 varian Expired

1. Buka tautan reset yang memuat token tidak aktif atau kadaluwarsa
2. Verifikasi halaman 404 varian Expired tampil dengan benar
3. Verifikasi logo TAG Samurai tampil di bagian atas
4. Verifikasi title halaman adalah "Reset Link Expired"
5. Verifikasi message halaman berbunyi: "This password reset link has expired. Reset links are valid for 24 hours."
6. Verifikasi tombol [Request New Link] tampil dengan styling primary

### Navigasi tombol [Request New Link]

7. Klik tombol [Request New Link] pada Halaman 404 varian Expired
8. Verifikasi browser berpindah ke halaman Request Reset Password (`/reset-password`)
9. Verifikasi field Email kosong dan form siap menerima input email baru

### Tautan berusia lebih dari 24 jam (Batas 24 jam 1 menit)

10. Siapkan token reset yang telah berusia 24 jam 1 menit sejak waktu pembuatan di database
11. Buka tautan reset tersebut di browser
12. Verifikasi sistem menolak token dan merender Halaman 404 varian Expired
13. Verifikasi status token di database berubah/tercatat sebagai `expired`

### Tautan dibuka setelah akun menjadi Inactive

14. Siapkan token reset aktif milik user yang awalnya berstatus aktif
15. Melalui sesi admin di Global Settings > User, ubah status akun user tersebut menjadi Inactive
16. Buka tautan reset milik user tersebut di browser
17. Verifikasi Halaman 404 varian Expired tampil ("Reset Link Expired")
18. Verifikasi token di database di-invalidate seketika
19. Buka Activity Log Session dan User Log menggunakan sesi admin
20. Verifikasi tercatat entri log baru dengan Activity "Reset Password", Status "Failed", dan Note "Reset link expired"

### Tautan dibuka setelah akun dihapus (Deleted)

21. Siapkan token reset aktif milik akun uji lain
22. Melalui sesi admin di Global Settings > User, lakukan penghapusan (delete) terhadap akun tersebut
23. Buka tautan reset akun yang sudah dihapus di browser
24. Verifikasi Halaman 404 varian Expired tampil ("Reset Link Expired")
25. Verifikasi token di-invalidate dan log tercatat dengan Note "Reset link expired"

## Notes

- Sesuai keputusan NC-04, pembukaan tautan reset saat akun nonaktif atau dihapus meng-invalidate token, menampilkan Halaman 404 varian Expired ("Reset Link Expired"), dan mencatat entri log Failed dengan Note "Reset link expired".
- Sesuai PRD §4.2 Halaman 5 dan §9.4.2 baris 23, masa berlaku token reset adalah tepat 24 jam sejak waktu pembuatan.
