---
id: TC-AUTH-SES-E2E-045-ketersediaan-biometric-perangkat-dan-ios
title: "Ketersediaan Biometric Perangkat Android, Enroll dan Re-login iOS, serta Enroll Ulang"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-147
  - TC-AUTH-SES-148
  - TC-AUTH-SES-149
  - TC-AUTH-SES-260
  - TC-AUTH-SES-261
coverage:
  web: automated
  mobile: automated
---

# Ketersediaan Biometric Perangkat Android, Enroll dan Re-login iOS, serta Enroll Ulang

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai terpasang di tiga perangkat uji (Tabel Data Uji Pre-setup #10): Android uji C (tanpa hardware biometric, TC-AUTH-SES-147), Android uji D (hardware biometric, tanpa sidik jari atau wajah terdaftar di OS, TC-AUTH-SES-148), iOS uji F (Face ID atau Touch ID terdaftar, TC-AUTH-SES-260 dan 261), dan Android uji B (hardware biometric dan sidik jari terdaftar, TC-AUTH-SES-149). Tanpa sesi aktif di aplikasi pada semua perangkat.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): lima user profil BIO milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #9 dan #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu; belum pernah enroll biometric), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-147: `Tari Kusuma` (`tarikusuma+{runId}-045@qwertysystem.net`), perangkat Android uji C
  - TC-AUTH-SES-148: `Budi Ramadhan` (`budiramadhan+{runId}-045@qwertysystem.net`), perangkat Android uji D
  - TC-AUTH-SES-260: `Taufik Wulandari` (`taufikwulandari+{runId}-045@qwertysystem.net`), perangkat iOS uji F
  - TC-AUTH-SES-261: `Mega Hidayat` (`megahidayat+{runId}-045@qwertysystem.net`), perangkat iOS uji F
  - TC-AUTH-SES-149: `Siti Wulandari` (`sitiwulandari+{runId}-045@qwertysystem.net`), perangkat Android uji B
- Token biometric lokal hanya dapat dibuat oleh aplikasi di perangkat, sehingga enroll yang menjadi kondisi awal TC-AUTH-SES-261 dan TC-AUTH-SES-149 dijalankan sebagai langkah (dependensi TC-AUTH-SES-260 dan alur enroll TC-AUTH-SES-145; cara menyiapkan token biometric lokal mengikuti Tabel Data Uji Pre-setup #29) dengan data aplikasi yang bersih. Kondisi awal TC-AUTH-SES-261 "tidak ada sesi aktif di perangkat itu" dipenuhi dengan mengakhiri sesi platform hasil login enroll lewat API yang disediakan tim BE tanpa menghapus token biometric lokal (Tabel Data Uji Pre-setup #29), bukan lewat Log Out UI.
- Browser Admin: konteks browser terpisah dengan akun aktor Total Control (Global Settings) di atas, login di hook `before`, untuk membaca `Global Settings > Activity Log > Session` (TC-AUTH-SES-261).
- Suite berjalan serial (`parallel: false`) karena perangkat Android uji B, C, D dan iOS uji F dipakai bersama; state yang diubah pada perangkat itu (data aplikasi, status "sudah ditawari", token biometric lokal, kredensial biometric user uji) dibersihkan di hook `after`.
- Hook `after`: hapus data aplikasi pada perangkat Android uji B, C, D dan iOS uji F, tutup Browser Admin, akhiri semua sesi seed, lalu hapus kelima user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile; akun aktor Total Control hanya di Browser Admin (TC-AUTH-SES-261).
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: hardware biometrik): driver otomasi Android dan iOS (aplikasi native) pada perangkat B, C, D, dan F; simulasi sensor sidik jari pada OS biometric prompt Android dan simulasi Face ID atau Touch ID pada iOS (verifikasi lulus); menghapus data aplikasi dan menghapus app dari recent apps atau app switcher lalu membukanya kembali; REST client alat uji yang dapat mengirim request langsung ke `POST /v2/iam/auth/biometric/enroll` (header `X-Session-ID` berisi ID sesi mobile aktif milik `Siti Wulandari`, body `deviceId` perangkat Android uji B) untuk TC-AUTH-SES-149 dan membaca status kredensial biometric user; API untuk mengakhiri sesi platform mobile `Mega Hidayat` hasil login enroll tanpa menghapus token biometric lokal (langkah 37; Tabel Data Uji Pre-setup #29), tanpa endpoint; pembacaan status sesi mobile user uji (langkah 41) dan penolakan token biometric lama (langkah 57) dari sisi backend, disediakan tim FE/BE.

## Test Steps

### TC-AUTH-SES-147: Prompt Enable Biometric tidak muncul pada perangkat tanpa hardware biometric

1. Buka aplikasi mobile di perangkat Android uji C → halaman Login tampil
2. Ketik `tarikusuma+{runId}-045@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.SES_PASSWORD` pada field Password
4. Klik [Login]
5. Verifikasi App masuk Portal — Product Hub tanpa Prompt Enable Biometric
6. Hapus app dari recent apps
7. Buka kembali app → halaman Login tampil
8. Ketik `tarikusuma+{runId}-045@qwertysystem.net` pada field Email
9. Ketik `Spectra.env.SES_PASSWORD` pada field Password
10. Klik [Login]
11. Verifikasi Prompt Enable Biometric tidak muncul pada login berikutnya

### TC-AUTH-SES-148: Prompt Enable Biometric tidak muncul pada perangkat yang belum punya biometric terdaftar di OS

12. Buka aplikasi mobile di perangkat Android uji D → halaman Login tampil
13. Ketik `budiramadhan+{runId}-045@qwertysystem.net` pada field Email
14. Ketik `Spectra.env.SES_PASSWORD` pada field Password
15. Klik [Login]
16. Verifikasi App masuk Portal — Product Hub tanpa Prompt Enable Biometric

### TC-AUTH-SES-260: Prompt Enable Biometric dan Screen biometric sign-in di iOS memakai Face ID atau Touch ID

17. Buka aplikasi mobile iOS di perangkat iOS uji F → halaman Login tampil
18. Ketik `taufikwulandari+{runId}-045@qwertysystem.net` pada field Email
19. Ketik `Spectra.env.SES_PASSWORD` pada field Password
20. Klik [Login] → Prompt Enable Biometric muncul
21. Verifikasi Prompt "Enable Face ID / Touch ID?" tampil
22. Verifikasi Body "Sign in faster next time without typing your password"
23. Ketuk [Enable] → OS biometric prompt muncul
24. Lulus Face ID atau Touch ID
25. Hapus app dari app switcher
26. Buka kembali app
27. Verifikasi Screen "Sign in with Face ID / Touch ID" tampil
28. Verifikasi Body "Sign in as taufikwulandari+{runId}-045@qwertysystem.net"
29. Verifikasi OS biometric prompt iOS muncul otomatis

### TC-AUTH-SES-261: Biometric re-login sukses di iOS membuat sesi baru

30. Di Browser Admin catat baseline jumlah entri `Login with biometric` `Mega Hidayat` di `Global Settings > Activity Log > Session`; reset data aplikasi di perangkat iOS uji F lalu buka aplikasi mobile iOS → halaman Login tampil
31. Ketik `megahidayat+{runId}-045@qwertysystem.net` pada field Email
32. Ketik `Spectra.env.SES_PASSWORD` pada field Password
33. Klik [Login] → Prompt Enable Biometric muncul
34. Ketuk [Enable] → OS biometric prompt muncul
35. Lulus Face ID atau Touch ID
36. Hapus app dari app switcher
37. Akhiri sesi platform mobile `megahidayat+{runId}-045@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal
38. Buka aplikasi mobile iOS → Screen biometric sign-in tampil
39. Lulus Face ID atau Touch ID
40. Verifikasi App masuk Portal — Product Hub
41. Verifikasi Sesi mobile baru berstatus Active untuk `Mega Hidayat`
42. Pindah ke Browser Admin (akun aktor Total Control sudah login di hook)
43. Buka `Global Settings > Activity Log > Session`
44. Verifikasi Dicatat `Login with biometric` untuk `Mega Hidayat` (dicari berdasarkan Note dan email): entri bertambah 1 dari baseline dengan Activity `Login`, Status `Success`, Note `Login with biometric`

### TC-AUTH-SES-149: Enroll ulang tanpa disable membuat token baru dan mencabut token lama

45. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
46. Ketik `sitiwulandari+{runId}-045@qwertysystem.net` pada field Email
47. Ketik `Spectra.env.SES_PASSWORD` pada field Password
48. Klik [Login] → Prompt Enable Biometric muncul
49. Ketuk [Enable] → OS biometric prompt muncul
50. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub dengan sesi platform mobile aktif
51. Kirim request enroll biometric kedua (`POST /v2/iam/auth/biometric/enroll`) dari perangkat yang sama dengan sesi valid `Siti Wulandari` tanpa menonaktifkan kredensial pertama
52. Hapus app dari recent apps
53. Buka kembali app
54. Lulus verifikasi biometric pada OS biometric prompt
55. Verifikasi Re-login berhasil memakai token baru
56. Verifikasi Hanya satu kredensial biometric Active milik `Siti Wulandari` pada perangkat Android uji B
57. Verifikasi Token lama sudah ditolak

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-147, 148, 260, 261, 149 (urutan TC sumber 147, 148, 149, 260, 261). TC yang menolak prompt didahulukan, TC-AUTH-SES-260 harus mendahului TC-AUTH-SES-261 (dependensi), dan TC-AUTH-SES-149 yang menimpa kredensial lewat request langsung ditaruh paling akhir.
- Dependensi (S-04): TC-AUTH-SES-261 bergantung pada TC-AUTH-SES-260; langkah 30–36 menyalin langkah enroll TC-AUTH-SES-260 (kondisi "sudah enroll" di Precondition) dan langkah 37 mengakhiri sesi platform hasil login enroll lewat API yang disediakan tim BE (Pre-setup #29). Langkah 45–50 pada TC-AUTH-SES-149 menyalin alur enroll TC-AUTH-SES-145 untuk membuat enroll pertama.
- Pengecualian P-2 (pemicu bukan objek uji): request enroll kedua yang dikirim langsung ke `POST /v2/iam/auth/biometric/enroll` lewat alat uji (langkah 51, kelas harness a) hanya memicu state "enroll ulang tanpa disable"; yang diasersi adalah hasilnya pada aplikasi dan backend (langkah 55 sampai 57), bukan perilaku endpoint enroll itu sendiri, sehingga spec ini tetap berkelas d (hardware biometrik).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): hapus atau reset data aplikasi di awal TC-AUTH-SES-261 dan TC-AUTH-SES-149 (status "sudah ditawari" dan token biometric lokal disimpan per perangkat); mengakhiri sesi platform hasil login enroll TC-AUTH-SES-261 lewat API yang disediakan tim BE (langkah 37); pindah antara perangkat mobile dan Browser Admin; langkah 6–11 pada TC-AUTH-SES-147 (menghapus app lalu login lagi) ditambahkan supaya Expected b "Prompt tidak pernah muncul pada login berikutnya" punya `Verifikasi` (S-14).
- Pembagian TC lintas spec: pencatatan `Login with biometric` (TC-AUTH-SES-261 Expected b) diasersi di sini; pencatatan detail (kolom Date, User, IP Address, Device / Browser) ada di spec pencatatan. Baseline log (S-12): jumlah entri dicatat di langkah 30 sebelum aksi; asersi mengasersi selisih jumlah. Tidak ada asersi "tidak ada pencatatan" di spec ini.
- Jumlah langkah (57) melewati sekitar 35 karena lima TC, masing-masing dengan user dan perangkat sendiri, menyalin prefix login mobile identik dan alur enroll per TC (S-04); tiap TC berdiri sendiri sehingga bagian sesudahnya tetap bermakna walau bagian di atasnya gagal.
- Temuan untuk QA: (1) TC sumber menulis "login ... dan password yang benar" tanpa menyebut field dan tombol; spec menguraikannya menjadi ketik email, ketik password, klik [Login] (label tombol login mobile tidak disebut TC). (2) TC-AUTH-SES-149: Expected a menyebut re-login berhasil "memakai token baru", tetapi langkah 51 (langkah 1 TC-AUTH-SES-149) mengirim enroll lewat alat uji (token plaintext baru dikembalikan ke alat uji, bukan disimpan ke secure storage perangkat), sehingga app tetap memakai token lama; selain itu TC tidak menyebut cara alat uji memperoleh ID sesi mobile aktif (header `X-Session-ID`) dan cara membaca "hanya satu kredensial Active" serta "token lama sudah ditolak". Spec mengikuti TC. (3) TC-AUTH-SES-261 Expected b ("sesi mobile baru Active dan dicatat") tidak menyebut cara membaca status sesi; spec mengasersi status sesi langsung dan pencatatan lewat Activity Log > Session (Activity/Status/Note mengikuti TC-AUTH-SES-209). (4) TC-AUTH-SES-260/261 tidak menyebut cara mereset data aplikasi dan Keychain pada iOS; spec menuliskan "reset data aplikasi" dan kemampuannya di Prerequisites. (5) TC-AUTH-SES-261 prakondisi b mensyaratkan tidak ada sesi aktif di perangkat, sedangkan enroll lewat Prompt Enable Biometric berlangsung setelah login password yang membuat sesi platform; TC tidak menyebut langkah mengakhirinya, sehingga spec mengakhirinya lewat API yang disediakan tim BE (Pre-setup #29) di langkah 37.
