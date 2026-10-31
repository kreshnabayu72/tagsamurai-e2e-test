---
id: TC-GS-PROFILE-E2E-064-realtime-banner-pending-email-change
title: "Realtime: Banner Hilang Saat Admin Membatalkan atau Tautan Konfirmasi Diklik"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-PROFILE-209
  - TC-GS-PROFILE-210
coverage:
  web: automated
---

# Realtime: Banner Hilang Saat Admin Membatalkan atau Tautan Konfirmasi Diklik

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Pre-setup #8 (Citra Lestari, Activated, Email `citralestari@qwertysystem.net`) `pendingEmailProfile_automated_{namaCompany}@qwertysystem.net` (password `Spectra.env.GS_PROFILE_PENDING_PASSWORD`). Login sesi Citra di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Pelaku perubahan: admin Pre-setup #6 (Hendra Wijaya) `adminActor_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.GS_PROFILE_ADMIN_PASSWORD`) lewat sesi API. Password tidak ditulis di spec atau fixture.
- Data Dinamis #2: permintaan Email change live ke `citra.baru@qwertysystem.net`, dibuat lewat fixture BE sebelum tiap blok dan dipulihkan sesudahnya.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE yang membuat permintaan Email change live untuk Pre-setup #8 dan memulihkan Email Citra ke `citralestari@qwertysystem.net`; mail-catcher untuk membaca email konfirmasi di alamat `citra.baru@qwertysystem.net` (baseline jumlah email per alamat dicatat sebelum fixture, R-11); konteks browser kedua untuk membuka tautan konfirmasi (hasilnya tidak diasersi di konteks itu).
- Jendela amat SSE: asersi atas propagasi realtime didahului jeda 5 detik tanpa memuat ulang halaman. Lima detik adalah pilihan spec (bukan nilai TC atau PRD) sampai TC menyatakan durasinya.
- State global yang diubah: permintaan Email change dan Email akun #8. Dipulihkan oleh langkah pemulihan di akhir spec. Suite berjalan serial (`parallel: false`).
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Pelaku kedua admin (Pre-setup #6) memicu perubahan state lewat sesi API aktor yang tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE. Lihat `suite.md`, Hook suite 4.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.

## Test Steps

### TC-GS-PROFILE-209: Banner hilang otomatis tanpa refresh saat admin membatalkan perubahan Email

1. Fixture BE membuat permintaan Email change live untuk Citra Lestari ke `citra.baru@qwertysystem.net` hingga tersimpan, lalu muat ulang halaman My Profile
2. Verifikasi banner Pending Email Change dan teks bantu Email tampil di sesi Citra
3. Admin Pre-setup #6 membatalkan perubahan Email Citra (Cancel Change) lewat sesi API hingga pembatalan tersimpan
4. Tunggu 5 detik tanpa memuat ulang halaman
5. Verifikasi Email di Section Identity tetap `citralestari@qwertysystem.net`
6. Verifikasi banner dan teks bantu Email hilang tanpa refresh manual
7. Verifikasi tidak ada pesan error di halaman

### TC-GS-PROFILE-210: Banner hilang otomatis dan Email berubah saat tautan konfirmasi diklik

8. Catat jumlah email di alamat `citra.baru@qwertysystem.net` sebagai baseline (mail-catcher), lalu fixture BE membuat permintaan Email change live untuk Citra Lestari ke `citra.baru@qwertysystem.net` hingga tersimpan
9. Muat ulang halaman My Profile
10. Verifikasi banner Pending Email Change dan teks bantu Email tampil di sesi Citra
11. Buka konteks browser kedua, lalu buka tautan konfirmasi dari email baru yang masuk di alamat `citra.baru@qwertysystem.net`
12. Tunggu 5 detik tanpa memuat ulang halaman di sesi Citra
13. Verifikasi nilai Email di Section Identity menjadi `citra.baru@qwertysystem.net` tanpa memuat ulang halaman
14. Verifikasi banner dan teks bantu Email hilang

### Pemulihan state

15. Tutup konteks browser kedua dan hapus sesi loginnya, lalu fixture BE memulihkan Email Citra Lestari ke `citralestari@qwertysystem.net` dan menghapus permintaan Email change live

## Notes

- Urutan: TC-GS-PROFILE-209 dahulu karena tidak mengubah Email; TC-GS-PROFILE-210 mengubah Email Citra sehingga pemulihan di langkah 15.
- Langkah penghubung (S-03): langkah 1 dan 9 memuat ulang halaman sebelum aksi; langkah 4 dan 12 adalah jeda jendela amat SSE 5 detik (bagian 6) tanpa `Verifikasi`; langkah 2 dan 10 menegaskan banner tampil sebelum perubahan sebagai anchor positif untuk asersi hilangnya banner (bagian 8b butir 2); langkah 15 memulihkan state (S-09).
- Pembagian dengan spec lain: sinkronisasi saat admin mengubah Email (TC-GS-PROFILE-246) ada di spec 047; tampilan banner statis ada di spec 046.
- Temuan untuk QA:
  - TC-GS-PROFILE-209 menyebut admin berada "di sesi lain" di Global Settings > User; spec memakai sesi API admin Pre-setup #6 (Hook suite 4) karena hasil di UI admin tidak diasersi, sehingga konteks browser kedua hanya dipakai untuk membuka tautan konfirmasi pada TC-GS-PROFILE-210.
  - TC-GS-PROFILE-210 menyatakan Email berubah "bersamaan" dengan hilangnya banner; spec mengasersi keduanya sesudah jeda 5 detik dan tidak dapat mengasersi kesamaan waktu.
  - Teks banner dan teks bantu Email tidak disebut pada TC-GS-PROFILE-209 dan 210; spec mengasersi keberadaannya tanpa teks.
