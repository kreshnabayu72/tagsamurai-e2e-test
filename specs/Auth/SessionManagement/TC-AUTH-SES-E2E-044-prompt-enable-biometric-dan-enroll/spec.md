---
id: TC-AUTH-SES-E2E-044-prompt-enable-biometric-dan-enroll
title: "Prompt Enable Biometric: Not now, Tutup Prompt, Cancel OS Prompt, dan Enroll"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-145
  - TC-AUTH-SES-146
  - TC-AUTH-SES-324
  - TC-AUTH-SES-259
  - TC-AUTH-SES-313
  - TC-AUTH-SES-315
  - TC-AUTH-SES-314
coverage:
  mobile: automated
---

# Prompt Enable Biometric: Not now, Tutup Prompt, Cancel OS Prompt, dan Enroll

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) terpasang di perangkat Android uji B (Tabel Data Uji Pre-setup #10: hardware biometric, sidik jari terdaftar di OS). Semua TC memakai perangkat yang sama.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): enam user profil BIO milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #9 dan #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu; belum pernah enroll biometric), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-145: `Nadia Setiawan` (`nadiasetiawan+{runId}-044@qwertysystem.net`)
  - TC-AUTH-SES-146 dan TC-AUTH-SES-324: `Irfan Santoso` (`irfansantoso+{runId}-044@qwertysystem.net`)
  - TC-AUTH-SES-259: `Ayu Ramadhan` (`ayuramadhan+{runId}-044@qwertysystem.net`)
  - TC-AUTH-SES-313: `Bayu Wulandari` (`bayuwulandari+{runId}-044@qwertysystem.net`)
  - TC-AUTH-SES-314: `Intan Hidayat` (`intanhidayat+{runId}-044@qwertysystem.net`)
  - TC-AUTH-SES-315: `Joko Utami` (`jokoutami+{runId}-044@qwertysystem.net`)
- Status "sudah ditawari" Prompt Enable Biometric dan token biometric lokal disimpan di sisi client per perangkat (PRD F-AUTHSES-17), sehingga tiap TC dimulai dari kondisi bersih lewat langkah "Hapus data aplikasi" pada perangkat Android uji B.
- Suite berjalan serial (`parallel: false`) karena perangkat Android uji B dipakai bersama oleh seluruh TC spec ini; state yang diubah pada perangkat itu (data aplikasi, status "sudah ditawari", token biometric lokal) dibersihkan di hook `after`.
- Hook `after`: hapus data aplikasi pada perangkat Android uji B, akhiri semua sesi seed, lalu hapus keenam user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile; tanpa akun aktor di langkah.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: hardware biometrik): driver otomasi Android (aplikasi native); menghapus data aplikasi; menghapus app dari recent apps lalu membukanya kembali; menekan tombol back OS dan mengetuk area di luar prompt; simulasi sensor sidik jari pada OS biometric prompt (sidik jari terdaftar lulus) dan pembatalan OS biometric prompt; pembacaan status kredensial biometric user uji dari sisi backend (langkah 8, 19, 36, 44: "tidak ada kredensial biometric yang tersimpan"), disediakan tim FE/BE.

## Test Steps

### TC-AUTH-SES-146: Not now pada Prompt Enable Biometric menutup prompt tanpa perubahan

1. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
2. Ketik `irfansantoso+{runId}-044@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.SES_PASSWORD` pada field Password
4. Klik [Login] → Prompt Enable Biometric muncul
5. Ketuk [Not now]
6. Verifikasi Prompt tertutup
7. Verifikasi App masuk Portal — Product Hub
8. Verifikasi Tidak ada kredensial biometric yang tersimpan untuk `Irfan Santoso`
9. Hapus app dari recent apps
10. Buka kembali app
11. Verifikasi Setelah app dibuka kembali halaman Login (form) tampil, bukan Screen "Sign in with Face ID / Touch ID"

### TC-AUTH-SES-324: Prompt Enable Biometric tidak muncul lagi pada login berikutnya setelah Not now

12. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
13. Ketik `irfansantoso+{runId}-044@qwertysystem.net` pada field Email
14. Ketik `Spectra.env.SES_PASSWORD` pada field Password
15. Klik [Login] → Prompt Enable Biometric muncul
16. Ketuk [Not now]
17. Verifikasi Prompt tertutup
18. Verifikasi App masuk Portal — Product Hub
19. Verifikasi Tidak ada kredensial biometric yang tersimpan untuk `Irfan Santoso`
20. Hapus app dari recent apps
21. Buka kembali app
22. Verifikasi Setelah app dibuka kembali halaman Login (form) tampil, bukan Screen "Sign in with Face ID / Touch ID"
23. Ketik `irfansantoso+{runId}-044@qwertysystem.net` pada field Email
24. Ketik `Spectra.env.SES_PASSWORD` pada field Password
25. Klik [Login]
26. Verifikasi App masuk Portal — Product Hub tanpa Prompt Enable Biometric (perangkat sudah pernah ditawari)
27. Buka Settings > Security
28. Verifikasi Settings > Security tetap tersedia

### TC-AUTH-SES-259: Escape pada Prompt Enable Biometric menutup prompt dengan efek Not now

29. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
30. Ketik `ayuramadhan+{runId}-044@qwertysystem.net` pada field Email
31. Ketik `Spectra.env.SES_PASSWORD` pada field Password
32. Klik [Login] → Prompt Enable Biometric muncul
33. Tekan tombol back OS
34. Verifikasi Prompt tertutup dengan efek [Not now]
35. Verifikasi App masuk Portal — Product Hub
36. Verifikasi Tidak ada kredensial biometric yang tersimpan untuk `Ayu Ramadhan`

### TC-AUTH-SES-313: Klik backdrop pada Prompt Enable Biometric menutup prompt dengan efek Not now

37. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
38. Ketik `bayuwulandari+{runId}-044@qwertysystem.net` pada field Email
39. Ketik `Spectra.env.SES_PASSWORD` pada field Password
40. Klik [Login] → Prompt Enable Biometric muncul
41. Ketuk area gelap di luar prompt
42. Verifikasi Prompt tertutup dengan efek [Not now]
43. Verifikasi App masuk Portal — Product Hub
44. Verifikasi Tidak ada kredensial biometric yang tersimpan untuk `Bayu Wulandari`

### TC-AUTH-SES-314: Cancel OS biometric prompt saat enroll kembali tanpa enroll dan tanpa error

45. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
46. Ketik `intanhidayat+{runId}-044@qwertysystem.net` pada field Email
47. Ketik `Spectra.env.SES_PASSWORD` pada field Password
48. Klik [Login] → Prompt Enable Biometric muncul
49. Ketuk [Enable] → OS biometric prompt muncul
50. Batalkan (cancel) OS biometric prompt
51. Verifikasi App kembali tanpa enroll biometric
52. Verifikasi Tidak ada toast error
53. Hapus app dari recent apps
54. Buka kembali app
55. Verifikasi Setelah app dibuka kembali halaman Login (form) tampil, bukan Screen "Sign in with Face ID / Touch ID"

### TC-AUTH-SES-145: Accept pada Prompt Enable Biometric menyimpan token gated biometric dan re-entry berikutnya memakai biometric

56. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
57. Ketik `nadiasetiawan+{runId}-044@qwertysystem.net` pada field Email
58. Ketik `Spectra.env.SES_PASSWORD` pada field Password
59. Klik [Login] → Prompt Enable Biometric muncul
60. Ketuk [Enable] → OS biometric prompt muncul
61. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
62. Verifikasi Enrollment berhasil
63. Verifikasi App masuk Portal — Product Hub
64. Verifikasi Tidak ada toast sukses
65. Hapus app dari recent apps
66. Buka kembali app
67. Verifikasi Screen "Sign in with Face ID / Touch ID" tampil menggantikan form Login

### TC-AUTH-SES-315: Enroll biometric belakangan lewat toggle Settings > Security setelah memilih Not now

68. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
69. Ketik `jokoutami+{runId}-044@qwertysystem.net` pada field Email
70. Ketik `Spectra.env.SES_PASSWORD` pada field Password
71. Klik [Login] → Prompt Enable Biometric muncul
72. Ketuk [Not now] → app masuk Portal — Product Hub
73. Buka Settings > Security
74. Nyalakan toggle "Face ID / Touch ID" → OS biometric prompt muncul
75. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
76. Verifikasi Toggle "Face ID / Touch ID" tampil aktif
77. Verifikasi toast sukses: "Success, biometric enabled."
78. Hapus app dari recent apps
79. Buka kembali app
80. Verifikasi Screen "Sign in with Face ID / Touch ID" tampil

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pembagian TC lintas spec: asersi "tidak ada pencatatan" untuk enroll dan disable biometric (TC-AUTH-SES-145 Expected c, merujuk TC-AUTH-SES-212) tidak ditulis di spec ini; ia berada di spec absence `TC-AUTH-SES-E2E-070-absence-biometric` (aksi enroll dan disable nyata dengan baseline sendiri, S-05).
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-146, 324, 259, 313, 314, 145, 315 (urutan TC sumber 145, 146, 324, 259, 313, 315, 314). Penolakan dan penutupan prompt tanpa enroll didahulukan; dua TC yang berhasil enroll (145 dan 315) ditaruh paling akhir karena meninggalkan token biometric lokal di perangkat.
- Dependensi (S-04): TC-AUTH-SES-145, 146, 324, 259, 313, 314 bergantung pada TC-AUTH-SES-14 (login pertama sampai Prompt Enable Biometric muncul); langkah-langkahnya (buka app, ketik email dan password, klik [Login]) disalin di tiap TC. TC-AUTH-SES-315 bergantung pada TC-AUTH-SES-146; langkah 68–72 menyalin login sampai [Not now]. Screening isi Prompt (Title, Body, tombol) diuji TC-AUTH-SES-14 di spec lain.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): "Hapus data aplikasi" di awal tiap TC mengosongkan status "sudah ditawari" dan token biometric lokal (disimpan per perangkat) supaya TC berikutnya memulai dari kondisi bersih (S-09); langkah menghapus app dari recent apps dan membukanya kembali; langkah 27 (buka Settings > Security) dan 73 (arah ke Settings > Security).
- Jumlah langkah (80) melewati sekitar 35 karena tujuh TC, masing-masing dengan user dan sesi login sendiri, menyalin prefix login mobile identik (hapus data aplikasi sampai klik [Login], S-04) dan blok penutupan app; tiap TC berdiri sendiri sehingga bagian sesudahnya tetap bermakna walau bagian di atasnya gagal. Langkah `Verifikasi` yang bermajemuk dipecah per klausa (S-01).
- Temuan untuk QA: (1) TC sumber menulis "login dengan ... dan password yang benar" tanpa menyebut field dan tombol; spec menguraikannya menjadi ketik email, ketik password, klik [Login] mengikuti TC sesi lain (label tombol login mobile tidak disebut TC). (2) TC-AUTH-SES-259 menyebut "tombol back OS atau gestur tutup yang setara Escape" (alternatif); spec memakai tombol back OS. (3) TC-AUTH-SES-314 Expected a "app kembali tanpa enroll" tidak menyebut layar tujuan; spec mengasersi apa adanya. (4) TC-AUTH-SES-324 memakai user yang sama dengan TC-AUTH-SES-146; PRD F-AUTHSES-17 menyebut status "sudah ditawari" disimpan per perangkat (Changelog TC menyebut "per user per perangkat"), sehingga spec menghapus data aplikasi sebelum TC-AUTH-SES-324. (5) TC-AUTH-SES-146/324 Expected b "tidak ada kredensial biometric yang tersimpan" tidak menyebut cara membacanya; spec mengasersinya langsung setelah [Not now].
