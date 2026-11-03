---
id: TC-AC-DN-E2E-089-usage-company-khusus-dan-empty
title: "Usage by Company: Company Client Total SKU 1, BYO Tanpa SKU, Partner Murni, Agregat Stok, dan Empty"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-252
  - TC-AC-DN-253
  - TC-AC-DN-254
  - TC-AC-DN-255
  - TC-AC-DN-256
  - TC-AC-DN-251
coverage:
  web: automated
---

# Usage by Company: Company Client Total SKU 1, BYO Tanpa SKU, Partner Murni, Agregat Stok, dan Empty

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip dinyatakan di `suite.md`. Spec ini tidak mengulangnya.
- Data Pre-setup (dibaca saja, tidak diubah; nilai dirujuk lewat `Fixture.settings-device-name`): #16 Device Name inti `Gate Antenna`, `Field Radio` (tanpa SKU, unit BYO Hardware), `Tag Reel` (tanpa SKU, unit BYO TAG), dan `Cable Tester` (tanpa SKU, tanpa unit BYO); #18 Usage by Company untuk Device Name `Gate Antenna`: `Company A` (Principal, Total SKU 3, Total Stock 40), `Company B` (Distributor dan Client, 2, 2), `Company C` (Client, 0, 6), `Company D` (Distributor, 4, 0), `Company E` (Client, 0, 12); Usage `Field Radio`: `Company E` (Client, 0, 5); Usage `Tag Reel`: `Company E` (Client, 0, 3); Usage `Cable Tester`: tanpa baris; #22 unit BYO milik `Company E` disiapkan fixture BE; #10 entitas `Partner Jaringan` (Partner tanpa Client turunan yang memakai `Gate Antenna`). Daftar List default tanpa Search, Filter, atau Sidebar aktif saat spec dimulai.
- Data tambahan Usage (dibuat dan dibersihkan fixture BE yang disediakan tim FE/BE, pengecualian fixture di `suite.md`): `Company F` (Client; enam unit stok terdaftar dari satu SKU `Gate Antenna`; Total SKU 1, Total Stock 6) ditambahkan fixture BE sebelum blok TC-AC-DN-251 dan dihapus di hook `after` spec ini. Penambahan dilakukan sesudah blok lain karena blok TC-AC-DN-254 dan TC-AC-DN-255 mengasumsikan hanya lima baris Company.
- Data Dinamis: tidak ada record yang dibuat lewat UI; tabel Usage hanya dibaca.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: klik dan membaca isi sel tabel Usage by Company; fixture BE untuk menambah dan menghapus data Usage Company F.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-DN-252: Usage Device Name dengan unit BYO Hardware menampilkan stok tanpa SKU

1. Klik teks nama `Field Radio` pada kolom Device Name
2. Verifikasi dialog `Device Name Detail` terbuka dan tabel Usage memuat satu baris `Company E` dengan badge `Client`
3. Verifikasi baris `Company E` menampilkan Total SKU `0` dan Total Stock `5`
4. Klik ikon `[X]` pada dialog Detail

### TC-AC-DN-253: Usage Device Name dengan unit BYO TAG menampilkan stok tanpa SKU

5. Klik teks nama `Tag Reel` pada kolom Device Name
6. Verifikasi dialog `Device Name Detail` terbuka dan tabel Usage memuat satu baris `Company E` dengan badge `Client`
7. Verifikasi baris `Company E` menampilkan Total SKU `0` dan Total Stock `3`
8. Klik ikon `[X]` pada dialog Detail

### TC-AC-DN-254: Partner murni tidak memiliki baris pada Usage by Company

9. Klik teks nama `Gate Antenna` pada kolom Device Name
10. Verifikasi tabel Usage memuat lima baris `Company A` sampai `Company E`
11. Verifikasi tidak ada baris untuk `Partner Jaringan`
12. Verifikasi badge Entity Type pada seluruh baris hanya berupa `Principal`, `Distributor`, atau `Client`, dan tidak ada badge `Partner`
13. Klik ikon `[X]` pada dialog Detail

### TC-AC-DN-255: Dialog Detail dan List tidak menampilkan agregat stok lintas entitas

14. Verifikasi List Device Name menampilkan enam kolom data: `Device Name`, `Category`, `Brand`, `Model/Type`, `Measurement`, dan `Last Modified`
15. Verifikasi List tidak memiliki kolom stok
16. Klik teks nama `Gate Antenna` pada kolom Device Name
17. Verifikasi tabel Usage hanya memuat baris Company `Company A` sampai `Company E` dan tidak memuat baris atau kolom jumlah total stok lintas Company
18. Verifikasi nilai Total Stock hanya tampil per baris Company
19. Klik ikon `[X]` pada dialog Detail

### TC-AC-DN-256: Usage kosong menampilkan empty state

20. Klik teks nama `Cable Tester` pada kolom Device Name
21. Verifikasi dialog `Device Name Detail` terbuka
22. Verifikasi tabel Usage menampilkan empty state "No usage data yet"
23. Verifikasi tidak ada pesan error
24. Klik ikon `[X]` pada dialog Detail

### TC-AC-DN-251: Baris Company bertipe Client dengan unit dari satu SKU menampilkan Total SKU 1

25. Tambahkan lewat fixture BE data Company F pada Device Name `Gate Antenna`: Company F bertipe Client memiliki enam unit stok terdaftar dari satu SKU `Gate Antenna`
26. Klik teks nama `Gate Antenna` pada kolom Device Name
27. Verifikasi dialog `Device Name Detail` terbuka dan tabel Usage memuat baris `Company F` dengan satu badge `Client`
28. Verifikasi baris `Company F` menampilkan Total SKU `1`
29. Verifikasi baris `Company F` menampilkan Total Stock `6`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): menutup dialog Detail dengan ikon `[X]` di antara blok TC; langkah fixture penambah Company F sebelum blok TC-AC-DN-251.
- Urutan: TC-AC-DN-251 ditaruh di akhir karena TC-AC-DN-254 mengasersi tabel Usage hanya berisi lima baris `Company A` sampai `Company E`, dan data `Company F` ditambahkan khusus untuk TC-AC-DN-251 menurut TC sumber.
- Ukuran spec: di bawah smell 35 langkah.
- Temuan untuk QA:
  - Post Condition kosong (`-`) pada semua TC spec ini (S-01).
  - Pre-setup #18 mencantumkan `Company F` untuk `Gate Antenna` dan menyebut baris itu "hanya untuk TC khusus Total SKU baris Client" (TC-AC-DN-251), sedangkan TC-AC-DN-246 hingga TC-AC-DN-255 menyebut lima baris `Company A` sampai `Company E`. Spec memperlakukan `Company F` sebagai data tambahan yang ditambahkan fixture hanya untuk blok TC-AC-DN-251; nama `Company F` ditulis literal sesuai TC karena nama Company berasal dari data uji TC, bukan record yang ditulis lewat UI (S-12).
  - TC-AC-DN-252 dan TC-AC-DN-253 mensyaratkan unit BYO milik `Company E` dari Jalur B (Pre-setup #22); spec memakai data fixture BE yang disediakan tim FE/BE.
