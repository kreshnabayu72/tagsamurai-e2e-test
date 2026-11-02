---
id: TC-GS-PROFILE-E2E-050-pencatatan-change-password-dan-password-tidak-bocor
title: "Pencatatan Change Password: Note Sukses dan Salah, Tanpa Nilai Password"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-228
  - TC-GS-PROFILE-230
  - TC-GS-PROFILE-231
  - TC-GS-PROFILE-282
coverage:
  web: automated
---

# Pencatatan Change Password: Note Sukses dan Salah, Tanpa Nilai Password

## Prerequisites

- Mode: FE+BE.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`, `Spectra.env.GS_PROFILE_PWD12H_PASSWORD`, `Spectra.env.GS_PROFILE_SUSPENDED_PASSWORD`), counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Akun aktor pertama spec: Pre-setup #7 (Maya Anggraini, Total Control, password aktif `Spectra.env.GS_PROFILE_PWD_PASSWORD`, Time Format 24 jam, counter 0) `passwordProfile_automated_{namaCompany}@qwertysystem.net`, login di hook `before` spec ini dengan `Spectra.env.GS_PROFILE_PWD_PASSWORD`. Pembaca log: admin Pre-setup #6 (Hendra Wijaya) `adminActor_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.GS_PROFILE_ADMIN_PASSWORD`, login lewat UI pada langkah ganti akun.
- Env var: `GS_PROFILE_PWD_PASSWORD` (Current Password benar), `PROFILE_PASSWORD_NEW` (Data Dinamis #3), `GS_PROFILE_ADMIN_PASSWORD`.
- Input uji Current Password salah `Wr0ngPass!` ditulis literal seperti di TC: itu masukan uji yang ditolak server, bukan kredensial akun.
- Kemampuan teknis: kontrol show/hide password pada modal Change Password (tidak diaktifkan di spec ini); membaca jumlah baris User Log Detail User, Tab Changelog, Tab System Log, dan Activity Log > Session sebelum aksi (baseline, S-12; disediakan tim FE/BE); fixture BE memulihkan password.
- Pemulihan (R-08): langkah 29 memulihkan password Maya Anggraini ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`) dan counter ke 0 lewat fixture BE; hook `after` suite memulihkan state yang sama bila spec gagal di tengah.
- State global yang diubah: password dan counter Pre-setup #7. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-PROFILE-231 dan TC-GS-PROFILE-282: Current Password salah, masked, dan Note

1. Catat baseline lewat kemampuan baca: jumlah baris Activity `Change Password` per Note (`Incorrect current password`, `Password changed`) pada Tab User Log Detail Maya Anggraini dan Activity Log > Session, serta jumlah baris Tab Changelog dan Tab System Log Detail Maya Anggraini
2. Klik `[Change Password]`
3. Isi Current Password `Wr0ngPass!`, New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`
4. Verifikasi Current Password, New Password, dan Confirm New Password tersamarkan selama kontrol show/hide tidak diaktifkan
5. Klik `[Save]`

### TC-GS-PROFILE-230 dan TC-GS-PROFILE-228: Change Password berhasil

6. Ganti isi Current Password dengan `Spectra.env.GS_PROFILE_PWD_PASSWORD`
7. Klik `[Save]`
8. Tunggu aksi selesai
9. Logout
10. Login sebagai admin Hendra Wijaya (Pre-setup #6)
11. Buka Global Settings > User > Detail Maya Anggraini > Tab User Log

### Pembacaan User Log dan Activity Log > Session

12. Verifikasi Tab User Log memuat baris baru: Activity `Change Password`, Status `Failed`, Note `Incorrect current password` (jumlah baris dengan Note itu bertambah tepat satu dibanding baseline)
13. Verifikasi Note baris `Incorrect current password` hanya berisi `Incorrect current password`
14. Verifikasi Note baris `Incorrect current password` tidak memuat `Wr0ngPass!` maupun `Spectra.env.PROFILE_PASSWORD_NEW`
15. Verifikasi Tab User Log memuat baris baru: Activity `Change Password`, Status `Success`, Note `Password changed` (jumlah baris dengan Note itu bertambah tepat satu dibanding baseline)
16. Buka Global Settings > Activity Log > Session
17. Verifikasi Activity Log > Session memuat baris baru untuk Maya Anggraini: Activity `Change Password`, Status `Failed`, Note `Incorrect current password`
18. Verifikasi Activity Log > Session memuat baris baru untuk Maya Anggraini: Activity `Change Password`, Status `Success`, Note `Password changed`

### TC-GS-PROFILE-228: Nilai password tidak tercatat

19. Buka Global Settings > User > Detail Maya Anggraini > Tab Changelog
20. Verifikasi Tab Changelog memuat sedikitnya satu baris pembanding
21. Verifikasi Tab Changelog tidak memuat baris password
22. Buka Tab System Log
23. Verifikasi Tab System Log memuat sedikitnya satu baris pembanding
24. Verifikasi Tab System Log tidak memuat baris password
25. Buka Global Settings > Activity Log
26. Verifikasi Activity Log memuat sedikitnya satu baris pembanding
27. Verifikasi Activity Log tidak memuat baris password
28. Verifikasi nilai password (`Spectra.env.GS_PROFILE_PWD_PASSWORD` dan `Spectra.env.PROFILE_PASSWORD_NEW` sebagai teks biasa, serta nilai hash password) tidak ada di isi Tab Changelog, Tab System Log, dan Activity Log

### Pemulihan

29. Pulihkan password Maya Anggraini ke password awal (`Spectra.env.GS_PROFILE_PWD_PASSWORD`) dan counter Change Password ke 0 lewat fixture BE

## Notes

- Mode: FE+BE. Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pembagian TC: TC-GS-PROFILE-231 dan TC-GS-PROFILE-282 memakai isian yang sama (Current `Wr0ngPass!`) sehingga satu aksi Save salah (langkah 2 sampai 5) melayani keduanya; TC-GS-PROFILE-230 dan TC-GS-PROFILE-228 memakai satu aksi Change Password berhasil (langkah 6 dan 7). Urutan salah lebih dulu, lalu berhasil, supaya counter 0 menghasilkan percobaan ke-1 (TC-GS-PROFILE-231).
- Modal Change Password tetap terbuka dengan isian saat penolakan Current Password salah (PRD My Profile), sehingga langkah 6 hanya mengganti Current Password.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 8 (tunggu aksi selesai sebelum ganti akun), 29 (pemulihan password dan counter).
- Asersi tambahan di luar Expected TC (S-03): langkah 20, 23, dan 26 adalah pembanding (anchor) untuk absence baris password (8b butir 2).
- Temuan untuk QA:
  - TC-GS-PROFILE-228 Expected (d) menyebut "nilai password (plaintext maupun hash)" tanpa cara mengamati hash; spec memeriksa teks plaintext password lama dan baru serta ketiadaan baris password.
  - TC-GS-PROFILE-228 Expected (a) sampai (c) "tidak memuat baris password" tidak menyebut Field yang dicari; spec mengasersi tidak ada baris yang berkaitan dengan password.
  - TC-GS-PROFILE-230 dan 231 menyebut "Activity Log > Session" sedangkan TC-GS-PROFILE-228 menyebut "Activity Log" tanpa tab; spec memakai Activity Log (langkah 25) tanpa memilih tab untuk TC-GS-PROFILE-228.
  - TC-GS-PROFILE-282 Expected (b) "Note hanya `Incorrect current password`" tidak menyebut apakah ada Note lain pada baris yang sama; spec mengasersi isi Note baris itu.
