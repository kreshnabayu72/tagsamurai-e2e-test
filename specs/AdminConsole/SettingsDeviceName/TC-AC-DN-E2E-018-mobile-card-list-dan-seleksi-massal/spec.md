---
id: TC-AC-DN-E2E-018-mobile-card-list-dan-seleksi-massal
title: "Mobile: Card List, Long Press, dan Floating Bottom Bulk Bar"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-47
  - TC-AC-DN-48
  - TC-AC-DN-49
coverage:
  mobile: automated
---

# Mobile: Card List, Long Press, dan Floating Bottom Bulk Bar

## Prerequisites

- Mode: FE+BE (mobile Android).
- Akun aktor: Total Control (Pre-setup #1) `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini pada aplikasi mobile Android; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `beforeEach` suite membuka `Settings > Device > Device Name` pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes` (bukan pengganti langkah pemulihan di spec ini); hook `before` suite menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` ke `seen` dan hook `after` suite memulihkannya.
- Perangkat Android uji bersama untuk spec mobile (disediakan tim FE/BE); `parallel: false`. Aplikasi mobile Android dijalankan pada perangkat itu; kemampuan long press sekitar 500 ms dan ketuk disediakan harness mobile.
- Suite berjalan serial (`parallel: false`) karena memakai state global bersama (lihat `suite.md`). Spec ini tidak mengubah Pre-setup bersama: data Device Name inti (Pre-setup #16), seed 120 baris (#17), dan nama panjang (#23) hanya dibaca.
- Nilai data Pre-setup dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); teks yang diasersi ditulis persis seperti di TC.
- Data Pre-setup: Device Name inti (#16: `Barcode Station`, `Cable Tester`, `Door Antenna`) dan seed 120 Device Name (#17); baca-saja. Tidak ada data Dinamis dan tidak ada aksi tulis (seleksi dibatalkan di akhir tiap TC).

## Test Steps

### TC-AC-DN-47: Tabel runtuh menjadi Card List pada aplikasi mobile

1. Gunakan aplikasi mobile Android pada perangkat uji dan buka halaman `Settings > Device > Device Name`
2. Verifikasi daftar Device Name tampil sebagai card, satu card per Device Name, card pertama Barcode Station
3. Verifikasi header tabel dan kolom tidak tampil
4. Verifikasi card `Cable Tester` menampilkan tiga field: Device Name `Cable Tester`, Category `Accessory`, dan Measurement `Unit`
5. Verifikasi Brand, Model/Type, dan Last Modified tidak ditampilkan pada card
6. Verifikasi tidak ada kotak centang permanen pada card
7. Verifikasi Category Sidebar tidak tampil bersamaan dengan daftar card

### TC-AC-DN-48: Long press pada card masuk ke mode seleksi massal

8. Long press selama sekitar 500 ms pada card `Cable Tester`
9. Verifikasi card `Cable Tester` berstatus terpilih dengan sorotan visual
10. Verifikasi kotak seleksi kosong muncul di card lain pada daftar
11. Verifikasi Floating Contextual Bottom Bulk Action Bar muncul di bagian bawah layar
12. Ketuk tombol tutup `[✕]` pada Bulk Bar

### TC-AC-DN-49: Floating Bottom Bulk Bar menampilkan tombol tutup, penghitung, Select All, dan Delete

13. Long press selama sekitar 500 ms pada card `Cable Tester`
14. Verifikasi penghitung `1 Selected` tampil sebelum card kedua diketuk
15. Ketuk card `Door Antenna`
16. Verifikasi Bulk Bar memuat tombol tutup `[✕]`, penghitung `2 Selected`, tombol `[Select All]`, dan tombol `[Delete]` berseverity danger
17. Ketuk tombol tutup `[✕]` pada Bulk Bar

## Notes

- Mode: FE+BE (mobile Android). Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. `coverage.mobile: automated` (hanya spec yang berjalan di aplikasi mobile; tanpa `coverage.web`).
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 1: tampilan mobile diaktifkan dengan menjalankan aplikasi mobile Android; halaman dibuka hook `beforeEach` suite pada aplikasi tersebut.
- Langkah penghubung (S-03, S-09): langkah 12 dan 17 membatalkan mode seleksi supaya TC berikutnya dimulai dari daftar card tanpa seleksi.
- TC-AC-DN-47: asersi absence header tabel dan kolom didahului `Verifikasi` daftar card tampil sebagai anchor positif (bagian 8b butir 2).
- TC-AC-DN-49: Expected butir b (`1 Selected` sebelum card kedua diketuk) diasersi sebelum ketukan kedua sesuai urutan state (bagian 8b butir 5).
- Temuan untuk QA: tidak ada temuan sumber untuk TC dalam spec ini (precondition, Expected, dan data konsisten).
