---
id: TC-FA-MISS-BE-079-download-isi-berkas
title: "Server: isi berkas Missing-Active dan Missing-History per tipe kolom, BOM, sheet, urutan sort, 0 baris, kolom TAG hanya tipe terbuka"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: [EB-DL-4, EB-DL-5, §5#r6, §9.10#p1, §9.11#b1, §4.1a#r6, §4.1a#r12, §8.2#b3]
smoke: []
dependsOn: []
trace:
  EB-DL-4: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 22, 24, 25, 28, 30, 38]
  EB-DL-5: 32
  §5#r6: [4, 24, 27]
  §9.10#p1: 19
  §9.11#b1: 35
  §4.1a#r6: [7, 19]
  §4.1a#r12: 15
  §8.2#b3: 20
---

# Server: isi berkas Missing-Active dan Missing-History per tipe kolom, BOM, sheet, urutan sort, 0 baris, kolom TAG hanya tipe terbuka

## Prerequisites
- Aktor: `Hendra Pratama {runId}` (DU-079-1), Total Control dengan cakupan seluruh client; `Hari Susanto {runId}` (DU-079-2), pemegang View asset value dengan Group Head Office beserta descendant.
- Data:
  - DU-079-1: User Name `Hendra Pratama {runId}`, Peran `Total Control`, Cakupan `seluruh client`.
  - DU-079-2: User Name `Hari Susanto {runId}`, Peran `View asset value`, Cakupan `Group Head Office beserta descendant`.
  - DU-079-3: User Name `Budi Santoso {runId}`, Peran `karyawan tanpa akun`.
  - DU-079-4: User Name `Sari Dewi {runId}`, Peran `pemegang tanpa hak Aktor Missing`.
  - DU-079-5: User Name `Rudi Hartono {runId}`, Peran `PIC`.
  - DU-079-6: User Name `Joko Susilo {runId}`, Peran `karyawan tanpa akun`.
  - DU-079-7: Asset Name `Camera Canon EOS Berkas {runId}`, Asset ID `FA079-001`, Status `Missing`, Source `Manual`, TAG `NFC, QR`, Brand `Canon`, Model/Type `EOS R6`, Group `Head Office > Finance Room`, Category `Elektronik > Kamera`, Last Holder `Budi Santoso {runId}`, Reported By `Hendra Pratama {runId}`, Reported Date `T0 − 5 hari, pukul 09:00`, Purchase Cost `12500000`, Last Seen `Gate A reader pada T0 − 3 hari, pukul 09:00`.
  - DU-079-8: Asset Name `Printer, Laser HP M404 Berkas {runId}`, Asset ID `FA079-002`, Status `Waiting for Confirmation`, Source `Manual`, TAG `tidak ada`, Brand `tidak ada`, Model/Type `tidak ada`, Group `Head Office > Finance Room`, Category `Elektronik > Printer`, Last Holder `Sari Dewi {runId}`, Reported By `Sari Dewi {runId}`, Reported Date `T0 − 3 hari, pukul 09:00`, Purchase Cost `tidak ada`, Last Seen `tidak ada TAG`.
  - DU-079-9: Asset Name `Monitor 27" LG Berkas {runId}`, Asset ID `FA079-003`, Status `Missing`, Source `Manual`, TAG `QR`, Brand `LG`, Model/Type `27UL500`, Group `Head Office > Finance Room`, Category `Elektronik > Monitor`, Last Holder `tidak ada`, Reported By `Hendra Pratama {runId}`, Reported Date `T0 − 9 hari, pukul 09:00`, Purchase Cost `4500000`.
  - DU-079-10: Asset Name `Café Élan Rak Berkas {runId}`, Asset ID `FA079-004`, Status `Missing`, Source `Manual`, TAG `RFID`, Brand `tidak ada`, Model/Type `tidak ada`, Group `Head Office > Server Room`, Category `Furnitur > Rak`, Last Holder `tidak ada`, Reported By `Hendra Pratama {runId}`, Reported Date `T0 − 14 hari, pukul 09:00`, Purchase Cost `1750000`.
  - DU-079-11: Asset Name `Hand Pallet Truck Berkas {runId}`, Asset ID `FA079-005`, Status `Missing`, Source `Manual`, TAG `BLE`, Brand `tidak ada`, Model/Type `tidak ada`, Group `Warehouse`, Category `Alat Angkut > Troli`, Last Holder `Joko Susilo {runId}`, Reported By `Rudi Hartono {runId} (on behalf of Joko Susilo {runId})`, Reported Date `T0 − 31 hari, pukul 09:00`, Purchase Cost `2300000`.
  - DU-079-12: Asset Name `Gudang Cabang {n} Volume {runId}`, Status `Missing`, Source `Manual`, Group `Head Office > Finance Room`.
  - DU-079-13: Asset Name `Projector Epson EB-X06 Berkas {runId}`, Asset ID `FA079-011`, Status `Found`, Source `Borrow`, TAG `NFC`, Reported By `Hendra Pratama {runId}`, Reported Date `T0 − 30 hari, pukul 09:00`, Resolved By `Hendra Pratama {runId}`, Resolved Date `T0 − 20 hari, pukul 09:00`, Duration `10 days`.
  - DU-079-14: Asset Name `Toyota Innova Berkas {runId}`, Asset ID `FA079-012`, Status `Disposed`, Source `Manual`, TAG `NFC`, Reported By `Hendra Pratama {runId}`, Reported Date `T0 − 90 hari, pukul 09:00`, Resolved By `System`, Resolved Date `T0 − 10 hari, pukul 09:00`, Duration `80 days`.
  - DU-079-18: Asset Name `Genset Honda EU22 Multilabel {runId}`, Asset ID `FA079-018`, Status `Missing`, Source `Manual`, TAG `NFC`, Labels `Aset Kritis, Garansi Aktif, Pinjaman Cabang`, Brand `Honda`, Model/Type `EU22i`, Group `Head Office > Server Room`, Category `Elektronik > Genset`, Last Holder `tidak ada`, Reported By `Hendra Pratama {runId}`, Reported Date `T0 − 2 hari, pukul 09:00`, Purchase Cost `18500000`.
- Kondisi:
  - Plan client membuka semua tipe TAG `RFID`, `NFC`, `QR`, `BLE`, dan `GPS`
  - Date Format bernilai `DD/MM/YY`
  - Time Format bernilai `HH:mm`

## Test Steps
### Berkas CSV Active memuat isi per tipe kolom dan mengikuti saringan, kolom, dan urutan aktif
1. `Hendra Pratama {runId}` menampilkan kolom Brand, Model/Type, TAG, Category, Last Holder, Last Seen, dan Purchase Cost lewat Setup Column
2. `Hendra Pratama {runId}` menyembunyikan kolom Source lewat Setup Column
3. `Hendra Pratama {runId}` mengambil Download as CSV dari sub-tab Active dengan Search `Berkas {runId}`
4. Verifikasi berkas bernama `Missing-Active.csv`, berpemisah koma, dan berkodekan UTF-8 dengan BOM
5. Verifikasi berkas tidak memuat kolom Photo
6. Verifikasi berkas tidak memuat kolom Source karena kolom itu sedang disembunyikan
7. Verifikasi sel TAG baris `Camera Canon EOS Berkas {runId}` bernilai `NFC, QR` sebagai label ikon yang dipisah koma dan spasi, dan sel TAG baris `Monitor 27" LG Berkas {runId}` bernilai `QR`
8. Verifikasi sel Status baris `Camera Canon EOS Berkas {runId}` bernilai `Missing` dan baris `Printer, Laser HP M404 Berkas {runId}` bernilai `Waiting for Confirmation` sebagai teks label tanpa warna
9. Verifikasi sel Brand dan Model/Type baris `Camera Canon EOS Berkas {runId}` bernilai `Canon` dan `EOS R6` tanpa hierarki
10. Verifikasi sel Group baris `Camera Canon EOS Berkas {runId}` bernilai `Head Office > Finance Room` dan sel Category bernilai `Elektronik > Kamera` sebagai hierarki penuh dari root
11. Verifikasi sel Last Holder baris `Camera Canon EOS Berkas {runId}` bernilai `Budi Santoso {runId}` sebagai nama lengkap, dan sel Reported By baris `Hand Pallet Truck Berkas {runId}` memuat `Rudi Hartono {runId}` beserta `Joko Susilo {runId}` sebagai nama lengkap
12. Verifikasi sel Days Missing baris `Camera Canon EOS Berkas {runId}` bernilai angka `5` tanpa kata `days`
13. Verifikasi sel Purchase Cost baris `Camera Canon EOS Berkas {runId}` bernilai angka `12500000` tanpa simbol mata uang dan tanpa pemisah ribuan
14. Verifikasi sel Brand baris `Printer, Laser HP M404 Berkas {runId}` bernilai `-` dan bukan sel kosong, `—`, maupun `null`
15. Verifikasi sel Last Seen baris `Camera Canon EOS Berkas {runId}` memuat tanggal dan jam menurut Date Format dan Time Format yang berlaku, lalu pemindai `Gate A reader`, dan baris `Printer, Laser HP M404 Berkas {runId}` bernilai `-`
16. Verifikasi nama baris `Printer, Laser HP M404 Berkas {runId}` yang memuat koma dibungkus tanda kutip ganda
17. Verifikasi nama baris `Monitor 27" LG Berkas {runId}` yang memuat tanda kutip ganda dibungkus tanda kutip ganda dengan kutip di dalamnya digandakan
18. Verifikasi nama baris `Café Élan Rak Berkas {runId}` yang memuat karakter non-ASCII terbaca utuh
19. Verifikasi kolom TAG hanya memuat tipe TAG yang terbuka di plan client
20. Verifikasi Download itu tidak menambah entri Activity Log maupun System Log milik `Hendra Pratama {runId}`
21. `Hendra Pratama {runId}` mengambil Download as CSV dari sub-tab Active dengan Search `Berkas {runId}` diurutkan menurut Days Missing ascending
22. Verifikasi urutan baris berkas mengikuti sort aktif: `Printer, Laser HP M404 Berkas {runId}`, lalu `Camera Canon EOS Berkas {runId}`, `Monitor 27" LG Berkas {runId}`, `Café Élan Rak Berkas {runId}`, dan `Hand Pallet Truck Berkas {runId}`

### Berkas XLSX Active memuat satu sheet dan sel angka
23. `Hendra Pratama {runId}` mengambil Download as XLSX dari sub-tab Active dengan Search `Berkas {runId}`
24. Verifikasi berkas bernama `Missing-Active.xlsx` dan hanya memuat satu sheet bernama `Sheet1`
25. Verifikasi sel Days Missing dan Purchase Cost baris `Camera Canon EOS Berkas {runId}` bertipe angka, bukan teks

### Berkas History memakai nama dan isi tab History
26. `Hendra Pratama {runId}` mengambil Download as CSV dari sub-tab History dengan Search `Berkas {runId}`
27. Verifikasi berkas bernama `Missing-History.csv` dan memuat baris `Projector Epson EB-X06 Berkas {runId}` dan `Toyota Innova Berkas {runId}`, tanpa baris sub-tab Active
28. Verifikasi sel Duration baris `Projector Epson EB-X06 Berkas {runId}` bernilai angka `10` dan sel Resolved By baris `Toyota Innova Berkas {runId}` bernilai `System`

### Nol baris menghasilkan berkas berisi header saja
29. `Hendra Pratama {runId}` mengambil Download as CSV dari sub-tab Active dengan Search `zzq-079-tidak-ada`
30. Verifikasi permintaan diterima, berkas hanya memuat baris header kolom yang visible, dan tidak ada toast

### Download di atas 5.000 baris langsung terunduh lengkap
31. `Hendra Pratama {runId}` mengambil Download as CSV dari sub-tab Active dengan Search `Volume {runId}`
32. Verifikasi berkas memuat seluruh 5.001 baris data, bukan hanya satu halaman, dan langsung terunduh tanpa job latar dan tanpa notifikasi in-app

### Pemegang View asset value mengunduh kolom finansial pada Group yang di-assign
33. `Hari Susanto {runId}` menampilkan kolom Purchase Cost lewat Setup Column
34. `Hari Susanto {runId}` mengambil Download as CSV dari sub-tab Active dengan Search `Berkas {runId}`
35. Verifikasi berkas memuat kolom Purchase Cost dengan nilai `12500000` pada baris `Camera Canon EOS Berkas {runId}`, dan tidak memuat baris `Hand Pallet Truck Berkas {runId}` yang berada di Group `Warehouse`

### Berkas CSV memuat semua label pada kolom badge ber-item banyak
36. `Hendra Pratama {runId}` menampilkan kolom Labels lewat Setup Column
37. `Hendra Pratama {runId}` mengambil Download as CSV dari sub-tab Active dengan Search `Multilabel {runId}`
38. Verifikasi sel Labels baris `Genset Honda EU22 Multilabel {runId}` memuat ketiga label `Aset Kritis`, `Garansi Aktif`, dan `Pinjaman Cabang` seluruhnya sebagai teks label, dipisah koma dan spasi
