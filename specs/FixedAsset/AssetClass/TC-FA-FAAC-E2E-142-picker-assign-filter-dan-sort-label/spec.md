---
id: TC-FA-FAAC-E2E-142-picker-assign-filter-dan-sort-label
title: "Picker Assign: Struktur Filter, Filter Category, Label, dan Rentang Assets, serta Kolom Label Tidak Dapat Diurutkan"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-516
  - TC-FA-FAAC-517
  - TC-FA-FAAC-518
  - TC-FA-FAAC-519
  - TC-FA-FAAC-524
coverage:
  web: automated
---

# Picker Assign: Struktur Filter, Filter Category, Label, dan Rentang Assets, serta Kolom Label Tidak Dapat Diurutkan

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Pre-setup picker Assign (hanya dibaca): Forklift 3T (Machinery > Warehouse; Label Warehouse dan Insured; tanpa Asset Class; 6 aset aktif), Laptop Standard (IT > Devices; Label IT dan Portable; tanpa Asset Class; 120 aset aktif), Delivery Van (Vehicles > Light; Label Fleet; Current Class Vehicles; 9), Office Chair (Furniture; Label kosong; Current Class Office Equipment; 0).
- Data Dinamis: Asset Class Active tanpa Asset Name ter-assign dengan Class Code literal `ANCHOR-142` dan Class Name `Anchor Class {runId}-142`, dibuat lewat API di hook `before` (setelah menghapus sisa run sebelumnya) dan dihapus di hook `after` (lihat Notes); dipakai sebagai Asset Class yang dibuka dan tidak diubah (tidak ada Asset Name yang di-assign).
- Keadaan awal picker (precondition butir d TC-FA-FAAC-516 sampai 519 dan 524): company uji hanya memiliki empat Asset Name di atas selama spec ini, sehingga asersi 'hanya memuat' dan 'tidak tampil' tidak tercampur seed Asset Name lain; keadaan ini disetel fixture BE pada langkah 1 dan seed Asset Name lain dipulihkan di hook `after` (kemampuan tim FE/BE; lihat `suite.md`).
- Nama seed Pre-setup picker (Forklift 3T, Laptop Standard, Delivery Van, Office Chair) memakai nama literal TC apa adanya karena asersi bergantung pada nama, Label, dan jumlah aset; dibaca saja. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Setel keadaan awal lewat fixture BE: company uji hanya memiliki empat Asset Name `Forklift 3T`, `Laptop Standard`, `Delivery Van`, dan `Office Chair` (precondition butir d TC-FA-FAAC-516 sampai 519 dan 524)
2. Ketik Search `ANCHOR-142`, tekan Enter
3. Klik link Class Code `ANCHOR-142` di tabel
4. Klik tab `Asset Names`
5. Klik tombol `+ Assign Asset Names`
6. Hilangkan centang `Without asset class only`
7. Verifikasi picker memuat tepat empat Asset Name `Forklift 3T`, `Laptop Standard`, `Delivery Van`, dan `Office Chair`, tanpa Asset Name lain

### TC-FA-FAAC-516: Screening Filter picker Assign

8. Klik tombol Filter pada toolbar dialog
9. Verifikasi Filter memuat field Category (multi-select) dengan placeholder `All categories`
10. Verifikasi Filter memuat field Label (multi-select) dengan placeholder `All labels`
11. Verifikasi Filter memuat field Assets dengan input `Min` dan `Max`
12. Verifikasi tidak ada field Current Class (diganti checkbox `Without asset class only`)

### TC-FA-FAAC-517: Filter picker Assign berdasarkan Category

13. Pada Category pilih `Devices`
14. Verifikasi picker hanya memuat baris `Laptop Standard`, sedangkan `Forklift 3T`, `Delivery Van`, dan `Office Chair` tidak tampil
15. Kosongkan filter Category

### TC-FA-FAAC-518: Filter picker Assign berdasarkan Label

16. Klik tombol Filter
17. Pada Label pilih `Insured`
18. Verifikasi picker hanya memuat baris `Forklift 3T`, sedangkan `Laptop Standard`, `Delivery Van`, dan `Office Chair` tidak tampil
19. Kosongkan filter Label

### TC-FA-FAAC-519: Filter picker Assign berdasarkan rentang Assets

20. Klik tombol Filter
21. Isi Assets Min = 7 dan Max = 100
22. Verifikasi picker hanya memuat baris `Delivery Van` (9), sedangkan `Forklift 3T` (6) dan `Laptop Standard` (120) tidak tampil
23. Kosongkan input Min dan Max pada filter Assets

### TC-FA-FAAC-524: Kolom Label picker Assign tidak dapat diurutkan

24. Klik header kolom `Label`
25. Verifikasi header `Label` tidak memiliki kontrol sort
26. Verifikasi urutan baris tidak berubah
27. Klik `Cancel` pada dialog picker Assign

## Notes

1. Pengecualian nama seed literal: nama Asset Name picker dan Label-nya dipakai apa adanya (S-06 dan S-12 dikecualikan dengan alasan ini); Asset Class yang dibuka adalah data milik spec.
2. Dialog picker Assign dibuka sekali per spec dan ditutup dengan `Cancel` di akhir tanpa memilih apa pun; `Verifikasi` tepat empat baris pada langkah 7 membuktikan keadaan awal (butir d TC) dan menjadi pembanding generik untuk asersi 'hanya memuat' dan 'tidak tampil' (bagian 8b butir 2).
3. Filter picker Assign memakai nilai pilihan yang disebut TC (Category `Devices`, Label `Insured`, Assets Min 7 dan Max 100); TC tidak menyebut tombol `Apply` pada Filter picker, sehingga spec mengikuti TC dan tidak menambah langkah `Apply` (Temuan untuk QA: TC perlu menyebut apakah filter picker berlaku langsung atau memakai `Apply`).
4. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 sampai 4, 15, 19, 23, 27, termasuk Search untuk menemukan baris target (R-16).
5. Class Code `ANCHOR-142` ditulis literal dan `{runId}-142` dipindah ke Class Name karena Class Code dibatasi 15 karakter sehingga `ANCHOR-{runId}-142` tidak muat (S-12, nama literal; pola spec 066 sampai 069; kode berbeda antar spec); hook `before` menghapus sisa run sebelumnya dan hook `after` menghapus kode itu (cleanup tidak berasumsi setup berhasil penuh). Link Class Code dicari lewat Search kode literal itu (R-16).
6. Keadaan awal dinamis (S-14): langkah 1 menyetel lewat fixture BE bahwa company uji hanya memiliki empat Asset Name seed picker (precondition butir d TC-FA-FAAC-516 sampai 519 dan 524); langkah ini bukan bagian TC dan tanpa `Verifikasi`, dan seed Asset Name lain dipulihkan fixture BE di hook `after`.
