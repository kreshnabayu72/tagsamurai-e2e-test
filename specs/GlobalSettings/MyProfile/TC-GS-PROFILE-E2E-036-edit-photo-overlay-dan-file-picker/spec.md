---
id: TC-GS-PROFILE-E2E-036-edit-photo-overlay-dan-file-picker
title: "Edit Photo: Hover Overlay, Edit Langsung dari Overlay, Filter File Picker, dan Batal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-157
  - TC-GS-PROFILE-158
  - TC-GS-PROFILE-159
  - TC-GS-PROFILE-160
  - TC-GS-PROFILE-165
coverage:
  web: automated
---

# Edit Photo: Hover Overlay, Edit Langsung dari Overlay, Filter File Picker, dan Batal

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Pre-setup #9 (Nadia Putri, Total Control, `Fixture.myProfile.accounts.photo.email`, `Spectra.env.GS_PROFILE_PHOTO_PASSWORD`; foto profil aktif `Fixture.myProfile.photo.nadiaActive`) untuk TC-GS-PROFILE-157 dan 165. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (Step ganti akun): Pre-setup #10 (Fajar Nugroho, Total Control, tanpa foto, `Fixture.myProfile.accounts.noPhoto.email`, `Spectra.env.GS_PROFILE_NOPHOTO_PASSWORD`) untuk TC-GS-PROFILE-158, 159, dan 160.
- Kemampuan teknis: penanganan file picker native (membuka, mengamati atribut `accept` input file, dan menutup tanpa memilih file), disediakan tim FE. Tidak ada file yang dipilih sehingga file Pre-setup #17 tidak dipakai.
- State global: spec ini tidak mengubah foto, data, atau state global. Foto #9 dan #10 dipulihkan hook `after` suite sebagai cadangan.
- Hook suite berikut berlaku; lihat `suite.md`:
  - Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
  - Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
  - Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
  - Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
  - Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke password awal masing-masing (`Spectra.env.GS_PROFILE_PWD_PASSWORD`, `Spectra.env.GS_PROFILE_PWD12H_PASSWORD`, `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`), counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Suite serial: `parallel: false`.

## Test Steps

### TC-GS-PROFILE-157: Overlay Avatar dengan foto (Pre-setup #9)

1. Hover Avatar di Header
2. Verifikasi overlay pada Avatar menampilkan tombol [Edit] dan [Delete]

### TC-GS-PROFILE-165: Batal memilih file (Pre-setup #9)

3. Hover Avatar lalu klik [Edit]
4. Tutup file picker tanpa memilih file
5. Verifikasi foto `Fixture.myProfile.photo.nadiaActive` tidak berubah (Avatar tetap menampilkan foto itu)
6. Verifikasi tidak ada toast

### Ganti akun ke Pre-setup #10

7. Logout
8. Login dengan `Fixture.myProfile.accounts.noPhoto.email` dan `Spectra.env.GS_PROFILE_NOPHOTO_PASSWORD`
9. Buka My Profile dari account menu navbar

### TC-GS-PROFILE-158: Overlay Avatar tanpa foto (Pre-setup #10)

10. Hover Avatar di Header
11. Verifikasi overlay pada Avatar menampilkan tombol [Edit] saja
12. Verifikasi tidak ada tombol [Delete]

### TC-GS-PROFILE-159: Edit langsung dari overlay (Pre-setup #10)

13. Hover Avatar lalu klik [Edit]
14. Verifikasi file picker terbuka langsung
15. Verifikasi tidak ada modal atau form Edit yang terbuka

### TC-GS-PROFILE-160: Filter file picker (Pre-setup #10)

16. Verifikasi atribut accept pada input file hanya menerima ekstensi PNG, JPG, dan JPEG
17. Tutup file picker tanpa memilih file

## Notes

- Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-157, 158, 159, 160, 165). Tidak ada TC hanya-BE.
- Subjudul `###` memetakan langkah ke id TC. Blok per akun karena ada Step ganti akun eksplisit dan bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3, pemisah nyata butir b); semua TC satu topik (Edit Photo, tanpa submit file).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 7 sampai 9 (Step ganti akun) dan langkah 17 (menutup file picker agar akhir spec bersih).
- TC-GS-PROFILE-159 dan 160 memakai satu pembukaan file picker (langkah 13); langkah 1 TC-GS-PROFILE-160 dipenuhi oleh langkah 13, sedangkan langkah 2 TC (periksa atribut `accept`) adalah langkah 16.
- Temuan untuk QA:
  - TC-GS-PROFILE-165 Expected b "Tidak ada toast" adalah asersi absence yang memakai butir Expected a (Avatar tetap menampilkan foto) sebagai anchor; spec absence terpisah tidak diperlukan karena TC bukan asersi log.
  - TC-GS-PROFILE-160 hanya menyebut "atribut accept"; nilai persis atribut (mis. daftar MIME atau ekstensi) tidak ditulis TC, sehingga asersi mengikuti kalimat Expected.
