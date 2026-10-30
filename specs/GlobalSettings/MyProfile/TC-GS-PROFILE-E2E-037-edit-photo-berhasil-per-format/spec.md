---
id: TC-GS-PROFILE-E2E-037-edit-photo-berhasil-per-format
title: "Edit Photo: Berhasil dengan PNG, JPG, dan JPEG"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-161
  - TC-GS-PROFILE-162
  - TC-GS-PROFILE-163
coverage:
  web: automated
---

# Edit Photo: Berhasil dengan PNG, JPG, dan JPEG

## Prerequisites

- Mode: FE+BE
- Akun aktor: Pre-setup #10 (Fajar Nugroho, Total Control, tanpa foto, tanpa Employee ID, tanpa TAG; inisial Avatar "FN"; `Fixture.myProfile.accounts.noPhoto.email`, `Spectra.env.GS_PROFILE_NOPHOTO_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- File uji (Pre-setup #17): `Fixture.myProfile.files.validPng`, `Fixture.myProfile.files.validJpg`, dan `Fixture.myProfile.files.validJpeg`, dipilih lewat kemampuan penanganan file picker native (disediakan tim FE).
- Kemampuan teknis disediakan tim BE/FE: fixture BE yang mengosongkan foto profil akun Pre-setup #10 (kembali ke tanpa foto) antar kasus, karena Data Dinamis #1 dipulihkan ke Pre-setup sebelum tiap TC.
- State global dan pemulihan: foto profil #10 berubah tiga kali; spec mengosongkannya kembali di akhir tiap kasus (langkah pemulihan) dan hook `after` suite memulihkannya sebagai cadangan.
- Jeda nyata 5 detik (pilihan spec, lebih panjang dari auto-hide toast sukses 4 detik menurut TL-11 TC) dipakai agar toast kasus sebelumnya hilang sebelum toast berikutnya diasersi.
- Hook suite berikut berlaku; lihat `suite.md`:
  - Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
  - Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
  - Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
  - Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
  - Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Suite serial: `parallel: false`.

## Test Steps

### TC-GS-PROFILE-161: Edit Photo dengan PNG

1. Hover Avatar lalu klik [Edit]
2. Pilih file `Fixture.myProfile.files.validPng`
3. Verifikasi toast sukses "Success, photo has been updated."
4. Verifikasi Avatar menampilkan foto baru menggantikan inisial "FN"
5. Hover Avatar di Header
6. Verifikasi overlay hover kini menampilkan [Edit] dan [Delete]
7. Kosongkan foto profil akun Pre-setup #10 lewat fixture BE, lalu muat ulang My Profile

### TC-GS-PROFILE-162: Edit Photo dengan JPG

8. Tunggu toast lama hilang otomatis
9. Hover Avatar lalu klik [Edit]
10. Pilih file `Fixture.myProfile.files.validJpg`
11. Verifikasi toast sukses "Success, photo has been updated."
12. Verifikasi Avatar menampilkan foto baru menggantikan inisial "FN"
13. Hover Avatar di Header
14. Verifikasi overlay hover kini menampilkan [Edit] dan [Delete]
15. Kosongkan foto profil akun Pre-setup #10 lewat fixture BE, lalu muat ulang My Profile

### TC-GS-PROFILE-163: Edit Photo dengan JPEG

16. Tunggu toast lama hilang otomatis
17. Hover Avatar lalu klik [Edit]
18. Pilih file `Fixture.myProfile.files.validJpeg`
19. Verifikasi toast sukses "Success, photo has been updated."
20. Verifikasi Avatar menampilkan foto baru menggantikan inisial "FN"
21. Hover Avatar di Header
22. Verifikasi overlay hover kini menampilkan [Edit] dan [Delete]
23. Kosongkan foto profil akun Pre-setup #10 lewat fixture BE, lalu muat ulang My Profile

## Notes

- Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-161, 162, 163). Tidak ada TC hanya-BE. Satu akun dan satu topik; tiga format berurutan dengan pemulihan foto di antaranya.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 5, 13, dan 21 (hover Avatar agar overlay teramati pada Expected c), langkah 7, 15, dan 23 (pemulihan foto ke tanpa foto lewat fixture BE; langkah 23 juga memulihkan state akhir spec), langkah 8 dan 16 (menunggu toast lama hilang otomatis sebelum toast berikutnya diasersi).
- Temuan untuk QA:
  - Post Condition TC-GS-PROFILE-161, 162, dan 163 "Foto profil aktif Fajar Nugroho adalah file baru" tidak punya langkah observasi di TC; diasersi hanya lewat Avatar (butir Expected b).
  - Mekanisme pengosongan foto antar kasus tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai fixture BE yang disediakan tim BE/FE tanpa endpoint karangan.
