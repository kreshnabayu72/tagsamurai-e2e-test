---
id: TC-FA-ASTL-E2E-048-asset-name-tercermin-dep-settings-asset-name
title: "Perubahan Asset Name tercermin di daftar"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.7#r7"]
smoke: []
dependsOn: ["Settings Asset Name: Asset Name dan Category"]
trace:
  "§9.7#r7": [8, 9, 11]
anchor: [4]
coverage:
  web: automated
---

# Perubahan Asset Name tercermin di daftar

## Prerequisites
- Aktor: Hendra Saputra, Total Control dengan cakupan seluruh client.
- Layar awal: Fixed Asset > Assets (tab Assets).
- Data:
  - DU-048-1: Asset Name `Laptop Pro 16 {runId}` dengan Category `Perangkat IT {runId}`, satu aset tampil sebagai `Laptop Pro 16 {runId} - 1` di Group `IT`.
  - DU-048-2: Asset Name hasil ubah `Laptop Pro 16 Gen2 {runId}`, dari `Laptop Pro 16 {runId}`; aset yang sama tampil sebagai `Laptop Pro 16 Gen2 {runId} - 1`.
  - DU-048-3: Category hasil ubah `Perangkat Kerja {runId}`, dari `Perangkat IT {runId}`.

## Test Steps

### Perubahan Asset Name dan Category tercermin tanpa log tingkat aset
1. Ketik Search `Laptop Pro 16 {runId}`, tekan Enter
2. Klik ikon `Changelog` pada toolbar
3. Catat entri milik aset `Laptop Pro 16 {runId} - 1` di modal Changelog, lalu tutup modal
4. Verifikasi baris `Laptop Pro 16 {runId} - 1` tampil dengan kolom `Category` `Perangkat IT {runId}`
5. Pada Settings Asset Name, ubah Asset Name `Laptop Pro 16 {runId}` menjadi `Laptop Pro 16 Gen2 {runId}`
6. Pada Settings Asset Name, ubah Category Asset Name tersebut menjadi `Perangkat Kerja {runId}`
7. Ganti isi kotak Search dengan `Laptop Pro 16 Gen2 {runId}`, tekan Enter, tanpa memuat ulang halaman
8. Verifikasi kolom `Name` baris aset tersebut menampilkan `Laptop Pro 16 Gen2 {runId} - 1`
9. Verifikasi kolom `Category` baris `Laptop Pro 16 Gen2 {runId} - 1` menampilkan `Perangkat Kerja {runId}`
10. Klik ikon `Changelog` pada toolbar
11. Verifikasi modal Changelog tidak memuat entri baru milik aset `Laptop Pro 16 Gen2 {runId} - 1` dibanding yang dicatat pada langkah 3 (entri aset lain diabaikan), sehingga perubahan Asset Name tidak menambah entri log tingkat aset
