---
id: TC-FA-FAAC-E2E-120-sort-3-state-kolom-teks-commercial-fiscal
title: "Sort 3-State Tabel Asset Class: Class Code, Class Name, Modified By, Commercial, Fiscal, Asset Names, Assets, dan Capitalization Threshold"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-385
  - TC-FA-FAAC-386
  - TC-FA-FAAC-387
  - TC-FA-FAAC-388
  - TC-FA-FAAC-389
sourceRules: ["§4.4#r14", "§4.1.1#r2", "§4.1.1#r3", "§4.1.1#r4", "§4.1.1#r5", "§4.1.1#r6", "§4.1.1#r8", "§4.1.1#r9", "§4.1.1#r10", "§4.1.1#r17", "§4.1.1#r18", "§4.1.1#r19", "§4.1.1#r20", "§4.1.1#r21", "§4.1.1#r22", "§4.1.1#r23", "§4.1.1#r24", "§4.1.1#r25", "§5#b4", "§9.5#r1"]
smoke: []
dependsOn: []
trace:
  "§4.4#r14": [4, 6, 8]
  "§4.1.1#r2": [4, 6, 8]
  "§4.1.1#r3": [4, 6]
  "§4.1.1#r4": [4, 6]
  "§4.1.1#r5": [4, 6]
  "§4.1.1#r6": [4, 6]
  "§4.1.1#r8": [4, 6]
  "§4.1.1#r9": [4, 6]
  "§4.1.1#r10": [4, 6]
  "§4.1.1#r17": [4, 6, 8]
  "§4.1.1#r18": [4, 6, 8]
  "§4.1.1#r19": [4, 6, 8]
  "§4.1.1#r20": [4, 6, 8]
  "§4.1.1#r21": [4, 6, 8]
  "§4.1.1#r22": [4, 6, 8]
  "§4.1.1#r23": [4, 6, 8]
  "§4.1.1#r24": [4, 6, 8]
  "§4.1.1#r25": [4, 6, 8]
  "§5#b4": 8
  "§9.5#r1": 8
coverage:
  web: automated
---

# Sort 3-State Tabel Asset Class: Class Code, Class Name, Modified By, Commercial, Fiscal, Asset Names, Assets, dan Capitalization Threshold

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Modified By (aktor entri Changelog terbaru): HEAVY-EQ, VEHICLES, MACHINERY, dan OFFICE-NEW = Rina P; OFFICE-OLD = Budi S; IT-EQ, STORAGE, BLDG, dan LAND = System. Seed disediakan tim FE/BE (lihat `suite.md`).
- Tabel "Kolom yang diuji" (parameter langkah 3 sampai 8; urutan relatif awal baris contoh pada Class Code A-Z: BLDG, HEAVY-EQ, IT-EQ, LAND, MACHINERY, OFFICE-NEW, OFFICE-OLD, STORAGE, VEHICLES). Baris bernilai sama mengikuti default sort Class Code A-Z pada klik 1 maupun klik 2:

| Kolom | TC | Klik 1 (naik) | Klik 2 (turun) |
|---|---|---|---|
| Class Code | TC-FA-FAAC-385 | BLDG, HEAVY-EQ, IT-EQ, LAND, MACHINERY, OFFICE-NEW, OFFICE-OLD, STORAGE, VEHICLES | VEHICLES, STORAGE, OFFICE-OLD, OFFICE-NEW, MACHINERY, LAND, IT-EQ, HEAVY-EQ, BLDG |
| Class Name | TC-FA-FAAC-385 | Buildings, Heavy Equipment, IT Equipment, Land, Machinery, Office Equipment (Legacy), Office Equipment (New), Storage Equipment, Vehicles | Vehicles, Storage Equipment, Office Equipment (New), Office Equipment (Legacy), Machinery, Land, IT Equipment, Heavy Equipment, Buildings |
| Modified By | TC-FA-FAAC-385 | kelompok Budi S: OFFICE-OLD; Rina P: HEAVY-EQ, MACHINERY, OFFICE-NEW, VEHICLES; System: BLDG, IT-EQ, LAND, STORAGE | kelompok System: BLDG, IT-EQ, LAND, STORAGE; Rina P: HEAVY-EQ, MACHINERY, OFFICE-NEW, VEHICLES; Budi S: OFFICE-OLD |
| Commercial | TC-FA-FAAC-386 | Method A-Z lalu Useful Life dalam bulan atau Total Estimated Units: IT-EQ (Declining Balance), LAND (Not Depreciated), OFFICE-NEW, OFFICE-OLD (Straight Line 4 yrs), STORAGE, VEHICLES (Straight Line 8 yrs), HEAVY-EQ (Straight Line 10 yrs), BLDG (Straight Line 20 yrs), MACHINERY (Units of Production) | MACHINERY, BLDG, HEAVY-EQ, STORAGE, VEHICLES, OFFICE-NEW, OFFICE-OLD, LAND, IT-EQ |
| Fiscal | TC-FA-FAAC-387 | Tax Depreciation Class A-Z lalu Tax Method A-Z: BLDG, IT-EQ, OFFICE-NEW, OFFICE-OLD, STORAGE, VEHICLES, MACHINERY, HEAVY-EQ, LAND | LAND, HEAVY-EQ, MACHINERY, STORAGE, VEHICLES, OFFICE-NEW, OFFICE-OLD, IT-EQ, BLDG |
| Asset Names | TC-FA-FAAC-388 | numerik naik: BLDG, OFFICE-OLD, STORAGE (0), LAND (1), MACHINERY, OFFICE-NEW (2), VEHICLES (3), IT-EQ (5), HEAVY-EQ (12) | numerik turun: HEAVY-EQ (12), IT-EQ (5), VEHICLES (3), MACHINERY, OFFICE-NEW (2), LAND (1), BLDG, OFFICE-OLD, STORAGE (0) |
| Assets | TC-FA-FAAC-388 | numerik naik: BLDG, OFFICE-NEW, OFFICE-OLD, STORAGE (0), LAND (4), MACHINERY (7), VEHICLES (18), HEAVY-EQ (40), IT-EQ (62) | numerik turun: IT-EQ (62), HEAVY-EQ (40), VEHICLES (18), MACHINERY (7), LAND (4), BLDG, OFFICE-NEW, OFFICE-OLD, STORAGE (0) |
| Capitalization Threshold | TC-FA-FAAC-389 | IT-EQ (2,000,000), HEAVY-EQ (5,000,000), lalu baris Default di akhir: BLDG, LAND, MACHINERY, OFFICE-NEW, OFFICE-OLD, STORAGE, VEHICLES | baris Default di awal (BLDG, LAND, MACHINERY, OFFICE-NEW, OFFICE-OLD, STORAGE, VEHICLES), lalu HEAVY-EQ, IT-EQ |

- State yang diubah spec: konfigurasi kolom tabel (kolom Modified By ditampilkan oleh langkah 1 dan 2 lalu disembunyikan oleh langkah 9 dan 10). Pemulihan cadangan di hook `after` dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE; lihat `suite.md`).
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (sembilan kelas contoh ditambah seed lain seperti `B-*`, `PMP-01`, `B-PAGE01` sampai `B-PAGE11`, `TEMP-EQ`, dan seed spec lain), sehingga sembilan kelas contoh tidak dijamin berada bersama pada halaman 1 dan baris seed lain dapat menyela atau ikut tampil. Asersi spec ini dibatasi pada keanggotaan dan urutan RELATIF antar baris contoh (atau pada baris yang dikenali lewat Search kode); baris seed lain tidak diasersi.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Persiapan (TC-FA-FAAC-385 langkah 1)

1. Aktifkan kolom Modified By lewat Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`, centang Modified By)
2. Klik `[Save]`

### Sort 3-state per kolom (TC-FA-FAAC-385 sampai 389)

Untuk setiap baris tabel "Kolom yang diuji" pada Prerequisites, dari Class Code sampai Capitalization Threshold (langkah 3 sampai 8):

3. Klik header kolom satu kali, lalu telusuri seluruh halaman tabel dari halaman 1 sampai halaman terakhir (Next)
4. Verifikasi urutan relatif baris contoh naik sesuai kolom "Klik 1 (naik)" pada baris tabel kolom itu
5. Klik header kolom kedua kali, lalu telusuri seluruh halaman tabel dari halaman 1 sampai halaman terakhir (Next)
6. Verifikasi urutan relatif baris contoh turun sesuai kolom "Klik 2 (turun)" pada baris tabel kolom itu
7. Klik header kolom ketiga kali, lalu telusuri seluruh halaman tabel dari halaman 1 sampai halaman terakhir (Next)
8. Verifikasi sort netral kembali ke Class Code A-Z dengan urutan relatif baris contoh: BLDG, HEAVY-EQ, IT-EQ, LAND, MACHINERY, OFFICE-NEW, OFFICE-OLD, STORAGE, VEHICLES

### Pemulihan

9. Sembunyikan kembali kolom Modified By lewat Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`, hilangkan centang Modified By)
10. Klik `[Save]`

## Notes

- Langkah 3 sampai 8 diulang untuk delapan baris tabel Prerequisites (bagian 8b butir 7), `Verifikasi` tetap satu per klausa: naik, turun, netral per kolom. Pembagian TC lintas baris tabel: TC-FA-FAAC-385 (Class Code, Class Name, Modified By), TC-FA-FAAC-386 (Commercial), TC-FA-FAAC-387 (Fiscal), TC-FA-FAAC-388 (Asset Names, Assets), TC-FA-FAAC-389 (Capitalization Threshold).
- Alasan melewati sekitar 35 langkah (dihitung dengan ekspansi: 2 + 8 kolom x 6 + 2 = 52): seluruh blok berstruktur identik, satu kelas harness (sort 3-state), satu dataset Pre-setup yang hanya dibaca, dan berdiri sendiri; kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Klausa "baris bernilai sama mengikuti Class Code A-Z" (TC-FA-FAAC-385 butir d, 386 butir d, 387, 388 butir c) tercermin pada urutan di tabel Prerequisites dan diasersi dalam `Verifikasi` langkah 4 dan 6.
- Urutan "turun" untuk Asset Names dan Assets diturunkan dari TC (klik 2 turun; baris bernilai sama mengikuti Class Code A-Z); TC-FA-FAAC-388 tidak menuliskan daftar turun satu per satu.
- Urutan "turun" Commercial pada TC (STORAGE, VEHICLES, OFFICE-NEW, OFFICE-OLD) bukan kebalikan persis dari "naik" karena baris bernilai sama mengikuti Class Code A-Z.
- Penelusuran seluruh halaman (S-14) menjadi bagian langkah 3, 5, dan 7: tabel memuat lebih dari 25 baris sehingga baris contoh tersebar di beberapa halaman dan seed lain dapat menyela; asersi `Verifikasi` hanya pada urutan relatif baris contoh.
- Langkah penghubung (S-03): langkah 9 dan 10 (memulihkan konfigurasi kolom, S-09). Sort kembali netral pada langkah 7 tiap iterasi (S-09).
- Nama literal Pre-setup (sembilan kelas contoh) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan urutan relatif antar baris contoh, dan data hanya dibaca (S-06, S-12).
- Temuan untuk QA: TC-FA-FAAC-385 butir d, 386 butir d, 387, dan 388 butir c menyatakan aturan tie pada Expected tanpa mengurutkannya baris per baris untuk klik 2; urutan klik 2 diambil dari daftar TC bila ada, selain itu diturunkan dari aturan tie.
