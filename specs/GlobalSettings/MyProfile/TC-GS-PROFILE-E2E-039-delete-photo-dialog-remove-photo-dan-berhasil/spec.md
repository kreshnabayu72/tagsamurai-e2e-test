---
id: TC-GS-PROFILE-E2E-039-delete-photo-dialog-remove-photo-dan-berhasil
title: "Delete Photo: Dialog Remove Photo (Cancel, Esc, Backdrop), Berhasil, dan Klik Ganda Remove"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-170
  - TC-GS-PROFILE-171
  - TC-GS-PROFILE-172
  - TC-GS-PROFILE-173
  - TC-GS-PROFILE-174
  - TC-GS-PROFILE-177
coverage:
  web: automated
---

# Delete Photo: Dialog Remove Photo (Cancel, Esc, Backdrop), Berhasil, dan Klik Ganda Remove

## Prerequisites

- Mode: FE+BE
- Akun aktor: Pre-setup #9 (Nadia Putri, Total Control, foto profil aktif `Fixture.myProfile.photo.nadiaActive`, inisial Avatar "NP"; `Fixture.myProfile.accounts.photo.email`, `Spectra.env.GS_PROFILE_PHOTO_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Kemampuan teknis disediakan tim BE/FE: (a) fixture BE yang memasang kembali foto aktif `nadia-photo.jpg` pada akun Pre-setup #9 sebelum TC-GS-PROFILE-177 (TC-GS-PROFILE-174 sudah menghapusnya); (b) pengamat jaringan yang menghitung jumlah request Delete Photo yang terkirim (TC-GS-PROFILE-177).
- State global dan pemulihan: foto #9 dihapus dua kali; spec memasang kembali foto di akhir (langkah pemulihan) dan hook `after` suite memulihkan foto #9 sebagai cadangan. Aksi menghapus foto ditaruh di akhir spec (prinsip 5).
- Jeda nyata: tidak ada. Langkah "Tunggu toast lama hilang otomatis" menunggu toast sukses (auto-hide 4 detik menurut TL-11 TC) hilang.
- Hook suite berikut berlaku; lihat `suite.md`:
  - Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
  - Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
  - Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
  - Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
  - Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke password awal masing-masing (`Spectra.env.GS_PROFILE_PWD_PASSWORD`, `Spectra.env.GS_PROFILE_PWD12H_PASSWORD`, `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`), counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Suite serial: `parallel: false`.

## Test Steps

### TC-GS-PROFILE-170: Screening dialog Remove Photo

1. Hover Avatar lalu klik [Delete]
2. Verifikasi Header dialog: judul "Remove Photo"
3. Verifikasi Body dialog: bullet "Nadia Putri" lalu teks "This will remove this user's profile photo. Are you sure you want to remove it?"
4. Verifikasi Footer dialog: tombol [Cancel] dan [Remove]

### TC-GS-PROFILE-171: [Cancel] menutup dialog

5. Klik [Cancel]
6. Verifikasi dialog tertutup
7. Verifikasi Avatar tetap menampilkan `Fixture.myProfile.photo.nadiaActive`
8. Verifikasi tidak ada toast

### TC-GS-PROFILE-172: Esc setara [Cancel]

9. Hover Avatar lalu klik [Delete]
10. Tekan Esc
11. Verifikasi dialog tertutup
12. Verifikasi Avatar tetap menampilkan `Fixture.myProfile.photo.nadiaActive`

### TC-GS-PROFILE-173: Klik backdrop tidak menutup dialog

13. Hover Avatar lalu klik [Delete]
14. Klik area backdrop di luar dialog
15. Verifikasi dialog tetap terbuka

### TC-GS-PROFILE-174: Delete Photo berhasil

16. Klik [Remove] pada dialog yang masih terbuka dari TC-GS-PROFILE-173
17. Verifikasi toast sukses "Success, photo has been removed."
18. Verifikasi Avatar menampilkan inisial "NP"
19. Hover Avatar di Header
20. Verifikasi overlay hover kini hanya menampilkan [Edit]
21. Verifikasi pengguna tetap berada di My Profile dan tidak diarahkan ke halaman Login (sesi tetap aktif)

### TC-GS-PROFILE-177: Klik ganda [Remove]

22. Pasang kembali foto aktif `Fixture.myProfile.photo.nadiaActive` pada akun Pre-setup #9 lewat fixture BE, lalu muat ulang My Profile
23. Tunggu toast lama hilang otomatis
24. Hover Avatar lalu klik [Delete]
25. Klik [Remove] dua kali dengan cepat
26. Verifikasi hanya satu request Delete Photo terkirim
27. Verifikasi hanya satu toast "Success, photo has been removed." tampil
28. Pasang kembali foto aktif `Fixture.myProfile.photo.nadiaActive` pada akun Pre-setup #9 lewat fixture BE

## Notes

- Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md` (TC-GS-PROFILE-170, 171, 172, 173, 174, 177). Tidak ada TC hanya-BE.
- Subjudul `###` memetakan langkah ke id TC. Urutan: screening (170), pembatalan (171 sampai 173), lalu aksi yang menghapus foto di akhir (174 dan 177; prinsip 5).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 19 (hover agar overlay teramati pada Expected c TC-GS-PROFILE-174), langkah 22 dan 28 (memasang kembali foto lewat fixture BE; langkah 28 memulihkan state akhir), langkah 23 (menunggu toast lama hilang otomatis sebelum hitungan toast TC-GS-PROFILE-177).
- TC-GS-PROFILE-174 memakai dialog yang masih terbuka dari TC-GS-PROFILE-173 (langkah 1 dan 2 TC dipenuhi oleh langkah 13 dan 16), sehingga tidak ada pembukaan dialog tambahan.
- Temuan untuk QA:
  - Post Condition TC-GS-PROFILE-174 ("Foto profil aktif kosong; `nadia-photo.jpg` tidak lagi aktif") tidak punya langkah observasi sendiri; diasersi hanya lewat Avatar dan overlay (butir Expected).
  - TC-GS-PROFILE-177 tidak menyebut cara menghitung request Delete Photo; spec memakai pengamat jaringan yang disediakan tim BE/FE (S-11).
  - TC-GS-PROFILE-177 tidak menyatakan precondition ulang foto aktif setelah TC-GS-PROFILE-174 menghapusnya; spec memasang ulang lewat fixture BE.
