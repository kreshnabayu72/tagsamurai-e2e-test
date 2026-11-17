---
id: TC-FA-MYASSET-E2E-032-tab-borrowed-sort-dep-borrow
title: "Sort tab Borrowed: urutan default Due Date terdekat, baris tanpa Due Date, dan kembali ke default"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1b#p7", "§5#r4", "EB-SRT-1", "EB-SRT-3@tabel-borrowed"]
smoke: ["EB-SRT-1", "EB-SRT-3@tabel-borrowed"]
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§4.1b#p7": [2, 3]
  "§5#r4": [2, 13]
  "EB-SRT-1": [5, 7]
  "EB-SRT-3@tabel-borrowed": [9, 11, 13]
anchor: [1]
coverage:
  web: automated
---

# Sort tab Borrowed: urutan default Due Date terdekat, baris tanpa Due Date, dan kembali ke default

## Prerequisites
- Aktor: Borrower `Dian Pratama {runId}`, pengguna karyawan ber-akun login tanpa role admin.
- Layar awal: halaman My Asset, tab `Borrowed`.
- Data:
  - DU-032-1: User `Dian Pratama {runId}`, tanpa role admin, cakupan Group `Head Office`.
  - DU-032-2: pinjaman Admin atas nama `Dian Pratama {runId}`, aset `Kamera Canon EOS 90D {runId}`, Group `Head Office`, Status `Overdue`, Duration `3 days`, Handed Over At `T0 − 5 hari`, Due Date `T0 − 2 hari`.
  - DU-032-3: pinjaman Admin atas nama `Dian Pratama {runId}`, aset `Tripod Manfrotto {runId}`, Group `Head Office`, Status `Borrowed`, Duration `1 day`, Handed Over At `T0`, Due Date `T0 + 1 hari`.
  - DU-032-4: pinjaman Admin atas nama `Dian Pratama {runId}`, aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, Status `Borrowed`, Duration `5 days`, Handed Over At `T0 − 2 hari`, Due Date `T0 + 3 hari`.
  - DU-032-5: pinjaman Admin atas nama `Dian Pratama {runId}`, aset `Proyektor Epson EB-X06 {runId}`, Group `Head Office`, Status `Waiting for Handover`, Duration `2 days`, Due Date `—`.
  - DU-032-6: pinjaman Admin atas nama `Dian Pratama {runId}`, aset `Monitor Dell 24 inci {runId}`, Group `Head Office`, Status `Waiting for Approval`, Duration `4 days`, Due Date `—`.
- Kondisi:
  - Tab Borrowed `Dian Pratama {runId}` hanya berisi 5 baris aset, dari DU-032-2 sampai DU-032-6, pada satu halaman.
  - Tidak ada Sort aktif pada tabel Borrowed.

## Test Steps

### Urutan default Due Date terdekat dan baris tanpa Due Date di akhir
1. Verifikasi tabel Borrowed memuat 5 baris
2. Verifikasi tiga baris ber-Due Date tampil dari atas ke bawah `Kamera Canon EOS 90D {runId}`, `Tripod Manfrotto {runId}`, lalu `Laptop Dell Latitude 5420 {runId}`
3. Verifikasi baris `Proyektor Epson EB-X06 {runId}` dan `Monitor Dell 24 inci {runId}` yang Due Date-nya `—` tampil sesudah ketiga baris ber-Due Date

### Sort kolom Due Date: Oldest First lalu Newest First
4. Klik header kolom Due Date
5. Verifikasi urutan Oldest First: `Kamera Canon EOS 90D {runId}`, `Tripod Manfrotto {runId}`, `Laptop Dell Latitude 5420 {runId}`, lalu dua baris tanpa Due Date di akhir
6. Klik header kolom Due Date
7. Verifikasi urutan Newest First: dua baris tanpa Due Date di awal, lalu `Laptop Dell Latitude 5420 {runId}`, `Tripod Manfrotto {runId}`, dan `Kamera Canon EOS 90D {runId}`

### Siklus tiga klik pada kolom Duration kembali ke urutan default
8. Klik header kolom Duration
9. Verifikasi urutan Shortest First: `Tripod Manfrotto {runId}`, `Proyektor Epson EB-X06 {runId}`, `Kamera Canon EOS 90D {runId}`, `Monitor Dell 24 inci {runId}`, lalu `Laptop Dell Latitude 5420 {runId}`
10. Klik header kolom Duration
11. Verifikasi urutan Longest First: `Laptop Dell Latitude 5420 {runId}`, `Monitor Dell 24 inci {runId}`, `Kamera Canon EOS 90D {runId}`, `Proyektor Epson EB-X06 {runId}`, lalu `Tripod Manfrotto {runId}`
12. Klik header kolom Duration
13. Verifikasi urutan kembali ke default Due Date terdekat: `Kamera Canon EOS 90D {runId}`, `Tripod Manfrotto {runId}`, `Laptop Dell Latitude 5420 {runId}`, lalu dua baris tanpa Due Date
