---
id: TC-FA-FAAC-E2E-141-picker-assign-search-dan-kolom
title: "Picker Assign: Search pada Lima Kolom dan Menyembunyikan Kolom Label dan Current Class"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-511
  - TC-FA-FAAC-512
  - TC-FA-FAAC-513
  - TC-FA-FAAC-514
  - TC-FA-FAAC-515
  - TC-FA-FAAC-525
coverage:
  web: automated
---

# Picker Assign: Search pada Lima Kolom dan Menyembunyikan Kolom Label dan Current Class

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Pre-setup picker Assign (hanya dibaca): Forklift 3T (Machinery > Warehouse; Label Warehouse dan Insured; tanpa Asset Class; 6 aset aktif), Laptop Standard (IT > Devices; Label IT dan Portable; tanpa Asset Class; 120 aset aktif), Delivery Van (Vehicles > Light; Label Fleet; Current Class Vehicles; 9), Office Chair (Furniture; Label kosong; Current Class Office Equipment; 0).
- Data Dinamis: Asset Class Active tanpa Asset Name ter-assign dengan Class Code literal `ANCHOR-141` dan Class Name `Anchor Class {runId}-141`, dibuat lewat API di hook `before` (setelah menghapus sisa run sebelumnya) dan dihapus di hook `after` (lihat Notes); dipakai sebagai Asset Class yang dibuka dan tidak diubah (tidak ada Asset Name yang di-assign).
- Keadaan awal picker (precondition butir d TC-FA-FAAC-511 sampai 515 dan 525): company uji hanya memiliki empat Asset Name di atas selama spec ini, sehingga asersi 'hanya memuat' dan 'tidak tampil' tidak tercampur seed Asset Name lain; keadaan ini disetel fixture BE pada langkah 1 dan seed Asset Name lain dipulihkan di hook `after` (kemampuan tim FE/BE; lihat `suite.md`).
- Nama seed Pre-setup picker (Forklift 3T, Laptop Standard, Delivery Van, Office Chair) memakai nama literal TC apa adanya karena asersi bergantung pada nama, Label, dan jumlah aset; dibaca saja. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Konfigurasi kolom: blok TC-525 menyembunyikan lalu menampilkan kembali kolom picker; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE).
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Setel keadaan awal lewat fixture BE: company uji hanya memiliki empat Asset Name `Forklift 3T`, `Laptop Standard`, `Delivery Van`, dan `Office Chair` (precondition butir d TC-FA-FAAC-511 sampai 515 dan 525)
2. Ketik Search `ANCHOR-141`, tekan Enter
3. Klik link Class Code `ANCHOR-141` di tabel
4. Klik tab `Asset Names`
5. Klik tombol `+ Assign Asset Names`
6. Hilangkan centang `Without asset class only`
7. Verifikasi picker memuat tepat empat Asset Name `Forklift 3T`, `Laptop Standard`, `Delivery Van`, dan `Office Chair`, tanpa Asset Name lain

### TC-FA-FAAC-511: Search picker Assign pada kolom Asset Name

8. Ketik Search `laptop` pada kotak `Search asset name...`, tekan Enter
9. Verifikasi picker hanya memuat baris `Laptop Standard`, sedangkan `Forklift 3T`, `Delivery Van`, dan `Office Chair` tidak tampil
10. Klik `(←)` pada kotak Search

### TC-FA-FAAC-512: Search picker Assign pada kolom Category

11. Ketik Search `Devices` pada kotak `Search asset name...`, tekan Enter
12. Verifikasi picker hanya memuat baris `Laptop Standard`, sedangkan `Forklift 3T`, `Delivery Van`, dan `Office Chair` tidak tampil
13. Klik `(←)` pada kotak Search

### TC-FA-FAAC-513: Search picker Assign pada kolom Label

14. Ketik Search `Fleet` pada kotak `Search asset name...`, tekan Enter
15. Verifikasi picker hanya memuat baris `Delivery Van`, sedangkan `Forklift 3T`, `Laptop Standard`, dan `Office Chair` tidak tampil
16. Klik `(←)` pada kotak Search

### TC-FA-FAAC-514: Search picker Assign pada kolom Current Class

17. Ketik Search `Vehicles` pada kotak `Search asset name...`, tekan Enter
18. Verifikasi picker hanya memuat baris `Delivery Van` (Current Class Vehicles), sedangkan `Forklift 3T`, `Laptop Standard`, dan `Office Chair` tidak tampil
19. Klik `(←)` pada kotak Search

### TC-FA-FAAC-515: Search picker Assign pada kolom Assets

20. Ketik Search `120` pada kotak `Search asset name...`, tekan Enter
21. Verifikasi picker hanya memuat baris `Laptop Standard`, sedangkan `Forklift 3T`, `Delivery Van`, dan `Office Chair` tidak tampil
22. Klik `(←)` pada kotak Search

### TC-FA-FAAC-525: Menyembunyikan kolom pada picker Assign

23. Klik ikon `⋯` pada header kolom Actions
24. Hilangkan centang `Label`
25. Hilangkan centang `Current Class`
26. Verifikasi kolom `Label` dan `Current Class` hilang dari tabel picker
27. Verifikasi kolom lain tidak terpengaruh
28. Centang kembali `Label` dan `Current Class`
29. Verifikasi kolom `Label` dan `Current Class` tampil lagi
30. Klik `Cancel` pada dialog picker Assign

## Notes

1. Pengecualian nama seed literal: nama Asset Name picker dan Label-nya dipakai apa adanya (S-06 dan S-12 dikecualikan dengan alasan ini); Asset Class yang dibuka adalah data milik spec.
2. Dialog picker Assign dibuka sekali per spec dan ditutup dengan `Cancel` di akhir tanpa memilih apa pun; `Verifikasi` tepat empat baris pada langkah 7 membuktikan keadaan awal (butir d TC) dan menjadi pembanding generik untuk asersi 'hanya memuat' dan 'tidak tampil' (bagian 8b butir 2).
3. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 sampai 4, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 30, termasuk Search untuk menemukan baris target (R-16).
4. Class Code `ANCHOR-141` ditulis literal dan `{runId}-141` dipindah ke Class Name karena Class Code dibatasi 15 karakter sehingga `ANCHOR-{runId}-141` tidak muat (S-12, nama literal; pola spec 066 sampai 069; kode berbeda antar spec); hook `before` menghapus sisa run sebelumnya dan hook `after` menghapus kode itu (cleanup tidak berasumsi setup berhasil penuh). Link Class Code dicari lewat Search kode literal itu (R-16).
5. Keadaan awal dinamis (S-14): langkah 1 menyetel lewat fixture BE bahwa company uji hanya memiliki empat Asset Name seed picker (precondition butir d TC-FA-FAAC-511 sampai 515 dan 525); langkah ini bukan bagian TC dan tanpa `Verifikasi`, dan seed Asset Name lain dipulihkan fixture BE di hook `after`.
