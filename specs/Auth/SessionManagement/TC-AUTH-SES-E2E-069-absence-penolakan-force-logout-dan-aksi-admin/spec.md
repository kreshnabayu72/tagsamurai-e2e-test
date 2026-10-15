---
id: TC-AUTH-SES-E2E-069-absence-penolakan-force-logout-dan-aksi-admin
title: "Absence Pencatatan: Penolakan Server, Force-logout Idempotent, dan Aksi Admin"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-136
  - TC-AUTH-SES-142
  - TC-AUTH-SES-233
  - TC-AUTH-SES-234
  - TC-AUTH-SES-239
  - TC-AUTH-SES-250
  - TC-AUTH-SES-320
  - TC-AUTH-SES-322
  - TC-AUTH-SES-327
coverage:
  web: automated
---

# Absence Pencatatan: Penolakan Server, Force-logout Idempotent, dan Aksi Admin

## Prerequisites

- Mode: FE+BE.
- Client uji:
  - Client Alpha `Alpha Logistik` (Tabel Data Uji Pre-setup #5): batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5.
  - Client Q2 (Tabel Data Uji Pre-setup #12): subscription Fixed Asset dan Supply Asset Active, batas idle 15 menit. Kuota concurrent Fixed Asset dinaikkan dari 2 ke 8 di hook `before` lewat `Admin Console > License Allocation` oleh akun aktor principal Admin Console (Tabel Data Uji Pre-setup #4) `principalAdminConsole_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD`, supaya sesi-produk `Sari Wibowo`, `Siti Ramadhan`, dan `Joko Saputra` dapat aktif bersamaan; dipulihkan ke 2 di hook `after`.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`: untuk user Client Alpha (Tabel Data Uji Pre-setup #1), untuk user Client Q2 dengan scope Client Q2 (Tabel Data Uji Pre-setup #26)): sepuluh user, password semua user `Spectra.env.SES_PASSWORD`, email bersuffix per run. Activated, Active ON, profil BASE, MFA dan Agreement tidak terpicu kecuali dinyatakan lain:
  - TC-AUTH-SES-320 (Client Alpha): `Mega Rahayu` (`megarahayu+{runId}-069@qwertysystem.net`), profil PENDING (belum aktivasi; Tabel Data Uji Pre-setup #25); token autentikasi diterbitkan alat uji
  - TC-AUTH-SES-250 (Client Alpha): `Dimas Nugroho` (`dimasnugroho+{runId}-069@qwertysystem.net`), profil INACTIVE (Toggle Active OFF); token autentikasi diterbitkan alat uji
  - TC-AUTH-SES-233 (Client Alpha): `Reza Wibowo` (`rezawibowo+{runId}-069@qwertysystem.net`) dengan sesi platform dan sesi-produk Fixed Asset Active di-seed lewat login API dan pembukaan produk API; user aktor tanpa capability `Sari Nugroho` (`sarinugroho+{runId}-069@qwertysystem.net`) tanpa Global Role Manage Global License
  - TC-AUTH-SES-234 (Client Alpha): `Galih Maulana` (`galihmaulana+{runId}-069@qwertysystem.net`) dengan sesi platform dan sesi-produk Fixed Asset Active di-seed lewat API; admin pengirim request adalah Admin License `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #2) di Client Q2, kredensial `Spectra.env.FA_MGL_PASSWORD`
  - TC-AUTH-SES-322 (Client Q2): `Sari Wibowo` (`sariwibowo+{runId}-069@qwertysystem.net`) dengan App Access Fixed Asset dan Supply Asset dan Global Role Manage Global License di Client Q2 (admin yang me-force-logout dirinya sendiri); sesi platform web Active di Browser Self dan sesi-produk Fixed Asset Active di-seed lewat login API dan pembukaan produk API
  - TC-AUTH-SES-327 (Client Alpha): `Lestari Maulana` (`lestarimaulana+{runId}-069@qwertysystem.net`), Active ON di Global Settings dan di produk Fixed Asset; sesi web Active di Browser A, sesi-produk Fixed Asset Active (seat terpakai) dan sesi-produk Supply Asset Active
  - TC-AUTH-SES-239 (Client Q2): `Siti Ramadhan` (`sitiramadhan+{runId}-069@qwertysystem.net`) dengan App Access Fixed Asset dan Supply Asset; sesi platform dan sesi-produk Fixed Asset Active di-seed lewat login API dan pembukaan produk API
  - TC-AUTH-SES-142 (Client Alpha): `Reza Nugroho` (`rezanugroho+{runId}-069@qwertysystem.net`); sesi web dibuat di langkah (lihat Notes)
  - TC-AUTH-SES-136 (Client Q2): `Joko Saputra` (`jokosaputra+{runId}-069@qwertysystem.net`) dengan App Access Fixed Asset dan Supply Asset; sesi platform dan sesi-produk Fixed Asset dibuat di langkah (lihat Notes)
- Konteks dan akun (dibuka di hook `before`, login pertama tiap konteks ada di hook):
  - Browser Log Alpha: akun Total Control (Global Settings) untuk Client Alpha (Tabel Data Uji Pre-setup #1) di atas, dipakai membaca `Global Settings > Activity Log > Session`, `Activity Log > Session` milik Fixed Asset, `Global Settings > User > Detail > User Log`, dan menonaktifkan serta mengaktifkan kembali status user di produk Fixed Asset (TC-AUTH-SES-327).
  - Browser Log Q2: akun Total Control (Global Settings) scope Client Q2 (Tabel Data Uji Pre-setup #26) di atas, dipakai membaca `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` untuk user Client Q2.
  - Browser Lisensi: Admin License `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.FA_MGL_PASSWORD`), dipakai mengirim request force-logout (TC-AUTH-SES-234), mengklik [Force Logout] dan [Confirm Logout] pada TC-AUTH-SES-239, dan membuka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) pada TC-AUTH-SES-136 dan 239.
  - Browser Self (memuat sesi seed `Sari Wibowo`), Browser A (memuat sesi seed `Lestari Maulana`; pada TC-AUTH-SES-239 memuat sesi seed `Siti Ramadhan`; pada TC-AUTH-SES-142 memuat sesi `Reza Nugroho`), dan Browser C (konteks bersih, dibuka ulang per TC).
- Suite berjalan serial (`parallel: false`); state global yang diubah: kuota Fixed Asset Client Q2 (dinaikkan, dipulihkan ke 2), jam server (dimajukan sendiri tanpa jam browser pada TC-AUTH-SES-142 dan dikembalikan sebelum Log Out) dan jam server bersama jam browser/perangkat (dimajukan bersama pada TC-AUTH-SES-136, dikembalikan bersama dengan langkah eksplisit sebelum akun pembaca membuka log), penahanan request heartbeat Browser A lewat proxy jaringan (TC-AUTH-SES-142, dilepas dengan langkah eksplisit), status `Lestari Maulana` di produk Fixed Asset (dinonaktifkan lalu diaktifkan kembali pada TC-AUTH-SES-327). Hook `after` mengembalikan semuanya walau spec gagal di tengah.
- Hook `after`: kembalikan jam server dan jam browser/perangkat ke waktu nyata, lepaskan penahanan heartbeat di proxy jaringan, aktifkan kembali `Lestari Maulana` di produk Fixed Asset bila masih nonaktif, pulihkan kuota Fixed Asset Client Q2 ke 2, akhiri semua sesi seed dan sesi-produk, tutup semua konteks browser, hapus kesepuluh user. Pembersihan tidak berasumsi seeding berhasil penuh. Sesi Browser Log dipulihkan ke akun default suite.
- Environment variable: `GS_TC_PASSWORD`, `FA_MGL_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `SES_PASSWORD`. Password dan token tidak ditulis di spec atau fixture.
- Kemampuan teknis: banyak konteks browser bersamaan (Browser Log Alpha, Browser Log Q2, Browser Lisensi, Browser Self, Browser A, Browser C); client HTTP yang mengirim request langsung ke API dari dalam konteks halaman browser supaya reaksi UI dapat diamati (Create Session dengan token tertentu; `POST /v2/iam/auth/product-sessions/{id}/force-logout` dengan header `X-Session-ID` sesi platform pengirim, TC-AUTH-SES-233, 234, 322; sumber: `auth/session-management/API/openapi.yaml`); alat uji yang menerbitkan token autentikasi untuk user PENDING dan INACTIVE; klik bersamaan di Browser Lisensi dan Browser A dengan selisih kurang dari 1 detik (TC-AUTH-SES-239); pengatur jam server uji (Tabel Data Uji Pre-setup #18) yang dapat dimajukan sendiri (TC-AUTH-SES-142) atau bersama jam browser/perangkat (TC-AUTH-SES-136) dan dikembalikan ke waktu nyata, dengan sinyal aktivitas (gerak mouse) lalu heartbeat Browser Log Alpha, Browser Log Q2, dan Browser Lisensi berjalan di antara dua kali pemajuan sehingga sesi ketiganya tidak kedaluwarsa; proxy jaringan yang menahan request heartbeat Browser A (TC-AUTH-SES-142); pembacaan stempel waktu entri log untuk membedakan entri baru dari entri seeding; reCAPTCHA mode uji di environment untuk login web (halaman Login with Password).
- Akun yang dipakai: user uji masing-masing TC di Browser A, Browser C, Browser Self, dan lewat API; akun aktor di Browser Log Alpha, Browser Log Q2, dan Browser Lisensi.

## Test Steps

### TC-AUTH-SES-320 (bagian absence, butir b): Create Session user belum aktivasi tidak dicatat

1. Buka Browser C (konteks baru) di halaman `Auth > Login with Password`
2. Di Browser Log Alpha buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Mega Rahayu`, lalu catat baseline: jumlah entri dan stempel waktu entri terbaru di kedua surface
3. Kirim dari Browser C request Create Session dengan token autentikasi `Mega Rahayu` (belum aktivasi) → server menolak dan Browser C diarahkan ke halaman Login
4. Di Browser Log Alpha buka `Global Settings > Activity Log > Session` dan cari entri `Mega Rahayu` lewat Note dan email yang bertambah dibanding baseline sejak langkah 3 dimulai
5. Verifikasi Tidak ada entri baru untuk `Mega Rahayu` di `Global Settings > Activity Log > Session` untuk kondisi Create Session ditolak karena user belum aktivasi
6. Buka `Global Settings > User > Detail > User Log` milik `Mega Rahayu` dan cari entri lewat Note dan email yang bertambah dibanding baseline sejak langkah 3 dimulai
7. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi Create Session ditolak karena user belum aktivasi

### TC-AUTH-SES-250 (bagian absence, butir b): Create Session user tidak aktif tidak dicatat

8. Buka Browser C (konteks baru) di halaman `Auth > Login with Password`
9. Di Browser Log Alpha buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Dimas Nugroho`, lalu catat baseline: jumlah entri dan stempel waktu entri terbaru di kedua surface
10. Kirim dari Browser C request Create Session dengan token autentikasi `Dimas Nugroho` (Toggle Active OFF) → server menolak dan Browser C diarahkan ke halaman Login
11. Di Browser Log Alpha buka `Global Settings > Activity Log > Session` dan cari entri `Dimas Nugroho` lewat Note dan email yang bertambah dibanding baseline sejak langkah 10 dimulai
12. Verifikasi Tidak ada entri baru untuk `Dimas Nugroho` di `Global Settings > Activity Log > Session` untuk kondisi Create Session ditolak karena user tidak aktif
13. Buka `Global Settings > User > Detail > User Log` milik `Dimas Nugroho` dan cari entri lewat Note dan email yang bertambah dibanding baseline sejak langkah 10 dimulai
14. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi Create Session ditolak karena user tidak aktif

### TC-AUTH-SES-233 (bagian absence, butir b): Force-logout tanpa capability Manage Global License tidak dicatat

15. Di Browser C (konteks baru, Chrome on Windows) login dengan `sarinugroho+{runId}-069@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
16. Di Browser Log Alpha buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Reza Wibowo`, lalu catat baseline: jumlah entri dan stempel waktu entri terbaru di kedua surface
17. Kirim dari Browser C request `POST /v2/iam/auth/product-sessions/{id}/force-logout` langsung untuk sesi-produk Fixed Asset milik `Reza Wibowo` → server menolak dengan 403
18. Di Browser Log Alpha buka `Global Settings > Activity Log > Session` dan cari entri `Reza Wibowo` lewat Note dan email yang bertambah dibanding baseline sejak langkah 17 dimulai
19. Verifikasi Tidak ada entri baru untuk `Reza Wibowo` di `Global Settings > Activity Log > Session` untuk kondisi request force-logout ditolak 403 karena aktor tanpa capability
20. Buka `Global Settings > User > Detail > User Log` milik `Reza Wibowo` dan cari entri lewat Note dan email yang bertambah dibanding baseline sejak langkah 17 dimulai
21. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi request force-logout ditolak 403 karena aktor tanpa capability
22. Di Browser Log Alpha buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Galih Maulana`, lalu catat baseline: jumlah entri dan stempel waktu entri terbaru di kedua surface

### TC-AUTH-SES-234 (bagian absence, butir a): Force-logout terhadap user di luar scope entitas admin tidak dicatat

23. Kirim dari Browser Lisensi (sesi Admin License Client Q2) request `POST /v2/iam/auth/product-sessions/{id}/force-logout` langsung untuk sesi-produk Fixed Asset milik `Galih Maulana` (Client `Alpha Logistik`) → server menolak dengan 403
24. Di Browser Log Alpha buka `Global Settings > Activity Log > Session` dan cari entri `Galih Maulana` lewat Note dan email yang bertambah dibanding baseline sejak langkah 23 dimulai
25. Verifikasi Tidak ada entri baru untuk `Galih Maulana` di `Global Settings > Activity Log > Session` untuk kondisi request force-logout ditolak 403 karena target di luar scope entitas admin
26. Buka `Global Settings > User > Detail > User Log` milik `Galih Maulana` dan cari entri lewat Note dan email yang bertambah dibanding baseline sejak langkah 23 dimulai
27. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi request force-logout ditolak 403 karena target di luar scope entitas admin
28. Di Browser Log Q2 buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Sari Wibowo`, lalu catat baseline: jumlah entri dan stempel waktu entri terbaru di kedua surface

### TC-AUTH-SES-322 (bagian absence, butir a): Admin me-force-logout dirinya sendiri tidak dicatat

29. Kirim dari Browser Self request `POST /v2/iam/auth/product-sessions/{id}/force-logout` langsung dengan header `X-Session-ID` berisi ID sesi platform `Sari Wibowo` dan `{id}` berisi ID sesi-produk Fixed Asset Active milik `Sari Wibowo` sendiri (target: diri sendiri) → server menolak dengan 403
30. Di Browser Log Q2 buka `Global Settings > Activity Log > Session` dan cari entri `Sari Wibowo` lewat Note dan email yang bertambah dibanding baseline sejak langkah 29 dimulai
31. Verifikasi Tidak ada entri baru untuk `Sari Wibowo` di `Global Settings > Activity Log > Session` untuk kondisi admin me-force-logout dirinya sendiri
32. Buka `Global Settings > User > Detail > User Log` milik `Sari Wibowo` dan cari entri lewat Note dan email yang bertambah dibanding baseline sejak langkah 29 dimulai
33. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi admin me-force-logout dirinya sendiri

### TC-AUTH-SES-327 (bagian absence, butir b): Pengaktifan kembali user di produk Fixed Asset tidak dicatat

34. Di Browser Log Alpha buka `Global Settings > User`, cari `Lestari Maulana`, buka Detail dan nonaktifkan status di produk Fixed Asset saja (status Global Settings tetap Active) → sesi-produk Fixed Asset `Lestari Maulana` berstatus Ended
35. Di Browser Log Alpha buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Lestari Maulana`, lalu catat baseline: jumlah entri dan stempel waktu entri terbaru di kedua surface
36. Di Browser Log Alpha aktifkan kembali status `Lestari Maulana` di produk Fixed Asset pada Detail yang sama
37. Buka Activity Log Session Fixed Asset dan cari entri `Lestari Maulana` lewat Note dan email yang bertambah dibanding baseline sejak langkah 36 dimulai
38. Verifikasi Tidak ada entri baru untuk `Lestari Maulana` di Activity Log Session Fixed Asset akibat pengaktifan kembali user di produk Fixed Asset
39. Buka `Global Settings > User > Detail > User Log` milik `Lestari Maulana` dan cari entri lewat Note dan email yang bertambah dibanding baseline sejak langkah 36 dimulai
40. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` akibat pengaktifan kembali user di produk Fixed Asset
41. Di Browser Log Q2 buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Siti Ramadhan`, lalu catat baseline: jumlah entri dan stempel waktu entri terbaru di kedua surface

### TC-AUTH-SES-239 (bagian absence, butir d): Race force-logout dan manual logout tidak menulis row log tambahan

42. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser), lalu buka konteks baru Browser A dengan memuat sesi web seed milik `Siti Ramadhan` (Chrome on Windows) → Portal — Product Hub tampil
43. Di Browser Lisensi buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset), pilih `Siti Ramadhan`, lalu klik [Force Logout] sampai dialog konfirmasi "Force Logout User" tampil
44. Di Browser A buka menu Profile
45. Klik [Confirm Logout] di Browser Lisensi dan Log Out di Browser A pada saat yang sama (klik bersamaan di kedua browser, selisih kurang dari 1 detik) → sesi berakhir tepat sekali
46. Di Browser Log Q2 buka `Global Settings > Activity Log > Session` dan cari entri `Siti Ramadhan` lewat Note dan email yang bertambah dibanding baseline sejak langkah 45 dimulai
47. Verifikasi Tidak ada row log tambahan dari sisi yang kalah di `Global Settings > Activity Log > Session`: row untuk `Siti Ramadhan` hanya milik pemenang (dua row `Logged out by admin` bila force-logout menang; row `Logged out` dan `Session ended` per sesi-produk anak bila manual logout menang), row `Logged out by admin` dan row `Logged out` atau `Session ended` tidak muncul bersamaan
48. Buka `Global Settings > User > Detail > User Log` milik `Siti Ramadhan` dan cari entri lewat Note dan email yang bertambah dibanding baseline sejak langkah 45 dimulai
49. Verifikasi Tidak ada row log tambahan dari sisi yang kalah di `Global Settings > User > Detail > User Log`: row untuk `Siti Ramadhan` hanya milik pemenang, row `Logged out by admin` dan row `Logged out` atau `Session ended` tidak muncul bersamaan

### TC-AUTH-SES-142 (bagian absence, butir b): Logout saat sesi sudah expired tidak dicatat

50. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser), lalu buat sesi web Active `Reza Nugroho` di Browser A baru (Chrome on Windows) lewat login API
51. Di Browser Log Alpha buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Reza Nugroho`, lalu catat baseline: jumlah entri dan stempel waktu entri terbaru di kedua surface
52. Tahan request heartbeat Browser A (sesi `Reza Nugroho`) lewat proxy jaringan
53. Majukan jam server saja 8 menit (jam browser/perangkat tidak dimajukan)
54. Gerakkan mouse di Browser Log Alpha, Browser Log Q2, dan Browser Lisensi (sinyal aktivitas) tanpa memuat ulang halaman
55. Tunggu heartbeat sesi Browser Log Alpha, Browser Log Q2, dan Browser Lisensi berjalan (menyegarkan ketiga sesi) tanpa memuat ulang halaman
56. Majukan jam server saja 8 menit lagi (total 16 menit; sesi web `Reza Nugroho` Expired sementara Browser A belum menampilkan dialog, ketiga sesi pembaca tetap berlaku)
57. Pulihkan jam server ke waktu nyata
58. Di Browser A klik menu Profile lalu pilih Log Out → Browser A diarahkan ke halaman Login
59. Di Browser Log Alpha login ulang dengan akun aktor Total Control (Global Settings) Client yang sama dan password `Spectra.env.GS_TC_PASSWORD` (jam digeser kumulatif melewati batas idle)
60. Di Browser Log Alpha buka `Global Settings > Activity Log > Session` dan cari entri `Reza Nugroho` lewat Note dan email yang bertambah dibanding baseline sejak langkah 58 dimulai
61. Verifikasi Tidak ada entri baru untuk `Reza Nugroho` di `Global Settings > Activity Log > Session` untuk kondisi Log Out saat sesi sudah Expired
62. Buka `Global Settings > User > Detail > User Log` milik `Reza Nugroho` dan cari entri lewat Note dan email yang bertambah dibanding baseline sejak langkah 58 dimulai
63. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi Log Out saat sesi sudah Expired
64. Lepaskan penahanan request heartbeat Browser A di proxy jaringan

### TC-AUTH-SES-136 (bagian absence, butir b): Force-logout terhadap sesi target yang sudah expired tidak dicatat

65. Buat sesi platform web Active dan sesi-produk Fixed Asset Active `Joko Saputra` lewat login API dan pembukaan produk API (tanpa konteks browser yang terbuka)
66. Di Browser Log Q2 buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Joko Saputra`, lalu catat baseline: jumlah entri dan stempel waktu entri terbaru di kedua surface
67. Di Browser Lisensi buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) sehingga baris `Joko Saputra` tampil (daftar tetap terbuka dan tidak dimuat ulang sesudahnya)
68. Majukan jam server dan jam browser/perangkat bersama 8 menit
69. Gerakkan mouse di Browser Lisensi dan Browser Log Q2 (sinyal aktivitas) tanpa memuat ulang daftar
70. Tunggu heartbeat sesi Browser Lisensi dan Browser Log Q2 berjalan (menyegarkan kedua sesi) tanpa memuat ulang daftar
71. Majukan jam server dan jam browser/perangkat bersama 8 menit lagi (total 16 menit; sesi `Joko Saputra` tanpa aktivitas melewati batas idle 15 menit, sesi Browser Lisensi dan Browser Log Q2 tetap berlaku)
72. Di Browser Lisensi klik [Force Logout] pada baris `Joko Saputra` (baris basi) → dialog konfirmasi "Force Logout User" muncul
73. Klik [Confirm Logout] → UI admin menampilkan Dialog "Session Already Expired"
74. Pulihkan jam server dan jam browser/perangkat ke waktu nyata
75. Di Browser Log Q2 login ulang dengan akun aktor Total Control (Global Settings) Client yang sama dan password `Spectra.env.GS_TC_PASSWORD` (jam digeser kumulatif melewati batas idle)
76. Di Browser Log Q2 buka `Global Settings > Activity Log > Session` dan cari entri `Joko Saputra` lewat Note dan email yang bertambah dibanding baseline sejak langkah 73 dimulai
77. Verifikasi Tidak ada entri baru untuk `Joko Saputra` di `Global Settings > Activity Log > Session` untuk kondisi force-logout terhadap sesi target yang sudah Expired
78. Buka `Global Settings > User > Detail > User Log` milik `Joko Saputra` dan cari entri lewat Note dan email yang bertambah dibanding baseline sejak langkah 73 dimulai
79. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi force-logout terhadap sesi target yang sudah Expired

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Spec absence (kelas g, prinsip 13) untuk klausa "tidak ada entri log / tidak dicatat" dari sembilan TC fungsional. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Asersi fungsional (dialog, toast, status sesi, penolakan 403, redirect ke Login) tidak diulang dan tetap di spec asal (S-05).
- Pembagian TC lintas spec: TC-AUTH-SES-136 dan 322 di `TC-AUTH-SES-E2E-042-admin-force-logout-license-concurrent-user`; TC-AUTH-SES-142 di `TC-AUTH-SES-E2E-043-manual-logout`; TC-AUTH-SES-233, 234, 250, dan 320 di `TC-AUTH-SES-E2E-064-defense-in-depth-server-side`; TC-AUTH-SES-239 di `TC-AUTH-SES-E2E-065-konkurensi-dan-urutan-event`; TC-AUTH-SES-327 di `TC-AUTH-SES-E2E-027-user-dinonaktifkan-di-produk-fixed-asset`. Spec ini hanya memuat bagian absence masing-masing; Notes spec asal merujuk ke spec ini.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-320, 250, 233, 234, 322, 327, 239, 142, 136 (urutan TC sumber 136, 142, 233, 234, 239, 250, 320, 322, 327). Penolakan server yang tidak mengubah data lebih dulu; TC-AUTH-SES-327 menonaktifkan dan mengaktifkan kembali user; TC-AUTH-SES-239 mengakhiri sesi; TC-AUTH-SES-142 dan 136 memajukan jam server uji sehingga ditaruh paling akhir. Tiap TC memakai user sendiri bersuffix `-069`, jadi urutan tidak membuat TC saling bergantung. Spec melewati sekitar 35 langkah karena sembilan TC masing-masing butuh konteks dan pembacaan dua surface log; bagian sesudah sebuah TC tetap bermakna walau TC sebelumnya gagal.
- Sesi `Reza Nugroho` (TC-AUTH-SES-142) dan `Joko Saputra` (TC-AUTH-SES-136) dibuat di langkah 50 dan 65, bukan di hook `before`, karena pemajuan jam server uji pada TC-AUTH-SES-142 membuat semua sesi seed lain kedaluwarsa; sesi `Joko Saputra` harus masih Active saat daftar admin dibuka. Jam server (TC-AUTH-SES-142, dipulihkan sebelum Log Out) dan jam server bersama jam browser/perangkat (TC-AUTH-SES-136) dipulihkan dengan langkah eksplisit sesudah pemicu dan sebelum akun pembaca membuka log (S-09); akun pembaca login ulang karena pergeseran kumulatif 16 menit melewati batas idle. Entri dicari lewat Note dan email user dan diasersi sebagai selisih terhadap baseline yang dicatat sebelum pemicu, bukan posisi teratas (S-12).
- Langkah dependensi disalin (S-04): TC-AUTH-SES-320 dan 250 dari langkah pengiriman request Create Session pada bagian TC-AUTH-SES-320 dan TC-AUTH-SES-250 spec `TC-AUTH-SES-E2E-064`; TC-AUTH-SES-233 dan 234 dari langkah login dan request langsung pada bagian TC-AUTH-SES-233 dan TC-AUTH-SES-234 spec `TC-AUTH-SES-E2E-064`; TC-AUTH-SES-322 dari langkah request force-logout pada bagian TC-AUTH-SES-322 spec `TC-AUTH-SES-E2E-042`; TC-AUTH-SES-327 dari TC-AUTH-SES-326 (langkah 34, menonaktifkan user di produk Fixed Asset); TC-AUTH-SES-239 dari langkah picu bersamaan (langkah 12 sampai 14) bagian TC-AUTH-SES-239 spec `TC-AUTH-SES-E2E-065`; TC-AUTH-SES-142 dari langkah Log Out saat sesi Expired pada bagian TC-AUTH-SES-142 spec `TC-AUTH-SES-E2E-043`; TC-AUTH-SES-136 dari langkah memajukan jam, sinyal aktivitas, dan [Force Logout] pada bagian TC-AUTH-SES-136 spec `TC-AUTH-SES-E2E-042`.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): perpindahan antar konteks browser; membuka Browser C; membuat sesi pada langkah 50 dan 65; menutup konteks Browser A TC sebelumnya (S-09); menahan heartbeat, memberi sinyal aktivitas (gerak mouse), dan menunggu heartbeat pembaca (langkah 52, 54, 55, 69, dan 70); mengembalikan jam server (dan jam browser/perangkat pada TC-AUTH-SES-136), login ulang akun pembaca di Browser Log Alpha dan Browser Log Q2, dan melepas penahanan heartbeat (hook `after` sebagai cadangan, S-09); mencatat baseline jumlah entri dan stempel waktu entri terbaru sebelum pemicu. Entri "baru" dibedakan lewat baseline dan pencarian Note+email: hanya entri yang dibuat sesudah langkah pemicu TC itu yang dihitung (langkah 3, 10, 17, 23, 29, 36, 45, 58, dan 73). Pada TC-AUTH-SES-327, baris `Session ended` dari penonaktifan (langkah 34) menjadi pembanding alami sehingga asersi absence bermakna.
- Surface log: TC-AUTH-SES-327 menyebut `Activity Log > Session` milik Fixed Asset, jadi dibaca di langkah 37. Untuk TC-AUTH-SES-233, 234, dan 322, TC merujuk kondisi yang sama dengan TC-AUTH-SES-203 yang menandai surface produk `[DEFERRED]` (NC-15, forward-dependency PRD Activity Log produk); spec ini membaca `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`. Spec absence `TC-AUTH-SES-E2E-060` (TC-AUTH-SES-203) tetap membaca surface produk bila sudah tersedia.
- Temuan untuk QA:
  - TC-AUTH-SES-322 Precondition menyebut dua pelaku: user `Sari Wibowo` (BASE, Client Q2) dan Admin License #2; Langkah Uji tidak memakai `Sari Wibowo` dan spec `TC-AUTH-SES-E2E-042` memakai akun #2. Spec ini men-seed `Sari Wibowo` sebagai admin dengan Global Role Manage Global License supaya entri log yang dibaca milik user ini saja dan tidak tercampur dengan aksi spec lain yang memakai akun #2; perlu konfirmasi QA bahwa `Sari Wibowo` adalah admin pelaku.
  - TC-AUTH-SES-233, 234, dan 322 Expected tidak menyebut surface log; spec mengikuti TC-AUTH-SES-203 (Global Settings Activity Log Session dan User Log target) tanpa surface produk karena `[DEFERRED]`. Log yang mungkin ditulis atas nama aktor penolak tidak dibaca karena TC tidak menyebutnya.
  - TC-AUTH-SES-250 dan 320 menyebut "endpoint Create Session" dan "token autentikasi" user PENDING atau INACTIVE tanpa path dan cara memperolehnya; endpoint tidak ada sebagai endpoint publik di `auth/session-management/API/openapi.yaml`, jadi spec tidak menulis path dan mengandalkan alat uji (sama dengan `TC-AUTH-SES-E2E-064`).
  - TC-AUTH-SES-239 Expected d ("tanpa row log tambahan") tidak menyebut tolok ukur row; pemenang tidak dapat ditentukan sebelumnya, jadi spec mengasersi bahwa row yang tercatat hanya milik pemenang dan tidak ada row dari kedua sisi sekaligus.
  - TC-AUTH-SES-136 dan 142 memakai pemajuan jam server uji yang juga membuat sesi pembaca log kedaluwarsa bila melewati batas idle; spec memajukan jam dua kali dengan heartbeat pembaca di antaranya, dan interval heartbeat perlu dipastikan tim FE (sama dengan Temuan spec `TC-AUTH-SES-E2E-042`). Heartbeat hanya dikirim bila ada sinyal aktivitas, jadi spec menggerakkan mouse di Browser Log Alpha, Browser Log Q2, dan Browser Lisensi (TC-AUTH-SES-142) serta Browser Lisensi dan Browser Log Q2 (TC-AUTH-SES-136) sebelum tiap menunggu heartbeat; TC-AUTH-SES-142 tidak menyebut sinyal aktivitas ini.
  - TC-AUTH-SES-142 precondition b memajukan hanya waktu server (waktu browser tidak dimajukan) dan memulihkan waktu server sebelum Log Out; spec mengikuti urutan itu dan menahan heartbeat Browser A lewat proxy jaringan supaya sesi tetap stale tanpa dialog.
  - TC-AUTH-SES-239 memicu force-logout dan manual logout lewat klik UI di dua browser (Browser Lisensi dan Browser A) dan tidak menyebut sesi web yang dipakai Browser A; spec memuat sesi web seed `Siti Ramadhan` di Browser A, sama dengan spec `TC-AUTH-SES-E2E-065`.
  - TC-AUTH-SES-136 Expected b dan TC-AUTH-SES-142 Expected b tidak menyebut apakah kedaluwarsa idle sendiri menulis entri; spec membatasi pencarian ke entri yang dibuat sesudah klik [Confirm Logout] (langkah 73) atau Log Out (langkah 58).
  - TC-AUTH-SES-327 Post Condition membatasi absence pada "pengaktifan kembali"; surface `Global Settings > Activity Log > Session` tidak dibaca karena TC hanya menyebut `Activity Log > Session` milik Fixed Asset dan `User Log` (langkah 37 dan 39).
- Alur login user uji pada langkah 15 mengikuti TC apa adanya (klik [Log in]) dan TC tidak menyebut widget reCAPTCHA; spec tidak menambahkannya.
- Pengecualian `P-5` (a): pemicu kelas lain (pergeseran jam, request langsung, konteks kedua) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC memakai user dan baseline sendiri.
