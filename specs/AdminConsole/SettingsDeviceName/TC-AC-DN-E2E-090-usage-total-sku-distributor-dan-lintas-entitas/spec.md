---
id: TC-AC-DN-E2E-090-usage-total-sku-distributor-dan-lintas-entitas
title: "Usage by Company: Total SKU Distributor/Client Tanpa Hitung Ganda dan Principal Lintas Entitas"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-560
  - TC-AC-DN-659
  - TC-AC-DN-660
  - TC-AC-DN-662
coverage:
  web: automated
---

# Usage by Company: Total SKU Distributor/Client Tanpa Hitung Ganda dan Principal Lintas Entitas

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE); password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip dinyatakan di `suite.md`. Spec ini tidak mengulangnya.
- Data Pre-setup (dibaca saja, tidak diubah; nilai dirujuk lewat `Fixture.settings-device-name`): #16 Device Name inti `Gate Antenna`; #18 Usage by Company untuk Device Name `Gate Antenna`: `Company A` (Principal, Total SKU 3, Total Stock 40), `Company B` (Distributor dan Client, 2, 2), `Company C` (Client, 0, 6), `Company D` (Distributor, 4, 0), `Company E` (Client, 0, 12). Daftar List default tanpa Search, Filter, atau Sidebar aktif saat spec dimulai.
- Data tambahan Usage (dibuat dan dibersihkan fixture BE yang disediakan tim FE/BE, pengecualian fixture di `suite.md`): Company F (Client; enam unit dari satu SKU `Gate Antenna`; Total SKU 1, Total Stock 6), Company G (Distributor; Total SKU 2, Total Stock 5), Company H (Distributor dan Client; Total SKU 3, Total Stock 4), dan Company I (Distributor bukan Client; Total SKU 3, Total Stock 3) ditambahkan fixture BE satu per satu sebelum blok TC yang memakainya, dan keempatnya dihapus di hook `after` spec ini. Penambahan berurutan menjaga blok TC-AC-DN-560 hanya memuat enam Company.
- Data Dinamis: tidak ada record yang dibuat lewat UI; tabel Usage hanya dibaca.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: klik, ketik, dan membaca isi sel tabel Usage by Company; fixture BE untuk menambah dan menghapus data Usage Company F sampai I.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-DN-560: Principal melihat penggunaan Device Name lintas entitas pada dialog Detail

1. Tambahkan lewat fixture BE data Company F pada Device Name `Gate Antenna`: Company F bertipe Client memiliki enam unit stok terdaftar dari satu SKU `Gate Antenna`
2. Klik teks nama `Gate Antenna` pada kolom Device Name
3. Verifikasi dialog `Device Name Detail` terbuka dan tabel Usage by Company memuat baris `Company A`, `Company B`, `Company C`, `Company D`, `Company E`, dan `Company F`
4. Verifikasi baris `Company A` berbadge `Principal` dengan Total SKU `3` dan Total Stock `40`
5. Verifikasi baris `Company B` berbadge `Distributor` dan `Client` dengan Total SKU `2` dan Total Stock `2`
6. Verifikasi baris `Company C` berbadge `Client` dengan Total SKU `0` dan Total Stock `6`
7. Verifikasi baris `Company D` berbadge `Distributor` dengan Total SKU `4` dan Total Stock `0`
8. Verifikasi baris `Company E` berbadge `Client` dengan Total SKU `0` dan Total Stock `12`
9. Verifikasi baris `Company F` berbadge `Client` dengan Total SKU `1` (jumlah SKU berbeda Device Name yang unitnya tercatat pada Company F) dan Total Stock `6`
10. Verifikasi tidak ada baris berbadge `Partner`
11. Klik ikon `[X]` pada dialog Detail

### TC-AC-DN-659: Distributor yang barisnya tampil hanya karena memegang unit SKU Principal hasil alokasi menampilkan Total SKU dari SKU berbeda pada unit tercatatnya

12. Tambahkan lewat fixture BE data Company G pada Device Name `Gate Antenna`: Company G bertipe Distributor tidak membuat SKU `Gate Antenna` dan memegang lima unit hasil alokasi dari dua SKU Principal `Gate Antenna` berbeda, tiga unit dan dua unit
13. Klik teks nama `Gate Antenna` pada kolom Device Name
14. Klik ikon Search pada toolbar tabel Usage, ketik `company g`, tekan Enter
15. Verifikasi satu baris `Company G` dengan satu badge `Distributor`
16. Verifikasi kolom Total SKU baris `Company G` bernilai `2` dan bukan `0`
17. Verifikasi kolom Total Stock baris `Company G` bernilai `5`
18. Klik ikon `[X]` pada dialog Detail

### TC-AC-DN-660: Distributor yang juga Client menghitung Total SKU sebagai gabungan SKU yang dibuat dan SKU pada unit tercatat tanpa hitung ganda

19. Tambahkan lewat fixture BE data Company H pada Device Name `Gate Antenna`: Company H bertipe Distributor dan Client membuat dua SKU `Gate Antenna` (SKU pertama dengan tiga unit tercatat, SKU kedua tanpa unit) dan mencatat satu unit dari SKU Principal hasil alokasi
20. Klik teks nama `Gate Antenna` pada kolom Device Name
21. Klik ikon Search pada toolbar tabel Usage, ketik `company h`, tekan Enter
22. Verifikasi satu baris `Company H` dengan dua badge eksplisit sekaligus: `Distributor` dan `Client`
23. Verifikasi kolom Total SKU baris `Company H` bernilai `3`, bukan `2` dan bukan `4`
24. Verifikasi kolom Total Stock baris `Company H` bernilai `4`
25. Klik ikon `[X]` pada dialog Detail

### TC-AC-DN-662: Distributor bukan Client yang membuat SKU sekaligus memegang unit SKU Principal hasil alokasi menampilkan Total SKU gabungan tanpa hitung ganda

26. Tambahkan lewat fixture BE data Company I pada Device Name `Gate Antenna`: Company I bertipe Distributor (bukan Client) membuat dua SKU `Gate Antenna` (SKU pertama dengan satu unit tercatat, SKU kedua tanpa unit) dan memegang dua unit dari satu SKU Principal hasil alokasi
27. Klik teks nama `Gate Antenna` pada kolom Device Name
28. Klik ikon Search pada toolbar tabel Usage, ketik `company i`, tekan Enter
29. Verifikasi satu baris `Company I` dengan satu badge `Distributor`
30. Verifikasi baris `Company I` tidak berbadge `Client`
31. Verifikasi kolom Total SKU baris `Company I` bernilai `3`, bukan `2` dan bukan `4`
32. Verifikasi kolom Total Stock baris `Company I` bernilai `3`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah fixture penambah Company F, G, H, dan I serta langkah menutup dialog Detail dengan ikon `[X]` di antara blok TC. Menutup dialog mengembalikan Search tabel Usage ke default sehingga Search `company g`, `company h`, dan `company i` tidak saling bergantung.
- Urutan: TC-AC-DN-560 di depan karena mengasersi tepat enam Company (`Company A` sampai `Company F`); sesudahnya Company G, H, dan I ditambahkan berurutan.
- Temuan untuk QA:
  - Post Condition kosong (`-`) pada semua TC spec ini (S-01).
  - Pre-setup #18 menyebut `Company F` hanya untuk TC-AC-DN-251, tetapi TC-AC-DN-560 menyebut enam Company A sampai F pada `Gate Antenna`; spec menambahkan `Company F` lewat fixture sebelum TC-AC-DN-560. Nama `Company F` sampai `Company I` ditulis literal sesuai TC karena berasal dari data uji TC, bukan record yang ditulis lewat UI (S-12).
  - TC-AC-DN-659 hingga TC-AC-DN-662 memakai skenario alokasi SKU Principal ke Distributor yang disiapkan fixture BE; kemampuan itu disediakan tim FE/BE.
