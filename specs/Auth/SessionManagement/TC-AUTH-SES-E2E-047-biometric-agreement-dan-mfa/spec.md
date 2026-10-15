---
id: TC-AUTH-SES-E2E-047-biometric-agreement-dan-mfa
title: "Re-login Biometric dengan Agreement dan MFA"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-161
  - TC-AUTH-SES-162
  - TC-AUTH-SES-163
  - TC-AUTH-SES-164
  - TC-AUTH-SES-247
coverage:
  web: automated
  mobile: automated
---

# Re-login Biometric dengan Agreement dan MFA

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) terpasang di perangkat Android uji B (Tabel Data Uji Pre-setup #10: hardware biometric, sidik jari terdaftar di OS). Semua TC memakai perangkat yang sama.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): lima user milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON) berbasis profil BIO (Tabel Data Uji Pre-setup #9: belum pernah enroll biometric), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-164: `Bayu Kusuma` (`bayukusuma+{runId}-047@qwertysystem.net`), profil BIOPOL (Tabel Data Uji Pre-setup #22)
  - TC-AUTH-SES-247: `Maya Rahayu` (`mayarahayu+{runId}-047@qwertysystem.net`), profil BIOPOL
  - TC-AUTH-SES-162: `Eko Setiawan` (`ekosetiawan+{runId}-047@qwertysystem.net`), profil BIOPOL
  - TC-AUTH-SES-163: `Wulan Santoso` (`wulansantoso+{runId}-047@qwertysystem.net`), profil BIOPOLMFA (Tabel Data Uji Pre-setup #24)
  - TC-AUTH-SES-161: `Putri Wijaya` (`putriwijaya+{runId}-047@qwertysystem.net`), profil BIOMFA (Tabel Data Uji Pre-setup #23)
- Kondisi tambahan profil, diterapkan BE pada langkah "Terapkan kondisi" sesudah enroll (supaya login password saat enroll tidak memicu Agreement atau MFA): BIOPOL = state per-user: versi Privacy Policy yang terakhir disetujui user lebih lama dari versi aktif, disediakan tim FE/BE tanpa mempublish Privacy Policy global; BIOMFA = logout terakhir lebih dari 30 hari lalu sehingga MFA terpicu; BIOPOLMFA = keduanya. Untuk profil dengan MFA, Authenticator user sudah terdaftar dan secret TOTP dipegang aplikasi authenticator uji (Tabel Data Uji Pre-setup #18).
- Kondisi awal tiap TC "sudah enroll biometric di perangkat Android uji B; tidak ada sesi platform aktif" dibuat di dalam TC dengan menyalin langkah enroll TC-AUTH-SES-145 (hapus data aplikasi, login, [Enable], lulus sidik jari, hapus app dari recent apps), lalu mengakhiri sesi platform hasil login enroll lewat API yang disediakan tim BE tanpa menghapus token biometric lokal (cara menyiapkan mengikuti Tabel Data Uji Pre-setup #29), karena token biometric lokal dan status "sudah ditawari" disimpan di perangkat dan hanya dapat dibuat oleh aplikasi.
- Browser Admin: konteks browser terpisah dengan akun aktor Total Control (Global Settings) di atas, login di hook `before`, untuk membaca `Global Settings > Activity Log > Session` (TC-AUTH-SES-161 dan TC-AUTH-SES-164).
- Suite berjalan serial (`parallel: false`) karena perangkat Android uji B dipakai bersama; state yang diubah pada perangkat itu (data aplikasi, status "sudah ditawari", token biometric lokal) dan kondisi profil user uji dipulihkan di hook `after`.
- Hook `after`: hapus data aplikasi pada perangkat Android uji B, tutup Browser Admin, akhiri semua sesi seed, lalu hapus kelima user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile; akun aktor Total Control hanya di Browser Admin.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: hardware biometrik dan authenticator): driver otomasi Android (aplikasi native); simulasi sensor sidik jari pada OS biometric prompt (sidik jari terdaftar lulus); menghapus data aplikasi dan menghapus app dari recent apps lalu membukanya kembali; aplikasi authenticator uji (TOTP) yang menghasilkan kode valid untuk `Wulan Santoso` dan `Putri Wijaya`; fixture BE untuk kondisi tambahan profil di atas; pembacaan status sesi baru user uji dari sisi backend (langkah 16, 33, 82: "tidak ada sesi baru" dan "sesi dibuat"), dan API untuk mengakhiri sesi platform mobile user uji tanpa menghapus token biometric lokal (langkah sesudah tiap enroll), disediakan tim FE/BE.

## Test Steps

### TC-AUTH-SES-164: Continue tanpa centang Agreement ditolak dan tetap di Screen Confirm to Continue

1. Di Browser Admin catat baseline jumlah entri `Consent not given` `Bayu Kusuma` di `Global Settings > Activity Log > Session`; hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
2. Ketik `bayukusuma+{runId}-047@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.SES_PASSWORD` pada field Password
4. Klik [Login] → Prompt Enable Biometric muncul
5. Ketuk [Enable] → OS biometric prompt muncul
6. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
7. Hapus app dari recent apps
8. Akhiri sesi platform mobile `bayukusuma+{runId}-047@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal
9. Terapkan kondisi profil BIOPOL untuk `Bayu Kusuma` (versi Privacy Policy aktif lebih baru dari yang terakhir disetujui; di-seed BE)
10. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
11. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → Screen Confirm to Continue tampil
12. Ketuk [Continue ➔] tanpa mencentang checkbox
13. Verifikasi Server menolak [Continue ➔]
14. Verifikasi Caption "You need to agree to the Privacy Policy to continue" tampil
15. Verifikasi App tetap di Screen Confirm to Continue
16. Verifikasi Tidak ada sesi baru untuk `Bayu Kusuma`
17. Pindah ke Browser Admin (akun aktor Total Control sudah login di hook)
18. Buka `Global Settings > Activity Log > Session`
19. Verifikasi Entri `Consent not given` untuk `Bayu Kusuma` (dicari berdasarkan Note dan email) bertambah 1 dari baseline

### TC-AUTH-SES-247: Centang Agreement lalu Continue pada biometric re-login melanjutkan evaluasi device-trust dan MFA

20. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
21. Ketik `mayarahayu+{runId}-047@qwertysystem.net` pada field Email
22. Ketik `Spectra.env.SES_PASSWORD` pada field Password
23. Klik [Login] → Prompt Enable Biometric muncul
24. Ketuk [Enable] → OS biometric prompt muncul
25. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
26. Hapus app dari recent apps
27. Akhiri sesi platform mobile `mayarahayu+{runId}-047@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal
28. Terapkan kondisi profil BIOPOL untuk `Maya Rahayu` (versi Privacy Policy aktif lebih baru dari yang terakhir disetujui; di-seed BE)
29. Buka aplikasi mobile di perangkat Android uji B dan lulus OS biometric prompt → Screen Confirm to Continue tampil
30. Centang checkbox "I have read and agree to the Privacy Policy *"
31. Ketuk [Continue ➔]
32. Verifikasi Evaluasi device-trust berlanjut seperti biometric sukses tanpa Agreement trigger
33. Verifikasi Device-trust aman sehingga sesi baru dibuat untuk `Maya Rahayu`
34. Verifikasi App masuk Portal — Product Hub

### TC-AUTH-SES-162: Agreement terpicu pada biometric re-login menampilkan Screen Confirm to Continue sebelum evaluasi lain

35. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
36. Ketik `ekosetiawan+{runId}-047@qwertysystem.net` pada field Email
37. Ketik `Spectra.env.SES_PASSWORD` pada field Password
38. Klik [Login] → Prompt Enable Biometric muncul
39. Ketuk [Enable] → OS biometric prompt muncul
40. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
41. Hapus app dari recent apps
42. Akhiri sesi platform mobile `ekosetiawan+{runId}-047@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal
43. Terapkan kondisi profil BIOPOL untuk `Eko Setiawan` (versi Privacy Policy aktif lebih baru dari yang terakhir disetujui; di-seed BE)
44. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
45. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
46. Verifikasi Setelah biometric sukses Screen "Confirm to Continue" tampil lebih dulu
47. Verifikasi App belum masuk Portal — Product Hub dan belum ke halaman MFA
48. Centang checkbox "I have read and agree to the Privacy Policy *"
49. Ketuk [Continue ➔]
50. Verifikasi Setelah Continue app masuk Portal — Product Hub (device-trust aman)

### TC-AUTH-SES-163: Agreement dan MFA terpicu bersamaan: Agreement dikonfirmasi dulu baru MFA

51. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
52. Ketik `wulansantoso+{runId}-047@qwertysystem.net` pada field Email
53. Ketik `Spectra.env.SES_PASSWORD` pada field Password
54. Klik [Login] → Prompt Enable Biometric muncul
55. Ketuk [Enable] → OS biometric prompt muncul
56. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
57. Hapus app dari recent apps
58. Akhiri sesi platform mobile `wulansantoso+{runId}-047@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal
59. Terapkan kondisi profil BIOPOLMFA untuk `Wulan Santoso` (Privacy Policy lebih baru dan MFA terpicu; di-seed BE)
60. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
61. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
62. Verifikasi Urutan layar pertama: Screen Confirm to Continue tampil
63. Verifikasi Halaman MFA tidak muncul sebelum Agreement dikonfirmasi
64. Centang checkbox "I have read and agree to the Privacy Policy *"
65. Ketuk [Continue ➔]
66. Verifikasi Urutan layar kedua: halaman MFA tampil
67. Ketik kode TOTP yang benar dari aplikasi authenticator uji pada halaman MFA
68. Verifikasi Urutan layar ketiga: app masuk Portal — Product Hub

### TC-AUTH-SES-161: Biometric sukses tetap melewati MFA bila device-trust memicu dan Login with biometric dicatat setelah MFA

69. Di Browser Admin catat baseline jumlah entri `Login with biometric` `Putri Wijaya` di `Global Settings > Activity Log > Session`; hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
70. Ketik `putriwijaya+{runId}-047@qwertysystem.net` pada field Email
71. Ketik `Spectra.env.SES_PASSWORD` pada field Password
72. Klik [Login] → Prompt Enable Biometric muncul
73. Ketuk [Enable] → OS biometric prompt muncul
74. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
75. Hapus app dari recent apps
76. Akhiri sesi platform mobile `putriwijaya+{runId}-047@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal
77. Terapkan kondisi profil BIOMFA untuk `Putri Wijaya` (logout terakhir lebih dari 30 hari lalu sehingga MFA terpicu; di-seed BE)
78. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
79. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
80. Verifikasi Setelah biometric sukses app diarahkan ke halaman MFA (biometric tidak mem-bypass MFA)
81. Ketik kode TOTP yang benar dari aplikasi authenticator uji pada halaman MFA
82. Verifikasi Sesi dibuat untuk `Putri Wijaya` setelah MFA tuntas
83. Verifikasi App masuk Portal — Product Hub setelah MFA tuntas
84. Pindah ke Browser Admin (akun aktor Total Control sudah login di hook)
85. Buka `Global Settings > Activity Log > Session`
86. Verifikasi Entri `Login with biometric` untuk `Putri Wijaya` (dicari berdasarkan Note dan email) bertambah 1 dari baseline setelah MFA tuntas

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-164, 247, 162, 163, 161 (urutan TC sumber 161, 162, 163, 164, 247). Penolakan Continue tanpa centang (164) didahulukan sebelum alur sukses; alur dengan MFA (163, 161) ditaruh terakhir.
- Dependensi (S-04): TC-AUTH-SES-162, 164, 247 bergantung pada TC-AUTH-SES-16 (membuka app, lulus OS biometric prompt, Screen Confirm to Continue tampil); langkah itu disalin pada langkah 10–11, 29, dan 44–45. Semua TC bergantung pada enroll (TC-AUTH-SES-145): langkah enroll disalin di awal tiap TC, termasuk langkah mengakhiri sesi platform hasil login enroll lewat API yang disediakan tim BE tanpa menghapus token biometric lokal (Pre-setup #29), bukan lewat Log Out UI.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): "Hapus data aplikasi" mengosongkan status "sudah ditawari" dan token biometric lokal di awal tiap TC (S-09); langkah "Terapkan kondisi profil" menerapkan kondisi tambahan profil sesudah enroll; perpindahan ke Browser Admin.
- Pembagian TC lintas spec: asersi "tidak ada entri log tersendiri untuk persetujuan; hanya `Login with biometric`" (TC-AUTH-SES-162 Expected c) tidak ditulis di sini dan berada di spec absence `TC-AUTH-SES-E2E-070-absence-biometric` (kelas g, S-05). Rujukan pencatatan lain ke `TC-AUTH-SES-E2E-059-pencatatan-biometric`. Pencatatan `Consent not given` (TC-AUTH-SES-164 Expected c, rujukan TC-AUTH-SES-267) dan `Login with biometric` setelah MFA (TC-AUTH-SES-161 Expected c, rujukan TC-AUTH-SES-210) diasersi di sini sebagai pencatatan; asersi "belum ada entri sebelum MFA tuntas" (TC-AUTH-SES-210) berada di spec pencatatan `TC-AUTH-SES-E2E-059-pencatatan-biometric` (memuat aksi nyata untuk TC-AUTH-SES-210).
- Jumlah langkah (86) melewati sekitar 35 karena lima TC, masing-masing dengan user dan sesi sendiri, menyalin prefix enroll per TC (S-04) dan blok baca log; tiap TC berdiri sendiri sehingga bagian sesudahnya tetap bermakna walau bagian di atasnya gagal. Blok enroll tidak dihitung ke batas ±35.
- Temuan untuk QA: (1) TC sumber menulis login dan enroll tanpa menyebut field dan tombol; spec menguraikannya menjadi ketik email, ketik password, klik [Login] (label tombol login mobile tidak disebut TC). (2) Profil BIOPOL, BIOMFA, dan BIOPOLMFA menuntut kondisi (Privacy Policy lebih baru, logout lebih dari 30 hari) yang tidak boleh sudah berlaku saat enroll lewat login password; TC tidak menyebut urutan atau cara BE menerapkannya, sehingga spec menambah langkah "Terapkan kondisi" sesudah enroll. Sifat kondisi BIOPOL (per-user atau publish Privacy Policy global) tidak ditetapkan TC dan PRD; spec memperlakukannya sebagai state per-user. (3) TC-AUTH-SES-161 dan TC-AUTH-SES-163 tidak menyebut apakah Authenticator user sudah terdaftar dan apakah halaman MFA memerlukan klik tombol sesudah mengetik kode TOTP; spec mengasumsikan Authenticator terdaftar dan tanpa klik tambahan. (4) TC-AUTH-SES-247 Expected a ("evaluasi device-trust berlanjut seperti biometric sukses") tidak menyebut hasil yang dapat diamati selain Expected b; spec mengasersinya apa adanya. (6) Pre-setup #29 tidak menyebut API untuk mengakhiri sesi platform hasil login enroll; spec menuliskannya sebagai kemampuan yang disediakan tim BE tanpa endpoint karangan. (5) TC-AUTH-SES-164 dan TC-AUTH-SES-161 membaca pencatatan dari Browser Admin tanpa menyebut filter user; spec menyebut entri milik user terkait.
- Baseline log (S-12): jumlah entri dicatat di langkah 1 dan 69 sebelum aksi; asersi mencari entri berdasarkan Note dan email dan mengasersi selisih jumlah. Asersi log hanya kemunculan entri sesuai Expected c TC-AUTH-SES-164 dan TC-AUTH-SES-161; kolom Activity, Status, dan Note diasersi di TC pencatatan (TC-AUTH-SES-267 dan TC-AUTH-SES-210).
