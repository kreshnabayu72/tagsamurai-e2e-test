---
id: TC-GS-PROFILE-E2E-023-change-password-berhasil-login-dan-reset-counter
title: "Change Password berhasil: login password baru, reset counter Change Password dan Login"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-107
  - TC-GS-PROFILE-108
  - TC-GS-PROFILE-307
coverage:
  web: automated
---

# Change Password berhasil: login password baru, reset counter Change Password dan Login

## Prerequisites

- Mode: FE+BE (backend nyata)
- Akun aktor: Pre-setup #7 `passwordProfile_automated_{namaCompany}@qwertysystem.net` (Maya Anggraini; Total Control; password aktif `Passw0rd!Old`; Time Format 24 jam; timezone Asia/Jakarta), kredensial `Spectra.env.GS_PROFILE_PWD_PASSWORD`. Akun ini bukan akun default suite.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Environment variable: `Spectra.env.GS_PROFILE_PWD_PASSWORD` (login akun #7 di hook `before` spec dan Current Password benar), `Spectra.env.PROFILE_PASSWORD_NEW` (`N3wPassw0rd!`, Data Dinamis #3). Password tidak ditulis di spec atau fixture. `Spectra.env.LP_PASSWORD_WRONG` (password salah untuk percobaan Login gagal, TC-GS-PROFILE-307).
- Data input uji (`Fixture.myProfile.changePassword`, literal input yang ditolak, bukan kredensial): `Wr0ngPass!` (Current Password salah) dan `Another1!x` (New Password dan Confirm New Password pada dua percobaan salah TC-GS-PROFILE-108).
- Kemampuan teknis (disediakan tim FE/BE): fixture BE yang mengatur counter Change Password dan counter Login akun #7 ke nilai tertentu serta memulihkan password akun #7 ke `Passw0rd!Old`, counter ke 0, dan lock Login; tiga blok mandiri dimulai dari pemulihan itu.
- State global yang berubah: password akun #7 (menjadi `Spectra.env.PROFILE_PASSWORD_NEW` pada tiap blok), counter Change Password dan Login, serta lock Login 15 menit di akhir TC-GS-PROFILE-307. Pemulihan dilakukan fixture BE di antara blok dan hook `after` suite (Hook suite 7). Suite berjalan serial (`parallel: false`).
- Spec ini berganti sesi di tengah alur (Logout lalu Login ulang akun #7 di blok TC-GS-PROFILE-107 dan 307); akun pertama login di hook `before` spec dan hook `after` mengembalikan sesi ke akun default.

## Test Steps

### Counter Change Password dihitung ulang dari 0 (TC-GS-PROFILE-108)
1. Atur counter Change Password akun #7 ke 2 lewat fixture BE
2. Klik [Change Password]
3. Ketik `Spectra.env.GS_PROFILE_PWD_PASSWORD` di Current Password
4. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di New Password
5. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di Confirm New Password
6. Klik [Save]
7. Verifikasi toast sukses: "Success, your password has been updated."
8. Klik [Change Password]
9. Ketik `Wr0ngPass!` di Current Password
10. Ketik `Another1!x` di New Password
11. Ketik `Another1!x` di Confirm New Password
12. Klik [Save]
13. Verifikasi inline error di bawah Current Password: "Current password is incorrect" (percobaan salah ke-1)
14. Kosongkan isi Current Password lalu ketik ulang `Wr0ngPass!`
15. Klik [Save]
16. Verifikasi inline error di bawah Current Password: "Current password is incorrect" (percobaan salah ke-2)
17. Verifikasi tidak ada toast terkunci
18. Klik [✕]
19. Verifikasi dialog "Unsaved Changes" dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] serta [Leave]
20. Klik [Leave]
21. Pulihkan password akun #7 ke `Passw0rd!Old` dan counter Change Password serta Login ke 0 lewat fixture BE
### Login dengan password lama ditolak dan password baru berhasil (TC-GS-PROFILE-107)
22. Klik [Change Password]
23. Ketik `Spectra.env.GS_PROFILE_PWD_PASSWORD` di Current Password
24. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di New Password
25. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di Confirm New Password
26. Klik [Save]
27. Tunggu modal Change Password tertutup
28. Logout
29. Login dengan email akun #7 dan password lama `Spectra.env.GS_PROFILE_PWD_PASSWORD`
30. Verifikasi login dengan password lama ditolak: halaman Login tetap tampil dan Portal tidak tampil
31. Login dengan email akun #7 dan password baru `Spectra.env.PROFILE_PASSWORD_NEW`
32. Verifikasi login dengan password baru berhasil: Portal tampil
33. Pulihkan password akun #7 ke `Passw0rd!Old` dan counter Change Password serta Login ke 0 lewat fixture BE
### Counter Login dihitung ulang dari 0 (TC-GS-PROFILE-307)
34. Buka My Profile dari account menu navbar
35. Atur counter Login akun #7 ke 2 lewat fixture BE
36. Klik [Change Password]
37. Ketik `Spectra.env.GS_PROFILE_PWD_PASSWORD` di Current Password
38. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di New Password
39. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di Confirm New Password
40. Klik [Save]
41. Verifikasi toast sukses: "Success, your password has been updated."
42. Logout
43. Login dengan email akun #7 dan password salah `Spectra.env.LP_PASSWORD_WRONG`
44. Verifikasi percobaan Login salah ke-1 menampilkan "Incorrect email or password"
45. Login dengan email akun #7 dan password salah `Spectra.env.LP_PASSWORD_WRONG`
46. Verifikasi percobaan Login salah ke-2 menampilkan "Incorrect email or password"
47. Verifikasi tidak ada caption lock Login
48. Login dengan email akun #7 dan password salah `Spectra.env.LP_PASSWORD_WRONG`
49. Verifikasi percobaan Login salah ke-3 memicu lock Login 15 menit dengan caption "Too many failed login attempts. Your account is locked for 15 minutes." (diikuti jam boleh-coba-lagi)

## Notes

- Pembagian TC: TC-GS-PROFILE-107, 108, dan 307 berada di spec ini. Urutan TC di dalam spec diubah dari 107, 108, 307 menjadi 108, 107, 307: TC-GS-PROFILE-108 tidak berganti sesi, sedangkan TC-GS-PROFILE-307 mengunci Login akun #7 dan harus terakhir.
- Langkah penghubung (S-03): "Pulihkan password ... lewat fixture BE" di antara blok mengembalikan precondition blok berikutnya (password aktif `Passw0rd!Old`, counter 0); "Kosongkan isi Current Password lalu ketik ulang" membersihkan inline error identik (R-12); "Buka My Profile dari account menu navbar" sebelum TC-GS-PROFILE-307 diperlukan karena sesudah login password baru halaman awal adalah Portal; "Tunggu modal Change Password tertutup" mengikuti bagian 8b butir 8 karena langkah berikutnya Logout. Tiga langkah penutup sesudah blok TC-GS-PROFILE-108 memulihkan form dirty (S-08, S-09).
- Spec ini di atas smell 35 langkah. Alasan: seluruh blok satu topik (efek Change Password berhasil pada login dan counter), satu akun, satu kelas harness; tiga blok mandiri karena masing-masing dimulai dengan password dan counter dipulihkan fixture, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah terbanyak berasal dari isi field per blok dan satu `Verifikasi` per klausa Expected (S-01).
- Temuan untuk QA:
  - TC-GS-PROFILE-107: Expected "Login dengan password lama ditolak" tidak menyebut teks penolakan; spec mengasersi halaman Login tetap tampil dan Portal tidak tampil tanpa mengarang copy.
  - TC-GS-PROFILE-108: Post Condition "Counter Change Password menjadi 2 (dihitung ulang dari 0)" dan TC-GS-PROFILE-307: Post Condition "Password akun `N3wPassw0rd!`" tidak punya langkah observasi di TC (Expected sudah mencakup hasil yang teramati), jadi tidak diasersi terpisah.
