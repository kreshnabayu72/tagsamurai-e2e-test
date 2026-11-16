---
id: TC-FA-FAAC-E2E-134-tab-asset-names-search
title: "Tab Asset Names: Search pada Kolom Asset Name, Category, Label, Assets, Assigned By, Assigned At, Debounce, dan Kolom Tersembunyi"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-441
  - TC-FA-FAAC-442
  - TC-FA-FAAC-443
  - TC-FA-FAAC-444
  - TC-FA-FAAC-445
  - TC-FA-FAAC-446
  - TC-FA-FAAC-447
  - TC-FA-FAAC-448
sourceRules: ["§4.1.3#p1", "§4.1.3#r9", "§4.1.3#r10", "§4.1.3#r11", "§5#b2", "§4.1.3#r2", "§4.1.3#r3", "§4.1.3#r4", "§4.1.3#r6", "ST-24"]
smoke: []
dependsOn: []
trace:
  "§4.1.3#p1": 5
  "§4.1.3#r9": [5, 7, 10, 13, 16, 19, 26, 28]
  "§4.1.3#r10": [5, 7, 10, 13, 16, 19, 26, 28, 30]
  "§4.1.3#r11": [5, 7, 10, 13, 16, 19, 26, 28]
  "§5#b2": [7, 10, 13, 16, 19, 22, 26, 28, 30, 34]
  "§4.1.3#r2": [10, 34]
  "§4.1.3#r3": 13
  "§4.1.3#r4": 16
  "§4.1.3#r6": 19
  "ST-24": [22, 34]
coverage:
  web: automated
---

# Tab Asset Names: Search pada Kolom Asset Name, Category, Label, Assets, Assigned By, Assigned At, Debounce, dan Kolom Tersembunyi

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Pre-setup (isi tabel Asset Names hanya dibaca; keadaan awal `Crane Rental Unit` disetel fixture BE, lihat butir Keadaan awal dinamis): Asset Class Active 'Heavy Equipment' (`HEAVY-EQ`) memiliki tiga Asset Name ter-assign: Excavator PC200 (8 aset aktif; Machinery > Heavy Equipment; Label Heavy dan Insured; Assigned At 02/01/26; Assigned By Rina W), Wheel Loader (4 aset aktif; Machinery > Heavy Equipment; Label Heavy; 02/01/26; Rina W), Crane Rental Unit (0 aset aktif; Machinery > Rented; Label Rented; 14/03/26; Budi S). Tanggal Assigned At memakai format dd/mm/yy sesuai General Settings.
- Keadaan awal dinamis: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (3 Asset Name) menurut precondition TC-441; fixture BE menyetelnya pada langkah 1 dan memulihkan keadaan semula sesudah spec (hook `after`), karena TC lain (TC-34, TC-35, TC-270 sampai TC-281) memerlukan `Crane Rental Unit` tanpa Asset Class.
- Jeda 2 detik pada blok TC-447 adalah pilihan spec (di bawah 30 detik, bagian 6) untuk membuktikan tidak ada pemfilteran otomatis tanpa Enter.
- Konfigurasi kolom: blok TC-448 menyembunyikan kolom `Category` lalu memulihkannya di spec; hook `after` juga menghapus preferensi kolom di browser (kemampuan disediakan tim FE).
- Kode dan nama seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nama itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Setel keadaan awal lewat fixture BE: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (precondition TC-441)
2. Ketik Search `HEAVY-EQ`, tekan Enter
3. Klik link Class Code `HEAVY-EQ` di tabel
4. Klik tab `Asset Names`
5. Verifikasi tabel tab Asset Names memuat tiga baris `Excavator PC200`, `Wheel Loader`, dan `Crane Rental Unit`

### TC-FA-FAAC-441: Search pada kolom Asset Name

6. Ketik Search `excav`, tekan Enter
7. Verifikasi tabel hanya memuat baris `Excavator PC200`, sedangkan `Wheel Loader` dan `Crane Rental Unit` tidak tampil (pencocokan substring tanpa membedakan huruf besar-kecil)
8. Klik `(←)` pada kotak Search

### TC-FA-FAAC-442: Search pada kolom Category

9. Ketik Search `Rented`, tekan Enter
10. Verifikasi tabel hanya memuat baris `Crane Rental Unit` (cocok dengan Category `Rented`), sedangkan `Excavator PC200` dan `Wheel Loader` tidak tampil
11. Klik `(←)` pada kotak Search

### TC-FA-FAAC-443: Search pada kolom Label

12. Ketik Search `Insured`, tekan Enter
13. Verifikasi tabel hanya memuat baris `Excavator PC200` (Label Heavy, Insured), sedangkan `Wheel Loader` dan `Crane Rental Unit` tidak tampil
14. Klik `(←)` pada kotak Search

### TC-FA-FAAC-444: Search pada kolom Assets

15. Ketik Search `8`, tekan Enter
16. Verifikasi tabel hanya memuat baris `Excavator PC200` (Assets 8), sedangkan `Wheel Loader` dan `Crane Rental Unit` tidak tampil
17. Klik `(←)` pada kotak Search

### TC-FA-FAAC-445: Search pada kolom Assigned By

18. Ketik Search `Budi`, tekan Enter
19. Verifikasi tabel hanya memuat baris `Crane Rental Unit` (Assigned By Budi S), sedangkan `Excavator PC200` dan `Wheel Loader` tidak tampil
20. Klik `(←)` pada kotak Search

### TC-FA-FAAC-446: Search tidak mencocokkan kolom Assigned At

21. Ketik Search `14/03/26`, tekan Enter
22. Verifikasi EmptyState `No results found` dengan deskripsi `Try adjusting your search or filter.` (kolom tanggal tidak ikut dicari)
23. Klik `(←)` pada kotak Search

### TC-FA-FAAC-447: Search hanya diproses setelah Enter tanpa debounce

24. Buka kotak Search lalu ketik `wheel` tanpa menekan Enter
25. Tunggu 2 detik
26. Verifikasi ketiga baris `Excavator PC200`, `Wheel Loader`, dan `Crane Rental Unit` tetap tampil (tidak ada pemfilteran otomatis)
27. Tekan Enter
28. Verifikasi tabel hanya memuat baris `Wheel Loader`, sedangkan `Excavator PC200` dan `Crane Rental Unit` tidak tampil
29. Ganti isi kotak search dengan ` WHEEL ` (dengan spasi di awal dan akhir, huruf besar), tekan Enter
30. Verifikasi tabel hanya memuat baris `Wheel Loader` (spasi dipangkas, tidak membedakan huruf besar-kecil)
31. Klik `(←)` pada kotak Search

### TC-FA-FAAC-448: Search tidak mencocokkan kolom yang disembunyikan

32. Klik ikon `⋯` pada header kolom Actions, lalu hilangkan centang `Category`
33. Ketik Search `Heavy Equipment`, tekan Enter
34. Verifikasi EmptyState `No results found` dengan deskripsi `Try adjusting your search or filter.` karena kolom Category sedang di-hide
35. Klik `(←)` pada kotak Search
36. Klik ikon `⋯` pada header kolom Actions, lalu centang kembali `Category`

## Notes

1. Pengecualian nama seed literal: TC mewajibkan baris seed bernama literal (`HEAVY-EQ` dan Asset Name-nya) dan asersi bergantung pada nama itu; seed dipakai apa adanya tanpa suffix `{runId}` dan hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Detail `HEAVY-EQ` dan tab `Asset Names` dibuka sekali di awal; langkah TC 'Klik tab Asset Names' pada blok berikutnya terpenuhi oleh tab yang sudah aktif (satu pembukaan, bagian 3).
3. Anchor absence: `Verifikasi` tiga baris tampil pada langkah 5 menjadi pembanding generik untuk seluruh asersi 'hanya memuat' dan 'tidak tampil' (bagian 8b butir 2); EmptyState `No results found` pada TC-446 dan TC-448 adalah anchor positif hasil Search.
4. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 (fixture BE menyetel keadaan awal dinamis), 2 sampai 4, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21, 23, 25, 29, 31, 35, 36, termasuk Search untuk menemukan baris target (R-16).
5. Keadaan awal dinamis (S-14): langkah 1 menyetel `Crane Rental Unit` ter-assign ke `HEAVY-EQ` lewat fixture BE sebagai precondition TC-441; langkah ini bukan bagian TC dan tanpa `Verifikasi`.
6. Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah (36) karena delapan TC Search satu topik (tab Asset Names HEAVY-EQ) yang berbagi satu pembukaan Detail dan tiap blok hanya memuat Search, `Verifikasi`, dan reset kotak Search, ditambah satu langkah fixture BE untuk keadaan awal dinamis; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
