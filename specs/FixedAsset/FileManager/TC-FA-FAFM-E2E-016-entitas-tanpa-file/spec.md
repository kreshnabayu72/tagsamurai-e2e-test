---
id: TC-FA-FAFM-E2E-016-entitas-tanpa-file
title: "Entitas tanpa file: kartu 0.0 KB dan empty state setiap tabel"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: ["ARS-07b", "EC-17", "F-FAFM-06.k1", "F-FAFM-06f", "F-FAFM-06g", "INV-02f", "SUC-06d"]
smoke: []
dependsOn: []
trace:
  "ARS-07b": [2, 3, 13]
  "EC-17": [2, 3, 4, 13]
  "F-FAFM-06.k1": 3
  "F-FAFM-06f": 3
  "F-FAFM-06g": [2, 4, 6, 8, 11, 13]
  "INV-02f": 3
  "SUC-06d": 3
anchor: []
coverage:
  web: automated
---

# Entitas tanpa file: kartu 0.0 KB dan empty state setiap tabel

## Prerequisites
- Aktor: Total Control, user `Kartika Lestari {runId}` (tampil `Kartika L`), akun aktif dengan kredensial disediakan fase 2.
- Layar awal: halaman beranda Fixed Asset, tempat sidebar tampil.
- Data:
  - Spec ini memakai entitas khusus (daftar-kosong): entitas belum menyimpan file apa pun, tidak punya file di Recycle Bin, tidak punya entri Changelog, dan tidak punya aset berstatus Disposed atau Unmanaged.
  - DU-016-1: User `Kartika Lestari {runId}` sebagai satu-satunya data ber-runId di entitas.
- Kondisi:
  - Storage Quota entitas terisi, sehingga kartu Storage Usage tampil normal.

## Test Steps

### Kartu Storage Usage menampilkan 0.0 KB saat entitas belum menyimpan file
1. Buka File Manager lewat grup `Settings` di sidebar Fixed Asset
2. Verifikasi kartu `Storage Usage` tampil terisi pada entitas tanpa file
3. Verifikasi kartu menampilkan `Fixed Asset 0.0 KB`

### Kartu tetap tampil dan setiap tabel tetap berfungsi dengan empty state
4. Verifikasi tab Files menampilkan empty state `No files yet` dengan deskripsi `Photos and documents will appear here once they are uploaded to assets.`
5. Klik tab `Disposed & Unmanaged Assets`
6. Verifikasi tab `Disposed & Unmanaged Assets` menampilkan empty state `No asset data yet` dengan deskripsi `Disposed and unmanaged assets will appear here.`
7. Klik `Recycle Bin` pada header kartu `Storage Usage`
8. Verifikasi modal `Recycle Bin` menampilkan empty state `Recycle bin is empty` dengan deskripsi `Deleted files will appear here before being permanently removed.`
9. Tutup modal `Recycle Bin`
10. Klik `Changelog` pada header kartu `Storage Usage`
11. Verifikasi modal `Changelog` menampilkan empty state `No changelog yet` dengan deskripsi `Activities and changes will appear here.`
12. Tutup modal `Changelog`
13. Verifikasi kartu menampilkan `Fixed Asset 0.0 KB` sesudah modal ditutup
