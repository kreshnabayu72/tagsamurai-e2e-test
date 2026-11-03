---
id: TC-AC-DN-E2E-110-sort-aturan-seri-kosong-dan-last-modified
title: "Sort List: Seri Brand, Posisi Baris Kosong, Last Modified, dan Urutan Badge"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-DN-320
  - TC-AC-DN-321
  - TC-AC-DN-322
  - TC-AC-DN-323
coverage:
  web: automated
---

# Sort List: Seri Brand, Posisi Baris Kosong, Last Modified, dan Urutan Badge

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #15 Brand; #16 Device Name inti beserta SKU-nya (`NFC Tag` ber-Brand A, `Barcode Station` ber-Brand `International Scanner Solutions`, `RFID Reader` ber-Brand A/B/C dan Model R1/R2/R3, `Cable Tester`, `Door Antenna`, `Field Radio`, dan `Tag Reel` tanpa SKU); #17 seed 120 baris; #19 riwayat Changelog yang menentukan Last Modified (`Cable Tester` 10/09/26 12:25, `NFC Tag` 08/09/26 15:40, `Gate Antenna` 05/09/26 13:15, `Tag Reel` 15/09/26 10:10, lainnya 01/09/26 06:00); #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Tidak ada data Dinamis dan tidak ada aksi tulis.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- State global: tidak ada yang diubah. Sort dikembalikan ke netral di akhir tiap blok. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-320: Seri Brand diurut alfabetis berdasarkan nilai pertama

1. Klik header `Brand`
2. Verifikasi ascending: NFC Tag (nilai pertama `Brand A`) tampil sebelum Barcode Station (nilai pertama `International Scanner Solutions`)
3. Klik header `Brand` lagi
4. Verifikasi descending: Barcode Station tampil sebelum NFC Tag (Z-A pada nilai pertama)

### TC-AC-DN-321: Posisi baris tanpa Brand dan tanpa Model/Type

5. Klik header `Brand` ketiga kali (netral)
6. Verifikasi sel Brand dan Model/Type pada baris Cable Tester, Door Antenna, dan Field Radio tampil `—`
7. Klik header `Brand`
8. Verifikasi Brand ascending: baris ber-Brand (NFC Tag, Legacy Scanner, Barcode Station, Gate Antenna, RFID Reader) tampil lebih dulu, lalu baris bernilai `—` yang dimulai Cable Tester, Door Antenna, Field Radio; tidak ada baris ber-Brand setelah baris `—` pertama
9. Verifikasi urutan antar baris bernilai `—` mengikuti default sort tabel (Device Name A-Z)
10. Klik header `Brand` lagi
11. Verifikasi Brand descending: halaman 1 hanya memuat baris bernilai `—` yang dimulai Cable Tester, Door Antenna, Field Radio
12. Verifikasi NFC Tag, Legacy Scanner, Barcode Station, Gate Antenna, dan RFID Reader tidak tampil di halaman 1
13. Verifikasi urutan antar baris bernilai `—` mengikuti default sort tabel (Device Name A-Z)
14. Klik header `Brand` ketiga kali (netral)
15. Klik header `Model/Type`
16. Verifikasi Model/Type ascending: baris ber-Model/Type tampil lebih dulu, lalu baris bernilai `—` yang dimulai Cable Tester, Door Antenna, Field Radio
17. Verifikasi urutan antar baris bernilai `—` mengikuti default sort tabel (Device Name A-Z)
18. Klik header `Model/Type` lagi
19. Verifikasi Model/Type descending: halaman 1 hanya memuat baris bernilai `—` yang dimulai Cable Tester, Door Antenna, Field Radio
20. Verifikasi urutan antar baris bernilai `—` mengikuti default sort tabel (Device Name A-Z)
21. Klik header `Model/Type` ketiga kali (netral)

### TC-AC-DN-322: Siklus sort Last Modified

22. Klik header `Last Modified`
23. Verifikasi Oldest First: panah naik dan halaman 1: Barcode Station, Door Antenna, Field Radio, Legacy Scanner, RFID Reader, Seed Device 001 sampai Seed Device 005 (01/09/26 06:00 diurut Device Name A-Z)
24. Klik header `Last Modified` lagi
25. Verifikasi Newest First: panah turun dan halaman 1: Tag Reel (15/09/26 10:10), Cable Tester (10/09/26 12:25), NFC Tag (08/09/26 15:40), Gate Antenna (05/09/26 13:15), Barcode Station, Door Antenna, Field Radio, Legacy Scanner, RFID Reader, Seed Device 001
26. Klik header `Last Modified` ketiga kali
27. Verifikasi panah hilang
28. Verifikasi urutan kembali ke default Device Name A-Z

### TC-AC-DN-323: Urutan badge di dalam sel tetap A-Z saat Brand descending

29. Klik header `Brand` dua kali (descending)
30. Verifikasi sel Brand RFID Reader menampilkan `Brand A`, `Brand B`, lalu chip `+1 more` (bukan urutan terbalik)
31. Verifikasi sel Model/Type RFID Reader menampilkan `Model R1`, `Model R2`, lalu chip `+1 more`
32. Klik header `Brand` ketiga kali (netral)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis.
- Langkah penghubung (S-03, S-09): langkah 5, 14, 21, dan 32 mengembalikan sort ke netral sebelum blok berikutnya.
- Urutan: mengikuti sourceTc.
- Temuan untuk QA:
  - TC-AC-DN-321 Expected f ("urutan antar baris bernilai `—` mengikuti default sort pada keempat urutan") ditulis satu `Verifikasi` per urutan (langkah 9, 13, 17, 20).
