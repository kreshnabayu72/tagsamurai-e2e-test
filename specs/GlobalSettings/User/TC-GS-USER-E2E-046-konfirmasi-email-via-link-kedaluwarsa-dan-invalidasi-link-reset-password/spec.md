---
id: TC-GS-USER-E2E-046-konfirmasi-email-via-link-kedaluwarsa-dan-invalidasi-link-reset-password
title: "Konfirmasi Email via Link: Email Resmi Pindah, Link Reset Password Lama Tidak Berlaku, Link Bentrok dan Link Kedaluwarsa Ditolak Tanpa Mengubah Email Pending"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-231
  - TC-GS-USER-232
  - TC-GS-USER-1081
  - TC-GS-USER-968
coverage:
  web: automated
---

# Konfirmasi Email via Link: Email Resmi Pindah, Link Reset Password Lama Tidak Berlaku, Link Bentrok dan Link Kedaluwarsa Ditolak Tanpa Mengubah Email Pending

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Dinamis (di-seed lewat API di hook `before`, dibersihkan di `after`; menggantikan Rina Putri No. 15 agar data Pre-setup tidak diubah dan karena tiap link konfirmasi hanya bisa dipakai sekali, S-06):
  - `Rina Putri A {runId}-046`: email `rinaputri.a+{runId}-046@qwertysystem.net`, Activated, dengan email pending `rinaputri.a.new+{runId}-046@qwertysystem.net` (TC-GS-USER-231 dan TC-GS-USER-968).
  - `Rina Putri B {runId}-046`: email `rinaputri.b+{runId}-046@qwertysystem.net`, Activated, dengan email pending `rinaputri.b.new+{runId}-046@qwertysystem.net` (TC-GS-USER-232). Waktu terbit link konfirmasi (T0) dibaca dari API seeding.
  - `Rina Putri C {runId}-046`: email `rinaputri.c+{runId}-046@qwertysystem.net`, Activated, dengan email pending `rinaputri.c.new+{runId}-046@qwertysystem.net`; email itu sudah dipakai user `Pengguna Bentrok {runId}-046` melalui fixture BE (melewati validasi UI) (TC-GS-USER-1081).
- Kemampuan teknis:
  - Mail-catcher yang dapat dibaca per alamat email dan link di dalamnya dapat dibuka dari tab baru (kelas d; disediakan tim FE). Email dicari berdasarkan alamat tujuan, bukan posisi teratas.
  - Meminta reset password untuk Rina Putri A lewat alur Reset Password Auth di jendela privat baru; jendela itu ditutup dan sesi browser-nya dihapus sesudah dipakai (S-09).
  - Manipulasi jam server (TTL link konfirmasi dihitung murni di server dan tidak diamati lewat UI, sehingga jam browser tidak diubah): jam server diset absolut ke T0 + 25 jam (margin 1 jam di atas batas 24 jam, lebih dari 5 menit; T0 dibaca dari API seeding, bukan dari waktu hook) pada langkah spec dan dipulihkan lewat langkah aksi sebelum kembali ke User List; hook `after` memulihkan jam server sebagai cadangan. Mekanisme penggeseran jam disediakan tim FE/BE.
  - Fixture BE untuk memasang email pending Rina Putri C ke user lain tanpa melewati validasi UI (nama endpoint ditentukan tim FE di tahap script).
- State global: jam server (dipulihkan). Suite berjalan serial (`parallel: false`, lihat `suite.md`); blok yang menggeser jam berada paling akhir.
- Cleanup (`after`): pulihkan jam server, hapus keempat user seed.

## Test Steps

### Pembukaan layar

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Klik icon Search, ketik `Rina Putri A {runId}-046`, tekan Enter

### TC-GS-USER-968 dan TC-GS-USER-231: Konfirmasi link memindahkan email resmi dan membatalkan link reset password lama

3. Buka jendela privat baru, minta reset password untuk email lama `rinaputri.a+{runId}-046@qwertysystem.net` lewat alur Reset Password
4. Ambil link reset password dari email ke `rinaputri.a+{runId}-046@qwertysystem.net` di mail-catcher
5. Tutup jendela privat dan hapus sesi browser-nya
6. Buka tab baru, buka link konfirmasi email `Rina Putri A {runId}-046` (email ke `rinaputri.a.new+{runId}-046@qwertysystem.net`) dari mail-catcher
7. Tutup tab link konfirmasi
8. Kembali ke User List, refresh
9. Klik icon Search, ketik `Rina Putri A {runId}-046`, tekan Enter
10. Verifikasi kolom Email baris `Rina Putri A {runId}-046` berubah ke `rinaputri.a.new+{runId}-046@qwertysystem.net`
11. Verifikasi badge `Pending Email Confirmation` hilang dari baris `Rina Putri A {runId}-046`
12. Buka jendela privat baru, buka link reset password lama (langkah 4)
13. Verifikasi link reset password lama ditolak (tidak berlaku)
14. Tutup jendela privat dan hapus sesi browser-nya

### TC-GS-USER-1081: Link konfirmasi diklik saat email pending sudah dipakai user lain ditolak sebagai link kedaluwarsa

15. Ganti isi kotak search dengan `Rina Putri C {runId}-046`, tekan Enter
16. Buka tab baru, buka link konfirmasi email `Rina Putri C {runId}-046` (email ke `rinaputri.c.new+{runId}-046@qwertysystem.net`) dari mail-catcher
17. Verifikasi halaman link menampilkan `"This confirmation link has expired or was already used."`
18. Tutup tab link konfirmasi
19. Kembali ke User List, refresh
20. Klik icon Search, ketik `Rina Putri C {runId}-046`, tekan Enter
21. Verifikasi kolom Email baris `Rina Putri C {runId}-046` tetap `rinaputri.c+{runId}-046@qwertysystem.net`

### TC-GS-USER-232: Link konfirmasi kedaluwarsa tidak menghapus email pending

22. Atur jam server absolut ke T0 + 25 jam (T0 = waktu terbit link konfirmasi `Rina Putri B {runId}-046`)
23. Buka tab baru, buka link konfirmasi `Rina Putri B {runId}-046` (email ke `rinaputri.b.new+{runId}-046@qwertysystem.net`) dari mail-catcher
24. Verifikasi link ditolak: `"This confirmation link has expired or was already used."`
25. Pulihkan jam server ke waktu nyata
26. Tutup tab link konfirmasi
27. Kembali ke User List, refresh
28. Klik icon Search, ketik `Rina Putri B {runId}-046`, tekan Enter
29. Verifikasi badge `Pending Email Confirmation` tetap pada baris `Rina Putri B {runId}-046`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Kelas harness d (mail-catcher dan time-travel TTL link sebagai objek uji); semua TC di spec ini berkelas itu.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 29 langkah, di bawah batas sekitar 35.
- Urutan TC sumber diubah: TC-GS-USER-968 digabung dengan TC-GS-USER-231 dalam satu alur (permintaan reset password sebelum konfirmasi, link reset lama dibuka sesudah konfirmasi; langkah 2 TC-GS-USER-968 setara langkah 6 sampai 11); TC-GS-USER-1081 mendahului TC-GS-USER-232; TC-GS-USER-232 paling akhir karena menggeser jam server (bagian 3 dan 6).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 sampai 2 (pembukaan), 3 sampai 5 (permintaan reset password untuk Rina Putri A dan penutupan jendela privat), 7, 18, 26 (menutup tab), 8 sampai 9, 19 sampai 20, 27 sampai 28 (kembali ke User List, refresh, Search), 14 (menutup jendela privat), 15 (Search), 22 dan 25 (mengatur dan memulihkan jam server, jam dipulihkan sebelum kembali ke User List, S-09).
- Tiap alamat email pending di-seed pada user berbeda karena tiap link konfirmasi hanya dapat dipakai sekali dan token pada TC-GS-USER-231 dan TC-GS-USER-232 saling tidak boleh mengonsumsi satu sama lain.
- Temuan untuk QA:
  - TC-GS-USER-231 Post Condition (token reset password aktif milik email lama tidak berlaku lagi; terdampak My Profile dan Auth > Reset Password) tidak punya langkah observasi di TC-GS-USER-231; observasi token reset dilakukan oleh TC-GS-USER-968 pada langkah 12 sampai 13, Post Condition lain tidak diasersi (S-01).
  - TC-GS-USER-1081 Post Condition (email aktual Rina Putri tetap email lama; tidak ada invalidasi token reset password) hanya sebagian punya observasi (langkah 21 untuk email aktual); "tidak ada invalidasi token reset password" tidak punya langkah observasi dan tidak diasersi (S-01).
  - TC-GS-USER-968 Expected "Link reset password lama ditolak (tidak berlaku)" tidak menyebut teks atau halaman penolakan; spec mengasersi link ditolak tanpa teks, dan alur "Rina Putri minta reset password" tidak menyebut label halaman (spec tidak mengarang label).
  - TC-GS-USER-231 dan TC-GS-USER-968 tidak menyebut hasil yang tampil di halaman link konfirmasi yang berhasil; tidak diasersi.
  - TC-GS-USER-232 menyebut "waktu sistem dimajukan" tanpa mekanisme dan tanpa nilai; spec memakai jam server absolut T0 + 25 jam dengan mekanisme disediakan tim FE/BE.
  - TC-GS-USER-1081 menyebut "fixture BE" tanpa mekanisme; disediakan tim FE/BE (S-13).
  - TC-GS-USER-231, 232, 1081, dan 968 menyebut Rina Putri Pre-setup (No. 15); spec memakai tiga user seed bersuffix karena setiap link hanya bisa dipakai sekali dan data Pre-setup tidak diubah (S-06).
