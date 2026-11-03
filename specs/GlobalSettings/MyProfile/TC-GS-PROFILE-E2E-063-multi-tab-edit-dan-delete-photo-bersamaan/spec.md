---
id: TC-GS-PROFILE-E2E-063-multi-tab-edit-dan-delete-photo-bersamaan
title: "Multi-Tab: Edit Photo dan Delete Photo Bersamaan di Dua Tab"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-PROFILE-301
  - TC-GS-PROFILE-302
  - TC-GS-PROFILE-311
coverage:
  web: automated
---

# Multi-Tab: Edit Photo dan Delete Photo Bersamaan di Dua Tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #9 (Nadia Putri) `photoProfile_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.GS_PROFILE_PHOTO_PASSWORD`), foto profil aktif `nadia-photo.jpg`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Konteks: dua tab pada sesi yang sama (kelas c); tab 1 adalah tab utama, tab 2 dibuka spec. File uji Pre-setup #17: `valid-photo.png`, `valid-photo.jpg`.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): menjalankan aksi di dua tab secara bersamaan; fixture BE yang memasang foto aktif `nadia-photo.jpg` untuk Nadia Putri; kemampuan baca jumlah entri Recycle Bin File Manager milik Nadia Putri (total dan per nama file) dan jumlah baris log `Field = Photo` di Changelog, System Log, dan Activity Log aktor, untuk baseline (S-12).
- State global yang diubah: foto profil aktif akun #9 dan isi Recycle Bin File Manager. Foto dipulihkan oleh fixture BE pada langkah 13 dan 22 dan oleh hook `after` suite (foto #9 ke keadaan awal). Suite berjalan serial (`parallel: false`).
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`, `Spectra.env.GS_PROFILE_PWD12H_PASSWORD`, `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`), counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.

## Test Steps

### TC-GS-PROFILE-301: Dua tab mengganti foto bersamaan, last-write-wins dan tiap foto tergantikan di-soft-delete

1. Catat baseline Recycle Bin File Manager milik Nadia Putri: total entri T0 dan jumlah entri bernama `nadia-photo.jpg` N0 (kemampuan baca)
2. Buka tab 2 pada sesi yang sama, lalu buka My Profile lewat account menu navbar > My Profile di tab 2
3. Di tab 1 hover Avatar, klik [Edit], pilih file `valid-photo.png`, dan di tab 2 hover Avatar, klik [Edit], pilih file `valid-photo.jpg`, kedua aksi dijalankan bersamaan
4. Tunggu aksi selesai di kedua tab
5. Di tab 1 muat ulang halaman My Profile
6. Verifikasi Avatar menampilkan salah satu dari `valid-photo.png` atau `valid-photo.jpg` (bukan `nadia-photo.jpg`)
7. Di tab 1 buka File Manager dan lihat tabel utama
8. Verifikasi tabel utama memuat tepat satu foto aktif milik Nadia Putri
9. Buka File Manager > Recycle Bin
10. Verifikasi Recycle Bin memuat entri `nadia-photo.jpg` baru (jumlah entri bernama `nadia-photo.jpg` menjadi N0 + 1)
11. Verifikasi Recycle Bin memuat foto yang tergantikan (total entri menjadi T0 + 2)
12. Verifikasi tidak ada foto yatim yang masih aktif: tidak ada entri Recycle Bin milik Nadia Putri yang juga tampil di tabel utama

### TC-GS-PROFILE-302: Delete Photo saat foto sudah dihapus dari tab lain, no-op sukses

13. Fixture BE memasang foto aktif `nadia-photo.jpg` untuk Nadia Putri hingga tersimpan, lalu buka My Profile di tab 1 dan muat ulang halaman di tab 2
14. Di tab 1 hover Avatar, klik [Delete], klik [Remove]
15. Tunggu aksi selesai di tab 1: toast sukses penghapusan tampil
16. Catat baseline kedua: total entri Recycle Bin milik Nadia Putri T1 dan jumlah baris log `Field = Photo` di Changelog, System Log, dan Activity Log aktor G1 (kemampuan baca)
17. Di tab 2 (masih menampilkan foto) hover Avatar, klik [Delete], klik [Remove]
18. Verifikasi tab 2 menampilkan toast sukses `Success, photo has been removed.`
19. Verifikasi Avatar di tab 2 menampilkan inisial "NP"
20. Verifikasi total entri Recycle Bin milik Nadia Putri tetap T1 (tidak ada soft-delete baru)
21. Verifikasi jumlah baris log `Field = Photo` tetap G1 (tidak ada baris log baru)

### TC-GS-PROFILE-311: Edit Photo dan Delete Photo bersamaan di dua tab, diserialisasi

22. Fixture BE memasang foto aktif `nadia-photo.jpg` untuk Nadia Putri hingga tersimpan, lalu catat jumlah entri Recycle Bin bernama `nadia-photo.jpg` sebagai baseline N1 (kemampuan baca)
23. Muat ulang halaman My Profile di tab 1 dan di tab 2
24. Di tab 1 klik [Edit] dan pilih file `valid-photo.png`, dan di tab 2 hover Avatar, klik [Delete], klik [Remove], kedua aksi dijalankan bersamaan
25. Tunggu aksi selesai di kedua tab
26. Di tab 1 buka File Manager > Recycle Bin
27. Verifikasi `nadia-photo.jpg` tampil sebagai tepat satu entri baru di Recycle Bin (jumlah entri bernama `nadia-photo.jpg` menjadi N1 + 1)
28. Buka tabel utama File Manager
29. Verifikasi tabel utama memuat paling banyak satu foto aktif milik Nadia Putri
30. Verifikasi tidak ada foto yatim yang masih aktif: tidak ada entri Recycle Bin milik Nadia Putri yang juga tampil di tabel utama

### Pemulihan state

31. Tutup tab 2

## Notes

- Urutan: TC-GS-PROFILE-301 (Edit bersamaan) dahulu, TC-GS-PROFILE-302 (Delete dua kali), lalu TC-GS-PROFILE-311; tiap blok memasang ulang foto aktif lewat fixture BE (langkah 13 dan 22) karena blok sebelumnya mengganti atau menghapusnya. Langkah 14 menghapus foto sehingga TC-GS-PROFILE-311 memakai pemasangan ulang.
- Langkah penghubung (S-03): langkah 2 membuka tab 2; langkah 5, 13 dan 23 memuat ulang tampilan tab; langkah 4, 15 dan 25 menunggu aksi selesai (bagian 8b butir 8); langkah 7, 9, 26 dan 28 membuka File Manager untuk memeriksa hasil; langkah 31 menutup tab 2 (S-09).
- P-1: asersi "tidak ada baris log baru" TC-GS-PROFILE-302 (langkah 21) tetap di spec ini karena konteksnya bergantung pada state yang baru dibangun langkah 14 (foto sudah dihapus dari tab lain); asersi memakai baseline G1 (S-12) dan toast sukses langkah 18 sebagai anchor. TC-GS-PROFILE-302 tidak ada di `sourceTc` spec absence.
- Temuan untuk QA:
  - TC-GS-PROFILE-302 menyebut "baris log baru" tanpa menyebut surface; spec memakai Changelog, System Log, dan Activity Log yang dicatat PRD My Profile bagian 8 untuk `Field = Photo`.
  - TC-GS-PROFILE-301 menyebut "foto yang tergantikan" tanpa nama file; spec mengasersi jumlah entri baru (N0 + 1 untuk `nadia-photo.jpg`, T0 + 2 total) dan bukan nama foto yang kalah.
  - TC-GS-PROFILE-301 dan TC-GS-PROFILE-311 tidak menyebut cara menjalankan dua aksi "pada saat yang sama"; spec meminta kemampuan aksi bersamaan di dua tab yang disediakan tim FE/BE.
