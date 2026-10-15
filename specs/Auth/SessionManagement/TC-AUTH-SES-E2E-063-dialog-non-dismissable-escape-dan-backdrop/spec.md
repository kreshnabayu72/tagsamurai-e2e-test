---
id: TC-AUTH-SES-E2E-063-dialog-non-dismissable-escape-dan-backdrop
title: "Dialog Lifecycle Non-dismissable: Escape, Klik Backdrop, dan Tombol Silang"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-224
  - TC-AUTH-SES-225
  - TC-AUTH-SES-226
  - TC-AUTH-SES-227
  - TC-AUTH-SES-228
  - TC-AUTH-SES-229
  - TC-AUTH-SES-230
coverage:
  web: automated
---

# Dialog Lifecycle Non-dismissable: Escape, Klik Backdrop, dan Tombol Silang

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`; akun ini sudah login di Browser Admin pada hook; user Client Suspend di-seed oleh akun aktor Total Control (Global Settings) dengan scope Client Suspend, Tabel Data Uji Pre-setup #32): enam user profil BASE milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run; satu user lain (TC-AUTH-SES-229) milik Client Suspend dirinci di bawah. Sesi web tiap user dibuka lewat login pada langkah TC masing-masing (konteks Browser A baru per TC) agar tidak kedaluwarsa karena idle sebelum dipakai:
  - TC-AUTH-SES-225: `Bayu Hidayat` (`bayuhidayat+{runId}-063@qwertysystem.net`)
  - TC-AUTH-SES-227: `Joko Puspita` (`jokopuspita+{runId}-063@qwertysystem.net`)
  - TC-AUTH-SES-228: `Citra Saputra` (`citrasaputra+{runId}-063@qwertysystem.net`)
  - TC-AUTH-SES-230: `Ayu Damayanti` (`ayudamayanti+{runId}-063@qwertysystem.net`)
  - TC-AUTH-SES-226: `Intan Utami` (`intanutami+{runId}-063@qwertysystem.net`)
  - TC-AUTH-SES-224: `Wulan Wulandari` (`wulanwulandari+{runId}-063@qwertysystem.net`)
  - TC-AUTH-SES-229: `Yoga Firmansyah` (`yogafirmansyah+{runId}-063@qwertysystem.net`), profil BASE milik Client Suspend (Tabel Data Uji Pre-setup #16: subscription Fixed Asset Active), di-seed oleh akun aktor Total Control (Global Settings) dengan scope Client Suspend (Tabel Data Uji Pre-setup #32)
- Akun aktor lain (login eksplisit di langkah, ganti konteks): Admin License `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #2), `Spectra.env.FA_MGL_PASSWORD`, di Browser Lisensi (TC-AUTH-SES-228); Principal Admin Console `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #4), `Spectra.env.AC_PRINCIPAL_PASSWORD`, di Browser Principal untuk Suspend dan Unsuspend Client Suspend (TC-AUTH-SES-229).
- Password baru hasil Reset Password: `Spectra.env.SES_PASSWORD_NEW` (TC-AUTH-SES-230). Mail-catcher lingkungan uji (Tabel Data Uji Pre-setup #19) dapat membaca email reset `ayudamayanti+{runId}-063@qwertysystem.net`.
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server dan jam browser/perangkat dimajukan bersama pada TC-AUTH-SES-224 (keduanya dipulihkan dengan langkah eksplisit); Client Suspend di-Suspend pada TC-AUTH-SES-229 (di-Unsuspend dengan langkah eksplisit). Keduanya dipulihkan juga di hook `after`.
- Hook `after`: pulihkan jam server dan jam browser/perangkat ke waktu nyata; Unsuspend Client Suspend bila masih Suspended; akhiri semua sesi seed; tutup semua konteks browser; hapus ketujuh user (termasuk `Intan Utami` bila belum terhapus). Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`, `SES_PASSWORD_NEW`, `AC_PRINCIPAL_PASSWORD`, `FA_MGL_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness a): banyak konteks browser bersamaan (Browser Admin, Browser A, Browser B dengan user agent yang dapat ditetapkan: Chrome on Windows dan Firefox on macOS, Browser C, Browser Principal, Browser Lisensi); mengirim tombol Escape dan klik pada area backdrop; pembacaan ada atau tidaknya tombol silang (X) pada dialog; pengatur waktu server uji dan jam browser/perangkat yang dimajukan bersama (Tabel Data Uji Pre-setup #18); mail-catcher; reCAPTCHA mode uji di environment (halaman Login with Password).

## Test Steps

### TC-AUTH-SES-225: Dialog "Logged Out" tidak dapat ditutup lewat Escape atau klik backdrop

1. Di Browser A (konteks baru, Chrome on Windows) login dengan `bayuhidayat+{runId}-063@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
2. Di Browser B (konteks baru, Firefox on macOS) login dengan akun yang sama dan klik [Log in] → Dialog Duplicate Login Attempt muncul
3. Klik [Confirm] pada Dialog Duplicate Login Attempt
4. Pindah ke Browser A (tanpa mengklik apa pun) → Dialog "Logged Out" muncul
5. Tekan Escape
6. Verifikasi Dialog "Logged Out" tetap tampil setelah Escape
7. Klik area gelap di luar dialog
8. Verifikasi Dialog "Logged Out" tetap tampil setelah klik backdrop
9. Periksa tombol silang (X) pada dialog
10. Verifikasi Tidak ada tombol silang (X) pada Dialog "Logged Out"

### TC-AUTH-SES-227: Dialog "Account Deactivated" tidak dapat ditutup lewat Escape atau klik backdrop

11. Tutup konteks Browser A dan Browser B TC sebelumnya (hapus sesi login browser), lalu di Browser A (konteks baru, Chrome on Windows) login dengan `jokopuspita+{runId}-063@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
12. Di Browser Admin buka `Global Settings > User`, cari `Joko Puspita`, lalu matikan Toggle Active
13. Pindah ke Browser A → Dialog "Account Deactivated" muncul
14. Tekan Escape
15. Verifikasi Dialog "Account Deactivated" tetap tampil setelah Escape
16. Klik area gelap di luar dialog
17. Verifikasi Dialog "Account Deactivated" tetap tampil setelah klik backdrop
18. Periksa tombol silang (X) pada dialog
19. Verifikasi Tidak ada tombol silang (X) pada Dialog "Account Deactivated"

### TC-AUTH-SES-228: Dialog "Log Out" tidak dapat ditutup lewat Escape atau klik backdrop

20. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser), lalu di Browser A (konteks baru, Chrome on Windows) login dengan `citrasaputra+{runId}-063@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
21. Di Browser A klik card Fixed Asset → sesi-produk Fixed Asset aktif dan seat terpakai
22. Buka Browser Lisensi (konteks baru) dan login sebagai `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.FA_MGL_PASSWORD`
23. Di Browser Lisensi buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset), pilih `Citra Saputra`, lalu klik [Force Logout]
24. Klik [Confirm Logout] pada dialog konfirmasi "Force Logout User"
25. Pindah ke Browser A → Dialog "Log Out" muncul
26. Tekan Escape
27. Verifikasi Dialog "Log Out" tetap tampil setelah Escape
28. Klik area gelap di luar dialog
29. Verifikasi Dialog "Log Out" tetap tampil setelah klik backdrop
30. Periksa tombol silang (X) pada dialog
31. Verifikasi Tidak ada tombol silang (X) pada Dialog "Log Out"

### TC-AUTH-SES-230: Dialog "Password Changed" tidak dapat ditutup lewat Escape atau klik backdrop

32. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser), lalu di Browser A (konteks baru, Chrome on Windows) login dengan `ayudamayanti+{runId}-063@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
33. Di Browser C (konteks baru, belum login) buka `Auth > Login with Password` dan jalankan Forgot Password untuk `ayudamayanti+{runId}-063@qwertysystem.net`
34. Buka email reset password di mail-catcher dan buka tautan Reset Password-nya di Browser C
35. Isi password baru `Spectra.env.SES_PASSWORD_NEW` yang valid dan selesaikan Reset Password
36. Pindah ke Browser A dan klik menu apa pun → Dialog "Password Changed" muncul
37. Tekan Escape
38. Verifikasi Dialog "Password Changed" tetap tampil setelah Escape
39. Klik area gelap di luar dialog
40. Verifikasi Dialog "Password Changed" tetap tampil setelah klik backdrop

### TC-AUTH-SES-226: Dialog "Account no longer Active" tidak dapat ditutup lewat Escape atau klik backdrop

41. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser), lalu di Browser A (konteks baru, Chrome on Windows) login dengan `intanutami+{runId}-063@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
42. Di Browser Admin buka `Global Settings > User`, cari `Intan Utami`, lalu hapus user tersebut sampai konfirmasi selesai
43. Pindah ke Browser A → Dialog "Account no longer Active" muncul
44. Tekan Escape
45. Verifikasi Dialog "Account no longer Active" tetap tampil setelah Escape
46. Klik area gelap di luar dialog
47. Verifikasi Dialog "Account no longer Active" tetap tampil setelah klik backdrop
48. Periksa tombol silang (X) pada dialog
49. Verifikasi Tidak ada tombol silang (X) pada Dialog "Account no longer Active"

### TC-AUTH-SES-224: Dialog Session Expired tidak dapat ditutup lewat Escape atau klik backdrop

50. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser), lalu di Browser A (konteks baru, Chrome on Windows) login dengan `wulanwulandari+{runId}-063@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
51. Biarkan Browser A tanpa aktivitas dan majukan jam server dan jam browser/perangkat bersama 10 menit → Toast Idle Warning tampil
52. Majukan jam server dan jam browser/perangkat bersama 6 menit lagi (idle 16 menit) → Dialog "Session Expired" muncul
53. Tekan Escape
54. Verifikasi Dialog Session Expired tetap tampil setelah Escape
55. Klik area gelap di luar dialog
56. Verifikasi Dialog Session Expired tetap tampil setelah klik backdrop
57. Coba klik tombol atau menu di halaman di belakang dialog
58. Verifikasi Halaman di belakang dialog tetap beku: klik tidak berpengaruh
59. Pulihkan jam server dan jam browser/perangkat ke waktu nyata

### TC-AUTH-SES-229: Dialog "Access Restricted" tidak dapat ditutup lewat Escape atau klik backdrop

60. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser), lalu di Browser A (konteks baru, Chrome on Windows) login dengan `yogafirmansyah+{runId}-063@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
61. Buka Browser Principal (konteks baru) dan login sebagai `principalAdminConsole_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_PRINCIPAL_PASSWORD`
62. Di Browser Principal buka `Admin Console > Client`, buka menu elipsis Client Suspend, dan pilih Suspend
63. Pindah ke Browser A → Dialog "Access Restricted" muncul
64. Tekan Escape
65. Verifikasi Dialog "Access Restricted" tetap tampil setelah Escape
66. Klik area gelap di luar dialog
67. Verifikasi Dialog "Access Restricted" tetap tampil setelah klik backdrop
68. Periksa tombol silang (X) pada dialog
69. Verifikasi Tidak ada tombol silang (X) pada Dialog "Access Restricted"
70. Di Browser Principal buka menu elipsis Client Suspend dan pilih Unsuspend

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec melewati sekitar 35 langkah karena tujuh dialog masing-masing butuh pemicu dan konteks sendiri; tiap TC memakai user dan Browser A sendiri, sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-225, 227, 228, 230, 226, 224, 229 (urutan TC sumber 224 sampai 230). TC-AUTH-SES-224 memajukan waktu server sehingga dipindah sesudah TC lain yang memakai sesi aktif; TC-AUTH-SES-226 menghapus user; TC-AUTH-SES-229 men-Suspend Client Suspend sehingga ditaruh paling akhir dan di-Unsuspend di akhir TC (langkah 70).
- Dependensi disalin sebagai langkah (S-04): TC-AUTH-SES-225 menyalin langkah TC-AUTH-SES-2; TC-AUTH-SES-227 menyalin TC-AUTH-SES-7; TC-AUTH-SES-228 menyalin TC-AUTH-SES-8; TC-AUTH-SES-226 menyalin TC-AUTH-SES-6; TC-AUTH-SES-224 menyalin TC-AUTH-SES-46 (langkah 51 sampai 52; langkah mencoba klik halaman belakang ditaruh sebagai langkah 57 setelah Escape dan klik backdrop, supaya asersi "halaman beku" memuat keadaan sesudah kedua cara); TC-AUTH-SES-229 menyalin TC-AUTH-SES-9; TC-AUTH-SES-230 memakai Reset Password pada Browser C (lihat Temuan 1).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): login user uji (langkah pembuka tiap TC juga menutup konteks Browser A, dan Browser B untuk TC-AUTH-SES-227, TC sebelumnya serta menghapus sesi login browser, S-09); ganti akun ke Admin License dan Principal; memajukan dan memulihkan jam server dan jam browser/perangkat; Unsuspend Client Suspend (langkah 70); membuka konteks Browser C; membuka mail-catcher.
- Temuan untuk QA: (1) TC-AUTH-SES-230 menyebut Dialog "Password Changed" tampil di Browser A, sedangkan dependensi TC-AUTH-SES-5 memicunya di perangkat mobile A setelah Change Password dari Browser A. Agar dialog tampil di Browser A, spec memakai Reset Password dari Browser C yang belum login (aturan `AUTHSES-LOGIC-07d`: semua sesi aktif user ter-invalidate) dan mail-catcher. (2) TC-AUTH-SES-230 Langkah Uji tidak memuat langkah "Periksa tidak ada tombol silang (X)" seperti TC-224 sampai 229 lain; spec tidak mengasersi tombol silang untuk dialog Password Changed dan Session Expired (TC-AUTH-SES-224 dan 230). (3) TC-AUTH-SES-228 dan 8 tidak menyebut bahwa user harus membuka produk Fixed Asset sebelum force-logout; langkah 21 ditambahkan dari precondition TC-AUTH-SES-8 (sesi-produk Fixed Asset aktif).
