---
id: TC-FA-FAAC-E2E-129-download-isi-berkas-csv-xlsx
title: "Download Tabel Asset Class: Isi Berkas CSV dan XLSX (Nilai Sel, BOM, Sheet, Urutan Baris, dan Kesamaan dengan Tabel, serta Cakupan Search dan Filter)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-422
  - TC-FA-FAAC-427
  - TC-FA-FAAC-428
  - TC-FA-FAAC-429
  - TC-FA-FAAC-432
  - TC-FA-FAAC-433
  - TC-FA-FAAC-434
  - TC-FA-FAAC-656
coverage:
  web: automated
---

# Download Tabel Asset Class: Isi Berkas CSV dan XLSX (Nilai Sel, BOM, Sheet, Urutan Baris, dan Kesamaan dengan Tabel, serta Cakupan Search dan Filter)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ (Class Name Heavy Equipment; Commercial `Straight Line · 10 yrs · 10%`; Fiscal `Bukan bangunan – Kelompok 3 · Declining Balance`; Capitalization Threshold 5,000,000; Modified By Rina P, nama lengkap Rina Pratiwi), VEHICLES (Capitalization Threshold Default), IT-EQ (Commercial `Declining Balance · 4 yrs · 50%/yr · 5%`; Modified By System), MACHINERY, BLDG, STORAGE (Storage Equipment), OFFICE-NEW, LAND (Fiscal `Tanah`) (Active) dan OFFICE-OLD (Inactive). Kondisi Accounts: BLDG lengkap, MACHINERY belum lengkap, IT-EQ memiliki akun Inactive. Search `equip` mencocokkan HEAVY-EQ, IT-EQ, OFFICE-NEW, OFFICE-OLD, dan STORAGE; filter Active = Active menyisakan empat di antaranya (tanpa OFFICE-OLD) (TC-FA-FAAC-422).
- Populasi tabel nyata: tabel memuat sembilan kelas contoh ditambah seed lain (`B-*`, `PMP-01`, `TEMP-EQ`, dan seed spec lain), sehingga baris contoh dijangkau lewat Search kode Class Code dan baris seed lain tidak diasersi.
- Data Pre-setup tambahan (hanya dibaca; TC-FA-FAAC-432): Asset Class PMP-01 dengan Class Name `Pump, "Heavy" Duty`. Seed disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: pembaca berkas unduhan CSV/XLSX (byte awal, sel, tipe sel, daftar sheet) disediakan tim FE; unduhan dicegat browser uji pada folder unduhan sementara.
- State yang diubah spec: konfigurasi kolom tabel (kolom Modified By ditampilkan oleh langkah 19 lalu disembunyikan oleh langkah 34), sort Class Name (dikembalikan oleh langkah 18), dan Search serta Filter (dilepas oleh langkah 41 dan 42). Pemulihan cadangan di hook `after` dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Berkas CSV (TC-FA-FAAC-427, 428, 432)

1. Klik icon Download lalu pilih `Download as CSV`
2. Buka berkas dengan pembaca CSV dan periksa byte awal

### TC-FA-FAAC-427: Nilai kolom Active ditulis Active atau Inactive di berkas

3. Verifikasi baris HEAVY-EQ pada kolom Active bernilai `Active`
4. Verifikasi baris OFFICE-OLD pada kolom Active bernilai `Inactive`

### TC-FA-FAAC-428: Nilai kolom Accounts ditulis Complete, Incomplete, atau Has inactive account

5. Verifikasi baris BLDG pada kolom Accounts bernilai `Complete`
6. Verifikasi baris MACHINERY pada kolom Accounts bernilai `Incomplete`
7. Verifikasi baris IT-EQ pada kolom Accounts bernilai `Has inactive account`

### TC-FA-FAAC-432: Berkas CSV berenkode UTF-8 BOM dengan escaping nilai

8. Verifikasi berkas diawali BOM UTF-8
9. Verifikasi Class Name `Pump, "Heavy" Duty` pada baris PMP-01 terbaca sebagai satu sel utuh (koma dan tanda kutip ter-escape)

### Berkas XLSX (TC-FA-FAAC-429, 433)

10. Klik icon Download lalu pilih `Download as XLSX`
11. Buka berkas dengan pembaca XLSX dan periksa daftar sheet

### TC-FA-FAAC-429: Nilai Capitalization Threshold di berkas

12. Verifikasi baris HEAVY-EQ pada kolom Capitalization Threshold berupa sel angka 5000000 tanpa simbol dan pemisah ribuan
13. Verifikasi baris VEHICLES (tanpa nilai) pada kolom Capitalization Threshold bernilai `Default`

### TC-FA-FAAC-433: Berkas XLSX memiliki satu sheet bernama Sheet1

14. Verifikasi berkas memiliki satu sheet bernama `Sheet1`

### TC-FA-FAAC-434: Urutan baris berkas mengikuti sort aktif

15. Klik header Class Name dua kali (Z-A)
16. Klik icon Download lalu pilih `Download as CSV`
17. Verifikasi baris contoh Vehicles berada sebelum Storage Equipment pada berkas yang berurutan menurut Class Name Z-A

### TC-FA-FAAC-656: Nilai Commercial dan Fiscal di berkas Download identik dengan sel tabel dan Modified By berupa nama lengkap

18. Klik header Class Name sekali lagi
19. Aktifkan kolom Modified By lewat Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`, centang Modified By), klik `[Save]`
20. Ketik Search `HEAVY-EQ`, tekan Enter
21. Catat teks sel Commercial, Fiscal, dan Modified By baris HEAVY-EQ di tabel
22. Verifikasi sel Modified By baris HEAVY-EQ di tabel `Rina P`
23. Ganti isi kotak search dengan `IT-EQ`, tekan Enter
24. Catat teks sel Commercial, Fiscal, dan Modified By baris IT-EQ di tabel
25. Ganti isi kotak search dengan `LAND`, tekan Enter
26. Catat teks sel Commercial, Fiscal, dan Modified By baris LAND di tabel
27. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
28. Klik icon Download lalu pilih `Download as CSV`
29. Verifikasi HEAVY-EQ: Commercial `Straight Line · 10 yrs · 10%` dan Fiscal `Bukan bangunan – Kelompok 3 · Declining Balance` di berkas sama persis dengan sel tabel
30. Verifikasi HEAVY-EQ: Modified By di berkas `Rina Pratiwi` (nama lengkap utuh)
31. Verifikasi IT-EQ: Commercial `Declining Balance · 4 yrs · 50%/yr · 5%` di berkas sama persis dengan sel tabel
32. Verifikasi IT-EQ: Modified By di berkas `System` sama dengan sel tabel (aktor System, bukan user)
33. Verifikasi LAND: Fiscal `Tanah` di berkas sama persis dengan sel tabel
34. Sembunyikan kembali kolom Modified By lewat Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`, hilangkan centang Modified By), klik `[Save]`

### TC-FA-FAAC-422: Download mengikuti Search dan Filter yang aktif

35. Ketik Search `equip`, tekan Enter
36. Klik icon Filter untuk membuka Filter Panel
37. Pilih Active = Active, klik `[Apply]`
38. Klik icon Download lalu pilih `Download as CSV`
39. Verifikasi berkas memuat baris HEAVY-EQ, IT-EQ, OFFICE-NEW, dan STORAGE
40. Verifikasi berkas tidak memuat baris contoh lain (OFFICE-OLD, VEHICLES)
41. Klik Clear all
42. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah 1 menjadi unduhan CSV bersama TC-FA-FAAC-427, 428, dan 432; langkah 10 menjadi unduhan XLSX bersama TC-FA-FAAC-429 dan 433. Langkah Uji TC yang sama persis ("Klik icon Download lalu pilih Download as CSV/XLSX") dipenuhi oleh unduhan bersama pada keadaan tabel yang identik (tanpa Search, Filter, dan sort).
- Langkah penghubung (S-03): langkah 18 (mengembalikan sort ke netral setelah langkah 15, S-09), langkah 20, 23, dan 25 (Search kode untuk menjangkau baris contoh, R-16), langkah 27, 41, dan 42 (menutup input Search dan mereset tabel, S-09; langkah 41 melepas Filter), langkah 34 (memulihkan konfigurasi kolom, S-09).
- Kelas harness f (isi berkas): nama berkas, header, dan jumlah baris diasersi di spec 128 (TC-FA-FAAC-418 sampai 421, 423 sampai 425, dan 430); spec ini hanya isi berkas. TC-FA-FAAC-422 (keanggotaan baris berkas) berada di spec ini, bukan di spec 128, karena TC itu tidak memuat klausa UI; Search dan Filter hanya membentuk kondisi cakupan berkas dan bukan objek uji (P-5).
- Langkah 22 mengasersi bagian sel tabel TC-FA-FAAC-656 butir a (tabel tetap `Rina P`) pada saat sel dicatat; langkah 21, 24, dan 26 (mencatat teks sel tabel) adalah langkah observasi TC. Pencatatan dilakukan sebelum unduhan karena unduhan mengikuti Search yang aktif.
- Urutan baris langkah 17 diasersi relatif antar baris contoh (Vehicles sebelum Storage Equipment); seed tambahan (PMP-01, TEMP-EQ, dan baris lain di luar sembilan kelas contoh) dapat menyela dan tidak diasersi (S-11, S-14).
- Alasan melebihi sekitar 35 langkah (42 langkah): seluruh blok satu kelas harness (isi berkas unduhan tabel Asset Class), tiap blok berdiri sendiri, dan pencatatan sel lewat Search kode menambah langkah tanpa mengubah topik.
- Nama literal Pre-setup (sembilan kelas contoh dan PMP-01) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan nilai persis, dan data hanya dibaca (S-06, S-12).
- Temuan untuk QA: TC-FA-FAAC-434 kini menyebut urutan relatif Vehicles sebelum Storage Equipment; spec mengikuti TC. TC-FA-FAAC-422 menulis "berkas hanya memuat baris HEAVY-EQ, IT-EQ, OFFICE-NEW, dan STORAGE" tanpa membatasi pada baris contoh, sedangkan tabel memuat seed lain yang dapat cocok `equip`; spec mengasersi keanggotaan relatif terhadap baris contoh (langkah 39 dan 40).
