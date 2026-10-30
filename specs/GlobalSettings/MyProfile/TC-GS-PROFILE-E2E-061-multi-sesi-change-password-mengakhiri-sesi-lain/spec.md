---
id: TC-GS-PROFILE-E2E-061-multi-sesi-change-password-mengakhiri-sesi-lain
title: "Multi-Sesi: Change Password Mengakhiri Sesi Lain, Dialog Password Changed, dan Lock Lintas Sesi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-136
  - TC-GS-PROFILE-140
  - TC-GS-PROFILE-249
  - TC-GS-PROFILE-292
  - TC-GS-PROFILE-293
  - TC-GS-PROFILE-294
coverage:
  web: automated
---

# Multi-Sesi: Change Password Mengakhiri Sesi Lain, Dialog Password Changed, dan Lock Lintas Sesi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #7 (Maya Anggraini) `passwordProfile_automated_{namaCompany}@qwertysystem.net`, password aktif `Passw0rd!Old` (`Spectra.env.GS_PROFILE_PWD_PASSWORD`); password baru `N3wPassw0rd!` (Data Dinamis #3, `Spectra.env.PROFILE_PASSWORD_NEW`). Login sesi A di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Konteks: dua sesi web akun yang sama. Sesi A adalah konteks browser utama; sesi B adalah konteks browser kedua (kelas c). Environment mengizinkan dua sesi web bersamaan untuk akun #7. Konteks B ditutup dan sesi loginnya dihapus di akhir tiap blok (S-09).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE jam server (diset absolut 09:05) dan fixture BE lock Change Password tier 15 menit (terkunci sampai 09:15); fixture BE reset counter Change Password dan Login ke 0; fixture BE memulihkan password akun #7 ke `Passw0rd!Old`; kemampuan baca status sesi produk Fixed Asset sesi B (Expected TC-249). Pilihan spec (bukan nilai TC atau PRD): menunggu dialog `Password Changed` di sesi B sampai batas tunggu 2 menit setelah aksi (interval request atau heartbeat tidak disebut TC).
- State global yang diubah: jam server, lock dan counter Change Password akun #7, password akun #7. Dipulihkan oleh langkah pemulihan antar blok dan oleh hook `after` suite. Suite berjalan serial (`parallel: false`).
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Counter Change Password dan Login akun Pre-setup #7 dan #18 direset ke 0 di hook `beforeEach` suite; spec yang menguji counter mengaturnya sesudah hook; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 6.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.

## Test Steps

### TC-GS-PROFILE-136: Change Password terkunci tidak mengunci Login dan sesi yang berjalan

1. Fixture BE mengatur jam server ke 09:05 dan memasang lock tier 15 menit pada Change Password akun #7 hingga tersimpan
2. Buka konteks browser kedua (sesi B), login sebagai Pre-setup #7 dengan password benar `Spectra.env.GS_PROFILE_PWD_PASSWORD`
3. Verifikasi login di sesi B berhasil
4. Di sesi A klik menu General Settings pada sidebar
5. Verifikasi halaman General Settings termuat di sesi A

### TC-GS-PROFILE-140: Lock yang terjadi dari sesi lain terlihat saat modal dibuka di sesi ini

6. Di sesi B buka My Profile lewat account menu navbar > My Profile
7. Di sesi B klik [Change Password]
8. Verifikasi [Save] Disabled di sesi B
9. Di sesi B klik [Cancel], lalu tutup konteks sesi B dan hapus sesi loginnya
10. Fixture BE mereset counter Change Password dan Login akun #7 ke 0 dan memulihkan jam server ke waktu nyata

### TC-GS-PROFILE-292: Sesi lain menerima Dialog Password Changed pada request berikutnya

11. Di sesi A buka My Profile lewat account menu navbar > My Profile
12. Buka konteks browser kedua (sesi B), login sebagai Pre-setup #7, lalu buka My Profile lewat account menu navbar > My Profile
13. Di sesi A klik [Change Password]
14. Di sesi A isi Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD`, New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`, klik [Save]
15. Tunggu aksi selesai di sesi A: modal Change Password tertutup
16. Di sesi B pilih opsi lain pada Product Selector (aksi yang memicu request berikutnya) lalu tunggu hingga request atau heartbeat berikutnya terkirim
17. Verifikasi sesi B menampilkan dialog `Password Changed` dengan body `Your password has been changed. Please log in again.` dan tombol [OK]
18. Verifikasi dialog di sesi B bukan Dialog `Session Expired`

### TC-GS-PROFILE-293: Dialog Password Changed non-dismissable

19. Di sesi B tekan Esc
20. Di sesi B klik area backdrop
21. Verifikasi dialog `Password Changed` tetap tampil di sesi B

### TC-GS-PROFILE-294: Dialog Password Changed, [OK] mengarahkan ke halaman Login

22. Di sesi B klik [OK]
23. Verifikasi sesi B diarahkan ke halaman Login
24. Tutup konteks sesi B dan hapus sesi loginnya, lalu fixture BE memulihkan password akun #7 ke `Passw0rd!Old` dan mereset counter Change Password dan Login ke 0

### TC-GS-PROFILE-249: Change Password mengakhiri sesi lain dan sesi produk turunannya

25. Buka konteks browser kedua (sesi B), login sebagai Pre-setup #7 dengan password `Spectra.env.GS_PROFILE_PWD_PASSWORD`, lalu buka app Fixed Asset
26. Di sesi A klik [Change Password]
27. Di sesi A isi Current Password `Spectra.env.GS_PROFILE_PWD_PASSWORD`, New Password `Spectra.env.PROFILE_PASSWORD_NEW`, Confirm New Password `Spectra.env.PROFILE_PASSWORD_NEW`, klik [Save]
28. Tunggu aksi selesai di sesi A: modal Change Password tertutup
29. Di sesi B klik menu mana pun pada sidebar Fixed Asset (request berikutnya)
30. Verifikasi sesi B menampilkan dialog `Password Changed`
31. Verifikasi sesi produk Fixed Asset di sesi B berakhir
32. Di sesi A klik menu General Settings pada sidebar
33. Verifikasi halaman General Settings termuat di sesi A tanpa dialog dan tanpa pengalihan ke halaman Login (sesi A tetap aktif)

### Pemulihan state

34. Tutup konteks sesi B dan hapus sesi loginnya, lalu fixture BE memulihkan password akun #7 ke `Passw0rd!Old` dan mereset counter Change Password dan Login ke 0

## Notes

- Seluruh blok memakai dua konteks browser dengan akun #7 (kelas c); tiap blok membuka konteks B sendiri dan dimulai dari state hasil fixture, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan: TC-GS-PROFILE-136 dan TC-GS-PROFILE-140 (lock, tanpa mengubah password) dahulu; TC-GS-PROFILE-292, 293, 294 memakai satu dialog yang sama (langkah 1 dan 2 tiap TC identik: Change Password di sesi A, lalu aksi di sesi B hingga dialog tampil, dijalankan sekali pada langkah 13 sampai 17); TC-GS-PROFILE-249 terakhir karena memerlukan password dipulihkan.
- Langkah penghubung (S-03): langkah 4 dan 32 membuka halaman lain di sesi A; langkah 6, 11 dan 12 membuka My Profile; langkah 9, 24 dan 34 menutup konteks B (S-09); langkah 10, 24 dan 34 memulihkan jam server, lock, counter, dan password antar blok; langkah 15 dan 28 menunggu aksi selesai (bagian 8b butir 8).
- Temuan untuk QA:
  - TC-GS-PROFILE-140 menyebut lock "terjadi dari sesi lain" tetapi tidak menyebut cara membangunnya; spec memasang lock tier 15 menit lewat fixture BE (langkah 1) yang disediakan tim FE/BE.
  - TC-GS-PROFILE-249 tidak menyebut cara mengamati "sesi produk Fixed Asset berakhir"; spec memakai kemampuan baca status sesi produk yang disediakan tim FE/BE.
  - TC-GS-PROFILE-292 sampai 294 tidak menyebut interval request atau heartbeat; spec memakai batas tunggu 2 menit sebagai pilihan spec.
