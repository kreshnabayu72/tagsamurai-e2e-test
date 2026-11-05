---
id: TC-AC-LA-E2E-129-integritas-log-dan-ringkasan-trigger
title: "Integritas Log: Satu Baris per Field, Tidak Nyasar, Snapshot Immutability, Ringkasan Trigger, dan Rename Client"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-415
  - TC-AC-LA-416
  - TC-AC-LA-417
  - TC-AC-LA-400
  - TC-AC-LA-418
coverage:
  web: automated
---

# Integritas Log: Satu Baris per Field, Tidak Nyasar, Snapshot Immutability, Ringkasan Trigger, dan Rename Client

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Dewi Anggraini; halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Dewi Anggraini | #4 | Distributor PT Maju Bersama, Manage allocation Create+Read+Update | `dewiFullLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_DIST_FULL_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE). Akun approver record Pre-setup #55 (`{approver55}`) tidak tertulis di Pre-setup TC; disediakan tim FE.
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19; `SUBS-20260101-A1B2C`), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price (Pre-setup #34), Require Approval for Allocation ON (Pre-setup #38), alokasi dengan riwayat log lengkap (Pre-setup #55, hanya dibaca): `{idFull}` (created, edited, approved, activated, expired) dan `{idCancelHist}` (canceled dan auto-canceled).
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #41 dan #42 bersama): alokasi `Waiting for Approval` Concurrent User ke `SUBS-20260101-A1B2C` PT Sejahtera, requester Dewi Anggraini, Cost di-Reserve (bentuk Pre-setup #41 dan #42): `{idMulti}` (+5), `{idOne}` (+5), `{idTwo}` (+10), `{idHist}` (+5).
- Kemampuan teknis (disediakan tim FE/BE): seeding alokasi dan pembersihannya; kemampuan membaca jumlah entri `{idTwo}` pada Changelog, System Log, Activity Log, dan Allocation Log (`{nTwoChangelog}`, `{nTwoSystemLog}`, `{nTwoActivityLog}`, `{nTwoAllocLog}`), dicatat di hook `before` setelah seeding; fixture backend untuk memulihkan nama Client Pre-setup #19.
- State global: nama Client `PT Sejahtera` (Pre-setup #19) diubah menjadi `PT Sejahtera Makmur` pada blok TC-AC-LA-418 dan dipulihkan lewat fixture backend pada langkah terakhir spec dan di hook `after`; Last Updated Client #19 dan entri audit trail Client berubah dan dicatat sebagai efek pengecualian S-06 (pemulihan dijamin fixture backend, suite serial).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Edit multi-field: satu baris log per field (TC-AC-LA-415)

1. Ketik Search `{idMulti}`, tekan Enter
2. Klik row action `Edit` pada baris `{idMulti}`
3. Ubah Type dari `Concurrent User` menjadi `Asset License`
4. Ubah Additional Quantity dari `5` menjadi `8`
5. Klik `[Save]`
6. Tunggu aksi selesai
7. Klik ikon `Changelog` pada List
8. Ketik Search `{idMulti}`, tekan Enter
9. Verifikasi Changelog memuat tepat dua baris `Edit` untuk `{idMulti}` (Field `Type` dan Field `Additional Quantity`), tanpa duplikat dan tanpa baris hilang
10. Tutup modal Changelog
11. Buka Detail User `Dewi Anggraini` > tab System Log
12. Ketik Search `{idMulti}`, tekan Enter
13. Verifikasi System Log memuat tepat dua baris `Edit` untuk `{idMulti}` (Field `Type` dan Field `Additional Quantity`), tanpa duplikat dan tanpa baris hilang
14. Buka Activity Log Admin Console
15. Ketik Search `{idMulti}`, tekan Enter
16. Verifikasi Activity Log memuat tepat dua baris `Edit` untuk `{idMulti}` (Field `Type` dan Field `Additional Quantity`), tanpa duplikat dan tanpa baris hilang
17. Buka Allocation > License Allocation (tab Current)

### Field tidak berubah dan record lain tidak nyasar (TC-AC-LA-416)

18. Ketik Search `{idOne}`, tekan Enter
19. Klik row action `Edit` pada baris `{idOne}`
20. Ubah Additional Quantity dari `5` menjadi `8`
21. Klik `[Save]`
22. Tunggu aksi selesai
23. Klik ikon `Changelog` pada List
24. Ketik Search `{idOne}`, tekan Enter
25. Verifikasi Changelog untuk `{idOne}` hanya memuat baris `Edit` Field `Additional Quantity`
26. Ganti isi kotak search dengan `{idTwo}`, tekan Enter
27. Verifikasi jumlah entri Changelog `{idTwo}` sama dengan `{nTwoChangelog}`
28. Tutup modal Changelog
29. Buka Detail User `Dewi Anggraini` > tab System Log
30. Ketik Search `{idOne}`, tekan Enter
31. Verifikasi System Log untuk `{idOne}` hanya memuat baris `Edit` Field `Additional Quantity`
32. Ganti isi kotak search dengan `{idTwo}`, tekan Enter
33. Verifikasi jumlah entri System Log `{idTwo}` sama dengan `{nTwoSystemLog}`
34. Buka Activity Log Admin Console
35. Ketik Search `{idOne}`, tekan Enter
36. Verifikasi Activity Log untuk `{idOne}` hanya memuat baris `Edit` Field `Additional Quantity`
37. Ganti isi kotak search dengan `{idTwo}`, tekan Enter
38. Verifikasi jumlah entri Activity Log `{idTwo}` sama dengan `{nTwoActivityLog}`
39. Buka Allocation > License Allocation (tab Current)
40. Ketik Search `{idTwo}`, tekan Enter
41. Klik row action `Allocation Log` pada baris `{idTwo}`
42. Verifikasi jumlah entri Allocation Log `{idTwo}` sama dengan `{nTwoAllocLog}`
43. Tutup modal Allocation Log

### Snapshot immutability setelah Edit kedua (TC-AC-LA-417)

44. Ganti isi kotak search dengan `{idHist}`, tekan Enter
45. Klik row action `Edit` pada baris `{idHist}`
46. Ubah Additional Quantity dari `5` menjadi `8`
47. Klik `[Save]`
48. Klik row action `Edit` pada baris `{idHist}`
49. Ubah Additional Quantity dari `8` menjadi `9`
50. Klik `[Save]`
51. Tunggu aksi selesai
52. Klik ikon `Changelog` pada List
53. Ketik Search `{idHist}`, tekan Enter
54. Verifikasi entri Edit pertama tetap Old `5` New `8`
55. Verifikasi entri Edit kedua Old `8` New `9`
56. Tutup modal Changelog

### Ringkasan trigger per surface (TC-AC-LA-400)

57. Klik ikon `Changelog` pada List
58. Ketik Search `{idFull}`, tekan Enter
59. Verifikasi Changelog `{idFull}` memuat baris Action `Create` dan Action `Edit`
60. Verifikasi Changelog `{idFull}` memuat baris `Auto-Activate` dan `Auto-Expire` dengan Modified By `System`
61. Verifikasi Changelog `{idFull}` tidak memuat baris Action `Approve` maupun `Reject`
62. Ganti isi kotak search dengan `{idCancelHist}`, tekan Enter
63. Verifikasi Changelog `{idCancelHist}` memuat baris Action `Cancel`
64. Verifikasi Changelog `{idCancelHist}` memuat baris `Timeout Auto-Cancel` dengan Modified By `System`
65. Tutup modal Changelog
66. Buka Detail User `Dewi Anggraini` > tab System Log
67. Ketik Search `{idFull}`, tekan Enter
68. Verifikasi System Log aktor memuat baris Action `Create` dan Action `Edit` untuk `{idFull}`
69. Verifikasi System Log aktor untuk `{idFull}` tidak memuat baris `Auto-Activate` maupun `Auto-Expire`
70. Ganti isi kotak search dengan `{idCancelHist}`, tekan Enter
71. Verifikasi System Log aktor memuat baris Action `Cancel` untuk `{idCancelHist}`
72. Verifikasi System Log aktor untuk `{idCancelHist}` tidak memuat baris `Timeout Auto-Cancel`
73. Buka Detail User `{approver55}` > tab System Log
74. Ketik Search `{idFull}`, tekan Enter
75. Verifikasi System Log approver memuat baris Action `Approve` untuk `{idFull}`
76. Buka Activity Log Admin Console
77. Ketik Search `{idFull}`, tekan Enter
78. Verifikasi Activity Log memuat baris Action `Create`, `Edit`, dan `Approve` untuk `{idFull}` serta baris `Auto-Activate` dan `Auto-Expire` dengan Modified By `System`
79. Ganti isi kotak search dengan `{idCancelHist}`, tekan Enter
80. Verifikasi Activity Log memuat baris Action `Cancel` dan baris `Timeout Auto-Cancel` dengan Modified By `System` untuk `{idCancelHist}`
81. Buka Allocation > License Allocation (tab Current)

### Rename Client tidak mengubah entri Changelog lama (TC-AC-LA-418)

82. Klik ikon `Changelog` pada List
83. Ketik Search `{idFull}`, tekan Enter
84. Verifikasi entri `Create` `{idFull}` memuat New Value dengan nama Client `PT Sejahtera` (`... to PT Sejahtera`) sebelum rename
85. Tutup modal Changelog
86. Buka Client Detail `PT Sejahtera`
87. Ubah nama Client menjadi `PT Sejahtera Makmur`
88. Klik `[Save]`
89. Tunggu aksi selesai
90. Buka Allocation > License Allocation (tab Current)
91. Klik ikon `Changelog` pada List
92. Ketik Search `{idFull}`, tekan Enter
93. Verifikasi entri `Create` `{idFull}` lama tetap menampilkan New Value dengan nama Client saat entri dibuat (`... to PT Sejahtera`)
94. Tutup modal Changelog
95. Klik tab `History`
96. Ketik Search `{idFull}`, tekan Enter
97. Verifikasi kolom Client pada baris `{idFull}` menampilkan `PT Sejahtera Makmur`
98. Pulihkan nama Client menjadi `PT Sejahtera` lewat fixture backend

## Notes

- Alasan di atas sekitar 35 langkah: seluruh blok satu topik (integritas pencatatan log di tiga surface oleh Dewi Anggraini), satu kelas harness fungsional, dan berdiri sendiri pada record seed masing-masing. Hampir seluruh langkah adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung pada ambang smell; langkah aksi (Edit dan rename) hanya sekitar 25.
- Asersi jumlah pada langkah 9, 13, 16, 27, 33, 38, dan 42 memakai baseline (S-12) dan bukan kelas g. Asersi absence pada langkah 61, 69, 72 (ringkasan trigger) memakai anchor positif pada surface dan record yang sama (langkah 59 sampai 60, 68, dan 71). Asersi "record lain tidak mendapat entri" (langkah 27, 33, 38, 42) memakai anchor baris `Edit` `{idOne}` pada surface yang sama (langkah 25, 31, 36).
- Langkah penghubung (S-03, R-16): langkah 6, 22, 51 dan 89 (menunggu aksi selesai karena langkah berikutnya berpindah surface, 8b butir 8), langkah 1, 8, 12, 15, 18, 24, 26, 30, 32, 35, 37, 40, 44, 53, 58, 62, 67, 70, 74, 77, 79, 83, 92, dan 96 (Search baris atau entri berdasarkan Allocation ID), langkah 10, 28, 56, 65, 85, dan 94 (menutup modal Changelog), langkah 43 (menutup modal Allocation Log), langkah 17, 39, 81, dan 90 (kembali ke List), langkah 95 (pindah tab History), langkah 98 (memulihkan nama Client).
- Pembagian TC lintas spec: TC-AC-LA-388 (dependensi TC-AC-LA-415 dan TC-AC-LA-416) ada di spec 124.
- Temuan untuk QA:
  - TC-AC-LA-400 tidak menyebut record, aktor, maupun approver pada Pre-setup #55 (dua alokasi: riwayat lengkap, dan riwayat canceled dan auto-canceled); spec memakai dua record (`{idFull}` dan `{idCancelHist}`), requester Dewi Anggraini untuk System Log aktor, dan approver `{approver55}` yang disediakan tim FE. Langkah Uji menyebut "Telusuri Allocation Log" tetapi Expected tidak memuat butir tentang Allocation Log; tidak diasersi.
  - TC-AC-LA-400 butir b menyebut "Approve dan Reject" sedangkan Pre-setup #55 hanya memuat riwayat approved; entri Reject pada record #55 tidak tersedia sehingga tidak diasersi.
  - TC-AC-LA-418 tidak menyebut record dan Client entri lama pada Pre-setup #55; spec memakai entri Create `{idFull}` dan mengasumsikan Client record itu `PT Sejahtera`. Akun pelaku rename Client tidak disebut TC selain Pre-setup #4; spec memakai Dewi Anggraini, dan tab History dipakai karena record `{idFull}` berstatus akhir `Expired`.
  - TC-AC-LA-415 dan TC-AC-LA-416 tidak menyebut cara menemukan entri di tiga surface; spec memakai Search dengan Allocation ID. TC-AC-LA-416 butir b ("surface mana pun") tidak mendaftar surface; spec memakai Changelog, System Log, Activity Log, dan Allocation Log.
  - TC-AC-LA-417 hanya menyebut Changelog; spec tidak mengasersi surface lain.
