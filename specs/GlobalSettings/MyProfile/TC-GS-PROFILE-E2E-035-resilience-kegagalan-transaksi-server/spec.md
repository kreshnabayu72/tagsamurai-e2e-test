---
id: TC-GS-PROFILE-E2E-035-resilience-kegagalan-transaksi-server
title: "Resilience: Kegagalan di Tengah Transaksi Server pada Change Password, Edit Photo, dan Delete Photo"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-PROFILE-298
  - TC-GS-PROFILE-299
  - TC-GS-PROFILE-300
coverage:
  web: automated
---

# Resilience: Kegagalan di Tengah Transaksi Server pada Change Password, Edit Photo, dan Delete Photo

## Prerequisites

- Mode: FE+BE (kegagalan terjadi di sisi server dan tidak dapat di-intercept di browser; asersi state backend).
- Akun aktor pertama: Pre-setup #7 (Maya Anggraini, Total Control, `Fixture.myProfile.accounts.password.email`, `Spectra.env.GS_PROFILE_PWD_PASSWORD`, nilai `Passw0rd!Old`) untuk TC-GS-PROFILE-298. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (Step ganti akun): Pre-setup #9 (Nadia Putri, Total Control, `Fixture.myProfile.accounts.photo.email`, `Spectra.env.GS_PROFILE_PHOTO_PASSWORD`; foto profil aktif `Fixture.myProfile.photo.nadiaActive`) untuk TC-GS-PROFILE-299 dan 300.
- Nilai yang diketik pada form Change Password: Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD`, New Password dan Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW` (Data Dinamis #3, nilai `N3wPassw0rd!`).
- File uji Edit Photo: `Fixture.myProfile.files.validPng` (`valid-photo.png`, Pre-setup #17), dipilih lewat kemampuan penanganan file picker native (disediakan tim FE).
- Kemampuan teknis yang disediakan tim BE/FE (tanpa endpoint karangan):
  - Pemicu kegagalan sisi server: (1) kegagalan Auth saat invalidasi sesi atau revoke biometric untuk akun Pre-setup #7; (2) kegagalan setelah file baru tersimpan pada Edit Photo akun Pre-setup #9; (3) kegagalan transaksi Delete Photo akun Pre-setup #9. Tiap pemicu dinonaktifkan segera sesudah bloknya (S-09) dan sekali lagi di hook `after`.
  - Sesi API akun Pre-setup #7 yang tidak dihitung sebagai sesi web: dipakai sebagai "sesi lain" pada TC-GS-PROFILE-298 dan untuk login password lama; kemampuan memeriksa bahwa sesi itu masih aktif juga disediakan tim BE/FE.
  - Pencarian File Manager (Global Settings > File Manager) lewat UI, tanpa kemampuan tambahan.
- Hook suite berikut berlaku; lihat `suite.md`:
  - Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
  - Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
  - Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
  - Sesi API aktor tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE. Lihat `suite.md`, Hook suite 4.
  - Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
  - Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
  - Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- State global yang disentuh: pemicu kegagalan sisi server (dinonaktifkan di akhir tiap blok dan di hook `after`); password #7 dan foto #9 tidak berubah karena transaksi gagal dan tetap dipulihkan hook `after` suite sebagai cadangan.
- Suite serial: `parallel: false`.

## Test Steps

### TC-GS-PROFILE-298: Kegagalan invalidasi sesi atau revoke biometric (Pre-setup #7)

1. Buat sesi API akun Pre-setup #7 sebagai sesi lain (login API dengan `Spectra.env.GS_PROFILE_PWD_PASSWORD`)
2. Aktifkan pemicu kegagalan Auth saat invalidasi sesi atau revoke biometric untuk akun Pre-setup #7
3. Klik [Change Password]
4. Isi Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD`, New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
5. Klik [Save]
6. Verifikasi toast error "Error, failed to update your password."
7. Login API akun Pre-setup #7 dengan password lama `Spectra.env.GS_PROFILE_PWD_PASSWORD`
8. Verifikasi login dengan password lama berhasil (transaksi rollback, password tidak berubah)
9. Verifikasi sesi lain dari langkah 1 masih aktif
10. Nonaktifkan pemicu kegagalan Auth
11. Tutup (dismiss) toast Error
12. Klik [✕] pada modal Change Password
13. Verifikasi dialog "Unsaved Changes" tampil
14. Klik [Leave]

### Ganti akun ke Pre-setup #9

15. Logout
16. Login dengan `Fixture.myProfile.accounts.photo.email` dan `Spectra.env.GS_PROFILE_PHOTO_PASSWORD`
17. Buka My Profile dari account menu navbar

### TC-GS-PROFILE-299: Kegagalan transaksi saat Edit Photo (Pre-setup #9)

18. Aktifkan pemicu kegagalan di server setelah file baru tersimpan pada Edit Photo akun Pre-setup #9
19. Hover Avatar lalu klik [Edit]
20. Pilih file `Fixture.myProfile.files.validPng`
21. Verifikasi toast error "Error, failed to update photo."
22. Verifikasi Avatar tetap menampilkan `Fixture.myProfile.photo.nadiaActive`
23. Nonaktifkan pemicu kegagalan Edit Photo
24. Tutup (dismiss) toast Error
25. Buka File Manager (Global Settings > File Manager)
26. Verifikasi tabel File Manager memuat sedikitnya satu baris
27. Ketik Search `Fixture.myProfile.files.validPng`, tekan Enter
28. Verifikasi hasil Search kosong ("No results found"): tabel File Manager tidak memuat `Fixture.myProfile.files.validPng`
29. Buka My Profile dari account menu navbar

### TC-GS-PROFILE-300: Kegagalan transaksi saat Delete Photo (Pre-setup #9)

30. Aktifkan pemicu kegagalan transaksi Delete Photo akun Pre-setup #9
31. Hover Avatar lalu klik [Delete]
32. Klik [Remove]
33. Verifikasi toast error "Error, failed to remove photo."
34. Verifikasi Avatar tetap menampilkan `Fixture.myProfile.photo.nadiaActive`
35. Nonaktifkan pemicu kegagalan Delete Photo

## Notes

- Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-298, 299, 300). Tidak ada TC hanya-BE; ketiganya masuk FE+BE karena kegagalan sisi server tidak dapat di-intercept (konvensi bagian 6).
- Kelas harness b (kegagalan sisi server). Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (sesi lain sebagai prasyarat butir Expected c TC-GS-PROFILE-298), langkah 2, 10, 18, 23, 30, dan 35 (mengaktifkan atau menonaktifkan pemicu), langkah 7 (login API sebagai observasi butir Expected b), langkah 11 dan 24 (dismiss toast Error), langkah 12 sampai 14 (menutup modal terisi deterministik), langkah 15 sampai 17 (Step ganti akun), langkah 27 (Search untuk menemukan berkas target), dan langkah 29 (kembali ke My Profile).
- Langkah 26 adalah pembanding positif (tabel sudah termuat) sebelum asersi absence di langkah 28; hasil Search kosong ("No results found") menjadi anchor positif asersi absence (bagian 8b butir 2). Urutan TC (langkah 3 TC-GS-PROFILE-299 membuka File Manager) tidak berubah.
- Temuan untuk QA:
  - TC-GS-PROFILE-298 Expected c "Sesi lain tetap aktif" tidak punya sesi lain di Precondition; spec membuat sesi API akun Pre-setup #7 di langkah 1 dan kemampuan memeriksanya disediakan tim BE/FE.
  - TC-GS-PROFILE-299 Expected c hanya menyebut tidak ada `valid-photo.png` di tabel File Manager; "tidak ada file yatim" pada Title hanya diasersi sebatas itu.
  - TC-GS-PROFILE-299 dan 300 Post Condition "Foto aktif tidak berubah" tidak punya langkah observasi sendiri selain Avatar; diasersi hanya lewat Avatar.
  - TC-GS-PROFILE-300 tidak menyatakan apakah dialog Remove Photo tertutup setelah toast Error; spec langsung mengasersi Avatar.
  - Mekanisme pemicu kegagalan sisi server tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim BE/FE tanpa endpoint karangan.
