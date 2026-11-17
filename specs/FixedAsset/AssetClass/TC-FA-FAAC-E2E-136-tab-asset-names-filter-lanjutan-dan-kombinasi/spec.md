---
id: TC-FA-FAAC-E2E-136-tab-asset-names-filter-lanjutan-dan-kombinasi
title: "Tab Asset Names: Filter Assigned At, Filter Assigned By, serta Kombinasi Search dan Filter dengan Clear all"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-454
  - TC-FA-FAAC-455
  - TC-FA-FAAC-456
sourceRules: ["§4.1.3#p1", "§4.1.3#r9", "§4.1.3#r10", "§4.1.3#r11", "§4.1.3#r5", "§5#b3", "§4.1.3#r6", "§5#b2", "ST-24", "§4.1.3#r4", "§4.4#r13"]
smoke: []
dependsOn: []
trace:
  "§4.1.3#p1": 5
  "§4.1.3#r9": [5, 8, 13]
  "§4.1.3#r10": [5, 8, 13, 18, 20, 24]
  "§4.1.3#r11": [5, 9, 13]
  "§4.1.3#r5": [8, 9]
  "§5#b3": [8, 9, 13, 18, 20, 24]
  "§4.1.3#r6": 13
  "§5#b2": [18, 20, 24]
  "ST-24": 18
  "§4.1.3#r4": [18, 20]
  "§4.4#r13": [22, 23]
coverage:
  web: automated
---

# Tab Asset Names: Filter Assigned At, Filter Assigned By, serta Kombinasi Search dan Filter dengan Clear all

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Pre-setup (isi tabel Asset Names hanya dibaca; keadaan awal `Crane Rental Unit` disetel fixture BE, lihat butir Keadaan awal dinamis): Asset Class Active 'Heavy Equipment' (`HEAVY-EQ`) memiliki tiga Asset Name ter-assign: Excavator PC200 (8 aset aktif; Machinery > Heavy Equipment; Label Heavy dan Insured; Assigned At 02/01/26; Assigned By Rina W), Wheel Loader (4 aset aktif; Machinery > Heavy Equipment; Label Heavy; 02/01/26; Rina W), Crane Rental Unit (0 aset aktif; Machinery > Rented; Label Rented; 14/03/26; Budi S). Tanggal Assigned At memakai format dd/mm/yy sesuai General Settings.
- Keadaan awal dinamis: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (3 Asset Name) menurut precondition TC-454; fixture BE menyetelnya pada langkah 1 dan memulihkan keadaan semula sesudah spec (hook `after`), karena TC lain (TC-34, TC-35, TC-270 sampai TC-281) memerlukan `Crane Rental Unit` tanpa Asset Class.
- Kode dan nama seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nama itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Setel keadaan awal lewat fixture BE: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (precondition TC-454)
2. Ketik Search `HEAVY-EQ`, tekan Enter
3. Klik link Class Code `HEAVY-EQ` di tabel
4. Klik tab `Asset Names`
5. Verifikasi tabel tab Asset Names memuat tiga baris `Excavator PC200`, `Wheel Loader`, dan `Crane Rental Unit`

### TC-FA-FAAC-454: Filter berdasarkan rentang Assigned At

6. Klik tombol Filter
7. Pada field Assigned At pilih rentang 01/01/26 sampai 31/01/26
8. Verifikasi tabel memuat baris `Excavator PC200` dan `Wheel Loader` (Assigned At 02/01/26)
9. Verifikasi baris `Crane Rental Unit` (14/03/26) tidak tampil
10. Klik `Clear all`

### TC-FA-FAAC-455: Filter berdasarkan Assigned By

11. Klik tombol Filter
12. Pada field Assigned By pilih `Budi S`
13. Verifikasi tabel hanya memuat baris `Crane Rental Unit`, sedangkan `Excavator PC200` dan `Wheel Loader` tidak tampil
14. Klik `Clear all`

### TC-FA-FAAC-456: Kombinasi Search dan Filter berlaku bersamaan (AND) lalu Clear all

15. Ketik Search `loader`, tekan Enter
16. Klik tombol Filter
17. Pada field Assets pilih `No`
18. Verifikasi EmptyState `No results found` (tidak ada baris yang memenuhi Search `loader` dan Assets `No` sekaligus)
19. Ubah field Assets menjadi `Yes`
20. Verifikasi tabel hanya memuat baris `Wheel Loader`, sedangkan `Excavator PC200` dan `Crane Rental Unit` tidak tampil
21. Klik `Clear all` pada chip filter
22. Verifikasi semua filter dilepas (tidak ada chip filter aktif)
23. Verifikasi kotak Search masih berisi `loader`
24. Verifikasi tabel hanya memuat baris `Wheel Loader`
25. Klik `(←)` pada kotak Search

## Notes

1. Pengecualian nama seed literal: TC mewajibkan baris seed bernama literal (`HEAVY-EQ` dan Asset Name-nya) dan asersi bergantung pada nama itu; seed dipakai apa adanya tanpa suffix `{runId}`, isi tabel Asset Names hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Detail `HEAVY-EQ` dan tab `Asset Names` dibuka sekali di awal; langkah TC 'Klik tab Asset Names' pada blok berikutnya terpenuhi oleh tab yang sudah aktif (satu pembukaan, bagian 3).
3. Search `loader` pada TC-456 dipakai sebagai bagian langkah TC (kombinasi dengan Filter), bukan sekadar mencari target.
4. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 2 sampai 4, 10, 14, 15, 25, termasuk Search untuk menemukan baris target (R-16).
5. Keadaan awal dinamis (S-14): langkah 1 menyetel `Crane Rental Unit` ter-assign ke `HEAVY-EQ` lewat fixture BE sebagai precondition TC-454; langkah ini bukan bagian TC dan tanpa `Verifikasi`.
