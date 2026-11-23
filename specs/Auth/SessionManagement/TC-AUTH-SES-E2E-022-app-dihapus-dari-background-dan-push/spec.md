---
id: TC-AUTH-SES-E2E-022-app-dihapus-dari-background-dan-push
title: "App Dihapus dari Background dan Notifikasi Push Setelah Sesi Berakhir"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-67
  - TC-AUTH-SES-68
  - TC-AUTH-SES-69
  - TC-AUTH-SES-317
  - TC-AUTH-SES-70
coverage:
  mobile: automated
---

# App Dihapus dari Background dan Notifikasi Push Setelah Sesi Berakhir

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) di perangkat Android uji A (TC-AUTH-SES-67, 69, 317, 70) dan perangkat Android uji B dengan biometric dan sidik jari terdaftar (TC-AUTH-SES-68), keduanya Tabel Data Uji Pre-setup #10.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): lima user milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5), user Activated, Active ON, MFA dan Agreement tidak terpicu, password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-67: `Agus Damayanti` (`agusdamayanti+{runId}-022@qwertysystem.net`), profil BASE
  - TC-AUTH-SES-68: `Rina Rahayu` (`rinarahayu+{runId}-022@qwertysystem.net`), profil BIO (Tabel Data Uji Pre-setup #9): belum pernah enroll biometric; enroll dilakukan di `## Test Steps` lewat login pertama di perangkat Android uji B dan Prompt Enable Biometric (Tabel Data Uji Pre-setup #29, alur TC-AUTH-SES-14)
  - TC-AUTH-SES-69: `Hendra Anggraini` (`hendraanggraini+{runId}-022@qwertysystem.net`), profil BASE; push token perangkat A terdaftar
  - TC-AUTH-SES-317: `Yoga Saputra` (`yogasaputra+{runId}-022@qwertysystem.net`), profil BASE; push token perangkat A terdaftar
  - TC-AUTH-SES-70: `Maya Wibowo` (`mayawibowo+{runId}-022@qwertysystem.net`), profil BASE; sesi-produk Fixed Asset anak yang Active (kondisi yang di-seed BE, terkait sesi mobile yang dibuat di langkah penghubung)
- Sesi mobile yang dibutuhkan TC tanpa langkah login di TC sumber (TC-AUTH-SES-317, 70) dibuat lewat langkah login pada awal TC di `## Test Steps`, karena token sesi mobile hanya ada di memori app dan hanya satu app yang aktif per perangkat. Sesi mobile TC-AUTH-SES-68 dibuat oleh login pertama yang sekaligus meng-enroll biometric.
- Hook `after`: kembalikan jam server uji dan jam browser/perangkat ke waktu nyata, akhiri semua sesi mobile yang dibuat spec, hentikan dan bersihkan aplikasi mobile pada perangkat A dan B, hapus kelima user. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile; tidak ada langkah ganti ke akun aktor.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: time-travel dan push notification):
  - driver otomasi Android (hapus app dari recent apps dengan swipe sehingga app dihentikan, buka kembali app, kirim app ke background);
  - pengatur waktu server uji (Tabel Data Uji Pre-setup #18) yang dapat memajukan dan memulihkan jam server per menit; jam server dan jam browser/perangkat diatur bersama;
  - pemicu notifikasi untuk user uji dari modul lain (mis. approval) dan penerimaan notifikasi push di perangkat A;
  - pembacaan status sesi mobile, sesi-produk (Active, Ended, Expired), seat, dan status push token dari BE;
  - simulasi OS biometric prompt pada perangkat B (TC-AUTH-SES-68), termasuk menyelesaikan prompt enroll dengan sidik jari terdaftar.
- Suite berjalan serial (`parallel: false`), juga karena perangkat Android uji A dan B dipakai bersama; state global yang diubah: jam server uji dan jam browser/perangkat (diatur bersama), dipulihkan di hook `after`.
- Menunggu waktu nyata tidak dipakai; jeda waktu dipenuhi dengan menggeser jam server dan jam browser/perangkat bersama.
- Fixture yang belum ada, disediakan tim FE/BE: pembacaan status sesi mobile, sesi-produk, seat, dan push token dari BE.

## Test Steps

### TC-AUTH-SES-67: App dihapus dari background lalu dibuka lagi tanpa sesi mengarah ke halaman Login

1. Buka aplikasi mobile di perangkat Android uji A, login sebagai `agusdamayanti+{runId}-022@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD` dan masuk Portal — Product Hub → halaman Portal — Product Hub tampil
2. Hapus app dari recent apps (swipe) sehingga app dihentikan
3. Buka kembali app
4. Verifikasi App menampilkan halaman Login (pengguna tanpa biometric enrolled) karena token sesi mobile hanya ada di memori app
5. Verifikasi Tidak ada Dialog Session Expired yang tampil

### TC-AUTH-SES-68: App dihapus dari background lalu dibuka lagi pada pengguna dengan biometric menampilkan Screen biometric sign-in

6. Buka aplikasi mobile di perangkat Android uji B (halaman Login tampil), login sebagai `rinarahayu+{runId}-022@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD` → Prompt Enable Biometric tampil
7. Ketuk [Enable] pada Prompt Enable Biometric dan selesaikan OS biometric prompt dengan sidik jari terdaftar → masuk Portal — Product Hub (biometric ter-enroll, user sedang login) → halaman Portal — Product Hub tampil
8. Hapus app dari recent apps di perangkat Android uji B
9. Buka kembali app
10. Verifikasi Screen "Sign in with biometrics" tampil menggantikan form Login
11. Verifikasi Body "Sign in as rinarahayu+{runId}-022@qwertysystem.net"

### TC-AUTH-SES-317: Notifikasi push tetap masuk setelah app dihapus dari background

12. Bersihkan state app mobile dari TC sebelumnya di perangkat Android uji A (logout atau bersihkan data app, tutup dialog yang masih tampil)
13. Buka aplikasi mobile di perangkat Android uji A, login sebagai `yogasaputra+{runId}-022@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD` dan masuk Portal — Product Hub (sesi mobile Active) → halaman Portal — Product Hub tampil
14. Hapus app dari recent apps
15. Picu satu notifikasi untuk `Yoga Saputra` dari modul lain (mis. approval)
16. Verifikasi Notifikasi push tetap diterima di perangkat tanpa filter
17. Verifikasi Push token tidak di-revoke

### TC-AUTH-SES-70: Login baru dari perangkat mobile yang sama setelah app dihapus menggantikan sesi lama tanpa Dialog Duplicate Login

18. Bersihkan state app mobile dari TC sebelumnya di perangkat Android uji A (logout atau bersihkan data app, tutup dialog yang masih tampil)
19. Buka aplikasi mobile di perangkat Android uji A, login sebagai `mayawibowo+{runId}-022@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD` dan masuk Portal — Product Hub (sesi mobile Active dengan sesi-produk Fixed Asset anak yang Active) → halaman Portal — Product Hub tampil
20. Hapus app dari recent apps
21. Majukan jam server uji dan jam browser/perangkat bersama 70 detik tanpa membuka app (heartbeat terakhir lebih dari 60 detik, sesi belum ditandai Expired oleh server)
22. Buka aplikasi mobile di perangkat Android uji A dan login sebagai `mayawibowo+{runId}-022@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD`
23. Verifikasi Halaman Portal — Product Hub tampil
24. Verifikasi Dialog "Duplicate Login Attempt" tidak tampil
25. Verifikasi Sesi lama dikenali sebagai sisa app-kill karena ID device sama dan tidak ada heartbeat lebih dari 60 detik
26. Verifikasi Sesi lama berstatus Expired
27. Verifikasi Sesi-produk anak dari sesi lama berakhir (Ended)
28. Verifikasi Seat sesi-produk anak dilepas

### TC-AUTH-SES-69: Notifikasi push tetap masuk setelah sesi mobile kedaluwarsa

29. Bersihkan state app mobile dari TC sebelumnya di perangkat Android uji A (logout atau bersihkan data app, tutup dialog yang masih tampil)
30. Buka aplikasi mobile di perangkat Android uji A, login sebagai `hendraanggraini+{runId}-022@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD` dan masuk Portal — Product Hub → halaman Portal — Product Hub tampil
31. Kirim app ke background (tombol Home)
32. Biarkan app di background tanpa aktivitas dan majukan jam server uji dan jam browser/perangkat bersama 16 menit sampai sesi Expired
33. Picu satu notifikasi untuk `Hendra Anggraini` dari modul lain (mis. approval)
34. Verifikasi Notifikasi push tetap diterima di perangkat tanpa filter atau subset
35. Verifikasi Push token tidak di-revoke saat sesi expired

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness d (push notification, time-travel).
- Penyimpangan urutan (S-05, S-10): urutan spec TC-AUTH-SES-67, 68, 317, 70, 69 (urutan TC sumber 67, 68, 69, 317, 70). TC-AUTH-SES-69 memajukan jam server 16 menit; ditaruh paling akhir supaya sesi sisa app-kill milik TC-AUTH-SES-70 tidak ditandai Expired oleh pergeseran jam sebelum TC itu berjalan. Tiap TC memakai user sendiri sehingga urutan tidak membuat TC saling bergantung.
- TC-AUTH-SES-68 berdependensi pada TC-AUTH-SES-15 (profil BIO sudah enroll biometric); prasyarat itu disiapkan lewat Pre-setup #29 (alur TC-AUTH-SES-14), disalin sebagai langkah 6 dan 7: login pertama di perangkat B, Prompt Enable Biometric [Enable], dan OS biometric prompt (S-04). Sesi mobile hasil login itu menjadi sesi "sedang login" yang dibutuhkan TC. TC-AUTH-SES-317 berdependensi pada TC-AUTH-SES-67; langkah menghapus app dari recent apps disalin sebagai langkah 14 (S-04).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): langkah login pada awal TC-AUTH-SES-317, 70 (membuat sesi aktif yang di TC sumber berupa precondition), langkah login dan enroll TC-AUTH-SES-68 (langkah 6 dan 7), langkah memajukan jam 70 detik pada TC-AUTH-SES-70 (menjadikan heartbeat terakhir lebih dari 60 detik), dan pembersihan state app mobile (logout atau bersihkan data app, tutup dialog) di awal TC-AUTH-SES-317, 70, 69 supaya login user berikutnya tidak terjadi di app yang masih berisi sesi user sebelumnya.
- Pencatatan log tidak diasersikan di spec ini (S-05).
- Temuan untuk QA: (1) TC-AUTH-SES-317 dan 70 tidak menyebut langkah login yang membuat sesi aktif (hanya precondition "sesi mobile aktif"); spec menambah langkah login sebagai langkah penghubung. (2) TC-AUTH-SES-70 precondition b tidak menyebut cara membuat sesi-produk Fixed Asset anak yang Active dari sesi mobile; spec mengandalkan kondisi yang di-seed BE tanpa endpoint, dan memajukan jam 70 detik untuk melewati batas 60 detik. (2b) TC-AUTH-SES-70 d dan TC-AUTH-SES-69 b serta 317 b tidak menyebut permukaan pembacaan status sesi, sesi-produk, seat, dan push token; spec memakai kemampuan BE yang disediakan tim FE/BE. (3) TC-AUTH-SES-69 dan 317 tidak menyebut cara memicu notifikasi dari modul lain dan cara memeriksa push token tidak di-revoke; kebutuhannya dicatat di Prerequisites. (4) TC-AUTH-SES-67, 68, 69, 317, 70 menulis "login sebagai <email>" tanpa menyebut password dan reCAPTCHA; spec memakai `Spectra.env.SES_PASSWORD`. (5) TC-AUTH-SES-68 Body menyebut `rinarahayu@qwertysystem.net`; spec memakai email bersuffix per run sesuai konvensi.
