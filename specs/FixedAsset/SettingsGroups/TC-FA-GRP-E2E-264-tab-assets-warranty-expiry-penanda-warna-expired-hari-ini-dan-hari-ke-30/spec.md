---
id: TC-FA-GRP-E2E-264-tab-assets-warranty-expiry-penanda-warna-expired-hari-ini-dan-hari-ke-30
title: "Tab Assets Warranty Expiry Penanda Warna: Tanggal Lewat Danger dengan Tooltip, Hari Ini Warning, dan Hari ke-30 Warning Inklusif, Hari ke-31 Normal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1277
  - TC-FA-GRP-1278
  - TC-FA-GRP-1279
  - TC-FA-GRP-1280
coverage:
  web: automated
---

# Tab Assets Warranty Expiry Penanda Warna: Tanggal Lewat Danger dengan Tooltip, Hari Ini Warning, dan Hari ke-30 Warning Inklusif, Hari ke-31 Normal

## Prerequisites

- Mode: FE+BE.
- Akun warrantyWatch (Pre-setup No 21; Group Role Manage purchase pada Value Warranty Node): `warrantyWatch_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GRP_WARRANTYWATCH_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`) berlaku: sesi API aktor, fixture BE, flag Guided Tooltip `seen`, dan pemulihan state global; tidak ditulis ulang di sini.
- General Settings client: Date Format DD/MM/YYYY, Time 24-hour, Timezone Asia/Jakarta (dibaca; tidak diubah).
- Data Value Warranty Node (Tabel Dinamis No 19; tanggal Warranty Expiry diisi ulang relatif terhadap hari uji di hook `before`, kemampuan disediakan tim FE/BE): W1 `Laptop Dell - 5` (hari uji − 1), W2 `Laptop Dell - 6` (hari uji), W3 `Laptop Dell - 7` (hari uji + 1), W4 `Laptop Dell - 8` (hari uji + 30), W5 `Laptop Dell - 9` (hari uji + 31), W6 `Laptop Dell - 10` (belum ada). Akun WW memegang Manage Group R pada node ini.
- Kemampuan teknis: mengisi ulang tanggal Warranty Expiry W1–W6 relatif terhadap hari uji (disediakan tim FE/BE); menghapus preferensi kolom Setup Column di browser (disediakan tim FE). Kode warna spesifik tidak diasersi; kelas danger dan warning diamati lewat kelas warna sel.
- Preferensi kolom Setup Column yang disimpan spec ini dihapus dari browser di hook `after` (kemampuan disediakan tim FE).
- State global: tidak ada yang diubah. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1277: Tanggal lewat tampil danger

1. Buka Detail Value Warranty Node (Tab Assets)
2. Buka Popup Setup Column, centang kolom Warranty Expiry, klik [Save]
3. Verifikasi W1 (hari uji − 1) menampilkan tanggal penuh dengan kelas warna danger
4. Hover sel W1
5. Verifikasi tooltip "Warranty expired"

### TC-FA-GRP-1278: Hari ini dan besok tampil warning

6. Verifikasi W2 (hari uji) menampilkan tanggal penuh dengan kelas warning, bukan danger
7. Hover sel W2
8. Verifikasi tooltip "Warranty expires soon" pada W2
9. Verifikasi W3 (hari uji + 1) menampilkan tanggal penuh dengan kelas warning, bukan danger
10. Hover sel W3
11. Verifikasi tooltip "Warranty expires soon" pada W3

### TC-FA-GRP-1279: Batas hari ke-30 inklusif

12. Verifikasi W4 (hari uji + 30) menampilkan kelas warning
13. Hover sel W4
14. Verifikasi tooltip "Warranty expires soon" pada W4

### TC-FA-GRP-1280: Hari ke-31 tampil normal

15. Verifikasi W5 (hari uji + 31) menampilkan tanggal penuh tanpa warna danger/warning
16. Hover sel W5
17. Verifikasi W5 tanpa tooltip penanda masa garansi

## Notes

- Satu pembukaan Detail Value Warranty Node dan satu centang kolom dipakai bersama keempat TC karena hanya mengamati sel (halaman yang dipakai berulang).
- TC-1279 dan TC-1280 berlabel Boundary; caseType spec mengikuti alur utama (Positive).
- Temuan untuk QA:
  - TC-1277 hingga TC-1280 tidak menyebut kode warna atau kelas CSS persis; spec mengasersi kelas danger/warning secara umum dan teks tooltip.
