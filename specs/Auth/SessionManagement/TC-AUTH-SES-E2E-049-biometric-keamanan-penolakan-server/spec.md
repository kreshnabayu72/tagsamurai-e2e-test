---
id: TC-AUTH-SES-E2E-049-biometric-keamanan-penolakan-server
title: "Re-login Biometric: Penolakan Server dan ID Device Tidak Cocok"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-170
  - TC-AUTH-SES-171
  - TC-AUTH-SES-176
  - TC-AUTH-SES-257
  - TC-AUTH-SES-258
coverage:
  web: automated
  mobile: automated
---

# Re-login Biometric: Penolakan Server dan ID Device Tidak Cocok

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) terpasang di perangkat Android uji B (Tabel Data Uji Pre-setup #10: hardware biometric, sidik jari terdaftar di OS). TC-AUTH-SES-257 dan 258 tidak memakai perangkat; keduanya hanya mengirim request langsung.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): lima user profil BIO milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #9 dan #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu; belum pernah enroll biometric), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-257: `Citra Lestari` (`citralestari+{runId}-049@qwertysystem.net`)
  - TC-AUTH-SES-258: `Yoga Pratama` (`yogapratama+{runId}-049@qwertysystem.net`)
  - TC-AUTH-SES-176: `Irfan Rahayu` (`irfanrahayu+{runId}-049@qwertysystem.net`)
  - TC-AUTH-SES-170: `Taufik Hidayat` (`taufikhidayat+{runId}-049@qwertysystem.net`)
  - TC-AUTH-SES-171: `Mega Utami` (`megautami+{runId}-049@qwertysystem.net`)
- Kondisi di-seed BE untuk TC-AUTH-SES-257 dan 258: kredensial biometric Active milik `Citra Lestari` dan `Yoga Pratama` pada ID device perangkat Android uji B, dengan `refreshToken` plaintext dari respons enroll diserahkan ke alat uji (plaintext hanya dikembalikan sekali saat enroll, sehingga alat uji tidak dapat membacanya dari perangkat). Kondisi di-seed BE untuk TC-AUTH-SES-171: akun `Mega Utami` terkunci akibat lock progression password (Locked 15 minutes).
- Untuk TC-AUTH-SES-176, TC-AUTH-SES-170, dan TC-AUTH-SES-171 kondisi awal "sudah enroll biometric di perangkat Android uji B; tidak ada sesi platform aktif" dibuat di dalam TC dengan menyalin langkah enroll TC-AUTH-SES-145 (hapus data aplikasi, login, [Enable], lulus sidik jari), lalu mengakhiri sesi platform hasil login enroll lewat Manual Logout di aplikasi (menu Profile → Log Out; logout mobile tidak menghapus token biometric lokal dan tidak mencabut kredensial di server) dan menghapus app dari recent apps sehingga pembukaan berikutnya menampilkan Screen "Sign in with biometrics" (cara menyiapkan mengikuti Tabel Data Uji Pre-setup #29), karena token biometric lokal dan status "sudah ditawari" disimpan di perangkat dan hanya dapat dibuat oleh aplikasi.
- Browser Admin: konteks browser terpisah dengan akun aktor Total Control (Global Settings) di atas, login di hook `before`, untuk mematikan Toggle Active user di `Global Settings > User` (TC-AUTH-SES-176).
- Suite berjalan serial (`parallel: false`), juga karena perangkat Android uji B dipakai bersama; state global yang diubah dan pemulihannya di hook `after`: status Active user `Irfan Rahayu` (TC-AUTH-SES-176; user dihapus); status Locked `Mega Utami` (TC-AUTH-SES-171; user dihapus).
- Hook `after`: hapus data aplikasi pada perangkat Android uji B, tutup Browser Admin, akhiri semua sesi seed, lalu hapus kelima user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile atau request langsung; akun aktor Total Control hanya di Browser Admin (TC-AUTH-SES-176).
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness a: defense-in-depth; kelas d: hardware biometrik): driver otomasi Android (aplikasi native); simulasi sensor sidik jari pada OS biometric prompt (sidik jari terdaftar lulus, sidik jari tidak terdaftar gagal); menghapus data aplikasi dan menghapus app dari recent apps lalu membukanya kembali; REST client alat uji yang dapat mengirim request langsung ke `POST /v2/iam/auth/biometric/relogin` (body `deviceId` dan `refreshToken`); pembacaan status sesi user uji dari sisi backend (langkah 3, 6, 20) dan pembacaan penyimpanan token biometric lokal (langkah 21), disediakan tim FE/BE.

## Test Steps

### TC-AUTH-SES-257: Biometric re-login dengan ID device yang tidak cocok ditolak

1. Kirim request relogin (`POST /v2/iam/auth/biometric/relogin`) dengan `refreshToken` valid milik `Citra Lestari` dan `deviceId` milik perangkat lain (bukan perangkat Android uji B)
2. Verifikasi Request ditolak (token tidak valid)
3. Verifikasi Tidak ada sesi yang dibuat untuk `Citra Lestari`

### TC-AUTH-SES-258: Biometric re-login dengan token yang tidak ditemukan di server ditolak

4. Kirim request relogin (`POST /v2/iam/auth/biometric/relogin`) dengan `refreshToken` acak yang tidak pernah diterbitkan dan `deviceId` perangkat Android uji B
5. Verifikasi Request ditolak (token tidak valid)
6. Verifikasi Tidak ada sesi yang dibuat untuk `Yoga Pratama`

### TC-AUTH-SES-176: Token biometric Active ditolak saat akun sudah dinonaktifkan atau dihapus

7. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
8. Ketik `irfanrahayu+{runId}-049@qwertysystem.net` pada field Email
9. Ketik `Spectra.env.SES_PASSWORD` pada field Password
10. Klik [Login] → Prompt Enable Biometric muncul
11. Ketuk [Enable] → OS biometric prompt muncul
12. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub
13. Buka menu Profile lalu pilih Log Out → form Login tampil (Manual Logout mengakhiri sesi platform hasil login enroll tanpa menghapus token biometric lokal dan tanpa mencabut kredensial biometric; Tabel Data Uji Pre-setup #29)
14. Hapus app dari recent apps
15. Pindah ke Browser Admin (akun aktor Total Control sudah login di hook)
16. Matikan Toggle Active `Irfan Rahayu` di `Global Settings > User`
17. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
18. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
19. Verifikasi Re-login ditolak
20. Verifikasi Tidak ada sesi yang dibuat untuk `Irfan Rahayu`
21. Verifikasi Token lokal dihapus
22. Verifikasi Halaman Login penuh tampil
23. Verifikasi Tidak ada caption yang menyebut status akun

### TC-AUTH-SES-170: Kegagalan biometric tidak menambah hitungan gagal password

24. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
25. Ketik `taufikhidayat+{runId}-049@qwertysystem.net` pada field Email
26. Ketik `Spectra.env.SES_PASSWORD` pada field Password
27. Klik [Login] → Prompt Enable Biometric muncul
28. Ketuk [Enable] → OS biometric prompt muncul
29. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub
30. Buka menu Profile lalu pilih Log Out → form Login tampil (Manual Logout mengakhiri sesi platform hasil login enroll tanpa menghapus token biometric lokal dan tanpa mencabut kredensial biometric; Tabel Data Uji Pre-setup #29)
31. Hapus app dari recent apps
32. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
33. Tempelkan sidik jari yang tidak terdaftar pada OS biometric prompt (kegagalan biometric ke-1)
34. Ketuk [Try Again]
35. Tempelkan sidik jari yang tidak terdaftar pada OS biometric prompt (kegagalan biometric ke-2)
36. Ketuk tautan "Sign in with password instead"
37. Hapus app dari recent apps
38. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
39. Tempelkan sidik jari yang tidak terdaftar pada OS biometric prompt (kegagalan biometric ke-3)
40. Ketuk [Try Again]
41. Tempelkan sidik jari yang tidak terdaftar pada OS biometric prompt (kegagalan biometric ke-4)
42. Ketuk [Try Again]
43. Tempelkan sidik jari yang tidak terdaftar pada OS biometric prompt (kegagalan biometric ke-5)
44. Ketuk tautan "Sign in with password instead" → halaman Login penuh tampil
45. Ketik `taufikhidayat+{runId}-049@qwertysystem.net` pada field Email
46. Ketik `Spectra.env.SES_PASSWORD` pada field Password
47. Klik [Login]
48. Verifikasi Login password berhasil
49. Verifikasi App masuk Portal — Product Hub
50. Verifikasi Akun `Taufik Hidayat` tidak terkunci karena kegagalan biometric

### TC-AUTH-SES-171: Lock password aktif tidak memblokir biometric re-login

51. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
52. Ketik `megautami+{runId}-049@qwertysystem.net` pada field Email
53. Ketik `Spectra.env.SES_PASSWORD` pada field Password
54. Klik [Login] → Prompt Enable Biometric muncul
55. Ketuk [Enable] → OS biometric prompt muncul
56. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub
57. Buka menu Profile lalu pilih Log Out → form Login tampil (Manual Logout mengakhiri sesi platform hasil login enroll tanpa menghapus token biometric lokal dan tanpa mencabut kredensial biometric; Tabel Data Uji Pre-setup #29)
58. Hapus app dari recent apps
59. Kunci akun `Mega Utami` akibat lock progression password sehingga berstatus Locked 15 minutes (kondisi di-seed BE)
60. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
61. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
62. Verifikasi Biometric re-login berhasil
63. Verifikasi App masuk Portal — Product Hub
64. Verifikasi Lock password tidak memblokir jalur biometric

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-257, 258, 176, 170, 171 (urutan TC sumber 170, 171, 176, 257, 258). Request langsung yang ditolak tanpa perangkat (257, 258) didahulukan, TC yang mematikan Toggle Active user (176) memakai user miliknya sendiri, dan TC dengan kondisi kunci akun di-seed BE (171) ditaruh paling akhir.
- TC-AUTH-SES-175 (IP rate limit) ada di spec `TC-AUTH-SES-E2E-074-biometric-relogin-ip-rate-limit-429`.
- Spec ini memuat dua jenis harness (request langsung dan hardware biometrik); pengecualian yang dipakai adalah `P-5` (b) untuk TC-AUTH-SES-257 dan 258 (butir di bawah).
- Dependensi (S-04): tidak ada TC dependensi di kolom Dependensi; kondisi "sudah enroll" pada TC-AUTH-SES-176, 170, 171 dibuat dengan menyalin langkah enroll TC-AUTH-SES-145 di awal tiap TC, termasuk langkah mengakhiri sesi platform hasil login enroll lewat Manual Logout di aplikasi (menu Profile → Log Out) lalu menghapus app dari recent apps (Pre-setup #29); logout mobile tidak menghapus token biometric lokal dan tidak mencabut kredensial biometric.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): "Hapus data aplikasi" di awal tiap TC yang memakai perangkat (S-09); perpindahan ke Browser Admin; langkah 37–38 pada TC-AUTH-SES-170 menghapus app lalu membuka kembali supaya Screen biometric sign-in tampil lagi untuk pengulangan kegagalan biometric.
- Pembagian TC lintas spec: asersi "tidak ada entri log" (TC-AUTH-SES-170 Expected b, TC-AUTH-SES-176 Expected b, TC-AUTH-SES-257 Expected b, TC-AUTH-SES-258 Expected b) tidak ditulis di spec ini dan berada di spec absence `TC-AUTH-SES-E2E-070-absence-biometric` (kelas g, S-05).
- Temuan untuk QA: (1) TC sumber menulis login dan enroll tanpa menyebut field dan tombol; spec menguraikannya menjadi ketik email, ketik password, klik [Login] (label tombol login mobile tidak disebut TC). (2) TC-AUTH-SES-257 dan 258 menyebut "token valid" dan "alat uji dapat mengirim request relogin langsung" tanpa menyebut dari mana alat uji memperoleh `refreshToken` plaintext yang hanya dikembalikan sekali saat enroll; spec memakai seeding BE. (3) TC-AUTH-SES-176: judul menyebut "dinonaktifkan atau dihapus" tetapi langkah hanya mematikan Toggle Active; dialog konfirmasi Deactivate tidak disebut TC. (4) TC-AUTH-SES-170 Langkah 3 "sampai batas lock progression password terlampaui bila dihitung" kondisional dan batas tidak disebut; spec memakai Data Uji (5 kegagalan biometric). (5) TC-AUTH-SES-171 tidak menyebut cara mengunci akun; spec memakai langkah kunci yang di-seed BE. (6) TC-AUTH-SES-176 Expected b ('token lokal dihapus') tidak menyebut cara membaca penyimpanan token lokal; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan.
- Jumlah langkah (64) melewati sekitar 35 karena tiga TC berperangkat, masing-masing dengan user dan sesi sendiri, menyalin prefix enroll per TC (S-04) dan satu `Verifikasi` dipecah per klausa (S-01); tiap TC berdiri sendiri sehingga bagian sesudahnya tetap bermakna walau bagian di atasnya gagal. Blok enroll tidak dihitung ke batas ±35.
- Pengecualian `P-5` (b): TC-AUTH-SES-257 dan 258 (request langsung ke server, kelas a) adalah TC objek-uji ringan tanpa harness eksternal dan tanpa state berat sendiri, pada alur re-login biometric yang sama dengan TC lain di spec ini.
