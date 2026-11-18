---
id: TC-FA-BORROW-BE-095-download-isi-berkas
title: "Isi berkas Download Borrow per tipe kolom, encoding, dan urutan baris"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
owner: BE
sourceRules: [EB-DL-4]
smoke: []
dependsOn: []
trace:
  EB-DL-4: [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 17]
anchor: []
---

# Isi berkas Download Borrow per tipe kolom, encoding, dan urutan baris

## Prerequisites
- Aktor:
  - Total Control `Hendra Wijaya {runId}`, cakupan seluruh client, pengaju DU-095-1 dan DU-095-2.
  - Borrower `Ezra Mahendra {runId}`, karyawan tanpa role Aktor Borrow, cakupan hanya My Asset, pemicu DU-095-3 lewat `Borrow an Asset`.
- Data:
  - Tab Transactions, tabel Borrow. Ketiga BRW diajukan berurutan dari DU-095-1 sampai DU-095-3, sehingga Request Date DU-095-1 paling lama dan DU-095-3 paling baru. Transaction ID dibentuk server dan menjadi milik tiap entri.
  - Ketiga Borrower adalah karyawan tanpa role Aktor Borrow, cakupan hanya My Asset. Setiap BRW berisi aset berstatus Ready sebanyak Total Asset-nya, dan tiap aset hanya ada di satu BRW.
  - DU-095-1: Borrower `Élan Kusuma {runId}`, Group `Head Office`, Status `Waiting for Handover`, Total Asset `2`, Source `Admin`, Requested By `Hendra Wijaya {runId}`.
  - DU-095-2: Borrower `Bambang Prakoso {runId}`, Group `Head Office`, Status `Waiting for Approval`, Total Asset `10`, Source `Admin`, Requested By `Hendra Wijaya {runId}`.
  - DU-095-3: Borrower `Ezra Mahendra {runId}`, Group `Head Office`, Status `Waiting for Handover`, Total Asset `1`, Source `Self-service`, Requested By `—`.
- Kondisi:
  - Aset DU-095-2 memakai aturan approval yang belum diputuskan; aset DU-095-1 dan DU-095-3 tanpa approval.
  - Kolom Source tersembunyi seperti pengaturan awal tabel; kolom lain tampil.

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
