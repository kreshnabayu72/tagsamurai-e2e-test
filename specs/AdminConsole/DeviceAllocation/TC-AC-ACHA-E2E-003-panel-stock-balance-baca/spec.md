---
id: TC-AC-ACHA-E2E-003-panel-stock-balance-baca
title: "Panel Stock Balance Summary: Judul, Kuota per Entitas Aktor, dan State Loading"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-21
  - TC-AC-ACHA-22
  - TC-AC-ACHA-23
  - TC-AC-ACHA-24
coverage:
  web: automated
---

# Panel Stock Balance Summary: Judul, Kuota per Entitas Aktor, dan State Loading

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Distributor PT Global Distribusi (Pre-setup #27) `totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_TC_DIST_PASSWORD` (TC-21, TC-24). Akun kedua: Total Control Partner CV Mitra Solusi (Pre-setup #43) `totalControlPartner1_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_TC_P1_PASSWORD` (TC-22). Akun ketiga: Total Control Principal PT ABC (Pre-setup #21) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (TC-23).
- Login akun aktor pertama di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal PT ABC, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah logout dan login eksplisit.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor, flag Guided Tooltip `guided_tooltip_seen_ac-device-allocation` true untuk akun aktor, fixture API Pre-setup #20 (disediakan tim FE/BE; endpoint tidak dikarang di spec ini), dan pemulihan preferensi kolom Setup Column. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (hanya dibaca, tidak diubah): Seed 30 alokasi (Pre-setup #48) dengan nilai literal; kuota panel dihitung dari total Quantity transaksi Completed yang dikirim entitas aktor: PT Global Distribusi RFID 500 | NFC 1 | BLE 80 | GPS 9 | Handheld Reader 8 | Smart Fixed Reader 3 | BLE Gateway 65; CV Mitra Solusi RFID 60 | NFC 0 | BLE 0 | GPS 45 | Handheld Reader 6 | Smart Fixed Reader 0 | BLE Gateway 0; PT ABC RFID 0 | NFC 30 | BLE 90 | GPS 0 | Handheld Reader 20 | Smart Fixed Reader 5 | BLE Gateway 10. Fixture baseline memulihkan seed ke keadaan awal sebelum spec dijalankan (tanpa Completed tambahan).
- Stok fisik pengirim PT Global Distribusi (Hardware Stock dan TAG Stock) diatur lewat fixture Pre-setup #20 ke nilai yang berbeda dari kuota panel untuk tiap Category (nilai disediakan tim FE/BE; TC tidak menyebut nilainya), dipulihkan di hook `after`.
- General Settings Pre-setup #1 tidak diubah.
- Kemampuan teknis: intercept penundaan respons permintaan data panel selama 3 detik (TC-24), dilepas segera sesudah asersi Loading.
- State global: stok fisik pengirim diubah oleh fixture dan dipulihkan hook `after`; suite berjalan serial.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_DA_TC_DIST_PASSWORD` dan `AC_DA_TC_P1_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` dan `.env.example` pada tahap script. Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-ACHA-21: Judul, urutan Category, dan kuota entitas aktor (Distributor)

1. Amati SectionCard `Allocated quota` (halaman dibuka hook `beforeEach`)
2. Verifikasi judul SectionCard `Allocated quota` tampil di atas tabel
3. Verifikasi tujuh baris berurutan sesuai urutan Category, tiap baris memuat nama Category lalu angka kuota: RFID | NFC | BLE | GPS | Handheld Reader | Smart Fixed Reader | BLE Gateway
4. Verifikasi kuota per Category memakai total Quantity transaksi Completed yang dikirim PT Global Distribusi: RFID 500 | NFC 1 | BLE 80 | GPS 9 | Handheld Reader 8 | Smart Fixed Reader 3 | BLE Gateway 65
5. Verifikasi kuota panel tidak mengikuti stok fisik Hardware Stock atau TAG Stock (stok fisik diatur berbeda lewat fixture)

### TC-AC-ACHA-24: State Loading pada panel

6. Tahan respons permintaan data panel selama 3 detik (intercept), lalu muat ulang halaman (F5)
7. Verifikasi panel `Allocated quota` menampilkan state Loading (skeleton atau spinner)
8. Verifikasi tabel List memuat sendiri, tidak menunggu panel
9. Lepas tahanan respons (hapus intercept) dan tunggu respons diterima

### Ganti akun ke Total Control Partner CV Mitra Solusi

10. Logout dari akun Total Control Distributor
11. Login sebagai Total Control Partner CV Mitra Solusi (`totalControlPartner1_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_TC_P1_PASSWORD`)
12. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-22: Kuota Category bernilai 0

13. Amati baris Category tanpa transaksi Completed pada panel `Allocated quota`
14. Verifikasi panel menampilkan RFID 60 | NFC 0 | BLE 0 | GPS 45 | Handheld Reader 6 | Smart Fixed Reader 0 | BLE Gateway 0
15. Verifikasi Category dengan kuota 0 (NFC, BLE, Smart Fixed Reader, BLE Gateway) menampilkan angka `0` biasa tanpa indikator khusus

### Ganti akun ke Total Control Principal

16. Logout dari akun Total Control Partner CV Mitra Solusi
17. Login sebagai Total Control Principal (`totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`)
18. Buka Allocation > Device Allocation lewat sidebar

### TC-AC-ACHA-23: Panel menghitung hanya kuota entitas aktor

19. Amati panel `Allocated quota` sebagai PT ABC
20. Verifikasi tabel tetap menampilkan seluruh transaksi platform: pagination menampilkan tiga halaman untuk 30 baris
21. Verifikasi panel PT ABC menampilkan RFID 0 | NFC 30 | BLE 90 | GPS 0 | Handheld Reader 20 | Smart Fixed Reader 5 | BLE Gateway 10
22. Verifikasi kuota yang dikirim PT Global Distribusi, CV Mitra Solusi, dan PT Nusa Distribusi tidak ikut dihitung pada panel

## Notes

- Mode: FE+BE. Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Spec baca panel; tidak ada aksi tulis. Pengecualian S-12 nama literal: seed Pre-setup #48 bernilai literal (lihat spec 001 Notes).
- Urutan TC di spec: TC-21, TC-24, TC-22, TC-23 (TC-24 memakai akun yang sama dengan TC-21 sehingga ganti akun minimal). Tiga ganti akun (langkah 10 sampai 12, 16 sampai 18) adalah langkah penghubung (S-03); langkah 9 melepas intercept.
- Ukuran spec memenuhi batas sekitar 35 langkah.
- Temuan untuk QA:
  - TC-21 Expected d ("kuota tidak dibaca dari stok fisik") tidak punya data uji pembeda; spec mengatur stok fisik berbeda lewat fixture (nilai disediakan tim FE/BE) agar klausa teramati.
  - TC-24 Expected menyebut "sementara tabel List memuat sendiri" tanpa menyatakan apakah tabel boleh sudah tampil; spec mengasersi tabel memuat tanpa menunggu panel.
  - TC-23 Expected b ("kuota entitas lain tidak ikut dihitung") adalah kesimpulan dari nilai panel; diasersi lewat anchor tabel seluruh transaksi platform dan nilai panel PT ABC.
  - Post Condition TC-21 sampai TC-24 bernilai `-`.
