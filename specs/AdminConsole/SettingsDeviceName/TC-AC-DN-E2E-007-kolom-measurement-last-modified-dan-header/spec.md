---
id: TC-AC-DN-E2E-007-kolom-measurement-last-modified-dan-header
title: "Kolom Measurement, Last Modified, Nama 120 Karakter, Header Layar Sempit, Tanpa Agregat Stok"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-18
  - TC-AC-DN-19
  - TC-AC-DN-20
  - TC-AC-DN-21
  - TC-AC-DN-22
coverage:
  web: automated
---

# Kolom Measurement, Last Modified, Nama 120 Karakter, Header Layar Sempit, Tanpa Agregat Stok

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Master Measurement (#13: `Unit`, `Meter`, `Box`), Device Name inti (#16: `Cable Tester`, `Field Radio`, `NFC Tag`, `Barcode Station`), seed 120 Device Name (#17: `Seed Device 001`), General Settings entitas uji (#20: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta), dan Device Name panjang (#23, 120 karakter). Seluruhnya baca-saja; tidak ada data Dinamis.
- Kemampuan teknis: mengubah lebar viewport (1024 px) dan memulihkannya; mengukur tinggi baris tabel.
- State global: General Settings (#20) tidak diubah.

## Test Steps

### TC-AC-DN-18: Kolom Measurement menampilkan nama Measurement sebagai teks polos

1. Verifikasi baris `Cable Tester`: Measurement teks polos `Unit`
2. Verifikasi baris `Field Radio`: Measurement teks polos `Box`
3. Verifikasi baris `NFC Tag`: Measurement teks polos `Unit`
4. Verifikasi sel Measurement pada baris `Cable Tester`, `Field Radio`, dan `NFC Tag` tidak berupa badge
5. Verifikasi tiap sel Measurement pada ketiga baris itu hanya berisi satu nilai

### TC-AC-DN-19: Kolom Last Modified mengikuti Date Format dan Time Format General Settings

6. Verifikasi baris `Cable Tester`: Last Modified `10/09/26 12:25` (waktu entri Changelog terbaru)
7. Verifikasi baris `Seed Device 001`: Last Modified `01/09/26 06:00` (record seed tanpa entri Changelog memakai waktu pembuatan)
8. Verifikasi sel Last Modified tidak pernah kosong

### TC-AC-DN-20: Device Name 120 karakter tampil penuh tanpa pemotongan dan tanpa tooltip

9. Catat tinggi baris `Barcode Station` pada List (tanpa Verifikasi)
10. Ketik Search `Zona Pemindai`, tekan Enter
11. Verifikasi sel Device Name menampilkan nama lengkap `Zona Pemindai Kode Batang Industri Tahan Banting Gudang Besar Nirkabel Pemindai Kode Batang Industri Tahan Banting Gudan` tanpa `..`
12. Verifikasi nama lengkap itu tanpa ellipsis
13. Verifikasi kolom Device Name melebar mengikuti isi (hug content)
14. Hover sel Device Name pada baris itu
15. Verifikasi hover sel tidak memunculkan tooltip
16. Verifikasi tinggi baris Device Name panjang sama dengan tinggi baris `Barcode Station` yang dicatat (satu baris)
17. Klik `(←)` pada kotak Search

### TC-AC-DN-21: Label header kolom tetap satu baris pada lebar layar sempit

18. Ubah lebar viewport menjadi 1024 px
19. Verifikasi label header kolom `Device Name`, `Category`, `Brand`, `Model/Type`, `Measurement`, dan `Last Modified` tampil dalam satu baris dengan tinggi tetap (tidak wrap ke dua baris)
20. Verifikasi tabel memakai horizontal scroll standar ketika ruang kolom tidak cukup
21. Pulihkan lebar viewport ke ukuran awal suite

### TC-AC-DN-22: List dan Column Visibility tidak memuat kolom atau agregat stok

22. Klik ikon `⋯` pada header kolom Actions
23. Verifikasi header tabel dan Overlay Column Visibility hanya memuat enam kolom data: Device Name, Category, Brand, Model/Type, Measurement, Last Modified
24. Verifikasi tidak ada kolom `Total Stock`, `Total SKU`, maupun agregat stok lintas entitas pada List
25. Tekan Esc untuk menutup Overlay Column Visibility

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Semua TC tanpa aksi tulis.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 10 (Search `Zona Pemindai`) hanya untuk menemukan baris Device Name panjang karena baris itu tidak ada di halaman 1; langkah 17 mengosongkan Search; langkah 21 memulihkan viewport; langkah 25 menutup overlay.
- TC-AC-DN-20: Expected butir c ("Tinggi baris sama dengan baris lain") tidak dapat dibandingkan setelah Search karena hanya satu baris tampil; spec mencatat tinggi baris `Barcode Station` sebelum Search (langkah 9, tanpa `Verifikasi`) sebagai pembanding.
- Temuan untuk QA:
  - TC-AC-DN-20: TC tidak menyebut baris pembanding untuk "tinggi baris sama dengan baris lain"; spec memakai baris `Barcode Station` (Pre-setup #16).
