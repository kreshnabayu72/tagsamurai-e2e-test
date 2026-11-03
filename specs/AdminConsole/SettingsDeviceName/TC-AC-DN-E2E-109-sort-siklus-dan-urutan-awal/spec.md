---
id: TC-AC-DN-E2E-109-sort-siklus-dan-urutan-awal
title: "Sort List: Urutan Awal dan Siklus Tiga Tahap Kolom Teks serta Hitungan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-317
  - TC-AC-DN-318
  - TC-AC-DN-319
coverage:
  web: automated
---

# Sort List: Urutan Awal dan Siklus Tiga Tahap Kolom Teks serta Hitungan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #16 Device Name inti beserta Category, Measurement, dan jumlah Brand serta Model/Type per Device Name (`NFC Tag` 1, `Legacy Scanner` 1, `Barcode Station` 1, `Gate Antenna` 2, `RFID Reader` 3); #17 seed `Seed Device 001` sampai `Seed Device 120` (Accessory, Unit); #23 nama panjang 120 karakter (`Zona Pemindai Kode Batang Industri Tahan Banting Gudang Besar Nirkabel Pemindai Kode Batang Industri Tahan Banting Gudan`); total 130 baris. Tidak ada data Dinamis dan tidak ada aksi tulis.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- State global: tidak ada yang diubah. Sort kolom dikembalikan ke netral di akhir tiap siklus. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-317: Urutan awal List adalah Device Name A-Z

1. Verifikasi halaman 1 menampilkan urutan: Barcode Station, Cable Tester, Door Antenna, Field Radio, Gate Antenna, Legacy Scanner, NFC Tag, RFID Reader, Seed Device 001, Seed Device 002
2. Verifikasi urutan alfabetis tidak membedakan huruf besar-kecil

### TC-AC-DN-318: Siklus sort tiga tahap kolom teks Device Name, Category, dan Measurement

3. Klik header `Device Name`
4. Verifikasi panah naik aktif dan urutan A-Z
5. Verifikasi baris pertama Barcode Station
6. Klik header `Device Name` lagi
7. Verifikasi panah turun aktif dan urutan Z-A
8. Verifikasi halaman 1 dimulai `Zona Pemindai Kode Batang Industri Tahan Banting Gudang Besar Nirkabel Pemindai Kode Batang Industri Tahan Banting Gudan`, lalu Tag Reel, diikuti Seed Device 120 sampai Seed Device 113
9. Klik header `Device Name` ketiga kali
10. Verifikasi panah sort hilang
11. Verifikasi urutan kembali ke default A-Z (halaman 1: Barcode Station, Cable Tester, Door Antenna, Field Radio, Gate Antenna, Legacy Scanner, NFC Tag, RFID Reader, Seed Device 001, Seed Device 002)
12. Klik header `Category`
13. Verifikasi ascending berdasarkan nama badge, halaman 1: Cable Tester, Field Radio, lalu Seed Device 001 sampai Seed Device 008 (Accessory; nilai sama diurut Device Name A-Z)
14. Klik header `Category` lagi
15. Verifikasi descending, halaman 1: Legacy Scanner, RFID Reader (badge UHF Handheld), NFC Tag, Tag Reel (badge Tag), Barcode Station, Door Antenna, Gate Antenna, Cable Tester, Field Radio, Seed Device 001
16. Klik header `Category` ketiga kali
17. Verifikasi netral dan urutan kembali ke default A-Z
18. Klik header `Measurement`
19. Verifikasi ascending: baris pertama Field Radio (Box) dan Tag Reel (Meter) berada sebelum semua baris ber-Measurement Unit
20. Klik header `Measurement` lagi
21. Verifikasi descending: baris pertama Barcode Station (Unit)
22. Klik header `Measurement` ketiga kali
23. Verifikasi netral dan urutan kembali ke default A-Z

### TC-AC-DN-319: Siklus sort tiga tahap kolom hitungan Brand dan Model/Type

24. Klik header `Brand`
25. Verifikasi urutan relatif baris ber-Brand menaik berdasarkan jumlah nilai: NFC Tag (1), Legacy Scanner (1), Barcode Station (1), Gate Antenna (2), RFID Reader (3)
26. Klik header `Brand` lagi
27. Verifikasi urutan relatif menurun: RFID Reader (3), Gate Antenna (2), Barcode Station (1), Legacy Scanner (1), NFC Tag (1)
28. Klik header `Brand` ketiga kali
29. Verifikasi netral dan urutan kembali ke default A-Z
30. Klik header `Model/Type`
31. Verifikasi urutan relatif menaik: Barcode Station (1), Legacy Scanner (1), NFC Tag (1), Gate Antenna (2), RFID Reader (3)
32. Klik header `Model/Type` lagi
33. Verifikasi urutan relatif menurun: RFID Reader (3), Gate Antenna (2), NFC Tag (1), Legacy Scanner (1), Barcode Station (1)
34. Klik header `Model/Type` ketiga kali
35. Verifikasi netral dan urutan kembali ke default A-Z

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis.
- Urutan: mengikuti sourceTc; urutan awal (TC-AC-DN-317) di awal, lalu kolom teks, lalu kolom hitungan.
- Langkah penghubung (S-03, S-09): klik ketiga tiap kolom (langkah 9, 16, 22, 28, 34) mengembalikan sort ke netral sebelum kolom berikutnya.
- Temuan untuk QA:
  - TC-AC-DN-317 Expected b ("urutan alfabetis tidak membedakan huruf besar-kecil") tidak punya data pembeda huruf besar-kecil di halaman 1; spec mengasersinya pada daftar halaman 1 dan perilaku collation en-US diuji di TC-AC-DN-326.
  - TC-AC-DN-319 menulis hanya urutan relatif untuk baris ber-Brand/Model; spec tidak menambahkan asersi posisi baris tanpa nilai (itu TC-AC-DN-321).
