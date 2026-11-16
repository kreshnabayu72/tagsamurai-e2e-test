---
id: TC-FA-FATR-BE-118-aturan-license-dep-license
title: "Kuota Group pada Destination quota check"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["§11#r12"]
smoke: []
dependsOn:
  - "License: alokasi kuota per Group"
trace:
  "§11#r12": [2, 4, 6, 9]
---

# Kuota Group pada Destination quota check

## Prerequisites
- Aktor: Total Control.
- Data:
  - DU-118-1: Group `Divisi Cabang Timur {runId}`, alokasi kuota per Group bernilai `3`.
  - DU-118-2: Group `Divisi Pusat {runId}`.
  - DU-118-3: aset `Meja Lipat Unit 1 {runId}` di Group `Divisi Pusat {runId}`, transfer aktif berstatus In Transit menuju `Divisi Cabang Timur {runId}`.
  - DU-118-4: aset `Meja Lipat Unit 5 {runId}` di Group `Divisi Pusat {runId}`, transfer aktif berstatus In Transit menuju `Divisi Cabang Timur {runId}`, Destination quota check `OFF` lewat override aset.
  - DU-118-5: aset `Meja Lipat Unit 2 {runId}` di Group `Divisi Pusat {runId}`.
  - DU-118-6: aset `Meja Lipat Unit 3 {runId}` di Group `Divisi Pusat {runId}`.
  - DU-118-7: aset `Meja Lipat Unit 4 {runId}` di Group `Divisi Pusat {runId}`.
  - DU-118-8: aset `Meja Lipat Unit 6 {runId}` di Group `Divisi Pusat {runId}`, Destination quota check `OFF` lewat override aset.
- Kondisi:
  - Alokasi kuota per Group aktif pada entitas.
  - Destination quota check bernilai `ON` untuk aset `Meja Lipat Unit 2 {runId}`, `Meja Lipat Unit 3 {runId}`, dan `Meja Lipat Unit 4 {runId}`.

## Test Steps

### Submit tepat sampai batas kuota Group tujuan diterima
1. Total Control mengajukan transfer aset `Meja Lipat Unit 2 {runId}` dari Group `Divisi Pusat {runId}` ke Group `Divisi Cabang Timur {runId}`
2. Verifikasi pengajuan transfer aset `Meja Lipat Unit 2 {runId}` diterima karena baris ini ditambah dua baris aktif lain menuju Group tujuan berjumlah `3`, tidak melebihi alokasi kuota `3` yang diperiksa `check_group_quota()`

### Submit yang melebihi kuota Group tujuan diblokir seluruhnya
3. Total Control mengajukan transfer aset `Meja Lipat Unit 3 {runId}` dan `Meja Lipat Unit 4 {runId}` dalam satu pengajuan dari Group `Divisi Pusat {runId}` ke Group `Divisi Cabang Timur {runId}`
4. Verifikasi pengajuan ditolak seluruhnya karena kuota Group `Divisi Cabang Timur {runId}` terlampaui menurut `check_group_quota()`, dan tidak ada transfer yang dibuat untuk `Meja Lipat Unit 3 {runId}` maupun `Meja Lipat Unit 4 {runId}`

### Pemeriksaan kuota diulang saat Receive
5. Total Control mengajukan transfer aset `Meja Lipat Unit 6 {runId}` dari Group `Divisi Pusat {runId}` ke Group `Divisi Cabang Timur {runId}` dengan Destination quota check `OFF`
6. Verifikasi pengajuan transfer aset `Meja Lipat Unit 6 {runId}` diterima tanpa pemeriksaan kuota karena Destination quota check `OFF`
7. Total Control mengirim (Send) transfer aset `Meja Lipat Unit 2 {runId}` sehingga berstatus In Transit
8. Total Control menerima (Receive) transfer aset `Meja Lipat Unit 2 {runId}` di Group `Divisi Cabang Timur {runId}`
9. Verifikasi Receive transfer aset `Meja Lipat Unit 2 {runId}` ditolak karena pemeriksaan `check_group_quota()` diulang saat Receive dan kuota Group `Divisi Cabang Timur {runId}` sudah terlampaui oleh baris aktif lain
