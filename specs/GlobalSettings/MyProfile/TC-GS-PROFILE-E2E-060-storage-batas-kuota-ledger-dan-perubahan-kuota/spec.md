---
id: TC-GS-PROFILE-E2E-060-storage-batas-kuota-ledger-dan-perubahan-kuota
title: "Storage di Bawah Kuota, Tanpa Kuota, Cek Ledger, dan Perubahan Kuota di License Allocation"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-PROFILE-286
  - TC-GS-PROFILE-287
  - TC-GS-PROFILE-291
  - TC-GS-PROFILE-252
  - TC-GS-PROFILE-253
coverage:
  web: automated
---

# Storage di Bawah Kuota, Tanpa Kuota, Cek Ledger, dan Perubahan Kuota di License Allocation

## Prerequisites

- Mode: FE+BE.
- Akun aktor (Total Control, ganti akun eksplisit antar blok): Pre-setup #12 `totalControlStorageNear_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.GS_PROFILE_STORAGENEAR_PASSWORD`, login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite), Pre-setup #13 `totalControlNoQuota_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.GS_PROFILE_NOQUOTA_PASSWORD`), dan Pre-setup #11 `totalControlStorageFull_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.GS_PROFILE_STORAGEFULL_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Data Pre-setup: #12 (usage 49.9 GB, kuota 50.0 GB), #13 (Client tanpa kuota Storage, belum pernah dialokasikan), #11 (usage 50.0 GB, kuota 50.0 GB). File uji Pre-setup #17: `valid-photo.png`.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE ledger Storage (menetapkan usage Client, termasuk menaikkannya sesaat sebelum simpan); pelaku perubahan kuota Storage lewat License Allocation (akun pelaku tidak disebut TC, PRD, atau LLD, lihat Temuan untuk QA); fixture BE yang memulihkan foto akun #12, #13, dan #11 ke keadaan awal; kemampuan menahan request unggahan foto lewat `Spectra.intercept()` lalu melepasnya (hanya menahan, bukan memaksa kegagalan).
- State global yang diubah: usage dan kuota Storage Client #12, #13, #11 serta foto akun-akun itu. Dipulihkan oleh langkah pemulihan antar blok dan oleh hook `after` suite. Suite berjalan serial (`parallel: false`).
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.

## Test Steps

### TC-GS-PROFILE-286: Usage tepat di bawah kuota, Edit Photo diterima (akun #12)

1. Hover Avatar, klik [Edit]
2. Pilih file `valid-photo.png`
3. Verifikasi toast sukses `Success, photo has been updated.` tampil
4. Fixture BE memulihkan foto akun #12 ke keadaan awal dan mengembalikan usage Client ke 49.9 GB hingga tersimpan, lalu muat ulang halaman My Profile

### TC-GS-PROFILE-291: Cek Storage memakai ledger saat file disimpan

5. Hover Avatar, klik [Edit]
6. Tahan request unggahan foto, lalu pilih file `valid-photo.png`
7. Fixture BE menaikkan ledger usage Client menjadi 50.0 GB hingga tersimpan
8. Lepas tahanan request unggahan foto
9. Verifikasi toast error `Error, failed to upload photo. Storage is full (50.0 GB of 50.0 GB used).` tampil
10. Fixture BE mengembalikan usage Client ke 49.9 GB hingga tersimpan

### TC-GS-PROFILE-253: Kuota diturunkan sama dengan usage, Edit Photo diblokir tanpa memuat ulang halaman

11. Pelaku perubahan kuota menurunkan kuota Storage Client #12 menjadi 49.9 GB lewat License Allocation hingga tersimpan
12. Hover Avatar, klik [Edit]
13. Pilih file `valid-photo.png`
14. Verifikasi toast error `Error, failed to upload photo. Storage is full (49.9 GB of 49.9 GB used).` tampil
15. Pelaku perubahan kuota mengembalikan kuota Storage Client #12 menjadi 50.0 GB lewat License Allocation hingga tersimpan

### TC-GS-PROFILE-287: Client tanpa kuota Storage, Edit Photo tidak diblokir (akun #13)

16. Ganti akun: klik Logout, lalu login sebagai Pre-setup #13 dengan `Spectra.env.GS_PROFILE_NOQUOTA_PASSWORD`
17. Buka My Profile lewat account menu navbar > My Profile
18. Hover Avatar, klik [Edit]
19. Pilih file `valid-photo.png`
20. Verifikasi toast sukses `Success, photo has been updated.` tampil
21. Fixture BE memulihkan foto akun #13 ke keadaan awal

### TC-GS-PROFILE-252: Kuota dinaikkan di License Allocation, Edit Photo yang sebelumnya diblokir kini diterima (akun #11)

22. Ganti akun: klik Logout, lalu login sebagai Pre-setup #11 dengan `Spectra.env.GS_PROFILE_STORAGEFULL_PASSWORD`
23. Buka My Profile lewat account menu navbar > My Profile
24. Pelaku perubahan kuota menaikkan kuota Storage Client #11 menjadi 100 GB lewat License Allocation hingga tersimpan
25. Hover Avatar, klik [Edit]
26. Pilih file `valid-photo.png`
27. Verifikasi toast sukses `Success, photo has been updated.` tampil

### Pemulihan state

28. Pelaku perubahan kuota mengembalikan kuota Storage Client #11 menjadi 50.0 GB, lalu fixture BE mengembalikan usage Client #11 ke 50.0 GB dan memulihkan foto akun #11 ke keadaan awal

## Notes

- Urutan akun: blok akun #12 (TC-GS-PROFILE-286, 291, 253), lalu #13 (TC-GS-PROFILE-287), lalu #11 (TC-GS-PROFILE-252). Ganti akun memakai Step eksplisit (langkah 16 dan 22) dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Langkah penghubung (S-03): langkah 4, 10, 15, 21 dan 28 memulihkan usage, kuota, atau foto antar blok (S-09); langkah 7 dan 8 menahan lalu melepas request unggahan (intercept dilepas segera, bukan kegagalan yang dipaksa); langkah 17 dan 23 membuka My Profile sesudah login.
- P-2: fixture BE ledger pada langkah 7 hanya memicu state yang diuji TC-GS-PROFILE-291 (usage naik sesaat sebelum simpan) dan bukan objek asersi.
- Temuan untuk QA:
  - TC-GS-PROFILE-252 dan TC-GS-PROFILE-253 menyebut "lewat License Allocation" tanpa menyebut akun pelaku perubahan kuota; spec menulisnya sebagai pelaku yang disediakan tim FE.
  - Pre-setup #12 dan #13 tidak menyebut keadaan foto awal; spec memulihkan foto "ke keadaan awal" lewat fixture BE.
  - TC-GS-PROFILE-253 berjenis Positive padahal Expected-nya toast error penolakan; spec mengikuti Expected.
