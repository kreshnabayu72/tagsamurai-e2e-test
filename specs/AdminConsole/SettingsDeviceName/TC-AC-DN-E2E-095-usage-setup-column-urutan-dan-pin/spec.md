---
id: TC-AC-DN-E2E-095-usage-setup-column-urutan-dan-pin
title: "Usage by Company: Geser Urutan dan Pin/Unpin Kolom di Setup Column"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-633
  - TC-AC-DN-634
coverage:
  web: automated
---

# Usage by Company: Geser Urutan dan Pin/Unpin Kolom di Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip dinyatakan di `suite.md`. Spec ini tidak mengulangnya.
- Data Pre-setup (dibaca saja, tidak diubah; nilai dirujuk lewat `Fixture.settings-device-name`): #16 Device Name inti `Gate Antenna` (Category `Antenna`, Measurement `Unit`); #18 Usage by Company untuk Device Name `Gate Antenna`: `Company A` (Principal, Total SKU 3, Total Stock 40), `Company B` (Distributor dan Client, 2, 2), `Company C` (Client, 0, 6), `Company D` (Distributor, 4, 0), `Company E` (Client, 0, 12). Daftar List default tanpa Search, Filter, atau Sidebar aktif saat spec dimulai.
- Data Dinamis: tidak ada record yang dibuat atau diubah; tabel Usage hanya dibaca.
- State global: konfigurasi Setup Column tabel Usage by Company tersimpan di cache browser per user (Column Visibility, urutan, dan pin). Hook `before` dan `after` spec ini memanggil kemampuan "hapus preferensi kolom Usage di browser" (`suite.md`; disediakan tim FE) sehingga spec mulai dan berakhir dari konfigurasi default. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: klik, hover, tekan Esc, tarik-lepas (drag and drop) kolom di modal Setup Column, dan muat ulang halaman (F5).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Klik teks nama `Gate Antenna` pada kolom Device Name

### TC-AC-DN-633: Geser urutan tiap kolom tabel Usage by Company di modal Setup Column lalu Save

2. Klik trigger Column Visibility pada header kolom Actions tabel Usage, lalu klik `Setup Column...`
3. Seret `Company` ke posisi paling akhir
4. Verifikasi `Company` berada di posisi terakhir pada Live Preview
5. Seret `Entity Type` ke posisi paling akhir
6. Verifikasi `Entity Type` berada di posisi terakhir pada Live Preview
7. Seret `Total SKU` ke posisi paling akhir
8. Verifikasi `Total SKU` berada di posisi terakhir pada Live Preview
9. Seret `Total Stock` ke posisi paling akhir
10. Verifikasi `Total Stock` berada di posisi terakhir pada Live Preview
11. Seret `Total Stock` ke posisi pertama
12. Verifikasi `Total Stock` berada di posisi pertama pada Live Preview
13. Klik `[Save]`
14. Verifikasi header tabel Usage berurutan `Total Stock`, `Company`, `Entity Type`, `Total SKU`
15. Muat ulang halaman dengan F5, lalu klik teks nama `Gate Antenna` pada kolom Device Name
16. Verifikasi header tabel Usage berurutan `Total Stock`, `Company`, `Entity Type`, `Total SKU` (urutan bertahan setelah F5)
17. Klik trigger Column Visibility pada header kolom Actions tabel Usage, lalu klik `Setup Column...`
18. Hapus preferensi kolom Usage di browser, muat ulang halaman dengan F5, lalu klik teks nama `Gate Antenna` pada kolom Device Name

### TC-AC-DN-634: Pin dan unpin tiap kolom tabel Usage by Company di modal Setup Column

19. Klik trigger Column Visibility pada header kolom Actions tabel Usage, lalu klik `Setup Column...`
20. Klik ikon Pin pada `Company`
21. Verifikasi ikon Pin `Company` aktif dan Live Preview membekukan kolom di sisi kiri
22. Klik ikon Pin pada `Company` lagi
23. Verifikasi ikon Pin `Company` nonaktif dan Live Preview melepaskan kolom
24. Klik ikon Pin pada `Entity Type`
25. Verifikasi ikon Pin `Entity Type` aktif dan Live Preview membekukan kolom di sisi kiri
26. Klik ikon Pin pada `Entity Type` lagi
27. Verifikasi ikon Pin `Entity Type` nonaktif dan Live Preview melepaskan kolom
28. Klik ikon Pin pada `Total SKU`
29. Verifikasi ikon Pin `Total SKU` aktif dan Live Preview membekukan kolom di sisi kiri
30. Klik ikon Pin pada `Total SKU` lagi
31. Verifikasi ikon Pin `Total SKU` nonaktif dan Live Preview melepaskan kolom
32. Klik ikon Pin pada `Total Stock`
33. Verifikasi ikon Pin `Total Stock` aktif dan Live Preview membekukan kolom di sisi kiri
34. Klik ikon Pin pada `Total Stock` lagi
35. Verifikasi ikon Pin `Total Stock` nonaktif dan Live Preview melepaskan kolom
36. Klik ikon close `(✕)` pada modal Setup Column
37. Klik ikon `[X]` pada dialog Detail

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): sesudah blok TC-AC-DN-633, penghapusan preferensi kolom Usage di browser (kemampuan `suite.md`, hook `before`/`after` memanggilnya juga) memulihkan konfigurasi kolom tabel Usage ke default (S-09); sesudah blok TC-AC-DN-634, modal ditutup dengan ikon close `(✕)` tanpa Save dan dialog Detail ditutup dengan ikon `[X]`. Dialog dibuka kembali sesudah F5 oleh klik nama, bagian dari asersi persistensi TC-AC-DN-633.
- Asersi urutan pada Live Preview untuk tiap seretan memakai posisi yang disebut TC (posisi terakhir; posisi pertama pada seretan terakhir).
- Langkah berulang per kolom (seret, pin, unpin) ditulis per kolom dengan verifikasi masing-masing karena tiap kolom adalah butir Expected sendiri (S-01).
- Ukuran spec (37 langkah, di atas smell 35 langkah): modal Setup Column yang sama dipakai berulang untuk dua topik berbeda (seret urutan dan pin); estimasi menghitung pembukaan modal per TC, dan langkah berulang per kolom ditulis tegas karena Expected-nya per kolom.
- Temuan untuk QA:
  - Post Condition kosong (`-`) atau tanpa langkah observasi pada TC spec ini tidak diasersi (S-01).
  - TC-AC-DN-633 mencatat Post Condition "Konfigurasi urutan kolom tersimpan di cache browser tabel Usage"; spec memulihkannya dengan penghapusan preferensi kolom di browser dan tidak mengasersi isi cache.
