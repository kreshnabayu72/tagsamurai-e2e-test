---
id: TC-AUTH-MFA-E2E-027-sekuensialitas-agreement-dan-mfa
title: "Sekuensialitas Agreement dan MFA"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-47
  - TC-AUTH-MFA-48
coverage:
  web: automated
---

# Sekuensialitas Agreement dan MFA

## Prerequisites

- Mode: FE+BE.
- Principal `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #22, kredensial `Spectra.env.AC_PRINCIPAL_PP_PASSWORD`) sudah mempublikasikan versi Privacy Policy di `Admin Console > Settings > Privacy Policy` sebagai prasyarat environment. Hook `before` hanya memverifikasi (pembacaan lewat API oleh akun Principal) bahwa versi terbitan itu sudah ada sebelum seeding user; hook tidak mem-publish, mengubah, atau menghapus Privacy Policy. Bila versi terbitan belum ada, spec berhenti karena prasyarat environment tidak terpenuhi.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): dua user profil POLICY (Tabel Data Uji Pre-setup #12: seperti FIRST, yaitu Activated, Active ON, belum pernah menyelesaikan login di platform mana pun, Authenticator belum terdaftar, tanpa trusted device; versi Privacy Policy terbitan Principal belum disetujui user sehingga layar Confirm to Continue (Agreement) dan MFA sama-sama terpicu), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-47: `Fikri Ramadhan` (`fikriramadhan+{runId}-027@qwertysystem.net`)
  - TC-AUTH-MFA-48: `Desi Natalia` (`desinatalia+{runId}-027@qwertysystem.net`)
- Hook `after`: hapus kedua user. Pembersihan tidak berasumsi seeding berhasil penuh. Versi Privacy Policy terbitan Principal tidak diubah atau dihapus oleh spec ini.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC dimulai di jendela baru browser uji A tanpa sesi login.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PP_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- State global: tidak ada yang diubah spec ini (jam server, IP uji, geo-IP, counter rate limit, dan versi Privacy Policy tidak disentuh).
- Kemampuan teknis:
  - Seeding state BE per user (dua user POLICY): belum pernah menyelesaikan login di platform mana pun, Authenticator belum terdaftar, tanpa trusted device, dan persetujuan Privacy Policy versi terbitan Principal belum ada; mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - Browser uji A: konteks browser dengan cookie ID device persisten yang belum pernah login untuk user TC itu; setiap TC memakai konteks baru. IP uji tidak diubah.
  - Mail-catcher lingkungan uji untuk membaca jumlah email per alamat tujuan dan memastikan tidak ada email OTP faktor-2 dan tidak ada email alert "New sign-in to your TAG Samurai account". Asersi "tidak ada email" memakai baseline jumlah email sebelum aksi.
  - reCAPTCHA mode uji di environment.

## Test Steps

### TC-AUTH-MFA-47: MFA dievaluasi setelah Agreement dikonfirmasi pada login pertama yang juga memicu Confirm to Continue

1. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
2. Ketik `fikriramadhan+{runId}-027@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Catat jumlah email di mail-catcher untuk `fikriramadhan+{runId}-027@qwertysystem.net` (baseline sebelum login)
6. Klik button [Log in]
7. Amati halaman setelah klik [Log in]
8. Verifikasi Layar "Confirm to Continue" tampil
9. Verifikasi Halaman MFA belum tampil
10. Periksa mail-catcher lingkungan uji untuk `fikriramadhan+{runId}-027@qwertysystem.net`
11. Verifikasi Tidak ada email OTP faktor-2 baru di mail-catcher untuk `fikriramadhan+{runId}-027@qwertysystem.net` dibanding baseline langkah 5
12. Centang checkbox "I have read and agree to the Privacy Policy" lalu klik button [Continue]
13. Amati halaman setelah klik [Continue]
14. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil setelah Agreement dikonfirmasi

### TC-AUTH-MFA-48: Attempt yang menolak Agreement tidak memicu efek samping MFA

15. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
16. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
17. Ketik `desinatalia+{runId}-027@qwertysystem.net` pada field Email
18. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
19. Centang widget reCAPTCHA "I'm not a robot"
20. Catat jumlah email di mail-catcher untuk `desinatalia+{runId}-027@qwertysystem.net` (baseline sebelum login)
21. Klik button [Log in]
22. Amati halaman setelah klik [Log in]
23. Verifikasi Layar "Confirm to Continue" tampil
24. Tinggalkan layar Confirm to Continue tanpa klik [Continue] (kembali ke halaman Login with Password)
25. Periksa mail-catcher lingkungan uji untuk `desinatalia+{runId}-027@qwertysystem.net`
26. Verifikasi Tidak ada halaman MFA yang tampil
27. Verifikasi Tidak ada email OTP faktor-2 baru di mail-catcher untuk `desinatalia+{runId}-027@qwertysystem.net` dibanding baseline langkah 20
28. Verifikasi Tidak ada email alert "New sign-in to your TAG Samurai account" baru di mail-catcher untuk `desinatalia+{runId}-027@qwertysystem.net` dibanding baseline langkah 20
29. Verifikasi Tidak ada sesi penuh untuk `Desi Natalia`

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela baru browser uji A, catat baseline email) bukan asersi tambahan (S-03).
- Baseline email (S-12): langkah 5 dan 20 mencatat jumlah email di mail-catcher sebelum login; asersi "tidak ada email OTP faktor-2" dan "tidak ada email alert" (langkah 11, 27, 28) hanya menghitung email sesudah baseline itu.
- Asersi absence log (S-05): Langkah Uji 8 TC-AUTH-MFA-48 memeriksa "kedua surface log" (`Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`) untuk memastikan tidak ada entri; asersi absence log tidak ditulis di spec ini; diasersi di spec `TC-AUTH-MFA-E2E-035-absence-pencatatan-log` (bagian TC-AUTH-MFA-48, prinsip 10). Bagian TC-AUTH-MFA-48 di spec tersebut membutuhkan prasyarat Principal penerbit Privacy Policy dan versi terbitan yang sama dengan Prerequisites spec ini.
- Post Condition "Sesi pre-auth MFA aktif" (TC-AUTH-MFA-47) dan "Tidak ada sesi pre-auth MFA yang dibuat" (TC-AUTH-MFA-48) tidak diasersi terpisah: sesi pre-auth teramati sebagai halaman Choose Verification Method tampil (langkah 14) dan ketiadaannya sebagai halaman MFA tidak tampil (langkah 26), yang sudah menjadi Expected.
- Temuan untuk QA: (1) TC-AUTH-MFA-47 dan 48 memakai label button "[Continue]" pada layar Confirm to Continue, sedangkan TC MFA lain memakai "[Continue ➔]"; spec mengikuti TC masing-masing. (2) TC-AUTH-MFA-47 menyebut checkbox "I have read and agree to the Privacy Policy" sedangkan TC lain hanya "checkbox persetujuan"; spec mengikuti TC. (3) TC-AUTH-MFA-48 Expected tidak memuat hasil pemeriksaan kedua surface log yang disebut Langkah Uji 8; dirujuk ke spec absence log. (4) TC-AUTH-MFA-47 Langkah Uji 6 ("amati halaman setelah klik [Log in]") dan Expected butir a (halaman MFA belum tampil, tidak ada email OTP faktor-2) tidak punya langkah periksa mail-catcher di Langkah Uji; spec menambahkan langkah 10. (5) Post Condition berupa state BE tanpa langkah observasi dan tanpa Expected padanan tidak diasersi: TC-AUTH-MFA-47 "persetujuan Privacy Policy versi terbaru tersimpan". (6) Mekanisme seeding state BE profil POLICY (belum pernah login, persetujuan Privacy Policy versi terbitan belum ada) belum ada di Pre-setup TC (#20/#21 hanya memuat sebagian) dan tidak didefinisikan di PRD atau LLD; spec tidak menyebut endpoint seeding.
