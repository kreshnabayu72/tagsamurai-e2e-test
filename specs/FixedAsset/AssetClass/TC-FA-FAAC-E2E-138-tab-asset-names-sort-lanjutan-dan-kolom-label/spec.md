---
id: TC-FA-FAAC-E2E-138-tab-asset-names-sort-lanjutan-dan-kolom-label
title: "Tab Asset Names: Sort Tiga Tahap pada Kolom Assigned At dan Assigned By serta Kolom Label Tidak Dapat Diurutkan"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-460
  - TC-FA-FAAC-461
  - TC-FA-FAAC-462
coverage:
  web: automated
---

# Tab Asset Names: Sort Tiga Tahap pada Kolom Assigned At dan Assigned By serta Kolom Label Tidak Dapat Diurutkan

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Pre-setup (isi tabel Asset Names hanya dibaca; keadaan awal `Crane Rental Unit` disetel fixture BE, lihat butir Keadaan awal dinamis): Asset Class Active 'Heavy Equipment' (`HEAVY-EQ`) memiliki tiga Asset Name ter-assign: Excavator PC200 (8 aset aktif; Machinery > Heavy Equipment; Label Heavy dan Insured; Assigned At 02/01/26; Assigned By Rina W), Wheel Loader (4 aset aktif; Machinery > Heavy Equipment; Label Heavy; 02/01/26; Rina W), Crane Rental Unit (0 aset aktif; Machinery > Rented; Label Rented; 14/03/26; Budi S). Tanggal Assigned At memakai format dd/mm/yy sesuai General Settings.
- Keadaan awal dinamis: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (3 Asset Name) menurut precondition TC-460; fixture BE menyetelnya pada langkah 1 dan memulihkan keadaan semula sesudah spec (hook `after`), karena TC lain (TC-34, TC-35, TC-270 sampai TC-281) memerlukan `Crane Rental Unit` tanpa Asset Class.
- Kode dan nama seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nama itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Setel keadaan awal lewat fixture BE: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (precondition TC-460)
2. Ketik Search `HEAVY-EQ`, tekan Enter
3. Klik link Class Code `HEAVY-EQ` di tabel
4. Klik tab `Asset Names`

### TC-FA-FAAC-460: Sort kolom Assigned At

5. Klik header `Assigned At` sekali
6. Verifikasi urutan baris klik 1: Oldest First (`Excavator PC200` dan `Wheel Loader` 02/01/26 lebih dulu, lalu `Crane Rental Unit` 14/03/26)
7. Klik header `Assigned At` sekali lagi
8. Verifikasi urutan baris klik 2: Newest First (`Crane Rental Unit` lebih dulu)
9. Klik header `Assigned At` sekali lagi
10. Verifikasi indikator sort netral
11. Verifikasi urutan baris kembali ke default Asset Name A-Z (`Crane Rental Unit`, `Excavator PC200`, `Wheel Loader`)

### TC-FA-FAAC-461: Sort kolom Assigned By

12. Klik header `Assigned By` sekali
13. Verifikasi urutan baris klik 1: A-Z (`Crane Rental Unit` oleh Budi S, lalu `Excavator PC200` dan `Wheel Loader` oleh Rina W)
14. Klik header `Assigned By` sekali lagi
15. Verifikasi urutan baris klik 2: Z-A (Rina W lebih dulu)
16. Klik header `Assigned By` sekali lagi
17. Verifikasi indikator sort netral
18. Verifikasi urutan baris kembali ke default Asset Name A-Z (`Crane Rental Unit`, `Excavator PC200`, `Wheel Loader`)

### TC-FA-FAAC-462: Kolom Label tidak dapat diurutkan

19. Klik header kolom `Label`
20. Verifikasi header `Label` tidak memiliki kontrol sort
21. Verifikasi urutan baris tetap default Asset Name A-Z

## Notes

1. Pengecualian nama seed literal: TC mewajibkan baris seed bernama literal (`HEAVY-EQ` dan Asset Name-nya) dan asersi bergantung pada nama itu; seed dipakai apa adanya tanpa suffix `{runId}`, isi tabel Asset Names hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Detail `HEAVY-EQ` dan tab `Asset Names` dibuka sekali di awal; langkah TC 'Klik tab Asset Names' pada blok berikutnya terpenuhi oleh tab yang sudah aktif (satu pembukaan, bagian 3).
3. Kolom Assigned At bernilai distinct pada dua tanggal (02/01/26 dan 14/03/26) dan Assigned By pada dua nilai (Rina W, Budi S) sehingga asersi sort bermakna (S-11).
4. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 2 sampai 4, termasuk Search untuk menemukan baris target (R-16).
5. Keadaan awal dinamis (S-14): langkah 1 menyetel `Crane Rental Unit` ter-assign ke `HEAVY-EQ` lewat fixture BE sebagai precondition TC-460; langkah ini bukan bagian TC dan tanpa `Verifikasi`.
