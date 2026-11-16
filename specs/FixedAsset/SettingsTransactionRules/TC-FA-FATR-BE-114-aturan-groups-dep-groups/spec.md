---
id: TC-FA-FATR-BE-114-aturan-groups-dep-groups
title: "Override saat Group berubah"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["§9.2#b121", "§9.2#b123", "§9.2#b129", "§9.2#b130", "§9.2#b146", "§9.2#b148", "§9.4.2#r34", "§9.4.3#b11"]
smoke: []
dependsOn:
  - "Settings Groups: hapus dan nonaktifkan Group"
trace:
  "§9.2#b121": [2, 6]
  "§9.2#b146": [2, 6]
  "§9.4.2#r34": [2, 6, 8]
  "§9.2#b123": [4, 8]
  "§9.2#b148": 8
  "§9.4.3#b11": 8
  "§9.2#b129": 12
  "§9.2#b130": [14, 17]
---

# Override saat Group berubah

## Prerequisites
- Aktor: Total Control.
- Data:
  - DU-114-1: Group `Divisi Gudang Lama {runId}`.
  - DU-114-2: override pada transaksi pinjam All categories, target Group `Divisi Gudang Lama {runId}`, Max duration `5`.
  - DU-114-3: Group `Divisi Pengecatan {runId}`, aktif.
  - DU-114-4: override pada transaksi pinjam All categories, target Group `Divisi Pengecatan {runId}`, Max duration `5`.
  - DU-114-5: aset `Gerinda Meja Unit 1 {runId}` di Group `Divisi Pengecatan {runId}`.
  - DU-114-6: Group `Divisi Fabrikasi {runId}`.
  - DU-114-7: override pada transaksi pinjam All categories, target Group `Divisi Fabrikasi {runId}`, Max duration `5`.
  - DU-114-8: Group `Seksi Las {runId}`, sub-Group dari `Divisi Fabrikasi {runId}`.
  - DU-114-9: aset `Mesin Las Unit 1 {runId}` di Group `Seksi Las {runId}`.
  - DU-114-10: Group `Divisi Pemeliharaan {runId}`, di luar subtree `Divisi Fabrikasi {runId}`.
  - DU-114-12: aset `Kompresor Cat Unit 1 {runId}` di Group `Divisi Pemeliharaan {runId}`, di luar subtree `Divisi Fabrikasi {runId}`.
  - DU-114-13: pengajuan pinjam selama `10` Days.
- Kondisi:
  - Max duration bernilai `14` di Company default untuk transaksi pinjam.

## Test Steps

### Group yang dihapus: override tetap tersimpan
1. Total Control menghapus Group `Divisi Gudang Lama {runId}`
2. Verifikasi override target Group `Divisi Gudang Lama {runId}` tetap tersimpan dan tampil di tabel Overrides sesudah Group dihapus

### Group yang dinonaktifkan: override tidak berlaku
3. Total Control mengajukan peminjaman aset `Gerinda Meja Unit 1 {runId}` selama `10` Days saat Group `Divisi Pengecatan {runId}` masih aktif
4. Verifikasi pengajuan selama `10` Days ditolak karena override Max duration `5` untuk Group `Divisi Pengecatan {runId}` berlaku selama Group aktif
5. Total Control menonaktifkan Group `Divisi Pengecatan {runId}`
6. Verifikasi override target Group `Divisi Pengecatan {runId}` tetap tersimpan dan tampil di tabel Overrides sesudah Group dinonaktifkan
7. Total Control mengajukan peminjaman aset `Gerinda Meja Unit 1 {runId}` selama `10` Days sesudah Group `Divisi Pengecatan {runId}` dinonaktifkan
8. Verifikasi pengajuan selama `10` Days diterima karena override pada Group yang dinonaktifkan tidak berlaku, dan Max duration efektif adalah `14` dari Company default

### Group override berlaku untuk sub-Group yang ditambahkan kemudian
9. Total Control menambah sub-Group `Seksi Cat {runId}` di bawah Group `Divisi Fabrikasi {runId}`, sesudah override target `Divisi Fabrikasi {runId}` ada
10. Total Control menempatkan aset `Kompresor Cat Unit 1 {runId}` di Group `Seksi Cat {runId}`
11. Total Control mengajukan peminjaman aset `Kompresor Cat Unit 1 {runId}` di Group `Seksi Cat {runId}`, sub-Group baru dari `Divisi Fabrikasi {runId}`, selama `10` Days
12. Verifikasi pengajuan selama `10` Days ditolak karena override Max duration `5` untuk Group `Divisi Fabrikasi {runId}` berlaku untuk sub-Group yang ditambahkan kemudian

### Group yang dipindah keluar dari subtree tidak lagi terkena override
13. Total Control mengajukan peminjaman aset `Mesin Las Unit 1 {runId}` di Group `Seksi Las {runId}` selama `10` Days
14. Verifikasi pengajuan selama `10` Days ditolak karena override Max duration `5` untuk Group `Divisi Fabrikasi {runId}` berlaku selama `Seksi Las {runId}` ada di subtree-nya
15. Total Control memindahkan Group `Seksi Las {runId}` ke bawah Group `Divisi Pemeliharaan {runId}`
16. Total Control mengajukan peminjaman aset `Mesin Las Unit 1 {runId}` selama `10` Days sesudah `Seksi Las {runId}` dipindah keluar dari subtree `Divisi Fabrikasi {runId}`
17. Verifikasi pengajuan selama `10` Days diterima karena override Group `Divisi Fabrikasi {runId}` berhenti berlaku bagi Group yang dipindah keluar dari subtree-nya, dan Max duration efektif adalah `14`
