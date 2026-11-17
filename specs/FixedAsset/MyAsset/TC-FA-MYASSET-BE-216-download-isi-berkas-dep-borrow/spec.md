---
id: TC-FA-MYASSET-BE-216-download-isi-berkas-dep-borrow
title: "Isi berkas Download My Asset per tipe kolom"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§5#r6", "EB-DL-4", "EB-DL-5"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow", "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"]
owner: BE
trace:
  "§5#r6": [2, 13, 23, 28, 30, 40]
  "EB-DL-4": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 19, 20, 21, 25, 30, 32, 33, 35, 36, 38, 39]
  "EB-DL-5": [40, 41]
---

# Isi berkas Download My Asset per tipe kolom

## Prerequisites
- Aktor: Borrower dan Assignee, yaitu pengguna ber-akun login `Rina Wulandari {runId}` (DU-216-1) yang membuka My Asset dan tidak punya baris lain selain DU-216-2 sampai DU-216-12. Aktor Borrow dan Aktor Assignment menyerahkan aset ke Aktor, masing-masing dengan hak atas Group aset yang diserahkannya; Aktor Borrow `Budi Santoso {runId}` dan `Citra Dewi {runId}`, Aktor Assignment `Siti Nur Rahmawati {runId}`. Division `Divisi Keuangan {runId}` memakai Aktor sebagai PIC.
- Data:
  - DU-216-1: Aktor pemegang semua baris di bawah, tanpa baris lain di My Asset: Name `Rina Wulandari {runId}`, Posisi `Borrower dan Assignee`.
  - DU-216-2: pinjaman Admin Borrowed dengan marker Damaged dan laporan Missing, Group tiga tingkat, Purpose berkoma: Name `Laptop Operasional {runId}`, Photo `foto utama aset`, Asset ID `LPT-0101 {runId}`, Brand `Dell`, Model/Type `Latitude 5440`, Group `Kantor Jakarta > Lantai 2 > Ruang Server`, Status `Borrowed · Damaged · Reported Missing`, TAG `RFID`, Category `Elektronik > Komputer`, Source `Admin`, Handed Over At `T0`, Purpose `Rapat, presentasi, dan demo`, Status (berkas) `Borrowed, Damaged, Reported Missing`, TAG (berkas) `RFID`, Group (berkas) `Kantor Jakarta > Lantai 2 > Ruang Server`, Category (berkas) `Elektronik > Komputer`, Brand (berkas) `Dell`, Model/Type (berkas) `Latitude 5440`, Source (berkas) `Admin`, Purpose (berkas CSV) `"Rapat, presentasi, dan demo"`, Purpose (berkas XLSX) `Rapat, presentasi, dan demo`.
  - DU-216-3: pinjaman self-service Waiting for Approval tanpa Brand, Model, TAG, dan handover, Purpose bertanda kutip: Name `Proyektor Rapat {runId}`, Photo `foto utama aset`, Asset ID `PRJ-0202 {runId}`, Brand `—`, Model/Type `—`, Group `Kantor Jakarta > Lantai 2`, Status `Waiting for Approval`, TAG `—`, Category `Elektronik`, Source `Self-service`, Handed Over At `—`, Purpose `Kebutuhan "urgent" klien`, Brand (berkas) `-`, TAG (berkas) `-`, Handed Over At (berkas) `-`, Group (berkas) `Kantor Jakarta > Lantai 2`, Source (berkas) `Self-service`, Purpose (berkas CSV) `"Kebutuhan ""urgent"" klien"`, Purpose (berkas XLSX) `Kebutuhan "urgent" klien`.
  - DU-216-4: pinjaman self-service Borrowed pada Group dengan leaf yang sama dengan DU-216-3 tetapi parent berbeda, Purpose non-ASCII: Name `Kamera Dokumentasi {runId}`, Photo `foto utama aset`, Asset ID `CAM-0303 {runId}`, Brand `Canon`, Model/Type `EOS R50`, Group `Kantor Bandung > Lantai 2`, Status `Borrowed`, TAG `NFC`, Category `Fotografi`, Source `Self-service`, Handed Over At `T0`, Purpose `Pameran Café Élan`, Group (berkas) `Kantor Bandung > Lantai 2`, Purpose (berkas) `Pameran Café Élan`.
  - DU-216-5: pinjaman Admin Borrowed dengan Purpose dua baris: Name `Kabel Roll {runId}`, Photo `foto utama aset`, Asset ID `CBL-0404 {runId}`, Brand `Belden`, Model/Type `Cat6`, Group `Kantor Jakarta > Lantai 1`, Status `Borrowed`, TAG `BLE`, Category `Jaringan`, Source `Admin`, Handed Over At `T0`, Purpose `Tahap satu⏎Tahap dua`, Purpose (berkas CSV) `"Tahap satu⏎Tahap dua"`.
  - DU-216-6: pinjaman Returned dengan marker Damaged milik Aktor: Name `Mikrofon Studio {runId}`, Asset ID `MIC-0301 {runId}`, Brand `Shure`, Model/Type `SM58`, Group `Kantor Jakarta > Lantai 1`, Status `Returned · Damaged`, Holder `Me`, TAG `RFID`, Category `Audio`, Type `Borrow`, Handed Over At `T0`, Closed At `T0`, Purpose `Rekaman siaran internal`, Status (berkas) `Returned, Damaged`, Type (berkas) `Borrow`.
  - DU-216-7: penugasan Unassigned atas nama Division yang PIC-nya Aktor: Name `Monitor Kerja {runId}`, Asset ID `MON-0302 {runId}`, Brand `Samsung`, Model/Type `S24C`, Group `Kantor Jakarta > Lantai 1`, Status `Unassigned`, Holder `Divisi Keuangan {runId}`, TAG `NFC`, Category `Peripheral`, Type `Assignment`, Handed Over At `T0`, Closed At `T0`, Purpose `Penggunaan harian tim keuangan`, Type (berkas) `Assignment`.
  - DU-216-8: lima ribu satu pinjaman Returned milik Aktor, di atas ambang 5.000 baris: Name `Selang Udara {n} {runId}`, Asset ID `SLG-{n} {runId}`, Brand `Gates`, Model/Type `AX10`, Group `Kantor Jakarta > Lantai 1`, Status `Returned`, Holder `Me`, TAG `RFID`, Category `Peralatan`, Type `Borrow`, Handed Over At `T0`, Closed At `T0`, Purpose `Pengujian volume berkas`.
  - DU-216-9: penugasan Assigned oleh Aktor Assignment dengan last name dua kata: Name `Notebook Staf {runId}`, Photo `foto utama aset`, Asset ID `NBK-0201 {runId}`, Brand `Lenovo`, Model/Type `T14`, Group `Kantor Jakarta > Lantai 2`, Status `Assigned`, Assigned To `Me`, TAG `RFID`, Category `Elektronik > Komputer`, Assigned Date `T0`, Assigned By `Siti Nur Rahmawati {runId}`, Assigned By (berkas) `Siti Nur Rahmawati {runId}`.
  - DU-216-10: penugasan Waiting for Handover yang belum diserahkan: Name `Meja Rapat Besar {runId}`, Photo `foto utama aset`, Asset ID `FRN-0202 {runId}`, Brand `Informa`, Model/Type `Oval 200`, Group `Kantor Jakarta > Lantai 2`, Status `Waiting for Handover`, Assigned To `Divisi Keuangan {runId}`, TAG `NFC`, Category `Furnitur`, Assigned Date `—`, Assigned By `—`, Assigned Date (berkas) `-`, Assigned By (berkas) `-`.
  - DU-216-11: Task Confirm Handover pinjaman dengan Total Asset dua digit: Transaction ID `nomor BRW milik DU-216-11`, Task `Confirm Handover`, Group `Kantor Jakarta > Lantai 2`, Total Asset `12`, Handed Over By `Budi Santoso {runId}`, Expires At `T0 + 1 hari`, Handed Over By (berkas) `Budi Santoso {runId}`.
  - DU-216-12: Task Confirm Handover pinjaman dengan Total Asset satu digit: Transaction ID `nomor BRW milik DU-216-12`, Task `Confirm Handover`, Group `Kantor Bandung > Lantai 2`, Total Asset `3`, Handed Over By `Citra Dewi {runId}`, Expires At `T0 + 1 hari`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`
  - T0 adalah tanggal run
  - Kolom `TAG`, `Category`, dan `Purpose` tampil pada tabel yang diunduh
  - Tab History Aktor berisi 5003 baris dan tab lain hanya berisi baris di atas

## Test Steps

### Isi berkas CSV tab Borrowed menurut tipe kolom
1. Aktor mengunduh berkas CSV tab Borrowed tanpa Search dan Filter
2. Verifikasi berkas berupa CSV dengan pemisah koma dan encoding UTF-8 dengan BOM
3. Verifikasi baris header berkas tidak memuat kolom `Photo`, sehingga foto aset tidak ikut diekspor
4. Verifikasi sel `TAG` baris DU-216-2 berisi label ikon `RFID`, bukan nama komponen ikon
5. Verifikasi sel `Source` baris DU-216-2 berisi `Admin` dan baris DU-216-3 berisi `Self-service`, yaitu label badge apa adanya
6. Verifikasi sel `Status` baris DU-216-2 berisi seluruh label badge terpisah koma dan spasi, yaitu `Borrowed, Damaged, Reported Missing`
7. Verifikasi sel `Group` baris DU-216-2 berisi hierarki penuh dari root `Kantor Jakarta > Lantai 2 > Ruang Server`
8. Verifikasi sel `Category` baris DU-216-2 berisi hierarki penuh dari root `Elektronik > Komputer`
9. Verifikasi sel `Group` baris DU-216-3 berisi `Kantor Jakarta > Lantai 2` dan baris DU-216-4 berisi `Kantor Bandung > Lantai 2`, sehingga Group yang leaf-nya sama tetap dapat dibedakan lewat parent-nya
10. Verifikasi sel `Brand` dan `Model/Type` baris DU-216-2 berisi `Dell` dan `Latitude 5440` tanpa hierarki
11. Verifikasi sel `Brand` baris DU-216-3 yang kosong dan sel `TAG` baris DU-216-3 yang kosong masing-masing berisi `-`, bukan sel kosong, bukan `—`, dan bukan teks `null`
12. Verifikasi sel `Handed Over At` baris DU-216-3 yang belum diserahkan berisi `-`
13. Verifikasi nilai tanggal dan jam pada kolom `Handed Over At` baris DU-216-2 ditulis menurut Date Format dan Time Format di Kondisi
14. Verifikasi sel `Purpose` baris DU-216-2 yang mengandung koma dibungkus tanda kutip ganda, yaitu `"Rapat, presentasi, dan demo"`
15. Verifikasi sel `Purpose` baris DU-216-3 yang mengandung tanda kutip ditulis `"Kebutuhan ""urgent"" klien"`, dengan tanda kutip di dalamnya digandakan
16. Verifikasi sel `Purpose` baris DU-216-5 yang mengandung baris baru dibungkus tanda kutip ganda dan tetap menjadi satu sel
17. Verifikasi sel `Purpose` baris DU-216-4 terbaca sebagai `Pameran Café Élan` ketika berkas dibaca sebagai UTF-8

### Isi berkas XLSX tab Borrowed
18. Aktor mengunduh berkas XLSX tab Borrowed tanpa Search dan Filter
19. Verifikasi berkas XLSX hanya memuat satu sheet bernama `Sheet1`
20. Verifikasi sel `Purpose` baris DU-216-3 berisi `Kebutuhan "urgent" klien` tanpa pembungkus kutip tambahan, dan sel `Status` baris DU-216-2 berisi `Borrowed, Damaged, Reported Missing`
21. Verifikasi header berkas XLSX tidak memuat kolom `Photo`

### Cakupan baris, kolom, dan urutan berkas mengikuti keadaan tabel saat Download
22. Aktor mengunduh berkas CSV tab Borrowed dengan Search `Dokumentasi`
23. Verifikasi berkas memuat baris DU-216-4 dan tidak memuat baris DU-216-2, DU-216-3, maupun DU-216-5, karena isi berkas mengikuti hasil Search
24. Aktor mengunduh berkas CSV tab Borrowed diurutkan naik menurut kolom `Name`
25. Verifikasi baris berkas tampil berurutan menurut sort aktif: DU-216-5, DU-216-4, DU-216-2, DU-216-3
26. Kolom `Purpose` disembunyikan pada tabel Borrowed
27. Aktor mengunduh berkas CSV tab Borrowed tanpa Search dan Filter
28. Verifikasi baris header berkas tidak memuat kolom `Purpose` yang sedang disembunyikan, sedangkan kolom `Source` yang tampil tetap ada
29. Aktor mengunduh berkas CSV tab Borrowed dengan Search `zzz tidak ada`
30. Verifikasi berkas tetap dihasilkan dan hanya berisi baris header kolom yang tampil tanpa baris data

### Isi berkas tab Assigned dan tab Task
31. Aktor mengunduh berkas CSV tab Assigned tanpa Search dan Filter
32. Verifikasi sel `Assigned By` baris DU-216-9 berisi nama lengkap utuh `Siti Nur Rahmawati {runId}`, bukan format tampilan nama depan dan inisial
33. Verifikasi sel `Assigned By` dan `Assigned Date` baris DU-216-10 yang belum diserahkan masing-masing berisi `-`
34. Aktor mengunduh berkas XLSX tab Task tanpa Search dan Filter
35. Verifikasi sel `Total Asset` baris DU-216-11 berisi angka `12` sebagai sel angka, bukan teks
36. Verifikasi sel `Handed Over By` baris DU-216-11 berisi nama lengkap utuh `Budi Santoso {runId}`

### Isi berkas tab History dan berkas di atas ambang 5.000 baris
37. Aktor mengunduh berkas CSV tab History tanpa Search dan Filter
38. Verifikasi sel `Type` baris DU-216-6 berisi `Borrow` dan baris DU-216-7 berisi `Assignment`, yaitu label badge apa adanya
39. Verifikasi sel `Status` baris DU-216-6 berisi dua label badge terpisah koma dan spasi, yaitu `Returned, Damaged`
40. Verifikasi berkas memuat seluruh 5003 baris data tab History, yaitu 5001 baris DU-216-8 ditambah DU-216-6 dan DU-216-7, dan bukan hanya satu halaman
41. Verifikasi berkas lengkap itu langsung diterima sebagai hasil permintaan unduh yang sama tanpa menunggu job background
