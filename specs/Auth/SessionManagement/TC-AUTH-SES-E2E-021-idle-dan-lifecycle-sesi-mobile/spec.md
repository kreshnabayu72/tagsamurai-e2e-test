---
id: TC-AUTH-SES-E2E-021-idle-dan-lifecycle-sesi-mobile
title: "Idle Timeout dan Lifecycle Sesi Mobile: Foreground, Background, dan Biometric"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-63
  - TC-AUTH-SES-64
  - TC-AUTH-SES-65
  - TC-AUTH-SES-66
  - TC-AUTH-SES-71
  - TC-AUTH-SES-253
coverage:
  web: automated
  mobile: automated
---

# Idle Timeout dan Lifecycle Sesi Mobile: Foreground, Background, dan Biometric

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) di perangkat Android uji A (TC-AUTH-SES-63, 64, 65, 66, 71) dan perangkat Android uji B dengan biometric dan sidik jari terdaftar (TC-AUTH-SES-253), keduanya Tabel Data Uji Pre-setup #10. TC-AUTH-SES-71 juga memakai Browser A (Chrome on Windows).
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): enam user milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #11: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5), user Activated, Active ON, MFA dan Agreement tidak terpicu, password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-63: `Andi Utami` (`andiutami+{runId}-021@qwertysystem.net`), profil BASE
  - TC-AUTH-SES-64: `Dewi Puspita` (`dewipuspita+{runId}-021@qwertysystem.net`), profil BASE
  - TC-AUTH-SES-65: `Rizky Saputra` (`rizkysaputra+{runId}-021@qwertysystem.net`), profil BASE
  - TC-AUTH-SES-66: `Nur Firmansyah` (`nurfirmansyah+{runId}-021@qwertysystem.net`), profil BASE
  - TC-AUTH-SES-71: `Fajar Nugroho` (`fajarnugroho+{runId}-021@qwertysystem.net`), profil BASE
  - TC-AUTH-SES-253: `Wulan Setiawan` (`wulansetiawan+{runId}-021@qwertysystem.net`), profil BIO (Tabel Data Uji Pre-setup #9): belum pernah enroll biometric; enroll dilakukan di `## Test Steps` lewat login pertama di perangkat Android uji B dan Prompt Enable Biometric (Tabel Data Uji Pre-setup #29, alur TC-AUTH-SES-14)
- Sesi mobile dan sesi web yang dibutuhkan TC dibuat lewat langkah login di `## Test Steps` pada awal tiap TC, bukan di hook `before`: akumulasi pergeseran jam dari TC sebelumnya akan membuat sesi yang di-seed di awal sudah melewati batas idle 15 menit.
- Hook `after`: kembalikan jam server uji dan jam browser/perangkat ke waktu nyata, akhiri semua sesi mobile dan web yang dibuat spec, hentikan dan bersihkan aplikasi mobile pada perangkat A dan B, hapus keenam user. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile (dan Browser A untuk TC-AUTH-SES-71); tidak ada langkah ganti ke akun aktor.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: time-travel dan heartbeat):
  - driver otomasi Android (ketuk layar, kirim app ke background dengan tombol Home, buka kembali app, kembali ke foreground);
  - pengatur waktu server uji (Tabel Data Uji Pre-setup #18) yang dapat memajukan dan memulihkan jam server per menit, dengan jam browser/perangkat diatur bersama jam server;
  - proxy jaringan pada perangkat A untuk memantau request heartbeat (TC-AUTH-SES-64);
  - pembacaan status sesi mobile dan sesi web (Active atau Expired) dari BE;
  - simulasi OS biometric prompt pada perangkat B (TC-AUTH-SES-253), termasuk menyelesaikan prompt enroll dengan sidik jari terdaftar;
  - reCAPTCHA mode uji di environment untuk login web di Browser A (TC-AUTH-SES-71).
- Suite berjalan serial (`parallel: false`), juga karena perangkat Android uji A dan B dipakai bersama; state global yang diubah: jam server uji dan jam browser/perangkat (diatur bersama), dipulihkan di hook `after`.
- Menunggu waktu nyata tidak dipakai; semua jeda waktu dipenuhi dengan menggeser jam server dan jam browser/perangkat bersama.

## Test Steps

### TC-AUTH-SES-66: App di-minimize kurang dari batas idle tetap memiliki sesi aktif

1. Buka aplikasi mobile di perangkat Android uji A, login sebagai `nurfirmansyah+{runId}-021@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD` dan masuk Portal — Product Hub → halaman Portal — Product Hub tampil
2. Kirim app ke background (tidak dihapus dari recent apps)
3. Majukan jam server uji dan jam browser/perangkat bersama 3 menit
4. Buka kembali app
5. Verifikasi App kembali ke halaman terakhir tanpa Login
6. Verifikasi Sesi mobile tetap Active (bukan logout)

### TC-AUTH-SES-64: Sentuhan layar mereset timer idle mobile dan heartbeat hanya dikirim saat foreground

7. Bersihkan state app mobile dari TC sebelumnya di perangkat Android uji A (logout atau bersihkan data app, tutup dialog yang masih tampil)
8. Buka aplikasi mobile di perangkat Android uji A, login sebagai `dewipuspita+{runId}-021@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD` dan masuk Portal — Product Hub → halaman Portal — Product Hub tampil
9. Majukan jam server uji dan jam browser/perangkat bersama 12 menit tanpa sentuhan
10. Ketuk layar dan amati request heartbeat pada proxy jaringan perangkat
11. Verifikasi Sentuhan layar mengirim heartbeat
12. Verifikasi Waktu kedaluwarsa dihitung ulang (aktivitas terakhir + 15 menit)
13. Kirim app ke background
14. Majukan jam server uji dan jam browser/perangkat bersama 2 menit lalu amati request pada proxy jaringan perangkat selama rentang itu
15. Verifikasi Selama app di background tidak ada heartbeat yang dikirim

### TC-AUTH-SES-65: App di background saat batas idle terlewati menampilkan Dialog Session Expired setelah kembali ke foreground

16. Bersihkan state app mobile dari TC sebelumnya di perangkat Android uji A (logout atau bersihkan data app, tutup dialog yang masih tampil)
17. Buka aplikasi mobile di perangkat Android uji A, login sebagai `rizkysaputra+{runId}-021@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD` dan masuk Portal — Product Hub → halaman Portal — Product Hub tampil
18. Kirim app ke background (tekan tombol Home)
19. Majukan jam server uji dan jam browser/perangkat bersama 16 menit
20. Verifikasi Selama di background tidak ada toast
21. Buka kembali app (foreground) → Dialog Session Expired muncul
22. Verifikasi Dialog "Session Expired" tampil dengan Body "Your session has expired due to inactivity."
23. Verifikasi Dialog memuat tombol [OK]
24. Verifikasi Timer idle server tidak dijeda selama app di background (sesi mobile berstatus Expired)

### TC-AUTH-SES-63: Idle mobile sampai batas memunculkan Dialog Session Expired dan OK mengarah ke Login

25. Bersihkan state app mobile dari TC sebelumnya di perangkat Android uji A (logout atau bersihkan data app, tutup dialog yang masih tampil)
26. Buka aplikasi mobile di perangkat Android uji A, login sebagai `andiutami+{runId}-021@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD` dan masuk Portal — Product Hub → halaman Portal — Product Hub tampil
27. Biarkan app di foreground tanpa sentuhan dan majukan jam server uji dan jam browser/perangkat bersama 16 menit
28. Ketuk layar → Dialog Session Expired muncul
29. Verifikasi Dialog "Session Expired" tampil dengan Body "Your session has expired due to inactivity."
30. Verifikasi Dialog memuat satu tombol [OK]
31. Ketuk [OK]
32. Verifikasi App diarahkan ke halaman Login (pengguna tanpa biometric enrolled)
33. Verifikasi Sesi mobile berstatus Expired

### TC-AUTH-SES-71: Idle tracking web dan mobile dihitung terpisah per sesi platform

34. Di Browser A (Chrome on Windows) buka halaman `Auth > Login with Password`, login dengan email `fajarnugroho+{runId}-021@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD` → Portal — Product Hub tampil
35. Bersihkan state app mobile dari TC sebelumnya di perangkat Android uji A (logout atau bersihkan data app, tutup dialog yang masih tampil)
36. Buka aplikasi mobile di perangkat Android uji A, login sebagai `fajarnugroho+{runId}-021@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD` dan masuk Portal — Product Hub → halaman Portal — Product Hub tampil
37. Majukan jam server uji dan jam browser/perangkat bersama 5 menit
38. Gerakkan mouse di Browser A
39. Majukan jam server uji dan jam browser/perangkat bersama 5 menit lagi
40. Gerakkan mouse di Browser A
41. Majukan jam server uji dan jam browser/perangkat bersama 4 menit lagi (total 14 menit) tanpa menyentuh app mobile
42. Majukan jam server uji dan jam browser/perangkat bersama 2 menit lagi tanpa aktivitas
43. Amati Browser A dan perangkat mobile
44. Ketuk layar app mobile di perangkat Android uji A → Dialog Session Expired muncul
45. Verifikasi Sesi mobile berstatus Expired
46. Verifikasi App menampilkan Dialog Session Expired saat disentuh
47. Verifikasi Sesi web di Browser A tetap Active karena aktivitas web tidak memperpanjang sesi mobile dan sebaliknya

### TC-AUTH-SES-253: Idle mobile pada pengguna dengan biometric: OK pada Dialog Session Expired membuka Screen biometric sign-in

48. Buka aplikasi mobile di perangkat Android uji B (halaman Login tampil), login sebagai `wulansetiawan+{runId}-021@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD` → Prompt Enable Biometric tampil
49. Ketuk [Enable] pada Prompt Enable Biometric dan selesaikan OS biometric prompt dengan sidik jari terdaftar → masuk Portal — Product Hub (biometric ter-enroll, sesi mobile Active di foreground) → halaman Portal — Product Hub tampil
50. Biarkan aplikasi di foreground tanpa sentuhan dan majukan jam server uji dan jam browser/perangkat bersama 16 menit
51. Ketuk layar → Dialog Session Expired muncul
52. Verifikasi Dialog "Session Expired" tampil dengan Body "Your session has expired due to inactivity."
53. Verifikasi Dialog memuat satu tombol [OK]
54. Ketuk [OK]
55. Verifikasi Screen "Sign in with biometrics" tampil menggantikan form Login
56. Verifikasi OS biometric prompt muncul otomatis

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness d (time-travel dan heartbeat); spec memuat enam TC karena satu kelas harness dan satu platform.
- Penyimpangan urutan (S-05, S-10): urutan spec TC-AUTH-SES-66, 64, 65, 63, 71, 253 (urutan TC sumber 63, 64, 65, 66, 71, 253). TC tanpa pergeseran jam besar (66) dan TC pengamatan heartbeat (64) ditaruh di depan, TC dengan pergeseran 16 menit sesudahnya. Jam tidak dipulihkan antar-TC (spec ini tidak membuka Activity Log atau User Log), jadi tiap TC membuat sesinya sendiri lewat langkah login pada awal TC sehingga pergeseran kumulatif tidak mengubah hasil.
- TC-AUTH-SES-66 menulis "Tunggu 3 menit"; spec menuliskannya "Majukan jam server uji dan jam browser/perangkat bersama 3 menit" supaya satu mekanisme waktu dipakai di seluruh spec. TC-AUTH-SES-64 langkah 4 ("amati request selama 2 menit") dipenuhi dengan memajukan jam server dan jam perangkat bersama 2 menit; yang diamati adalah ketiadaan request heartbeat dari klien pada rentang itu.
- TC-AUTH-SES-253 berdependensi pada TC-AUTH-SES-15 (profil BIO sudah enroll biometric di perangkat B); prasyarat itu disiapkan lewat Pre-setup #29 (alur TC-AUTH-SES-14), disalin sebagai langkah 48 dan 49: login pertama di perangkat B, Prompt Enable Biometric [Enable], dan OS biometric prompt (S-04). Sesi mobile hasil login itu menjadi sesi Active di foreground yang dibutuhkan TC. Layar biometric sign-in saat app dibuka tanpa sesi diuji di spec lain.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah login dan enroll pada awal TC-AUTH-SES-253 (langkah 48 dan 49) dan langkah login pada TC-AUTH-SES-71 (membuat sesi aktif yang di TC sumber berupa precondition), langkah "Amati ..." (langkah 10, 14, 43), dan pergerakan mouse pada TC-AUTH-SES-71.
- Langkah penghubung S-03 tambahan: pembersihan state app mobile antar-TC (logout atau bersihkan data app, tutup dialog) di awal TC-AUTH-SES-64, 65, 63 dan sebelum login mobile TC-AUTH-SES-71, supaya login user berikutnya tidak terjadi di app yang masih berisi sesi user sebelumnya.
- Pencatatan `Session expired` ke Activity Log tidak diasersikan di spec ini; pencatatan diuji di spec log, asersi absence di spec absence (S-05).
- Ukuran spec melewati sekitar 35 langkah (56 langkah): tiap TC memakai user dan sesi sendiri lewat langkah login di awal TC, sehingga TC sesudahnya tetap bermakna bila TC sebelumnya gagal. Kelas harness tunggal (d).
- Temuan untuk QA: (1) TC-AUTH-SES-63, 64, 65, 66, 71, 253 tidak menyebut cara membaca status sesi mobile atau web (Active atau Expired); spec mengandalkan pembacaan status dari BE dan kebutuhannya dicatat di Prerequisites. (2) TC-AUTH-SES-71 langkah 1 "tiap 5 menit" selama 14 menit tidak menyebut apakah ada gerakan mouse pada menit ke-14; spec menggerakkan mouse pada menit ke-5 dan ke-10 saja. (3) TC-AUTH-SES-253 tidak menyebut langkah login sebelum idle (precondition "sesi mobile Active di foreground"); spec memakai login pertama di perangkat B beserta enroll biometric sesuai Pre-setup #29 sebagai langkah penghubung. (4) TC-AUTH-SES-63, 64, 65, 66, 71 menulis "login sebagai <email> " tanpa menyebut password dan reCAPTCHA; spec memakai `Spectra.env.SES_PASSWORD`; kemampuan reCAPTCHA mode uji untuk login web di Browser A dicatat di Prerequisites, tanpa langkah reCAPTCHA.
