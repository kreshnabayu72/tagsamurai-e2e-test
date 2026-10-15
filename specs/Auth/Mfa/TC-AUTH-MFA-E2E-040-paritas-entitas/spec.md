---
id: TC-AUTH-MFA-E2E-040-paritas-entitas
title: "Paritas MFA untuk User Entitas Distributor, Partner, dan Principal"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-185
  - TC-AUTH-MFA-186
  - TC-AUTH-MFA-187
coverage:
  web: automated
---

# Paritas MFA untuk User Entitas Distributor, Partner, dan Principal

## Prerequisites

- Mode: FE+BE.
- Entitas uji milik automation (Tabel Data Uji Pre-setup #24; fixture belum ada, disiapkan tim FE), masing-masing dengan akun aktor Total Control (Global Settings) untuk entitas itu (pola email `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dan kredensial `Spectra.env.GS_TC_PASSWORD` dari Pre-setup; akun dan env var per entitas belum didefinisikan, lihat Temuan untuk QA): satu entitas Distributor, satu entitas Partner, dan satu entitas Principal.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) tiap entitas): tiga user profil NEWDEVE (Tabel Data Uji Pre-setup #5: Activated, Active ON, seperti BASE tetapi ID device browser uji B belum ada di daftar trusted device, Authenticator sudah terdaftar; secret-nya dimuat ke aplikasi authenticator uji), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-185: `Yuni Santoso` (`yunisantoso+{runId}-040@qwertysystem.net`) milik entitas Distributor
  - TC-AUTH-MFA-186: `Bayu Santoso` (`bayusantoso+{runId}-040@qwertysystem.net`) milik entitas Partner
  - TC-AUTH-MFA-187: `Wulan Santoso` (`wulansantoso+{runId}-040@qwertysystem.net`) milik entitas Principal
- Hook `after`: hapus ketiga user. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC dimulai di jendela privat baru (browser uji B, ID device belum dikenali).
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik); reCAPTCHA mode uji di environment.
  - Seeding state BE per user: tanpa ID device browser uji B di daftar trusted device dan Authenticator terdaftar dengan secret yang dikenal aplikasi authenticator uji; mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.

## Test Steps

### TC-AUTH-MFA-185: MFA berlaku identik untuk user dari entitas Distributor

1. Buka jendela privat baru (tanpa sesi login)
2. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
3. Ketik `yunisantoso+{runId}-040@qwertysystem.net` pada field Email
4. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
5. Centang widget reCAPTCHA "I'm not a robot"
6. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
7. Verifikasi Halaman Choose Verification Method identik dengan entitas lain: Title "Choose verification method"
8. Verifikasi Halaman Choose Verification Method identik dengan entitas lain: opsi "OTP via email"
9. Verifikasi Halaman Choose Verification Method identik dengan entitas lain: opsi "Authenticator app"
10. Verifikasi Halaman Choose Verification Method identik dengan entitas lain: Button [Login]
11. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
12. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
13. Verifikasi Halaman Authenticator Verification identik dengan entitas lain: Title "Enter authenticator code"
14. Verifikasi Halaman Authenticator Verification identik dengan entitas lain: Button [Login] (tidak ada pengecualian MFA per jenis entitas)
15. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `yunisantoso+{runId}-040@qwertysystem.net` pada kotak digit lalu klik [Login]
16. Verifikasi Browser dialihkan ke Portal — Product Hub
17. Verifikasi Sesi web aktif untuk `Yuni Santoso`

### TC-AUTH-MFA-186: MFA berlaku identik untuk user dari entitas Partner

18. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
19. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
20. Ketik `bayusantoso+{runId}-040@qwertysystem.net` pada field Email
21. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
22. Centang widget reCAPTCHA "I'm not a robot"
23. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
24. Verifikasi Halaman Choose Verification Method identik dengan entitas lain: Title "Choose verification method"
25. Verifikasi Halaman Choose Verification Method identik dengan entitas lain: opsi "OTP via email"
26. Verifikasi Halaman Choose Verification Method identik dengan entitas lain: opsi "Authenticator app"
27. Verifikasi Halaman Choose Verification Method identik dengan entitas lain: Button [Login]
28. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
29. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
30. Verifikasi Halaman Authenticator Verification identik dengan entitas lain: Title "Enter authenticator code"
31. Verifikasi Halaman Authenticator Verification identik dengan entitas lain: Button [Login] (tidak ada pengecualian MFA per jenis entitas)
32. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `bayusantoso+{runId}-040@qwertysystem.net` pada kotak digit lalu klik [Login]
33. Verifikasi Browser dialihkan ke Portal — Product Hub
34. Verifikasi Sesi web aktif untuk `Bayu Santoso`

### TC-AUTH-MFA-187: MFA berlaku identik untuk user dari entitas Principal

35. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
36. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
37. Ketik `wulansantoso+{runId}-040@qwertysystem.net` pada field Email
38. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
39. Centang widget reCAPTCHA "I'm not a robot"
40. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
41. Verifikasi Halaman Choose Verification Method identik dengan entitas lain: Title "Choose verification method"
42. Verifikasi Halaman Choose Verification Method identik dengan entitas lain: opsi "OTP via email"
43. Verifikasi Halaman Choose Verification Method identik dengan entitas lain: opsi "Authenticator app"
44. Verifikasi Halaman Choose Verification Method identik dengan entitas lain: Button [Login]
45. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
46. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
47. Verifikasi Halaman Authenticator Verification identik dengan entitas lain: Title "Enter authenticator code"
48. Verifikasi Halaman Authenticator Verification identik dengan entitas lain: Button [Login] (tidak ada pengecualian MFA per jenis entitas)
49. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `wulansantoso+{runId}-040@qwertysystem.net` pada kotak digit lalu klik [Login]
50. Verifikasi Browser dialihkan ke Portal — Product Hub
51. Verifikasi Sesi web aktif untuk `Wulan Santoso`

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Paritas entitas: langkah dan asersi ketiga TC identik; hanya user dan entitas yang berbeda. Spec ini bukan Role Matrix karena tidak ada perbedaan akun login atau hasil antar entitas.
- Urutan mengikuti TC sumber. Tiap TC memakai entitas dan user sendiri, jadi urutan antar TC tidak saling bergantung.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): buka jendela privat baru di awal tiap TC (langkah 1, 18, 35).
- Expected butir a dipecah menjadi satu `Verifikasi` per klausa (S-01): Title, tiap opsi, dan Button [Login] pada Choose Verification Method; Title dan Button [Login] pada Authenticator Verification.
- Batas ukuran: 51 langkah, tetapi ketiga TC identik dan independen (entitas dan user sendiri) dan langkah prefix login faktor-1 (langkah 1-6, 18-23, 35-40) tidak dihitung, sehingga ±33 langkah (di bawah ±35) dan spec tidak dipecah.
- Temuan untuk QA:
  - Seluruh TC di spec ini menulis "password valid `Nama User`" pada Langkah Uji; spec memakai `Spectra.env.MFA_PASSWORD` sebagai password valid user seeding.
  - Expected butir a ("halaman MFA dan alur verifikasi identik dengan entitas lain") tidak merinci elemen yang dibandingkan; spec mengonkretkannya dengan Title, opsi, dan CTA dari TC-AUTH-MFA-01 dan PRD `auth/mfa/PRD/mfa.md §4.2` (Halaman 1 dan 3).
  - Data Uji hanya menyebut "entitas: Distributor/Partner/Principal"; TC tidak menyebut akun aktor yang berwenang membuat user di tiap entitas. Spec mengasumsikan akun aktor Total Control (Global Settings) per entitas. Akun dan env var kredensial per entitas (Distributor, Partner, Principal) belum didefinisikan di Pre-setup; Prerequisites memakai pola email dan `GS_TC_PASSWORD` yang ada untuk ketiganya sampai tim FE/QA menetapkannya.
  - Mekanisme seeding state BE profil NEWDEVE (trusted device, Authenticator dengan secret dikenal) belum ada di Pre-setup TC (#20/#21).
  - Post Condition "Satu sesi web aktif" sama dengan klausa sesi pada Expected butir b (langkah 17, 34, 51), jadi tidak ada asersi tambahan dari Post Condition.
