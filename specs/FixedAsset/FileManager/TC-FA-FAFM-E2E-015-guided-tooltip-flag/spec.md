---
id: TC-FA-FAFM-E2E-015-guided-tooltip-flag
title: "Guided Tooltip muncul di kunjungan pertama dan flag bertahan antar sesi"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.7#r1", "EB-TBL-10"]
smoke: []
dependsOn: []
trace:
  "§4.7#r1": 2
  "EB-TBL-10": [2, 4, 6, 7, 9, 12, 13, 15, 16, 18, 21, 23, 27, 28]
anchor: [2, 6, 9, 12, 15, 18, 21, 23, 27]
coverage:
  web: automated
---

# Guided Tooltip muncul di kunjungan pertama dan flag bertahan antar sesi

## Prerequisites
- Aktor: Total Control, user `Indra Kusuma {runId}` (tampil `Indra K`), akun aktif dengan kredensial disediakan fase 2. Aktor kedua: Total Control lain `Jihan Safitri {runId}` (tampil `Jihan S`) di entitas yang sama.
- Layar awal: halaman beranda Fixed Asset, tempat sidebar tampil.
- Data:
  - DU-015-1: User `Indra Kusuma {runId}` yang belum pernah membuka halaman File Manager, sehingga flag `guided_tooltip_seen_fams-file-manager` belum tersetel.
  - DU-015-2: User `Jihan Safitri {runId}` yang belum pernah membuka halaman File Manager, sehingga flag `guided_tooltip_seen_fams-file-manager` belum tersetel.
- Kondisi:
  - Aktor pertama dan aktor kedua memakai browser yang berbeda dengan sesi login masing-masing.

## Test Steps

### Guided Tooltip muncul otomatis di kunjungan pertama dan tidak muncul lagi sesudah Skip
1. Buka File Manager lewat grup `Settings` di sidebar Fixed Asset
2. Verifikasi Guided Tooltip halaman File Manager tampil otomatis dengan indikator `Step 1 of 4`
3. Klik `[Skip]`
4. Verifikasi Guided Tooltip tertutup
5. Muat ulang halaman dengan F5
6. Verifikasi kartu `Storage Usage` tampil sesudah Skip dan muat ulang
7. Verifikasi Guided Tooltip tidak tampil sesudah muat ulang

### Putar ulang lewat tombol bantuan tidak mereset flag
8. Klik `[?]` di sebelah kanan Breadcrumb
9. Verifikasi Guided Tooltip tampil dari `Step 1 of 4`
10. Klik `[Skip]`
11. Muat ulang halaman dengan F5
12. Verifikasi kartu `Storage Usage` tampil sesudah putar ulang
13. Verifikasi Guided Tooltip tidak tampil sesudah putar ulang dan muat ulang

### Flag tersimpan di akun dan berlaku di browser lain untuk user yang sama
14. Aktor pertama login di browser lain dan membuka File Manager lewat grup `Settings` di sidebar Fixed Asset
15. Verifikasi kartu `Storage Usage` tampil di browser lain
16. Verifikasi Guided Tooltip tidak tampil di browser lain

### User lain dengan flag belum tersetel tetap mendapat Guided Tooltip di kunjungan pertama
17. Aktor kedua login di browser lain dan membuka File Manager lewat grup `Settings` di sidebar Fixed Asset
18. Verifikasi Guided Tooltip tampil otomatis bagi aktor kedua dengan indikator `Step 1 of 4`

### Keluar tanpa menyelesaikan tidak menyetel flag
19. Aktor kedua membuka halaman beranda Fixed Asset
20. Aktor kedua membuka File Manager lewat grup `Settings` di sidebar Fixed Asset
21. Verifikasi Guided Tooltip tampil lagi bagi aktor kedua dengan indikator `Step 1 of 4`

### Flag tersetel sesudah Done dan bertahan setelah logout lalu login lagi
22. Klik `[Next]` pada Guided Tooltip sampai indikator `Step 4 of 4` tampil
23. Verifikasi tombol `[Done]` tampil pada step terakhir
24. Klik `[Done]`
25. Aktor kedua logout dari browser lain
26. Aktor kedua login kembali dan membuka File Manager lewat grup `Settings` di sidebar Fixed Asset
27. Verifikasi kartu `Storage Usage` tampil bagi aktor kedua sesudah login kembali
28. Verifikasi Guided Tooltip tidak tampil bagi aktor kedua sesudah login kembali
