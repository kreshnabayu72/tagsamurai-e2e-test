---
id: TC-AUTH-SES-E2E-082-kembali-ke-foreground-setelah-sesi-diakhiri-server
title: "Kembali ke Foreground Setelah Sesi Diakhiri Server Saat App di Background"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-341
  - TC-AUTH-SES-342
  - TC-AUTH-SES-343
coverage:
  web: automated
  mobile: automated
---

# Kembali ke Foreground Setelah Sesi Diakhiri Server Saat App di Background

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) terpasang di perangkat Android uji A (ketiga TC) dan perangkat Android uji E (TC-AUTH-SES-342) (Tabel Data Uji Pre-setup #10). Tanpa sesi aktif di aplikasi pada kedua perangkat saat spec dimulai.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, Tabel Data Uji Pre-setup #1, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu) dengan App Access Fixed Asset, password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-341: `Vina Anggraeni` (`vinaanggraeni+{runId}-082@qwertysystem.net`)
  - TC-AUTH-SES-342: `Wahyu Nugraha` (`wahyunugraha+{runId}-082@qwertysystem.net`)
  - TC-AUTH-SES-343: `Yudistira Kamal` (`yudistirakamal+{runId}-082@qwertysystem.net`); sesi platform web Active di Browser A (Chrome on Windows), dibuat di `before` lewat login API
- Sesi mobile tiap TC dibuat lewat login nyata di perangkat Android uji A dan ketuk [Not now] bila Prompt Enable Biometric muncul (Tabel Data Uji Pre-setup #28), sebagai langkah di awal bagian TC.
- Browser License (login di hook `before`): Admin License `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #2, Global Role Manage Global License), kredensial `Spectra.env.FA_MGL_PASSWORD`, membuka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) pada TC-AUTH-SES-341.
- Password: password lama user uji `Spectra.env.SES_PASSWORD`; password baru hasil Change Password `Spectra.env.SES_PASSWORD_NEW` (TC-AUTH-SES-343). Nilai password lama dan baru yang ditulis TC-AUTH-SES-343 diisikan lewat kedua environment variable itu, tidak ditulis literal di spec.
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server uji dan jam browser/perangkat (dimajukan bersama pada TC-AUTH-SES-341), perangkat Android uji A dan E yang dipakai bersama, pemantauan proxy jaringan. Jam dipulihkan ke waktu nyata lewat langkah eksplisit dan di hook `after`.
- Hook `after`: pulihkan jam server dan jam browser/perangkat ke waktu nyata; hentikan pemantauan proxy; hapus data aplikasi pada perangkat Android uji A dan E; akhiri semua sesi seed dan sesi-produk; tutup Browser A dan Browser License; hapus ketiga user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile dan Browser A; Admin License pada Browser License; akun aktor Total Control hanya di hook dan untuk pembacaan status sesi dari backend.
- Environment variable: `GS_TC_PASSWORD`, `FA_MGL_PASSWORD`, `SES_PASSWORD`, `SES_PASSWORD_NEW`. Password tidak ditulis di spec atau fixture.
- Menunggu waktu nyata tidak dipakai; jeda dipenuhi dengan menggeser jam server dan jam browser/perangkat bersama.
- Kemampuan teknis (kelas harness c: multi-perangkat; sesi perangkat Android uji E diasersi pada TC-AUTH-SES-342): driver otomasi Android (aplikasi native) pada perangkat A dan E (kirim app ke background tanpa menghapusnya dari recent apps, buka kembali dari recent apps, membaca area notifikasi); proxy jaringan (Tabel Data Uji Pre-setup #18) yang mencatat request perangkat Android uji A untuk menghitung request cek sesi sebelum konten terlindungi tampil; jam server uji dan jam browser/perangkat yang dimajukan bersama dan dipulihkan ke waktu nyata (Tabel Data Uji Pre-setup #18); konteks browser bersamaan (Browser A, Browser License); pembacaan status sesi user dari backend, disediakan tim FE/BE.

## Test Steps

### TC-AUTH-SES-341: Force-logout admin selama app di background menampilkan Dialog Log Out saat app kembali ke foreground

1. Bersihkan state app mobile di perangkat Android uji A (hapus data aplikasi, tutup dialog yang masih tampil), lalu buka aplikasi mobile di perangkat Android uji A, login sebagai `vinaanggraeni+{runId}-082@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD`, ketuk [Not now] bila Prompt Enable Biometric muncul, dan masuk Portal — Product Hub → halaman Portal — Product Hub tampil
2. Di aplikasi mobile ketuk card Fixed Asset → Fixed Asset tampil (sesi-produk Fixed Asset Active, seat terpakai)
3. Mulai pemantauan request perangkat Android uji A di proxy jaringan
4. Kirim app ke background (tidak dihapus dari recent apps)
5. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset), pilih `Vina Anggraeni`, lalu klik [Force Logout] → dialog konfirmasi "Force Logout User" muncul
6. Klik [Confirm Logout]
7. Majukan jam server uji dan jam browser/perangkat bersama 1 menit dengan app tetap di background, lalu amati layar dan area notifikasi perangkat Android uji A
8. Verifikasi Selama app di background tidak ada dialog tentang force-logout
9. Verifikasi Selama app di background tidak ada notifikasi push tentang force-logout
10. Buka kembali app dari recent apps
11. Verifikasi Saat kembali ke foreground app mengecek sesi ke server satu kali sebelum konten terlindungi tampil (proxy mencatat tepat satu request cek sesi sebelum konten terlindungi dimuat)
12. Verifikasi Dialog "Log Out" tampil
13. Verifikasi Body Dialog "Log Out": "You have been logged out by an administrator."
14. Ketuk [OK]
15. Verifikasi Setelah [OK] form Login tampil
16. Pulihkan jam server uji dan jam browser/perangkat ke waktu nyata

### TC-AUTH-SES-342: Duplicate Login yang dikonfirmasi selama app di background menampilkan Dialog Logged Out saat app kembali ke foreground

17. Bersihkan state app mobile di perangkat Android uji A (hapus data aplikasi, tutup dialog yang masih tampil), lalu buka aplikasi mobile di perangkat Android uji A, login sebagai `wahyunugraha+{runId}-082@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD`, ketuk [Not now] bila Prompt Enable Biometric muncul, dan masuk Portal — Product Hub → halaman Portal — Product Hub tampil
18. Hapus data aplikasi di perangkat Android uji E (perangkat belum login)
19. Catat titik awal pemantauan request perangkat Android uji A di proxy jaringan
20. Di perangkat Android uji A kirim app ke background (tidak dihapus dari recent apps)
21. Buka aplikasi mobile di perangkat Android uji E → halaman Login tampil
22. Ketik `wahyunugraha+{runId}-082@qwertysystem.net` pada field Email
23. Ketik `Spectra.env.SES_PASSWORD` pada field Password
24. Klik [Login] → Dialog Duplicate Login Attempt muncul
25. Ketuk [Confirm] pada Dialog Duplicate Login Attempt, lalu ketuk [Not now] bila Prompt Enable Biometric muncul
26. Amati layar dan area notifikasi perangkat Android uji A dengan app tetap di background
27. Verifikasi Selama app di background tidak ada dialog tentang sesi
28. Verifikasi Selama app di background tidak ada notifikasi push tentang sesi
29. Di perangkat Android uji A buka kembali app dari recent apps
30. Verifikasi Saat kembali ke foreground app mengecek sesi ke server satu kali sebelum konten terlindungi tampil (proxy mencatat tepat satu request cek sesi sebelum konten terlindungi dimuat)
31. Verifikasi Dialog "Logged Out" tampil
32. Verifikasi Body Dialog "Logged Out": "You have been logged out because another session was started on a different device."
33. Ketuk [OK]
34. Verifikasi Setelah [OK] form Login tampil di perangkat Android uji A
35. Verifikasi Sesi `Wahyu Nugraha` di perangkat Android uji E tetap Active

### TC-AUTH-SES-343: Password diganti selama app di background menampilkan Dialog Password Changed saat app kembali ke foreground

36. Bersihkan state app mobile di perangkat Android uji A (hapus data aplikasi, tutup dialog yang masih tampil), lalu buka aplikasi mobile di perangkat Android uji A, login sebagai `yudistirakamal+{runId}-082@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD`, ketuk [Not now] bila Prompt Enable Biometric muncul, dan masuk Portal — Product Hub → halaman Portal — Product Hub tampil
37. Catat titik awal pemantauan request perangkat Android uji A di proxy jaringan
38. Di perangkat Android uji A kirim app ke background (tidak dihapus dari recent apps)
39. Di Browser A (sesi web Active `Yudistira Kamal`) buka `Global Settings > My Profile > Change Password` → modal Change Password tampil
40. Ketik `Spectra.env.SES_PASSWORD` pada field Current Password
41. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field New Password
42. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field Confirm New Password
43. Klik [Save] → password berhasil diubah
44. Di perangkat Android uji A buka kembali app dari recent apps
45. Verifikasi Saat kembali ke foreground app mengecek sesi ke server satu kali sebelum konten terlindungi tampil (proxy mencatat tepat satu request cek sesi sebelum konten terlindungi dimuat)
46. Verifikasi Dialog "Password Changed" tampil
47. Verifikasi Body Dialog "Password Changed": "Your password has been changed. Please log in again."
48. Ketuk [OK]
49. Verifikasi Setelah [OK] form Login tampil

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pengelompokan: tiga TC "sesi diakhiri server selama app di background, lalu app kembali ke foreground" dengan harness yang sama (perangkat Android uji A dengan proxy pengamat dan konteks pemicu lain). Kelas harness c karena TC-AUTH-SES-342 mengasersi sesi di perangkat Android uji E; pada TC-AUTH-SES-341 dan 343 Browser License dan Browser A hanya pemicu (P-2).
- Pemantauan proxy bersifat pengamat (P-6) untuk menghitung request cek sesi; pergeseran jam 1 menit pada TC-AUTH-SES-341 hanya jeda pengamatan, bukan objek uji (P-2).
- Urutan mengikuti TC sumber (341, 342, 343); tidak ada penyimpangan (S-10). Tiap TC memakai user sendiri.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): login mobile di awal tiap TC (Pre-setup #28); membuka card Fixed Asset (langkah 2) untuk membentuk sesi-produk yang dapat di-force-logout; memulai atau mencatat titik awal pemantauan proxy; menghapus data aplikasi perangkat E (langkah 18); aksi pemicu di Browser License, perangkat E, dan Browser A; mengamati layar dan area notifikasi; memajukan dan memulihkan jam.
- Pencatatan log tidak diasersikan di spec ini; pencatatan force-logout, Duplicate Login, dan password changed diuji di spec pencatatan modul ini (S-05).
- Jumlah langkah (49) melewati batas sekitar 35 langkah karena tiga TC masing-masing menyalin prefix login mobile sendiri (langkah 1, 17, 36) dan TC-AUTH-SES-342 serta 343 menyalin langkah pemicu di perangkat atau browser kedua (login perangkat E, form Change Password); tiap TC berdiri sendiri.
- Temuan untuk QA: (1) TC-AUTH-SES-341 langkah 3 "Tunggu 1 menit" tidak menyebut tujuannya (jeda pengamatan push atau batas waktu tertentu); spec memenuhinya dengan memajukan jam server dan jam perangkat bersama 1 menit sebagai jeda pengamatan. (2) TC-AUTH-SES-341 dan 342 Expected a "tidak ada notifikasi push" tidak menyebut permukaan amatan; spec membaca area notifikasi perangkat. (3) TC-AUTH-SES-342 tidak menyebut perlakuan Prompt Enable Biometric sesudah [Confirm] di perangkat E (perangkat E ber-hardware biometric); spec mengetuk [Not now] bila prompt muncul. (4) TC-AUTH-SES-342 Expected d "sesi di perangkat E tetap Active" dan status sesi tidak menyebut cara membaca; spec memakai pembacaan dari backend yang disediakan tim FE/BE (S-13).
