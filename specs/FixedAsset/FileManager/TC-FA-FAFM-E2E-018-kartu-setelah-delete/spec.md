---
id: TC-FA-FAFM-E2E-018-kartu-setelah-delete
title: "Kartu Storage Usage dan label tab sesudah Delete file"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: [EC-21, F-FAFM-06.k2, SYN-01i]
smoke: []
dependsOn: []
trace:
  EC-21: [11, 13]
  F-FAFM-06.k2: 13
  SYN-01i: [11, 12]
anchor: [2, 3, 6]
coverage:
  web: automated
---

# Kartu Storage Usage dan label tab sesudah Delete file

## Prerequisites
- Aktor: Total Control.
- Layar awal: Halaman utama Fixed Asset.
- Data:
  - DU-018-1: Entitas khusus `FAMS Kartu Delete {runId}`.
  - DU-018-2: File aktif `laptop-front-{runId}.jpg`, Source `Asset Photo`, Kategori `Asset Photo`, Size `300.0 KB`, Asset `Laptop Dell Latitude 5420 - 4`, Group `Head Office`.
  - DU-018-3: File aktif `damage-01-{runId}.jpg`, Source `Damaged Photo`, Kategori `Damaged`, Size `200.0 KB`, Asset `Toyota Avanza - 2`, Group `Fleet`, yang di-Delete pada spec ini.
  - DU-018-4: File di Recycle Bin `repair-02-{runId}.jpg`, Source `Repair Photo`, Size `100.0 KB`, Deleted By `Rina A`, Asset `Toyota Avanza - 2`, Group `Fleet`.
  - Fixed Asset yang diharapkan `600.0 KB`, dari 300.0 KB + 200.0 KB (file aktif) + 100.0 KB (file Recycle Bin), sebelum dan sesudah Delete karena file di Recycle Bin tetap dihitung.
  - Label tab yang diharapkan sesudah Delete `Damaged (0.0 KB)` dan `Asset Photo (300.0 KB)`, dari total ukuran file aktif per Kategori.
- Kondisi:
  - Spec ini memakai entitas khusus DU-018-1 yang tidak dipakai spec lain.
  - Entitas tidak memiliki aset `Disposed` atau Unmanaged dan tidak memiliki file di luar aset, sehingga Fixed Asset hanya terdiri dari file aktif dan file Recycle Bin.

## Test Steps

### Kartu dan label tab sebelum Delete
1. Buka File Manager lewat grup `Settings` di sidebar Fixed Asset
2. Verifikasi label tab `Damaged (200.0 KB)` sebelum Delete
3. Verifikasi kartu `Fixed Asset` bernilai `600.0 KB` sebelum Delete

### Delete satu file aktif
4. Klik tab `Damaged`
5. Ketik Search `{runId}`, tekan Enter
6. Verifikasi file `damage-01-{runId}.jpg` tampil di tab `Damaged`
7. Buka aksi baris `damage-01-{runId}.jpg`
8. Klik `Delete`
9. Klik `[Delete]` pada dialog `Delete File`

### Kartu dan label tab sesudah Delete dibaca ulang
10. Muat ulang halaman
11. Verifikasi label tab `Damaged (0.0 KB)` sesudah Delete
12. Verifikasi label tab `Asset Photo (300.0 KB)` tidak berubah sesudah Delete
13. Verifikasi kartu `Fixed Asset` tetap bernilai `600.0 KB` sesudah Delete
