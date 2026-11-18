---
id: TC-FA-ASTL-E2E-039-status-borrow-dep-borrow
title: "Status Borrow dan pintasan Borrow"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-02d", "ASTL-LOGIC-16e", "ASTL-LOGIC-16f", "§9.7#r1"]
smoke: []
dependsOn: ["Borrow: transaksi Borrow"]
trace:
  "ASTL-LOGIC-02d": 4
  "ASTL-LOGIC-16e": 12
  "ASTL-LOGIC-16f": 9
  "§9.7#r1": [4, 5]
anchor: [2, 8]
coverage:
  web: automated
---

# Status Borrow dan pintasan Borrow

## Prerequisites
- Aktor: Hendra Saputra, Total Control dengan cakupan seluruh client
- Layar awal: Fixed Asset > Assets (tab Assets).
- Data:
  - DU-039-1: aset `Laptop Pro 16 {runId} - 1`, Group `IT {runId}`, managed, Custody `Available`.
  - DU-039-2: aset `Kamera Mirrorless {runId} - 1`, Group `Cabang Bandung {runId}`, Unmanaged, Custody `Borrowed` oleh transaksi Borrow yang sedang berjalan. Keadaan ini dibentuk lewat produk: aset managed dipinjam lewat modul Borrow, lalu ditukar menjadi Unmanaged lewat Manage sumber Switch pada group yang sama.

## Test Steps

### Status Borrow tercermin tanpa muat ulang
1. Ketik Search `Laptop Pro 16 {runId}`, tekan Enter
2. Verifikasi baris `Laptop Pro 16 {runId} - 1` menampilkan `Available`
3. Pada modul Borrow, Hendra Saputra membuat transaksi Borrow atas `Laptop Pro 16 {runId} - 1` hingga aset dipinjam, tanpa memuat ulang halaman Fixed Asset > Assets
4. Verifikasi badge Status baris `Laptop Pro 16 {runId} - 1` berubah menjadi `Borrowed` dan `Available` tidak lagi tampil
5. Verifikasi angka kartu `In Transaction` menjadi `1` karena Search hanya memuat aset ini

### Transaksi berjalan pada aset Unmanaged tidak diselesaikan dari daftar
6. Ketik Search `Kamera Mirrorless {runId}`, tekan Enter
7. Buka menu `⋯` baris `Kamera Mirrorless {runId} - 1`
8. Verifikasi menu aksi baris `Kamera Mirrorless {runId} - 1` memuat `Detail`
9. Verifikasi menu aksi baris tidak menawarkan aksi untuk menyelesaikan atau melepas transaksi Borrow yang berjalan
10. Tutup menu aksi baris
11. Pada modul Borrow, Hendra Saputra menyelesaikan pengembalian aset `Kamera Mirrorless {runId} - 1`, tanpa memuat ulang halaman Fixed Asset > Assets
12. Verifikasi badge Status baris `Kamera Mirrorless {runId} - 1` berubah menjadi `Available` dengan badge overlay `Unmanaged`
