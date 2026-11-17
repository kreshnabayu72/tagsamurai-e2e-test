---
id: TC-FA-FAAC-E2E-143-picker-assign-sort-kolom
title: "Picker Assign: Sort pada Kolom Asset Name, Category, Current Class, dan Assets"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-520
  - TC-FA-FAAC-521
  - TC-FA-FAAC-522
  - TC-FA-FAAC-523
sourceRules: ["§4.1.4#p1", "§4.1.4#r6", "§4.1.4#r7", "§4.1.4#r8", "§4.1.4#r9", "§4.1.4#r1", "§4.4#r14", "§9.5#r2", "§4.1.4#r2", "§4.1.4#r4", "§4.1.4#r5"]
smoke: []
dependsOn: []
trace:
  "§4.1.4#p1": 7
  "§4.1.4#r6": 7
  "§4.1.4#r7": 7
  "§4.1.4#r8": 7
  "§4.1.4#r9": 7
  "§4.1.4#r1": [9, 11]
  "§4.4#r14": [9, 11, 13, 14, 18, 23, 25, 26, 28, 30]
  "§9.5#r2": [14, 26]
  "§4.1.4#r2": [16, 18]
  "§4.1.4#r4": [21, 23]
  "§4.1.4#r5": [28, 30]
coverage:
  web: automated
---

# Picker Assign: Sort pada Kolom Asset Name, Category, Current Class, dan Assets

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed Pre-setup picker Assign (hanya dibaca): Forklift 3T (Machinery > Warehouse; Label Warehouse dan Insured; tanpa Asset Class; 6 aset aktif), Laptop Standard (IT > Devices; Label IT dan Portable; tanpa Asset Class; 120 aset aktif), Delivery Van (Vehicles > Light; Label Fleet; Current Class Vehicles; 9), Office Chair (Furniture; Label kosong; Current Class Office Equipment; 0).
- Data Dinamis: Asset Class Active tanpa Asset Name ter-assign dengan Class Code literal `ANCHOR-143` dan Class Name `Anchor Class {runId}-143`, dibuat lewat API di hook `before` (setelah menghapus sisa run sebelumnya) dan dihapus di hook `after` (lihat Notes); dipakai sebagai Asset Class yang dibuka dan tidak diubah (tidak ada Asset Name yang di-assign).
- Keadaan awal picker (precondition butir d TC-FA-FAAC-520 sampai 523): company uji hanya memiliki empat Asset Name di atas selama spec ini, sehingga asersi 'hanya memuat' dan 'tidak tampil' tidak tercampur seed Asset Name lain; keadaan ini disetel fixture BE pada langkah 1 dan seed Asset Name lain dipulihkan di hook `after` (kemampuan tim FE/BE; lihat `suite.md`).
- Nama seed Pre-setup picker (Forklift 3T, Laptop Standard, Delivery Van, Office Chair) memakai nama literal TC apa adanya karena asersi bergantung pada nama, Label, dan jumlah aset; dibaca saja. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE, pemulihan Setup Column): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

1. Setel keadaan awal lewat fixture BE: company uji hanya memiliki empat Asset Name `Forklift 3T`, `Laptop Standard`, `Delivery Van`, dan `Office Chair` (precondition butir d TC-FA-FAAC-520 sampai 523)
2. Ketik Search `ANCHOR-143`, tekan Enter
3. Klik link Class Code `ANCHOR-143` di tabel
4. Klik tab `Asset Names`
5. Klik tombol `+ Assign Asset Names`
6. Hilangkan centang `Without asset class only`
7. Verifikasi picker memuat tepat empat Asset Name `Forklift 3T`, `Laptop Standard`, `Delivery Van`, dan `Office Chair`, tanpa Asset Name lain

### TC-FA-FAAC-520: Sort kolom Asset Name picker Assign

8. Klik header `Asset Name` sekali
9. Verifikasi urutan baris klik 1: A-Z (`Delivery Van`, `Forklift 3T`, `Laptop Standard`, `Office Chair`)
10. Klik header `Asset Name` sekali lagi
11. Verifikasi urutan baris klik 2: Z-A (`Office Chair`, `Laptop Standard`, `Forklift 3T`, `Delivery Van`)
12. Klik header `Asset Name` sekali lagi
13. Verifikasi indikator sort netral
14. Verifikasi urutan baris kembali ke default Asset Name A-Z

### TC-FA-FAAC-521: Sort kolom Category picker Assign

15. Klik header `Category` sekali
16. Verifikasi urutan baris klik 1: A-Z menurut leaf (`Laptop Standard` Devices, `Office Chair` Furniture, `Delivery Van` Light, `Forklift 3T` Warehouse)
17. Klik header `Category` sekali lagi
18. Verifikasi urutan baris klik 2: Z-A (urutan kebalikan klik 1)
19. Klik header `Category` sekali lagi hingga indikator sort netral

### TC-FA-FAAC-522: Sort kolom Current Class picker Assign

20. Klik header `Current Class` sekali
21. Verifikasi urutan baris klik 1: A-Z menurut label badge (`Office Chair` Office Equipment, `Delivery Van` Vehicles, lalu `Forklift 3T` dan `Laptop Standard` dengan Current Class `—` di akhir, sesama `—` mengikuti default Asset Name A-Z)
22. Klik header `Current Class` sekali lagi
23. Verifikasi urutan baris klik 2: Z-A (`Forklift 3T` dan `Laptop Standard` dengan `—` di awal, urut Asset Name A-Z, lalu `Delivery Van` Vehicles, `Office Chair` Office Equipment)
24. Klik header `Current Class` sekali lagi
25. Verifikasi indikator sort netral
26. Verifikasi urutan baris kembali ke default Asset Name A-Z

### TC-FA-FAAC-523: Sort kolom Assets picker Assign

27. Klik header `Assets` sekali
28. Verifikasi urutan baris klik 1: numerik naik (`Office Chair` 0, `Forklift 3T` 6, `Delivery Van` 9, `Laptop Standard` 120)
29. Klik header `Assets` sekali lagi
30. Verifikasi urutan baris klik 2: numerik turun (urutan kebalikan klik 1)
31. Klik header `Assets` sekali lagi hingga indikator sort netral

32. Klik `Cancel` pada dialog picker Assign

## Notes

1. Pengecualian nama seed literal: nama Asset Name picker dan Label-nya dipakai apa adanya (S-06 dan S-12 dikecualikan dengan alasan ini); Asset Class yang dibuka adalah data milik spec.
2. Dialog picker Assign dibuka sekali per spec dan ditutup dengan `Cancel` di akhir tanpa memilih apa pun; `Verifikasi` tepat empat baris pada langkah 7 membuktikan keadaan awal (butir d TC) dan menjadi pembanding generik untuk asersi 'hanya memuat' dan 'tidak tampil' (bagian 8b butir 2).
3. TC-521 dan TC-523 hanya menyebut dua klik; langkah klik ketiga setelah klik 2 adalah langkah penghubung yang mengembalikan sort ke netral supaya TC berikutnya mulai dari default (S-09).
4. Z-A pada TC-521 dan TC-523 tidak menyebut urutan baris; spec mengasersi kebalikan urutan klik 1 yang memuat empat nilai distinct (S-11).
5. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1 sampai 4, 19, 31, 32, termasuk Search untuk menemukan baris target (R-16).
6. Class Code `ANCHOR-143` ditulis literal dan `{runId}-143` dipindah ke Class Name karena Class Code dibatasi 15 karakter sehingga `ANCHOR-{runId}-143` tidak muat (S-12, nama literal; pola spec 066 sampai 069; kode berbeda antar spec); hook `before` menghapus sisa run sebelumnya dan hook `after` menghapus kode itu (cleanup tidak berasumsi setup berhasil penuh). Link Class Code dicari lewat Search kode literal itu (R-16).
7. Keadaan awal dinamis (S-14): langkah 1 menyetel lewat fixture BE bahwa company uji hanya memiliki empat Asset Name seed picker (precondition butir d TC-FA-FAAC-520 sampai 523); langkah ini bukan bagian TC dan tanpa `Verifikasi`, dan seed Asset Name lain dipulihkan fixture BE di hook `after`.
