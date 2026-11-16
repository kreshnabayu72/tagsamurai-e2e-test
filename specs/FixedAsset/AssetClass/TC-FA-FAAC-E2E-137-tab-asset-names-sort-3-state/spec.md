---
id: TC-FA-FAAC-E2E-137-tab-asset-names-sort-3-state
title: "Tab Asset Names: Sort Tiga Tahap pada Kolom Asset Name, Category, dan Assets"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-457
  - TC-FA-FAAC-458
  - TC-FA-FAAC-459
sourceRules: ["§4.1.3#r1", "§4.4#r14", "§4.1.3#r9", "§4.1.3#r10", "§4.1.3#r11", "§5#b4", "§4.1.3#r2", "§4.1.3#r4"]
smoke: []
dependsOn: []
trace:
  "§4.1.3#r1": [6, 8, 11, 18, 25]
  "§4.4#r14": [6, 8, 10, 15, 17, 20, 22, 24]
  "§4.1.3#r9": [6, 8, 11, 13, 15, 18, 20, 22, 25]
  "§4.1.3#r10": [6, 8, 11, 13, 15, 18, 20, 22, 25]
  "§4.1.3#r11": [6, 8, 11, 13, 15, 18, 20, 22, 25]
  "§5#b4": [11, 13, 15, 18, 25]
  "§4.1.3#r2": [13, 15]
  "§4.1.3#r4": [20, 22]
coverage:
  web: automated
---

# Tab Asset Names: Sort Tiga Tahap pada Kolom Asset Name, Category, dan Assets

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Pre-setup (isi tabel Asset Names hanya dibaca; keadaan awal `Crane Rental Unit` disetel fixture BE, lihat butir Keadaan awal dinamis): Asset Class Active 'Heavy Equipment' (`HEAVY-EQ`) memiliki tiga Asset Name ter-assign: Excavator PC200 (8 aset aktif; Machinery > Heavy Equipment; Label Heavy dan Insured; Assigned At 02/01/26; Assigned By Rina W), Wheel Loader (4 aset aktif; Machinery > Heavy Equipment; Label Heavy; 02/01/26; Rina W), Crane Rental Unit (0 aset aktif; Machinery > Rented; Label Rented; 14/03/26; Budi S). Tanggal Assigned At memakai format dd/mm/yy sesuai General Settings.
- Keadaan awal dinamis: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (3 Asset Name) menurut precondition TC-457; fixture BE menyetelnya pada langkah 1 dan memulihkan keadaan semula sesudah spec (hook `after`), karena TC lain (TC-34, TC-35, TC-270 sampai TC-281) memerlukan `Crane Rental Unit` tanpa Asset Class.
- Kode dan nama seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nama itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Setel keadaan awal lewat fixture BE: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (precondition TC-457)
2. Ketik Search `HEAVY-EQ`, tekan Enter
3. Klik link Class Code `HEAVY-EQ` di tabel
4. Klik tab `Asset Names`

### TC-FA-FAAC-457: Sort kolom Asset Name

5. Klik header `Asset Name` sekali
6. Verifikasi urutan baris klik 1: A-Z (`Crane Rental Unit`, `Excavator PC200`, `Wheel Loader`)
7. Klik header `Asset Name` sekali lagi
8. Verifikasi urutan baris klik 2: Z-A (`Wheel Loader`, `Excavator PC200`, `Crane Rental Unit`)
9. Klik header `Asset Name` sekali lagi
10. Verifikasi indikator sort netral
11. Verifikasi urutan baris kembali ke default Asset Name A-Z (`Crane Rental Unit`, `Excavator PC200`, `Wheel Loader`)

### TC-FA-FAAC-458: Sort kolom Category

12. Klik header `Category` sekali
13. Verifikasi urutan baris klik 1: A-Z menurut leaf (`Excavator PC200` dan `Wheel Loader` dengan `Heavy Equipment` lebih dulu, lalu `Crane Rental Unit` dengan `Rented`; baris bernilai sama mengikuti default Asset Name A-Z)
14. Klik header `Category` sekali lagi
15. Verifikasi urutan baris klik 2: Z-A (`Crane Rental Unit`, lalu `Wheel Loader` dan `Excavator PC200`)
16. Klik header `Category` sekali lagi
17. Verifikasi indikator sort netral
18. Verifikasi urutan baris kembali ke default Asset Name A-Z (`Crane Rental Unit`, `Excavator PC200`, `Wheel Loader`)

### TC-FA-FAAC-459: Sort kolom Assets

19. Klik header `Assets` sekali
20. Verifikasi urutan baris klik 1: numerik naik (`Crane Rental Unit` 0, `Wheel Loader` 4, `Excavator PC200` 8)
21. Klik header `Assets` sekali lagi
22. Verifikasi urutan baris klik 2: numerik turun (`Excavator PC200`, `Wheel Loader`, `Crane Rental Unit`)
23. Klik header `Assets` sekali lagi
24. Verifikasi indikator sort netral
25. Verifikasi urutan baris kembali ke default Asset Name A-Z (`Crane Rental Unit`, `Excavator PC200`, `Wheel Loader`)

## Notes

1. Pengecualian nama seed literal: TC mewajibkan baris seed bernama literal (`HEAVY-EQ` dan Asset Name-nya) dan asersi bergantung pada nama itu; seed dipakai apa adanya tanpa suffix `{runId}`, isi tabel Asset Names hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Detail `HEAVY-EQ` dan tab `Asset Names` dibuka sekali di awal; langkah TC 'Klik tab Asset Names' pada blok berikutnya terpenuhi oleh tab yang sudah aktif (satu pembukaan, bagian 3).
3. Klik ketiga tiap kolom mengembalikan sort ke netral sehingga kolom berikutnya mulai dari default (S-09); tidak ada langkah penghubung tambahan.
4. Ketiga kolom bernilai distinct pada tiga baris seed (S-11): Asset Name, Category (dua nilai leaf), dan Assets (0, 4, 8).
5. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 2 sampai 4, termasuk Search untuk menemukan baris target (R-16).
6. Keadaan awal dinamis (S-14): langkah 1 menyetel `Crane Rental Unit` ter-assign ke `HEAVY-EQ` lewat fixture BE sebagai precondition TC-457; langkah ini bukan bagian TC dan tanpa `Verifikasi`.
