---
id: TC-FA-LIC-E2E-115-sesi-lain-force-logout-ganda-sse-concurrent-user-seat
title: "Concurrent User dengan Sesi Lain: Pembaruan SSE dan Dialog Log Out pada Pengguna yang Di-Force-Logout"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-179
  - TC-FA-LIC-615
coverage:
  web: automated
---

# Concurrent User dengan Sesi Lain: Pembaruan SSE dan Dialog Log Out pada Pengguna yang Di-Force-Logout

## Prerequisites

- Mode: FE+BE.
- Akun sesi A (aktor hook `before`): Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun konteks lain (dibuka dan ditutup di langkah spec, hasilnya diasersi):
  - Default User (Pre-setup #7) `defaultUser_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_DU_PASSWORD` (konteks browser C pada TC-FA-LIC-615).
  - Total Control kedua (Pre-setup #22) `totalControlSecond_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC2_PASSWORD` (sesi API aktor pada TC-FA-LIC-615).
  - Budi Santoso (Pre-setup #14): email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA), disediakan tim FE; dipakai sebagai konteks browser pada TC-FA-LIC-179.
  Nama env `FA_TC_PASSWORD`, `FA_DU_PASSWORD`, dan `FA_TC2_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup dan penyetel state): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup yang diubah spec: fixture tabel sesi #26 (lima sesi cuplikan: Rudi Hartono, Dewi Lestari, Andi Pratama, Siti Rahma, Budi Santoso; Online Users 5/25) dan sesi aktif #14 (18 sesi, seat 25; sesi Budi Santoso Chrome on Windows tidak aktif lebih dari 2 jam). Pemulihan oleh fixture BE pemulih (disediakan tim FE/BE) di hook `before` dan `after` serta di awal tiap blok TC (pengecualian S-06: sesi Pre-setup tidak dapat dimiliki spec, suite berjalan serial). Efek yang dicatat: sesi Budi Santoso berakhir, Last Activity berubah, dan entri baru bertambah permanen di Changelog Concurrent User dan Activity Log.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak dikarang):
  - Asersi propagasi SSE didahului "Tunggu 5 detik tanpa memuat ulang halaman" (jendela standar pilihan spec, bukan nilai TC atau PRD).
- Konteks kedua adalah objek uji kelas c; spec ini tidak memakai `P-2` atau `P-7`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-615: Daftar Active Sessions dan Online Users diperbarui otomatis lewat SSE

1. Pulihkan fixture tabel sesi Pre-setup #26 lewat fixture BE (lima sesi, Online Users 5/25)
2. Sesi A: buka License > Concurrent User (halaman 1, tanpa Search), catat jumlah baris dan Online Users
3. Buka konteks browser C, login sebagai Default User (#7)
4. Sesi A: tunggu 5 detik tanpa memuat ulang halaman
5. Verifikasi baris sesi Default User disisipkan di baris teratas (Sort default Login Time terbaru)
6. Verifikasi Metric Summary Bar menjadi `Online Users: 6/25`
7. Verifikasi halaman tidak dimuat ulang dan tidak direset
8. Konteks C: logout sesi Default User
9. Sesi A: tunggu 5 detik tanpa memuat ulang halaman
10. Verifikasi baris Default User hilang
11. Verifikasi `Online Users: 5/25`
12. Sesi API admin lain (#22): Force Logout sesi Budi Santoso hingga Force Logout tersimpan
13. Sesi A: tunggu 5 detik tanpa memuat ulang halaman
14. Verifikasi baris Budi Santoso hilang
15. Verifikasi `Online Users: 4/25`
16. Sesi A: ketik Search `Dewi`, tekan Enter
17. Verifikasi baris Dewi Lestari tampil
18. Konteks C: login lagi sebagai Default User (#7)
19. Sesi A: tunggu 5 detik tanpa memuat ulang halaman
20. Verifikasi baris Default User tidak disisipkan (tidak cocok Search)
21. Verifikasi `Online Users: 5/25`
22. Verifikasi Search `Dewi` tetap aktif
23. Sesi A: klik `[Force Logout]` pada baris Dewi Lestari sehingga dialog `Force Logout User` terbuka
24. Konteks C: logout sesi Default User, lalu tutup konteks C dan hapus sesi login-nya
25. Sesi A: tunggu 5 detik tanpa memuat ulang halaman
26. Verifikasi dialog `Force Logout User` tetap terbuka dan tidak terpengaruh perubahan daftar
27. Tutup dialog dengan `[Cancel]`, klik icon panah `(←)` di kiri toolbar Search

### TC-FA-LIC-179: Pengguna yang di-force-logout menerima dialog Log Out

28. Pulihkan Pre-setup #14 lewat fixture BE (Online Users 18/25, sesi Budi Santoso aktif)
29. Buka konteks browser kedua, login sebagai Budi Santoso (Chrome on Windows)
30. Sesi A: ketik Search `Budi`, tekan Enter, klik `[Force Logout]` pada baris Budi Santoso, klik `[Confirm Logout]`
31. Browser Budi Santoso: amati layar
32. Verifikasi browser Budi menampilkan dialog `Log Out`
33. Verifikasi dialog `Log Out` non-dismissable
34. Verifikasi sesi Budi Santoso berakhir
35. Tutup konteks browser kedua dan hapus sesi login-nya

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 dan 28 memulihkan Pre-setup antar blok; langkah 3, 24, 29, dan 35 membuka dan menutup konteks lain (S-09); langkah 4, 9, 13, 19, dan 25 menunggu jendela SSE (bagian 6); langkah 27 menutup dialog dan Search; langkah 30 menemukan baris target lewat Search `Budi` (R-16).
- Urutan blok: TC-FA-LIC-615 (sesi bertambah dan berkurang, tanpa Force Logout yang dikonfirmasi) lebih dulu; TC-FA-LIC-179 (Force Logout oleh aktor) sesudahnya (S-10). Tiap blok dimulai dari pemulihan state lewat fixture BE sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-FA-LIC-87, 460, dan 173 ada di spec `TC-FA-LIC-E2E-169`.
- Temuan untuk QA:
  - TC-FA-LIC-179 berjudul "sisi pemicu" tetapi Expected mengasersi dialog `Log Out` di browser Budi Santoso (konteks kedua, kelas c); spec mengikuti Expected.
  - TC-FA-LIC-179 memakai akun login Budi Santoso yang email-nya tidak tertulis di Pre-setup TC.
  - TC-FA-LIC-615 langkah 6 dan TC-FA-LIC-179 tidak menyebut tombol `[Cancel]` atau cara menutup dialog; spec memakai `[Cancel]` pada dialog `Force Logout User` untuk membersihkan state.
