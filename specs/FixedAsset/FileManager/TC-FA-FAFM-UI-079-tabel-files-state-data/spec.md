---
id: TC-FA-FAFM-UI-079-tabel-files-state-data
title: "Tabel Files: loading, kosong, kosong tersaring, dan gagal muat"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["S-01", "S-02", "S-06", "S-07", "S-17", "S-26a", "S-26b", "§7.1#p1", "EB-TBL-1@tabel-files"]
smoke: []
dependsOn: []
trace:
  "S-01": [2, 3]
  "S-02": [5, 6, 11, 12, 15, 17, 18, 19]
  "S-06": [24, 25, 29, 30]
  "S-07": [33, 34]
  "S-17": [33, 34]
  "S-26a": [5, 6, 11, 12, 17, 18]
  "S-26b": [24, 25, 29, 30]
  "§7.1#p1": [5, 6, 24, 25]
  "EB-TBL-1@tabel-files": [3, 5, 6, 7, 8, 9, 11, 12, 13, 17, 18, 20, 24, 25, 26, 27, 29, 30, 31, 33, 34, 35, 36]
anchor: []
coverage:
  web: automated
---

# Tabel Files: loading, kosong, kosong tersaring, dan gagal muat

## Prerequisites
- Aktor: Total Control (K1, K2, K4, K5, K6, K7); Group Manager atas group `Head Office` (K3).
- Layar awal: Tabel File Manager tab Files.
- Komponen: Tabel File Manager tab Files.
- Data:
  - DU-079-1: `laptop-front.jpg`, JPG, Source Asset Photo, Reference `—`, Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Size `820.4 KB`, Uploaded By `Budi S`, Upload Date `02/11/26 14:30`.
  - DU-079-2: `warranty-card-lpt0004.pdf`, PDF, Source Attachment, Reference `General`, Asset `Laptop Dell Latitude 5420 - 4`, Asset ID `LPT-2026-0004`, Group `Head Office`, Size `310.0 KB`, Uploaded By `Rina A`, Upload Date `28/10/26 09:00`.
  - DU-079-3: `handover-brw0148.jpg`, JPG, Source Handover Photo, Reference `BRW-2026-0148`, Asset `Laptop Dell Latitude 5420 - 9`, Asset ID `LPT-2026-0009`, Group `Head Office`, Size `640.0 KB`, Uploaded By `Dodi P`, Upload Date `03/11/26 09:00`.
  - DU-079-4: akun tanpa satu pun file aktif.
  - DU-079-5: `warranty-card-scn0003.pdf`, PDF, Source Custom Field Document, Reference `Warranty Card`, Asset `Scanner Epson DS-530 - 3`, Asset ID `SCN-2026-0003`, Group `Branch Bandung`, Size `300.0 KB`, Uploaded By `Rina A`, Upload Date `20/10/26 08:45`.
- Kondisi:
  - K1: pemuatan data tabel lambat; belum ada respons.
  - K2: server mengembalikan daftar kosong untuk akun; data DU-079-4.
  - K3: server mengembalikan daftar kosong untuk aktor karena satu-satunya file akun, DU-079-5, berada di group `Branch Bandung` di luar scope aktor.
  - K4: tabel berisi DU-079-1; setelah file itu dihapus, server mengembalikan daftar kosong.
  - K5: tabel berisi DU-079-1 dan DU-079-2; pencarian `invoice-lpt0004.pdf` tidak cocok dengan baris mana pun.
  - K6: Filter Panel sudah menerapkan File Format `PDF`; tabel semula berisi DU-079-1 dan DU-079-3 yang keduanya berformat JPG, sehingga tidak ada baris yang cocok.
  - K7: pemuatan data tabel gagal karena error server.

## Test Steps

### Tabel sedang dimuat
1. Tampilkan Tabel File Manager tab Files dengan kondisi K1
2. Verifikasi tabel Files ditandai sedang dimuat
3. Verifikasi `No files yet` tidak tampil

### Belum ada file sama sekali
4. Tampilkan Tabel File Manager tab Files dengan kondisi K2
5. Verifikasi judul `No files yet` tampil
6. Verifikasi deskripsi `Photos and documents will appear here once they are uploaded to assets.` tampil
7. Verifikasi empty state tidak memuat tombol aksi
8. Verifikasi `Unable to load this data.` tidak tampil
9. Verifikasi `No results found` tidak tampil

### Ada file di akun, tetapi tidak ada di scope aktor
10. Tampilkan Tabel File Manager tab Files dengan kondisi K3
11. Verifikasi judul `No files yet` tampil
12. Verifikasi deskripsi `Photos and documents will appear here once they are uploaded to assets.` tampil
13. Verifikasi `No results found` tidak tampil

### Daftar menjadi kosong setelah file terakhir dihapus
14. Tampilkan Tabel File Manager tab Files dengan kondisi K4
15. Verifikasi baris `laptop-front.jpg` tampil
16. Perbarui data tabel menjadi tanpa file setelah `laptop-front.jpg` dihapus
17. Verifikasi judul `No files yet` tampil
18. Verifikasi deskripsi `Photos and documents will appear here once they are uploaded to assets.` tampil
19. Verifikasi baris `laptop-front.jpg` tidak tampil
20. Verifikasi `No results found` tidak tampil

### Search tanpa hasil
21. Tampilkan Tabel File Manager tab Files dengan kondisi K5
22. Isi kotak Search dengan `invoice-lpt0004.pdf`
23. Tekan Enter pada kotak Search
24. Verifikasi judul `No results found` tampil
25. Verifikasi deskripsi `Try adjusting your search or filter.` tampil
26. Verifikasi empty state tidak memuat tombol aksi
27. Verifikasi `No files yet` tidak tampil

### Filter tanpa hasil
28. Tampilkan Tabel File Manager tab Files dengan kondisi K6
29. Verifikasi judul `No results found` tampil
30. Verifikasi deskripsi `Try adjusting your search or filter.` tampil
31. Verifikasi `No files yet` tidak tampil

### Gagal memuat
32. Tampilkan Tabel File Manager tab Files dengan kondisi K7
33. Verifikasi `Unable to load this data.` tampil
34. Verifikasi tombol `[Try Again]` tampil
35. Verifikasi `No files yet` tidak tampil
36. Verifikasi `No results found` tidak tampil
