---
id: TC-AUTH-SES-E2E-020-accessibility-focus-trap-dialog-lifecycle
title: "Accessibility Focus Trap dan Role Alertdialog Dialog Lifecycle"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-251
  - TC-AUTH-SES-252
  - TC-AUTH-SES-305
  - TC-AUTH-SES-309
  - TC-AUTH-SES-310
  - TC-AUTH-SES-311
  - TC-AUTH-SES-312
coverage:
  web: automated
  mobile: automated
---

# Accessibility Focus Trap dan Role Alertdialog Dialog Lifecycle

## Prerequisites

- Mode: FE+BE.
- Akun aktor (Tabel Data Uji Pre-setup #1), nilai `{namaCompany}` mengikuti Client yang dikelola:
  - Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`: seeding user (hook `before`) lewat API; `namaCompany` mengikuti Client masing-masing: Alpha Logistik (Pre-setup #1), akun dengan scope Client Q2 (Tabel Data Uji Pre-setup #26), dan akun dengan scope Client Expired/uji (Tabel Data Uji Pre-setup #31).
- Seeding (hook `before`, lewat API oleh akun aktor Total Control): tujuh user profil BASE (user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-251: `Putri Maulana` (`putrimaulana+{runId}-020@qwertysystem.net`), Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #11: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5)
  - TC-AUTH-SES-252: `Eko Wijaya` (`ekowijaya+{runId}-020@qwertysystem.net`), Client Q2 (Pre-setup #12: subscription Fixed Asset dan Supply Asset Active, kuota masing-masing 2; batas idle 15 menit), App Access Fixed Asset dan Supply Asset, disiapkan oleh akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26)
  - TC-AUTH-SES-305: `Hendra Wijaya` (`hendrawijaya+{runId}-020@qwertysystem.net`), Client `Alpha Logistik`
  - TC-AUTH-SES-309: `Dimas Permata` (`dimaspermata+{runId}-020@qwertysystem.net`), Client `Alpha Logistik`
  - TC-AUTH-SES-310: `Putri Lestari` (`putrilestari+{runId}-020@qwertysystem.net`), Client `Alpha Logistik`
  - TC-AUTH-SES-311: `Eko Pratama` (`ekopratama+{runId}-020@qwertysystem.net`), Client Q2, App Access Fixed Asset, tanpa sesi-produk Fixed Asset, disiapkan oleh akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26)
  - TC-AUTH-SES-312: `Wulan Ramadhan` (`wulanramadhan+{runId}-020@qwertysystem.net`), Client dengan subscription Fixed Asset berstatus Expired (Pre-setup #14), App Access Fixed Asset, tanpa sesi-produk Fixed Asset Active, disiapkan oleh akun aktor Total Control (Global Settings) dengan scope Client Expired/uji (Tabel Data Uji Pre-setup #31)
- Seeding tambahan Client Q2 (TC-AUTH-SES-252 dan 311): dua user seed (disiapkan oleh akun aktor Total Control dengan scope Client Q2, Pre-setup #26) `Gunawan Prakoso` (`gunawanprakoso+{runId}-020@qwertysystem.net`) dan `Melati Anggun` (`melatianggun+{runId}-020@qwertysystem.net`) (padanan Pre-setup #7), password `Spectra.env.SES_PASSWORD`, masing-masing dengan sesi-produk Fixed Asset Active sehingga kuota concurrent Fixed Asset 2 penuh. Sesi-produk seed dibuat oleh langkah seeding di dalam TC-AUTH-SES-252 dan 311 (bukan di hook `before`) dan diakhiri di akhir TC masing-masing.
- Sesi web aktif (status Active) tiap user di Browser A dibuat lewat login API oleh langkah seeding di awal TC masing-masing, bukan di hook `before`: jam server uji dan jam browser/perangkat uji dimajukan kumulatif (TC-AUTH-SES-251 dan 252) sehingga sesi yang dibuat lebih awal akan menua dan kedaluwarsa sebelum TC-nya berjalan. TC-AUTH-SES-309 membuat sesi web (Chrome on Windows) lewat login API dan sesi mobile milik `Dimas Permata` lewat login nyata di perangkat Android uji A (Pre-setup #10 dan #28: email dan password user, lalu [Not now] pada Prompt Enable Biometric).
- Hook `after`: akhiri semua sesi seed (web, mobile, dan sesi-produk), tutup konteks Browser A dan B, kembalikan jam server uji dan jam browser uji ke waktu nyata, hapus semua user seed (termasuk dua user seat). Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`, `SES_PASSWORD_NEW` (password baru hasil Change Password TC-AUTH-SES-309). Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness c: multi-konteks, dan d: time-travel): navigasi keyboard Tab dan Shift+Tab dengan pelacakan elemen yang sedang terfokus (di web dan di perangkat Android uji A dengan keyboard eksternal atau emulasi tombol Tab pada TC-AUTH-SES-309); pemeriksaan atribut DOM `role` pada dialog dan popup; pembaca layar uji atau pemeriksa accessibility tree untuk memastikan pesan dibacakan seketika (TC-AUTH-SES-252); konteks Browser A (Chrome on Windows), dan Browser B (Firefox on macOS) bersamaan; perangkat Android uji A dengan sesi mobile aktif; jam server uji dan jam browser/perangkat uji dapat dimajukan bersama dengan presisi detik dan dipulihkan ke waktu nyata (TC-AUTH-SES-251 dan 252); reCAPTCHA mode uji di environment (halaman Login with Password).
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server uji dan jam browser/perangkat uji (diatur bersama; pemulihan di hook `after`); password `Dimas Permata` (user dihapus di `after`).
- Akun yang dipakai: user uji masing-masing TC di Browser A dan Browser B (bukan akun aktor).

## Test Steps

### TC-AUTH-SES-251: Dialog lifecycle blocking mengunci fokus keyboard di dalam dialog

1. Buka konteks Browser A baru lalu buat sesi web aktif `Putri Maulana` lewat login API (seeding BE) → sesi berstatus Active
2. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
3. Biarkan Browser A tanpa aktivitas dan majukan jam server uji dan jam browser/perangkat uji bersama 10 menit → Toast Idle Warning tampil
4. Majukan jam server uji dan jam browser/perangkat uji bersama 6 menit lagi (idle 16 menit) → Dialog Session Expired tampil
5. Tekan tombol Tab berulang kali (5 kali) dan Shift+Tab berulang kali (5 kali) sambil mencatat elemen yang terfokus setelah tiap penekanan
6. Verifikasi Fokus keyboard hanya berpindah di dalam dialog (focus trap) dan tidak keluar ke halaman di belakangnya
7. Verifikasi Elemen halaman di belakang dialog tidak dapat difokuskan

### TC-AUTH-SES-252: Pesan dialog lifecycle dibacakan dengan peran alertdialog termasuk Popup Concurrent limit reached

8. Buka konteks Browser A baru lalu buat sesi web aktif `Eko Wijaya` (Client Q2) lewat login API (seeding BE) → sesi berstatus Active
9. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
10. Biarkan Browser A tanpa aktivitas dan majukan jam server uji dan jam browser/perangkat uji bersama 10 menit → Toast Idle Warning tampil
11. Majukan jam server uji dan jam browser/perangkat uji bersama 6 menit lagi (idle 16 menit pada batas 15 menit) → Dialog Session Expired tampil
12. Periksa atribut peran dialog
13. Verifikasi Dialog Session Expired memiliki `role="alertdialog"`
14. Verifikasi Pesan Dialog Session Expired dibacakan seketika saat muncul
15. Buat dua sesi-produk Fixed Asset Active milik `Gunawan Prakoso` dan `Melati Anggun` (Client Q2) lewat seeding BE sehingga seat penuh (kuota 2, seat terpakai 2)
16. Buka konteks Browser B baru lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
17. Ketik email `ekowijaya+{runId}-020@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil (sesi sebelumnya sudah expired)
18. Klik card Fixed Asset → Popup "Concurrent session limit reached" tampil
19. Periksa atribut peran popup
20. Verifikasi Popup Concurrent session limit reached memiliki `role="alertdialog"`
21. Verifikasi Pesan Popup Concurrent session limit reached dibacakan seketika saat muncul
22. Verifikasi Popup Concurrent session limit reached diperlakukan sebagai dialog, bukan toast
23. Akhiri kedua sesi-produk seed `Gunawan Prakoso` dan `Melati Anggun` supaya seat kosong

### TC-AUTH-SES-305: Focus trap dan role alertdialog pada Dialog "Logged Out"

24. Buka konteks Browser A baru (Chrome on Windows) lalu buat sesi web aktif `Hendra Wijaya` lewat login API (seeding BE) → sesi berstatus Active
25. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
26. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), buka konteks Browser B baru (Firefox on macOS) lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
27. Di Browser B ketik email `hendrawijaya+{runId}-020@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog Duplicate Login Attempt muncul
28. Klik [Confirm] pada Dialog Duplicate Login Attempt
29. Pindah ke Browser A (tanpa mengklik apa pun) → Dialog "Logged Out" muncul
30. Tekan Tab dan Shift+Tab berulang kali (5 kali tiap arah) sambil mencatat elemen yang terfokus
31. Verifikasi Fokus keyboard hanya berpindah di dalam Dialog "Logged Out"
32. Periksa atribut peran dialog
33. Verifikasi Dialog memiliki `role="alertdialog"`

### TC-AUTH-SES-310: Focus trap dan role alertdialog pada Dialog "Duplicate Login Attempt"

34. Buka konteks Browser A baru (Chrome on Windows) lalu buat sesi web aktif `Putri Lestari` lewat login API (seeding BE) → sesi berstatus Active
35. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
36. Tutup konteks Browser B TC sebelumnya (hapus sesi login browser), buka konteks Browser B baru (Firefox on macOS) lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
37. Di Browser B ketik email `putrilestari+{runId}-020@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog "Duplicate Login Attempt" muncul
38. Tekan Tab dan Shift+Tab berulang kali (5 kali tiap arah) sambil mencatat elemen yang terfokus
39. Verifikasi Fokus keyboard hanya berpindah di dalam Dialog "Duplicate Login Attempt"
40. Periksa atribut peran dialog
41. Verifikasi Dialog memiliki `role="alertdialog"`

### TC-AUTH-SES-311: Focus trap dan role alertdialog pada Popup "Concurrent session limit reached"

42. Buat dua sesi-produk Fixed Asset Active milik `Gunawan Prakoso` dan `Melati Anggun` (Client Q2) lewat seeding BE sehingga seat penuh (kuota 2, seat terpakai 2)
43. Buka konteks Browser A baru lalu buat sesi web (sesi platform) aktif `Eko Pratama` (Client Q2, tanpa sesi-produk Fixed Asset) lewat login API (seeding BE) → sesi berstatus Active
44. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
45. Klik card Fixed Asset → Popup "Concurrent session limit reached" tampil
46. Tekan Tab dan Shift+Tab berulang kali (5 kali tiap arah) sambil mencatat elemen yang terfokus
47. Verifikasi Fokus keyboard hanya berpindah di dalam Popup "Concurrent session limit reached"
48. Periksa atribut peran popup
49. Verifikasi Popup memiliki `role="alertdialog"`
50. Akhiri kedua sesi-produk seed `Gunawan Prakoso` dan `Melati Anggun` supaya seat kosong

### TC-AUTH-SES-312: Focus trap dan role alertdialog pada Popup "Subscription Not Active"

51. Tutup konteks Browser A TC sebelumnya (hapus sesi login browser), buka konteks Browser A baru lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
52. Ketik email `wulanramadhan+{runId}-020@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Portal — Product Hub tampil
53. Klik card Fixed Asset → Popup "Subscription Not Active" tampil
54. Tekan Tab dan Shift+Tab berulang kali (5 kali tiap arah) sambil mencatat elemen yang terfokus
55. Verifikasi Fokus keyboard hanya berpindah di dalam Popup "Subscription Not Active"
56. Periksa atribut peran popup
57. Verifikasi Popup memiliki `role="alertdialog"`

### TC-AUTH-SES-309: Focus trap dan role alertdialog pada Dialog "Password Changed"

58. Buka konteks Browser A baru (Chrome on Windows) lalu buat sesi web aktif `Dimas Permata` lewat login API (seeding BE), dan buat sesi mobile aktif `Dimas Permata` lewat login nyata di perangkat Android uji A dengan email `dimaspermata+{runId}-020@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu ketuk [Not now] pada Prompt Enable Biometric → kedua sesi berstatus Active
59. Di Browser A buka Portal — Product Hub → halaman Portal — Product Hub tampil
60. Di Browser A ubah password lewat `Global Settings > My Profile > Change Password` dengan password lama yang benar `Spectra.env.SES_PASSWORD` dan password baru yang valid `Spectra.env.SES_PASSWORD_NEW`
61. Di perangkat Android uji A ketuk layar → Dialog "Password Changed" muncul
62. Tekan Tab dan Shift+Tab berulang kali (5 kali tiap arah) pada perangkat Android uji A sambil mencatat elemen yang terfokus
63. Verifikasi Fokus keyboard hanya berpindah di dalam Dialog "Password Changed"
64. Periksa atribut peran dialog
65. Verifikasi Dialog memiliki `role="alertdialog"`

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness c (multi-konteks) dan d (time-travel); spec accessibility keyboard dan atribut `role` tanpa pemicu dari admin.
- TC-AUTH-SES-306, 307, dan 308 (dialog yang dipicu aksi admin) ada di spec `TC-AUTH-SES-E2E-071-admin-triggered-dialog-focus-trap`.
- Ukuran 65 langkah dibenarkan: seluruh TC memakai pola asersi yang sama (focus trap Tab dan Shift+Tab plus atribut `role`) pada satu kelas aksi, yaitu tanpa aktor admin; tiap TC berdiri sendiri dengan seeding di langkah awalnya.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-251, 252, 305, 310, 311, 312, 309 (urutan TC sumber 251, 252, 305, 309 sampai 312). TC yang memajukan jam server dan memakai seat Client Q2 ditaruh di awal; TC-AUTH-SES-309 terakhir karena mengubah password `Dimas Permata`.
- Dependensi (S-04): langkah pemicu tiap dialog disalin dari TC dependensi tanpa asersi isi dialog (asersi isi dialog ada di spec lain): TC-AUTH-SES-305 dari TC-AUTH-SES-2 (spec `TC-AUTH-SES-E2E-001-screening-dialog-duplicate-login-dan-logged-out`), TC-AUTH-SES-309 dari TC-AUTH-SES-5, TC-AUTH-SES-310 dari TC-AUTH-SES-1, TC-AUTH-SES-311 dari TC-AUTH-SES-10, TC-AUTH-SES-312 dari TC-AUTH-SES-11, TC-AUTH-SES-251 dari TC-AUTH-SES-46 (langkah 3-4), dan TC-AUTH-SES-252 dari TC-AUTH-SES-46 dan TC-AUTH-SES-96.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): membuka konteks browser baru dan membuat sesi seed; membuka Portal — Product Hub; mencatat elemen yang terfokus; memeriksa atribut peran; berpindah antar Browser A dan B; menutup konteks Browser B TC sebelumnya (langkah 26 dan 36) dan konteks Browser A TC sebelumnya sebelum login lewat UI (langkah 51); mengakhiri sesi-produk seed.
- Temuan untuk QA: (1) TC-AUTH-SES-309 berdependensi pada TC-AUTH-SES-5, yang memunculkan Dialog Password Changed di perangkat Android uji A; spec mengikuti dependensi itu sehingga Tab dan Shift+Tab dijalankan di perangkat Android dengan keyboard eksternal atau emulasi tombol Tab. Bila dialog itu seharusnya diuji di web, TC perlu menyebut sesi web kedua. (2) TC-AUTH-SES-311 dan 312 Precondition a menyebut user milik Client Alpha, sedangkan dependensi TC-AUTH-SES-10 dan 11 membutuhkan seat penuh di Client Q2 dan subscription Fixed Asset Expired; spec memakai user milik Client Q2 (TC-AUTH-SES-311) dan Client dengan subscription Fixed Asset Expired (TC-AUTH-SES-312). (3) TC-AUTH-SES-252 langkah 3 "pada sesi lain" tidak menyebut sesi mana; spec membuat login baru user yang sama di Browser B sesudah sesi lama expired, lalu mengklik card Fixed Asset saat seat penuh (mengikuti TC-AUTH-SES-96). (4) "Berulang kali (minimal 5 kali)" ditulis 5 kali tiap arah; TC tidak menyebut cara mengamati elemen terfokus, sehingga pelacakan fokus dan pemeriksaan `role` diputuskan di tahap script. (5) TC-AUTH-SES-252 "pesannya dibacakan seketika saat muncul" butuh pembaca layar uji atau accessibility tree yang kemampuannya tidak terdaftar di Tabel Data Uji Pre-setup #18; ditulis di Prerequisites. (6) TC-AUTH-SES-309 mengambil langkah Change Password dari TC-AUTH-SES-5 tanpa merinci field dan tombolnya; spec menuliskannya seperti di TC. (7) TC-AUTH-SES-251, 252, 305, 309 sampai 312 tidak menyebut widget reCAPTCHA pada langkah login; spec mengikuti TC dan mengandalkan reCAPTCHA mode uji.
