---
id: TC-GS-PROFILE-E2E-059-storage-penuh-edit-photo-diblokir
title: "Storage Penuh atau Melebihi Kuota: Edit Photo Diblokir, Delete Photo Tetap Berhasil"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-PROFILE-283
  - TC-GS-PROFILE-284
  - TC-GS-PROFILE-285
  - TC-GS-PROFILE-288
  - TC-GS-PROFILE-289
  - TC-GS-PROFILE-290
coverage:
  web: automated
---

# Storage Penuh atau Melebihi Kuota: Edit Photo Diblokir, Delete Photo Tetap Berhasil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #11 `totalControlStorageFull_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.GS_PROFILE_STORAGEFULL_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Data Pre-setup #11: Client Storage penuh (kuota 50.0 GB, usage 50.0 GB). Varian untuk spec ini: usage 51.2 GB (TC-284); pemilik akun Fajar Nugroho tanpa foto (TC-283, TC-284, TC-289); pemilik akun Nadia Putri dengan foto aktif `nadia-photo.jpg` (TC-285, TC-288, TC-290). File uji Pre-setup #17: `valid-photo.png`, `document.pdf`.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE kuota dan ledger Storage Client (menetapkan usage 50.0 GB atau 51.2 GB dengan kuota 50.0 GB); fixture BE yang menukar varian pemilik akun #11 (Fajar tanpa foto atau Nadia dengan foto aktif `nadia-photo.jpg`) dan memasang ulang foto; kemampuan memberikan file ke file chooser tanpa filter ekstensi picker (bypass file picker); kemampuan baca jumlah entri Recycle Bin File Manager milik pemilik akun untuk baseline (S-12).
- Jeda 5 detik pada asersi toast persisten adalah pilihan spec (lebih lama dari auto-hide toast sukses 4 detik), bukan nilai TC atau PRD.
- State global yang diubah: usage dan kuota Storage Client #11, varian pemilik dan foto akun #11. Dipulihkan oleh langkah pemulihan di akhir spec dan oleh hook `after` suite. Suite berjalan serial (`parallel: false`).
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`, `Spectra.env.GS_PROFILE_PWD12H_PASSWORD`, `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`), counter ke 0, foto #9-#13 dan varian pemilik #11, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.

## Test Steps

### TC-GS-PROFILE-283: Storage penuh (usage sama dengan kuota), Edit Photo diblokir dengan toast Error persisten

1. Hover Avatar, klik [Edit]
2. Pilih file `valid-photo.png`
3. Verifikasi toast error `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` tampil
4. Tunggu 5 detik tanpa memuat ulang halaman
5. Verifikasi toast Error tidak hilang otomatis
6. Verifikasi Avatar tetap menampilkan inisial "FN"
7. Tutup toast Error

### TC-GS-PROFILE-284: Storage melebihi kuota, nilai pada toast memakai format Size

8. Fixture BE menetapkan usage Client 51.2 GB dengan kuota 50.0 GB hingga tersimpan
9. Hover Avatar, klik [Edit]
10. Pilih file `valid-photo.png`
11. Verifikasi toast error `Error, failed to upload photo. Storage is full (51.2 GB of 50.0 GB used).` tampil
12. Tutup toast Error, lalu fixture BE mengembalikan usage Client 50.0 GB dengan kuota 50.0 GB hingga tersimpan

### TC-GS-PROFILE-289: Ekstensi tidak valid saat Storage penuh, penolakan format didahulukan

13. Hover Avatar, klik [Edit], berikan file `document.pdf` ke file chooser tanpa filter ekstensi (bypass file picker)
14. Verifikasi toast error `Error, failed to update photo.` tampil
15. Verifikasi tidak ada toast `Storage is full` yang tampil
16. Verifikasi Avatar tetap menampilkan inisial "FN" (foto tidak berubah)
17. Tutup toast Error

### TC-GS-PROFILE-290: Overlay [Edit] dan [Delete] tidak Disabled saat Storage penuh

18. Fixture BE menyetel akun Pre-setup #11 ke varian pemilik Nadia Putri dengan foto aktif `nadia-photo.jpg` (usage 50.0 GB, kuota 50.0 GB) hingga tersimpan, lalu muat ulang halaman My Profile
19. Catat jumlah entri Recycle Bin File Manager milik Nadia Putri sebagai baseline B0 (kemampuan baca)
20. Hover Avatar
21. Verifikasi tombol [Edit] dan [Delete] tampil dan Enabled

### TC-GS-PROFILE-285: Storage penuh, foto aktif dan foto lama tidak berubah dan tidak ada soft-delete

22. Klik [Edit]
23. Pilih file `valid-photo.png`
24. Tunggu aksi selesai: toast error Storage penuh tampil
25. Verifikasi Avatar tetap menampilkan foto aktif `nadia-photo.jpg`
26. Tutup toast Error, lalu buka File Manager > Recycle Bin
27. Verifikasi jumlah entri Recycle Bin milik Nadia Putri sama dengan baseline B0 (tidak ada entri baru dari aksi itu)
28. Kembali ke My Profile lewat account menu navbar > My Profile

### TC-GS-PROFILE-288: Storage penuh, Delete Photo tetap berhasil tanpa cek Storage

29. Hover Avatar, klik [Delete], klik [Remove]
30. Verifikasi toast sukses `Success, photo has been removed.` tampil
31. Verifikasi Avatar menampilkan inisial "NP"

### Pemulihan state

32. Fixture BE memasang kembali foto aktif `nadia-photo.jpg` dan mengembalikan akun Pre-setup #11 ke varian awal (usage 50.0 GB, kuota 50.0 GB)

## Notes

- Pembagian TC: TC-GS-PROFILE-283, 284, 289 memakai varian pemilik Fajar Nugroho (tanpa foto); TC-GS-PROFILE-290, 285, 288 memakai varian pemilik Nadia Putri (foto aktif). Langkah 18 menukar varian dan memuat ulang halaman.
- Urutan: TC-GS-PROFILE-290 sebelum TC-GS-PROFILE-285 dan TC-GS-PROFILE-288 karena overlay diamati sebelum aksi; TC-GS-PROFILE-288 (menghapus foto) paling akhir (prinsip 5).
- Langkah penghubung (S-03): langkah 7, 12, 17 dan 26 menutup toast Error; langkah 4 adalah jeda 5 detik; langkah 24 menunggu aksi selesai; langkah 28 kembali dari File Manager; langkah 19 mencatat baseline Recycle Bin (S-12); langkah 32 memulihkan state.
- P-5 (butir b): TC-GS-PROFILE-289 adalah satu TC objek-uji ringan kelas a (pemicu bypass file picker) pada permukaan yang sama dengan blokir Storage penuh (Edit Photo ditolak saat Storage penuh); tanpa harness eksternal dan tanpa state berat sendiri.
- Temuan untuk QA:
  - Pre-setup #11 satu email akun tetapi TC menyebut dua pemilik berbeda (Fajar Nugroho tanpa foto untuk TC-283; Nadia Putri dengan foto untuk TC-285, 288, 290). Spec menukar varian lewat fixture BE (langkah 18).
  - TC-GS-PROFILE-289 tidak menyebut pemilik akun #11 yang dipakai; spec memakai varian Fajar Nugroho (tanpa foto), konsisten dengan Avatar inisial "FN".
  - "Bypass file picker" pada TC-GS-PROFILE-289 tidak menyebut mekanisme; spec memakai pemberian file ke file chooser tanpa filter ekstensi sehingga validasi FE tetap dilewati dan toast tetap diasersi.
  - Post Condition TC-GS-PROFILE-283 ("tidak ada file baru tersimpan") tidak punya langkah observasi sehingga tidak diasersi.
  - Expected TC-GS-PROFILE-285 tidak menyebut toast Storage penuh; spec hanya menunggu aksi selesai (langkah 24) tanpa asersi toast.
