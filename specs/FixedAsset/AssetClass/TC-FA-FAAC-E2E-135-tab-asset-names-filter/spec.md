---
id: TC-FA-FAAC-E2E-135-tab-asset-names-filter
title: "Tab Asset Names: Struktur Filter Panel serta Filter Category, Label, Assets Yes, dan Assets No"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-449
  - TC-FA-FAAC-450
  - TC-FA-FAAC-451
  - TC-FA-FAAC-452
  - TC-FA-FAAC-453
coverage:
  web: automated
---

# Tab Asset Names: Struktur Filter Panel serta Filter Category, Label, Assets Yes, dan Assets No

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Pre-setup (isi tabel Asset Names hanya dibaca; keadaan awal `Crane Rental Unit` disetel fixture BE, lihat butir Keadaan awal dinamis): Asset Class Active 'Heavy Equipment' (`HEAVY-EQ`) memiliki tiga Asset Name ter-assign: Excavator PC200 (8 aset aktif; Machinery > Heavy Equipment; Label Heavy dan Insured; Assigned At 02/01/26; Assigned By Rina W), Wheel Loader (4 aset aktif; Machinery > Heavy Equipment; Label Heavy; 02/01/26; Rina W), Crane Rental Unit (0 aset aktif; Machinery > Rented; Label Rented; 14/03/26; Budi S). Tanggal Assigned At memakai format dd/mm/yy sesuai General Settings.
- Keadaan awal dinamis: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (3 Asset Name) menurut precondition TC-449; fixture BE menyetelnya pada langkah 1 dan memulihkan keadaan semula sesudah spec (hook `after`), karena TC lain (TC-34, TC-35, TC-270 sampai TC-281) memerlukan `Crane Rental Unit` tanpa Asset Class.
- Kode dan nama seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nama itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Setel keadaan awal lewat fixture BE: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (precondition TC-449)
2. Ketik Search `HEAVY-EQ`, tekan Enter
3. Klik link Class Code `HEAVY-EQ` di tabel
4. Klik tab `Asset Names`
5. Verifikasi tabel tab Asset Names memuat tiga baris `Excavator PC200`, `Wheel Loader`, dan `Crane Rental Unit`

### TC-FA-FAAC-449: Screening Filter Panel memuat lima field termasuk Label

6. Klik tombol Filter
7. Verifikasi Filter Panel memuat lima field berurutan Category, Label, Assets, Assigned At, dan Assigned By
8. Verifikasi field Category berupa tree select multi dengan placeholder `All categories`
9. Verifikasi field Label berupa multi-select dengan pencarian dan placeholder `All labels`
10. Verifikasi field Assets berupa multi-select `Yes` / `No` dengan placeholder `All assets`
11. Verifikasi field Assigned At berupa rentang tanggal dengan placeholder `Select date`
12. Verifikasi field Assigned By berupa multi-select searchable dengan placeholder `All users`
13. Verifikasi tidak ada field filter untuk Asset Name

### TC-FA-FAAC-450: Filter berdasarkan Category

14. Pada field Category pilih `Rented`
15. Verifikasi tabel hanya memuat baris `Crane Rental Unit`, sedangkan `Excavator PC200` dan `Wheel Loader` tidak tampil
16. Verifikasi chip filter aktif tampil di atas tabel
17. Verifikasi tautan `Clear all` tampil bersama chip filter
18. Klik `Clear all`

### TC-FA-FAAC-451: Filter berdasarkan Label

19. Klik tombol Filter
20. Pada field Label pilih `Insured`
21. Verifikasi tabel hanya memuat baris `Excavator PC200`, sedangkan `Wheel Loader` dan `Crane Rental Unit` tidak tampil
22. Klik `Clear all`

### TC-FA-FAAC-452: Filter Assets = Yes menyaring Asset Name dengan aset aktif

23. Klik tombol Filter
24. Pada field Assets pilih `Yes`
25. Verifikasi tabel memuat baris `Excavator PC200` dan `Wheel Loader` (Assets lebih dari 0)
26. Verifikasi baris `Crane Rental Unit` tidak tampil
27. Klik `Clear all`

### TC-FA-FAAC-453: Filter Assets = No menyaring Asset Name tanpa aset aktif

28. Klik tombol Filter
29. Pada field Assets pilih `No`
30. Verifikasi tabel hanya memuat baris `Crane Rental Unit` (Assets 0), sedangkan `Excavator PC200` dan `Wheel Loader` tidak tampil
31. Klik `Clear all`

## Notes

1. Pengecualian nama seed literal: TC mewajibkan baris seed bernama literal (`HEAVY-EQ` dan Asset Name-nya) dan asersi bergantung pada nama itu; seed dipakai apa adanya tanpa suffix `{runId}`, isi tabel Asset Names hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Detail `HEAVY-EQ` dan tab `Asset Names` dibuka sekali di awal; langkah TC 'Klik tab Asset Names' pada blok berikutnya terpenuhi oleh tab yang sudah aktif (satu pembukaan, bagian 3).
3. Urutan `Verifikasi` placeholder TC-449 mengikuti kolom Expected butir a; hasil filter yang disebut 'hanya' diasersi bersama baris lain yang dijamin ada (bagian 8b butir 2), dengan `Verifikasi` tiga baris awal sebagai pembanding generik.
4. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 2 sampai 4, 18, 22, 27, 31, termasuk Search untuk menemukan baris target (R-16).
5. Keadaan awal dinamis (S-14): langkah 1 menyetel `Crane Rental Unit` ter-assign ke `HEAVY-EQ` lewat fixture BE sebagai precondition TC-449; langkah ini bukan bagian TC dan tanpa `Verifikasi`.
