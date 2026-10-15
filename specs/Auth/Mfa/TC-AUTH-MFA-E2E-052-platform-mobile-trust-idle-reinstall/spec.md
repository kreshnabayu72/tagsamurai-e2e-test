---
id: TC-AUTH-MFA-E2E-052-platform-mobile-trust-idle-reinstall
title: "Trust, Idle, dan Pasang Ulang Aplikasi per Platform"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-29
  - TC-AUTH-MFA-32
  - TC-AUTH-MFA-49
  - TC-AUTH-MFA-146
coverage:
  mobile: automated
  web: automated
---

# Trust, Idle, dan Pasang Ulang Aplikasi per Platform

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) untuk semua TC; browser uji A (profil browser dengan ID device persisten yang dikenali) untuk bagian web TC-AUTH-MFA-29.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): empat user profil MOB (Tabel Data Uji Pre-setup #11: Activated, Active ON, Authenticator sudah terdaftar), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Kondisi per platform di-seed BE (Tabel Data Uji Pre-setup #20: seed `last_logout_at` per platform dan trusted device per platform):
  - TC-AUTH-MFA-29: `Adi Nugraha` (`adinugraha+{runId}-052@qwertysystem.net`); logout mobile terakhir 31 hari yang lalu, logout web terakhir 5 hari yang lalu; ID device browser uji A terdaftar sebagai trusted device web
  - TC-AUTH-MFA-32: `Rina Oktaviani` (`rinaoktaviani+{runId}-052@qwertysystem.net`); sudah pernah login sukses di mobile dari perangkat uji yang sama (ID device aplikasi terpasang terdaftar sebagai trusted device mobile); logout mobile terakhir kurang dari 30 hari
  - TC-AUTH-MFA-49: `Iwan Setyawan` (`iwansetyawan+{runId}-052@qwertysystem.net`); sudah login sukses di web, belum pernah login di aplikasi mobile
  - TC-AUTH-MFA-146: `Jaya Kusuma` (`jayakusuma+{runId}-052@qwertysystem.net`); sudah login sukses di web dan device web dikenali; belum ada trusted device di mobile
- Hook `after`: hapus keempat user, pastikan aplikasi mobile terpasang dan tanpa sesi aktif, dan bersihkan sesi browser uji A. Pembersihan tidak berasumsi seeding berhasil penuh. Jam server uji tidak digeser oleh spec ini.
- Akun yang dipakai: tanpa login (halaman publik di aplikasi mobile dan di browser uji A) untuk semua TC.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: driver otomasi Android (aplikasi native) dengan uninstall dan install ulang aplikasi pada perangkat uji (APK uji tersedia; penyimpanan aman perangkat ikut hilang saat aplikasi dihapus); mail-catcher lingkungan uji untuk email alert "New sign-in to your TAG Samurai account" (TC-AUTH-MFA-32, 49); browser uji A dengan ID device persisten; reCAPTCHA mode uji di environment.
- Seeding state BE per user (kemampuan teknis): `last_logout_at` per platform (Adi Nugraha, Rina Oktaviani), trusted device web ber-ID device browser uji A (Adi Nugraha, Jaya Kusuma), trusted device mobile ber-ID device aplikasi saat instal (Rina Oktaviani), riwayat login sukses di web (Iwan Setyawan, Jaya Kusuma), dan Authenticator terdaftar dengan secret yang dikenal aplikasi authenticator uji; mekanisme seeding (endpoint atau skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.

## Test Steps

### TC-AUTH-MFA-49: Login pertama di platform kedua setelah login sukses di platform lain

1. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher `iwansetyawan+{runId}-052@qwertysystem.net` sebagai baseline
2. Buka aplikasi mobile TAG Samurai → halaman Login with Password tampil
3. Ketik `iwansetyawan+{runId}-052@qwertysystem.net` pada field Email
4. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
5. Klik button [Log in] → layar Confirm to Continue tampil
6. Centang checkbox persetujuan, lalu klik [Continue ➔]
7. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil di mobile (MFA wajib karena belum ada trusted device di platform mobile)
8. Buka mail-catcher lingkungan uji untuk `iwansetyawan+{runId}-052@qwertysystem.net`
9. Verifikasi Email alert dengan subject "New sign-in to your TAG Samurai account" diterima di mail-catcher untuk `iwansetyawan+{runId}-052@qwertysystem.net` (jumlah bertambah satu dari baseline; diperlakukan device baru, bukan login pertama)

### TC-AUTH-MFA-146: Trust device bersifat per platform: trust web tidak membebaskan mobile

10. Tutup paksa aplikasi mobile TAG Samurai agar sesi pre-auth TC sebelumnya tidak dilanjutkan
11. Buka aplikasi mobile TAG Samurai → halaman Login with Password tampil
12. Ketik `jayakusuma+{runId}-052@qwertysystem.net` pada field Email
13. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
14. Klik button [Log in]
15. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil di mobile walau `Jaya Kusuma` memiliki trusted device dan login terakhir di web

### TC-AUTH-MFA-29: Idle ≥30 hari dihitung per platform: mobile idle memicu MFA, web aktif tetap single-step

16. Tutup paksa aplikasi mobile TAG Samurai agar sesi pre-auth TC sebelumnya tidak dilanjutkan
17. Buka aplikasi mobile TAG Samurai → halaman Login with Password tampil
18. Ketik `adinugraha+{runId}-052@qwertysystem.net` pada field Email
19. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
20. Klik button [Log in] → layar Confirm to Continue tampil
21. Centang checkbox persetujuan, lalu klik [Continue ➔]
22. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil di mobile (MFA wajib; logout mobile terakhir 31 hari)
23. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka browser uji A tanpa sesi login
24. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
25. Ketik `adinugraha+{runId}-052@qwertysystem.net` pada field Email
26. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
27. Centang widget reCAPTCHA "I'm not a robot"
28. Klik button [Log in]
29. Verifikasi Halaman MFA tidak tampil di web
30. Verifikasi Browser dialihkan ke Portal — Product Hub (logout web terakhir kurang dari 30 hari)

### TC-AUTH-MFA-32: Memasang ulang aplikasi mobile membuat perangkat dianggap device baru

31. Tutup paksa aplikasi mobile TAG Samurai agar sesi pre-auth TC sebelumnya tidak dilanjutkan
32. Buka aplikasi mobile TAG Samurai → halaman Login with Password tampil
33. Ketik `rinaoktaviani+{runId}-052@qwertysystem.net` pada field Email
34. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
35. Klik button [Log in]
36. Verifikasi Halaman MFA tidak tampil
37. Verifikasi Portal — Product Hub tampil
38. Hapus aplikasi mobile TAG Samurai dari perangkat uji
39. Pasang kembali aplikasi mobile TAG Samurai pada perangkat uji yang sama
40. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher `rinaoktaviani+{runId}-052@qwertysystem.net` sebagai baseline
41. Buka aplikasi mobile TAG Samurai → halaman Login with Password tampil
42. Ketik `rinaoktaviani+{runId}-052@qwertysystem.net` pada field Email
43. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
44. Klik button [Log in]
45. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (ID device di penyimpanan aman hilang bersama aplikasi)
46. Buka mail-catcher lingkungan uji untuk `rinaoktaviani+{runId}-052@qwertysystem.net`
47. Verifikasi Email alert dengan subject "New sign-in to your TAG Samurai account" diterima di mail-catcher untuk `rinaoktaviani+{runId}-052@qwertysystem.net` (jumlah bertambah satu dari baseline)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Kelas harness d (kondisi per platform dan uninstall/reinstall perangkat): keempat TC memakai satu jenis harness, aplikasi Android dengan seeding per platform.
- Penyimpangan urutan (S-05): urutan di spec TC-AUTH-MFA-49, TC-AUTH-MFA-146, TC-AUTH-MFA-29, TC-AUTH-MFA-32, bukan urutan TC sumber (29, 32, 49, 146). TC-AUTH-MFA-49 dan 146 hanya sampai halaman Choose Verification Method tanpa mengubah state, TC-AUTH-MFA-29 menambah sesi web, dan TC-AUTH-MFA-32 menghapus dan memasang ulang aplikasi sehingga ditaruh paling akhir (S-10).
- Langkah penghubung tanpa awalan `Verifikasi` (langkah 10, 16, 31 menutup paksa aplikasi; langkah 1 dan 40 mencatat baseline jumlah email alert; langkah 8 dan 46 membuka mail-catcher; langkah 23 membuka browser uji A; langkah 27 reCAPTCHA di web) bukan asersi tambahan (S-03).
- Asersi pencatatan log tidak ada di spec ini; hanya halaman yang tampil dan email alert yang dicek sesuai TC.
- Temuan untuk QA: (1) TC-AUTH-MFA-29 precondition d menulis "seed; manipulasi jam server" tanpa menetapkan salah satu; spec men-seed `last_logout_at` per platform. (2) TC-AUTH-MFA-29 Langkah Uji 6 tidak menyebut layar Confirm to Continue di web, sedangkan Langkah Uji mobile menyebutnya; TC-AUTH-MFA-146 dan 32 juga tidak menyebut layar Confirm to Continue padahal profil MOB yang sama; spec mengikuti TC. (3) Post Condition TC-AUTH-MFA-146 "Daftar trusted device web `Jaya Kusuma` tidak berubah", TC-AUTH-MFA-49 dan TC-AUTH-MFA-32 "Sesi pre-auth MFA aktif untuk `Iwan Setyawan`/`Rina Oktaviani` di platform mobile", dan TC-AUTH-MFA-29 "Sesi pre-auth MFA aktif untuk `Adi Nugraha` di platform mobile; sesi web aktif untuk `Adi Nugraha`" tidak punya Expected padanan atau langkah observasi di TC (state BE) dan tidak diasersi; padanan yang teramati hanya halaman Choose Verification Method (mobile) dan Portal (web) pada Expected. (4) TC-AUTH-MFA-32 precondition d mensyaratkan perangkat uji yang sama sudah trusted, tetapi ID device aplikasi dibuat saat pemasangan; cara men-seed trusted device untuk ID itu tidak dijelaskan. (5) TC-AUTH-MFA-49 precondition d menyebut "belum pernah login di mobile" sedangkan Expected b menyebut "device baru, bukan login pertama"; spec mengikuti Expected. (6) TC-AUTH-MFA-29 Langkah Uji 6 memakai "browser uji A", tetapi precondition tidak menyebut browser itu sudah trusted; spec mengasumsikan ID device browser uji A trusted untuk user (profil MOB mengikuti BASE). (7) Antar TC tidak ada langkah keluar dari sesi pre-auth mobile; langkah 10, 16, 31 mengandaikan menutup paksa aplikasi mengembalikan halaman Login with Password. (8) Mekanisme seeding state BE (trusted device per platform ber-ID device browser uji A dan ID device aplikasi saat instal, `last_logout_at` per platform, riwayat login sukses di web) belum ada di Pre-setup (#20/#21) TC dan tidak didefinisikan di PRD atau LLD; spec tidak menyebut endpoint seeding.
