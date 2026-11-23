---
id: TC-FA-FAFM-E2E-017-kartu-storage-usage-nilai
title: "Kartu Storage Usage: angka sesuai data dan label tab"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EC-16, F-FAFM-06a, F-FAFM-06d, FAFM-LOGIC-06a, INV-02b, INV-02c, SUC-06a, "§4.2c#p1", "§4.4#b11", "EB-TBL-13@kartu-storage-usage"]
smoke: []
dependsOn: []
trace:
  EC-16: [3, 4, 5]
  F-FAFM-06a: 2
  F-FAFM-06d: 5
  FAFM-LOGIC-06a: [3, 4, 5, 20]
  INV-02b: 2
  INV-02c: 6
  SUC-06a: [5, 19, 20]
  "§4.2c#p1": 2
  "§4.4#b11": 16
  "EB-TBL-13@kartu-storage-usage": [5, 7, 8, 9, 16, 20]
coverage:
  web: automated
---

# Kartu Storage Usage: angka sesuai data dan label tab

## Prerequisites
- Aktor: Total Control.
- Layar awal: Halaman utama Fixed Asset.
- Data:
  - DU-017-1: Entitas khusus `FAMS Kartu Storage {runId}`.
  - DU-017-2: File aktif `laptop-front-{runId}.jpg`, Source `Asset Photo`, Kategori `Asset Photo`, Size `300.0 KB`, Asset `Laptop Dell Latitude 5420 - 4`, Group `Head Office`.
  - DU-017-3: File aktif `damage-01-{runId}.jpg`, Source `Damaged Photo`, Kategori `Damaged`, Size `200.0 KB`, Asset `Toyota Avanza - 2`, Group `Fleet`.
  - DU-017-4: File di Recycle Bin `laptop-old-{runId}.png`, Source `Asset Photo`, Size `150.0 KB`, Deleted By `System`, Asset `Laptop Dell Latitude 5420 - 4`, Group `Head Office`.
  - DU-017-5: File di Recycle Bin `repair-02-{runId}.jpg`, Source `Repair Photo`, Size `100.0 KB`, Deleted By `Rina A`, Asset `Toyota Avanza - 2`, Group `Fleet`.
  - DU-017-6: Kategori `Missing` tanpa file aktif, Total Size `0.0 KB`.
  - DU-017-7: Storage Quota entitas `50.0 GB`.
  - DU-017-8: Aset `Printer HP LaserJet {runId}` berstatus `Disposed`, Group `Head Office`, tanpa file.
  - DU-017-9: File di luar aset (Other files) `lampiran-servis-{runId}.pdf`, Size `50.0 KB`, tidak melekat pada aset mana pun.
  - Fixed Asset yang diharapkan sesudah DU-017-4 dihapus permanen: lebih kecil `150.0 KB` dari nilai awal pada langkah 5.
  - Fixed Asset yang diharapkan sesudah DU-017-4 dihapus permanen `650.0 KB` ditambah Data & Log Size aset DU-017-8, dari 300.0 KB + 200.0 KB (file aktif) + 100.0 KB (file Recycle Bin) + 50.0 KB (Other files).
  - Label tab yang diharapkan `Asset Photo (300.0 KB)`, `Damaged (200.0 KB)`, dan `Missing (0.0 KB)`, dari total ukuran file aktif per Kategori.
- Kondisi:
  - Spec ini memakai entitas khusus DU-017-1 yang tidak dipakai spec lain.
  - Entitas memiliki satu aset `Disposed` (DU-017-8) dan satu file di luar aset (DU-017-9), sehingga Fixed Asset terdiri dari file aktif, file Recycle Bin, Data & Log Size aset `Disposed`, dan Other files.
  - Data & Log Size aset `Disposed` dibentuk server dan nilainya tidak ditetapkan spec, sehingga Fixed Asset dibandingkan dengan selisih dan jumlah komponen, bukan dengan nilai mutlak.
  - Total Used pada Global Settings > File Manager entitas ini sudah terisi, dan Storage Quota bernilai `50.0 GB`.

## Test Steps

### Kartu Storage Usage tampil bersama halaman
1. Buka File Manager lewat grup `Settings` di sidebar Fixed Asset
2. Verifikasi kartu `Storage Usage` tampil tanpa aksi tambahan sesudah halaman terbuka

### Angka kartu sesuai data entitas
3. Verifikasi `Total Used` pada kartu terisi dengan ukuran, bukan `—`
4. Verifikasi `Storage Quota` pada kartu menampilkan `50.0 GB`
5. Verifikasi kartu menampilkan `Fixed Asset` terisi, dicatat sebagai nilai awal
6. Verifikasi kartu hanya menampilkan angka dan tidak memuat kontrol untuk mengubah `Total Used` atau `Storage Quota`

### Label tab Kategori memuat total ukuran file aktif
7. Verifikasi label tab `Asset Photo (300.0 KB)`
8. Verifikasi label tab `Damaged (200.0 KB)`
9. Verifikasi label tab `Missing (0.0 KB)`

### Angka kartu mengikuti data sesudah satu penggeser
10. Klik tombol `Recycle Bin` pada header kartu `Storage Usage`
11. Ketik Search `{runId}`, tekan Enter
12. Klik `Permanently Delete` pada baris `laptop-old-{runId}.png`
13. Klik `[Permanently Delete]` pada dialog `Permanently Delete File`
14. Tutup modal `Recycle Bin`
15. Muat ulang halaman
16. Verifikasi kartu `Fixed Asset` lebih kecil 150.0 KB dari nilai awal pada langkah 5

### Fixed Asset memuat seluruh komponen penyimpanan
17. Klik tab `Disposed & Unmanaged Assets`
18. Ketik Search `{runId}`, tekan Enter
19. Verifikasi aset `Printer HP LaserJet {runId}` tampil dengan Data & Log Size terisi, dicatat untuk langkah berikutnya
20. Verifikasi kartu `Fixed Asset` sama dengan `650.0 KB` ditambah Data & Log Size aset pada langkah 19
