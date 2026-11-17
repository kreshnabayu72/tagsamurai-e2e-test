---
id: TC-FA-DAMAGED-BE-211-download-isi-berkas
title: "Isi berkas Download Damaged-Active dan Damaged-History per tipe kolom, encoding CSV, cakupan baris dan kolom mengikuti saringan, kolom nilai finansial menurut hak, dan ambang 5.000 baris"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§5#r6", "EB-DL-4", "EB-DL-5", "T-DMG-01", "T-DMG-02", "§2.1#r10"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§5#r6": [2, 5, 7, 19, 30, 32, 47, 54]
  "EB-DL-4": [3, 5, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 21, 23, 25, 27, 28, 34, 36, 38, 40, 42, 44]
  "EB-DL-5": [47, 49, 50]
  "T-DMG-01": [2, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 23, 25, 30, 32, 34, 38, 40, 42, 44, 56]
  "T-DMG-02": [7, 27, 28]
  "§2.1#r10": [52, 54, 56]
---

# Isi berkas Download Damaged-Active dan Damaged-History per tipe kolom, encoding CSV, cakupan baris dan kolom mengikuti saringan, kolom nilai finansial menurut hak, dan ambang 5.000 baris

## Prerequisites
- Aktor:
  - Total Control `Agus Pratama {runId}`, seluruh client, berhak melihat nilai finansial.
  - Group Manager `Gunawan Hartono {runId}`, binaan Group `Head Office {runId}` beserta sub-group.
  - Read Only `Rosa Maharani {runId}`, tanpa hak lihat nilai finansial.
  - Pelapor umum `Budi Santoso {runId}`, tanpa role Damaged.
- Data:
  - DU-211-1: User `Agus Pratama {runId}`, Total Control, cakupan seluruh client.
  - DU-211-2: User `Gunawan Hartono {runId}`, Group Manager, cakupan Group `Head Office {runId}` beserta sub-group.
  - DU-211-3: User `Rosa Maharani {runId}`, Read Only, cakupan seluruh client tanpa hak lihat nilai finansial.
  - DU-211-4: User `Budi Santoso {runId}`, pelapor umum, cakupan aset yang ia pegang.
  - DU-211-5: User `Siti Nur Rahmawati {runId}`, Total Control, pelaku node terbaru record `Laptop Lenovo ThinkPad - 301 {runId}`, nama belakang dua kata, cakupan seluruh client.
  - DU-211-6: Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}`.
  - DU-211-7: Group `Bandung Office {runId} > Floor 2 {runId}`, leaf-nya sama dengan Group di bawah `Head Office {runId}` tetapi parent berbeda.
  - DU-211-8: Aset `Laptop Lenovo ThinkPad - 301 {runId}`, Asset ID `LPT-0301-{runId}`, Status `Damaged`, Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}`, TAG `RFID, NFC`, Brand `Lenovo {runId}`, Model/Type `ThinkPad X1 {runId}`, Category `Elektronik {runId} > Laptop {runId}`, Source `Manual`, Last Holder `—`, Reported By `Agus P`, Modified By `Siti Nur Rahmawati {runId}`, Labels `Prioritas {runId}, Aset Kantor {runId}, Aset Lantai Dua {runId}`, Purchase Cost `12500000`, Asset Value (Commercial) `10000000`, Days Damaged `7`, sub-tab Active.
  - DU-211-9: Aset `Laptop Lenovo ThinkPad - 302 {runId}`, Asset ID `LPT-0302-{runId}`, Status `Waiting for Confirmation`, Group `Bandung Office {runId} > Floor 2 {runId}`, TAG `QR`, Brand `Lenovo {runId}`, Source `Reported by holder`, Purchase Cost `4500000`, sub-tab Active.
  - DU-211-10: Aset `Printer Canon Pixma - 303 {runId}`, Asset ID `PRN-0303-{runId}`, Status `Reported Disposal`, Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}`, TAG `RFID`, Brand `Canon {runId}`, Source `Stock opname`, Purchase Cost `2100000`, sub-tab Active.
  - DU-211-11: Aset `Printer Canon Pixma - 304 {runId}`, Asset ID `PRN-0304-{runId}`, Status `In Disposal Process`, Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}`, TAG `RFID`, Brand `Canon {runId}`, Source `Manual`, Purchase Cost `3300000`, sub-tab Active.
  - DU-211-12: Aset `Monitor, Curved Dell - 305 {runId}`, Asset ID `MON-0305-{runId}`, Status `Damaged`, Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}`, TAG `QR`, Brand `Dell {runId}`, Source `Manual`, sub-tab Active.
  - DU-211-13: Aset `Monitor "Curved" 27 inci - 306 {runId}`, Asset ID `MON-0306-{runId}`, Status `Damaged`, Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}`, TAG `QR`, Brand `Dell {runId}`, Source `Manual`, sub-tab Active.
  - DU-211-14: Aset `Printer Epson L3150 - 307 {runId}`, Asset ID `PRN-0307-{runId}`, Status `Damaged`, Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}`, TAG `QR`, Brand `Epson {runId}`, Source `Manual`, Alias Name `Printer Lobi
Lantai 2 {runId}`, sub-tab Active.
  - DU-211-15: Aset `Kamera Café Élan - 308 {runId}`, Asset ID `CAM-0308-{runId}`, Status `Damaged`, Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}`, TAG `RFID`, Brand `Café Élan {runId}`, Source `Manual`, sub-tab Active.
  - DU-211-16: Aset `Laptop Lenovo ThinkPad - 311 {runId}`, Asset ID `HST-h1-{runId}`, Status `Repaired`, Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}`, TAG `RFID`, Brand `Lenovo {runId}`, Source `Manual`, Resolved By `Agus P`, Duration `6`, sub-tab History.
  - DU-211-17: Aset `Drill Bosch GSB - 312 {runId}`, Asset ID `HST-h2-{runId}`, Status `Disposed`, Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}`, TAG `RFID`, Brand `Lenovo {runId}`, Source `Manual`, Resolved By `System`, Duration `62`, sub-tab History.
  - DU-211-18: Aset `Camera Canon EOS - 313 {runId}`, Asset ID `HST-h3-{runId}`, Status `Rejected`, Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}`, TAG `RFID`, Brand `Lenovo {runId}`, Source `Manual`, Resolved By `Rina W`, Duration `1`, sub-tab History.
  - DU-211-19: Aset `Scanner Fujitsu fi-7160 - 314 {runId}`, Asset ID `HST-h4-{runId}`, Status `Canceled`, Group `Head Office {runId} > Floor 2 {runId} > Server Room {runId}`, TAG `RFID`, Brand `Lenovo {runId}`, Source `Manual`, Resolved By `Dewi A`, Duration `1`, sub-tab History.
  - DU-211-20: Aset `Aset Volume A {n} {runId}` sebanyak 5.000 record `Damaged` di Group `Head Office {runId}`.
  - DU-211-21: Aset `Aset Volume B {n} {runId}` sebanyak 5.001 record `Damaged` di Group `Head Office {runId}`.
  - DU-211-22: Group `Head Office {runId}`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24h`.

## Test Steps

### Nama berkas, ekstensi, dan struktur mengikuti sub-tab dan pilihan format
1. Total Control `Agus Pratama {runId}` memilih Download as CSV pada sub-tab Active dengan Search `ThinkPad - 301 {runId}`
2. Verifikasi berkas bernama `Damaged-Active` dengan ekstensi `.csv` sesuai pilihan format
3. Verifikasi berkas CSV memakai encoding UTF-8 dengan BOM dan pemisah koma
4. Total Control `Agus Pratama {runId}` memilih Download as XLSX pada sub-tab Active dengan Search `ThinkPad - 301 {runId}`
5. Verifikasi berkas bernama `Damaged-Active` dengan ekstensi `.xlsx` dan satu sheet bernama `Sheet1`
6. Total Control `Agus Pratama {runId}` memilih Download as CSV pada sub-tab History dengan Search `{runId}`
7. Verifikasi berkas bernama `Damaged-History` dan memuat record `Laptop Lenovo ThinkPad - 311 {runId}` sampai `Scanner Fujitsu fi-7160 - 314 {runId}`, bukan record Active

### Isi sel per tipe kolom pada sub-tab Active
8. Total Control `Agus Pratama {runId}` mengunduh CSV sub-tab Active dengan Search `ThinkPad - 301 {runId}` setelah kolom Brand, Model/Type, TAG, Category, Labels, Purchase Cost, Asset Value (Commercial), dan Modified By ditampilkan
9. Verifikasi kolom Photo tidak ikut dan sel foto tidak ada di berkas
10. Verifikasi kolom TAG berisi label ikon `RFID, NFC` terpisah koma dan spasi, bukan nama komponen ikon
11. Verifikasi kolom Status berisi label badge `Damaged` apa adanya tanpa warna
12. Verifikasi kolom Group berisi hierarki penuh dari root `Head Office {runId} > Floor 2 {runId} > Server Room {runId}` dan kolom Category berisi `Elektronik {runId} > Laptop {runId}`
13. Verifikasi kolom Brand berisi nama penuh `Lenovo {runId}` dan Model/Type `ThinkPad X1 {runId}` tanpa hierarki
14. Verifikasi kolom Labels berisi seluruh item `Prioritas {runId}, Aset Kantor {runId}, Aset Lantai Dua {runId}` tanpa dipotong menjadi +N more
15. Verifikasi kolom Modified By berisi nama lengkap utuh `Siti Nur Rahmawati {runId}`, bukan format tampilan nama depan dan inisial
16. Verifikasi kolom Purchase Cost berisi nilai numerik asli `12500000` tanpa simbol, kode mata uang, atau pemisah ribuan
17. Verifikasi kolom Days Damaged berisi nilai numerik tanpa kata `days`
18. Verifikasi kolom Last Holder yang kosong berisi `-`, bukan blank, `—`, atau `null`
19. Verifikasi kolom Reported Date memakai format tanggal `dd/MM/yy` diikuti jam format 24 jam
20. Total Control `Agus Pratama {runId}` mengunduh XLSX sub-tab Active dengan Search `ThinkPad - 301 {runId}` dengan kolom Purchase Cost ditampilkan
21. Verifikasi sel Purchase Cost di XLSX berupa sel angka, bukan teks
22. Total Control `Agus Pratama {runId}` mengunduh CSV sub-tab Active dengan Search `Laptop Lenovo ThinkPad {runId}`
23. Verifikasi `Laptop Lenovo ThinkPad - 302 {runId}` memakai hierarki penuh `Bandung Office {runId} > Floor 2 {runId}` sehingga leaf yang sama dengan Group lain tetap terbedakan

### Nilai badge status pada kedua sub-tab
24. Total Control `Agus Pratama {runId}` mengunduh CSV sub-tab Active dengan Search `{runId}` tanpa saringan lain
25. Verifikasi kolom Status memuat label `Waiting for Confirmation`, `Damaged`, `Reported Disposal`, dan `In Disposal Process` apa adanya
26. Total Control `Agus Pratama {runId}` mengunduh CSV sub-tab History dengan Search `{runId}` tanpa saringan lain
27. Verifikasi kolom Status memuat label `Repaired`, `Disposed`, `Rejected`, dan `Canceled` apa adanya
28. Verifikasi kolom Resolved By berisi `System` untuk `Drill Bosch GSB - 312 {runId}` dan kolom Duration berisi nilai numerik tanpa kata `days`

### Cakupan baris dan kolom mengikuti saringan, Setup Column, dan urutan aktif
29. Total Control `Agus Pratama {runId}` mengunduh CSV sub-tab Active dengan Filter Status `Reported Disposal` dan Search `Printer Canon Pixma {runId}`
30. Verifikasi berkas hanya memuat `Printer Canon Pixma - 303 {runId}` dan tidak memuat `Printer Canon Pixma - 304 {runId}`
31. Total Control `Agus Pratama {runId}` mengunduh CSV sub-tab Active dengan Search `Lenovo {runId}` setelah kolom Brand disembunyikan lewat Setup Column
32. Verifikasi kolom Brand yang disembunyikan tidak ikut di berkas
33. Total Control `Agus Pratama {runId}` mengunduh CSV sub-tab Active dengan Search `Lenovo {runId}` dan sort Name descending
34. Verifikasi urutan baris berkas mengikuti sort aktif: `Laptop Lenovo ThinkPad - 302 {runId}` mendahului `Laptop Lenovo ThinkPad - 301 {runId}`
35. Total Control `Agus Pratama {runId}` mengunduh CSV sub-tab Active dengan Search `tidak-ada {runId}` yang tidak cocok dengan record mana pun
36. Verifikasi berkas hanya berisi baris header kolom yang tampil tanpa baris data

### Encoding dan escaping CSV
37. Total Control `Agus Pratama {runId}` mengunduh CSV sub-tab Active dengan Search `Monitor, Curved Dell - 305 {runId}`
38. Verifikasi nilai Name `Monitor, Curved Dell - 305 {runId}` yang memuat koma dibungkus tanda kutip ganda
39. Total Control `Agus Pratama {runId}` mengunduh CSV sub-tab Active dengan Search `27 inci - 306 {runId}`
40. Verifikasi tanda kutip pada Name `Monitor "Curved" 27 inci - 306 {runId}` digandakan di dalam pembungkus tanda kutip ganda
41. Total Control `Agus Pratama {runId}` mengunduh CSV sub-tab Active dengan Search `Printer Epson L3150 - 307 {runId}` dan kolom Alias Name ditampilkan
42. Verifikasi Alias Name yang memuat baris baru dibungkus tanda kutip ganda dan baris baru tetap utuh dalam satu sel
43. Total Control `Agus Pratama {runId}` mengunduh CSV sub-tab Active dengan Search `Café Élan {runId}`
44. Verifikasi karakter `Café Élan {runId}` tersimpan benar dalam UTF-8 dengan BOM

### Ambang 5.000 baris: berkas selalu lengkap tanpa job latar dan tanpa notifikasi
45. Catat jumlah notifikasi in-app `Agus Pratama {runId}`
46. Total Control `Agus Pratama {runId}` mengunduh CSV sub-tab Active dengan Search `Aset Volume A {runId}` yang cocok tepat 5.000 baris
47. Verifikasi berkas memuat tepat 5.000 baris data
48. Total Control `Agus Pratama {runId}` mengunduh CSV sub-tab Active dengan Search `Aset Volume B {runId}` yang cocok 5.001 baris
49. Verifikasi berkas memuat seluruh 5.001 baris data dan langsung terunduh dalam satu permintaan tanpa job latar
50. Verifikasi jumlah notifikasi in-app `Agus Pratama {runId}` tidak bertambah karena Download tidak memakai notifikasi

### Hak Download dan kolom nilai finansial menurut hak
51. Pelapor umum `Budi Santoso {runId}` mengunduh CSV sub-tab Active
52. Verifikasi permintaan Download ditolak
53. Group Manager `Gunawan Hartono {runId}` mengunduh CSV sub-tab Active dengan Search `{runId}`
54. Verifikasi berkas hanya memuat record Group binaan beserta sub-group
55. Read Only `Rosa Maharani {runId}` mengunduh CSV sub-tab Active dengan Search `ThinkPad - 301 {runId}`
56. Verifikasi berkas diterima tanpa kolom Purchase Cost dan Asset Value karena tanpa hak lihat nilai finansial
