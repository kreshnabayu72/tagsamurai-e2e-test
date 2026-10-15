---
id: TC-AUTH-MFA-E2E-018-akses-halaman-mfa-dan-navigasi-browser
title: "Akses Halaman MFA dan Navigasi Browser"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-19
  - TC-AUTH-MFA-20
  - TC-AUTH-MFA-21
  - TC-AUTH-MFA-137
coverage:
  web: automated
---

# Akses Halaman MFA dan Navigasi Browser

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`), password user `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-19: `Bayu Saputra` (`bayusaputra+{runId}-018@qwertysystem.net`), profil FIRST (Tabel Data Uji Pre-setup #3: Activated, Active ON, belum pernah login di platform mana pun, Authenticator belum terdaftar) dengan role Read Only pada Global Settings (role di-assign saat seeding; pengguna ini adalah akun yang login pada TC-AUTH-MFA-19, bukan akun aktor)
  - TC-AUTH-MFA-21: `Eko Prasetyo` (`ekoprasetyo+{runId}-018@qwertysystem.net`), profil BASE (Tabel Data Uji Pre-setup #2: Activated, Active ON, sudah login sukses di web dari browser uji A sehingga device dikenali, login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari, Authenticator sudah terdaftar, persetujuan Privacy Policy versi terbaru sudah tersimpan)
  - TC-AUTH-MFA-137: `Cindy Oktavia` (`cindyoktavia+{runId}-018@qwertysystem.net`), profil NEWDEVE (Tabel Data Uji Pre-setup #5: seperti BASE, tetapi login dari browser uji B yang ID device-nya belum ada di daftar trusted device; Authenticator sudah terdaftar, persetujuan Privacy Policy versi terbaru sudah tersimpan)
  - TC-AUTH-MFA-20 tidak membutuhkan user: Langkah Uji dan Expected hanya membuka alamat halaman MFA langsung tanpa sesi.
- Seeding state BE per user: `Bayu Saputra` hanya profil FIRST dengan role Read Only Global Settings; `Eko Prasetyo` trusted device ber-ID device browser uji A, lokasi dan waktu login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari, Authenticator terdaftar, dan persetujuan Privacy Policy versi terbaru tersimpan; `Cindy Oktavia` seperti `Eko Prasetyo` tetapi ID device browser uji B belum ada di daftar trusted device. Mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah IP uji koneksi browser; hook `before` mengatur IP uji ke Jakarta (ID) (dipakai login TC-AUTH-MFA-21 dan 137 supaya tidak ada pemicu lokasi) dan hook `after` memulihkan IP uji ke nilai awal.
- Hook `after`: hapus ketiga user dan pulihkan IP uji. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. TC-AUTH-MFA-19 dimulai di konteks bersih pertama; TC berikutnya memulai konteks bersih secara eksplisit (jendela privat baru, browser uji A, atau browser uji B).
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: jendela privat; browser uji A (profil browser dengan ID device persisten yang didaftarkan sebagai trusted device `Eko Prasetyo` saat seeding BE) dan browser uji B (profil browser dengan ID device persisten yang belum dikenali); IP uji geo-IP Jakarta (ID) yang diatur di hook `before`; reCAPTCHA mode uji di environment; mail-catcher lingkungan uji untuk membaca kode OTP faktor-2 (TC-AUTH-MFA-19); membuka alamat halaman MFA langsung di bilah alamat browser (TC-AUTH-MFA-20, 21); muat ulang halaman (F5) dan tombol Back browser (TC-AUTH-MFA-137).
- Kemampuan teknis, pembacaan state BE: pembacaan jumlah sesi user dan status sesi pre-auth oleh sisi BE untuk Expected TC-AUTH-MFA-21 butir a (langkah 39) dan TC-AUTH-MFA-137 butir a dan b (langkah 52 dan 55); disediakan tim FE/BE karena tidak ada cara cek di UI atau Langkah Uji TC; endpoint/skrip tidak didefinisikan di TC, PRD, atau LLD.
- Akun dengan role: `Bayu Saputra` (Read Only, Global Settings) untuk TC-AUTH-MFA-19; user lain tanpa penekanan role (halaman MFA publik, tanpa gate role).

## Test Steps

### TC-AUTH-MFA-19: Halaman MFA dapat diselesaikan tanpa gate role oleh user dengan role Read Only

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `bayusaputra+{runId}-018@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → layar Confirm to Continue tampil
6. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
7. Verifikasi Title "Choose verification method" tampil identik dengan screening user lain
8. Verifikasi Subtitle "Select how you'd like to verify your identity" tampil identik dengan screening user lain
9. Verifikasi Opsi "OTP via email" tampil
10. Verifikasi Opsi "Authenticator app" tampil
11. Verifikasi Button [Login] tampil
12. Verifikasi Tidak ada elemen Choose Verification Method yang disembunyikan atau di-disable karena role
13. Pilih opsi "OTP via email" pada halaman Choose Verification Method
14. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `bayusaputra+{runId}-018@qwertysystem.net`
15. Verifikasi Title "Enter verification code" tampil identik dengan screening user lain
16. Verifikasi Subtitle "We sent a code to bayusaputra+{runId}-018@qwertysystem.net" tampil identik dengan screening user lain
17. Verifikasi 6 kotak digit tampil
18. Verifikasi Button Text [Resend code in Ns] tampil
19. Verifikasi Button [Login] tampil
20. Verifikasi Button Text [Use a different method] tampil
21. Verifikasi Tidak ada elemen OTP Verification yang disembunyikan atau di-disable karena role
22. Ketik 6 digit kode OTP faktor-2 dari email `bayusaputra+{runId}-018@qwertysystem.net` pada kotak digit
23. Verifikasi berhasil pada digit ke-6
24. Verifikasi Browser dialihkan ke Portal — Product Hub
25. Verifikasi Sesi aktif untuk `Bayu Saputra`

### TC-AUTH-MFA-20: Akses langsung ke halaman MFA tanpa sesi pre-auth tidak menghasilkan sesi penuh

26. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
27. Buka alamat halaman `Auth > MFA > OTP Verification` langsung di browser (tanpa melalui Login with Password atau Login with OTP)
28. Verifikasi Tidak ada sesi penuh yang dibuat
29. Verifikasi Portal — Product Hub tidak ditampilkan
30. Verifikasi Halaman login tampil (user harus memulai dari faktor-1)

### TC-AUTH-MFA-21: Pengguna yang sudah login membuka alamat halaman MFA langsung

31. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka browser uji A (device dikenali, tanpa sesi login)
32. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
33. Ketik `ekoprasetyo+{runId}-018@qwertysystem.net` pada field Email
34. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
35. Centang widget reCAPTCHA "I'm not a robot"
36. Klik button [Log in] → Portal — Product Hub tampil (single-step, Login with Password)
37. Buka alamat halaman `Auth > MFA > Authenticator Verification` langsung di browser yang sama
38. Verifikasi Sesi `Eko Prasetyo` tetap aktif
39. Verifikasi Tidak ada sesi tambahan yang dibuat (dibaca lewat pembacaan jumlah sesi user oleh sisi BE)
40. Verifikasi Browser dialihkan ke Portal — Product Hub (halaman MFA tidak ditampilkan)

### TC-AUTH-MFA-137: Muat ulang (F5) dan tombol Back pada halaman MFA

41. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka browser uji B (ID device belum dikenali, tanpa sesi login)
42. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
43. Ketik `cindyoktavia+{runId}-018@qwertysystem.net` pada field Email
44. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
45. Centang widget reCAPTCHA "I'm not a robot"
46. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
47. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
48. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
49. Muat ulang halaman (F5)
50. Verifikasi Halaman Authenticator Verification tetap tampil
51. Verifikasi Kotak digit kosong
52. Verifikasi Sesi pre-auth tetap berlaku (dibaca lewat pembacaan status sesi pre-auth oleh sisi BE)
53. Tekan tombol Back browser
54. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil
55. Verifikasi Sesi pre-auth tidak di-invalidate oleh tombol Back (dibaca lewat pembacaan status sesi pre-auth oleh sisi BE)
56. Verifikasi Tidak ada sesi penuh yang dibuat untuk `Cindy Oktavia`

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Urutan mengikuti urutan TC sumber (19, 20, 21, 137); tidak ada penyimpangan. Tiap TC memakai user sendiri. TC-AUTH-MFA-19 berakhir dengan sesi penuh `Bayu Saputra`; TC berikutnya membuka konteks bersih sehingga sesi itu tidak terbawa.
- Langkah penghubung tanpa awalan `Verifikasi` (langkah 26, 31, 41 membuka konteks bersih) bukan asersi tambahan (S-03).
- Verifikasi elemen pada langkah 7 sampai 12 dan 15 sampai 21 mengambil daftar elemen dari Expected TC-AUTH-MFA-01 dan TC-AUTH-MFA-04 sebagai pembanding "identik dengan screening user lain".
- Temuan untuk QA: (1) Post Condition TC tanpa langkah observasi dan tanpa Expected padanan tidak diasersi di spec ini (S-01): TC-AUTH-MFA-19 "Role Read Only `Bayu Saputra` tidak mengubah alur MFA" (kesimpulan Expected a dan b); TC-AUTH-MFA-20 "Tidak ada sesi untuk `Wulan Permata`" (padanan: Expected a, langkah 28 dan 29); TC-AUTH-MFA-21 "Satu sesi web aktif untuk `Eko Prasetyo`" (padanan: Expected a dan b, langkah 38 sampai 40). Post Condition absence dan pencatatan juga tidak diasersi (S-05): TC-AUTH-MFA-19 "satu entri Success `Login with password`" dan TC-AUTH-MFA-20 "tidak ada entri log". QA dapat menambah Expected atau langkah observasi di TC. (2) TC-AUTH-MFA-20 mencantumkan user `Wulan Permata` profil BASE di Precondition tetapi Langkah Uji dan Expected tidak memakai user itu (hanya membuka alamat halaman); user tidak di-seed karena tidak ada asersi yang memakainya. (3) TC-AUTH-MFA-21 mensyaratkan browser uji A (device dikenali) padahal Precondition dimulai dengan "Tanpa login (halaman publik)"; spec membuka browser uji A tanpa sesi aktif dan memulai dari login. (4) TC-AUTH-MFA-19 tidak menjelaskan cara role Read Only di-assign pada user profil FIRST; spec menuliskannya sebagai kondisi seeding. (5) TC-AUTH-MFA-137 Expected butir a ("sesi pre-auth tetap berlaku") dan butir b ("tidak di-invalidate") tidak memberi cara cek status sesi pre-auth di UI maupun di Langkah Uji; spec membacanya sebagai state BE lewat kemampuan pembacaan status sesi pre-auth oleh sisi BE yang disediakan tim FE/BE (langkah 52 dan 55), selain halaman yang tampil (langkah 50 dan 54). QA perlu menambah langkah observasi atau menyatakan cara cek lain. (6) Alamat halaman MFA pada TC-AUTH-MFA-20 dan 21 ditulis sebagai nama halaman (`Auth > MFA > OTP Verification`, `Auth > MFA > Authenticator Verification`) tanpa path URL di TC. (7) TC-AUTH-MFA-21 Expected butir a ("tidak ada sesi tambahan yang dibuat") tidak memberi cara cek jumlah sesi di UI maupun di Langkah Uji; spec membacanya lewat kemampuan pembacaan jumlah sesi user oleh sisi BE yang disediakan tim FE/BE (langkah 39). TC-AUTH-MFA-21 dan 137 juga tidak menyebut kondisi persetujuan Privacy Policy `Eko Prasetyo` dan `Cindy Oktavia`; spec menganggap sudah tersimpan karena Expected tidak melewati layar Confirm to Continue (TC-AUTH-MFA-21) dan alur ke Choose Verification Method (TC-AUTH-MFA-137). (8) Mekanisme seeding state BE (trusted device ber-ID device browser uji A, lokasi dan waktu login terakhir, Authenticator terdaftar) belum ada di Pre-setup (#20/#21 hanya memuat `last_logout_at`, pasangan negara, dan `first_login_at`); tidak ada endpoint atau skrip uji yang disebut di TC, PRD, atau LLD.
