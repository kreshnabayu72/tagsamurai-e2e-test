---
id: TC-GS-PROFILE-E2E-021-change-password-penolakan-server-lanjutan
title: "Change Password: batas 72 karakter, multi-aturan, non-ASCII, sama dengan password aktif, dan anti-reuse"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-PROFILE-99
  - TC-GS-PROFILE-100
  - TC-GS-PROFILE-101
  - TC-GS-PROFILE-104
  - TC-GS-PROFILE-315
coverage:
  web: automated
---

# Change Password: batas 72 karakter, multi-aturan, non-ASCII, sama dengan password aktif, dan anti-reuse

## Prerequisites

- Mode: FE+BE (backend nyata)
- Akun aktor: Pre-setup #7 `passwordProfile_automated_{namaCompany}@qwertysystem.net` (Maya Anggraini; Total Control; password aktif `Passw0rd!Old`; Time Format 24 jam; timezone Asia/Jakarta), kredensial `Spectra.env.GS_PROFILE_PWD_PASSWORD`. Akun ini bukan akun default suite.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Environment variable: `Spectra.env.GS_PROFILE_PWD_PASSWORD` (login akun #7 di hook `before` spec dan Current Password benar), `Spectra.env.PROFILE_PASSWORD_NEW` (`N3wPassw0rd!`, Data Dinamis #3). Password tidak ditulis di spec atau fixture.
- Data input uji (`Fixture.myProfile.changePassword`, literal input yang ditolak, bukan kredensial): 73 karakter `Ab1!` + 69 huruf `x` (TC-GS-PROFILE-99), `abc` (TC-GS-PROFILE-100), `Ab1éxyzw` (TC-GS-PROFILE-315), `Wr0ngPass!` (Current Password salah, TC-GS-PROFILE-104).
- Kemampuan baca state BE (disediakan tim FE/BE, tanpa endpoint karangan): jumlah sesi aktif akun Pre-setup #7. Nilainya dicatat sebagai baseline di langkah pertama dan dibandingkan di setiap `Verifikasi` "tidak ada sesi yang di-invalidate".
- Kemampuan teknis (disediakan tim FE/BE): mengatur counter Change Password akun #7 ke 2 sebelum TC-GS-PROFILE-104.
- State global yang berubah: TC-GS-PROFILE-104 menaikkan counter Change Password akun #7 ke 3 dan mengunci Change Password 15 menit. Pemulihan counter dan password dilakukan hook `after` suite (Hook suite 7). Suite berjalan serial (`parallel: false`). Tidak ada password yang berubah.

## Test Steps

1. Catat jumlah sesi aktif akun Pre-setup #7 lewat kemampuan baca state BE sebagai baseline
2. Klik [Change Password]
3. Ketik `Spectra.env.GS_PROFILE_PWD_PASSWORD` di Current Password
### Melebihi 72 karakter ditolak server (TC-GS-PROFILE-99)
4. Ketik New Password 73 karakter (`Ab1!` + 69 huruf `x`)
5. Ketik Confirm New Password dengan nilai yang sama
6. Klik [Save]
7. Verifikasi caption merah "Max. 72 characters" tampil di bawah New Password
8. Verifikasi checklist real-time tetap tampil tanpa perubahan warna menjadi merah
9. Verifikasi modal Change Password tetap terbuka
10. Verifikasi jumlah sesi aktif akun #7 sama dengan baseline (tidak ada sesi yang di-invalidate)
### Melanggar beberapa aturan (TC-GS-PROFILE-100)
11. Ganti isi New Password dengan `abc`
12. Ganti isi Confirm New Password dengan `abc`
13. Klik [Save]
14. Verifikasi caption merah di bawah New Password: "Minimum 8 characters"
15. Verifikasi caption merah di bawah New Password: "One uppercase (A-Z)"
16. Verifikasi caption merah di bawah New Password: "One number (0-9)"
17. Verifikasi caption merah di bawah New Password: "One special character"
18. Verifikasi tidak ada caption untuk aturan yang terpenuhi ("One lowercase (a-z)" dan "Password cannot contain spaces")
### Huruf non-ASCII bukan karakter spesial (TC-GS-PROFILE-315)
19. Kosongkan isi New Password dan Confirm New Password
20. Ketik `Ab1éxyzw` di New Password
21. Ketik `Ab1éxyzw` di Confirm New Password
22. Klik [Save]
23. Verifikasi caption merah "One special character" tampil di bawah New Password (huruf non-ASCII tidak dihitung sebagai karakter spesial)
24. Verifikasi modal Change Password tetap terbuka
25. Verifikasi jumlah sesi aktif akun #7 sama dengan baseline
### Sama dengan password aktif (TC-GS-PROFILE-101)
26. Ganti isi New Password dengan `Spectra.env.GS_PROFILE_PWD_PASSWORD`
27. Ganti isi Confirm New Password dengan `Spectra.env.GS_PROFILE_PWD_PASSWORD`
28. Klik [Save]
29. Verifikasi inline error di bawah New Password: "Password must be different from your old password"
30. Verifikasi modal Change Password tetap terbuka
31. Verifikasi jumlah sesi aktif akun #7 sama dengan baseline
### Anti-reuse tidak menaikkan counter (TC-GS-PROFILE-104)
32. Atur counter Change Password akun #7 ke 2 lewat fixture BE
33. Kosongkan isi New Password dan Confirm New Password
34. Ketik `Spectra.env.GS_PROFILE_PWD_PASSWORD` di New Password
35. Ketik `Spectra.env.GS_PROFILE_PWD_PASSWORD` di Confirm New Password
36. Klik [Save]
37. Verifikasi inline error di bawah New Password: "Password must be different from your old password"
38. Ganti isi Current Password dengan `Wr0ngPass!`
39. Ganti isi New Password dengan `Spectra.env.PROFILE_PASSWORD_NEW`
40. Ganti isi Confirm New Password dengan `Spectra.env.PROFILE_PASSWORD_NEW`
41. Klik [Save]
42. Verifikasi toast terkunci Change Password tampil untuk percobaan salah ke-3
### Menutup modal yang terisi
43. Klik [✕]
44. Verifikasi dialog "Unsaved Changes" dengan teks "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] serta [Leave]
45. Klik [Leave]

## Notes

- Pembagian TC: TC-GS-PROFILE-99, 100, 101, 104, dan 315 berada di spec ini.
- Urutan TC di dalam spec diubah dari 99, 100, 101, 104, 315 menjadi 99, 100, 315, 101, 104. Alasan: TC-GS-PROFILE-100 dan 315 sama-sama menampilkan caption "One special character", jadi 315 mengikuti 100 dengan langkah pembersih di antaranya (R-12); TC-GS-PROFILE-104 mengunci Change Password dan harus terakhir.
- Langkah penghubung (S-03): "Kosongkan isi New Password dan Confirm New Password" sebelum TC-GS-PROFILE-315 dan sebelum TC-GS-PROFILE-104 membersihkan caption dan inline error identik dari kasus sebelumnya. Mengganti Current Password dengan `Wr0ngPass!` mengikuti langkah uji ke-3 TC-GS-PROFILE-104. Tiga langkah penutup memulihkan form dirty (S-08, S-09).
- Spec ini di atas smell 35 langkah. Alasan: seluruh blok satu topik (penolakan server atas New Password pada modal dan akun yang sama), satu kelas harness; langkah terbanyak berasal dari satu `Verifikasi` per klausa Expected (S-01) dan satu pembukaan modal dipakai berulang. Blok mandiri karena field diganti di antara kasus dan blok yang mengunci diletakkan terakhir.
- Temuan untuk QA:
  - TC-GS-PROFILE-104: Expected hanya menyebut "toast terkunci tampil" tanpa teks; spec mengasersi tampilnya toast terkunci Change Password (teks lengkap ada di TC-GS-PROFILE-103) tanpa menyalin teks.
  - TC-GS-PROFILE-99, 315, 101, 104: Post Condition counter Change Password ("tetap 0", "menjadi 3") tidak punya langkah observasi di TC, jadi tidak diasersi.
  - TC-GS-PROFILE-99, 315, 101: Expected "Tidak ada sesi yang di-invalidate" tidak memberi cara memeriksa; spec memakai kemampuan baca jumlah sesi aktif akun #7 yang disediakan tim FE/BE.
