---
id: TC-AUTH-MFA-E2E-023-deteksi-lokasi-lebih-100-km
title: "Deteksi Lokasi Lebih dari 100 km"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-33
  - TC-AUTH-MFA-38
  - TC-AUTH-MFA-51
  - TC-AUTH-MFA-208
coverage:
  web: automated
---

# Deteksi Lokasi Lebih dari 100 km

## Prerequisites

- Mode: FE+BE.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah IP uji (lokasi koneksi login ditetapkan ke Surabaya (ID) dan Singapura (SG)); hook `after` memulihkan IP uji ke IP default lingkungan uji.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): empat user berpassword `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Kondisi yang di-seed BE untuk semua user: Activated, Active ON, logout web terakhir kurang dari 30 hari, Authenticator sudah terdaftar, persetujuan Privacy Policy versi terbaru sudah tersimpan:
  - TC-AUTH-MFA-33: `Bagas Firmansyah` (`bagasfirmansyah+{runId}-023@qwertysystem.net`), profil FAR (Tabel Data Uji Pre-setup #7): ID device browser uji A trusted; login terakhir dari IP uji Jakarta (ID).
  - TC-AUTH-MFA-38: `Mega Safitri` (`megasafitri+{runId}-023@qwertysystem.net`), profil XCTF (Tabel Data Uji Pre-setup #13): ID device browser uji A trusted; login terakhir dari IP uji Jakarta (ID); pasangan negara ID-SG trusted (hitungan 3 dalam window 90 hari, terakhir terlihat kurang dari 180 hari).
  - TC-AUTH-MFA-51: `Dewi Wijaya` (`dewiwijaya+{runId}-023@qwertysystem.net`), profil TWODEV (Tabel Data Uji Pre-setup #14): dua trusted device web, yaitu ID device browser uji A (login terakhir user, 1 hari lalu dari Jakarta (ID)) dan ID device browser uji B (login terakhir pada device itu 20 hari lalu dari Surabaya (ID)).
  - TC-AUTH-MFA-208: `Maria Ulfa` (`mariaulfa+{runId}-023@qwertysystem.net`), profil NOLOC (Tabel Data Uji Pre-setup #26): ID device browser uji A trusted; tidak ada catatan lokasi login terakhir untuk platform web.
- Hook `after`: kembalikan IP uji ke IP default lingkungan uji, lalu hapus keempat user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah yang pertama dimulai di jendela baru browser uji tanpa sesi login; TC pertama berjalan di browser awal.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Seeding state BE per user: trusted device (ID device browser uji A trusted untuk TC-AUTH-MFA-33, 38, 208; ID device browser uji A dan B trusted untuk TC-AUTH-MFA-51), lokasi dan waktu login terakhir per user dan per device (Jakarta (ID); untuk `Dewi Wijaya` device A 1 hari lalu Jakarta (ID) dan device B 20 hari lalu Surabaya (ID); untuk `Maria Ulfa` tidak ada catatan), hitungan pasangan negara ID-SG (`Mega Safitri`), `last_logout_at` kurang dari 30 hari, Authenticator terdaftar, dan persetujuan Privacy Policy; mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - Browser uji A (ID device trusted untuk user TC itu), browser uji B (ID device trusted hanya untuk `Dewi Wijaya`), dan browser uji C (ID device belum dikenali; TC-AUTH-MFA-208): konteks browser dengan cookie ID device persisten; setiap TC memakai konteks baru.
  - IP uji: IP sumber permintaan login dapat ditetapkan ke IP uji geo-IP Surabaya (ID) dan Singapura (SG) (Tabel Data Uji Pre-setup #19); geo-IP service aktif.
  - Mail-catcher lingkungan uji untuk membaca email alert "New sign-in to your TAG Samurai account", termasuk waktu terima tiap email. Asersi email memakai baseline jumlah email alert untuk alamat user yang dicatat sebelum login.
  - reCAPTCHA mode uji di environment.

## Test Steps

### TC-AUTH-MFA-33: Login dari lokasi lebih dari 100 km dari login terakhir memicu MFA dan email alert

1. Atur IP uji ke Surabaya (ID); login terakhir `Bagas Firmansyah` dari Jakarta (ID), jarak lebih dari 100 km
2. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `bagasfirmansyah+{runId}-023@qwertysystem.net` sebagai baseline
3. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
4. Ketik `bagasfirmansyah+{runId}-023@qwertysystem.net` pada field Email
5. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
6. Centang widget reCAPTCHA "I'm not a robot"
7. Klik button [Log in]
8. Amati halaman setelah klik [Log in]
9. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (MFA wajib karena lokasi lebih dari 100 km, negara sama)
10. Periksa mail-catcher lingkungan uji untuk `bagasfirmansyah+{runId}-023@qwertysystem.net`
11. Verifikasi Email alert dengan subject "New sign-in to your TAG Samurai account" diterima di mail-catcher untuk `bagasfirmansyah+{runId}-023@qwertysystem.net` (jumlah bertambah dibanding baseline langkah 2)
12. Verifikasi Jarak dihitung terhadap catatan login terakhir user di platform web (Jakarta), bukan terhadap catatan per device

### TC-AUTH-MFA-38: Pasangan negara trusted tidak membebaskan lokasi lebih dari 100 km dari MFA dan email alert

13. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
14. Atur IP uji ke Singapura (SG); login terakhir `Mega Safitri` dari Jakarta (ID), jarak lebih dari 100 km
15. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `megasafitri+{runId}-023@qwertysystem.net` sebagai baseline
16. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
17. Ketik `megasafitri+{runId}-023@qwertysystem.net` pada field Email
18. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
19. Centang widget reCAPTCHA "I'm not a robot"
20. Klik button [Log in]
21. Amati halaman setelah klik [Log in]
22. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (MFA wajib karena jarak lebih dari 100 km walau pasangan negara trusted)
23. Periksa mail-catcher lingkungan uji untuk `megasafitri+{runId}-023@qwertysystem.net`
24. Verifikasi Email alert dengan subject "New sign-in to your TAG Samurai account" diterima di mail-catcher untuk `megasafitri+{runId}-023@qwertysystem.net` (jumlah bertambah dibanding baseline langkah 15)

### TC-AUTH-MFA-51: Baseline lokasi adalah login terakhir user di platform, bukan login terakhir device yang dipakai

25. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji B (konteks bersih tanpa sesi login; ID device trusted)
26. Atur IP uji ke Surabaya (ID); login terakhir user `Dewi Wijaya` dari Jakarta (ID) 1 hari lalu
27. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `dewiwijaya+{runId}-023@qwertysystem.net` sebagai baseline
28. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
29. Ketik `dewiwijaya+{runId}-023@qwertysystem.net` pada field Email
30. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
31. Centang widget reCAPTCHA "I'm not a robot"
32. Klik button [Log in]
33. Amati halaman setelah klik [Log in]
34. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (MFA wajib karena jarak lebih dari 100 km dari login terakhir user di Jakarta, walau login terakhir device ini juga dari Surabaya)
35. Periksa mail-catcher lingkungan uji untuk `dewiwijaya+{runId}-023@qwertysystem.net`
36. Verifikasi Email alert dengan subject "New sign-in to your TAG Samurai account" diterima di mail-catcher untuk `dewiwijaya+{runId}-023@qwertysystem.net` (jumlah bertambah dibanding baseline langkah 27)

### TC-AUTH-MFA-208: Tanpa catatan lokasi login terakhir kriteria lebih dari 100 km dilewati sedangkan device baru tetap memicu MFA

37. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login; ID device dikenali)
38. Atur IP uji ke Surabaya (ID); catatan lokasi login terakhir `Maria Ulfa` tidak ada
39. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `mariaulfa+{runId}-023@qwertysystem.net` sebagai baseline
40. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
41. Ketik `mariaulfa+{runId}-023@qwertysystem.net` pada field Email
42. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
43. Centang widget reCAPTCHA "I'm not a robot"
44. Klik button [Log in]
45. Amati halaman setelah klik [Log in]
46. Verifikasi Halaman MFA tidak tampil
47. Verifikasi Browser dialihkan ke Portal — Product Hub (kriteria lokasi lebih dari 100 km dilewati karena catatan lokasi login terakhir tidak ada)
48. Logout dari Portal — Product Hub
49. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji C (konteks bersih tanpa sesi login; ID device belum dikenali)
50. Atur IP uji ke Surabaya (ID)
51. Buka halaman `Auth > Login with Password` di browser uji C → halaman Login with Password tampil
52. Ketik `mariaulfa+{runId}-023@qwertysystem.net` pada field Email
53. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
54. Centang widget reCAPTCHA "I'm not a robot"
55. Klik button [Log in]
56. Amati halaman setelah klik [Log in]
57. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (MFA wajib karena device baru; kriteria device baru tetap dievaluasi)
58. Buka mail-catcher lingkungan uji untuk `mariaulfa+{runId}-023@qwertysystem.net`
59. Verifikasi Email alert dengan subject "New sign-in to your TAG Samurai account" diterima untuk `mariaulfa+{runId}-023@qwertysystem.net` pada login browser uji C (langkah 55): jumlah bertambah satu dibanding baseline langkah 39
60. Verifikasi Waktu terima email alert baru itu sesudah klik [Log in] langkah 55
61. Verifikasi Tidak ada email alert untuk `mariaulfa+{runId}-023@qwertysystem.net` dari login browser uji A (langkah 44): tidak ada email alert baru dengan waktu terima sebelum klik [Log in] langkah 55

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela baru browser uji, atur IP uji, catat baseline email, logout pada TC-AUTH-MFA-208) bukan asersi tambahan (S-03). Langkah 2, 15, 27, dan 39 mencatat baseline jumlah email alert (S-12) supaya "email alert diterima" diasersi sebagai bertambah; Expected c TC-AUTH-MFA-208 ("pada langkah 7 saja") dipecah menjadi langkah 59 dan 60 (alert dari login browser uji C: jumlah bertambah satu, lalu waktu terima sesudah klik [Log in]) dan langkah 61 (tidak ada alert dari login browser uji A) dengan penanda waktu terima.
- Urutan TC mengikuti TC sumber; TC-AUTH-MFA-208 ditaruh terakhir karena berpindah browser uji (A lalu C). Perpindahan itu berurutan dan hanya membentuk identitas device (login pertama dari device dikenali, lalu dari device baru) tanpa asersi lintas keduanya, jadi bukan konteks kedua (kelas c) dan tidak memakai pengecualian P-2.
- Sesi teramati lewat halaman yang tampil: sesi pre-auth MFA = halaman Choose Verification Method tampil; sesi web aktif = Portal — Product Hub tampil. Post Condition sesi tidak diasersi terpisah.
- Jumlah langkah melewati ±35 karena empat TC independen dengan prefix login faktor-1 yang identik (tidak dihitung) dan TC-AUTH-MFA-208 yang berisi dua login berurutan; spec tidak dipecah.
- Temuan untuk QA:
  1. TC-AUTH-MFA-33 Expected butir c (jarak dihitung terhadap catatan login terakhir user, bukan per device) tidak dapat dibedakan dari butir a pada TC ini; pembuktian ada di TC-AUTH-MFA-51.
  2. TC-AUTH-MFA-208 Langkah Uji 5 dan 7 menggabung penentuan browser, IP uji, dan klik [Log in] dalam satu langkah, dan Expected butir c menyebut "langkah 7" untuk email alert; spec memisahkannya menjadi langkah per aksi.
  3. TC-AUTH-MFA-208 profil NOLOC tidak menyatakan apakah login pertama di browser uji A memicu layar Confirm to Continue; spec mengikuti Expected (langsung ke Portal).
  4. Post Condition berupa state BE tidak diasersi (S-01, S-15): TC-AUTH-MFA-33, 38, 51 "Sesi pre-auth MFA aktif untuk <user>" (teramati lewat halaman Choose Verification Method tampil pada Expected) dan TC-AUTH-MFA-208 "Lokasi login terakhir `Maria Ulfa` tercatat Surabaya (ID) sejak langkah 5" (tanpa cara pengecekan lewat UI). QA menambah Expected atau langkah observasi di TC bila ada yang harus diuji lebih jauh.
  5. Mekanisme seeding state BE (trusted device per ID device browser A/B, lokasi dan waktu login terakhir per user dan per device, hitungan pasangan negara, tanpa catatan lokasi untuk profil NOLOC, consent) belum ada di Tabel Data Uji Pre-setup (#20 dan #21 hanya memuat manipulasi jam server, seed `last_logout_at`, pasangan negara, `first_login_at`, dan failure injection); tim FE/BE menyediakan dan QA melengkapi Pre-setup.
