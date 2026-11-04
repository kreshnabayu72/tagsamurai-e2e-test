---
id: TC-FA-NOTIF-E2E-011-guided-tooltip-menutup-tur-done-skip-overlay-resize-navigasi
title: "Guided Tooltip: Menutup Tur lewat Done, Skip, Overlay, atau Navigasi Keluar dan Penyimpanan Flag Seen"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-50
  - TC-FA-NOTIF-51
  - TC-FA-NOTIF-52
  - TC-FA-NOTIF-428
  - TC-FA-NOTIF-429
coverage:
  web: automated
---

# Guided Tooltip: Menutup Tur lewat Done, Skip, Overlay, atau Navigasi Keluar dan Penyimpanan Flag Seen

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard, Notification Center, dan Guided Tooltip `fa-notification`.
- Akun aktor: Total Control Pre-setup #31 (`totalControlTour_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_NOTIFTOUR_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Pre-setup #1).
- Pengecualian atas hook suite untuk flag Guided Tooltip: spec ini menguji flag `guided_tooltip_seen_fa-notification` sehingga hook `before` suite tidak menyetelnya true untuk akun #31. Fixture BE menghapus flag itu untuk akun #31 di hook `before` spec ini dan di awal tiap blok TC yang menyimpan flag (TC-50, 51, 52, 429; langkah penghubung); hook `after` memulihkan keadaan Pre-setup #31 (tanpa flag).
- Data: seed notifikasi N-01 sampai N-07 (Pre-setup #17) tersedia untuk akun #31. Spec hanya membaca data; fixture BE pemulih seed dijalankan di hook `before` dan `after`. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor dan fixture BE pemulih seed notifikasi.

## Test Steps

### TC-FA-NOTIF-428: Navigasi keluar di tengah tur menutup tur tanpa menyimpan flag seen

1. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center untuk pertama kali (flag seen belum ada)
2. Verifikasi tooltip Step 1 tampil
3. Klik tombol Back browser sehingga kembali ke Fixed Asset > Dashboard
4. Verifikasi halaman Fixed Asset > Dashboard tampil
5. Verifikasi tur tertutup
6. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center lagi
7. Verifikasi tur muncul lagi otomatis dari Step 1

### TC-FA-NOTIF-50: [Done] menutup tur dan Dropdown Panel serta menyimpan flag seen

8. Hapus flag seen akun #31 lewat fixture BE, muat ulang halaman, lalu klik Bell icon dan `[Show All]` untuk membuka Notification Center untuk pertama kali
9. Klik `[Next]` dua kali
10. Klik `[Done]`
11. Verifikasi tur tertutup
12. Verifikasi Dropdown Panel tertutup
13. Muat ulang halaman
14. Verifikasi Breadcrumb `Notification Center` tampil
15. Verifikasi tur tidak muncul lagi otomatis

### TC-FA-NOTIF-51: [Skip] menutup tur dan menyimpan flag seen

16. Hapus flag seen akun #31 lewat fixture BE, muat ulang halaman, lalu klik Bell icon dan `[Show All]` untuk membuka Notification Center untuk pertama kali
17. Klik `[Skip]`
18. Verifikasi tur tertutup
19. Muat ulang halaman
20. Verifikasi Breadcrumb `Notification Center` tampil
21. Verifikasi tur tidak muncul lagi otomatis

### TC-FA-NOTIF-52: Klik overlay gelap sama dengan Skip

22. Hapus flag seen akun #31 lewat fixture BE, muat ulang halaman, lalu klik Bell icon dan `[Show All]` untuk membuka Notification Center untuk pertama kali
23. Klik area overlay gelap di luar spotlight
24. Verifikasi tur tertutup
25. Muat ulang halaman
26. Verifikasi Breadcrumb `Notification Center` tampil
27. Verifikasi tur tidak muncul lagi otomatis

### TC-FA-NOTIF-429: [Skip] di Step 3 menutup tur dan Dropdown Panel serta menyimpan flag seen

28. Hapus flag seen akun #31 lewat fixture BE, muat ulang halaman, lalu klik Bell icon dan `[Show All]` untuk membuka Notification Center untuk pertama kali
29. Klik `[Next]` dua kali
30. Klik `[Skip]` pada Step 3
31. Verifikasi tur tertutup
32. Verifikasi Dropdown Panel yang dibuka otomatis tertutup
33. Muat ulang halaman
34. Verifikasi Breadcrumb `Notification Center` tampil
35. Verifikasi tur tidak muncul lagi otomatis

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan blok: TC-428 di awal karena tidak menyimpan flag seen sehingga tidak membutuhkan penghapusan flag; TC-50, 51, 52, 429 menyimpan flag dan masing-masing diawali penghapusan flag. Urutan menyimpang dari urutan nomor TC.
- Langkah penghubung (S-03): langkah 8, 16, 22, 28 (hapus flag, muat ulang halaman, buka Notification Center), langkah 6 (buka Notification Center kembali; TC-428 menulis "Buka Notification Center lagi"), langkah 13, 19, 25, 33 adalah Langkah TC (muat ulang halaman).
- Asersi tambahan sebagai anchor positif (S-03; 8b butir 2): langkah 2 (tur sempat tampil sebelum asersi tur tertutup pada langkah 5), langkah 4 (halaman Dashboard sebagai anchor), langkah 14, 20, 26, 34 (Breadcrumb sesudah muat ulang halaman sebagai anchor sebelum asersi tur tidak muncul).
- Spec ini 35 langkah; kelimanya satu topik (menutup tur dan efeknya pada flag) dengan akun dan seed yang sama, dan tiap blok berdiri sendiri karena flag dihapus di awal blok.
- Guided Tooltip dipisah menjadi tiga spec (010 konten Step 1 sampai 3 dan Back, 011 menutup tur dan flag seen, 012 keyboard, replay, dan varian tanpa notifikasi) walau berbagi akun #31 dan seed N-01 sampai N-07, karena blok yang menyimpan flag menghapus flag di awal blok dan gabungannya jauh melampaui ~35 langkah.
- Temuan untuk QA:
  - TC-50, 51, 52, 429 mengasersi "tur tidak muncul lagi" sesudah muat ulang sebagai bukti flag tersimpan, tanpa langkah baca flag langsung; spec mengikuti TC.
  - TC-428 menulis "klik tombol Back browser" tanpa menyebut halaman asal selain Fixed Asset > Dashboard; spec mengasumsikan jalur Dashboard, Bell icon, `[Show All]`.
