---
id: TC-AUTH-MFA-E2E-038-client-suspended-dan-expired
title: "MFA pada User dari Client Suspended dan Client Expired"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-179
  - TC-AUTH-MFA-180
coverage:
  web: automated
---

# MFA pada User dari Client Suspended dan Client Expired

## Prerequisites

- Mode: FE+BE.
- Client uji milik automation (fixture belum ada; disiapkan tim FE), masing-masing dengan akun aktor Total Control (Global Settings) sendiri (`{namaCompany}` = nama company Client itu):
  - Client uji S untuk TC-AUTH-MFA-179, berstatus Suspended saat spec berjalan. Akun aktor: `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` milik Client uji S, kredensial `Spectra.env.GS_CLIENTSUSP_TC_PASSWORD`.
  - Client uji E untuk TC-AUTH-MFA-180, berstatus Expired saat spec berjalan. Akun aktor: `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` milik Client uji E, kredensial `Spectra.env.GS_CLIENTEXP_TC_PASSWORD`.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) tiap Client, saat Client masih berstatus aktif): dua user profil NEWDEVE (Tabel Data Uji Pre-setup #5: Activated, Active ON, seperti BASE tetapi ID device browser uji B belum ada di daftar trusted device, Authenticator sudah terdaftar; secret-nya dimuat ke aplikasi authenticator uji), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-179: `Ratna Santoso` (`ratnasantoso+{runId}-038@qwertysystem.net`) pada Client uji S
  - TC-AUTH-MFA-180: `Dimas Santoso` (`dimassantoso+{runId}-038@qwertysystem.net`) pada Client uji E
- Setelah seeding user, hook `before` mengubah status Client uji S menjadi Suspended dan Client uji E menjadi Expired. Aktor dan API pengubah status Client tidak disebut di TC, PRD, maupun LLD (TC-AUTH-MFA-179 dan 180 hanya menyatakan Precondition "Client berstatus Suspended/Expired"), sehingga mekanismenya disediakan tim FE/BE dan dicatat di "Temuan untuk QA".
- Hook `after`: kembalikan status Client uji S dan Client uji E ke status aktif terlebih dahulu (memakai mekanisme yang sama dengan hook `before`), lalu hapus kedua user. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC dimulai di jendela privat baru (browser uji B, ID device belum dikenali).
- Environment variable: `GS_CLIENTSUSP_TC_PASSWORD`, `GS_CLIENTEXP_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik); reCAPTCHA mode uji di environment; mekanisme mengubah dan memulihkan status Client (Suspended, Expired, aktif) dari hook (lihat Temuan untuk QA); seeding state BE per user: tanpa ID device browser uji B di daftar trusted device dan Authenticator terdaftar dengan secret yang dikenal aplikasi authenticator uji, mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.

## Test Steps

### TC-AUTH-MFA-179: User dari Client Suspended tetap dapat menyelesaikan MFA

1. Buka jendela privat baru (tanpa sesi login)
2. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
3. Ketik `ratnasantoso+{runId}-038@qwertysystem.net` pada field Email
4. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
5. Centang widget reCAPTCHA "I'm not a robot"
6. Klik button [Log in]
7. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (MFA tidak diblok oleh status Client Suspended)
8. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
9. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
10. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `ratnasantoso+{runId}-038@qwertysystem.net` pada kotak digit lalu klik [Login]
11. Verifikasi Browser dialihkan ke Portal — Product Hub
12. Verifikasi Sesi web aktif untuk `Ratna Santoso`

### TC-AUTH-MFA-180: User dari Client Expired tetap dapat menyelesaikan MFA

13. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
14. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
15. Ketik `dimassantoso+{runId}-038@qwertysystem.net` pada field Email
16. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
17. Centang widget reCAPTCHA "I'm not a robot"
18. Klik button [Log in]
19. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (MFA tidak diblok oleh status Client Expired)
20. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
21. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
22. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `dimassantoso+{runId}-038@qwertysystem.net` pada kotak digit lalu klik [Login]
23. Verifikasi Browser dialihkan ke Portal — Product Hub
24. Verifikasi Sesi web aktif untuk `Dimas Santoso`

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Kelas harness h (state tenant: Client Suspended dan Expired), dipisah dari verifikasi baca murni. Spec ini hanya memverifikasi bahwa MFA tidak diblok oleh status Client.
- Pembatasan akses read-only Client Suspended dan popup Subscription Not Active saat membuka produk dimiliki session-management dan tidak diasersi di spec ini (sesuai Expected TC).
- Urutan mengikuti TC sumber. Tiap TC memakai Client dan user sendiri, jadi urutan antar TC tidak saling bergantung. Status Client diubah di hook `before` dan dipulihkan di hook `after` (pemulihan dilakukan sebelum penghapusan user).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): buka jendela privat baru di awal tiap TC (langkah 1 dan 13).
- Temuan untuk QA:
  - TC-AUTH-MFA-179 dan 180 menulis "password valid `Nama User`" pada Langkah Uji; spec memakai `Spectra.env.MFA_PASSWORD` sebagai password valid user seeding.
  - TC-AUTH-MFA-179 dan 180 Precondition d hanya menyebut status Client (Suspended, Expired), tanpa menyebut aktor atau API yang mengubah dan memulihkan status itu, dan tanpa menyebut apakah satu Client dapat dipakai bergantian. Spec memakai dua Client terpisah dan tidak menyebut endpoint (tidak ada di TC, PRD, atau LLD); QA/BE perlu menetapkan mekanismenya dan menambahkannya ke Pre-setup TC.
  - Mekanisme seeding state BE per user (profil NEWDEVE: trusted device, Authenticator dengan secret dikenal) belum ada di Pre-setup TC (#20/#21).
  - Post Condition "Satu sesi web aktif untuk `<user>`" (TC-AUTH-MFA-179, 180) sama dengan klausa sesi pada Expected b (langkah 12 dan 24), jadi tidak ada asersi tambahan dari Post Condition.
