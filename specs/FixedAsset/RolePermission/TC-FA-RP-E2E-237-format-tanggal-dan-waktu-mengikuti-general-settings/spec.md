---
id: TC-FA-RP-E2E-237-format-tanggal-dan-waktu-mengikuti-general-settings
title: Format tanggal dan waktu mengikuti General Settings
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-773
  - TC-FA-RP-774
  - TC-FA-RP-775
  - TC-FA-RP-776
  - TC-FA-RP-777
coverage:
  web: automated
---

# Format tanggal dan waktu mengikuti General Settings

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control. Langkah 27 sampai 28 mengganti akun ke Ahmad Fauzi (pengguna sasaran, email `ahmadfauzi@qwertysystem.net`, password disediakan tim FE; nama env belum didaftarkan di `suite.md`, lihat Temuan untuk QA); hook `after` memulihkan sesi ke akun default suite.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris; Rudi Hartono dengan Temporary User Yes dan Temporary Until terisi; Ahmad Fauzi berstatus Total Control). Pre-setup #24 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Tab Group Manager dan modal Changelog memakai data #38 dan #42 hanya sebagai sumber kolom Last Updated dan Date. Remove Total Control Ahmad Fauzi (langkah 24 sampai 25) mengubah Pre-setup #36; hook `after` memulihkannya.
- State global (Pre-setup #34): Date Format dan Time Format General Settings diubah pada langkah 7 ke format lain (kemampuan baca dan ubah General Settings disediakan tim FE/BE); nilai awal dicatat di hook `before` dan dipulihkan di hook `after`. Format awal dirujuk lewat `Fixture.fixedAssetRolePermission.dateFormatAwal` dan `timeFormatAwal`, format lain lewat `Fixture.fixedAssetRolePermission.dateFormatLain` dan `timeFormatLain` (dipilih dari opsi yang tersedia). Timezone entitas `Asia/Jakarta (UTC+07:00)`. Suite berjalan serial.
- Konfigurasi kolom Setup Column disimpan di browser; hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).

## Test Steps

### Kolom Last Updated dan Temporary Until Tab Total Control (TC 773)

1. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`.
2. Centang kolom `Temporary Until`.
3. Klik `[Save]`.
4. Verifikasi sel Last Updated baris Rudi Hartono menampilkan tanggal dan jam sesuai Date Format dan Time Format yang dipilih.
5. Verifikasi waktu pada sel Last Updated dikonversi ke Timezone entitas `Asia/Jakarta (UTC+07:00)`.
6. Verifikasi sel Temporary Until baris Rudi Hartono menampilkan tanggal sesuai Date Format yang dipilih.
7. Ubah Date Format dan Time Format di General Settings ke format lain (kemampuan disediakan tim FE/BE).
8. Muat ulang halaman (F5).
9. Verifikasi sel Last Updated baris Rudi Hartono mengikuti format baru.
10. Verifikasi sel Temporary Until baris Rudi Hartono mengikuti format baru.

### Isian tanggal Filter Panel Tab Total Control (TC 774)

11. Klik ikon Filter.
12. Pilih rentang pada field Last Updated.
13. Verifikasi teks rentang tanggal pada kotak input field Last Updated terformat sesuai Date Format General Settings.
14. Klik ikon Filter untuk menutup panel.

### Kolom Last Updated Tab Group Manager (TC 775)

15. Klik Tab `Group Manager`.
16. Verifikasi sel Last Updated terformat sesuai Date Format dan Time Format yang dipilih.

### Kolom Date modal Changelog dan isian tanggal Filter (TC 776)

17. Klik Tab `Total Control`.
18. Klik ikon Changelog pada toolbar.
19. Verifikasi kolom Date terformat sesuai Date Format dan Time Format yang dipilih.
20. Klik ikon Filter modal.
21. Pilih rentang Date.
22. Verifikasi teks rentang pada kotak input Date terformat sesuai Date Format.
23. Klik ikon Filter modal untuk menutup panel, lalu tutup modal Changelog.

### Tanggal pada body notifikasi in-app (TC 777)

24. Klik `[⋯]` baris Ahmad Fauzi, lalu klik `Remove`.
25. Klik `[Remove]` pada dialog konfirmasi.
26. Tunggu aksi selesai: dialog tertutup dan baris Ahmad Fauzi tidak lagi tampil.
27. Logout dari akun Total Control Siti Rahmawati.
28. Login sebagai Ahmad Fauzi.
29. Buka notifikasi `Your Total Control access was removed`.
30. Verifikasi body notifikasi memuat `Siti Rahmawati removed your Total Control access on` diikuti tanggal terformat sesuai Date Format yang dipilih.

## Notes

- Langkah penghubung (S-03): langkah 14 dan 23 (menutup panel dan modal), 17 (kembali ke Tab `Total Control`), 26 (menunggu aksi selesai sebelum ganti akun, bagian 8b butir 8), dan 27 sampai 28 (ganti akun eksplisit, S-07).
- Remove Total Control (TC 777) dijalankan di akhir spec karena menghapus tingkat akses (S-10); dialog Remove mengikuti TC 205 (`[⋯]` baris lalu `Remove`, tombol `[Remove]`).
- Langkah 4 sampai 6 dan 9 sampai 10 mengasersi format dengan membandingkan sel terhadap Date Format dan Time Format yang dibaca lewat kemampuan baca General Settings; nilai format yang dipilih dirujuk lewat fixture.
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Buka Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - Password akun Ahmad Fauzi (pengguna sasaran TC 777) tidak tertulis di Pre-setup TC dan tidak terdaftar sebagai nama env di `suite.md`; akun disediakan tim FE.
  - TC 773 sampai 777 mencantumkan Pre-setup #24 (Company Changelog) pada Precondition tanpa memakainya pada langkah; spec tidak memakai data #24.
  - TC 773 butir a menyebut "waktu dikonversi ke Timezone entitas" tanpa nilai waktu seed pada baris Rudi Hartono; spec mengasersi konversi terhadap waktu seed yang dirujuk lewat fixture.
  - TC 774 tidak menyebut rentang tanggal yang dipilih; spec mengasersi hanya format teks pada kotak input.
  - TC 775 sampai 777 bergantung pada format hasil TC 773 langkah 3 (Date Format dan Time Format yang sudah diubah); spec memakai format baru itu secara berurutan dan memulihkannya di hook `after`.
