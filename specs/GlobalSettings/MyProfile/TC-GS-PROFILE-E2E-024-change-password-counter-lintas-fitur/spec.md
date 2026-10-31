---
id: TC-GS-PROFILE-E2E-024-change-password-counter-lintas-fitur
title: "Change Password: hitungan independen dari Login dan reset oleh Reset Password"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-137
  - TC-GS-PROFILE-138
  - TC-GS-PROFILE-247
  - TC-GS-PROFILE-248
coverage:
  web: automated
---

# Change Password: hitungan independen dari Login dan reset oleh Reset Password

## Prerequisites

- Mode: FE+BE (backend nyata)
- Akun aktor: Pre-setup #7 `passwordProfile_automated_{namaCompany}@qwertysystem.net` (Maya Anggraini; Total Control; password aktif `Passw0rd!Old`; Time Format 24 jam; timezone Asia/Jakarta), kredensial `Spectra.env.GS_PROFILE_PWD_PASSWORD`. Akun ini bukan akun default suite.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Environment variable: `Spectra.env.GS_PROFILE_PWD_PASSWORD` (login akun #7 di hook `before` spec dan Current Password benar), `Spectra.env.PROFILE_PASSWORD_NEW` (`N3wPassw0rd!`, Data Dinamis #3). Password tidak ditulis di spec atau fixture. `Spectra.env.LP_PASSWORD_WRONG` (password salah untuk percobaan Login gagal, TC-GS-PROFILE-137).
- Data input uji (`Fixture.myProfile.changePassword`, literal input yang ditolak, bukan kredensial): `Wr0ngPass!` (Current Password salah) dan `Another1!x` (New Password dan Confirm New Password pada dua percobaan salah TC-GS-PROFILE-248; nilainya tidak tertulis di TC-GS-PROFILE-248, lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE/BE): fixture BE yang mengatur counter Change Password dan counter Login akun #7, mengatur akun #7 ke tier wajib-reset Change Password, serta memulihkan password ke `Passw0rd!Old`, counter ke 0, dan lock Login; mail-catcher uji untuk membaca email Reset Password akun #7 (kemampuan baca jumlah email per alamat, baseline dicatat sebelum aksi pemicu).
- Alur Reset Password (meminta tautan dari halaman Login, membuka tautan email, mengatur password baru) adalah langkah rutin yang labelnya tidak tertulis di TC; kebutuhannya disediakan tim FE sebagai Step bersama (lihat Temuan untuk QA).
- State global yang berubah: password akun #7 (menjadi `Spectra.env.PROFILE_PASSWORD_NEW` oleh Reset Password), counter Change Password dan Login, lock Login 15 menit di akhir TC-GS-PROFILE-137, dan tier wajib-reset. Pemulihan dilakukan fixture BE di antara blok dan hook `after` suite (Hook suite 7). Suite berjalan serial (`parallel: false`).
- Spec ini berganti sesi di tengah alur (Logout dan Login ulang akun #7); akun pertama login di hook `before` spec dan hook `after` mengembalikan sesi ke akun default.

## Test Steps

### Percobaan salah Login tidak menaikkan hitungan Change Password (TC-GS-PROFILE-138)
1. Atur counter Login akun #7 ke 2 lewat fixture BE
2. Klik [Change Password]
3. Ketik `Wr0ngPass!` di Current Password
4. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di New Password
5. Ketik `Spectra.env.PROFILE_PASSWORD_NEW` di Confirm New Password
6. Klik [Save]
7. Verifikasi inline error di bawah Current Password: "Current password is incorrect" (percobaan Change Password ke-1)
8. Kosongkan isi Current Password lalu ketik ulang `Wr0ngPass!`
9. Klik [Save]
10. Verifikasi inline error di bawah Current Password: "Current password is incorrect" (percobaan Change Password ke-2)
11. Verifikasi tidak ada toast terkunci
12. Klik [✕]
13. Verifikasi dialog "Unsaved Changes" dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] serta [Leave]
14. Klik [Leave]
### Percobaan salah Change Password tidak menaikkan hitungan Login (TC-GS-PROFILE-137)
15. Atur counter Change Password akun #7 ke 2 dan counter Login ke 0 lewat fixture BE
16. Logout
17. Login dengan email akun #7 dan password salah `Spectra.env.LP_PASSWORD_WRONG`
18. Verifikasi percobaan Login salah ke-1 menampilkan "Incorrect email or password"
19. Login dengan email akun #7 dan password salah `Spectra.env.LP_PASSWORD_WRONG`
20. Verifikasi percobaan Login salah ke-2 menampilkan "Incorrect email or password"
21. Verifikasi tidak ada caption lock Login
22. Login dengan email akun #7 dan password salah `Spectra.env.LP_PASSWORD_WRONG`
23. Verifikasi percobaan Login salah ke-3 memicu lock Login 15 menit dengan caption "Too many failed login attempts. Your account is locked for 15 minutes." (diikuti jam boleh-coba-lagi)
### Reset Password melepas tier wajib-reset (TC-GS-PROFILE-247)
24. Pulihkan password akun #7 ke `Passw0rd!Old`, counter Change Password dan Login ke 0, dan lock Login lewat fixture BE
25. Atur akun #7 ke tier wajib-reset Change Password lewat fixture BE
26. Catat jumlah email akun Pre-setup #7 di mail-catcher sebagai baseline
27. Minta tautan Reset Password untuk email akun #7 dari halaman Login
28. Ambil email Reset Password akun #7 dari mail-catcher (jumlah email bertambah dari baseline; polling, batas tunggu 2 menit)
29. Buka tautan Reset Password dari email tersebut
30. Atur password baru `Spectra.env.PROFILE_PASSWORD_NEW` pada New Password dan Confirm New Password lalu kirim
31. Tunggu proses Reset Password selesai
32. Login dengan email akun #7 dan password baru `Spectra.env.PROFILE_PASSWORD_NEW`
33. Buka My Profile dari account menu navbar
34. Klik [Change Password]
35. Verifikasi [Save] Enabled
36. Klik [✕]
### Reset Password mereset counter Change Password (TC-GS-PROFILE-248)
37. Pulihkan password akun #7 ke `Passw0rd!Old` dan counter Login ke 0 lewat fixture BE
38. Atur counter Change Password akun #7 ke 2 lewat fixture BE
39. Logout
40. Catat jumlah email akun Pre-setup #7 di mail-catcher sebagai baseline
41. Minta tautan Reset Password untuk email akun #7 dari halaman Login
42. Ambil email Reset Password akun #7 dari mail-catcher (jumlah email bertambah dari baseline; polling, batas tunggu 2 menit)
43. Buka tautan Reset Password dari email tersebut
44. Atur password baru `Spectra.env.PROFILE_PASSWORD_NEW` pada New Password dan Confirm New Password lalu kirim
45. Tunggu proses Reset Password selesai
46. Login dengan email akun #7 dan password baru `Spectra.env.PROFILE_PASSWORD_NEW`
47. Buka My Profile dari account menu navbar
48. Klik [Change Password]
49. Ketik `Wr0ngPass!` di Current Password
50. Ketik `Another1!x` di New Password
51. Ketik `Another1!x` di Confirm New Password
52. Klik [Save]
53. Verifikasi inline error di bawah Current Password: "Current password is incorrect" (percobaan salah ke-1)
54. Kosongkan isi Current Password lalu ketik ulang `Wr0ngPass!`
55. Klik [Save]
56. Verifikasi inline error di bawah Current Password: "Current password is incorrect" (percobaan salah ke-2)
57. Verifikasi tidak ada toast terkunci
58. Klik [✕]
59. Verifikasi dialog "Unsaved Changes" dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] serta [Leave]
60. Klik [Leave]

## Notes

- Pembagian TC: TC-GS-PROFILE-137, 138, 247, dan 248 berada di spec ini. Urutan TC di dalam spec diubah dari 137, 138, 247, 248 menjadi 138, 137, 247, 248: TC-GS-PROFILE-137 berakhir dengan akun #7 ter-logout dan Login terkunci, sehingga TC-GS-PROFILE-138 yang membutuhkan sesi login dijalankan lebih dulu; blok Reset Password dimulai dari halaman Login.
- Langkah penghubung (S-03): "Pulihkan password ... lewat fixture BE" sebelum TC-GS-PROFILE-247 dan 248 mengembalikan precondition blok (password aktif `Passw0rd!Old`, counter 0, lock Login dilepas) karena Reset Password menolak password yang sama dengan password aktif; "Kosongkan isi Current Password lalu ketik ulang" membersihkan inline error identik (R-12); "Buka My Profile dari account menu navbar" diperlukan karena sesudah Login halaman awal adalah Portal; "Tunggu proses Reset Password selesai" mengikuti bagian 8b butir 8 karena langkah berikutnya Login. Tiga langkah penutup sesudah TC-GS-PROFILE-138 dan di akhir spec memulihkan form dirty (S-08, S-09). Klik [✕] sesudah `Verifikasi` [Save] Enabled pada TC-GS-PROFILE-247 menutup modal kosong tanpa dialog.
- Spec ini di atas smell 35 langkah. Alasan: seluruh blok satu topik (hitungan Change Password dan Login saling independen dan di-reset oleh Reset Password), satu akun, satu kelas harness; empat blok mandiri karena masing-masing dimulai dengan state dipulihkan fixture, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah terbanyak berasal dari dua kali alur Reset Password (TC-GS-PROFILE-247 dan 248) dan satu `Verifikasi` per klausa Expected (S-01).
- Temuan untuk QA:
  - TC-GS-PROFILE-247 dan 248: langkah "Selesaikan Reset Password lewat tautan email" tidak merinci halaman, label, dan password baru yang diatur. Spec menulis alur dengan kata umum dan memakai `Spectra.env.PROFILE_PASSWORD_NEW` sebagai password baru; label persisnya perlu ditetapkan dari modul Reset Password.
  - TC-GS-PROFILE-248: langkah uji ke-3 "Kirim Current salah dua kali" tidak menyebut nilai New Password dan Confirm New Password; spec memakai `Another1!x` (nilai TC-GS-PROFILE-108).
  - TC-GS-PROFILE-248: Post Condition "Counter Change Password menjadi 2 (dihitung ulang dari 0)" tidak punya langkah observasi terpisah di TC (Expected sudah mencakup hasil yang teramati), jadi tidak diasersi.
