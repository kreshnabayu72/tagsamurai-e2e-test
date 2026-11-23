---
id: TC-AUTH-SES-E2E-084-os-kill-app-mobile-dan-sesi-tanpa-cookie
title: "OS Kill App Mobile di Background Diperlakukan sebagai App-kill dan Sesi Mobile Tanpa Cookie"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-SES-345
  - TC-AUTH-SES-346
  - TC-AUTH-SES-349
coverage:
  mobile: automated
---

# OS Kill App Mobile di Background Diperlakukan sebagai App-kill dan Sesi Mobile Tanpa Cookie

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) terpasang di perangkat Android uji A (TC-AUTH-SES-345 dan 349) dan perangkat Android uji B (TC-AUTH-SES-346: hardware biometric dan sidik jari terdaftar di OS) (Tabel Data Uji Pre-setup #10). Tanpa sesi aktif di aplikasi pada kedua perangkat saat spec dimulai.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, Tabel Data Uji Pre-setup #1, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga user milik Client `Alpha Logistik` (batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-345: `Agus Setiadi` (`agussetiadi+{runId}-084@qwertysystem.net`), profil BASE (Tabel Data Uji Pre-setup #5)
  - TC-AUTH-SES-346: `Bella Novita` (`bellanovita+{runId}-084@qwertysystem.net`), profil BIO (Tabel Data Uji Pre-setup #9), belum pernah enroll biometric
  - TC-AUTH-SES-349: `Feri Irawan` (`feriirawan+{runId}-084@qwertysystem.net`), profil BASE (Tabel Data Uji Pre-setup #5)
- Sesi mobile TC-AUTH-SES-345 dibuat lewat login nyata di perangkat Android uji A dan ketuk [Not now] bila Prompt Enable Biometric muncul (Tabel Data Uji Pre-setup #28), sebagai langkah di awal bagian TC. Kondisi "sudah enroll biometric di perangkat Android uji B dengan sesi mobile Active" pada TC-AUTH-SES-346 dibuat sebagai langkah dengan alur Prompt Enable Biometric (login, [Enable], lulus verifikasi sidik jari; TC-AUTH-SES-14 dan 15; Tabel Data Uji Pre-setup #29) dengan data aplikasi yang bersih; sesi hasil login enroll dibiarkan Active.
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server uji dan jam browser/perangkat (dimajukan bersama pada TC-AUTH-SES-345 dan 346 dan dipulihkan ke waktu nyata di akhir bagiannya), proses app di perangkat Android uji A dan B, data aplikasi dan token biometric lokal di perangkat Android uji B, pemantauan proxy jaringan.
- Hook `after`: pulihkan jam server dan jam browser/perangkat ke waktu nyata; hentikan pemantauan proxy; hapus data aplikasi pada perangkat Android uji A dan B; akhiri semua sesi seed; hapus ketiga user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile; akun aktor Total Control hanya di hook dan untuk pembacaan status sesi dari backend.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture; nilai password yang ditulis TC-AUTH-SES-349 diisikan lewat `SES_PASSWORD`.
- Menunggu waktu nyata tidak dipakai; jeda dipenuhi dengan menggeser jam server dan jam browser/perangkat bersama.
- Kemampuan teknis (kelas harness d: hardware biometrik pada TC-AUTH-SES-346): driver otomasi Android (aplikasi native) pada perangkat A dan B (kirim app ke background tanpa menghapusnya dari recent apps, buka kembali dari recent apps); ADB terhubung ke perangkat Android uji A dan B (Tabel Data Uji Pre-setup #18) untuk menjalankan `adb shell am kill <package app>`; simulasi sensor sidik jari pada OS biometric prompt Android (verifikasi lulus); proxy jaringan (Tabel Data Uji Pre-setup #18) yang mencatat request perangkat dan membaca token sesi pada respons login serta header request terautentikasi (termasuk header `Cookie`); jam server uji dan jam browser/perangkat yang dimajukan bersama dan dipulihkan ke waktu nyata (Tabel Data Uji Pre-setup #18); pembacaan status sesi user dari backend oleh akun aktor, disediakan tim FE/BE.

## Test Steps

### TC-AUTH-SES-345: OS kill saat app di background tanpa tindakan user diperlakukan sebagai app-kill dan membuka form Login

1. Bersihkan state app mobile di perangkat Android uji A (hapus data aplikasi, tutup dialog yang masih tampil), lalu buka aplikasi mobile di perangkat Android uji A, login sebagai `agussetiadi+{runId}-084@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD`, ketuk [Not now] bila Prompt Enable Biometric muncul, dan masuk Portal — Product Hub → halaman Portal — Product Hub tampil
2. Catat token sesi `Agus Setiadi` yang sedang dipakai app dan titik awal pemantauan request perangkat Android uji A di proxy jaringan
3. Kirim app ke background (tidak dihapus dari recent apps)
4. Jalankan `adb shell am kill <package app>` untuk membunuh proses app di background
5. Buka kembali app dari recent apps
6. Verifikasi Setelah app dibuka kembali form Login tampil
7. Verifikasi Halaman terakhir (Portal — Product Hub) tidak tampil
8. Verifikasi Sesudah app dibuka kembali tidak ada request yang membawa token sesi yang dicatat pada langkah 2
9. Majukan jam server uji dan jam browser/perangkat bersama 15 menit (melewati batas idle)
10. Verifikasi Sesi lama `Agus Setiadi` berstatus Expired
11. Pulihkan jam server uji dan jam browser/perangkat ke waktu nyata

### TC-AUTH-SES-346: OS kill saat app di background tanpa tindakan user diperlakukan sebagai app-kill dan membuka Screen biometric sign-in

12. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
13. Ketik `bellanovita+{runId}-084@qwertysystem.net` pada field Email
14. Ketik `Spectra.env.SES_PASSWORD` pada field Password
15. Klik [Login] → Prompt Enable Biometric muncul
16. Ketuk [Enable] → OS biometric prompt muncul
17. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub dengan sesi mobile Active
18. Catat token sesi `Bella Novita` yang sedang dipakai app dan titik awal pemantauan request perangkat Android uji B di proxy jaringan
19. Kirim app ke background (tidak dihapus dari recent apps)
20. Jalankan `adb shell am kill <package app>` untuk membunuh proses app di background
21. Buka kembali app dari recent apps
22. Verifikasi Setelah app dibuka kembali Screen "Sign in with biometrics" tampil
23. Verifikasi OS biometric prompt muncul otomatis
24. Verifikasi Halaman terakhir (Portal — Product Hub) tidak tampil
25. Verifikasi Sesudah app dibuka kembali tidak ada request yang membawa token sesi yang dicatat pada langkah 18
26. Majukan jam server uji dan jam browser/perangkat bersama 15 menit (melewati batas idle) tanpa melewati OS biometric prompt
27. Verifikasi Sesi lama `Bella Novita` berstatus Expired
28. Pulihkan jam server uji dan jam browser/perangkat ke waktu nyata

### TC-AUTH-SES-349: Sesi mobile tidak memakai cookie sehingga app yang dibunuh tidak membawa sesi lama

29. Hapus data aplikasi di perangkat Android uji A lalu buka aplikasi mobile → halaman Login tampil
30. Mulai pemantauan request perangkat Android uji A di proxy jaringan
31. Ketik `feriirawan+{runId}-084@qwertysystem.net` pada field Email
32. Ketik `Spectra.env.SES_PASSWORD` pada field Password
33. Klik [Login], lalu ketuk [Not now] bila Prompt Enable Biometric muncul → halaman Portal — Product Hub tampil
34. Buka Settings > Security lalu amati header request terautentikasi di proxy
35. Verifikasi Request terautentikasi membawa token sesi dari respons login
36. Verifikasi Request terautentikasi tidak membawa header `Cookie` berisi sesi
37. Kirim app ke background (tidak dihapus dari recent apps)
38. Jalankan `adb shell am kill <package app>` untuk membunuh proses app di background
39. Buka kembali app dari recent apps lalu amati request di proxy
40. Verifikasi Setelah app dibuka kembali tidak ada request yang membawa sesi lama
41. Verifikasi Form Login tampil

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pengelompokan: tiga TC "proses app dibunuh OS lewat `adb shell am kill` lalu app dibuka kembali" dengan harness yang sama (driver Android, ADB, proxy pengamat). caseType Edge mengikuti dua TC dominan (TC-AUTH-SES-345 dan 346 Edge Case; TC-AUTH-SES-349 Security dipetakan Negative). Kelas harness d karena TC-AUTH-SES-346 membutuhkan hardware biometrik, sama dengan spec `TC-AUTH-SES-E2E-079-logout-manual-mobile-dan-ganti-akun`.
- Pemantauan proxy hanya pengamat (P-6). Pergeseran jam 15 menit pada TC-AUTH-SES-345 dan 346 hanya menghabiskan batas idle agar status lazy expire dapat dibaca; batas idle bukan objek uji, sehingga tidak memecah spec ke kelas d TTL (P-2).
- Urutan mengikuti TC sumber (345, 346, 349); tidak ada penyimpangan (S-10). Tiap TC memakai user sendiri.
- Dependensi (S-04): TC-AUTH-SES-346 bergantung pada TC-AUTH-SES-15 (enroll biometric); langkah 12–17 menyalin blok enroll. Prefix login (langkah 1, 29–33) dan blok enroll tidak dihitung ke batas sekitar 35 langkah.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): login mobile dan blok enroll; mencatat token sesi dan titik awal pemantauan proxy (langkah 2 dan 18, pembanding S-14); memulai pemantauan proxy (langkah 30); kirim app ke background, `adb shell am kill`, dan membuka kembali app; membuka Settings > Security (langkah 34); memajukan dan memulihkan jam.
- Pencatatan log tidak diasersikan di spec ini (S-05).
- Temuan untuk QA: (1) Expected b TC-AUTH-SES-345 dan 346 "sesi lama di-expire server secara lazy saat request berikutnya dari sesi itu atau saat idle timeout terlampaui" tidak menyebut pemicu yang dipakai untuk mengamati status Expired; spec memilih jalur idle timeout (jam dimajukan 15 menit) dan membaca status dari backend yang disediakan tim FE/BE (S-13), karena jalur "request berikutnya dari sesi itu" butuh pengiriman token lama lewat alat uji (kelas a). (2) TC-AUTH-SES-349 langkah 2 "buka satu halaman di Portal" tidak menyebut halaman; spec memakai Settings > Security. (3) TC-AUTH-SES-349 tidak menyebut perlakuan Prompt Enable Biometric sesudah login di perangkat Android uji A; spec mengetuk [Not now] bila prompt muncul.
