---
id: TC-FA-FACO-UI-140-popup-used-by-dep-asset-class
title: "Popup Used By: identitas akun, daftar bullet, dan teks jumlah Asset Name"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules:
  - ST-12
  - §4.1#r3
  - §4.1.4#p1
  - §4.1.4#p2
  - §4.2d#p1
  - §4.5#b1
smoke: []
dependsOn:
  - "Asset Class: pemakaian akun pada field akun Asset Class (Used By)"
trace:
  ST-12: [2, 4, 5]
  §4.1#r3: [16, 20]
  §4.1.4#p1: [7, 8, 13, 14]
  §4.1.4#p2: [9, 10, 11, 12, 16]
  §4.2d#p1: [7, 8, 9, 10, 11]
  §4.5#b1: 24
anchor: [18, 22]
coverage:
  web: automated
---

# Popup Used By: identitas akun, daftar bullet, dan teks jumlah Asset Name

## Prerequisites
- Aktor: Total Control.
- Layar awal: Popup Used By pada Settings > Accounting > Chart of Accounts.
- Komponen: Popup Used By
- Data:
  - DU-140-1: Akun, Account Code `1-1001`, Account Name `Fixed Assets – Equipment`, Account Function `Asset Cost`, Used By `3`.
  - DU-140-2: Asset Class pemakai DU-140-1, Asset Class Name `Heavy Equipment`, Asset Name Count `12`.
  - DU-140-3: Asset Class pemakai DU-140-1, Asset Class Name `Office Equipment`, Asset Name Count `1`.
  - DU-140-4: Asset Class pemakai DU-140-1, Asset Class Name `Vehicles`, Asset Name Count `0`.
  - Jumlah yang diharapkan pada identitas akun `3`, dari 3 Asset Class pemakai (DU-140-2 sampai DU-140-4)
  - Teks jumlah yang diharapkan `12 Asset Names`, `1 Asset Name`, dan `0 Asset Names`, dari Asset Name Count DU-140-2 sampai DU-140-4
- Kondisi:
  - K1: Popup Used By akun DU-140-1 terbuka dan daftar pemakai berisi DU-140-2 sampai DU-140-4
  - K2: Popup Used By akun DU-140-1 terbuka dan daftar pemakai DU-140-2 sampai DU-140-4 belum selesai dimuat karena respons lambat

## Test Steps

### Popup memuat daftar pemakai
1. Tampilkan Popup Used By dengan kondisi K2
2. Verifikasi konten popup Used By ditandai sedang dimuat sebelum daftar pemakai tiba
3. Daftar pemakai selesai dimuat
4. Verifikasi daftar bullet pemakai tampil pada popup Used By
5. Verifikasi penanda sedang dimuat pada konten popup Used By sudah tidak ada

### Isi popup Used By
6. Tampilkan Popup Used By dengan kondisi K1
7. Verifikasi judul popup `Used By` tampil
8. Verifikasi Account Code `1-1001`, Account Name `Fixed Assets – Equipment`, dan jumlah `3` tampil sebagai identitas akun pada popup
9. Verifikasi Asset Class `Heavy Equipment` tampil pada daftar pemakai bersama teks jumlah `12 Asset Names`
10. Verifikasi Asset Class `Office Equipment` tampil pada daftar pemakai bersama teks jumlah `1 Asset Name`
11. Verifikasi Asset Class `Vehicles` tampil pada daftar pemakai bersama teks jumlah `0 Asset Names`
12. Verifikasi popup tidak memuat toolbar, kolom, maupun tabel
13. Verifikasi ikon close `✕` tampil pada popup
14. Verifikasi popup tidak memiliki tombol teks `Close`
15. Klik Asset Class `Heavy Equipment` pada daftar pemakai
16. Verifikasi popup tetap menampilkan daftar bullet yang sama dan tidak ada aksi apa pun yang terpicu

### Popup ditutup lewat ikon close
17. Tampilkan Popup Used By dengan kondisi K1
18. Verifikasi judul popup `Used By` tampil
19. Klik ikon close `✕` pada popup
20. Verifikasi popup Used By tidak tampil lagi

### Popup ditutup lewat Esc
21. Tampilkan Popup Used By dengan kondisi K1
22. Verifikasi judul popup `Used By` tampil
23. Tekan `Esc`
24. Verifikasi popup Used By tidak tampil lagi
