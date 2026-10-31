---
id: TC-GS-PROFILE-E2E-038-edit-photo-ganti-resize-dan-toast
title: "Edit Photo: Ganti Foto, Resize Lebih dari 1 MB, Tepat 1 MB, dan Toast Baru Menggantikan Toast Lama"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-164
  - TC-GS-PROFILE-166
  - TC-GS-PROFILE-167
  - TC-GS-PROFILE-314
coverage:
  web: automated
---

# Edit Photo: Ganti Foto, Resize Lebih dari 1 MB, Tepat 1 MB, dan Toast Baru Menggantikan Toast Lama

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Pre-setup #10 (Fajar Nugroho, Total Control, tanpa foto; `Fixture.myProfile.accounts.noPhoto.email`, `Spectra.env.GS_PROFILE_NOPHOTO_PASSWORD`) untuk TC-GS-PROFILE-166 dan 167. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (Step ganti akun): Pre-setup #9 (Nadia Putri, Total Control, foto profil aktif `Fixture.myProfile.photo.nadiaActive`; `Fixture.myProfile.accounts.photo.email`, `Spectra.env.GS_PROFILE_PHOTO_PASSWORD`) untuk TC-GS-PROFILE-164 dan 314. TC-GS-PROFILE-314 diakhiri Delete Photo sehingga ditaruh paling akhir.
- File uji (Pre-setup #17): `Fixture.myProfile.files.largePhoto3mb` (`large-photo-3mb.jpg`, 3 MB), `Fixture.myProfile.files.exact1mb` (`exactly-1mb.png`, 1.048.576 byte), dan `Fixture.myProfile.files.validPng` (`valid-photo.png`), dipilih lewat kemampuan penanganan file picker native (disediakan tim FE).
- Kemampuan teknis disediakan tim BE/FE (TC tidak memberi cara cek, lihat Temuan untuk QA): (a) fixture BE untuk mengosongkan foto akun Pre-setup #10 dan memasang kembali foto aktif `nadia-photo.jpg` pada akun Pre-setup #9; (b) pembacaan ukuran berkas foto yang tersimpan pada akun yang diuji untuk butir Expected c TC-GS-PROFILE-166 dan 167.
- State global dan pemulihan: foto #10 dan #9 berubah; spec memulihkan foto #10 ke tanpa foto dan foto #9 ke `nadia-photo.jpg` di akhir tiap blok, dan hook `after` suite memulihkan foto #9/#10 sebagai cadangan.
- Jeda nyata 5 detik (pilihan spec, lebih panjang dari auto-hide toast sukses 4 detik menurut TL-11 TC) dipakai agar toast kasus sebelumnya hilang sebelum toast berikutnya diasersi.
- Hook suite berikut berlaku; lihat `suite.md`:
  - Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
  - Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
  - Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
  - Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
  - Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Suite serial: `parallel: false`.

## Test Steps

### TC-GS-PROFILE-166: File lebih dari 1 MB di-resize (Pre-setup #10)

1. Hover Avatar lalu klik [Edit]
2. Pilih file `Fixture.myProfile.files.largePhoto3mb`
3. Verifikasi toast sukses "Success, photo has been updated."
4. Verifikasi tidak ada pesan error ukuran
5. Verifikasi file yang tersimpan berukuran tidak lebih dari 1 MB
6. Kosongkan foto profil akun Pre-setup #10 lewat fixture BE, lalu muat ulang My Profile

### TC-GS-PROFILE-167: File tepat 1 MB (Pre-setup #10)

7. Tunggu toast lama hilang otomatis
8. Hover Avatar lalu klik [Edit]
9. Pilih file `Fixture.myProfile.files.exact1mb`
10. Verifikasi toast sukses "Success, photo has been updated."
11. Verifikasi tidak ada pesan error
12. Verifikasi file yang tersimpan tetap berukuran 1.048.576 byte (tidak di-resize)
13. Kosongkan foto profil akun Pre-setup #10 lewat fixture BE

### Ganti akun ke Pre-setup #9

14. Logout
15. Login dengan `Fixture.myProfile.accounts.photo.email` dan `Spectra.env.GS_PROFILE_PHOTO_PASSWORD`
16. Buka My Profile dari account menu navbar

### TC-GS-PROFILE-164: Edit Photo menggantikan foto yang ada (Pre-setup #9)

17. Hover Avatar lalu klik [Edit]
18. Pilih file `Fixture.myProfile.files.validPng`
19. Verifikasi toast sukses "Success, photo has been updated."
20. Verifikasi Avatar menampilkan `Fixture.myProfile.files.validPng`
21. Pasang kembali foto aktif `Fixture.myProfile.photo.nadiaActive` pada akun Pre-setup #9 lewat fixture BE, lalu muat ulang My Profile

### TC-GS-PROFILE-314: Toast baru menggantikan toast lama (Pre-setup #9)

22. Tunggu toast lama hilang otomatis
23. Hover Avatar lalu klik [Edit]
24. Pilih file `Fixture.myProfile.files.validPng`
25. Sebelum toast hilang, hover Avatar lalu klik [Delete]
26. Klik [Remove]
27. Verifikasi toast "Success, photo has been removed." menggantikan toast "Success, photo has been updated." (toast "Success, photo has been updated." tidak lagi tampil)
28. Verifikasi hanya satu toast tampil
29. Verifikasi toast tampil di kanan bawah
30. Pasang kembali foto aktif `Fixture.myProfile.photo.nadiaActive` pada akun Pre-setup #9 lewat fixture BE

## Notes

- Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-164, 166, 167, 314). Tidak ada TC hanya-BE.
- Subjudul `###` memetakan langkah ke id TC. Blok per akun karena ada Step ganti akun eksplisit dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3, pemisah nyata butir b); semua TC satu topik (Edit Photo berhasil).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 6, 13, 21, dan 30 (pemulihan foto lewat fixture BE; langkah 13 dan 30 juga memulihkan state akhir blok), langkah 7 dan 22 (menunggu toast lama hilang otomatis), langkah 14 sampai 16 (Step ganti akun).
- Urutan Expected TC-GS-PROFILE-166 dan 167: toast sukses (langkah 3 dan 10) ditaruh sebelum "tidak ada pesan error" karena toast sukses menjadi anchor positif asersi absence (bagian 8b butir 2); perubahan urutan ini dicatat sesuai S-05.
- TC-GS-PROFILE-314 ditaruh paling akhir karena diakhiri Delete Photo (prinsip 5).
- Temuan untuk QA:
  - TC-GS-PROFILE-166 dan 167 Expected c (ukuran berkas tersimpan) tidak memberi cara cek; spec memakai kemampuan baca ukuran berkas yang disediakan tim BE/FE (S-11).
  - Post Condition TC-GS-PROFILE-164 ("`nadia-photo.jpg` tidak lagi aktif") dan 166 ("Foto aktif tersimpan ≤ 1 MB") tidak punya langkah observasi sendiri; diasersi hanya sebatas butir Expected.
  - TC-GS-PROFILE-314 tidak menyebut jendela waktu untuk "Sebelum toast hilang"; toast sukses hilang otomatis dalam 4 detik (TL-11), sehingga aksi Delete di langkah 25 sampai 26 harus selesai dalam jendela itu. Cara menjamin jendela (mis. menahan jam browser) ditetapkan saat script.
  - Precondition TC-GS-PROFILE-314 dan 164 menulis "Login sbg Role: Total Control" bersama akun Pre-setup #9; spec memakai akun Pre-setup #9 sebagai sumber.
