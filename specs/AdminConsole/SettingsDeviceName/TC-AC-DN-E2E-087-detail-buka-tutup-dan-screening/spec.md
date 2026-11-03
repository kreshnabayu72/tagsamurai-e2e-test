---
id: TC-AC-DN-E2E-087-detail-buka-tutup-dan-screening
title: "Dialog Detail: Buka (Nama dan Row Action), Screening, Tutup X/Esc, dan Backdrop"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-242
  - TC-AC-DN-240
  - TC-AC-DN-243
  - TC-AC-DN-244
  - TC-AC-DN-245
  - TC-AC-DN-241
coverage:
  web: automated
---

# Dialog Detail: Buka (Nama dan Row Action), Screening, Tutup X/Esc, dan Backdrop

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip dinyatakan di `suite.md`. Spec ini tidak mengulangnya.
- Data Pre-setup (dibaca saja, tidak diubah; nilai dirujuk lewat `Fixture.settings-device-name`): #16 Device Name inti `Gate Antenna` (Category `Antenna`, Measurement `Unit`); #18 Usage by Company untuk Device Name `Gate Antenna`: `Company A` (Principal, Total SKU 3, Total Stock 40), `Company B` (Distributor dan Client, 2, 2), `Company C` (Client, 0, 6), `Company D` (Distributor, 4, 0), `Company E` (Client, 0, 12). Daftar List default tanpa Search, Filter, atau Sidebar aktif saat spec dimulai.
- Data Dinamis: tidak ada record yang dibuat atau diubah; tabel Usage hanya dibaca.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: klik, hover, tekan Esc, dan klik area gelap di luar dialog.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-DN-242: Screening dialog Detail Device Name

1. Klik teks nama `Gate Antenna` pada kolom Device Name
2. Verifikasi judul flat `Device Name Detail` tampil pada header dialog, tanpa nama record dan tanpa breadcrumb
3. Verifikasi ikon `[X]` tampil di pojok kanan atas dialog
4. Verifikasi grid label:value dua kolom: `Device Name` bernilai `Gate Antenna`, `Measurement` bernilai `Unit`, dan `Category` bernilai satu badge `Antenna` (nama Category)
5. Hover badge `Category`
6. Verifikasi tooltip jalur penuh `Hardware > Smart Fixed Reader > Antenna` tampil
7. Verifikasi di bawah grid tampil tabel Usage by Company dengan kolom `Company`, `Entity Type`, `Total SKU`, dan `Total Stock`
8. Verifikasi toolbar tabel Usage memuat ikon Search dan Filter, dan tidak ada ikon Download
9. Verifikasi Setup Column dibuka dari trigger Column Visibility pada header kolom Actions tabel Usage
10. Verifikasi pagination tabel Usage tampil dengan default global (Page Size 10)
11. Verifikasi footer dialog tidak memuat tombol teks `Close`
12. Klik ikon `[X]` pada dialog Detail

### TC-AC-DN-240: Klik nama Device Name membuka dialog Detail di atas List

13. Klik teks nama `Gate Antenna` pada kolom Device Name
14. Verifikasi dialog dengan judul `Device Name Detail` terbuka di atas halaman List
15. Verifikasi halaman tetap `Settings > Device > Device Name` dan tidak berpindah ke halaman terpisah
16. Klik ikon `[X]` pada dialog Detail

### TC-AC-DN-243: Ikon X menutup dialog Detail

17. Klik teks nama `Gate Antenna` pada kolom Device Name
18. Klik ikon `[X]` pada dialog Detail
19. Verifikasi dialog Detail tertutup
20. Verifikasi List tampil tanpa perubahan

### TC-AC-DN-244: Esc menutup dialog Detail

21. Klik teks nama `Gate Antenna` pada kolom Device Name
22. Tekan tombol Esc
23. Verifikasi dialog Detail tertutup
24. Verifikasi List tampil tanpa perubahan

### TC-AC-DN-245: Klik backdrop tidak menutup dialog Detail

25. Klik teks nama `Gate Antenna` pada kolom Device Name
26. Klik area gelap di luar dialog
27. Verifikasi dialog Detail tetap terbuka
28. Klik ikon `[X]` pada dialog Detail

### TC-AC-DN-241: Row action Detail membuka dialog Detail yang sama

29. Klik ikon Search, ketik `Gate Antenna`, tekan Enter
30. Verifikasi baris `Gate Antenna` tampil di List
31. Klik ikon aksi pada kolom Actions baris `Gate Antenna`
32. Verifikasi Overlay Row Action tampil dengan opsi `Detail`, `Edit`, dan `Delete`
33. Klik `Detail`
34. Verifikasi dialog dengan judul `Device Name Detail` terbuka
35. Verifikasi grid menampilkan `Device Name` bernilai `Gate Antenna`
36. Verifikasi isi dialog sama seperti saat nama diklik: `Measurement` bernilai `Unit`, `Category` berbadge `Antenna`, dan tabel Usage by Company memuat lima baris `Company A` sampai `Company E`
37. Klik ikon `[X]` pada dialog Detail

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): menutup dialog Detail dengan ikon `[X]` di antara blok TC supaya blok berikut mulai dari List; Search `Gate Antenna` pada blok TC-AC-DN-241 menemukan baris target, tanpa asersi. Tidak ada form dirty (S-08 tidak berlaku).
- Urutan: blok screening (TC-AC-DN-242) di depan, lalu buka lewat nama (TC-AC-DN-240), menutup lewat `[X]` dan Esc, backdrop, dan terakhir TC-AC-DN-241 karena memakai Search yang tetap aktif sesudahnya.
- Langkah penutup `[X]` (langkah 37) menutup dialog Detail yang dibuka blok TC-AC-DN-241 supaya spec tidak berakhir dengan dialog terbuka (S-09).
- Ukuran spec: 37 langkah, di atas smell 35 langkah (satu topik dialog Detail, satu kelas harness). Tiap blok membuka dialog sendiri dari List. Data Pre-setup #16 dan #18 hanya dibaca (S-06).
- Temuan untuk QA:
  - Post Condition kosong (`-`) pada semua TC spec ini, tidak ada yang diasersi (S-01).
  - TC-AC-DN-242 butir b.iv menyebut "Setup Column dibuka dari trigger Column Visibility pada header kolom Actions"; spec hanya memverifikasi keberadaan trigger lewat teks TC, bukan pembukaan modalnya (dicakup spec Setup Column).
