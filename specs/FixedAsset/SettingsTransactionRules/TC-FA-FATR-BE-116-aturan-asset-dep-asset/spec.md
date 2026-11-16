---
id: TC-FA-FATR-BE-116-aturan-asset-dep-asset
title: "Override saat aset berubah"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["§9.2#b121", "§9.2#b123", "§9.2#b132", "§9.2#b133", "§9.2#b134", "§9.2#b146", "§9.2#b148", "§9.4.2#r34", "§9.4.3#b11"]
smoke: []
dependsOn:
  - "Asset: Asset Detail dan penghapusan aset"
trace:
  "§9.2#b121": 2
  "§9.2#b146": 2
  "§9.4.2#r34": [2, 4, 8]
  "§9.2#b123": 4
  "§9.2#b148": 4
  "§9.4.3#b11": 4
  "§9.2#b132": [6, 12]
  "§9.2#b134": 8
  "§9.2#b133": 10
---

# Override saat aset berubah

## Prerequisites
- Aktor: Total Control.
- Data:
  - DU-116-1: Category `Perangkat Akses {runId} > Pintu Gerbang {runId}`.
  - DU-116-2: Category `Perangkat Akses {runId} > Palang Parkir {runId}`.
  - DU-116-3: Asset Name `Gerbang Geser {runId}` di Category `Perangkat Akses {runId} > Pintu Gerbang {runId}`.
  - DU-116-4: Asset Name `Palang Otomatis {runId}` di Category `Perangkat Akses {runId} > Palang Parkir {runId}`.
  - DU-116-5: aset `Gerbang Kontrol Unit 1 {runId}` ber-Asset Name `Gerbang Geser {runId}`, di Category `Perangkat Akses {runId} > Pintu Gerbang {runId}`.
  - DU-116-6: override transaksi pinjam, target aset `Gerbang Kontrol Unit 1 {runId}`, Category `Perangkat Akses {runId} > Pintu Gerbang {runId}`, Max duration `5`.
  - DU-116-7: override transaksi pinjam, target aset `Gerbang Kontrol Unit 1 {runId}`, Category All categories, Max duration `8`.
  - DU-116-8: aset `Gerbang Kontrol Unit 2 {runId}` ber-Asset Name `Gerbang Geser {runId}`, di Category `Perangkat Akses {runId} > Pintu Gerbang {runId}`.
  - DU-116-9: override transaksi pinjam, target aset `Gerbang Kontrol Unit 2 {runId}`, Category All categories, Max duration `5`.
  - DU-116-10: aset `Gerbang Kontrol Unit 3 {runId}` ber-Asset Name `Gerbang Geser {runId}`, di Category `Perangkat Akses {runId} > Pintu Gerbang {runId}`, tanpa override.
  - DU-116-11: pengajuan pinjam selama `7` Days.
  - DU-116-12: pengajuan pinjam selama `10` Days.
- Kondisi:
  - Max duration bernilai `14` di Company default untuk transaksi pinjam.

## Test Steps

### Aset yang dihapus: override tetap tersimpan
1. Total Control menghapus aset `Gerbang Kontrol Unit 2 {runId}`
2. Verifikasi override target aset `Gerbang Kontrol Unit 2 {runId}` tetap tersimpan dan tampil di tabel Overrides sesudah aset dihapus
3. Total Control mengajukan peminjaman aset `Gerbang Kontrol Unit 3 {runId}`, aset lain tanpa override, selama `10` Days
4. Verifikasi pengajuan selama `10` Days atas aset `Gerbang Kontrol Unit 3 {runId}`, yang tidak punya override, diterima dan Max duration efektif adalah `14` dari Company default

### Asset Name aset diganti: override aset ber-Category leaf tidak berlaku, All categories tetap berlaku
5. Total Control mengajukan peminjaman aset `Gerbang Kontrol Unit 1 {runId}` selama `7` Days saat aset ber-Asset Name `Gerbang Geser {runId}` di Category `Perangkat Akses {runId} > Pintu Gerbang {runId}`
6. Verifikasi pengajuan selama `7` Days ditolak karena override aset ber-Category leaf Max duration `5` menang atas override All categories Max duration `8` selama Category aset `Perangkat Akses {runId} > Pintu Gerbang {runId}`
7. Total Control mengganti Asset Name aset `Gerbang Kontrol Unit 1 {runId}` menjadi `Palang Otomatis {runId}` di Category `Perangkat Akses {runId} > Palang Parkir {runId}`
8. Verifikasi kedua override target aset `Gerbang Kontrol Unit 1 {runId}`, yaitu Category `Perangkat Akses {runId} > Pintu Gerbang {runId}` dan All categories, tetap tersimpan dan tampil di tabel Overrides sesudah Asset Name aset diganti
9. Total Control mengajukan peminjaman aset `Gerbang Kontrol Unit 1 {runId}` selama `10` Days sesudah Asset Name aset diganti
10. Verifikasi pengajuan selama `10` Days ditolak karena override aset All categories Max duration `8` tetap berlaku sesudah Category aset berubah
11. Total Control mengajukan peminjaman aset `Gerbang Kontrol Unit 1 {runId}` selama `7` Days sesudah Asset Name aset diganti
12. Verifikasi pengajuan selama `7` Days diterima karena override aset ber-Category leaf Max duration `5` untuk Category `Perangkat Akses {runId} > Pintu Gerbang {runId}` tidak berlaku bila Category aset berubah
