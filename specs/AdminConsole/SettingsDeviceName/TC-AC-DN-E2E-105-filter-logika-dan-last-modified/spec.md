---
id: TC-AC-DN-E2E-105-filter-logika-dan-last-modified
title: "Filter Panel List: Logika OR/AND dan Filter Last Modified (Rentang, Satu Hari, Inklusif, Format)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-299
  - TC-AC-DN-300
  - TC-AC-DN-301
  - TC-AC-DN-302
  - TC-AC-DN-303
  - TC-AC-DN-304
coverage:
  web: automated
---

# Filter Panel List: Logika OR/AND dan Filter Last Modified (Rentang, Satu Hari, Inklusif, Format)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `Fixture.settings-device-name.totalControl` (email `totalControlDevName_automated_{namaCompany}@qwertysystem.net`, nama tampil `Budi Santoso`, Principal), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` serta dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Data Pre-setup (hanya dibaca, tidak diubah): #15 Brand (`Brand A`, `Brand B`, `International Scanner Solutions`); #16 Device Name inti beserta SKU-nya (`Barcode Station`, `Gate Antenna`, `NFC Tag`, `RFID Reader` ber-Model R1); #17 seed 120 baris; #19 riwayat Changelog yang menentukan Last Modified (`Cable Tester` 10/09/26 12:25, `NFC Tag` 08/09/26 15:40, `Gate Antenna` 05/09/26 13:15, `Tag Reel` 15/09/26 10:10, Device Name lain 01/09/26 06:00); #20 General Settings (Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Tidak ada data Dinamis dan tidak ada aksi tulis.
- Nilai data dirujuk lewat `Fixture.settings-device-name` (belum ada, disediakan tim FE).
- State global: tidak ada yang diubah. Filter yang di-Apply dilepas lewat `[Clear Field]` lalu `[Apply]` di akhir tiap blok. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-DN-299: Beberapa opsi satu field Brand digabung OR

1. Klik ikon Filter di toolbar
2. Klik field `Brand`, centang `Brand A` dan `International Scanner Solutions`
3. Klik `[Apply]`
4. Verifikasi tabel menampilkan 4 baris: Barcode Station, Gate Antenna, NFC Tag, RFID Reader (union Brand A dan International Scanner Solutions)
5. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-DN-300: Field filter berbeda digabung AND

6. Klik ikon Filter, klik field `Brand`, centang `Brand A`
7. Klik field `Model/Type`, centang `Model R1`
8. Klik `[Apply]`
9. Verifikasi tabel menampilkan 1 baris: RFID Reader (irisan Brand A yang menghasilkan Gate Antenna, NFC Tag, RFID Reader dan Model R1 yang menghasilkan RFID Reader)
10. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-DN-301: Filter Last Modified rentang tanggal

11. Klik ikon Filter, klik field `Last Modified`
12. Pilih tanggal mulai 05/09/26 dan tanggal akhir 09/09/26
13. Klik `[Apply]`
14. Verifikasi tabel menampilkan 2 baris: Gate Antenna (Last Modified 05/09/26 13:15) dan NFC Tag (08/09/26 15:40)
15. Verifikasi Cable Tester (10/09/26 12:25), Tag Reel (15/09/26 10:10), dan Device Name ber-Last Modified 01/09/26 06:00 tidak tampil
16. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-DN-302: Filter Last Modified satu hari

17. Klik ikon Filter, klik field `Last Modified`
18. Pilih 10/09/26 sebagai tanggal mulai dan tanggal akhir
19. Klik `[Apply]`
20. Verifikasi tabel menampilkan 1 baris: Cable Tester (Last Modified 10/09/26 12:25), karena tanggal mulai sama dengan tanggal akhir bersifat inklusif
21. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-DN-303: Filter Last Modified menyertakan tanggal mulai dan tanggal akhir

22. Klik ikon Filter, klik field `Last Modified`
23. Pilih 10/09/26 sebagai tanggal mulai dan 15/09/26 sebagai tanggal akhir
24. Klik `[Apply]`
25. Verifikasi tabel menampilkan 2 baris: Cable Tester (10/09/26 12:25, di tanggal mulai) dan Tag Reel (15/09/26 10:10, di tanggal akhir)
26. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-DN-304: Format tanggal pada field Last Modified

27. Klik ikon Filter, klik field `Last Modified`
28. Pilih tanggal mulai 05/09/26 dan tanggal akhir 09/09/26
29. Verifikasi teks tanggal terpilih di dalam input mengikuti Date Format `dd/MM/yy` (05/09/26 sampai 09/09/26), bukan format lain
30. Klik `[Clear Field]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini tanpa aksi tulis.
- Langkah penghubung (S-03, S-09): langkah 5, 10, 16, 21, 26, dan 30 membersihkan Filter Panel sebelum blok berikutnya; langkah 6, 11, 17, 22, dan 27 membuka kembali Filter Panel karena panel menutup setelah `[Apply]` (lihat Temuan untuk QA).
- Urutan: mengikuti sourceTc; logika OR dan AND di awal, lalu Last Modified (rentang, satu hari, inklusif, format).
- Temuan untuk QA:
  - Perilaku Filter Panel setelah `[Apply]` tidak konsisten di TC sumber (TC-AC-DN-311 dan TC-AC-DN-312 membuka panel lagi sesudah Apply, TC-AC-DN-314 menutupnya lewat klik ikon); spec mengasumsikan panel menutup setelah `[Apply]`.
  - TC-AC-DN-301 hingga TC-AC-DN-303: asersi bergantung pada Last Modified Pre-setup #19 (bukan record milik spec); nilai itu hanya sah selama tidak ada spec lain yang mengubah record Pre-setup terkait tanpa memulihkannya.
