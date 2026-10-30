---
id: TC-GS-TAG-E2E-002-isi-sel-registri-ikon-tipe-code-badge-dan-popup-combined
title: "Isi Sel Registri: Ikon TAG Type, Code dan Popup Combined TAG, Teks Polos, Badge Brand/Model, Badge Status, Last Scanned, dan Kolom Curated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-5
  - TC-GS-TAG-6
  - TC-GS-TAG-7
  - TC-GS-TAG-8
  - TC-GS-TAG-9
  - TC-GS-TAG-10
  - TC-GS-TAG-11
  - TC-GS-TAG-378
coverage:
  web: automated
---

# Isi Sel Registri: Ikon TAG Type, Code dan Popup Combined TAG, Teks Polos, Badge Brand/Model, Badge Status, Last Scanned, dan Kolom Curated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca): Seed Registri A (DD-01 s.d. DD-14 dipakai langkah; DD-15 s.d. DD-30 filler). Khusus TC-GS-TAG-378: fixture BE di luar hitungan Seed Registri A, DD-60 (RFID `E2801160600002054D8A0060`, `Official`, Available) combined dengan DD-61 (NFC `04A224B2C15E90`, `Self-Purchased`, Available); disisipkan dan dibersihkan oleh hook `before` dan `after` spec ini. Combined: DD-11 (RFID `E2801160600002054D8A0011`) dengan DD-13 (NFC `04A224B2C15E83`); DD-10 (NFC `04A224B2C15E82`) dengan DD-14 (QR `TAG-QR-00611`). Format tanggal default General Settings Client A (`dd/MM/yy`, 24-hour). Seed di-seed ulang idempotent oleh hook `before` (Q-4); mekanisme disediakan tim FE/BE.
- Layar awal: Global Settings > TAG Tab All dibuka di hook `beforeEach`.
- Guided Tooltip: flag `guided_tooltip_seen_gs-tag-registry` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- State global: spec mengubah preferensi Setup Column akun Total Control (kolom curated dicentang pada TC-11); dipulihkan lewat langkah 102 (`[Reset to Default]`) dan hook `after` sebagai cadangan. Suite berjalan serial (`parallel: false`).
- Selektor: ikon 🔗, badge, dan sel belum punya ID di sumber (hanya target Guided Tooltip); diselesaikan tim FE di tahap script.

## Test Steps

### TC-GS-TAG-5: Kolom TAG Type tampil sebagai ikon dengan accessibility label saat hover

1. Hover ikon TAG Type baris `E2801160600002054D8A0001`
2. Verifikasi baris DD-01 menampilkan ikon, bukan teks
3. Verifikasi hover DD-01 menampilkan label `RFID`
4. Hover ikon TAG Type baris `04A224B2C15E80`
5. Verifikasi baris DD-03 menampilkan ikon, bukan teks
6. Verifikasi hover DD-03 menampilkan label `NFC`
7. Hover ikon TAG Type baris `AABBCCDDEE80`
8. Verifikasi baris DD-04 menampilkan ikon, bukan teks
9. Verifikasi hover DD-04 menampilkan label `BLE`
10. Hover ikon TAG Type baris `356938035643501`
11. Verifikasi baris DD-09 menampilkan ikon, bukan teks
12. Verifikasi hover DD-09 menampilkan label `GPS`
13. Hover ikon TAG Type baris `TAG-QR-00512`
14. Verifikasi baris DD-05 menampilkan ikon, bukan teks
15. Verifikasi hover DD-05 menampilkan label `QR`
16. Verifikasi kolom `Type` DD-01 berisi `Object TAG`
17. Verifikasi label ikon tidak membedakan Object TAG dan User TAG

### TC-GS-TAG-6: Kolom Code tampil penuh tanpa pemotongan; ikon 🔗 pada tag combined membuka popup

18. Amati sel Code baris `E2801160600002054D8A0011`
19. Verifikasi Code `E2801160600002054D8A0011` tampil penuh 24 karakter tanpa `..`
20. Verifikasi ikon 🔗 tampil di sebelah Code baris DD-11
21. Verifikasi baris `E2801160600002054D8A0001` tidak punya ikon 🔗
22. Klik ikon 🔗 pada baris `E2801160600002054D8A0011`
23. Verifikasi Popup Combined TAG berjudul `Combined TAG` terbuka dengan baris di bawah judul `+1 More`
24. Verifikasi popup memuat kolom `TAG Type`, `Code`, `Device Name`
25. Verifikasi popup memuat tag sibling `04A224B2C15E83`
26. Verifikasi halaman registri tidak berpindah
27. Tutup popup, lalu klik ikon 🔗 pada baris `04A224B2C15E82`
28. Verifikasi Popup Combined TAG berjudul `Combined TAG` (`+1 More`) terbuka
29. Verifikasi popup memuat tag sibling QR `TAG-QR-00611`
30. Tutup popup

### TC-GS-TAG-7: Sel Device Name, SKU, Source, dan Type tampil teks polos; nilai kosong tampil —

31. Amati sel Device Name, SKU, Source, Type baris `E2801160600002054D8A0001`
32. Verifikasi DD-01: Device Name `Handheld Scanner X1`
33. Verifikasi DD-01: SKU `SKU-8821`
34. Verifikasi DD-01: Source `Official`
35. Verifikasi DD-01: Type `Object TAG`
36. Amati baris `E2801160600002054D8A0002`
37. Verifikasi DD-02: Device Name `Alien H3 Tag`
38. Verifikasi DD-02: SKU `—`
39. Verifikasi DD-02: Source `Self-Purchased`
40. Verifikasi DD-02: Type `User TAG`
41. Amati baris `04A224B2C15E82`
42. Verifikasi DD-10 (NFC): Type `—`
43. Amati baris `TAG-QR-00512`
44. Verifikasi DD-05 (QR): Device Name `—`
45. Verifikasi DD-05 (QR): SKU `—`
46. Verifikasi DD-05 (QR): Source `Official`
47. Verifikasi DD-05 (QR): Type `—`
48. Verifikasi nilai kosong tidak pernah tampil sebagai kosong, `null`, atau `-`

### TC-GS-TAG-8: Kolom Brand dan Model/Type tampil sebagai badge dark; nama dipotong 12+..+12

49. Amati sel Brand dan Model/Type baris `E2801160600002054D8A0001`
50. Verifikasi DD-01: badge Brand `Zebra` tampil penuh dengan severity dark
51. Verifikasi DD-01: badge Model/Type `ZT410` tampil penuh dengan severity dark
52. Amati sel Brand dan Model/Type baris `E2801160600002054D8A0012`
53. Verifikasi DD-12: badge Brand tampil `Internationa..tion Systems`
54. Verifikasi DD-12: badge Model/Type tampil `Enterprise S..Range Reader`
55. Hover badge Brand baris `E2801160600002054D8A0012`
56. Verifikasi tooltip `International Telecommunication Systems`
57. Hover badge Model/Type baris `E2801160600002054D8A0012`
58. Verifikasi tooltip `Enterprise Series 9000 Long Range Reader`
59. Hover badge Brand baris `E2801160600002054D8A0001`
60. Verifikasi tooltip `Zebra`

### TC-GS-TAG-9: Badge Status memakai severity sesuai nilai

61. Amati badge Status baris DD-01 (Paired), DD-02 (Available), DD-03 (Waiting for Approval), DD-04 (Damaged/Missing), DD-06 (Reserved), DD-07 (To be Returned), DD-08 (Retired)
62. Verifikasi badge Paired severity info
63. Verifikasi badge Available severity success
64. Verifikasi badge Waiting for Approval severity warning
65. Verifikasi badge Damaged/Missing severity danger
66. Verifikasi badge Reserved severity secondary
67. Verifikasi badge To be Returned severity warning
68. Verifikasi badge Retired severity dark
69. Verifikasi kolom Status tidak pernah kosong

### TC-GS-TAG-10: Kolom Last Scanned tampil mengikuti General Settings; belum pernah dipindai tampil —

70. Amati sel Last Scanned baris DD-01
71. Verifikasi DD-01 tampil `16/09/26 14:30`
72. Amati sel Last Scanned baris DD-03 dan DD-05
73. Verifikasi DD-03 tampil `—`
74. Verifikasi DD-05 tampil `—`

### TC-GS-TAG-378: Popup Combined TAG memuat sibling berbeda Source (Official dan Self-Purchased)

75. Amati sel Source baris `E2801160600002054D8A0060` dan baris `04A224B2C15E90`
76. Verifikasi DD-60 Source `Official`
77. Verifikasi DD-61 Source `Self-Purchased`
78. Verifikasi baris DD-60 dan DD-61 menampilkan ikon 🔗
79. Klik ikon 🔗 pada baris `E2801160600002054D8A0060`
80. Verifikasi Popup Combined TAG memuat sibling NFC `04A224B2C15E90`
81. Tutup popup, lalu klik ikon 🔗 pada baris `04A224B2C15E90`
82. Verifikasi Popup Combined TAG memuat sibling RFID `E2801160600002054D8A0060`
83. Verifikasi tidak ada pesan atau penanda yang menyatakan perbedaan Source sebagai penghalang combined
84. Tutup popup

### TC-GS-TAG-11: Kolom curated default Hidden dan tampil setelah dicentang di Setup Column

85. Buka overlay Column Visibility lalu klik `Setup Column`
86. Centang `Last Scanned In`, `Activated At`, `Last User`
87. Klik `[Save]`
88. Amati sel baris DD-01
89. Verifikasi DD-01: badge Last Scanned In `Fixed Asset` severity info
90. Verifikasi DD-01: Activated At `10/09/26 08:00`
91. Verifikasi DD-01: Last User `Budi S` plain text
92. Amati sel baris DD-02
93. Hover badge Last Scanned In baris DD-02
94. Verifikasi DD-02: badge `Global Settings` severity secondary
95. Verifikasi hover badge menampilkan path menu lengkap tempat pemindaian terakhir
96. Amati sel baris DD-03
97. Verifikasi DD-03: Last Scanned In `—`
98. Verifikasi DD-03: Last User `—`
99. Verifikasi DD-03: Activated At `15/09/26 13:00`
100. Hover sel Last User baris DD-01
101. Verifikasi tooltip nama lengkap `Budi Santoso`
102. Buka overlay Column Visibility, klik `Setup Column`, klik `[Reset to Default]`, lalu klik `[Save]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md` (Section 1b). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 102 adalah langkah penghubung pemulihan preferensi Setup Column (aksi tanpa `Verifikasi`, S-03, S-09). Kolom curated Hidden default sehingga `[Reset to Default]` mengembalikannya; hook `after` sebagai cadangan.
- Langkah penghubung lain (tanpa `Verifikasi`, S-03): langkah 27 (menutup popup pertama lalu membuka popup kedua, langkah 4 TC-6) dan langkah 30 (menutup popup sebelum blok TC-7; tidak ada di TC-6). Langkah 81 (menutup popup pertama lalu membuka popup kedua, langkah 3 TC-378) dan langkah 84 (menutup popup sebelum blok TC-11) juga langkah penghubung tanpa `Verifikasi`. Langkah hover pada blok TC-5 (langkah 1, 4, 7, 10, 13) diulang per baris data sesuai langkah 1 sampai 5 TC-5, dan setiap hover diikuti `Verifikasi` label.
- Alasan spec melewati sekitar 35 langkah (92 nominal): tujuh TC baca-saja atas satu dataset (Seed Registri A), tanpa kelas harness khusus; tiap blok berdiri sendiri dan tidak bergantung pada hasil blok lain, kecuali TC-11 yang mengubah Setup Column dan ditaruh terakhir. Langkah hover dan asersi diulang per baris data (lima baris ikon, tujuh Status) sehingga jumlah nominal besar tanpa langkah bersyarat.
- Rujukan lintas spec: perilaku Setup Column secara penuh (hide/show, reorder, persistensi) ada di spec 076; TC-11 di sini hanya langkah penghubung untuk menampilkan kolom curated.
- Temuan untuk QA:
  - TC-9 butir a-g menyebut severity badge tanpa cara teramati di UI (nama kelas CSS atau warna); spec mengasersi severity sebagaimana TC dan tim FE menetapkan cara pembacaannya di tahap script (S-13).
  - TC-9 mencakup tujuh dari delapan nilai Status; Status lain tidak ada di TC.
  - TC-11 butir b ("path menu lengkap") tidak menyebut teks path-nya; spec hanya mengasersi tooltip tampil dengan path menu lengkap tanpa nilai literal.
  - TC-11 tidak menyatakan keadaan awal Setup Column Total Control Client A; spec mengasumsikan default (curated Hidden) dari hook `before`.
  - TC-378 tidak menyatakan apakah ikon 🔗 muncul pada tag combined berbeda Source selain lewat Expected a; spec mengasersi ikon tampil pada kedua baris (langkah 78).
  - Post Condition semua TC bernilai `-`.
