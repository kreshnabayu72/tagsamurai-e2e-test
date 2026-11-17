---
id: TC-FA-FAAC-E2E-139-tab-asset-names-kolom-dan-persistensi
title: "Tab Asset Names: Overlay Column Visibility, Kolom Terakhir Tidak Dapat Disembunyikan, dan Persistensi Setelah Muat Ulang"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-463
  - TC-FA-FAAC-465
  - TC-FA-FAAC-466
sourceRules: ["§4.1.3#r1", "§4.1.3#r2", "§4.1.3#r3", "§4.1.3#r4", "§4.1.3#r5", "§4.1.3#r6", "§4.4#r15", "§4.1.1#b2", "§5#b10"]
smoke: []
dependsOn: []
trace:
  "§4.1.3#r1": [6, 19]
  "§4.1.3#r2": 6
  "§4.1.3#r3": 6
  "§4.1.3#r4": 6
  "§4.1.3#r5": 6
  "§4.1.3#r6": 6
  "§4.4#r15": 7
  "§4.1.1#b2": [12, 13]
  "§5#b10": 20
coverage:
  web: automated
---

# Tab Asset Names: Overlay Column Visibility, Kolom Terakhir Tidak Dapat Disembunyikan, dan Persistensi Setelah Muat Ulang

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Pre-setup (isi tabel Asset Names hanya dibaca; keadaan awal `Crane Rental Unit` disetel fixture BE, lihat butir Keadaan awal dinamis): Asset Class Active 'Heavy Equipment' (`HEAVY-EQ`) memiliki tiga Asset Name ter-assign: Excavator PC200 (8 aset aktif; Machinery > Heavy Equipment; Label Heavy dan Insured; Assigned At 02/01/26; Assigned By Rina W), Wheel Loader (4 aset aktif; Machinery > Heavy Equipment; Label Heavy; 02/01/26; Rina W), Crane Rental Unit (0 aset aktif; Machinery > Rented; Label Rented; 14/03/26; Budi S). Tanggal Assigned At memakai format dd/mm/yy sesuai General Settings.
- Keadaan awal dinamis: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (3 Asset Name) menurut precondition TC-463; fixture BE menyetelnya pada langkah 1 dan memulihkan keadaan semula sesudah spec (hook `after`), karena TC lain (TC-34, TC-35, TC-270 sampai TC-281) memerlukan `Crane Rental Unit` tanpa Asset Class.
- Konfigurasi kolom: spec menyembunyikan kolom di tab Asset Names dan memulihkannya lewat langkah penghubung; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE). Muat ulang halaman pada blok TC-466 memakai kemampuan browser yang sama.
- Kode dan nama seed memakai nama literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada nama itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Setel keadaan awal lewat fixture BE: `Crane Rental Unit` ter-assign ke `HEAVY-EQ` (precondition TC-463)
2. Ketik Search `HEAVY-EQ`, tekan Enter
3. Klik link Class Code `HEAVY-EQ` di tabel
4. Klik tab `Asset Names`

### TC-FA-FAAC-463: Overlay Column Visibility memuat enam kolom

5. Klik ikon `⋯` pada header kolom Actions
6. Verifikasi overlay Column Visibility menampilkan enam kolom `Asset Name`, `Category`, `Label`, `Assets`, `Assigned At`, dan `Assigned By` dalam keadaan tercentang
7. Verifikasi overlay memuat item `Setup Column...`
8. Tutup overlay Column Visibility

### TC-FA-FAAC-465: Kolom terakhir yang visible tidak dapat disembunyikan

9. Klik ikon `⋯` pada header kolom Actions
10. Hilangkan centang lima kolom `Asset Name`, `Category`, `Label`, `Assets`, dan `Assigned At` sehingga hanya `Assigned By` tersisa
11. Arahkan kursor ke centang `Assigned By` dan coba hilangkan
12. Verifikasi centang `Assigned By` tidak dapat dihilangkan
13. Verifikasi tooltip menampilkan `At least one column must remain visible.`
14. Centang kembali lima kolom yang disembunyikan sehingga keenam kolom tampil
15. Tutup overlay Column Visibility

### TC-FA-FAAC-466: Pengaturan kolom bertahan setelah halaman dimuat ulang

16. Sembunyikan kolom `Label` lewat overlay Column Visibility
17. Muat ulang halaman (refresh)
18. Buka kembali Detail `HEAVY-EQ` lewat Search dan link Class Code lalu klik tab `Asset Names`
19. Verifikasi kolom `Asset Name` tampil di tabel tab Asset Names
20. Verifikasi kolom `Label` tetap tersembunyi setelah muat ulang
21. Tampilkan kembali kolom `Label` lewat overlay Column Visibility

## Notes

1. Pengecualian nama seed literal: TC mewajibkan baris seed bernama literal (`HEAVY-EQ` dan Asset Name-nya) dan asersi bergantung pada nama itu; seed dipakai apa adanya tanpa suffix `{runId}`, isi tabel Asset Names hanya dibaca (S-06 dan S-12 dikecualikan dengan alasan ini).
2. Detail `HEAVY-EQ` dan tab `Asset Names` dibuka sekali di awal; langkah TC 'Klik tab Asset Names' pada blok berikutnya terpenuhi oleh tab yang sudah aktif (satu pembukaan, bagian 3).
3. TC-464 (menyembunyikan dan menampilkan tiap kolom satu per satu) ada di spec 156.
4. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 2 sampai 4, 8, 14, 15, 18, 21, termasuk Search untuk menemukan baris target (R-16).
5. Keadaan awal dinamis (S-14): langkah 1 menyetel `Crane Rental Unit` ter-assign ke `HEAVY-EQ` lewat fixture BE sebagai precondition TC-463; langkah ini bukan bagian TC dan tanpa `Verifikasi`.
6. Anchor absence (8b butir 2): `Verifikasi` kolom `Asset Name` tampil (langkah 19) mendahului `Verifikasi` kolom `Label` tetap tersembunyi (langkah 20) pada tabel yang sama setelah muat ulang.
