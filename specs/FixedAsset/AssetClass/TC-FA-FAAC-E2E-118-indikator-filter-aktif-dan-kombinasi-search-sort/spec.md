---
id: TC-FA-FAAC-E2E-118-indikator-filter-aktif-dan-kombinasi-search-sort
title: "Filter Tabel Asset Class: Indikator Filter Aktif, Pelepasan Filter, dan Kombinasi dengan Search dan Sort"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-374
  - TC-FA-FAAC-375
  - TC-FA-FAAC-376
  - TC-FA-FAAC-377
  - TC-FA-FAAC-378
sourceRules: ["§4.1.1#b4", "§4.4#r13", "§4.1.1#r19", "§4.1.1#r25", "§5#b2", "§5#b3", "§4.1.1#r17", "§4.1.1#r22", "§4.1.1#r23", "§4.4#r14", "§4.1.1#r3"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#b4": [3, 4, 6, 29]
  "§4.4#r13": [3, 6, 7, 20]
  "§4.1.1#r19": [7, 11, 22, 28]
  "§4.1.1#r25": [7, 11, 16, 22, 28]
  "§5#b2": 11
  "§5#b3": [11, 12, 16, 21, 28]
  "§4.1.1#r17": [11, 16, 22, 28]
  "§4.1.1#r22": [11, 22, 28]
  "§4.1.1#r23": [11, 22, 28]
  "§4.4#r14": [17, 22]
  "§4.1.1#r3": 22
anchor: [15]
coverage:
  web: automated
---

# Filter Tabel Asset Class: Indikator Filter Aktif, Pelepasan Filter, dan Kombinasi dengan Search dan Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ (Heavy Equipment), VEHICLES, IT-EQ (IT Equipment), MACHINERY, BLDG, STORAGE (Storage Equipment), OFFICE-NEW (Office Equipment (New)), LAND (Active) dan OFFICE-OLD (Office Equipment (Legacy), Inactive). Search `equip` mencocokkan HEAVY-EQ, IT-EQ, OFFICE-NEW, OFFICE-OLD, dan STORAGE; Commercial Method Straight Line dimiliki HEAVY-EQ, OFFICE-NEW, dan seterusnya (bukan IT-EQ). Seed disediakan tim FE/BE (lihat `suite.md`).
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (sembilan kelas contoh ditambah seed lain seperti `B-*`, `PMP-01`, `B-PAGE01` sampai `B-PAGE11`, `TEMP-EQ`, dan seed spec lain), sehingga sembilan kelas contoh tidak dijamin berada bersama pada halaman 1 dan baris seed lain dapat menyela atau ikut tampil. Asersi spec ini dibatasi pada keanggotaan dan urutan RELATIF antar baris contoh (atau pada baris yang dikenali lewat Search kode); baris seed lain tidak diasersi.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-FAAC-374: Badge titik pada icon Filter tampil saat filter ter-Apply dan hilang saat filter dilepas

1. Klik icon Filter untuk membuka Filter Panel
2. Pilih Active = Active dan Commercial Method = Straight Line, klik `[Apply]`
3. Verifikasi badge titik (Standalone Dot, tanpa angka) tampil pada icon Filter saat Filter Panel terbuka
4. Klik ulang icon Filter untuk menutup Filter Panel, lalu verifikasi badge titik tetap tampil pada icon Filter
5. Buka Filter Panel (klik icon Filter, karena panel ditutup pada langkah 4), klik `[Clear Field]`, lalu klik `[Apply]`, lalu telusuri seluruh halaman tabel dari halaman 1 sampai halaman terakhir (Next)
6. Verifikasi semua filter dilepas dan badge titik pada icon Filter hilang
7. Verifikasi tabel kembali menampilkan semua baris: IT-EQ (Declining Balance) dan OFFICE-OLD (Inactive), yang tersaring pada langkah 2, tampil kembali

### TC-FA-FAAC-375: Search lalu Filter menghasilkan irisan

8. Ketik Search `equip`, tekan Enter
9. Lanjutkan pada Filter Panel yang masih terbuka sesudah `[Apply]` langkah 5 (tanpa klik icon Filter, karena klik itu menutup panel)
10. Pilih Active = Active, klik `[Apply]`
11. Verifikasi baris HEAVY-EQ, IT-EQ, OFFICE-NEW, dan STORAGE tampil dan baris contoh lain tidak tampil (OFFICE-OLD tersaring oleh Active); baris seed lain yang cocok `equip` tidak diasersi
12. Verifikasi keyword `equip` tetap terisi pada kotak Search setelah Filter diterapkan

### TC-FA-FAAC-378: Kosongkan Search saat Filter dan Sort aktif

13. Klik header Class Name dua kali (Z-A)
14. Klik icon `←` pada kotak Search, lalu telusuri seluruh halaman tabel dari halaman 1 sampai halaman terakhir (Next)
15. Verifikasi Search dikosongkan
16. Verifikasi filter Active tetap aktif: baris contoh Active (mis. HEAVY-EQ) tampil dan baris OFFICE-OLD tidak tampil
17. Verifikasi sort Class Name Z-A tetap aktif

### TC-FA-FAAC-377: Lepas Filter saat Search dan Sort aktif

18. Ketik Search `equip`, tekan Enter
19. Klik `[Clear Field]` pada Filter Panel yang masih terbuka sejak langkah 10, lalu klik `[Apply]`
20. Verifikasi filter dilepas
21. Verifikasi Search `equip` tetap aktif
22. Verifikasi sort Class Name Z-A tetap aktif: urutan relatif antar baris contoh STORAGE, OFFICE-NEW, OFFICE-OLD, IT-EQ, HEAVY-EQ (baris seed lain yang cocok `equip` dapat menyela)

### TC-FA-FAAC-376: Filter lalu Search menghasilkan irisan

23. Klik icon `←` pada kotak Search
24. Klik header Class Name sekali lagi (sort kembali netral, Class Code A-Z)
25. Lanjutkan pada Filter Panel yang masih terbuka sesudah `[Apply]` langkah 19 (tanpa klik icon Filter, karena klik itu menutup panel)
26. Pilih Active = Active, klik `[Apply]`
27. Ketik Search `equip`, tekan Enter
28. Verifikasi baris HEAVY-EQ, IT-EQ, OFFICE-NEW, dan STORAGE tampil dan baris contoh lain tidak tampil; baris seed lain yang cocok `equip` tidak diasersi
29. Verifikasi badge titik pada icon Filter tetap tampil setelah Search karena filter Active tetap ter-Apply
30. Klik `[Clear Field]` pada Filter Panel yang masih terbuka sejak langkah 26, lalu klik `[Apply]`
31. Klik icon `←` pada kotak Search

## Notes

- Urutan TC di dalam spec: TC-FA-FAAC-378, 377, lalu 376 diletakkan sesudah TC-FA-FAAC-375 supaya state Search, Filter, dan Sort yang dibangun TC sebelumnya dipakai ulang tanpa membangunnya dari awal (S-10); setiap TC tetap memuat semua aksi yang diminta TC-nya dan precondition TC tidak bergantung pada hasil TC lain.
- Penelusuran seluruh halaman (S-14) menjadi bagian langkah 5 dan 14: tabel tanpa Search memuat lebih dari 25 baris sehingga baris IT-EQ, OFFICE-OLD, dan HEAVY-EQ tidak dijamin berada di halaman 1.
- Langkah penghubung (S-03): langkah 23 dan 24 (mengosongkan Search dan mereset sort sebelum TC-FA-FAAC-376, S-09), langkah 30 dan 31 (melepas filter dan menutup Search di akhir spec, S-09). Klik `←` pada langkah 14 dan 23 mengikuti 8b butir 9 untuk mengosongkan Search.
- Panel (prd-conventions §9.8): Filter Panel tetap terbuka sesudah `[Apply]`, sehingga langkah 9 dan 25 melanjutkan pada panel yang masih terbuka tanpa klik icon Filter (klik itu menutup panel); panel hanya ditutup eksplisit pada langkah 4, sehingga langkah 5 membukanya lagi.
- Langkah 13 dan 14 memakai state langkah 8 sampai 10 (Search `equip` dan filter Active): langkah TC-FA-FAAC-378 membangun Filter lalu Sort lalu Search; urutan pembentukan diubah menjadi Search, Filter, Sort karena hasil akhir state sama.
- Klausa "baris contoh lain tidak tampil" diasersi pada satu `Verifikasi` bersama baris target yang tampil sebagai pembanding (8b butir 2); baris seed lain tidak diasersi.
- Nama literal Pre-setup (sembilan kelas contoh) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan urutan relatif antar baris contoh, dan data hanya dibaca (S-06, S-12).
- Temuan untuk QA: tidak ada.
