---
id: TC-FA-GRP-E2E-013-guided-tooltip-groups-navigasi-keluar-resize-viewport-dan-keyboard
title: "Guided Tooltip Groups: Navigasi Keluar, Resize Viewport, dan Keyboard"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-38
  - TC-FA-GRP-39
  - TC-FA-GRP-1094
coverage:
  web: automated
---

# Guided Tooltip Groups: Navigasi Keluar, Resize Viewport, dan Keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Spec ini mengatur flag Guided Tooltip `fa-settings-groups` sendiri sesudah hook suite menyetelnya `seen`: kemampuan menyetel flag menjadi belum diset atau `seen` untuk akun aktor disediakan tim FE/BE; flag dipulihkan ke `seen` di hook `after`.
- Lebar viewport awal 1440px; langkah mengubah lebar viewport dan memulihkannya ke 1440px (langkah 32).
- Data Pre-setup (hanya dibaca): pohon group baku Tabel A (Pre-setup No 9). Seluruh kolom tabel dalam keadaan visible.
- Kemampuan teknis: fixture BE dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini mengubah flag Guided Tooltip akun aktor dan memulihkannya di hook `after`.

## Test Steps

### TC-FA-GRP-38: Navigasi keluar di tengah walkthrough tidak menyetel flag

1. Setel flag `fa-settings-groups` menjadi belum diset
2. Muat ulang halaman dengan F5
3. Verifikasi walkthrough muncul otomatis pada Step 1
4. Klik [Next]
5. Verifikasi walkthrough berada pada Step 2
6. Klik menu Fixed Asset > Dashboard
7. Klik menu Fixed Asset > Settings > Groups
8. Verifikasi walkthrough muncul lagi otomatis dari Step 1

### TC-FA-GRP-39: Keyboard Esc, Enter, dan panah

9. Setel flag `fa-settings-groups` menjadi belum diset
10. Muat ulang halaman dengan F5
11. Verifikasi walkthrough muncul otomatis pada Step 1
12. Tekan Enter
13. Verifikasi walkthrough berpindah ke Step 2 (Enter = Next)
14. Tekan ←
15. Verifikasi walkthrough kembali ke Step 1 (← = Back)
16. Tekan Esc
17. Verifikasi walkthrough tertutup (Esc = Skip)
18. Muat ulang halaman dengan F5
19. Verifikasi Breadcrumb `Settings > Groups` tampil
20. Verifikasi walkthrough tidak muncul otomatis sehingga flag seen telah diset

### TC-FA-GRP-1094: Resize viewport di tengah walkthrough menutup walkthrough tanpa menyetel flag

21. Setel flag `fa-settings-groups` menjadi belum diset
22. Ubah lebar viewport ke 1440px
23. Muat ulang halaman dengan F5
24. Verifikasi walkthrough tampil otomatis dari Step 1
25. Klik [Next]
26. Verifikasi walkthrough berada pada Step 2
27. Ubah lebar viewport ke 1100px
28. Verifikasi walkthrough tertutup
29. Muat ulang halaman dengan F5
30. Verifikasi walkthrough muncul lagi otomatis dari Step 1 sehingga flag seen tidak diset
31. Klik [Skip]
32. Ubah lebar viewport kembali ke 1440px

## Notes

- Langkah penghubung (S-03): langkah 1, 9, 21 (menyetel flag), langkah 2, 10, 23 (muat ulang agar flag dievaluasi, menggantikan "Buka Fixed Asset > Settings > Groups" karena halaman sudah dibuka hook `beforeEach`), langkah 22 (memastikan lebar awal 1440px), langkah 31 (menutup walkthrough) dan langkah 32 (memulihkan viewport).
- Langkah 6 dan 7 adalah "navigasi ke menu lain" lalu "kembali" dari TC-FA-GRP-38; menu lain yang dipakai adalah Fixed Asset > Dashboard.
- Urutan TC dalam spec: 38, 39, 1094. TC-FA-GRP-970 dan TC-FA-GRP-41 (sidebar collapsed dan kolom Total Asset di-hide) berada di spec 277 karena mengubah preferensi sidebar dan konfigurasi kolom.
- Temuan untuk QA:
  - TC-FA-GRP-38 menyebut "navigasi ke menu lain" tanpa nama menu; spec memakai Fixed Asset > Dashboard.
  - TC-FA-GRP-39 menyebut Enter, ←, Esc tetapi tidak menyebut Step yang diharapkan setelah Esc selain "flag seen diset"; spec mengasersi lewat muat ulang.
  - TC-FA-GRP-1094 menyebut Step 2 saat resize tanpa menyebut lebar tempat sidebar collapse otomatis; spec memakai 1100px sesuai TC.
