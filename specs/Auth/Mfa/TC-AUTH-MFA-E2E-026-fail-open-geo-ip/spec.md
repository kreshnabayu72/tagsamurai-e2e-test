---
id: TC-AUTH-MFA-E2E-026-fail-open-geo-ip
title: "Fail-Open Geo-IP"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-45
  - TC-AUTH-MFA-46
  - TC-AUTH-MFA-209
coverage:
  web: automated
---

# Fail-Open Geo-IP

## Prerequisites

- Mode: FE+BE.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah geo-IP service (dimatikan dan dipulihkan) dan IP uji (lokasi koneksi login); hook `after` memulihkan geo-IP service ke kondisi aktif dan IP uji ke IP default lingkungan uji.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga user berpassword `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Kondisi yang di-seed BE untuk semua user: Activated, Active ON, sudah pernah login sukses di web, logout web terakhir kurang dari 30 hari, Authenticator sudah terdaftar, persetujuan Privacy Policy versi terbaru sudah tersimpan:
  - TC-AUTH-MFA-45: `Cahyo Widodo` (`cahyowidodo+{runId}-026@qwertysystem.net`), profil FAR (Tabel Data Uji Pre-setup #7): ID device browser uji A trusted; login terakhir dari IP uji Jakarta (ID).
  - TC-AUTH-MFA-46: `Ayu Ningsih` (`ayuningsih+{runId}-026@qwertysystem.net`), profil NEWDEVE (Tabel Data Uji Pre-setup #5): ID device browser uji B tidak ada di daftar trusted device.
  - TC-AUTH-MFA-209: `Rangga Putra` (`ranggaputra+{runId}-026@qwertysystem.net`), profil XC2 (Tabel Data Uji Pre-setup #27): ID device browser uji A trusted; login terakhir dari IP uji Batam (ID); pasangan negara ID-SG tersimpan dengan hitungan tepat 2 dalam window 90 hari (belum trusted); secret Authenticator yang terdaftar diketahui aplikasi authenticator uji.
- Hook `after` (tetap jalan walau spec gagal di tengah): pulihkan geo-IP service ke kondisi aktif, pulihkan IP uji ke IP default lingkungan uji, lalu hapus ketiga user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah yang pertama dimulai di jendela baru browser uji tanpa sesi login; TC pertama berjalan di browser awal.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Seeding state BE per user: trusted device ber-ID device browser uji A (Cahyo Widodo, Rangga Putra), lokasi dan waktu login terakhir (Jakarta untuk Cahyo Widodo, Batam untuk Rangga Putra), Authenticator terdaftar dengan secret yang dikenal aplikasi authenticator uji (Rangga Putra), persetujuan Privacy Policy versi terbaru, dan hitungan pasangan negara ID-SG tepat 2 (Rangga Putra); mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - Failure injection: geo-IP service di lingkungan uji dapat dimatikan dan dipulihkan sesuai langkah (Tabel Data Uji Pre-setup #21).
  - Browser uji A (ID device trusted untuk user TC itu) dan browser uji B (ID device belum dikenali): konteks browser dengan cookie ID device persisten; setiap TC memakai konteks baru.
  - IP uji: IP sumber permintaan login dapat ditetapkan ke IP uji geo-IP Surabaya (ID), Singapura (SG), dan Batam (ID) (Tabel Data Uji Pre-setup #19).
  - Mail-catcher lingkungan uji untuk membaca jumlah email dan email alert "New sign-in to your TAG Samurai account" per alamat tujuan beserta baris Location di isinya. Asersi "ada" atau "tidak ada" email alert memakai baseline jumlah email sebelum aksi.
  - Aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) untuk `Rangga Putra`; jam aplikasi sama dengan jam server uji.
  - reCAPTCHA mode uji di environment.

## Test Steps

### TC-AUTH-MFA-45: Geo-IP service tidak tersedia: deteksi lokasi dan negara dilewati dan login dengan device dikenali tetap single-step

1. Matikan geo-IP service di lingkungan uji (failure injection)
2. Atur IP uji ke Surabaya (ID); login terakhir `Cahyo Widodo` dari Jakarta (ID)
3. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
4. Ketik `cahyowidodo+{runId}-026@qwertysystem.net` pada field Email
5. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
6. Centang widget reCAPTCHA "I'm not a robot"
7. Catat jumlah email di mail-catcher untuk `cahyowidodo+{runId}-026@qwertysystem.net` (baseline sebelum login pertama)
8. Klik button [Log in]
9. Amati halaman setelah klik [Log in]
10. Verifikasi Halaman MFA tidak tampil (kriteria lokasi lebih dari 100 km dilewati)
11. Verifikasi Browser dialihkan ke Portal — Product Hub
12. Periksa mail-catcher lingkungan uji untuk `cahyowidodo+{runId}-026@qwertysystem.net`
13. Verifikasi Tidak ada email alert "New sign-in to your TAG Samurai account" baru di mail-catcher untuk `cahyowidodo+{runId}-026@qwertysystem.net` dibanding baseline langkah 7
14. Pulihkan geo-IP service
15. Logout dari akun `Cahyo Widodo`
16. Atur IP uji ke Surabaya (ID)
17. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
18. Ketik `cahyowidodo+{runId}-026@qwertysystem.net` pada field Email
19. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
20. Centang widget reCAPTCHA "I'm not a robot"
21. Klik button [Log in]
22. Amati halaman setelah klik [Log in]
23. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil karena jarak dihitung terhadap lokasi login terakhir yang dipertahankan (Jakarta), bukan terhadap nilai kosong

### TC-AUTH-MFA-46: Geo-IP service tidak tersedia: device baru tetap memicu MFA dan email alert

24. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji B (konteks bersih tanpa sesi login; ID device belum dikenali)
25. Matikan geo-IP service di lingkungan uji (failure injection)
26. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
27. Ketik `ayuningsih+{runId}-026@qwertysystem.net` pada field Email
28. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
29. Centang widget reCAPTCHA "I'm not a robot"
30. Catat jumlah email di mail-catcher untuk `ayuningsih+{runId}-026@qwertysystem.net` (baseline sebelum login)
31. Klik button [Log in]
32. Amati halaman setelah klik [Log in]
33. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (MFA wajib karena device baru; deteksi device bukan panggilan service eksternal)
34. Periksa mail-catcher lingkungan uji untuk `ayuningsih+{runId}-026@qwertysystem.net`
35. Verifikasi Email alert dengan subject "New sign-in to your TAG Samurai account" baru diterima di mail-catcher untuk `ayuningsih+{runId}-026@qwertysystem.net` dibanding baseline langkah 30
36. Verifikasi Baris Location pada email alert berisi "Unknown location"

### TC-AUTH-MFA-209: Geo-IP service tidak tersedia tidak menambah hitungan pasangan negara

37. Pulihkan geo-IP service
38. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
39. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
40. Ketik `ranggaputra+{runId}-026@qwertysystem.net` pada field Email
41. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
42. Centang widget reCAPTCHA "I'm not a robot"
43. Matikan geo-IP service di lingkungan uji (failure injection)
44. Atur IP uji ke Singapura (SG); login terakhir `Rangga Putra` dari Batam (ID); hitungan pasangan ID-SG awal 2 (belum trusted)
45. Klik button [Log in]
46. Amati halaman setelah klik [Log in]
47. Verifikasi Halaman MFA tidak tampil (kriteria negara dilewati saat geo-IP down)
48. Verifikasi Portal — Product Hub tampil
49. Pulihkan geo-IP service
50. Logout dari Portal — Product Hub
51. Buka halaman `Auth > Login with Password` di browser uji A (IP uji tetap Singapura (SG)) → halaman Login with Password tampil
52. Ketik `ranggaputra+{runId}-026@qwertysystem.net` pada field Email
53. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
54. Centang widget reCAPTCHA "I'm not a robot"
55. Catat jumlah email di mail-catcher untuk `ranggaputra+{runId}-026@qwertysystem.net` (baseline sebelum login kedua)
56. Klik button [Log in]
57. Amati halaman setelah klik [Log in]
58. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (hitungan pasangan masih 2 sehingga pasangan belum trusted; login saat geo-IP down tidak menambah hitungan)
59. Periksa mail-catcher lingkungan uji untuk `ranggaputra+{runId}-026@qwertysystem.net`
60. Verifikasi Email alert dengan subject "New sign-in to your TAG Samurai account" baru diterima di mail-catcher untuk `ranggaputra+{runId}-026@qwertysystem.net` dibanding baseline langkah 55
61. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
62. Klik button [Login] → halaman Authenticator Verification tampil
63. Ketik kode TOTP valid dari aplikasi authenticator uji pada kotak digit
64. Klik button [Login] → Portal — Product Hub tampil
65. Logout dari akun `Rangga Putra`
66. Atur IP uji ke Batam (ID)
67. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
68. Ketik `ranggaputra+{runId}-026@qwertysystem.net` pada field Email
69. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
70. Centang widget reCAPTCHA "I'm not a robot"
71. Klik button [Log in]
72. Amati halaman setelah klik [Log in]
73. Verifikasi Halaman MFA tidak tampil (hitungan menjadi 3 setelah MFA sukses pada langkah 64 sehingga pasangan ID-SG trusted)
74. Verifikasi Portal — Product Hub tampil

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Kelas harness b (fault injection / resilience: geo-IP service mati). Pemulihan geo-IP service dan IP uji dilakukan di hook `after` sebagai cadangan.
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela baru browser uji, atur IP uji, pulihkan geo-IP service sebelum TC-AUTH-MFA-209 karena TC-AUTH-MFA-46 membiarkan geo-IP mati, logout, periksa mail-catcher) bukan asersi tambahan (S-03).
- Baseline email (S-12): langkah 7, 30, dan 55 mencatat jumlah email di mail-catcher sebelum login; asersi email alert ada atau tidak ada (langkah 13, 35, 60) hanya menghitung email sesudah baseline itu.
- Penyimpangan urutan (S-05): pada TC-AUTH-MFA-45, pemeriksaan mail-catcher (Langkah Uji 10) dipindahkan ke tepat setelah login pertama (langkah 12 dan 13 spec) sebelum geo-IP dipulihkan dan login kedua, agar Expected butir b (tidak ada email alert) tidak tercampur dengan email alert dari login kedua.
- Post Condition TC-AUTH-MFA-45 ("Satu sesi web aktif") dan TC-AUTH-MFA-46 ("Sesi pre-auth MFA aktif") tidak diasersi terpisah: sesi web teramati sebagai Portal — Product Hub tampil (langkah 11) dan sesi pre-auth sebagai halaman Choose Verification Method tampil (langkah 33), yang sudah menjadi Expected.
- Post Condition TC-AUTH-MFA-209 (pasangan ID-SG `Rangga Putra` trusted dengan hitungan 3) dibuktikan lewat Verifikasi langkah 73 dan 74; nilai hitungan tidak diasersi langsung.
- Batas ukuran: jumlah langkah melewati ±35 karena tiga TC independen dengan prefix login faktor-1 yang identik (tidak dihitung ke ±35) dan login berulang pada TC-AUTH-MFA-45 dan TC-AUTH-MFA-209. Tiap TC memakai user dan jendela sendiri, sehingga tidak ada data yang dipakai bersama; bagian sesudah tetap bermakna bila bagian sebelumnya gagal, jadi spec tidak dipecah.
- Temuan untuk QA: (1) TC-AUTH-MFA-45 Expected butir b dan Langkah Uji 10 (periksa mail-catcher) berbenturan secara urutan: Langkah Uji 10 berada setelah login kedua yang memicu MFA dan email alert, sedangkan butir b mengacu pada login pertama. (2) TC-AUTH-MFA-209 Expected butir b (email alert diterima) tidak punya langkah periksa mail-catcher di Langkah Uji; spec menambahkan langkah 59. (3) TC-AUTH-MFA-209 Langkah Uji 5 menggabungkan mematikan geo-IP, penentuan browser dan IP uji, serta klik [Log in] dalam satu langkah, dan Langkah Uji 7 dan 9 memakai "ulangi langkah 1 sampai 4"; spec memisahkannya menjadi langkah per aksi. (4) TC-AUTH-MFA-46 tidak menyebut IP uji; geo-IP mati sehingga IP uji tidak relevan dan tidak ditetapkan. (5) Mekanisme seeding state BE (trusted device ber-ID device, lokasi dan waktu login terakhir, secret Authenticator yang dikenal authenticator uji, hitungan pasangan negara) belum ada di Pre-setup TC (#20/#21 hanya memuat sebagian) dan tidak didefinisikan di PRD atau LLD; spec tidak menyebut endpoint seeding.
