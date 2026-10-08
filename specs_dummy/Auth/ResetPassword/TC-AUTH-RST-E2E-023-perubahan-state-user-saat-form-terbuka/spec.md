---
id: TC-AUTH-RST-E2E-023-perubahan-state-user-saat-form-terbuka
title: "Perubahan state user di tengah alur: konfirmasi ubah email, token email lama, user dinonaktifkan, dan token expired saat form terbuka"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-RST-114
  - TC-AUTH-RST-115
  - TC-AUTH-RST-131
  - TC-AUTH-RST-132
  - TC-AUTH-RST-133
  - TC-AUTH-RST-141
coverage:
  web: automated
---

# Perubahan state user di tengah alur: konfirmasi ubah email, token email lama, user dinonaktifkan, dan token expired saat form terbuka

## Prerequisites

- User belum login (guest); form Setup New Password terbuka untuk `budisantoso@qwertysystem.net` dengan token valid.
- Admin `superAdminGlobalSettings_automated_qaTeam1@qwertysystem.net` memiliki akses ke Global Settings > User dan Activity Log > Session.
- Environment uji mendukung manipulasi waktu server, sesi paralel, dan fixture BE (penyetelan callback invalidation).

## Test Steps

### Konfirmasi perubahan email meng-invalidate token reset aktif

1. Terbitkan token reset aktif untuk `budisantoso@qwertysystem.net`
2. Melalui sesi admin di Global Settings > User, inisiasi dan konfirmasi perubahan email user "Budi Santoso" menjadi `budi.santoso@qwertysystem.net`
3. Periksa status token reset milik email lama di database
4. Verifikasi token reset aktif milik email lama otomatis diubah statusnya menjadi `invalidated`
5. Buka tautan reset lama tersebut di browser
6. Verifikasi sistem menolak dan merender Halaman 404 varian Expired ("Reset Link Expired")

### Token milik email lama yang belum ter-invalidate callback tetap ditolak (TC-141)

7. Setel user `agusprasetyo@qwertysystem.net` berstatus Active dengan token reset aktif terbit untuk email lamanya, lalu email user diganti melalui fixture BE TANPA menjalankan callback invalidation token (kondisi sebagaimana TC-141)
8. Buka tautan reset dari email lama tersebut di browser
9. Verifikasi Halaman 404 varian Expired ("Reset Link Expired") tampil dan Setup New Password tidak dirender
10. Buka Activity Log > Session menggunakan sesi admin
11. Verifikasi tercatat tepat 1 entri baru Activity "Reset Password", Status "Failed", dan Note "Reset link expired"
12. Verifikasi token di-invalidate (tidak dapat dipakai meskipun callback invalidation tidak dijalankan)

### Konfirmasi perubahan email saat form Setup New Password sedang terbuka

13. Siapkan form Setup New Password yang sedang terbuka aktif di browser untuk user lain
14. Melalui sesi admin, lakukan konfirmasi perubahan email untuk user tersebut
15. Kembali ke tab form Setup New Password yang masih terbuka
16. Masukkan password baru yang valid lalu klik tombol [Reset Password]
17. Verifikasi server menolak submit dan browser beralih ke Halaman 404 varian Expired
18. Verifikasi password akun tidak diperbarui

### User dinonaktifkan (Inactive) saat form Setup New Password terbuka

19. Buka form Setup New Password dengan token valid untuk user aktif
20. Melalui sesi admin di Global Settings > User, ubah status akun user tersebut menjadi Inactive
21. Kembali ke tab Setup New Password lalu klik tombol [Reset Password] dengan data valid
22. Verifikasi server mendeteksi status akun Inactive dan menolak submit
23. Verifikasi browser menampilkan Halaman 404 varian Expired
24. Verifikasi token di-invalidate seketika dan tercatat log Failed / "Reset link expired"

### Submit setelah token melewati batas 24 jam saat form terbuka

25. Buka form Setup New Password dengan token valid
26. Biarkan form terbuka dan simulasikan waktu server dimajukan sehingga token melewati usia 24 jam (misal 24 jam 5 menit)
27. Pada form yang masih terbuka, klik tombol [Reset Password] dengan password valid
28. Verifikasi server menolak submit karena token telah expired saat dievaluasi
29. Verifikasi browser menampilkan Halaman 404 varian Expired ("Reset Link Expired")
30. Verifikasi tercatat log Failed / "Reset link expired"

### Sinkronisasi perubahan status user terhadap Request baru

31. Melalui sesi admin, aktifkan kembali akun user yang sebelumnya Inactive
32. Buka halaman Reset Password sebagai guest dan lakukan request reset untuk user tersebut
33. Verifikasi request langsung diproses sukses menuju Email Sent!, membuktikan sinkronisasi status bersifat realtime

## Notes

- Sesuai PRD §9.4.2 baris 21 & 25 serta §9.7 baris 6, setiap perubahan identitas email terkonfirmasi atau penonaktifan akun akan membatalkan token reset yang sedang aktif demi keamanan akun.
- Validasi akhir di server (`POST /confirm`) selalu mengecek ulang keabsahan token dan status akun user secara realtime sebelum mengeksekusi penyimpanan password.
- Sesuai PRD §9.2 F-AUTHRST-03/04, §9.4.2 baris 40, dan §9.8 (`TC-AUTH-RST-141`), server tetap memvalidasi token terhadap email terkini dan menolak dengan 404 varian Expired (tepat 1 log Failed / "Reset link expired") meskipun callback invalidation tidak sempat dijalankan saat email diganti.
- Tambahan `TC-AUTH-RST-141` menutup gap coverage Automatable yang sebelumnya belum tercakup spec (GAP-RST-E2E-001).