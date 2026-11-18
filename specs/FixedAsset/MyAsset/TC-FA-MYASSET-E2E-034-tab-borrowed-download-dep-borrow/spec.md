---
id: TC-FA-MYASSET-E2E-034-tab-borrowed-download-dep-borrow
title: "Download tab Borrowed: cakupan baris dan kolom, nama berkas CSV dan XLSX, tanpa toast sukses"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§5#r6", "EB-FB-2@download", "EB-DL-1@tabel-borrowed", "EB-DL-2@tabel-borrowed", "EB-DL-3@tabel-borrowed", "EB-DL-4"]
smoke: ["EB-DL-4"]
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§5#r6": [3, 6, 7, 46, 47]
  "EB-FB-2@download": [5, 36]
  "EB-DL-1@tabel-borrowed": [7, 8, 18, 31, 46, 47]
  "EB-DL-2@tabel-borrowed": [5, 36]
  "EB-DL-3@tabel-borrowed": [6, 13]
  "EB-DL-4": [9, 10, 24, 37]
anchor: [1, 15, 21, 30, 33, 42, 43]
coverage:
  web: automated
---

# Download tab Borrowed: cakupan baris dan kolom, nama berkas CSV dan XLSX, tanpa toast sukses

## Prerequisites
- Aktor: Borrower `Fitri Handayani {runId}`, pengguna karyawan ber-akun login tanpa role admin.
- Layar awal: halaman My Asset, tab `Borrowed`.
- Data:
  - DU-034-1: User `Fitri Handayani {runId}`, tanpa role admin, cakupan Group `Head Office`.
  - DU-034-2: 12 pinjaman Admin atas nama `Fitri Handayani {runId}`, aset `Kursi Kerja {n} {runId}` dengan n dari 1 sampai 12, Brand `Informa`, Model/Type `Kursi`, Group `Head Office`, Status `Borrowed`, Duration `3 days`, Handed Over At `T0`.
  - DU-034-3: pinjaman Admin atas nama `Fitri Handayani {runId}`, aset `Proyektor Epson EB-X06 {runId}`, Brand `Epson`, Model/Type `EB-X06`, Group `Head Office`, Status `Borrowed`, Duration `2 days`, Handed Over At `T0`, Due Date `T0 + 2 hari`.
  - DU-034-4: pinjaman Admin atas nama `Fitri Handayani {runId}`, aset `Scanner Epson DS-530 {runId}`, Brand kosong, Model/Type `DS-530`, Group `Head Office`, Status `Borrowed`, Duration `5 days`, Handed Over At `T0`, Due Date `T0 + 5 hari`.
  - DU-034-5: pinjaman Admin atas nama `Fitri Handayani {runId}`, aset `Kamera Canon EOS 90D {runId}`, Brand `Canon`, Model/Type `EOS 90D`, Group `Head Office`, Status `Returned`, Duration `3 days`, Handed Over At `T0 − 6 hari`, Closed At `T0 − 3 hari`. Baris ini hanya ada di tab History.
  - Kata kunci Search: DU-034-6 `Epson`, DU-034-7 `Tidak Ada Barang Ini`.
  - Nilai Filter: DU-034-8 field `Brand` dengan nilai `Epson`.
- Kondisi:
  - Tab Borrowed `Fitri Handayani {runId}` berisi 14 baris aset, dari DU-034-2 sampai DU-034-4, dengan 10 baris per halaman bawaan.
  - Tidak ada Search, Filter, dan Sort aktif pada tabel Borrowed.

## Test Steps

### Download tanpa saringan memuat seluruh baris tab Borrowed
1. Verifikasi halaman pertama tabel Borrowed memuat 10 baris
2. Klik ikon `Download` pada toolbar
3. Verifikasi pilihan `Download as CSV` dan `Download as XLSX` tampil
4. Klik `Download as CSV`
5. Verifikasi tidak ada toast sukses yang tampil sesudah Download
6. Verifikasi berkas `My-Asset-Borrowed.csv` terunduh
7. Verifikasi berkas memuat 14 baris data walau tabel hanya menampilkan 10 baris per halaman
8. Verifikasi berkas tidak memuat baris `Kamera Canon EOS 90D {runId}` yang hanya ada di tab History
9. Verifikasi berkas tidak memuat kolom `Photo`
10. Verifikasi sel Brand baris `Scanner Epson DS-530 {runId}` di berkas bernilai `-`

### Download berkas XLSX
11. Klik ikon `Download` pada toolbar
12. Klik `Download as XLSX`
13. Verifikasi berkas `My-Asset-Borrowed.xlsx` terunduh

### Download hasil Search hanya memuat baris yang cocok
14. Ketik Search `Epson`, tekan Enter
15. Verifikasi tabel hanya memuat baris `Proyektor Epson EB-X06 {runId}` dan `Scanner Epson DS-530 {runId}`
16. Klik ikon `Download` pada toolbar
17. Klik `Download as CSV`
18. Verifikasi berkas memuat tepat dua baris data, yaitu `Proyektor Epson EB-X06 {runId}` dan `Scanner Epson DS-530 {runId}`

### Urutan baris berkas mengikuti Sort aktif
19. Klik header kolom Duration
20. Klik header kolom Duration
21. Verifikasi tabel menampilkan baris `Scanner Epson DS-530 {runId}` lalu `Proyektor Epson EB-X06 {runId}` dari atas ke bawah menurut Longest First
22. Klik ikon `Download` pada toolbar
23. Klik `Download as CSV`
24. Verifikasi baris berkas berurutan `Scanner Epson DS-530 {runId}` lalu `Proyektor Epson EB-X06 {runId}`

### Kolom yang disembunyikan tidak ikut diunduh
25. Klik header kolom Actions `⋯` untuk membuka Column Visibility
26. Hapus centang kolom `Brand`
27. Tekan `Esc` untuk menutup Column Visibility
28. Klik ikon `Download` pada toolbar
29. Klik `Download as CSV`
30. Verifikasi berkas memuat kolom `Name`
31. Verifikasi berkas tidak memuat kolom `Brand` yang sedang disembunyikan

### Download tanpa hasil menghasilkan berkas berisi header saja
32. Ganti isi kotak search dengan `Tidak Ada Barang Ini`, tekan Enter
33. Verifikasi empty state `No results found` tampil
34. Klik ikon `Download` pada toolbar
35. Klik `Download as CSV`
36. Verifikasi tidak ada toast yang tampil sesudah Download tanpa hasil
37. Verifikasi berkas hanya memuat baris header kolom yang tampil tanpa baris data

### Download hasil Filter hanya memuat baris yang lolos Filter
38. Klik `(←)` pada kotak Search
39. Klik ikon `Filter` pada toolbar
40. Pilih `Epson` pada field Filter `Brand`
41. Klik `[Apply]`
42. Verifikasi baris `Proyektor Epson EB-X06 {runId}` tampil di tabel
43. Verifikasi Filter `Brand` bernilai `Epson` menyisakan baris `Proyektor Epson EB-X06 {runId}` saja di tabel
44. Klik ikon `Download` pada toolbar
45. Klik `Download as CSV`
46. Verifikasi berkas memuat tepat satu baris data, yaitu `Proyektor Epson EB-X06 {runId}`
47. Verifikasi berkas tidak memuat baris `Scanner Epson DS-530 {runId}` yang Brand-nya kosong
