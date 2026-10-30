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
- State global: spec mengubah preferensi Setup Column akun Total Control (kolom curated dicentang pada TC-11); dipulihkan lewat langkah 104 (hapus preferensi kolom di browser) dan hook `after` sebagai cadangan. Kemampuan menghapus preferensi kolom di browser disediakan tim FE. Spec juga mengubah Rows per page menjadi 50 (langkah 1) dan memulihkannya ke 10 pada langkah 103 dan hook `after`. Suite berjalan serial (`parallel: false`).
- Selektor: ikon 🔗, badge, dan sel belum punya ID di sumber (hanya target Guided Tooltip); diselesaikan tim FE di tahap script.

## Test Steps

### Persiapan tampilan

1. Ubah Rows per page menjadi 50 (seluruh baris Seed Registri A dan DD-60, DD-61 tampil pada satu halaman)

### TC-GS-TAG-5: Kolom TAG Type tampil sebagai ikon dengan accessibility label saat hover

2. Hover ikon TAG Type baris `E2801160600002054D8A0001`
3. Verifikasi baris DD-01 menampilkan ikon, bukan teks
4. Verifikasi hover DD-01 menampilkan label `RFID`
5. Hover ikon TAG Type baris `04A224B2C15E80`
6. Verifikasi baris DD-03 menampilkan ikon, bukan teks
7. Verifikasi hover DD-03 menampilkan label `NFC`
8. Hover ikon TAG Type baris `AABBCCDDEE80`
9. Verifikasi baris DD-04 menampilkan ikon, bukan teks
10. Verifikasi hover DD-04 menampilkan label `BLE`
11. Hover ikon TAG Type baris `356938035643501`
12. Verifikasi baris DD-09 menampilkan ikon, bukan teks
13. Verifikasi hover DD-09 menampilkan label `GPS`
14. Hover ikon TAG Type baris `TAG-QR-00512`
15. Verifikasi baris DD-05 menampilkan ikon, bukan teks
16. Verifikasi hover DD-05 menampilkan label `QR`
17. Verifikasi kolom `Type` DD-01 berisi `Object TAG`
18. Verifikasi label ikon tidak membedakan Object TAG dan User TAG

### TC-GS-TAG-6: Kolom Code tampil penuh tanpa pemotongan; ikon 🔗 pada tag combined membuka popup

19. Amati sel Code baris `E2801160600002054D8A0011`
20. Verifikasi Code `E2801160600002054D8A0011` tampil penuh 24 karakter tanpa `..`
21. Verifikasi ikon 🔗 tampil di sebelah Code baris DD-11
22. Verifikasi baris `E2801160600002054D8A0001` tidak punya ikon 🔗
23. Klik ikon 🔗 pada baris `E2801160600002054D8A0011`
24. Verifikasi Popup Combined TAG berjudul `Combined TAG` terbuka dengan baris di bawah judul `+1 More`
25. Verifikasi popup memuat kolom `TAG Type`, `Code`, `Device Name`
26. Verifikasi popup memuat tag sibling `04A224B2C15E83`
27. Verifikasi halaman registri tidak berpindah
28. Tutup popup, lalu klik ikon 🔗 pada baris `04A224B2C15E82`
29. Verifikasi Popup Combined TAG berjudul `Combined TAG` (`+1 More`) terbuka
30. Verifikasi popup memuat tag sibling QR `TAG-QR-00611`
31. Tutup popup

### TC-GS-TAG-7: Sel Device Name, SKU, Source, dan Type tampil teks polos; nilai kosong tampil —

32. Amati sel Device Name, SKU, Source, Type baris `E2801160600002054D8A0001`
33. Verifikasi DD-01: Device Name `Handheld Scanner X1`
34. Verifikasi DD-01: SKU `SKU-8821`
35. Verifikasi DD-01: Source `Official`
36. Verifikasi DD-01: Type `Object TAG`
37. Amati baris `E2801160600002054D8A0002`
38. Verifikasi DD-02: Device Name `Alien H3 Tag`
39. Verifikasi DD-02: SKU `—`
40. Verifikasi DD-02: Source `Self-Purchased`
41. Verifikasi DD-02: Type `User TAG`
42. Amati baris `04A224B2C15E82`
43. Verifikasi DD-10 (NFC): Type `—`
44. Amati baris `TAG-QR-00512`
45. Verifikasi DD-05 (QR): Device Name `—`
46. Verifikasi DD-05 (QR): SKU `—`
47. Verifikasi DD-05 (QR): Source `Official`
48. Verifikasi DD-05 (QR): Type `—`
49. Verifikasi nilai kosong tidak pernah tampil sebagai kosong, `null`, atau `-`

### TC-GS-TAG-8: Kolom Brand dan Model/Type tampil sebagai badge dark; nama dipotong 12+..+12

50. Amati sel Brand dan Model/Type baris `E2801160600002054D8A0001`
51. Verifikasi DD-01: badge Brand `Zebra` tampil penuh dengan severity dark
52. Verifikasi DD-01: badge Model/Type `ZT410` tampil penuh dengan severity dark
53. Amati sel Brand dan Model/Type baris `E2801160600002054D8A0012`
54. Verifikasi DD-12: badge Brand tampil `Internationa..tion Systems`
55. Verifikasi DD-12: badge Model/Type tampil `Enterprise S..Range Reader`
56. Hover badge Brand baris `E2801160600002054D8A0012`
57. Verifikasi tooltip `International Telecommunication Systems`
58. Hover badge Model/Type baris `E2801160600002054D8A0012`
59. Verifikasi tooltip `Enterprise Series 9000 Long Range Reader`
60. Hover badge Brand baris `E2801160600002054D8A0001`
61. Verifikasi tooltip `Zebra`

### TC-GS-TAG-9: Badge Status memakai severity sesuai nilai

62. Amati badge Status baris DD-01 (Paired), DD-02 (Available), DD-03 (Waiting for Approval), DD-04 (Damaged/Missing), DD-06 (Reserved), DD-07 (To be Returned), DD-08 (Retired)
63. Verifikasi badge Paired severity info
64. Verifikasi badge Available severity success
65. Verifikasi badge Waiting for Approval severity warning
66. Verifikasi badge Damaged/Missing severity danger
67. Verifikasi badge Reserved severity secondary
68. Verifikasi badge To be Returned severity warning
69. Verifikasi badge Retired severity dark
70. Verifikasi kolom Status tidak pernah kosong

### TC-GS-TAG-10: Kolom Last Scanned tampil mengikuti General Settings; belum pernah dipindai tampil —

71. Amati sel Last Scanned baris DD-01
72. Verifikasi DD-01 tampil `16/09/26 14:30`
73. Amati sel Last Scanned baris DD-03 dan DD-05
74. Verifikasi DD-03 tampil `—`
75. Verifikasi DD-05 tampil `—`

### TC-GS-TAG-378: Popup Combined TAG memuat sibling berbeda Source (Official dan Self-Purchased)

76. Amati sel Source baris `E2801160600002054D8A0060` dan baris `04A224B2C15E90`
77. Verifikasi DD-60 Source `Official`
78. Verifikasi DD-61 Source `Self-Purchased`
79. Verifikasi baris DD-60 dan DD-61 menampilkan ikon 🔗
80. Klik ikon 🔗 pada baris `E2801160600002054D8A0060`
81. Verifikasi Popup Combined TAG memuat sibling NFC `04A224B2C15E90`
82. Tutup popup, lalu klik ikon 🔗 pada baris `04A224B2C15E90`
83. Verifikasi Popup Combined TAG memuat sibling RFID `E2801160600002054D8A0060`
84. Verifikasi tidak ada pesan atau penanda yang menyatakan perbedaan Source sebagai penghalang combined
85. Tutup popup

### TC-GS-TAG-11: Kolom curated default Hidden dan tampil setelah dicentang di Setup Column

86. Buka overlay Column Visibility lalu klik `Setup Column`
87. Centang `Last Scanned In`, `Activated At`, `Last User`
88. Klik `[Save]`
89. Amati sel baris DD-01
90. Verifikasi DD-01: badge Last Scanned In `Fixed Asset` severity info
91. Verifikasi DD-01: Activated At `10/09/26 08:00`
92. Verifikasi DD-01: Last User `Budi S` plain text
93. Amati sel baris DD-02
94. Hover badge Last Scanned In baris DD-02
95. Verifikasi DD-02: badge `Global Settings` severity secondary
96. Verifikasi hover badge menampilkan path menu lengkap tempat pemindaian terakhir
97. Amati sel baris DD-03
98. Verifikasi DD-03: Last Scanned In `—`
99. Verifikasi DD-03: Last User `—`
100. Verifikasi DD-03: Activated At `15/09/26 13:00`
101. Hover sel Last User baris DD-01
102. Verifikasi tooltip nama lengkap `Budi Santoso`
103. Ubah Rows per page kembali menjadi 10
104. Hapus preferensi kolom di browser (kemampuan disediakan tim FE)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md` (Section 1b). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah 104 adalah langkah penghubung pemulihan preferensi Setup Column (aksi tanpa `Verifikasi`, S-03, S-09). Penghapusan preferensi kolom mengembalikan kolom curated ke Hidden default; hook `after` sebagai cadangan.
- Langkah 1 dan 103 adalah langkah penghubung (aksi tanpa `Verifikasi`, S-03): Rows per page 50 supaya baris di luar halaman 1 terjangkau tanpa pindah halaman, lalu dipulihkan ke 10. Urutan default Code A-Z dengan 10 baris per halaman menempatkan DD-05 (`TAG-QR-00512`), DD-11, DD-12, DD-60, dan DD-61 di halaman 2 atau berikutnya (TC-1, TC-4); seluruh baris (30 Seed Registri A ditambah DD-60 dan DD-61) tampil pada satu halaman dengan 50 baris per halaman.
- Langkah penghubung lain (tanpa `Verifikasi`, S-03): langkah 28 (menutup popup pertama lalu membuka popup kedua, langkah 4 TC-6) dan langkah 31 (menutup popup sebelum blok TC-7; tidak ada di TC-6). Langkah 82 (menutup popup pertama lalu membuka popup kedua, langkah 3 TC-378) dan langkah 85 (menutup popup sebelum blok TC-11) juga langkah penghubung tanpa `Verifikasi`. Langkah hover pada blok TC-5 (langkah 2, 5, 8, 11, 14) diulang per baris data sesuai langkah 1 sampai 5 TC-5, dan setiap hover diikuti `Verifikasi` label.
- Alasan spec melewati sekitar 35 langkah (104 nominal): tujuh TC baca-saja atas satu dataset (Seed Registri A), tanpa kelas harness khusus; tiap blok berdiri sendiri dan tidak bergantung pada hasil blok lain, kecuali TC-11 yang mengubah Setup Column dan ditaruh terakhir. Langkah hover dan asersi diulang per baris data (lima baris ikon, tujuh Status) sehingga jumlah nominal besar tanpa langkah bersyarat.
- Rujukan lintas spec: perilaku Setup Column secara penuh (hide/show, reorder, persistensi) ada di spec 076; TC-11 di sini hanya langkah penghubung untuk menampilkan kolom curated.
- Temuan untuk QA:
  - TC-9 butir a-g menyebut severity badge tanpa cara teramati di UI (nama kelas CSS atau warna); spec mengasersi severity sebagaimana TC dan tim FE menetapkan cara pembacaannya di tahap script (S-13).
  - TC-9 mencakup tujuh dari delapan nilai Status; Status lain tidak ada di TC.
  - TC-11 butir b ("path menu lengkap") tidak menyebut teks path-nya; spec hanya mengasersi tooltip tampil dengan path menu lengkap tanpa nilai literal.
  - TC-11 tidak menyatakan keadaan awal Setup Column Total Control Client A; spec mengasumsikan default (curated Hidden) dari hook `before`.
  - TC-378 tidak menyatakan apakah ikon 🔗 muncul pada tag combined berbeda Source selain lewat Expected a; spec mengasersi ikon tampil pada kedua baris (langkah 79).
  - TC-5, TC-6, TC-8, dan TC-378 memakai baris di luar halaman 1 (DD-05, DD-11, DD-12, DD-60, DD-61) tanpa menyebut cara menjangkaunya; spec menaikkan Rows per page menjadi 50 (langkah 1).
  - Post Condition semua TC bernilai `-`.
