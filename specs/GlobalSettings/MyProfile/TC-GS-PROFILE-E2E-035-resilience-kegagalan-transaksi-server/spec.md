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
- Akun aktor pertama: Pre-setup #7 (Maya Anggraini, Total Control, `Fixture.myProfile.accounts.password.email`, `Spectra.env.GS_PROFILE_PWD_PASSWORD`) untuk TC-GS-PROFILE-298. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (Step ganti akun): Pre-setup #9 (Nadia Putri, Total Control, `Fixture.myProfile.accounts.photo.email`, `Spectra.env.GS_PROFILE_PHOTO_PASSWORD`; foto profil aktif `Fixture.myProfile.photo.nadiaActive`) untuk TC-GS-PROFILE-299 dan 300.
- Nilai yang diketik pada form Change Password: Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD`, New Password dan Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW` (Data Dinamis #3).
- File uji Edit Photo: `Fixture.myProfile.files.validPng` (`valid-photo.png`, Pre-setup #17), dipilih lewat kemampuan penanganan file picker native (disediakan tim FE).
- Kemampuan teknis yang disediakan tim BE/FE (tanpa endpoint karangan):
  - Pemicu kegagalan sisi server: (1) kegagalan Auth saat invalidasi sesi atau revoke biometric untuk akun Pre-setup #7; (2) kegagalan setelah file baru tersimpan pada Edit Photo akun Pre-setup #9; (3) kegagalan transaksi Delete Photo akun Pre-setup #9. Tiap pemicu dinonaktifkan segera sesudah bloknya (S-09) dan sekali lagi di hook `after`.
  - Sesi lain TC-GS-PROFILE-298 (P-2): sesi web akun Pre-setup #7 di konteks browser kedua. Environment mengizinkan dua sesi web bersamaan untuk akun #7 (disediakan tim FE, sama dengan spec 061 dan 062). Konteks kedua ditutup dan sesi loginnya dihapus di langkah 11. Login API untuk password lama (langkah 8 dan 9) memakai sesi API aktor (Hook suite 4), bukan sebagai sesi lain.
  - Pencarian File Manager (Global Settings > File Manager) lewat UI, tanpa kemampuan tambahan.
- Hook suite berikut berlaku; lihat `suite.md`:
  - Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
  - Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
  - Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
  - Sesi API aktor tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE. Lihat `suite.md`, Hook suite 4.
  - Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
  - Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
  - Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke password awal masing-masing (`Spectra.env.GS_PROFILE_PWD_PASSWORD`, `Spectra.env.GS_PROFILE_PWD12H_PASSWORD`, `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`), counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- State global yang disentuh: pemicu kegagalan sisi server (dinonaktifkan di akhir tiap blok dan di hook `after`); password #7 dan foto #9 tidak berubah karena transaksi gagal dan tetap dipulihkan hook `after` suite sebagai cadangan.
- Suite serial: `parallel: false`.

## Test Steps

### TC-GS-PROFILE-298: Kegagalan invalidasi sesi atau revoke biometric (Pre-setup #7)

1. Buka konteks browser kedua dan login akun Pre-setup #7 di dalamnya dengan `Fixture.myProfile.accounts.password.email` dan `Spectra.env.GS_PROFILE_PWD_PASSWORD` sebagai sesi lain
2. Di konteks browser kedua, buka My Profile dari account menu navbar
3. Aktifkan pemicu kegagalan Auth saat invalidasi sesi atau revoke biometric untuk akun Pre-setup #7
4. Klik [Change Password]
5. Isi Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD`, New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
6. Klik [Save]
7. Verifikasi toast error "Error, failed to update your password."
8. Login API akun Pre-setup #7 dengan password lama `Spectra.env.GS_PROFILE_PWD_PASSWORD`
9. Verifikasi login dengan password lama berhasil (transaksi rollback, password tidak berubah)
10. Di konteks browser kedua, muat ulang halaman lalu verifikasi sesi lain dari langkah 1 masih aktif (halaman My Profile tetap tampil, tidak diarahkan ke Login)
11. Tutup konteks browser kedua dan hapus sesi login-nya
12. Nonaktifkan pemicu kegagalan Auth
13. Tutup (dismiss) toast Error
14. Klik [✕] pada modal Change Password
15. Verifikasi dialog "Unsaved Changes" tampil
16. Klik [Leave]

### Ganti akun ke Pre-setup #9

17. Logout
18. Login dengan `Fixture.myProfile.accounts.photo.email` dan `Spectra.env.GS_PROFILE_PHOTO_PASSWORD`

### TC-GS-PROFILE-299: Kegagalan transaksi saat Edit Photo (Pre-setup #9)

19. Buka File Manager (Global Settings > File Manager)
20. Ketik Search `Fixture.myProfile.files.validPng`, tekan Enter
21. Catat jumlah baris hasil Search sebagai baseline sebelum aksi Edit Photo
22. Buka My Profile dari account menu navbar
23. Aktifkan pemicu kegagalan di server setelah file baru tersimpan pada Edit Photo akun Pre-setup #9
24. Hover Avatar lalu klik [Edit]
25. Pilih file `Fixture.myProfile.files.validPng`
26. Verifikasi toast error "Error, failed to update photo."
27. Verifikasi Avatar tetap menampilkan `Fixture.myProfile.photo.nadiaActive`
28. Nonaktifkan pemicu kegagalan Edit Photo
29. Tutup (dismiss) toast Error
30. Buka File Manager (Global Settings > File Manager)
31. Verifikasi tabel File Manager memuat sedikitnya satu baris
32. Ketik Search `Fixture.myProfile.files.validPng`, tekan Enter
33. Verifikasi jumlah baris hasil Search sama dengan baseline langkah 21 (selisih nol): tabel File Manager tidak memuat tambahan `Fixture.myProfile.files.validPng`
34. Buka My Profile dari account menu navbar

### TC-GS-PROFILE-300: Kegagalan transaksi saat Delete Photo (Pre-setup #9)

35. Aktifkan pemicu kegagalan transaksi Delete Photo akun Pre-setup #9
36. Hover Avatar lalu klik [Delete]
37. Klik [Remove]
38. Verifikasi toast error "Error, failed to remove photo."
39. Verifikasi Avatar tetap menampilkan `Fixture.myProfile.photo.nadiaActive`
40. Nonaktifkan pemicu kegagalan Delete Photo

## Notes

- Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-298, 299, 300). Tidak ada TC hanya-BE; ketiganya masuk FE+BE karena kegagalan sisi server tidak dapat di-intercept (konvensi bagian 6).
- Kelas harness b (kegagalan sisi server). Subjudul `###` memetakan langkah ke id TC.
- P-2: konteks browser kedua hanya membangun "sesi lain" untuk Expected c TC-GS-PROFILE-298 dan diobservasi sekali (langkah 10) sesudah kegagalan; pemicu spec tetap kegagalan sisi server, bukan interaksi antar konteks, sehingga spec tetap kelas b.
- Spec ini 40 langkah, di atas smell 35 langkah. Alasan: ketiga TC satu kelas harness (kegagalan sisi server) dengan dua akun (Pre-setup #7 dan #9) dan tiga pemicu kegagalan sejenis; tambahan langkah berasal dari sesi web kedua untuk Expected c TC-GS-PROFILE-298 (langkah 1, 2, 10, 11) dan baseline File Manager untuk Expected c TC-GS-PROFILE-299 (langkah 19 sampai 22). Memecahnya tidak mengurangi langkah per TC dan mengulang penyiapan pemicu.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 dan 2 (login di konteks browser kedua sebagai sesi lain dan membuka My Profile di sana, prasyarat butir Expected c TC-GS-PROFILE-298), langkah 11 (menutup konteks kedua dan menghapus sesi loginnya), langkah 3, 12, 23, 28, 35, dan 40 (mengaktifkan atau menonaktifkan pemicu), langkah 8 (login API sebagai observasi butir Expected b), langkah 13 dan 29 (dismiss toast Error), langkah 14 sampai 16 (menutup modal terisi deterministik), langkah 17 dan 18 (Step ganti akun; langkah 19 langsung membuka File Manager), langkah 19 sampai 22 (membuka File Manager, Search, mencatat baseline, kembali ke My Profile), langkah 30 dan 32 (membuka File Manager dan Search untuk menemukan berkas target), dan langkah 34 (kembali ke My Profile).
- Langkah 31 adalah pembanding positif (tabel sudah termuat) sebelum asersi selisih nol di langkah 33; baseline jumlah baris hasil Search dicatat di langkah 21 sebelum aksi Edit Photo karena `valid-photo.png` juga diunggah sukses oleh spec lain (TC-GS-PROFILE-299 Expected c). Urutan TC (langkah 3 TC-GS-PROFILE-299 membuka File Manager) tidak berubah.
- Temuan untuk QA:
  - TC-GS-PROFILE-298 Expected c "Sesi lain tetap aktif" tidak punya sesi lain di Precondition; spec membuat sesi web akun Pre-setup #7 di konteks browser kedua (langkah 1 dan 2) dan memeriksanya lewat observasi di konteks itu (langkah 10).
  - TC-GS-PROFILE-299 Expected c memakai nama berkas `valid-photo.png` yang juga hasil unggah sukses TC lain (tanpa baseline di TC); spec membandingkan jumlah baris hasil Search dengan baseline sebelum aksi (selisih nol), bukan hasil kosong.
  - TC-GS-PROFILE-299 Expected c hanya menyebut tidak ada `valid-photo.png` di tabel File Manager; "tidak ada file yatim" pada Title hanya diasersi sebatas itu.
  - TC-GS-PROFILE-299 dan 300 Post Condition "Foto aktif tidak berubah" tidak punya langkah observasi sendiri selain Avatar; diasersi hanya lewat Avatar.
  - TC-GS-PROFILE-300 tidak menyatakan apakah dialog Remove Photo tertutup setelah toast Error; spec langsung mengasersi Avatar.
  - Mekanisme pemicu kegagalan sisi server tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim BE/FE tanpa endpoint karangan.
