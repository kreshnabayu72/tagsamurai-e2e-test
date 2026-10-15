---
id: TC-AUTH-MFA-E2E-008-kedaluwarsa-kode-otp-5-menit
title: "Kedaluwarsa Kode OTP Faktor Kedua 5 Menit"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-73
  - TC-AUTH-MFA-74
  - TC-AUTH-MFA-211
  - TC-AUTH-MFA-160
coverage:
  web: automated
---

# Kedaluwarsa Kode OTP Faktor Kedua 5 Menit

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): empat user profil NEWDEV (Tabel Data Uji Pre-setup #4: Activated, Active ON, sudah pernah login sukses di web, Authenticator belum terdaftar; login dari jendela privat memicu MFA karena ID device belum dikenali (tiap jendela privat tanpa ID device tersimpan, dikenali sebagai browser uji B; TC pertama pun berjalan di jendela privat karena jendela utama memegang sesi aktor); tanpa layar Confirm to Continue), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-73: `Bella Kartika` (`bellakartika+{runId}-008@qwertysystem.net`)
  - TC-AUTH-MFA-160: `Rafli Pranata` (`raflipranata+{runId}-008@qwertysystem.net`)
  - TC-AUTH-MFA-74: `Cakra Wibisana` (`cakrawibisana+{runId}-008@qwertysystem.net`)
  - TC-AUTH-MFA-211: `Hendri Maulana` (`hendrimaulana+{runId}-008@qwertysystem.net`)
- Sesi aktor: hook `before` membuka sesi browser utama akun aktor Total Control (Global Settings) lewat `seedSession` (tanpa melewati MFA). Sesi ini dipakai TC-AUTH-MFA-160 untuk membaca `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`, dan tetap valid karena jam server uji sudah dipulihkan ke waktu nyata sebelum akun aktor membuka log pada TC-AUTH-MFA-160 (sesi aktor tidak menjalani pergeseran jam). Semua langkah login user uji dilakukan di jendela privat baru.
- Hook `after`: pulihkan jam server uji ke waktu nyata (termasuk melepas pembekuan jam), hapus keempat user (beserta sesi web yang terbentuk dari TC-AUTH-MFA-74 dan 211). Hook ini tetap jalan walau spec gagal di tengah, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di jendela privat) untuk login user uji; akun Total Control (Global Settings) hanya di jendela utama untuk TC-AUTH-MFA-160.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: pengaturan jam server uji (dimajukan relatif, diset absolut, dan dibekukan, lalu dipulihkan ke waktu nyata); jendela privat; reCAPTCHA mode uji di environment; mail-catcher lingkungan uji untuk membaca kode OTP faktor-2 dan penanda waktu penerbitan email OTP (dasar waktu terbit kode pada TC-AUTH-MFA-211); IP uji sebagai IP Address yang tercatat di log (TC-AUTH-MFA-160).
- Kemampuan teknis, seeding state BE per user: status Activated dan Active ON, sudah pernah login sukses di web (lokasi dan waktu login terakhir, logout web terakhir kurang dari 30 hari), consent sudah disetujui sehingga tanpa layar Confirm to Continue, dan Authenticator belum terdaftar. Mekanisme seeding (endpoint atau skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
- Jam: umur kode OTP 5 menit dihitung murni di server dan tidak diamati lewat hitung mundur UI pada asersi spec ini, sehingga hanya jam server uji yang diubah dan jam browser uji tidak diubah. Pergeseran dilakukan relatif terhadap saat kode diterbitkan pada tiap TC yang bukan batas eksak: 5 menit 30 detik (TC-AUTH-MFA-73), 5 menit 30 detik (TC-AUTH-MFA-160), dan 4 menit (TC-AUTH-MFA-74). TC-AUTH-MFA-211 adalah batas eksak (4 menit 59 detik): jam server diset absolut ke waktu terbit kode ditambah 4 menit 59 detik lalu dibekukan, supaya detik nyata sejak penerbitan tidak ikut terhitung. Sesi pre-auth berlaku 10 menit sehingga masih aktif pada tiap pergeseran. Jam server dipulihkan ke waktu nyata dengan langkah eksplisit: pada TC-AUTH-MFA-160 sesudah kode diketik dan sebelum pindah ke jendela akun aktor yang membuka log, pada TC lain di akhir TC; hook `after` sebagai cadangan.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah jam server uji; hook `after` memulihkan jam server uji.

## Test Steps

### TC-AUTH-MFA-73: Verifikasi OTP faktor-2 dengan kode yang sudah lebih dari 5 menit

1. Buka jendela privat baru (tanpa sesi login)
2. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
3. Ketik `bellakartika+{runId}-008@qwertysystem.net` pada field Email
4. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
5. Centang widget reCAPTCHA "I'm not a robot"
6. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
7. Pilih opsi "OTP via email" pada halaman Choose Verification Method
8. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `bellakartika+{runId}-008@qwertysystem.net`
9. Majukan jam server uji 5 menit 30 detik (kode berusia 5 menit 30 detik; sesi pre-auth masih berlaku)
10. Ketik 6 digit kode OTP faktor-2 dari email `bellakartika+{runId}-008@qwertysystem.net` pada kotak digit
11. Verifikasi Caption error di bawah kotak digit: "OTP expired"
12. Verifikasi Tidak ada sesi yang dibuat
13. Verifikasi Halaman tetap `Auth > MFA > OTP Verification`
14. Verifikasi Kotak digit dikosongkan
15. Verifikasi Fokus kembali ke kotak 1
16. Ketik ulang satu digit pada kotak 1 (digit `1`)
17. Verifikasi Caption error hilang
18. Verifikasi Border error hilang
19. Pulihkan jam server uji ke waktu nyata

### TC-AUTH-MFA-160: Pencatatan OTP faktor-2 expired dicatat Failed OTP expired

20. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
21. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
22. Ketik `raflipranata+{runId}-008@qwertysystem.net` pada field Email
23. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
24. Centang widget reCAPTCHA "I'm not a robot"
25. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
26. Pilih opsi "OTP via email" pada halaman Choose Verification Method
27. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `raflipranata+{runId}-008@qwertysystem.net`
28. Majukan jam server uji 5 menit 30 detik (kode berusia 5 menit 30 detik; sesi pre-auth masih berlaku)
29. Catat penanda waktu P1 sebagai waktu jam server uji saat ini (setelah jam dimajukan, sebelum kode diketik)
30. Ketik 6 digit kode OTP faktor-2 dari email `raflipranata+{runId}-008@qwertysystem.net` pada kotak digit
31. Pulihkan jam server uji ke waktu nyata (sebelum akun aktor membuka log)
32. Pindah ke jendela utama (sesi akun aktor Total Control (Global Settings) dari hook `before`)
33. Buka `Global Settings > Activity Log > Session` dan cari entri untuk `raflipranata+{runId}-008@qwertysystem.net` (`Rafli Pranata`) dengan waktu sesudah penanda P1
34. Verifikasi Tampil satu entri baru untuk `Rafli Pranata` pada Activity Log Session dengan Activity `Login`, Status `Failed`, dan Note `OTP expired`
35. Verifikasi IP Address pada entri Activity Log Session berisi IP uji
36. Verifikasi Entri Activity Log Session memuat tanggal dan waktu percobaan
37. Buka `Global Settings > User > Detail > User Log` untuk `Rafli Pranata` (user dicari lewat email bersuffix `raflipranata+{runId}-008@qwertysystem.net` pada daftar User) dan cari entri dengan waktu sesudah penanda P1
38. Verifikasi Tampil satu entri baru pada User Log dengan Activity `Login`, Status `Failed`, dan Note `OTP expired`
39. Verifikasi IP Address pada entri User Log sama dengan IP Address pada entri Activity Log Session
40. Verifikasi Tidak ada entri log tambahan untuk percobaan ini: tepat satu entri sesudah penanda P1 pada tiap surface (Activity Log Session dan User Log)

### TC-AUTH-MFA-74: Verifikasi OTP faktor-2 dengan kode berumur 4 menit diterima

41. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
42. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
43. Ketik `cakrawibisana+{runId}-008@qwertysystem.net` pada field Email
44. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
45. Centang widget reCAPTCHA "I'm not a robot"
46. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
47. Pilih opsi "OTP via email" pada halaman Choose Verification Method
48. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `cakrawibisana+{runId}-008@qwertysystem.net`
49. Majukan jam server uji 4 menit (kode berusia 4 menit)
50. Ketik 6 digit kode OTP faktor-2 dari email `cakrawibisana+{runId}-008@qwertysystem.net` pada kotak digit
51. Verifikasi Verifikasi berhasil
52. Verifikasi Browser dialihkan ke Portal — Product Hub
53. Verifikasi Sesi web aktif untuk `Cakra Wibisana` (teramati dari Portal — Product Hub yang tampil)
54. Pulihkan jam server uji ke waktu nyata

### TC-AUTH-MFA-211: Verifikasi OTP faktor-2 dengan kode berumur 4 menit 59 detik diterima (satu detik sebelum batas)

55. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
56. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
57. Ketik `hendrimaulana+{runId}-008@qwertysystem.net` pada field Email
58. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
59. Centang widget reCAPTCHA "I'm not a robot"
60. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
61. Pilih opsi "OTP via email" pada halaman Choose Verification Method
62. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `hendrimaulana+{runId}-008@qwertysystem.net`
63. Catat waktu terbit kode (T0) dari penanda waktu pengiriman email OTP di mail-catcher
64. Set jam server uji secara absolut ke T0 ditambah 4 menit 59 detik lalu bekukan jam tersebut (kode berusia 4 menit 59 detik)
65. Ketik 6 digit kode OTP faktor-2 dari email `hendrimaulana+{runId}-008@qwertysystem.net` pada kotak digit
66. Verifikasi Verifikasi berhasil (kode valid selama kurang dari 5 menit)
67. Verifikasi Browser dialihkan ke Portal — Product Hub
68. Verifikasi Sesi web aktif untuk `Hendri Maulana` (teramati dari Portal — Product Hub yang tampil)
69. Lepas pembekuan jam server uji dan pulihkan ke waktu nyata

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Kelas harness d (time-travel). Jam server digeser relatif terhadap penerbitan kode pada TC-AUTH-MFA-73, 160, dan 74 (bukan batas eksak) dan diset absolut lalu dibekukan pada TC-AUTH-MFA-211 (batas eksak 4 menit 59 detik). Tiap TC menerbitkan kodenya sendiri dan memulihkan jam dengan langkah eksplisit (langkah 19, 31, 54, 69; pada TC-AUTH-MFA-160 pemulihan di langkah 31 mendahului akun aktor membuka Activity Log Session dan User Log), sehingga tidak ada ketergantungan antar-TC; hook `after` sebagai cadangan. Jam browser tidak diubah karena umur kode dihitung murni di server dan tidak diamati lewat hitung mundur UI.
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal tiap TC karena jendela utama memegang sesi aktor; pindah ke jendela utama pada TC-AUTH-MFA-160; mengatur dan memulihkan jam; mencatat penanda waktu P1 dan T0) bukan asersi tambahan (S-03, S-09, S-12).
- Penyimpangan urutan (S-05, S-10): TC sumber memuat 73, 74, 211, 160; spec memakai 73 dan 160 (kode expired, ditolak) lebih dulu, lalu 74 dan 211 (kode diterima, berujung login sukses) di akhir.
- Pembagian TC lintas spec: asersi pencatatan Failed `OTP expired` (Activity Log Session dan User Log) ada di spec ini pada TC-AUTH-MFA-160 karena kondisinya sama dengan TC-AUTH-MFA-73 (kode berusia 5 menit 30 detik pada jam server yang sama). Post Condition TC-AUTH-MFA-73 "Percobaan dicatat Failed `OTP expired` (detail pada TC Logging)" merujuk ke TC-AUTH-MFA-160 dan tidak diasersi dua kali.
- Baseline log TC-AUTH-MFA-160 (S-12): asersi entri baru memakai penanda waktu P1 (langkah 29, diambil setelah jam server dimajukan; percobaan dicatat pada jam yang sama sehingga penanda tetap valid walau jam dipulihkan di langkah 31 sebelum log dibuka) dan pencarian lewat email bersuffix, bukan nama literal. Asersi "tepat satu entri" berarti tepat satu entri dengan waktu sesudah P1 pada tiap surface.
- Ukuran spec (smell sekitar 35 langkah): spec ini sekitar 49 langkah setelah langkah prefix login faktor-1 yang identik (buka Login with Password sampai klik [Log in]) tidak dihitung. Tidak dipecah karena keempat TC independen: tiap TC memakai user dan jendela privat sendiri serta memulihkan jamnya sendiri, sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA: (1) TC-AUTH-MFA-73 dan TC-AUTH-MFA-160 Langkah Uji "Tunggu 5 menit 30 detik" ditandai Automation berbeda (Manual Only dan Automatable) padahal kondisinya sama; spec memakai pergeseran jam server untuk keduanya. (2) TC-AUTH-MFA-74 Langkah Uji "Tunggu 4 menit" diwujudkan sebagai pergeseran jam server (TC bertanda Manual Only). (3) TC-AUTH-MFA-160 tidak menyebut cara akun Total Control (Global Settings) membuka sesi; spec memakai sesi aktor dari hook. (4) TC-AUTH-MFA-160 Expected a tidak menyebut format IP Address selain "berisi IP uji"; diikuti apa adanya. (5) TC-AUTH-MFA-211 Langkah Uji 8 tidak menyebut cara menentukan waktu terbit kode (T0); spec membacanya dari penanda waktu email OTP di mail-catcher dan mekanisme pengaturan jam absolut disediakan tim FE/BE. (6) Pre-setup TC (#20/#21) belum memuat mekanisme seeding state BE per user (login terakhir, consent, logout web terakhir); mekanisme seed disediakan tim FE/BE. (7) TC-AUTH-MFA-73 Langkah Uji 10 "Ketik ulang satu digit pada kotak 1" tidak menyebut digitnya; spec memakai `1` (S-15).
