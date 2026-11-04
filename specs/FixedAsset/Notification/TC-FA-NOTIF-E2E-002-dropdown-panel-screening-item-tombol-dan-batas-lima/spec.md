---
id: TC-FA-NOTIF-E2E-002-dropdown-panel-screening-item-tombol-dan-batas-lima
title: "Dropdown Panel: Screening, State Item Unread dan Read, serta Batas Lima Item"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-9
  - TC-FA-NOTIF-10
  - TC-FA-NOTIF-12
  - TC-FA-NOTIF-13
  - TC-FA-NOTIF-14
  - TC-FA-NOTIF-15
  - TC-FA-NOTIF-23
coverage:
  web: automated
---

# Dropdown Panel: Screening, State Item Unread dan Read, serta Batas Lima Item

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Dropdown Panel Bell icon).
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: tiga varian seed notifikasi akun aktor (Pre-setup #17 dan #18), ditukar fixture BE penukar varian seed lewat langkah penghubung eksplisit; spec hanya membaca data:
  - varian dasar N-01 sampai N-07 (N-01 sampai N-05 Unread, N-06 dan N-07 Read; urutan teratas N-01 sampai N-05): TC-9, 12, 13, 23;
  - varian dua notifikasi terbaru Read (N-06 dan N-07 menempati urutan teratas Dropdown Panel): TC-14, 15;
  - varian N-01 sampai N-37 (37 notifikasi): TC-10.
- Fixture BE pemulih seed dijalankan di hook `before` dan `after`. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true), fixture BE pemulih dan penukar seed notifikasi.

## Test Steps

### TC-FA-NOTIF-9: Screening Dropdown Panel: Header, Body, dan item

1. Klik Bell icon
2. Verifikasi Header Dropdown Panel menampilkan judul `Notifications` dan tautan `[Show All]`
3. Verifikasi Body berlebar 380px
4. Verifikasi Body bertinggi maksimum 480px
5. Verifikasi Body memuat 5 item berurutan dari terbaru: N-01, N-02, N-03, N-04, N-05
6. Verifikasi tiap item menampilkan icon, Title (bold bila Unread), Body, dan timestamp relatif
7. Verifikasi tombol pada tiap item hanya tampil bila item Unread

### TC-FA-NOTIF-12: Item Unread view-only menampilkan tombol [Mark as Read]

8. Verifikasi item N-03 (`Asset has been repaired`) berjudul bold
9. Verifikasi item N-03 menampilkan dot
10. Verifikasi item N-03 menampilkan tombol `[Mark as Read]`
11. Verifikasi item N-03 tidak memiliki tombol `[Detail]`
12. Verifikasi icon item N-03 `checkbox-circle-line` berseverity `success`

### TC-FA-NOTIF-13: Item Unread actionable menampilkan tombol [Detail]

13. Verifikasi item N-01 (`Waiting for your approval`) berjudul bold
14. Verifikasi item N-01 menampilkan dot
15. Verifikasi item N-01 menampilkan tombol `[Detail]`
16. Verifikasi item N-01 tidak memiliki tombol `[Mark as Read]`
17. Verifikasi icon item N-01 `time-line` berseverity `primary`

### TC-FA-NOTIF-23: Dropdown Panel tidak memiliki Breadcrumb

18. Verifikasi Header Dropdown Panel menampilkan judul `Notifications` dan tautan `[Show All]`
19. Verifikasi Dropdown Panel tidak menampilkan Breadcrumb

### TC-FA-NOTIF-14 dan TC-FA-NOTIF-15: Item Read tanpa tombol

20. Klik Bell icon untuk menutup Dropdown Panel, tukar seed ke varian dua notifikasi terbaru Read lewat fixture BE penukar, lalu muat ulang halaman
21. Klik Bell icon
22. Verifikasi item N-06 (`Your request has been rejected`) berjudul tidak bold
23. Verifikasi item N-06 tanpa dot
24. Verifikasi item N-06 tidak memiliki tombol apa pun (bukan tombol disabled)
25. Verifikasi icon item N-06 `close-circle-line` berseverity `danger` tetap tampil
26. Verifikasi item N-07 (`New audit task started`) berjudul tidak bold
27. Verifikasi item N-07 tidak memiliki tombol `[Detail]`
28. Verifikasi icon item N-07 `time-line` berseverity `primary` tetap tampil

### TC-FA-NOTIF-10: Dropdown Panel hanya menampilkan 5 notifikasi terbaru (hard cap)

29. Klik Bell icon untuk menutup Dropdown Panel, tukar seed ke varian N-01 sampai N-37 lewat fixture BE penukar, lalu muat ulang halaman
30. Klik Bell icon
31. Verifikasi Dropdown Panel menampilkan tepat 5 item
32. Verifikasi notifikasi terbaru berada di atas
33. Scroll isi panel sampai akhir
34. Verifikasi item ke-6 dan seterusnya tidak termuat di panel
35. Verifikasi scroll hanya mengakomodasi tinggi isi item

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan blok: varian dasar (TC-9, 12, 13, 23), varian Read terbaru (TC-14, 15), lalu varian N-37 (TC-10) supaya penukaran seed paling sedikit; urutan menyimpang dari urutan nomor TC. TC-12, 13, dan 23 memakai Dropdown Panel yang terbuka pada langkah 1 sehingga langkah "Klik Bell icon" tiap TC itu sudah terpenuhi (mengklik lagi akan menutup panel).
- Langkah penghubung (S-03): langkah 20 dan 29 (tutup panel, tukar seed, muat ulang halaman), langkah 21 dan 30 (buka panel kembali), langkah 33 (scroll).
- Urutan asersi TC-23 menyimpang dari Expected TC: Header (butir b) lebih dulu karena menjadi anchor positif bagi asersi absence Breadcrumb (butir a; 8b butir 2).
- Asersi item Read tanpa tombol (langkah 24, 27) memakai Title item yang sama sebagai anchor positif pada surface yang sama.
- Langkah 6 dan 7 memecah Expected TC-9 butir c menjadi unsur item dan aturan tombol (S-01).
- Spec 002 hanya membaca seed Pre-setup #17 dan #18 akun #1 (varian dasar, dua Read terbaru, N-01 sampai N-37), sedangkan spec 009 mengubah N-03 menjadi Read pada seed yang sama; keduanya dibedakan per topik supaya spec ini tidak bergantung pada pemulihan seed oleh spec lain.
- Temuan untuk QA:
  - TC-10 dan TC-14/15 memakai varian seed yang berbeda pada akun yang sama (N-01 sampai N-37; N-06 dan N-07 di urutan teratas); spec menukar varian lewat fixture BE penukar karena Pre-setup tidak memisahkan akun per varian.
