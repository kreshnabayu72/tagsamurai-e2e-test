---
id: TC-AUTH-SES-E2E-079-logout-manual-mobile-dan-ganti-akun
title: "Logout Manual di Mobile dengan dan tanpa Biometric serta Ganti Akun di Perangkat yang Sama"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-331
  - TC-AUTH-SES-332
  - TC-AUTH-SES-333
coverage:
  web: automated
  mobile: automated
---

# Logout Manual di Mobile dengan dan tanpa Biometric serta Ganti Akun di Perangkat yang Sama

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) terpasang di perangkat Android uji B (Tabel Data Uji Pre-setup #10: hardware biometric dan sidik jari terdaftar di OS; TC-AUTH-SES-331 dan 333) dan perangkat Android uji A (TC-AUTH-SES-332). Tanpa sesi aktif di aplikasi pada kedua perangkat saat spec dimulai.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, Tabel Data Uji Pre-setup #1, kredensial `Spectra.env.GS_TC_PASSWORD`): empat user milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu; belum pernah enroll biometric), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-331: `Ratna Kusuma` (`ratnakusuma+{runId}-079@qwertysystem.net`), profil BIO (Tabel Data Uji Pre-setup #9), perangkat Android uji B
  - TC-AUTH-SES-332: `Bambang Lestari` (`bambanglestari+{runId}-079@qwertysystem.net`), profil BASE, perangkat Android uji A
  - TC-AUTH-SES-333: `Citra Halim` (`citrahalim+{runId}-079@qwertysystem.net`), profil BIO, perangkat Android uji B
  - TC-AUTH-SES-333: `Dodi Pratama` (`dodipratama+{runId}-079@qwertysystem.net`), profil BIO, belum pernah login di perangkat Android uji B
- Kondisi "sudah enroll biometric di perangkat Android uji B dengan sesi mobile Active" (TC-AUTH-SES-331 dan 333) dibuat sebagai langkah dengan alur Prompt Enable Biometric (login, [Enable], lulus verifikasi sidik jari; TC-AUTH-SES-14 dan 15; Tabel Data Uji Pre-setup #29) dengan data aplikasi yang bersih, karena token biometric lokal hanya dapat dibuat aplikasi di perangkat; sesi hasil login enroll dibiarkan Active. Sesi mobile `Bambang Lestari` dibuat lewat login nyata di perangkat Android uji A dan ketuk [Not now] bila Prompt Enable Biometric muncul (Tabel Data Uji Pre-setup #28).
- Browser Admin (login di hook `before`): akun aktor Total Control (Global Settings) di atas, membaca `Global Settings > Activity Log > Session` dan status sesi serta kredensial biometric user uji.
- Suite berjalan serial (`parallel: false`) karena perangkat Android uji A dan B dipakai bersama; state yang diubah pada perangkat itu (data aplikasi, status "sudah ditawari", token biometric lokal, kredensial biometric user uji) dibersihkan di hook `after`.
- Hook `after`: hapus data aplikasi pada perangkat Android uji A dan B, akhiri semua sesi seed, tutup konteks Browser Admin, lalu hapus keempat user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: hardware biometrik): driver otomasi Android (aplikasi native) pada perangkat A dan B; simulasi sensor sidik jari pada OS biometric prompt Android (verifikasi lulus); menghapus data aplikasi dan menghapus app dari recent apps lalu membukanya kembali; pembacaan status sesi mobile dan status kredensial biometric user di server oleh akun aktor, disediakan tim FE/BE.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile; akun aktor Total Control (Global Settings) pada Browser Admin.

## Test Steps

### TC-AUTH-SES-331: Logout manual di mobile oleh user biometric menampilkan form Login dan tidak menghapus token biometric

1. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
2. Ketik `ratnakusuma+{runId}-079@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.SES_PASSWORD` pada field Password
4. Klik [Login] → Prompt Enable Biometric muncul
5. Ketuk [Enable] → OS biometric prompt muncul
6. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub dengan sesi mobile Active
7. Di Browser Admin buka `Global Settings > Activity Log > Session` dan catat baseline jumlah entri `Logged out` untuk `ratnakusuma+{runId}-079@qwertysystem.net`
8. Di aplikasi mobile perangkat Android uji B buka menu Profile lalu pilih Log Out
9. Amati layar tepat setelah logout
10. Verifikasi Tepat setelah logout form Login tampil
11. Verifikasi Screen biometric sign-in tidak tampil tepat setelah logout
12. Verifikasi Sesi mobile `Ratna Kusuma` berstatus Logged Out
13. Di Browser Admin muat ulang `Global Settings > Activity Log > Session` dan cari entri untuk `ratnakusuma+{runId}-079@qwertysystem.net` yang dibuat sesudah langkah 8 dimulai
14. Verifikasi Entri `Logged out` untuk `Ratna Kusuma` (dicari berdasarkan Note dan email) bertambah 1 dari baseline
15. Verifikasi Kredensial biometric `Ratna Kusuma` di server tetap Active
16. Hapus app dari recent apps
17. Buka kembali app
18. Verifikasi Screen "Sign in with biometrics" tampil
19. Verifikasi OS biometric prompt muncul otomatis

### TC-AUTH-SES-332: Logout manual di mobile oleh user tanpa biometric mengakhiri sesi dan menampilkan form Login

20. Bersihkan state app mobile dari TC sebelumnya di perangkat Android uji A (hapus data aplikasi, tutup dialog yang masih tampil), lalu buka aplikasi mobile di perangkat Android uji A, login sebagai `bambanglestari+{runId}-079@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD`, ketuk [Not now] bila Prompt Enable Biometric muncul, dan masuk Portal — Product Hub → halaman Portal — Product Hub tampil
21. Di Browser Admin buka `Global Settings > Activity Log > Session` dan catat baseline jumlah entri `Logged out` untuk `bambanglestari+{runId}-079@qwertysystem.net`
22. Di aplikasi mobile perangkat Android uji A buka menu Profile lalu pilih Log Out
23. Verifikasi Setelah logout form Login tampil
24. Verifikasi Sesi mobile `Bambang Lestari` berstatus Logged Out
25. Di Browser Admin muat ulang `Global Settings > Activity Log > Session` dan cari entri untuk `bambanglestari+{runId}-079@qwertysystem.net` yang dibuat sesudah langkah 22 dimulai
26. Verifikasi Entri `Logged out` untuk `Bambang Lestari` (dicari berdasarkan Note dan email) bertambah 1 dari baseline
27. Hapus app dari recent apps
28. Buka kembali app
29. Verifikasi Setelah app dibuka kembali form Login tampil
30. Verifikasi Screen biometric sign-in tidak tampil
31. Verifikasi Prompt "Enable Biometric" tidak tampil

### TC-AUTH-SES-333: Ganti akun di perangkat yang sama menghapus token biometric lokal user lama dan menawarkan Prompt Enable Biometric ke user baru

32. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
33. Ketik `citrahalim+{runId}-079@qwertysystem.net` pada field Email
34. Ketik `Spectra.env.SES_PASSWORD` pada field Password
35. Klik [Login] → Prompt Enable Biometric muncul
36. Ketuk [Enable] → OS biometric prompt muncul
37. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub dengan sesi mobile Active
38. Di aplikasi mobile perangkat Android uji B buka menu Profile lalu pilih Log Out → form Login tampil
39. Ketik `dodipratama+{runId}-079@qwertysystem.net` pada field Email
40. Ketik `Spectra.env.SES_PASSWORD` pada field Password
41. Klik [Login]
42. Verifikasi Setelah login `Dodi Pratama` Prompt "Enable biometric sign-in?" tampil
43. Ketuk [Not now] → app masuk Portal — Product Hub
44. Buka menu Profile lalu pilih Log Out → form Login tampil
45. Hapus app dari recent apps
46. Buka kembali app
47. Verifikasi Setelah app dibuka kembali form Login tampil
48. Verifikasi Screen biometric sign-in tidak tampil (token lokal, label email, dan status "sudah ditawari" milik `Citra Halim` sudah dihapus)
49. Verifikasi Kredensial biometric `Citra Halim` di server belum di-revoke (tetap Active) karena belum ada user lain yang enroll di perangkat itu

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pengelompokan: tiga TC logout manual di aplikasi mobile (dengan biometric, tanpa biometric, dan ganti akun sesudah logout) dengan harness yang sama (perangkat Android dan Browser Admin sebagai pengamat log); logout manual di web ada di spec `TC-AUTH-SES-E2E-043-manual-logout`.
- Urutan mengikuti TC sumber (331, 332, 333); tidak ada penyimpangan (S-10). Tiap TC memakai user sendiri.
- Dependensi (S-04): TC-AUTH-SES-331 bergantung pada TC-AUTH-SES-15 dan TC-AUTH-SES-333 pada TC-AUTH-SES-14; alur enroll (langkah 1–6 dan 32–37) disalin di tiap TC. Blok enroll berpola ini (Tabel Data Uji Pre-setup #29, tanpa mengakhiri sesi karena TC meminta sesi Active) dan prefix login mobile tidak dihitung ke batas sekitar 35 langkah.
- Pencatatan (S-12): Expected b TC-AUTH-SES-331 dan 332 ("dicatat `Logged out`, lihat TC-AUTH-SES-197") hanya diasersi kemunculan entri dengan baseline jumlah entri sebelum Log Out, mengikuti TC-AUTH-SES-140 di spec `TC-AUTH-SES-E2E-043-manual-logout`; kolom Activity, Status, dan Note diasersi TC-AUTH-SES-197 di spec pencatatan `TC-AUTH-SES-E2E-056`.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): hapus data aplikasi di awal tiap TC (status "sudah ditawari" dan token biometric lokal disimpan per perangkat); mencatat baseline dan memuat ulang log di Browser Admin; mengamati layar (langkah 9); Log Out `Citra Halim` dan `Dodi Pratama` (langkah 38 dan 44) serta [Not now] (langkah 43) sebagai bagian langkah TC; menghapus app dari recent apps lalu membukanya kembali.
- Jumlah langkah (49) melewati sekitar 35 karena tiga TC masing-masing menyalin prefix login dan blok enroll sendiri (S-04); di luar blok itu jumlah langkah di bawah batas.
- Temuan untuk QA: (1) TC-AUTH-SES-331 dan 332 Expected b menulis "dicatat `Logged out`" tanpa permukaan baca; spec membaca `Global Settings > Activity Log > Session` oleh akun Total Control (Global Settings) seperti TC-AUTH-SES-140. (2) Expected a dan c tentang status sesi Logged Out dan status kredensial biometric di server tidak menyebut cara membaca; spec memakai pembacaan dari backend yang disediakan tim FE/BE tanpa endpoint karangan (S-13). (3) TC-AUTH-SES-332 tidak menyebut perlakuan Prompt Enable Biometric saat login awal `Bambang Lestari` (profil BASE, perangkat Android uji A); spec mengetuk [Not now] bila prompt muncul (Pre-setup #28). (4) TC-AUTH-SES-333 langkah 4 menulis "Log Out" tanpa letak menu; spec memakai menu Profile lalu Log Out seperti langkah 1 TC yang sama. (5) TC sumber menulis "password yang benar" tanpa nilai; spec memakai `Spectra.env.SES_PASSWORD`.
