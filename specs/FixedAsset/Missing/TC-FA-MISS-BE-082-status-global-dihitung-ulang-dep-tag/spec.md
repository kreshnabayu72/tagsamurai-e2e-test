---
id: TC-FA-MISS-BE-082-status-global-dihitung-ulang-dep-tag
title: "Server: Cancel Report atas laporan Waiting for Confirmation menghitung ulang status global aset dari state aset terkini, bukan menyalin status saat laporan dibuat"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["§1.2#r58"]
smoke: []
dependsOn: ["Tag: dialog Report TAG (identifikasi manual)"]
trace:
  "§1.2#r58": [3, 5, 7, 8]
---

# Server: Cancel Report atas laporan Waiting for Confirmation menghitung ulang status global aset dari state aset terkini, bukan menyalin status saat laporan dibuat

## Prerequisites
- Aktor:
  - Pelapor sesi: Asset Admin sub-tab Audit tanpa hak Aktor Missing pada Group aset.
  - Total Control: cakupan seluruh client, melakukan Report TAG.
- Data:
  - DU-082-1: aset `Handheld Zebra MC9300 {runId}` di Group `Head Office`, tidak dipegang siapa pun, status global aset `Normal`, TAG terpasang `QR-082-0001`, belum punya record berjalan.
  - DU-082-2: What happened `Aset tidak berada di tempat terakhir dilihat`, dipakai Pelapor sesi.
  - DU-082-3: Reason `Label TAG rusak terkena air`, dipakai Total Control untuk Report TAG.
- Kondisi:
  - Cakupan Group Total Control meliputi `Head Office`.

## Test Steps

### Cancel Report sesudah state aset berubah menghitung ulang status global dari state terkini
1. Catat status global aset DU-082-1 sebelum laporan, yaitu `Normal`, dan jumlah node Missing Log aset itu
2. Pelapor sesi melakukan Report Missing atas aset DU-082-1 dari Task Detail sesi pemeriksaan dengan What happened `Aset tidak berada di tempat terakhir dilihat`
3. Verifikasi aset DU-082-1 mendapat record berstatus `Waiting for Confirmation` dan status global aset langsung `Missing`
4. Total Control melakukan Report TAG atas aset DU-082-1 lewat dialog Report TAG dengan identifikasi manual dan Reason `Label TAG rusak terkena air`
5. Verifikasi aset DU-082-1 menjadi `TAG Reported` sesudah Report TAG sementara record tetap `Waiting for Confirmation`, sehingga state aset berbeda dari saat laporan dibuat
6. Pelapor sesi melakukan Cancel my report atas record aset DU-082-1 dari Task Detail sesi pemeriksaan
7. Verifikasi status record aset DU-082-1 menjadi `Canceled` dengan satu node `Report canceled by`
8. Verifikasi status global aset DU-082-1 dihitung ulang dari state aset terkini menjadi `TAG Reported` karena aset tidak dipegang, dan bukan `Normal` yang berlaku saat laporan dibuat
