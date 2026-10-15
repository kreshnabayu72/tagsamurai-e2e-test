---
id: TC-AUTH-SES-E2E-050-biometric-siklus-token-90-hari-dan-rotasi
title: "Siklus Token Biometric 90 Hari, Perubahan Enrollment OS, dan Rotasi Token"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-SES-172
  - TC-AUTH-SES-173
  - TC-AUTH-SES-285
  - TC-AUTH-SES-181
  - TC-AUTH-SES-236
  - TC-AUTH-SES-237
coverage:
  mobile: automated
---

# Siklus Token Biometric 90 Hari, Perubahan Enrollment OS, dan Rotasi Token

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) terpasang di perangkat Android uji B (Tabel Data Uji Pre-setup #10: hardware biometric, sidik jari terdaftar di OS). Semua TC memakai perangkat yang sama.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): enam user profil BIO milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #9: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-172: `Reza Puspita` (`rezapuspita+{runId}-050@qwertysystem.net`)
  - TC-AUTH-SES-173: `Sari Saputra` (`sarisaputra+{runId}-050@qwertysystem.net`)
  - TC-AUTH-SES-285: `Intan Anggraini` (`intananggraini+{runId}-050@qwertysystem.net`)
  - TC-AUTH-SES-236: `Irfan Setiawan` (`irfansetiawan+{runId}-050@qwertysystem.net`)
  - TC-AUTH-SES-237: `Tari Santoso` (`tarisantoso+{runId}-050@qwertysystem.net`)
  - TC-AUTH-SES-181: `Dewi Kusuma` (`dewikusuma+{runId}-050@qwertysystem.net`)
- Kondisi "sudah enroll biometric di perangkat Android uji B, tanpa sesi platform aktif" per user disiapkan lewat alur Prompt Enable Biometric (login, [Enable], lulus verifikasi sidik jari; TC-AUTH-SES-14): user TC-AUTH-SES-172 di hook `before` (sesi platform hasil login enroll diakhiri lewat API yang disediakan tim BE tanpa menghapus token biometric lokal), user TC berikutnya lewat langkah enroll yang ditulis utuh di awal tiap TC (mengikuti Pre-setup #29; bila TC mensyaratkan tanpa sesi platform aktif, sesi hasil login enroll diakhiri lewat API yang disediakan tim BE tanpa menghapus token biometric lokal), karena token biometric lokal dan email cache lokal disimpan per perangkat (satu user per perangkat). Pada TC-AUTH-SES-236 dan TC-AUTH-SES-237 respons request enroll ditangkap proxy jaringan agar token plaintext (T1) tersimpan di alat uji.
- Suite berjalan serial (`parallel: false`), juga karena perangkat Android uji B dipakai bersama; state global yang diubah: jam server dan jam browser/perangkat, diatur bersama oleh pengatur waktu (Tabel Data Uji Pre-setup #18); tiap TC yang memajukan jam mengakhiri dengan langkah memulihkan jam server dan jam browser/perangkat ke waktu nyata supaya enrollment user TC berikutnya tidak ikut kedaluwarsa, dan dipulihkan di hook `after`.
- Hook `after`: pulihkan jam server dan jam browser/perangkat ke waktu nyata; hapus sidik jari tambahan yang ditambahkan TC-AUTH-SES-181 di pengaturan OS perangkat Android uji B; hapus data aplikasi pada perangkat; akhiri semua sesi seed; hapus keenam user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile; akun aktor hanya di hook.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: hardware biometrik dan time-travel): driver otomasi Android (aplikasi native); menghapus app dari recent apps lalu membukanya kembali; menutup paksa dan menghapus data aplikasi; simulasi sensor sidik jari pada OS biometric prompt (sidik jari terdaftar lulus); menambah dan menghapus sidik jari di pengaturan OS perangkat; pengatur waktu yang mengatur jam server dan jam browser/perangkat bersama, termasuk menyetel keduanya ke nilai absolut (T-terbit ditambah 90 hari pada TC-AUTH-SES-285, langkah 39) dan memulihkannya ke waktu nyata, serta membaca waktu server saat enroll berhasil sebagai T-terbit (langkah 36); pembacaan status sesi user uji dari sisi backend (langkah 85, "tidak ada sesi baru" TC-AUTH-SES-181) dan API untuk mengakhiri sesi platform mobile user uji hasil login enroll tanpa menghapus token biometric lokal (langkah sesudah enroll TC-AUTH-SES-173, 285, 181), disediakan tim FE/BE; proxy jaringan (Tabel Data Uji Pre-setup #18) untuk membaca request dan respons enroll serta relogin; alat uji untuk mengirim request relogin langsung (`/v2/iam/auth/biometric/relogin`) dengan ID device dan token tertentu.

## Test Steps

### TC-AUTH-SES-172: Setiap re-login sukses memperpanjang masa berlaku token biometric 90 hari

1. Majukan jam server dan jam browser/perangkat bersama 60 hari
2. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
3. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
4. Verifikasi Re-login pertama berhasil
5. Verifikasi Token baru diterbitkan pada re-login pertama (respons relogin memuat token baru)
6. Hapus app dari recent apps
7. Majukan jam server dan jam browser/perangkat bersama 60 hari lagi (total 120 hari sejak enroll)
8. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
9. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
10. Verifikasi Re-login kedua berhasil walau total 120 hari sejak enroll karena masa berlaku diperpanjang pada re-login pertama
11. Verifikasi Token baru diterbitkan pada re-login kedua (respons relogin memuat token baru)
12. Hapus app dari recent apps
13. Pulihkan jam server dan jam browser/perangkat ke waktu nyata

### TC-AUTH-SES-173: Token biometric yang tidak dipakai lebih dari 90 hari kedaluwarsa dan fallback ke Login penuh

14. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu buka aplikasi mobile → halaman Login tampil
15. Ketik `sarisaputra+{runId}-050@qwertysystem.net` pada field Email
16. Ketik `Spectra.env.SES_PASSWORD` pada field Password
17. Klik [Login] → Prompt Enable Biometric muncul
18. Ketuk [Enable] → OS biometric prompt muncul
19. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub (email cache lokal = email itu)
20. Hapus app dari recent apps
21. Akhiri sesi platform mobile `sarisaputra+{runId}-050@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal
22. Majukan jam server dan jam browser/perangkat bersama 91 hari
23. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
24. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
25. Verifikasi Server menolak relogin karena masa berlaku lewat (respons token tidak valid)
26. Verifikasi Halaman Login penuh tampil
27. Hapus app dari recent apps lalu buka kembali aplikasi mobile
28. Verifikasi Token lokal dihapus: halaman Login (form) tampil, bukan Screen biometric sign-in
29. Pulihkan jam server dan jam browser/perangkat ke waktu nyata

### TC-AUTH-SES-285: Token biometric pada hari ke-90 sejak terbit terakhir masih valid

30. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu buka aplikasi mobile → halaman Login tampil
31. Ketik `intananggraini+{runId}-050@qwertysystem.net` pada field Email
32. Ketik `Spectra.env.SES_PASSWORD` pada field Password
33. Klik [Login] → Prompt Enable Biometric muncul
34. Ketuk [Enable] → OS biometric prompt muncul
35. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub (email cache lokal = email itu)
36. Catat waktu terbit token biometric (waktu server saat enroll berhasil) sebagai T-terbit
37. Hapus app dari recent apps
38. Akhiri sesi platform mobile `intananggraini+{runId}-050@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal
39. Set jam server dan jam browser/perangkat bersama ke T-terbit ditambah tepat 90 hari (absolut, bukan digeser relatif)
40. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
41. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
42. Verifikasi Re-login berhasil dan app masuk Portal — Product Hub
43. Verifikasi Token baru diterbitkan (respons relogin memuat token baru)
44. Hapus app dari recent apps
45. Pulihkan jam server dan jam browser/perangkat ke waktu nyata

### TC-AUTH-SES-236: Refresh token biometric tidak pernah dapat diambil ulang dari server

46. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu buka aplikasi mobile → halaman Login tampil
47. Ketik `irfansetiawan+{runId}-050@qwertysystem.net` pada field Email
48. Ketik `Spectra.env.SES_PASSWORD` pada field Password
49. Klik [Login] → Prompt Enable Biometric muncul
50. Ketuk [Enable] → OS biometric prompt muncul; proxy jaringan menangkap respons request enroll
51. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub (email cache lokal = email itu)
52. Hapus app dari recent apps
53. Periksa respons request enroll yang ditangkap proxy
54. Verifikasi Token plaintext hanya dikembalikan satu kali, pada respons enroll
55. Kirim lewat alat uji request langsung, satu per satu, request terautentikasi milik `Irfan Setiawan` ke setiap endpoint Session Management yang tersedia selain enroll, lalu periksa respons masing-masing
56. Verifikasi Tidak ada endpoint yang mengembalikan token plaintext lagi
57. Hapus app dari recent apps

### TC-AUTH-SES-237: Token biometric lama ditolak setelah rotasi pada re-login sukses

58. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu buka aplikasi mobile → halaman Login tampil
59. Ketik `tarisantoso+{runId}-050@qwertysystem.net` pada field Email
60. Ketik `Spectra.env.SES_PASSWORD` pada field Password
61. Klik [Login] → Prompt Enable Biometric muncul
62. Ketuk [Enable] → OS biometric prompt muncul; proxy jaringan menangkap respons request enroll sebagai token lama T1
63. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub (email cache lokal = email itu)
64. Hapus app dari recent apps
65. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
66. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → re-login biometric sukses dan token baru T2 terbit (tertangkap proxy)
67. Hapus app dari recent apps
68. Kirim lewat alat uji request relogin langsung ke `/v2/iam/auth/biometric/relogin` dengan ID device perangkat Android uji B dan token T1 (lama)
69. Verifikasi Request ditolak (token tidak valid)
70. Verifikasi Tidak ada sesi dibuat oleh request tersebut (respons tidak memuat sessionId dan tidak ada cookie `sid` baru)

### TC-AUTH-SES-181: Perubahan enrollment biometric OS membuat token tidak dapat dipakai dan fallback ke Login penuh

71. Tutup paksa aplikasi mobile di perangkat Android uji B, hapus data aplikasi, lalu buka aplikasi mobile → halaman Login tampil
72. Ketik `dewikusuma+{runId}-050@qwertysystem.net` pada field Email
73. Ketik `Spectra.env.SES_PASSWORD` pada field Password
74. Klik [Login] → Prompt Enable Biometric muncul
75. Ketuk [Enable] → OS biometric prompt muncul
76. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub (email cache lokal = email itu)
77. Hapus app dari recent apps
78. Akhiri sesi platform mobile `dewikusuma+{runId}-050@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal
79. Tambahkan sidik jari baru di pengaturan OS perangkat Android uji B
80. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
81. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
82. Verifikasi Token tidak dapat di-decrypt
83. Verifikasi Token tidak pernah dikirim (proxy jaringan tidak menangkap request relogin dari perangkat)
84. Verifikasi App diarahkan ke halaman Login penuh
85. Verifikasi Biometric baru yang didaftarkan orang lain tidak mewarisi akses: tidak ada sesi baru yang dibuat untuk `Dewi Kusuma`
86. Hapus sidik jari tambahan di pengaturan OS perangkat Android uji B

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-172, 173, 285, 236, 237, 181 (urutan TC sumber 172, 173, 181, 285, 236, 237). TC-AUTH-SES-181 mengubah enrollment sidik jari di OS perangkat B sehingga merusak token biometric semua user di perangkat itu; ditaruh paling akhir. TC-AUTH-SES-285 mengikuti TC-AUTH-SES-173 sesuai kolom Dependensi.
- TC-AUTH-SES-285 berdependensi pada TC-AUTH-SES-173 hanya pada pola time-travel 90/91 hari; user TC-AUTH-SES-285 tidak boleh memakai token yang sudah kedaluwarsa di TC-AUTH-SES-173, jadi langkah dependensi tidak disalin dan user dibuat terpisah (S-04, S-06).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): menghapus app dari recent apps; menyiapkan enrollment user TC berikutnya (langkah 14, 30, 46, 58, 71); mengakhiri sesi platform hasil login enroll lewat API yang disediakan tim BE tanpa menghapus token biometric lokal (langkah 21, 38, 77; Pre-setup #29), bukan lewat Log Out UI; mencatat T-terbit (langkah 36); memajukan dan memulihkan waktu server; mengirim request langsung (langkah 55 dan 68 adalah aksi); memulihkan sidik jari tambahan (langkah 86). Memulihkan waktu server dan sidik jari juga dilakukan di hook `after` sebagai cadangan.
- Pencatatan: TC-AUTH-SES-173 Expected b ("tidak ada entri log" di `Global Settings > Activity Log > Session` dan User Log `Sari Saputra`) adalah asersi absence dan ditaruh di spec absence `TC-AUTH-SES-E2E-070-absence-biometric`; spec ini tidak mengasersinya (S-05).
- Asersi tambahan di luar Expected TC (S-03): langkah 4 ("Re-login pertama berhasil") mengasersi prasyarat Expected a TC-AUTH-SES-172 (masa berlaku diperpanjang pada re-login pertama) sehingga re-login kedua bermakna; langkah 70 menjabarkan "tidak ada sesi dibuat" (Expected TC-AUTH-SES-237) sebagai respons tanpa `sessionId` dan tanpa cookie `sid` baru berdasarkan `auth/session-management/API/openapi.yaml` (relogin: `sessionId` dan cookie `sid` hanya pada outcome `success`).
- TC-AUTH-SES-285: T-terbit dicatat di langkah 36 sebagai waktu server saat enroll berhasil; jam server dan jam browser/perangkat disetel absolut ke T-terbit ditambah tepat 90 hari pada langkah 39 (bukan digeser relatif, bagian 6) supaya detik nyata sejak enroll tidak membuat umur token melebihi 90 hari, lalu dipulihkan pada langkah 45.
- Jumlah langkah (86) melewati sekitar 35 karena enam TC, masing-masing dengan user dan sesi sendiri, menyalin prefix enroll per TC (S-04) dan blok pengaturan jam; tiap TC berdiri sendiri sehingga bagian sesudahnya tetap bermakna walau bagian di atasnya gagal. Blok enroll tidak dihitung ke batas ±35.
- Temuan untuk QA: (1) TC-AUTH-SES-172, 173, 285, 236, 237, 181 menyebut "sudah enroll biometric" tanpa langkah penyiapan, sementara satu perangkat hanya menyimpan satu token dan email cache lokal; langkah enroll ditulis utuh di awal tiap TC (mengikuti Pre-setup #29) dan perlu konfirmasi QA (S-15). (2) TC-AUTH-SES-236 langkah "coba ambil ulang token plaintext lewat request apa pun" ambigu; spec mengirim request terautentikasi ke setiap endpoint Session Management selain enroll dan memeriksa respons. (3) TC-AUTH-SES-181 Expected b ("biometric baru yang didaftarkan orang lain tidak mewarisi akses") dan langkah 3 ("sidik jari yang terdaftar") tidak menyebut sidik jari mana yang dipakai setelah penambahan; spec memakai sidik jari terdaftar semula. (4) TC-AUTH-SES-172 dan 285 Expected tidak menyebut tujuan setelah re-login; langkah 42 pada TC-AUTH-SES-285 memakai Portal — Product Hub seperti TC biometric lain. (5) TC-AUTH-SES-285 mencantumkan dependensi TC-AUTH-SES-173 tanpa kebutuhan state bersama. (6) TC-AUTH-SES-285 tidak menyebut cara membaca waktu terbit token; spec memakai waktu server saat enroll berhasil. (7) Pre-setup #29 tidak menyebut API untuk mengakhiri sesi platform hasil login enroll; spec menuliskannya sebagai kemampuan yang disediakan tim BE tanpa endpoint karangan; TC-AUTH-SES-236 dan 237 tidak menyatakan "tanpa sesi platform aktif" sehingga sesi enroll tidak diakhiri (TC-AUTH-SES-236 memakai sesi itu untuk request terautentikasi).
