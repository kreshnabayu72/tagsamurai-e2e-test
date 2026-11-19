---
id: TC-FA-BORROW-BE-095-download-isi-berkas
title: "Isi berkas Download Borrow per tipe kolom, encoding, dan urutan baris"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: [EB-DL-4]
smoke: []
dependsOn: []
trace:
  EB-DL-4: [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 17, 19, 20, 21, 22, 24, 25, 26, 28, 29]
anchor: []
---

# Isi berkas Download Borrow per tipe kolom, encoding, dan urutan baris

## Prerequisites
- Aktor:
  - Total Control `Hendra Wijaya {runId}`, cakupan seluruh client, pengaju DU-095-1, DU-095-2, DU-095-4, dan DU-095-6 sampai DU-095-8.
  - Borrower `Ezra Mahendra {runId}`, karyawan tanpa role Aktor Borrow, cakupan hanya My Asset, pemicu DU-095-3 lewat `Borrow an Asset`.
- Data:
  - Tab Transactions, tabel Borrow. Ketiga BRW diajukan berurutan dari DU-095-1 sampai DU-095-3, sehingga Request Date DU-095-1 paling lama dan DU-095-3 paling baru. Transaction ID dibentuk server dan menjadi milik tiap entri.
  - Ketiga Borrower adalah karyawan tanpa role Aktor Borrow, cakupan hanya My Asset. Setiap BRW berisi aset berstatus Ready sebanyak Total Asset-nya, dan tiap aset hanya ada di satu BRW.
  - DU-095-1: Borrower `Élan Kusuma {runId}`, Group `Head Office`, Status `Waiting for Handover`, Total Asset `2`, Source `Admin`, Requested By `Hendra Wijaya {runId}`.
  - DU-095-2: Borrower `Bambang Prakoso {runId}`, Group `Head Office`, Status `Waiting for Approval`, Total Asset `10`, Source `Admin`, Requested By `Hendra Wijaya {runId}`.
  - DU-095-3: Borrower `Ezra Mahendra {runId}`, Group `Head Office`, Status `Waiting for Handover`, Total Asset `1`, Source `Self-service`, Requested By `—`.
  - DU-095-5: Group `Gudang Pusat {runId}`, anak langsung dari Group `Head Office`, sehingga hierarki penuhnya dari root adalah `Head Office > Gudang Pusat {runId}`.
  - DU-095-6: Group `Gudang Timur {runId}`, anak langsung dari Group `Head Office`, sehingga hierarki penuhnya dari root adalah `Head Office > Gudang Timur {runId}`.
  - DU-095-7: Group `Gudang Barat {runId}`, anak langsung dari Group `Head Office`, sehingga hierarki penuhnya dari root adalah `Head Office > Gudang Barat {runId}`.
  - DU-095-4: Borrower `Anggoro Pratama {runId}`, karyawan di Group `Gudang Pusat {runId}` tanpa role Aktor Borrow dan cakupan hanya My Asset, Group aset `Gudang Pusat {runId}` (DU-095-5), Status `Borrowed` dengan penanda `Overdue`, Total Asset `1`, Source `Admin`, Requested By `Hendra Wijaya {runId}`. BRW ini diajukan sesudah DU-095-3 dan sudah di-Hand Over.
  - DU-095-8: Borrower `Kartika Dewi {runId}`, karyawan di Group `Head Office` tanpa role Aktor Borrow dan cakupan hanya My Asset, Group aset `Gudang Pusat {runId}` (DU-095-5), aset ber-TAG `RFID` dengan foto utama, Status `Borrowed`, Total Asset `1`, Source `Admin`, Requested By `Hendra Wijaya {runId}`. BRW ini diajukan sesudah DU-095-4 dan sudah di-Hand Over.
  - DU-095-9: Borrower `Kartika Dewi {runId}`, Group aset `Gudang Timur {runId}` (DU-095-6), aset Category `Non TAG`, Status `Borrowed`, Total Asset `1`, Source `Admin`, Requested By `Hendra Wijaya {runId}`. BRW ini diajukan sesudah DU-095-8 dan sudah di-Hand Over.
  - DU-095-10: Borrower `Kartika Dewi {runId}`, Group aset `Gudang Barat {runId}` (DU-095-7), aset Category `Non TAG`, Status `Borrowed`, Total Asset `1`, Source `Admin`, Requested By `Hendra Wijaya {runId}`. BRW ini diajukan sesudah DU-095-9 dan sudah di-Hand Over.
- Kondisi:
  - Aset DU-095-2 memakai aturan approval `Needs approval`, sehingga BRW-nya berstatus `Waiting for Approval` saat diajukan; aset DU-095-1, DU-095-3, dan DU-095-4 tanpa approval.
  - Baris aset DU-095-4 berstatus `Overdue` saat Download diminta, karena Due date baris itu sudah lewat.
  - Date Format dan Time Format di General Settings entitas berlaku untuk Request Date dan Last Updated.
  - Pada tabel Transactions, kolom Source tersembunyi seperti pengaturan awal tabel; kolom lain tampil.
  - Pada tabel Borrowed Assets By Asset, kolom TAG ditampilkan bagi Total Control sebagai tambahan atas kolom tampil awal.
  - Allowed borrower aset DU-095-8 sampai DU-095-10 terpenuhi Borrower `Kartika Dewi {runId}`.

## Test Steps

### Isi berkas CSV mengikuti tipe kolom, encoding, dan Sort aktif
1. Total Control meminta Download as CSV dari tab Transactions dengan Filter Borrower `Élan Kusuma {runId}`, `Bambang Prakoso {runId}`, dan `Ezra Mahendra {runId}`, dengan Sort Request Date `Oldest First`
2. Verifikasi nama berkas `Borrow-Transactions.csv`
3. Verifikasi berkas CSV berenkode UTF-8 dengan BOM
4. Verifikasi baris header berisi kolom yang tampil: `Transaction ID`, `Status`, `Group`, `Borrower`, `Total Asset`, `Requested By`, `Request Date`, dan `Last Updated`
5. Verifikasi kolom `Source` tidak ikut di berkas, karena tersembunyi saat Download diminta
6. Verifikasi sel Borrower baris pertama berisi nama lengkap utuh `Élan Kusuma {runId}`, bukan format tampilan singkat
7. Verifikasi sel Total Asset baris Borrower `Bambang Prakoso {runId}` bernilai `10`, tanpa format tampilan
8. Verifikasi sel Status baris Borrower `Bambang Prakoso {runId}` bernilai `Waiting for Approval`, label badge apa adanya
9. Verifikasi sel Requested By baris Borrower `Ezra Mahendra {runId}` bernilai `-`, bukan kosong, bukan `—`, dan bukan `null`
10. Verifikasi urutan baris menurut Borrower adalah `Élan Kusuma {runId}`, `Bambang Prakoso {runId}`, lalu `Ezra Mahendra {runId}`, mengikuti Sort Request Date `Oldest First`

### Isi berkas XLSX mengikuti sheet, tipe sel, dan Sort aktif
11. Total Control meminta Download as XLSX dari tab Transactions dengan Filter Borrower `Élan Kusuma {runId}`, `Bambang Prakoso {runId}`, dan `Ezra Mahendra {runId}`, dengan Sort Request Date `Newest First`
12. Verifikasi nama berkas `Borrow-Transactions.xlsx`
13. Verifikasi berkas memuat satu sheet bernama `Sheet1`
14. Verifikasi sel Total Asset baris Borrower `Bambang Prakoso {runId}` bernilai `10` dan tersimpan sebagai sel angka, bukan teks
15. Verifikasi urutan baris menurut Borrower adalah `Ezra Mahendra {runId}`, `Bambang Prakoso {runId}`, lalu `Élan Kusuma {runId}`, mengikuti Sort Request Date `Newest First`

### Hasil nol baris menghasilkan berkas berisi header saja
16. Total Control meminta Download as CSV dari tab Transactions dengan Search `zzqxv` dan Filter Borrower `Élan Kusuma {runId}`, `Bambang Prakoso {runId}`, dan `Ezra Mahendra {runId}`
17. Verifikasi permintaan Download tetap dilayani dan berkas CSV hanya berisi baris header kolom yang tampil, tanpa baris data

### Isi berkas CSV untuk Status multi-badge, Group berhierarki, dan format tanggal
18. Total Control meminta Download as CSV dari tab Transactions dengan Filter Borrower `Anggoro Pratama {runId}`
19. Verifikasi sel Status baris Borrower `Anggoro Pratama {runId}` bernilai `Borrowed, Overdue`, kedua badge ditulis labelnya apa adanya dan dipisah koma serta spasi
20. Verifikasi sel Group baris Borrower `Anggoro Pratama {runId}` berisi hierarki penuh dari root `Head Office > Gudang Pusat {runId}`, bukan hanya nama leaf
21. Verifikasi sel Request Date baris Borrower `Anggoro Pratama {runId}` berisi waktu Submit BRW itu menurut Date Format dan Time Format General Settings
22. Verifikasi sel Last Updated baris Borrower `Anggoro Pratama {runId}` berisi waktu ubah terakhir BRW itu menurut Date Format dan Time Format General Settings

### Isi berkas CSV Borrowed Assets By Asset: ikon ditulis label aksesibilitasnya dan foto tidak ikut
23. Total Control meminta Download as CSV dari tab Borrowed Assets tampilan By Asset dengan Filter Borrower `Kartika Dewi {runId}`
24. Verifikasi nama berkas `Borrowed-Assets.csv`
25. Verifikasi sel TAG baris dengan Transaction ID milik DU-095-8 bernilai `RFID`, label aksesibilitas ikon apa adanya dan bukan nama komponen ikon
26. Verifikasi foto aset milik DU-095-8 tidak ikut di berkas

### Isi berkas CSV Borrowed Assets By Borrower: chip +N more ditulis semua itemnya
27. Total Control meminta Download as CSV dari tab Borrowed Assets tampilan By Borrower dengan Filter Borrower `Kartika Dewi {runId}`
28. Verifikasi nama berkas `Borrowed-Borrowers.csv`
29. Verifikasi sel Group baris Borrower `Kartika Dewi {runId}` memuat ketiga hierarki penuh `Head Office > Gudang Pusat {runId}`, `Head Office > Gudang Timur {runId}`, dan `Head Office > Gudang Barat {runId}`, dipisah koma serta spasi, tidak diringkas menjadi dua Group dan chip `+N more`
