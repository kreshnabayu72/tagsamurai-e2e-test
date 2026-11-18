---
id: TC-FA-ASSIGN-BE-225-isi-berkas-download
title: "Isi berkas CSV dan XLSX hasil Download"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["EB-DL-4"]
smoke: []
dependsOn: []
owner: BE
trace:
  "EB-DL-4": [4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 17, 20, 23, 24, 25, 28]
---

# Isi berkas CSV dan XLSX hasil Download

## Prerequisites
- Aktor: Aktor Assignment `Rina Wijaya {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); Assignee Employee dan PIC ber-akun login seperti di entri data.
- Data:
  - DU-225-1: User, Aktor Assignment yang mengunduh: Nama `Rina Wijaya {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-225-2: Assignment, ASG Employee di Group bersarang dengan satu aset: Assignee `Anggi Maharani {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId} > Lantai 2 {runId}`, Baris 1 `Printer Epson L3250 {runId}`, Status `Waiting for Handover`, Total Asset `1`, Requested By `Rina Wijaya {runId}`.
  - DU-225-3: Assignment, ASG Employee dengan nama Assignee mengandung koma dan tiga aset: Assignee `Hartono, Rudi {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Kursi Lipat A {runId}`, Baris 2 `Kursi Lipat B {runId}`, Baris 3 `Kursi Lipat C {runId}`, Status `Waiting for Approval`, Total Asset `3`, Requested By `Rina Wijaya {runId}`.
  - DU-225-4: Assignment, ASG Division tanpa PIC aktif dengan dua aset: Assignee `Keuangan {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Baris 1 `Brankas Krisbow {runId}`, Baris 2 `Lemari Besi Alba {runId}`, Status `Waiting for Handover`, Penanda `No PIC`, Total Asset `2`, Requested By `Rina Wijaya {runId}`.
  - DU-225-6: Assignment, ASG Employee dengan dua baris Assigned, satu tanpa Brand dan Assignee bertanda kutip ganda: Assignee `Wawan "Kiki" Setiawan {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Router Mikrotik Wawan {runId}`, Baris 2 `Kabel Roll Wawan {runId}`, Status baris `Assigned`, Brand baris 1 `Mikrotik`, Brand baris 2 `—`.
  - DU-225-7: Draft, Draft multi-Group untuk kolom Group dengan banyak item: Assignee `Dina Pratiwi {runId}`, Tipe Assignee `Employee`, Pembuat `Rina Wijaya {runId}`, Aset 1 `Rak Arsip Besi {runId}`, Group aset 1 `Head Office {runId} > Lantai 2 {runId}`, Aset 2 `Kursi Tamu Informa {runId}`, Group aset 2 `Branch Surabaya {runId}`. Group di berkas CSV yang diharapkan `Branch Surabaya {runId}, Head Office {runId} > Lantai 2 {runId}`, dari Group aset 1 dan Group aset 2 yang diurutkan A-Z.
- Kondisi:
  - Tab Transactions memakai Setup Column bawaan dan format tanggal serta jam mengikuti General Settings entitas.
  - Nama berkas tabel Transactions adalah `Assignment-Transactions` tanpa ekstensi.

## Test Steps

### Isi berkas CSV mengikuti Search dan Sort aktif
1. Ketik Search `{runId}`, tekan Enter
2. Rina mengurutkan kolom Total Asset Descending
3. Rina memilih `Download as CSV` pada tabel Transactions
4. Verifikasi berkas CSV bernama `Assignment-Transactions` berisi hanya ASG milik spec ini dan baris berurutan menurut Total Asset Descending dari `3`, `2`, lalu `1`
5. Verifikasi CSV memakai pemisah koma dan encoding UTF-8 dengan BOM
6. Verifikasi nilai Assignee `Hartono, Rudi {runId}` yang mengandung koma dibungkus tanda kutip ganda di CSV
7. Verifikasi kolom Group untuk ASG `Anggi Maharani {runId}` ditulis hierarki penuh `Head Office {runId} > Lantai 2 {runId}`
8. Verifikasi kolom Total Asset ditulis sebagai angka asli `3`, `2`, dan `1`, bukan teks terformat
9. Verifikasi kolom Status ASG `Keuangan {runId}` memuat label `Waiting for Handover` dan `No PIC` yang dipisah koma dan spasi
10. Verifikasi kolom Assignee dan Requested By ditulis dengan nama lengkap utuh dan kolom tanggal mengikuti format General Settings
11. Verifikasi berkas tidak memuat foto dan warna badge

### Isi berkas XLSX
12. Rina memilih `Download as XLSX` pada tabel Transactions
13. Verifikasi berkas XLSX hanya memuat satu sheet bernama `Sheet1` dan urutan barisnya sama dengan Sort aktif
14. Verifikasi kolom Total Asset di XLSX ditulis sebagai sel angka, bukan teks

### Kolom yang disembunyikan dan hasil nol baris
15. Rina menyembunyikan kolom Last Updated lewat Setup Column
16. Rina memilih `Download as CSV` pada tabel Transactions
17. Verifikasi berkas CSV tidak memuat kolom Last Updated karena cakupan kolom mengikuti kolom yang tampil
18. Ketik Search `zzz tanpa kecocokan {runId}`, tekan Enter
19. Rina memilih `Download as CSV` pada tabel Transactions saat hasil Search kosong
20. Verifikasi berkas CSV berisi hanya baris header kolom yang tampil dan tidak ada toast

### Isi berkas tabel Assigned Assets By Asset per tipe kolom
21. Ketik Search `{runId}` pada tab Assigned Assets By Asset, tekan Enter
22. Rina mengunduh tabel Assigned Assets By Asset dengan pilihan `Download as CSV`
23. Verifikasi berkas CSV tidak memuat foto aset
24. Verifikasi Brand yang kosong pada baris `Kabel Roll Wawan {runId}` ditulis `-` dan bukan `—`
25. Verifikasi nilai Assignee `Wawan "Kiki" Setiawan {runId}` yang mengandung tanda kutip ganda ditulis dengan tanda kutip ganda digandakan di dalam pembungkus tanda kutip ganda

### Isi berkas kolom Group multi-Group pada tabel Drafts
26. Ketik Search `Dina Pratiwi {runId}` pada tab Drafts, tekan Enter
27. Rina mengunduh tabel Drafts dengan pilihan `Download as CSV`
28. Verifikasi kolom Group untuk Draft `Dina Pratiwi {runId}` pada berkas CSV ditulis `Branch Surabaya {runId}, Head Office {runId} > Lantai 2 {runId}`: semua item ditulis penuh, tiap item dengan hierarki penuh dari root dan dipisah `, `
