---
id: TC-FA-CAID-E2E-005-guided-tooltip-skip-overlay-keyboard
title: "Guided Tooltip: Skip, Overlay, Resize, Keyboard, dan Flag per User"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-17
  - TC-FA-CAID-18
  - TC-FA-CAID-19
  - TC-FA-CAID-20
  - TC-FA-CAID-21
coverage:
  web: automated
---

# Guided Tooltip: Skip, Overlay, Resize, Keyboard, dan Flag per User

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Akun aktor pertama: Total Control Company Alpha (Pre-setup No 1, akun default suite) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Akun kedua (TC-FA-CAID-21, ganti akun eksplisit): Config-Update (Pre-setup No 3, role Manage asset ID configuration dengan Read dan Update) `configUpdate_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_CFGUPD_PASSWORD` (nama env usulan di `suite.md`, perlu konfirmasi tim FE). Password tidak ditulis di spec atau fixture.
- Pengecualian hook suite untuk flag Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-asset-id` ke seen untuk semua akun UI suite dan hook `after` suite memulihkan nilai awalnya. Spec ini menguji flag itu sendiri, jadi langkah spec mengatur flag akun Total Control dan akun Config-Update ke belum diset dengan kemampuan "atur flag Guided Tooltip akun" (menulis flag; disediakan tim FE, mekanisme tidak tertulis di TC, PRD, atau LLD).
- Data Pre-setup No 10: baseline B1 (hanya dibaca). Spec tidak membuat data dan tidak menekan `[Save]`.
- Kemampuan teknis: mengubah ukuran viewport browser dan memulihkannya (TC-FA-CAID-19); penekanan tombol keyboard `Enter`, panah kanan, panah kiri, dan `Esc` (TC-FA-CAID-20).
- State global: flag Guided Tooltip dua akun (dipulihkan hook `after` suite; walkthrough akun Config-Update yang terbuka di akhir TC-FA-CAID-21 ditutup di langkah 40 agar tidak menutupi halaman spec berikutnya) dan ukuran viewport (dipulihkan di langkah 23). Hook `after` spec ini mengembalikan sesi ke akun default suite (Total Control Company Alpha). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-17: Tombol Skip menutup walkthrough dan menyetel flag seen

1. Atur flag Guided Tooltip akun Total Control ke belum diset hingga flag tersimpan, tanpa memuat ulang halaman
2. Klik tombol `[?]` di kanan Breadcrumb
3. Klik `[Next]` sampai step 2
4. Klik `[Skip]` di step 2
5. Verifikasi walkthrough tertutup
6. Muat ulang halaman (F5)
7. Verifikasi tab `Custom Asset ID` tampil dengan Breadcrumb `Settings > Asset Master > Custom Asset ID`
8. Verifikasi walkthrough tidak muncul otomatis

### TC-FA-CAID-18: Klik overlay gelap setara Skip

9. Atur flag Guided Tooltip akun Total Control ke belum diset hingga flag tersimpan, tanpa memuat ulang halaman
10. Klik tombol `[?]` di kanan Breadcrumb
11. Klik area overlay gelap di luar tooltip
12. Verifikasi walkthrough tertutup
13. Muat ulang halaman (F5)
14. Verifikasi tab `Custom Asset ID` tampil dengan Breadcrumb `Settings > Asset Master > Custom Asset ID`
15. Verifikasi walkthrough tidak muncul otomatis

### TC-FA-CAID-19: Resize viewport menutup walkthrough tanpa menyetel flag seen

16. Atur flag Guided Tooltip akun Total Control ke belum diset hingga flag tersimpan, tanpa memuat ulang halaman
17. Klik tombol `[?]` di kanan Breadcrumb
18. Ubah ukuran viewport browser
19. Verifikasi walkthrough tertutup saat viewport diubah
20. Muat ulang halaman (F5)
21. Verifikasi kartu `Custom Asset ID Configuration` tampil
22. Verifikasi walkthrough muncul otomatis lagi dari step 1 karena flag seen tidak disetel
23. Pulihkan ukuran viewport browser ke ukuran semula
24. Klik `[Skip]` untuk menutup walkthrough

### TC-FA-CAID-20: Aksesibilitas keyboard Esc, Enter, panah

25. Atur flag Guided Tooltip akun Total Control ke belum diset hingga flag tersimpan, tanpa memuat ulang halaman
26. Klik tombol `[?]` di kanan Breadcrumb
27. Verifikasi tooltip box menerima fokus keyboard
28. Tekan `Enter`
29. Verifikasi walkthrough maju ke step 2
30. Tekan panah kanan
31. Verifikasi walkthrough maju ke step 3
32. Tekan panah kiri
33. Verifikasi walkthrough kembali ke step 2
34. Tekan `Esc`
35. Verifikasi walkthrough tertutup (setara Skip)

### TC-FA-CAID-21: Flag guided tooltip disimpan per user

36. Atur flag Guided Tooltip akun Config-Update (Pre-setup No 3) ke belum diset hingga flag tersimpan; flag akun Total Control sudah seen dari langkah sebelumnya
37. Ganti akun: logout akun Total Control, lalu login sebagai Config-Update (Pre-setup No 3)
38. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
39. Verifikasi walkthrough tampil otomatis dari step 1 untuk user Config-Update walau user Total Control di Company yang sama sudah melihatnya
40. Klik `[Skip]` untuk menutup walkthrough dan menyetel flag seen akun Config-Update

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular. Langkah buka tab pada TC-FA-CAID-17 sampai 20 dipenuhi hook `beforeEach` suite.
- Spec ini 40 langkah, melewati sekitar 35 langkah. Alasan: semua blok satu kelas (fungsional, state flag Guided Tooltip), satu layar, dan tiap blok mengatur ulang flag sendiri sehingga berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 9, 16, 25, 36 (mengatur flag), langkah 2, 3, 4, 10, 11, 17, 18, 26, 28, 30, 32, 34 (aksi walkthrough sebagai pemicu), langkah 6, 13, 20 (muat ulang sebagai pemicu), langkah 23 (memulihkan viewport) dan langkah 24 (menutup walkthrough yang muncul otomatis agar klik `[?]` pada TC-FA-CAID-20 tidak tertahan overlay), langkah 37 dan 38 (ganti akun dan membuka halaman, karena akun kedua tidak login di hook), dan langkah 40 (menutup walkthrough yang muncul otomatis untuk akun Config-Update agar tidak menutupi halaman spec berikutnya; flag akun itu dipulihkan hook `after` suite).
- TC-FA-CAID-17 sampai 20 mengatur flag belum diset tanpa muat ulang agar klik `[?]` memulai walkthrough dari step 1 seperti tertulis di langkah TC. Flag diatur ulang sebelum tiap blok karena blok sebelumnya menyetelnya seen (Skip, overlay, Esc, atau langkah 24).
- Asersi absence (langkah 8 dan 15) didahului asersi positif atas elemen lain pada halaman yang sama (langkah 7 untuk langkah 8, langkah 14 untuk langkah 15: tab `Custom Asset ID` tampil dengan Breadcrumb, sesuai klausa Expected TC-FA-CAID-17 b dan TC-FA-CAID-18 b). Langkah 21 (kartu konfigurasi tampil) menandai halaman termuat sebelum asersi walkthrough muncul otomatis pada TC-FA-CAID-19; Expected TC-FA-CAID-19 tidak memuat klausa itu (S-03).
- Temuan untuk QA:
  - TC-FA-CAID-17 dan 18 menyebut "menyetel flag seen" di judul TC tetapi tidak memberi langkah observasi selain muat ulang; spec mengamatinya lewat muat ulang (langkah 6 sampai 8 dan 13 sampai 15).
  - TC-FA-CAID-19 tidak menyebut ukuran viewport yang dipakai; spec memakai ukuran lain yang tidak ditentukan TC (dipilih tim FE).
  - Mekanisme mengatur flag Guided Tooltip per akun tidak tertulis di TC, PRD, atau LLD; disediakan tim FE (S-13).
  - Post Condition TC-FA-CAID-17 sampai 21 kosong; tidak ada yang diasersi.
