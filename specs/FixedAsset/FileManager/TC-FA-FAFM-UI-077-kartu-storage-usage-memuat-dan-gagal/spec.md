---
id: TC-FA-FAFM-UI-077-kartu-storage-usage-memuat-dan-gagal
title: "Kartu Storage Usage: memuat, gagal memuat, dan Try Again"
layer: ui-client
priority: High
caseType: Negative
status: ready-for-automation
sourceRules: ["ARS-07c", "ARS-07e", "ARS-08d", "ARS-08e", "F-FAFM-06.k4", "F-FAFM-06l", "INV-02e", "INV-02g", "S-08", "S-09", "V-12", "§4.4#b12"]
smoke: []
dependsOn: []
trace:
  "ARS-07c": [6, 7]
  "ARS-07e": [9, 10, 21, 22, 23, 24]
  "ARS-08d": [12, 13]
  "ARS-08e": [8]
  "F-FAFM-06.k4": [3, 4, 9, 10, 21, 22, 23, 24]
  "F-FAFM-06l": [3, 4, 9, 10, 21, 22, 23, 24]
  "INV-02e": [2]
  "INV-02g": [6, 7]
  "S-08": [2, 3, 4]
  "S-09": [6, 9, 10]
  "V-12": [6, 8]
  "§4.4#b12": [17, 18, 19]
anchor: [15]
coverage:
  web: automated
---

# Kartu Storage Usage: memuat, gagal memuat, dan Try Again

## Prerequisites
- Aktor: Total Control.
- Layar awal: Kartu Storage Usage.
- Komponen: Kartu Storage Usage.
- Data:
  - DU-077-1: Total Used `4.8 GB`, Storage Quota `50.0 GB`, Fixed Asset `3.2 GB`.
  - DU-077-2: file `laptop-front.jpg`, File Format `JPG`, Source `Asset Photo`, Reference `—`, Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Size `820.4 KB`, Uploaded By `Budi S`, Upload Date `02/11/26 14:30`.
- Kondisi:
  - K1: pemuatan kartu lambat; tabel Files berhasil dimuat dengan DU-077-2.
  - K2: pemuatan kartu gagal karena error server; tabel Files berhasil dimuat dengan DU-077-2.
  - K3: pemuatan kartu lambat lalu gagal karena error server.
  - K4: pemuatan kartu gagal karena error server; pemuatan ulang berikutnya berhasil dengan DU-077-1.
  - K5: pemuatan kartu berhasil dengan DU-077-1; pemuatan tabel Files gagal karena error server.

## Test Steps

### Kartu sedang dimuat dan tabel dimuat mandiri
1. Tampilkan Kartu Storage Usage dengan kondisi K1
2. Verifikasi kartu ditandai sedang dimuat
3. Verifikasi tabel Files tampil dengan header kolom `File Name`
4. Verifikasi tabel Files tidak ditandai sedang dimuat

### Kartu gagal memuat dan tabel tidak terpengaruh
5. Tampilkan Kartu Storage Usage dengan kondisi K2
6. Verifikasi `Unable to load this data.` tampil di dalam kartu
7. Verifikasi tombol `[Try Again]` tampil di dalam kartu
8. Verifikasi tidak ada toast error yang tampil
9. Verifikasi tabel Files tampil dengan header kolom `File Name`
10. Verifikasi tabel Files tidak menampilkan state gagal memuat

### Keadaan memuat digantikan state gagal
11. Tampilkan Kartu Storage Usage dengan kondisi K3
12. Verifikasi kartu ditandai sedang dimuat sebelum respons gagal diterima
13. Verifikasi `Unable to load this data.` menggantikan keadaan memuat pada kartu

### Try Again memuat ulang kartu
14. Tampilkan Kartu Storage Usage dengan kondisi K4
15. Verifikasi `Unable to load this data.` tampil di dalam kartu
16. Klik `[Try Again]`
17. Verifikasi kartu yang dimuat ulang menampilkan `Total Used` `4.8 GB`
18. Verifikasi kartu yang dimuat ulang menampilkan `Storage Quota` `50.0 GB`
19. Verifikasi `Unable to load this data.` tidak tampil lagi pada kartu

### Tabel gagal memuat dan kartu tidak terpengaruh
20. Tampilkan Kartu Storage Usage dengan kondisi K5
21. Verifikasi kartu menampilkan `Total Used` `4.8 GB`
22. Verifikasi kartu menampilkan `Storage Quota` `50.0 GB`
23. Verifikasi tabel Files menampilkan `Unable to load this data.`
24. Verifikasi `Unable to load this data.` tidak tampil di dalam kartu
