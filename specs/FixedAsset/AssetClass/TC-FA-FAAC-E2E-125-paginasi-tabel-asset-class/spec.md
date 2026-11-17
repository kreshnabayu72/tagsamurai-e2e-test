---
id: TC-FA-FAAC-E2E-125-paginasi-tabel-asset-class
title: "Paginasi Tabel Asset Class: Ukuran Halaman, Navigasi Halaman, Interaksi dengan Search, Filter, dan Sort, serta Input Nomor Halaman Tidak Valid"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-383
  - TC-FA-FAAC-408
  - TC-FA-FAAC-409
  - TC-FA-FAAC-410
  - TC-FA-FAAC-411
  - TC-FA-FAAC-412
  - TC-FA-FAAC-702
sourceRules: ["§9.5#r5", "§4.1.1#r3", "§9.5#r1"]
smoke: []
dependsOn: []
trace:
  "§9.5#r5": [1, 3, 4, 7, 9, 18]
  "§4.1.1#r3": [23, 36]
  "§9.5#r1": 31
anchor: [13, 17, 22, 26, 30, 33, 35]
coverage:
  web: automated
---

# Paginasi Tabel Asset Class: Ukuran Halaman, Navigasi Halaman, Interaksi dengan Search, Filter, dan Sort, serta Input Nomor Halaman Tidak Valid

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ (Heavy Equipment), VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive).
- Data Pre-setup tambahan (hanya dibaca): jumlah Asset Class total lebih dari 25 (seed tambahan di luar sembilan kelas contoh, jumlah N diturunkan dari seeding dan tidak dibaca dari satu halaman tabel; 8b butir 10) sehingga halaman 2 ada pada ukuran halaman 10 dan 25 (TC-FA-FAAC-408, 409), termasuk sebelas Asset Class B-PAGE01 sampai B-PAGE11 (Class Name `Page Fixture 01` sampai `Page Fixture 10` untuk B-PAGE01 sampai B-PAGE10 dan `Page Fixture 00` untuk B-PAGE11) untuk TC-FA-FAAC-702. Seed disediakan tim FE/BE (lihat `suite.md`).
- Tabel "Nilai input nomor halaman tidak valid" (parameter langkah 32 dan 33): `0`, `-1`, `9999`, `abc`.
- Kondisi awal tabel: ukuran halaman 10, tanpa Search, Filter, dan sort selain default Class Code A-Z.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah data atau state global.

## Test Steps

### TC-FA-FAAC-408: Paginasi bawaan tabel Asset Class

1. Verifikasi halaman pertama menampilkan 10 baris
2. Buka pilihan ukuran halaman
3. Verifikasi pilihan ukuran halaman: 10, 25, 50, 100
4. Verifikasi nilai terpilih 10
5. Tutup pilihan ukuran halaman tanpa mengubah nilai

### TC-FA-FAAC-410: Navigasi halaman Next dan Previous tabel Asset Class

6. Klik halaman berikutnya
7. Verifikasi halaman 2 menampilkan baris lanjutan sesuai sort aktif
8. Klik halaman sebelumnya
9. Verifikasi halaman 1 menampilkan 10 baris pertama

### TC-FA-FAAC-383: Apply Filter mengembalikan tabel ke halaman 1

10. Klik halaman 2
11. Klik icon Filter untuk membuka Filter Panel
12. Pilih Active = Active, klik `[Apply]`
13. Verifikasi tabel kembali ke halaman 1 dengan hasil filter
14. Klik Clear all

### TC-FA-FAAC-409: Ganti ukuran halaman kembali ke halaman 1

15. Klik halaman 2
16. Ganti ukuran halaman ke 25
17. Verifikasi tabel kembali ke halaman 1 setelah ganti ukuran halaman
18. Verifikasi halaman 1 menampilkan 25 baris
19. Ganti ukuran halaman kembali ke 10

### TC-FA-FAAC-412: Ganti sort tidak memindahkan halaman

20. Klik halaman 2
21. Klik header kolom Class Name
22. Verifikasi tabel tetap berada di halaman 2
23. Verifikasi baris disusun ulang sesuai sort Class Name A-Z

### TC-FA-FAAC-411: Search mengembalikan tabel ke halaman 1

24. Klik halaman 2
25. Ketik Search `equip`, tekan Enter
26. Verifikasi tabel kembali ke halaman 1 dengan hasil Search `equip`

### TC-FA-FAAC-702: Input nomor halaman tidak valid diabaikan dan pergantian sort tetap di nomor halaman sekarang

27. Klik header kolom Class Name dua kali lagi (sort kembali netral, Class Code A-Z)
28. Ganti isi kotak search dengan `B-PAGE`, tekan Enter
29. Klik halaman 2
30. Verifikasi hasil Search `B-PAGE` berisi 11 baris
31. Verifikasi halaman 2 hanya memuat B-PAGE11 (sort default Class Code A-Z)

Untuk setiap nilai pada tabel "Nilai input nomor halaman tidak valid" di Prerequisites (langkah 32 dan 33):

32. Ketik nilai itu pada input nomor halaman, tekan Enter
33. Verifikasi input diabaikan dan tabel tetap di halaman 2 yang memuat B-PAGE11

34. Klik header kolom Class Name satu kali
35. Verifikasi tabel tetap di halaman 2 (nomor halaman tidak berubah)
36. Verifikasi urutan dataset berubah sehingga halaman 2 memuat B-PAGE10 (bukan B-PAGE11)
37. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Jumlah langkah tertulis 37 dan dengan ekspansi langkah 32 dan 33 (empat nilai) menjadi 43, di atas smell 35 langkah. Alasan: seluruh TC satu topik (paginasi tabel Asset Class) pada satu dataset yang hanya dibaca, saling berurutan tanpa mengubah data, langkah ulang berparameter di tabel Prerequisites (8b butir 7), dan `Verifikasi` tetap satu per klausa; langkah penghubung berjumlah enam dari 37.
- Langkah penghubung (S-03): langkah 5 (menutup pilihan ukuran halaman), langkah 14 (melepas filter, S-09), langkah 19 (mengembalikan ukuran halaman 10), langkah 27 (mengembalikan sort ke netral setelah langkah 21, S-09), langkah 28 (mengganti isi kotak Search; kotak masih berisi `equip` dari langkah 25), langkah 37 (menutup input Search dan mereset tabel, S-09; R-16).
- Urutan TC di dalam spec mengikuti state: TC-FA-FAAC-408, 410, 383, 409, 412, 411, lalu 702 (S-10); tiap TC memuat semua aksi TC-nya.
- Klausa "hanya memuat B-PAGE11" (langkah 31) dan "tidak berubah" memakai pembanding yang tampil: hasil Search berisi 11 baris (langkah 30) dan tabel tampil di halaman 2.
- Nama literal Pre-setup (sembilan kelas contoh dan B-PAGE01 sampai B-PAGE11) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis, dan data hanya dibaca (S-06, S-12).
- Temuan untuk QA: TC-FA-FAAC-408 dan 409 menyebut "lebih dari 25" tanpa jumlah pasti; jumlah ditetapkan seeding.
