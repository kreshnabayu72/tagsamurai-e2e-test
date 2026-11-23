---
id: TC-FA-FAFM-E2E-005-tab-files-paginasi-select-all
title: "Paginasi dan Select All tab Files atas seluruh daftar"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["TBL-02a", "TBL-02b", "EB-TBL-7@tabel-files", "EB-BLK-2@tabel-files"]
smoke: []
dependsOn: []
trace:
  "TBL-02a": [2, 3]
  "TBL-02b": [5, 7]
  "EB-TBL-7@tabel-files": [22, 25, 26]
  "EB-BLK-2@tabel-files": [11, 13, 14, 16, 18, 19]
anchor: [2, 10, 22]
coverage:
  web: automated
---

# Paginasi dan Select All tab Files atas seluruh daftar

## Prerequisites
- Aktor: Total Control, user `Maya Putri {runId}` (tampil `Maya P`), akun aktif dengan kredensial disediakan fase 2.
- Layar awal: halaman Settings > File Manager.
- Data:
  - Spec ini memakai entitas khusus yang tidak dipakai spec lain; tab `Asset Photo` entitas itu hanya berisi file di bawah, tepat 21 baris, tanpa file lain.
  - Group `Gudang Utama {runId}` ada di entitas aktor.
  - DU-005-1: File File Name `foto-{n}-{runId}.jpg`, File Format `JPG`, Source `Asset Photo`, Asset `Laptop Dell Latitude 5420 Unit {n} {runId}`, Group `Gudang Utama {runId}`, Size `500.0 KB`, Uploaded By `Maya P` (21 file; baris `foto-1-{runId}.jpg` dibuat paling lama dan `foto-21-{runId}.jpg` paling baru, dengan selisih waktu unggah minimal satu menit).
- Kondisi:
  - Selection Limit bernilai `1000`.

## Test Steps

### Default 10 baris dan opsi ukuran halaman
1. Klik tab `Asset Photo`
2. Verifikasi tabel menampilkan `10` baris pada halaman 1
3. Verifikasi Pagination menampilkan total `21` baris dalam `3` halaman
4. Buka pilihan ukuran halaman pada Pagination
5. Verifikasi pilihan ukuran halaman `10`, `25`, `50`, dan `100` tersedia
6. Pilih ukuran halaman `25`
7. Verifikasi tabel menampilkan `21` baris dalam `1` halaman
8. Pilih ukuran halaman `10`

### Select All memilih seluruh baris lintas halaman
9. Centang baris `foto-21-{runId}.jpg`
10. Verifikasi teks seleksi `1 File selected` tampil
11. Verifikasi tombol `Select All (21 records)` tampil
12. Klik `Select All (21 records)`
13. Verifikasi teks seleksi `21 Files selected` tampil
14. Verifikasi tombol berubah menjadi `Unselect All`
15. Klik halaman `2` pada Pagination
16. Verifikasi baris `foto-11-{runId}.jpg` tercentang
17. Hilangkan centang baris `foto-11-{runId}.jpg`
18. Verifikasi tombol kembali menjadi `Select All (21 records)` dengan jumlah total tetap `21`
19. Verifikasi teks seleksi `20 Files selected` tampil
20. Klik `×` pada bar seleksi untuk membatalkan seluruh seleksi

### Hapus baris terakhir di halaman terakhir pindah ke halaman terakhir yang masih ada
21. Klik halaman `3` pada Pagination
22. Verifikasi halaman 3 memuat satu baris `foto-1-{runId}.jpg`
23. Klik aksi `Delete` pada baris `foto-1-{runId}.jpg`
24. Klik `[Delete]` pada dialog Delete File
25. Verifikasi tabel pindah ke halaman `2`
26. Verifikasi Pagination menampilkan total `20` baris dalam `2` halaman
