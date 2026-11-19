---
id: TC-FA-ASTL-BE-080-cakupan-group-aset
title: "Cakupan group dan akses langsung aset"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [ASTL-LOGIC-01b, ASTL-LOGIC-01c, EC-17, F-ASTL-01.k1, "403", "§9.4.3#p2", "§9.2#p1"]
smoke: []
dependsOn: []
trace:
  ASTL-LOGIC-01b: [2, 14, 27]
  ASTL-LOGIC-01c: [16, 18]
  EC-17: [22, 25]
  F-ASTL-01.k1: [3, 6, 30]
  "403": [18, 19]
  "§9.4.3#p2": [3, 8, 12, 20]
  "§9.2#p1": [3, 8, 10, 12]
anchor: []
---

# Cakupan group dan akses langsung aset

## Prerequisites
- Aktor: Group Manager (Dewi), Total Control (Hendra), Asset Admin (Rina).
- Data:
  - DU-080-1: User `Dewi Lestari {runId}`, role Group Manager untuk group `Head Office {runId}`.
  - DU-080-2: User `Hendra Saputra {runId}`, role Total Control, cakupan seluruh client.
  - DU-080-3: Group `Head Office {runId}` dengan dua anak, `IT {runId}` dan `GA {runId}`; Group `Cabang Bandung {runId}` tanpa induk.
  - DU-080-4: Aset `Laptop Pro 16 - 1 {runId}` ber-Lifecycle `Active` di group `IT {runId}`.
  - DU-080-5: Aset `Meja Rapat - 1 {runId}` ber-Lifecycle `Active` di group `GA {runId}`.
  - DU-080-6: Aset `Proyektor X2 - 1 {runId}` ber-Lifecycle `Active` di group `Cabang Bandung {runId}`.
  - DU-080-7: Aset `Printer Laser - 1 {runId}` ber-Lifecycle `Active` di group `IT {runId}`.
  - DU-080-8: User `Rina Wijaya {runId}`, role Asset Admin (Role Transaksi) dengan node penugasan `Head Office {runId}`.

## Test Steps

### Daftar aset hanya memuat aset dalam cakupan group
1. Dewi meminta daftar aset
2. Verifikasi daftar memuat `Laptop Pro 16 - 1 {runId}` di `IT {runId}` dan `Meja Rapat - 1 {runId}` di `GA {runId}` sebagai aset descendant dari `Head Office {runId}`
3. Verifikasi daftar tidak memuat `Proyektor X2 - 1 {runId}` dan tidak mengirim data aset itu
4. Catat jumlah entri Changelog aset `Laptop Pro 16 - 1 {runId}`
5. Dewi meminta daftar aset sekali lagi
6. Verifikasi jumlah entri Changelog aset `Laptop Pro 16 - 1 {runId}` tidak berubah

### Pencarian dan Download tetap dalam cakupan
7. Dewi mencari `Proyektor X2 - 1 {runId}`
8. Verifikasi hasil pencarian tidak memuat `Proyektor X2 - 1 {runId}` dan tidak mengirim data aset itu
9. Dewi mencari `Meja Rapat - 1 {runId}`
10. Verifikasi hasil pencarian memuat `Meja Rapat - 1 {runId}`
11. Dewi mengunduh daftar aset
12. Verifikasi isi berkas Download tidak memuat `Proyektor X2 - 1 {runId}`

### Total Control mencakup seluruh client
13. Hendra meminta daftar aset
14. Verifikasi daftar memuat `Laptop Pro 16 - 1 {runId}`, `Meja Rapat - 1 {runId}`, dan `Proyektor X2 - 1 {runId}` dari ketiga group

### Akses langsung ke aset di luar cakupan ditolak
15. Dewi meminta akses langsung ke aset `Laptop Pro 16 - 1 {runId}`
16. Verifikasi akses langsung ke aset `Laptop Pro 16 - 1 {runId}` diterima karena aset ada di dalam cakupan Dewi
17. Dewi meminta akses langsung ke aset `Proyektor X2 - 1 {runId}` lewat tautan langsung
18. Verifikasi akses ke aset `Proyektor X2 - 1 {runId}` ditolak dengan pesan `You don't have permission to do this.`
19. Verifikasi penolakan itu terjadi karena aset berada di luar cakupan group Dewi, dan data aset `Proyektor X2 - 1 {runId}` tidak berubah
20. Verifikasi respons penolakan tidak memuat data aset `Proyektor X2 - 1 {runId}`

### Aset dipindahkan ke group di luar cakupan hilang dari daftar
21. Dewi meminta daftar aset
22. Verifikasi daftar memuat `Printer Laser - 1 {runId}` di group `IT {runId}`
23. Aset `Printer Laser - 1 {runId}` dipindahkan ke group `Cabang Bandung {runId}`
24. Dewi meminta daftar aset pada pemuatan berikutnya
25. Verifikasi daftar tidak memuat `Printer Laser - 1 {runId}` lagi

### Role Transaksi mencakup node penugasan beserta seluruh descendant
26. Rina meminta daftar aset
27. Verifikasi daftar memuat `Laptop Pro 16 - 1 {runId}` di `IT {runId}` dan `Meja Rapat - 1 {runId}` di `GA {runId}` sebagai descendant dari node penugasan `Head Office {runId}`, dan tidak memuat `Proyektor X2 - 1 {runId}`

### Melihat daftar tidak dicatat di log mana pun
28. Catat jumlah entri Activity Log dan System Log aset `Laptop Pro 16 - 1 {runId}`
29. Dewi meminta daftar aset
30. Verifikasi jumlah entri Activity Log dan System Log aset `Laptop Pro 16 - 1 {runId}` tidak berubah
