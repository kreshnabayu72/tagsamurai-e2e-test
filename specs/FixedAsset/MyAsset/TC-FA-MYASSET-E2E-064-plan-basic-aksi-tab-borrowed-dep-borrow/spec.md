---
id: TC-FA-MYASSET-E2E-064-plan-basic-aksi-tab-borrowed-dep-borrow
title: "Plan Basic: Request Extension tidak tampil di tab Borrowed, Return hanya pada baris self-service berjalan, pinjaman berjalan tetap berjalan"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§4.3#r7", "§9.10#p1", "§9.4.2#r84", "§9.4.2#r85", "§9.4.2#r86"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§4.3#r7": [7, 12, 16]
  "§9.10#p1": [7, 8, 11, 12, 16]
  "§9.4.2#r84": [7, 12, 16]
  "§9.4.2#r85": [8, 11]
  "§9.4.2#r86": [3, 4, 23, 24]
anchor: [6, 15]
coverage:
  web: automated
---

# Plan Basic: Request Extension tidak tampil di tab Borrowed, Return hanya pada baris self-service berjalan, pinjaman berjalan tetap berjalan

## Prerequisites
- Aktor: Borrower `Nadia Pratiwi {runId}` (DU-064-2). Aktor lain yang memicu perubahan: Aktor Borrow `Gita Permata {runId}` (DU-064-5), yang melakukan Extend dari web.
- Layar awal: My Asset, tab Task.
- Data:
  - DU-064-1: entitas khusus `Basic Aksi Borrowed {runId}` dengan plan `Basic`, yang tidak dipakai spec lain.
  - DU-064-2: pengguna `Nadia Pratiwi {runId}`, Borrower aktif ber-akun login di entitas DU-064-1, Group `Head Office`.
  - DU-064-3: pinjaman milik Borrower berstatus `Borrowed`, Source `Admin`, satu aset: Name `Kamera Canon EOS 90D {runId}`, Asset ID `CAM-90D-{runId}`, Brand `Canon`, Model/Type `EOS 90D`, Group `Head Office`, Duration `5 days`, Extensions `0 / 2`.
  - DU-064-4: pinjaman milik Borrower berstatus `Borrowed`, Source `Self-service`, satu aset: Name `Tablet Lenovo Tab P11 {runId}`, Asset ID `TAB-P11-{runId}`, Brand `Lenovo`, Model/Type `Tab P11`, Group `Head Office`, Duration `2 days`.
  - DU-064-5: pengguna `Gita Permata {runId}`, role Asset Admin, cakupan Group `Head Office`, Aktor Borrow di entitas DU-064-1.
- Kondisi:
  - Spec ini memakai entitas khusus berplan `Basic` yang tidak dipakai spec lain.
  - Pinjaman DU-064-3 dan DU-064-4 terbentuk saat entitas masih berplan `Full`, lalu entitas diturunkan ke plan `Basic` sebelum langkah 1; keduanya tetap berjalan.
  - Extend yang dilakukan Aktor Borrow pada pinjaman DU-064-3 berada dalam batas Max extensions `2` dan langsung berlaku tanpa approval.

## Test Steps

### Request Extension tidak tersedia dan Return hanya pada baris self-service pada menu baris tab Borrowed
1. Klik tab `Borrowed`
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi baris `Kamera Canon EOS 90D {runId}` berstatus `Borrowed`
4. Verifikasi baris `Tablet Lenovo Tab P11 {runId}` berstatus `Borrowed`
5. Klik `⋯` pada baris `Kamera Canon EOS 90D {runId}`
6. Verifikasi opsi `Borrow Log` tersedia pada menu baris
7. Verifikasi opsi `Request Extension` tidak tersedia pada menu baris
8. Verifikasi opsi `Return` tidak tersedia pada menu baris
9. Tutup menu baris
10. Klik `⋯` pada baris `Tablet Lenovo Tab P11 {runId}`
11. Verifikasi opsi `Return` tersedia pada menu baris
12. Verifikasi opsi `Request Extension` tidak tersedia pada menu baris
13. Tutup menu baris

### Bulk action Request Extension tidak tersedia
14. Centang baris `Kamera Canon EOS 90D {runId}`
15. Verifikasi baris `Kamera Canon EOS 90D {runId}` tercentang
16. Verifikasi bulk action `Request Extension` tidak tersedia
17. Hapus centang baris `Kamera Canon EOS 90D {runId}`

### Pinjaman berjalan tetap berjalan dan Extend oleh Aktor Borrow dari web
18. Catat Due Date baris `Kamera Canon EOS 90D {runId}`
19. Aktor Borrow `Gita Permata {runId}` melakukan Extend atas pinjaman `Kamera Canon EOS 90D {runId}` dari web
20. Muat ulang halaman
21. Klik tab `Borrowed`
22. Ketik Search `{runId}`, tekan Enter
23. Verifikasi baris `Kamera Canon EOS 90D {runId}` tetap berstatus `Borrowed`
24. Verifikasi Due Date baris `Kamera Canon EOS 90D {runId}` berbeda dari Due Date yang dicatat
