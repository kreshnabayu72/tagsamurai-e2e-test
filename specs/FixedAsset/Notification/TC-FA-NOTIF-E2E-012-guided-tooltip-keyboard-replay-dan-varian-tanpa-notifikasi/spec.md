---
id: TC-FA-NOTIF-E2E-012-guided-tooltip-keyboard-replay-dan-varian-tanpa-notifikasi
title: "Guided Tooltip: Resize Viewport, Keyboard, Varian Tanpa Notifikasi, dan Replay lewat Tombol Bantuan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-48
  - TC-FA-NOTIF-54
  - TC-FA-NOTIF-55
  - TC-FA-NOTIF-56
coverage:
  web: automated
---

# Guided Tooltip: Resize Viewport, Keyboard, Varian Tanpa Notifikasi, dan Replay lewat Tombol Bantuan

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard, Notification Center, dan Guided Tooltip `fa-notification`.
- Akun aktor pertama: Total Control Pre-setup #31 (`totalControlTour_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_NOTIFTOUR_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. TC-55, 56, dan 48 memakai akun ini.
- Akun kedua (ganti akun eksplisit pada langkah 25): Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar); flag `guided_tooltip_seen_fa-notification` akun ini true (Pre-setup #1). TC-54 memakai akun ini. Hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Pengecualian atas hook suite untuk flag Guided Tooltip: spec ini menguji flag `guided_tooltip_seen_fa-notification` untuk akun #31 sehingga hook `before` suite tidak menyetelnya true. Fixture BE menghapus flag itu untuk akun #31 di awal tiap blok TC-55, 56, 48; hook `after` memulihkan keadaan Pre-setup #31 (tanpa flag, seed N-01 sampai N-07).
- Data: seed notifikasi N-01 sampai N-07 (Pre-setup #17) untuk TC-55, 56, dan 54; TC-48 memakai varian akun #31 tanpa notifikasi (bell kosong) yang diatur fixture BE penukar varian seed. Kemampuan membaca flag seen akun dari state BE (untuk Expected TC-56 dan TC-54 tentang flag seen) disediakan tim FE/BE. Kemampuan teknis: mengubah ukuran viewport browser dan mengirim keystroke (`Enter`, panah kanan, panah kiri, `Esc`).
- Fixture BE pemulih seed dijalankan di hook `before` dan `after`. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor dan fixture BE pemulih dan penukar seed notifikasi.

## Test Steps

### TC-FA-NOTIF-55: Resize viewport menutup tur tanpa menyimpan flag seen

1. Hapus flag seen akun #31 lewat fixture BE, muat ulang halaman, lalu klik Bell icon dan `[Show All]` untuk membuka Notification Center untuk pertama kali
2. Verifikasi tooltip Step 1 tampil
3. Ubah ukuran viewport browser saat Step 1 tampil
4. Verifikasi tur tertutup
5. Muat ulang halaman
6. Verifikasi tur muncul lagi otomatis dari Step 1
7. Pulihkan ukuran viewport browser ke ukuran semula

### TC-FA-NOTIF-56: Fokus keyboard dan navigasi Esc, Enter, panah kanan, panah kiri

8. Hapus flag seen akun #31 lewat fixture BE, muat ulang halaman, lalu klik Bell icon dan `[Show All]` untuk membuka Notification Center untuk pertama kali
9. Verifikasi tooltip mendapat keyboard focus
10. Tekan Enter
11. Verifikasi Step 2 tampil
12. Tekan panah kanan
13. Verifikasi Step 3 tampil
14. Tekan panah kiri
15. Verifikasi Step 2 tampil
16. Tekan Esc
17. Verifikasi tur tertutup
18. Verifikasi flag seen akun #31 tersimpan (dibaca lewat kemampuan baca state BE)

### TC-FA-NOTIF-48: Step 2 tetap menyorot area badge saat tidak ada notifikasi Unread

19. Tukar seed akun #31 ke varian tanpa notifikasi lewat fixture BE penukar, hapus flag seen akun #31, muat ulang halaman, lalu klik Bell icon dan `[Show All]` untuk membuka Notification Center untuk pertama kali
20. Klik `[Next]`
21. Verifikasi spotlight menyorot area Bell icon tempat badge berada
22. Verifikasi badge Bell icon tidak tampil
23. Klik `[Skip]`
24. Tunggu aksi selesai (tur tertutup dan flag seen akun #31 tersimpan)

### TC-FA-NOTIF-54: Replay lewat tombol [?] tanpa mereset flag seen

25. Ganti akun: logout dari akun #31, login sebagai Total Control Pre-setup #1 dengan `Spectra.env.FA_TC_PASSWORD`, lalu buka Fixed Asset > Dashboard
26. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
27. Arahkan kursor ke tombol `[?]` di sebelah kanan Breadcrumb
28. Verifikasi tooltip tombol `[?]` `Show guide`
29. Klik tombol `[?]`
30. Verifikasi tur mulai dari Step 1
31. Klik `[Skip]`
32. Tunggu aksi selesai (tur tertutup)
33. Muat ulang halaman
34. Verifikasi Breadcrumb `Notification Center` tampil
35. Verifikasi tur tidak muncul otomatis
36. Verifikasi flag seen akun #1 tetap true (dibaca lewat kemampuan baca state BE)

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan blok: TC-55, 56 (seed N-01 sampai N-07), TC-48 (varian tanpa notifikasi), lalu ganti akun ke #1 untuk TC-54 supaya penggantian akun hanya sekali. Urutan menyimpang dari urutan nomor TC. Bagian sesudah ganti akun (TC-54) tetap bermakna walau bagian sebelumnya gagal; kelas harness tunggal (fungsional).
- Langkah penghubung (S-03): langkah 1, 8, 19 (hapus flag, tukar seed, muat ulang halaman, buka Notification Center untuk pertama kali), langkah 7 (pulihkan viewport), langkah 23 dan 24 (`[Skip]` menutup tur, lalu tunggu aksi selesai sebelum ganti akun; flag akun #31 yang tersimpan dipulihkan hook `after`), langkah 25 (ganti akun dan buka Fixed Asset > Dashboard; S-07), langkah 26 (buka Notification Center sesudah ganti akun), langkah 31 dan 32 (Langkah TC-54: "Klik `[Skip]` lalu muat ulang halaman" dipecah menjadi dua langkah dengan tunggu aksi selesai di antaranya).
- Asersi tambahan sebagai anchor positif (S-03; 8b butir 2): langkah 2 (Step 1 sempat tampil sebelum asersi tur tertutup pada langkah 4), langkah 34 (Breadcrumb sesudah muat ulang halaman sebelum asersi tur tidak muncul).
- Langkah 18 dan 36 mengasersi flag seen lewat kemampuan baca state BE yang disediakan tim FE/BE (endpoint tidak dikarang; S-11, S-13) karena Expected TC-56 butir e dan TC-54 butir c menyebut flag seen.
- Alasan melewati ambang sekitar 35 langkah (36 langkah): semua blok satu kelas (fungsional Guided Tooltip) dan tiap blok TC berdiri sendiri dengan flag dan seed dipulihkan di awal blok; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan dua langkah tunggu aksi selesai menambah langkah tanpa menambah asersi.
- Guided Tooltip dipisah menjadi tiga spec (010 konten Step 1 sampai 3 dan Back, 011 menutup tur dan flag seen, 012 keyboard, replay, dan varian tanpa notifikasi) walau berbagi akun #31 dan seed N-01 sampai N-07, karena blok yang menyimpan flag menghapus flag di awal blok dan gabungannya jauh melampaui ~35 langkah.
- Temuan untuk QA:
  - TC-56 tidak menyebut tombol yang memajukan step bersama `Enter`; spec mengasumsikan `Enter` memajukan satu step (Step 1 ke Step 2) sesuai Expected butir b.
  - TC-55 judulnya "tanpa menyimpan flag seen" tetapi Expected hanya mengasersi tur muncul lagi sesudah muat ulang halaman; spec mengikuti Expected TC tanpa membaca flag.
  - TC-48 dan TC-430 membutuhkan varian akun #31 tanpa notifikasi yang tidak dibedakan di Pre-setup #31 selain catatan "varian seed tanpa notifikasi"; spec menyerahkan penukaran varian ke fixture BE penukar.
