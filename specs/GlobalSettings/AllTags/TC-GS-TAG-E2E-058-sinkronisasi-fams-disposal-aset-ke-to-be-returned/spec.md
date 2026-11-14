---
id: TC-GS-TAG-E2E-058-sinkronisasi-fams-disposal-aset-ke-to-be-returned
title: "Sinkronisasi FAMS Disposal: Tag RFID/NFC Menjadi To be Returned, Penerimaan, Disposal Aset Bertag QR, dan Disposal Aset dengan Tag Combined"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-298
  - TC-GS-TAG-348
  - TC-GS-TAG-349
  - TC-GS-TAG-370
  - TC-GS-TAG-379
coverage:
  web: automated
---

# Sinkronisasi FAMS Disposal: Tag RFID/NFC Menjadi To be Returned, Penerimaan, Disposal Aset Bertag QR, dan Disposal Aset dengan Tag Combined

## Prerequisites

- Mode: FE+BE (backend nyata). Spec ini mengubah status tag lewat aksi FAMS; disposal aset bertag QR (TC-GS-TAG-349) dan disposal aset dengan tag combined RFID dan QR (TC-GS-TAG-379) yang mengeluarkan tag QR dari registri dijalankan terakhir.
- Akun aktor (seluruh blok, termasuk TC-GS-TAG-379): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Pemicu (sesi API aktor, tidak diasersi): Admin FAMS (Hendra Gunawan) `famsAdmin_automated_qaTeam1@qwertysystem.net` (Pre-setup TC), kredensial `Spectra.env.FA_ADMIN_PASSWORD`: menyelesaikan disposal aset dan menerima tag lewat `Receive TAG` (pemindaian disimulasikan; D-4). Mekanisme dan endpoint tidak didefinisikan di TC, PRD, atau LLD (Q-9).
- Layar awal: hook `beforeEach` membuka Global Settings > TAG > Tab All.
- Data Pre-setup: Seed Registri A (Client A, DD-01..DD-30; kartu RFID – Object TAG `21 of 50`, NFC `3 of 30`). Baris yang dipakai: DD-01 `E2801160600002054D8A0001` (RFID Paired), DD-13 `04A224B2C15E83` (NFC; disetel Paired ke aset FAMS lewat fixture BE dengan relasi combined ke DD-11 dilepas), DD-05 `TAG-QR-00512` (QR Paired), DD-10 `04A224B2C15E82` (NFC Paired), DD-02 (Available), DD-07 `E2801160600002054D8A0007` (To be Returned), DD-08 (Retired). Identifier tetap, tidak bisa bersufiks `{runId}` (S-12, Q-4); fixture BE memulihkan kondisi awal sebelum spec dan sebelum TC-GS-TAG-298 dan 370.
- Fixture khusus TC-GS-TAG-379 (di luar hitungan Seed Registri A, disisipkan fixture BE di langkah 59, setelah blok lain agar kartu RFID – Object TAG blok sebelumnya tidak berubah): DD-62 RFID `E2801160600002054D8A0062` dan DD-63 QR `TAG-QR-00620`, keduanya Paired ke Asset Z yang sama dan berelasi combined.
- Sesi API aktor (kemampuan dinyatakan di `suite.md`): Admin FAMS menyelesaikan disposal dan menerima tag lewat `Receive TAG`.
- Kemampuan teknis (disediakan tim FE/BE): sesi API FAMS untuk menyelesaikan disposal aset dan Receive TAG; penanda event selesai diproses (Eventual/SSE); pembacaan relasi aset sebuah tag (untuk asersi "tidak tertaut ke aset"; kolom registri yang menampilkannya tidak dinamai TC); seed dan reset idempotent Seed Registri A.
- Pemulihan di hook `after` (tidak berasumsi seeding berhasil penuh): kembalikan Seed Registri A (DD-01, DD-05, DD-13), hapus fixture DD-62 dan DD-63, pulihkan aset FAMS lewat fixture BE, dan kembalikan Rows per page ke 10.
- Suite serial (`parallel: false`). Spec tidak mengubah state global selain data registri dan sesi akun.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-tag-registry` dan `guided_tooltip_seen_gs-tag-activate`, lihat `suite.md`.

## Test Steps

### TC-GS-TAG-348: Disposal tag RFID, satu entri TAG Log

1. Buka menu baris DD-01, klik `TAG Log`, catat jumlah entri, lalu tutup popup
2. Selesaikan disposal aset bertag DD-01 di FAMS lewat sesi API Admin FAMS hingga selesai dan event diproses
3. Verifikasi status DD-01 `To be Returned` tanpa muat ulang
4. Verifikasi DD-01 tidak tertaut ke aset
5. Verifikasi status DD-01 bukan `Available` dan bukan `Retired`
6. Buka menu baris DD-01, lalu klik `TAG Log`
7. Verifikasi satu entri baru `TAG Marked To be Returned by [pelaku disposal]` dengan `Reason: Disposal` (jumlah entri bertambah satu dari nilai yang dicatat)
8. Verifikasi tidak ada entri `Unpaired` Reason `Disposal` maupun `Retired`
9. Tutup popup TAG Log
10. Verifikasi kartu RFID – Object TAG tetap `21 of 50`

### TC-GS-TAG-298: Disposal lalu penerimaan (Receive TAG)

11. Pulihkan DD-01 menjadi Paired ke aset lewat fixture BE, muat ulang halaman, lalu klik Tab Paired
12. Verifikasi DD-10 tampil di Tab Paired
13. Selesaikan disposal aset bertag DD-01 di FAMS lewat sesi API Admin FAMS hingga selesai dan event diproses
14. Verifikasi baris DD-01 tidak lagi di Tab Paired
15. Klik Tab Not Paired
16. Verifikasi DD-01 tampil di Tab Not Paired
17. Verifikasi status DD-01 `To be Returned` (badge warning)
18. Buka menu baris DD-01, lalu klik `TAG Log`
19. Verifikasi entri `TAG Marked To be Returned by [pelaku disposal]` dengan `Reason: Disposal` dan `Return Group`
20. Verifikasi tidak ada entri `Unpaired` maupun `Retired`
21. Tutup popup TAG Log
22. Terima tag DD-01 lewat `Receive TAG` (pemindaian) di FAMS lewat sesi API Admin FAMS hingga selesai dan event diproses
23. Verifikasi status DD-01 `Available`
24. Buka menu baris DD-01, lalu klik `TAG Log`
25. Verifikasi entri `TAG Received by [pelaku user FAMS yang menerima]` dengan `Previous Status: To be Returned → Available`
26. Verifikasi entri itu memuat `Return Group` group tujuan pengembalian yang menerima tag
27. Verifikasi tidak ada entri `Unpaired` Reason `Returned`
28. Tutup popup TAG Log

### TC-GS-TAG-370: Disposal aset bertag NFC

29. Atur DD-13 menjadi Paired ke aset FAMS (relasi combined dengan DD-11 dilepas) lewat fixture BE, muat ulang halaman, lalu klik Tab Paired
30. Buka menu baris DD-13, klik `TAG Log`, catat jumlah entri, lalu tutup popup
31. Verifikasi DD-10 tampil di Tab Paired
32. Selesaikan disposal aset bertag DD-13 di FAMS lewat sesi API Admin FAMS hingga selesai dan event diproses
33. Verifikasi DD-13 hilang dari Tab Paired tanpa muat ulang
34. Klik Tab Not Paired
35. Verifikasi DD-13 tampil di Tab Not Paired berstatus `To be Returned` (badge warning)
36. Verifikasi DD-13 tidak tertaut ke aset
37. Buka menu baris DD-13, lalu klik `TAG Log`
38. Verifikasi satu entri baru `TAG Marked To be Returned by [pelaku disposal]` (jumlah entri bertambah satu dari nilai yang dicatat)
39. Verifikasi entri itu memuat `Asset`, `Asset Code`, `Reason: Disposal`, dan `Return Group` Group asal aset pada transaksi disposal (Group DSP)
40. Verifikasi tidak ada entri `TAG Unpaired by ...` maupun `TAG Retired by ...`
41. Tutup popup TAG Log
42. Klik Tab All
43. Verifikasi kartu NFC tetap `3 of 30`

### TC-GS-TAG-349: Disposal aset bertag QR

44. Klik Tab Paired
45. Verifikasi DD-10 tampil di Tab Paired
46. Selesaikan disposal aset bertag QR DD-05 di FAMS lewat sesi API Admin FAMS hingga selesai dan event diproses
47. Verifikasi baris `TAG-QR-00512` tidak tampil di Tab Paired
48. Klik Tab Not Paired
49. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
50. Verifikasi DD-02 tampil di Tab Not Paired
51. Verifikasi baris `TAG-QR-00512` tidak tampil di Tab Not Paired
52. Klik Tab All, lalu pasang filter `Status` = `Retired`
53. Verifikasi DD-08 tampil pada hasil filter
54. Verifikasi tidak ada baris QR berstatus `Retired`
55. Ganti filter `Status` menjadi `To be Returned`
56. Verifikasi DD-07 tampil pada hasil filter
57. Verifikasi tidak ada baris QR berstatus `To be Returned`
58. Hapus filter `Status`

### TC-GS-TAG-379: Disposal aset: RFID combined masuk To be Returned, sibling QR keluar dari registri

59. Sisipkan DD-62 dan DD-63 (Paired ke Asset Z, combined) lewat fixture BE, muat ulang halaman, lalu klik Tab Paired
60. Verifikasi DD-62 tampil di Tab Paired
61. Klik ikon 🔗 pada baris DD-62
62. Verifikasi Popup Combined TAG baris DD-62 memuat sibling QR DD-63 (`TAG-QR-00620`)
63. Tutup popup
64. Selesaikan disposal Asset Z (bertag DD-62 dan DD-63) di FAMS lewat sesi API Admin FAMS hingga selesai dan event diproses
65. Verifikasi DD-62 tidak lagi tampil di Tab Paired tanpa muat ulang
66. Verifikasi baris `TAG-QR-00620` tidak tampil di Tab Paired
67. Klik Tab Not Paired
68. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
69. Verifikasi DD-62 tampil di Tab Not Paired
70. Verifikasi status DD-62 `To be Returned`
71. Verifikasi baris `TAG-QR-00620` tidak tampil di Tab Not Paired
72. Klik Tab All
73. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
74. Verifikasi DD-62 tampil di Tab All
75. Verifikasi baris `TAG-QR-00620` tidak tampil di Tab All
76. Ketik Search `TAG-QR-00620`, tekan Enter
77. Verifikasi pencarian `TAG-QR-00620` tidak menemukan baris (`No results found`)
78. Klik `(←)` pada kotak Search
79. Ubah Rows per page menjadi 50 (seluruh baris tab ini tampil pada satu halaman)
80. Klik ikon 🔗 pada baris DD-62
81. Verifikasi Popup Combined TAG baris DD-62 terbuka
82. Verifikasi popup tidak memuat baris sibling QR DD-63 (`TAG-QR-00620`)
83. Tutup popup, lalu pasang filter `Status` = `To be Returned`
84. Verifikasi DD-62 tampil pada hasil filter
85. Verifikasi tidak ada baris QR berstatus `To be Returned`
86. Ganti filter `Status` menjadi `Retired`
87. Verifikasi DD-08 tampil pada hasil filter
88. Verifikasi tidak ada baris QR berstatus `Retired`
89. Hapus filter `Status`

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (89 langkah nominal). Alasan: lima TC satu topik (efek disposal FAMS pada status tag) dengan satu dataset Seed Registri A dan satu kelas harness; pemicu FAMS lewat sesi API aktor dan tiap blok berdiri sendiri karena data dipulihkan lewat fixture BE di langkah 11, 29, dan 59.
- Perubahan urutan (S-05 butir terakhir): urutan TC sumber (298, 348, 349, 370, 379) disusun ulang menjadi 348, 298, 370, 349, 379. TC-GS-TAG-348 dan 298 memakai DD-01 yang sama (dipulihkan di langkah 11); TC-GS-TAG-349 (tag QR keluar dari registri) dan TC-GS-TAG-379 (sibling QR keluar bersama disposal RFID) di akhir.

- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 1 dan 30 (baseline jumlah entri TAG Log), 9, 21, 28, dan 41 (menutup popup TAG Log), 11 dan 29 (memulihkan data lewat fixture BE), 15, 34, 42, 44, 48, dan 52 (pindah tab dan memasang filter; langkah 42 klik Tab All karena kartu `N of M` hanya tampil di Tab All), 55 dan 58 (mengganti dan menghapus filter), 59 (menyisipkan fixture TC-GS-TAG-379 lewat fixture BE), 67 dan 72 (pindah tab), 63 (menutup popup), 78 (mengosongkan Search), 83 (menutup popup dan memasang filter), 86 dan 89 (mengganti dan menghapus filter), 49 (mengubah Rows per page menjadi 50 supaya baris halaman 2 dan 3 Tab Not Paired tampil; ukuran halaman tidak diasumsikan terbawa antar tab). Rows per page 50 pada langkah 68, 73, dan 79 adalah langkah TC-GS-TAG-379 (langkah 1); ukuran halaman dikembalikan ke 10 di hook `after`.
- Asersi tambahan di luar Expected TC (S-03): langkah 12, 31, 45, 50, 53, 56, 60, 65, 74, 84, dan 87 (data pembanding atau perubahan baris akibat disposal sebagai anchor absence, bagian 8b butir 2); langkah 81 (popup terbuka sebagai anchor absence langkah 82).
- Temuan untuk QA:
  - Q-9: langkah dan selektor FAMS (disposal, Receive TAG) tidak didefinisikan; verifikasi di modul konsumen hanya sejauh Expected TC.
  - Q-15: `[pelaku disposal]`, `[pelaku user FAMS yang menerima]`, dan Return Group pada TAG Log tidak diberi nilai dan format penulisan nama; spec menulis placeholder TC apa adanya.
  - TC-GS-TAG-348 Expected a "status tidak pernah `Available` maupun `Retired`" tidak teramati sebagai riwayat; spec mengasersi status akhir (langkah 5) dan tidak adanya entri `Unpaired`/`Retired` (langkah 8).
  - Kolom registri yang menampilkan relasi tag ke aset ("tidak tertaut ke aset") tidak dinamai di TC; asersinya memakai pembacaan relasi yang disediakan tim FE/BE.
  - TC-GS-TAG-298 butir c ("tidak ada entri `Unpaired` Reason `Returned`") tidak menyebut nilai Return Group; spec hanya mengasersi kehadiran field.
  - Q-1: TC-GS-TAG-298 berlabel Automatable, tetapi langkah `Receive TAG` bersifat pemindaian; kemampuan simulasi reader dicatat di Prerequisites sebagai kebutuhan (D-4).
  - TC-GS-TAG-379 Expected d ("baris DD-62 tidak lagi memuat DD-63 pada Popup Combined TAG") tidak menyatakan apakah ikon 🔗 tetap tampil pada baris DD-62 yang tidak punya sibling lagi; spec mengikuti TC dan membuka popup lewat ikon 🔗 (langkah 80). Hasilnya perlu keputusan PM.
  - TC-GS-TAG-379 tidak menyebut Return Group atau entri TAG Log DD-62; spec tidak mengasersinya. TC-GS-TAG-379 tidak punya Post Condition.
  - Post Condition TC-GS-TAG-348 tidak ada; Post Condition TC-GS-TAG-370 butir a dan b identik dengan Expected a dan c; TC-GS-TAG-349 tidak punya Post Condition.
