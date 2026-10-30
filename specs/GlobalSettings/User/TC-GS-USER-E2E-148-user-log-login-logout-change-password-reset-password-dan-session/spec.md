---
id: TC-GS-USER-E2E-148-user-log-login-logout-change-password-reset-password-dan-session
title: "Tab User Log: Login Success dan Failed, Logout, Change Password Success dan Failed, Reset Password Success dan Failed, serta Session started dan ended"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-933
  - TC-GS-USER-934
  - TC-GS-USER-935
  - TC-GS-USER-936
  - TC-GS-USER-937
  - TC-GS-USER-938
  - TC-GS-USER-939
  - TC-GS-USER-940
  - TC-GS-USER-941
coverage:
  web: automated
---

# Tab User Log: Login Success dan Failed, Logout, Change Password Success dan Failed, Reset Password Success dan Failed, serta Session started dan ended

## Prerequisites

- Mode: FE+BE (mail-catcher dan manipulasi jam server dan jam browser pada TC-GS-USER-939).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor pertama: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `USER_PASSWORD` (password login `Dewi Lestari {runId}-148`; memenuhi policy password), `USER_PASSWORD_NEW` (password pengganti yang memenuhi policy), `USER_PASSWORD_WRONG` (nilai password salah untuk percobaan Login dan Current Password yang ditolak; bukan password user mana pun), semuanya didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup (hanya dibaca): akun aktor Siti Nurhaliza (No. 2) di jendela akun aktor. User Pre-setup Dewi Lestari (No. 12) tidak dipakai karena password-nya diubah spec ini (S-06).
- Data Dinamis milik spec, di-seed lewat API di hook `before` (HK1) dan dihapus di hook `after`: `Dewi Lestari {runId}-148`, Email `dewilestari+{runId}-148@qwertysystem.net`, Activated, MFA Enrolled, Division `Finance`, Access `Global Settings`, `Fixed Asset`, dan `Supply Asset`, password `Spectra.env.USER_PASSWORD`.
- Dua jendela: jendela akun aktor (Total Control, hanya membaca Tab User Log) dan jendela user uji (jendela privat berisi sesi `Dewi Lestari {runId}-148`). Jendela akun aktor sebagai pembaca log bukan konteks kedua yang menjadi objek asersi. Jendela user uji ditutup dan sesi login browser terkait dihapus sebelum jendela user uji berikutnya dibuka.
- Kemampuan teknis, disediakan tim FE/BE (TC, PRD, dan LLD tidak menyebut cara atau endpoint): (1) sesi login user seed yang memenuhi MFA (kode authenticator); (2) reCAPTCHA pada Login with Password dan halaman Request Reset dapat diselesaikan di environment automation; (3) mail-catcher: membaca jumlah email per alamat, waktu terbit email, dan tautan reset dari badan email; (4) manipulasi jam: jam server dan jam browser diatur bersama ke nilai absolut atau dibekukan, dan dipulihkan ke waktu nyata; (5) mengakhiri sesi produk Supply Asset untuk user uji.
- Jam (TC-GS-USER-939): masa berlaku tautan reset 24 jam sejak terbit (PRD Reset Password `RSTPWD-LOGIC-01a`). Waktu terbit `{tIssue}` dibaca dari mail-catcher (waktu terbit email), bukan dari waktu hook. Jam server dan jam browser diset bersama ke nilai absolut `{tIssue}` + 24 jam + 60 detik; margin 60 detik (di bawah 5 menit) dihitung dari `{tIssue}`. Tautan dibuka sebelum jam digeser (Setup New Password tampil), sedangkan submit dilakukan setelah jam digeser. Jam dipulihkan lewat langkah aksi sebelum jendela akun aktor membuka Tab User Log; hook `after` memulihkan jam sebagai cadangan.
- State global yang diubah: jam server dan jam browser (TC-GS-USER-939); password `Dewi Lestari {runId}-148` berpindah `USER_PASSWORD`, `USER_PASSWORD_NEW` (TC-GS-USER-936), lalu `USER_PASSWORD` (TC-GS-USER-938). Suite berjalan serial (`suite.md`).
- Baseline log: penanda waktu dicatat pada langkah 2, sesudah hook `before` selesai dan sebelum aksi pemicu pertama (TC-GS-USER-934). Entri hasil seeding berada pada atau di bawah penanda. Baseline jumlah email dicatat per alamat sebelum tiap permintaan reset (`{nEmailA}` dan `{nEmailB}`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Dewi Lestari {runId}-148`, tutup jendela user uji dan hapus sesi login browser terkait, pulihkan jam server dan jam browser. Hook `before` menghapus sisa user bersuffix `-148` dari run lama. Entri log bersifat immutable dan tidak dihapus.

## Test Steps

### Pembukaan layar dan baseline

1. Di jendela akun aktor, buka Global Settings > User > User List (sub-tab Login User)
2. Catat penanda waktu baseline (waktu saat ini) untuk Tab User Log; baris yang diasersi adalah baris di atas penanda ini

### TC-GS-USER-934: Tab User Log mencatat Login Failed

3. Buka jendela user uji (jendela privat, terpisah dari jendela akun aktor)
4. Di jendela user uji, buka Login with Password, isi Email `dewilestari+{runId}-148@qwertysystem.net` dan Password `Spectra.env.USER_PASSWORD_WRONG` (salah; bukan password user uji), selesaikan reCAPTCHA, klik [Log in]
5. Tunggu aksi selesai (caption error tampil, halaman Login tetap)
6. Di jendela akun aktor, buka Global Settings > User > User List, klik icon Search, ketik `Dewi Lestari {runId}-148`, tekan Enter, klik Name `Dewi Lestari {runId}-148`, buka Tab User Log, klik icon Search, ketik `Incorrect password`, tekan Enter
7. Verifikasi Tab User Log `Dewi Lestari {runId}-148` memuat baris di atas penanda baseline dengan Activity `Login`, Status `Failed`, Note `Incorrect password`, IP Address terisi alamat IP dan Device / Browser berformat `[Browser] on [OS]`

### TC-GS-USER-933: Tab User Log mencatat Login Success

8. Di jendela user uji, ganti isi Password dengan `Spectra.env.USER_PASSWORD`, selesaikan reCAPTCHA, klik [Log in]
9. Selesaikan verifikasi MFA `Dewi Lestari {runId}-148` (kode authenticator disediakan tim FE/BE)
10. Tunggu aksi selesai (Portal - Product Hub tampil)
11. Di jendela akun aktor, buka Global Settings > User > User List, klik icon Search, ketik `Dewi Lestari {runId}-148`, tekan Enter, klik Name `Dewi Lestari {runId}-148`, buka Tab User Log, klik icon Search, ketik `Login`, tekan Enter
12. Verifikasi Tab User Log `Dewi Lestari {runId}-148` memuat baris di atas penanda baseline dengan Activity `Login`, Status `Success`, Note `—`, IP Address terisi alamat IP dan Device / Browser berformat `[Browser] on [OS]`

### TC-GS-USER-940: Tab User Log mencatat Session started (Fixed Asset)

13. Di jendela user uji, klik card Fixed Asset di Portal - Product Hub
14. Tunggu aksi selesai (Fixed Asset tampil)
15. Di jendela akun aktor, buka Global Settings > User > User List, klik icon Search, ketik `Dewi Lestari {runId}-148`, tekan Enter, klik Name `Dewi Lestari {runId}-148`, buka Tab User Log, klik icon Search, ketik `Session started (Fixed Asset)`, tekan Enter
16. Verifikasi Tab User Log `Dewi Lestari {runId}-148` memuat baris di atas penanda baseline dengan Activity `Session`, Status `—`, Note `Session started (Fixed Asset)`, IP Address terisi alamat IP dan Device / Browser berformat `[Browser] on [OS]`

### TC-GS-USER-941: Tab User Log mencatat Session ended (Supply Asset)

17. Di jendela user uji, kembali ke Portal - Product Hub, klik card Supply Asset
18. Tunggu aksi selesai (Supply Asset tampil)
19. Akhiri sesi Supply Asset Dewi (cara mengakhiri sesi produk disediakan tim FE/BE)
20. Tunggu aksi selesai (sesi Supply Asset berakhir)
21. Di jendela akun aktor, buka Global Settings > User > User List, klik icon Search, ketik `Dewi Lestari {runId}-148`, tekan Enter, klik Name `Dewi Lestari {runId}-148`, buka Tab User Log, klik icon Search, ketik `Session ended (Supply Asset)`, tekan Enter
22. Verifikasi Tab User Log `Dewi Lestari {runId}-148` memuat baris di atas penanda baseline dengan Activity `Session`, Status `—`, Note `Session ended (Supply Asset)`, IP Address terisi alamat IP dan Device / Browser berformat `[Browser] on [OS]`

### TC-GS-USER-937: Tab User Log mencatat Change Password Failed (Incorrect current password)

23. Di jendela user uji, buka Global Settings > My Profile, klik [Change Password]
24. Isi Current Password `Spectra.env.USER_PASSWORD_WRONG` (salah; bukan password aktif), New Password `Spectra.env.USER_PASSWORD_NEW`, dan Confirm New Password `Spectra.env.USER_PASSWORD_NEW`
25. Klik [Save]
26. Tunggu aksi selesai (inline error tampil, modal tetap terbuka)
27. Di jendela akun aktor, buka Global Settings > User > User List, klik icon Search, ketik `Dewi Lestari {runId}-148`, tekan Enter, klik Name `Dewi Lestari {runId}-148`, buka Tab User Log, klik icon Search, ketik `Incorrect current password`, tekan Enter
28. Verifikasi Tab User Log `Dewi Lestari {runId}-148` memuat baris di atas penanda baseline dengan Activity `Change Password`, Status `Failed`, Note `Incorrect current password`, IP Address terisi alamat IP dan Device / Browser berformat `[Browser] on [OS]`

### TC-GS-USER-936: Tab User Log mencatat Change Password Success (Password changed)

29. Di jendela user uji, ganti isi Current Password dengan `Spectra.env.USER_PASSWORD` (New Password dan Confirm New Password tetap `Spectra.env.USER_PASSWORD_NEW`)
30. Klik [Save]
31. Tunggu aksi selesai (modal Change Password tertutup)
32. Di jendela akun aktor, buka Global Settings > User > User List, klik icon Search, ketik `Dewi Lestari {runId}-148`, tekan Enter, klik Name `Dewi Lestari {runId}-148`, buka Tab User Log, klik icon Search, ketik `Password changed`, tekan Enter
33. Verifikasi Tab User Log `Dewi Lestari {runId}-148` memuat baris di atas penanda baseline dengan Activity `Change Password`, Status `Success`, Note `Password changed`, IP Address terisi alamat IP dan Device / Browser berformat `[Browser] on [OS]`

### TC-GS-USER-935: Tab User Log mencatat Logout

34. Di jendela user uji, logout
35. Tunggu aksi selesai (halaman Login tampil)
36. Di jendela akun aktor, buka Global Settings > User > User List, klik icon Search, ketik `Dewi Lestari {runId}-148`, tekan Enter, klik Name `Dewi Lestari {runId}-148`, buka Tab User Log, klik icon Search, ketik `Logout`, tekan Enter
37. Verifikasi Tab User Log `Dewi Lestari {runId}-148` memuat baris di atas penanda baseline dengan Activity `Logout`, Status `—`, Note `—`, IP Address terisi alamat IP dan Device / Browser berformat `[Browser] on [OS]`
38. Tutup jendela user uji dan hapus sesi login browser terkait

### TC-GS-USER-938: Tab User Log mencatat Reset Password Success (Reset password via email link)

39. Buka jendela user uji (jendela privat, terpisah dari jendela akun aktor)
40. Di jendela user uji, buka Login with Password, klik [Forgot password?]
41. Catat jumlah email di mail-catcher untuk alamat `dewilestari+{runId}-148@qwertysystem.net` sebagai `{nEmailA}`
42. Isi Email `dewilestari+{runId}-148@qwertysystem.net`, selesaikan reCAPTCHA, klik [Reset Password]
43. Tunggu email baru masuk di mail-catcher (jumlah email lebih dari `{nEmailA}`), ambil tautan reset dari email terbaru
44. Buka tautan reset di jendela user uji (Setup New Password tampil)
45. Isi New Password `Spectra.env.USER_PASSWORD` (berbeda dari password aktif `Spectra.env.USER_PASSWORD_NEW`) dan Confirm Password `Spectra.env.USER_PASSWORD`, klik [Reset Password]
46. Tunggu aksi selesai (Password Reset Successful tampil)
47. Tutup jendela user uji dan hapus sesi login browser terkait
48. Di jendela akun aktor, buka Global Settings > User > User List, klik icon Search, ketik `Dewi Lestari {runId}-148`, tekan Enter, klik Name `Dewi Lestari {runId}-148`, buka Tab User Log, klik icon Search, ketik `Reset password via email link`, tekan Enter
49. Verifikasi Tab User Log `Dewi Lestari {runId}-148` memuat baris di atas penanda baseline dengan Activity `Reset Password`, Status `Success`, Note `Reset password via email link`, IP Address terisi alamat IP dan Device / Browser berformat `[Browser] on [OS]`

### TC-GS-USER-939: Tab User Log mencatat Reset Password Failed (Reset link expired)

50. Buka jendela user uji (jendela privat, terpisah dari jendela akun aktor)
51. Di jendela user uji, buka Login with Password, klik [Forgot password?]
52. Catat jumlah email di mail-catcher untuk alamat `dewilestari+{runId}-148@qwertysystem.net` sebagai `{nEmailB}`
53. Isi Email `dewilestari+{runId}-148@qwertysystem.net`, selesaikan reCAPTCHA, klik [Reset Password]
54. Tunggu email baru masuk di mail-catcher (jumlah email lebih dari `{nEmailB}`), ambil tautan reset dan waktu terbit email terbaru sebagai `{tIssue}`
55. Buka tautan reset di jendela user uji (Setup New Password tampil)
56. Atur jam server dan jam browser bersama ke nilai absolut `{tIssue}` + 24 jam + 60 detik (dibekukan)
57. Isi New Password `Spectra.env.USER_PASSWORD_NEW` dan Confirm Password `Spectra.env.USER_PASSWORD_NEW`, klik [Reset Password]
58. Tunggu aksi selesai (halaman berganti dari Setup New Password)
59. Pulihkan jam server dan jam browser ke waktu nyata
60. Tutup jendela user uji dan hapus sesi login browser terkait
61. Di jendela akun aktor, buka Global Settings > User > User List, klik icon Search, ketik `Dewi Lestari {runId}-148`, tekan Enter, klik Name `Dewi Lestari {runId}-148`, buka Tab User Log, klik icon Search, ketik `Reset link expired`, tekan Enter
62. Verifikasi Tab User Log `Dewi Lestari {runId}-148` memuat baris di atas penanda baseline dengan Activity `Reset Password`, Status `Failed`, Note `Reset link expired`, IP Address terisi alamat IP dan Device / Browser berformat `[Browser] on [OS]`
63. Verifikasi Note baris `Reset Password` `Failed` tersebut bukan salinan Note Success `Reset password via email link`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Urutan TC di spec: 934, 933, 940, 941, 937, 936, 935, 938, 939. 934 (Login Failed) sebelum 933 supaya satu jendela user uji melanjutkan halaman Login yang sama; 937 (password lama salah) sebelum 936 (ganti password sukses) karena 936 mengubah password aktif; 935 (Logout) menutup sesi sebelum alur Reset Password; 938 sebelum 939 karena Submit New Password sukses menghapus cooldown dan counter Request Reset per email (PRD Reset Password `RSTPWD-LOGIC-04i`); 939 paling akhir karena menggeser jam.
- Baris log dikenali lewat Search Note (atau Activity) pada Tab User Log `Dewi Lestari {runId}-148` dan penanda baseline. Log yang dibuat saat jam digeser (TC-GS-USER-939) bercap waktu di masa depan sehingga tidak diasersi lewat posisi "teratas" (S-12); baris dicari lewat Note.
- Nilai [IP] dan [Browser] on [OS] pada Expected Result TC tidak berupa nilai konkret; spec mengasersi pola (alamat IP terisi dan format `[Browser] on [OS]`).
- Langkah penghubung (aksi tanpa `Verifikasi`): pencatatan penanda baseline (langkah 2), membuka dan menutup jendela user uji, Login with Password dan MFA user uji, "Tunggu aksi selesai" (8b butir 8), pencatatan baseline jumlah email, mengambil tautan reset, pemulihan jam, dan pembukaan Tab User Log beserta Search di jendela akun aktor.
- Spec melewati sekitar 35 langkah karena sembilan TC berada dalam satu kelas (pencatatan User Log), satu user uji, dan satu pola baca-log; tiap blok membangun satu event Auth yang berbeda dan berdiri sendiri pada Note-nya. Blok baca-log berpola (buka Tab User Log, Search, `Verifikasi` kolom) tidak dihitung ke batas ±35 langkah.
- Temuan untuk QA:
  - TC-GS-USER-933 sampai 941: kolom Automation bernilai "Manual Only" tetapi aksinya dapat diotomasi dengan jendela user uji, mail-catcher, dan manipulasi jam; spec ini otomatis dan kebutuhan teknis ditulis di Prerequisites.
  - TC-GS-USER-934: Expected Result "Alasan gagal" tidak berupa nilai; spec memakai Note `Incorrect password` (PRD Auth `auth-foundation.md` §3, percobaan salah pertama), sedangkan PRD `user.md` §8.4 memberi contoh "Invalid password". Perlu konfirmasi QA nilai Note yang benar.
  - TC-GS-USER-935: Expected Result Note `—` untuk Logout; daftar Note Auth pada `auth-foundation.md` memuat Note Logout (mis. `Logged out`). Spec mengikuti TC.
  - TC-GS-USER-938: Expected Result Note `Reset password via email link`, sedangkan `auth-foundation.md` §9 Tabel E mencatat Submit New Password sukses dengan Note `Password updated successfully` dan Request Reset dengan Note `Password reset requested`. Spec mengikuti TC dan butuh konfirmasi QA.
  - TC-GS-USER-939: "link reset sudah kedaluwarsa" tidak menyebut cara membuat tautan kedaluwarsa dan apakah Note dicatat saat membuka tautan atau saat Submit; spec membuka tautan sebelum kedaluwarsa lalu Submit sesudah jam digeser melewati 24 jam (`RSTPWD-LOGIC-01a`), mengikuti `auth-foundation.md` Tabel E baris 5 (Submit New Password, link expired).
  - TC-GS-USER-941: "Sesi Supply Asset Dewi berakhir" tidak menyebut cara sesi berakhir (menutup produk, logout, atau timeout); spec menyebutnya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-GS-USER-933 sampai 941: Precondition (a) "Login sbg Role: Total Control" hanya berlaku untuk jendela akun aktor; aksi user uji dilakukan di jendela terpisah yang tidak disebut TC.
  - Slice ini tidak punya Post Condition pada TC sumber.
