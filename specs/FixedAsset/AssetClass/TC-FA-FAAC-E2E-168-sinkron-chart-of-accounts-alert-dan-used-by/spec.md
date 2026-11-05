---
id: TC-FA-FAAC-E2E-168-sinkron-chart-of-accounts-alert-dan-used-by
title: "Sinkronisasi Chart of Accounts: Alert Dependensi Akun, Used By, dan Kolom Accounts"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-555
  - TC-FA-FAAC-556
  - TC-FA-FAAC-557
  - TC-FA-FAAC-558
  - TC-FA-FAAC-561
  - TC-FA-FAAC-567
  - TC-FA-FAAC-584
coverage:
  web: automated
---

# Sinkronisasi Chart of Accounts: Alert Dependensi Akun, Used By, dan Kolom Accounts

## Prerequisites

- Mode: FE+BE
- Akun aktor pertama: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.FA_TC_PASSWORD`). Nama tampil akun pada kolom Modified By: `Rina W` (format [First Name] [Last Initial], menurut TC-541 sampai TC-550). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > tab Asset Class dibuka hook `beforeEach` suite.
- Data seed (kode dan nama literal TC, disediakan tim FE/BE lewat fixture BE): Chart of Accounts per TC diatur lewat fixture BE sebelum tiap TC (akun `Asset Cost Uji`, `Beban Uji`, `Akumulasi Uji`, `Aset Uji`, `11001 – Machinery Cost`, `11003 – Machinery Cost Spare`, `12001`, `1-2100 – Vehicles Cost`, `1-2200 – Heavy Vehicles Cost`); Asset Class `B-SYNC3`, `B-ANCHOR`, dan `LT-VEH` Active.
- Nilai akun baru valid (TC-555 hanya menyebut nama, Account Function, dan status): Nama akun `Asset Cost Uji`; Account Function `Asset Cost`; Status `Active`; field wajib Chart of Accounts lain (mis. kode akun) diisi nilai bersuffix `{runId}-168` dari `Fixture.fixedAssetAssetClass.<kunci>` dan dicatat di Temuan untuk QA.
- Kemampuan baca log yang disediakan tim FE/BE: jumlah entri Changelog, System Log aktor, dan Activity Log FAMS dibaca tepat sebelum aksi pemicu tiap TC (audit trail permanen, total tidak diturunkan dari seeding, S-12).
- State yang diubah spec dan dipulihkan fixture BE di hook `after`: Chart of Accounts dikembalikan ke keadaan seed (nama akun 11001, status akun 12001, akun uji dihapus, Account Function Beban Uji); B-SYNC3 dan LT-VEH kembali ke Asset Cost seed. Chart of Accounts bersifat bersama per client sehingga suite berjalan serial.
- Kode dan nama seed memakai nilai literal TC apa adanya tanpa suffix `{runId}` karena asersi TC bergantung pada kode itu. Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip, sesi API aktor, seed dan fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-FAAC-555: Alert dependensi akun hilang setelah akun Active dibuat di Chart of Accounts

1. Atur Chart of Accounts lewat fixture BE: tidak ada akun Active ber-Account Function Asset Cost; dua Function wajib lain punya akun Active (precondition TC-555, tidak diasersi)
2. Klik tab `Asset Class`
3. Verifikasi Alert dependensi akun menyebut Asset Cost: `No active account for Asset Cost in Chart of Accounts. Add one so asset classes can map their accounts.`
4. Klik tab `Chart of Accounts`
5. Buat akun baru `Asset Cost Uji` dengan Account Function Asset Cost berstatus Active (nilai akun baru valid, Prerequisites)
6. Tunggu aksi selesai
7. Klik tab `Asset Class`
8. Verifikasi Table Tools tabel Asset Class tampil
9. Verifikasi Alert dependensi akun tidak tampil lagi

### TC-FA-FAAC-556: Alert dependensi akun muncul setelah Account Function akun satu-satunya diubah

10. Atur Chart of Accounts lewat fixture BE: akun Active satu-satunya ber-Account Function Depreciation Expense bernama `Beban Uji` ada; dua Function wajib lain punya akun Active (precondition TC-556, tidak diasersi)
11. Klik tab `Chart of Accounts`
12. Ubah Account Function akun `Beban Uji` dari `Depreciation Expense` ke `Gain on Disposal`
13. Tunggu aksi selesai
14. Klik tab `Asset Class`
15. Verifikasi Alert tampil dengan teks `No active account for Depreciation Expense in Chart of Accounts. Add one so asset classes can map their accounts.`

### TC-FA-FAAC-557: Alert dependensi akun muncul setelah akun Active satu-satunya dinonaktifkan

16. Atur Chart of Accounts lewat fixture BE: akun Active satu-satunya ber-Account Function Accumulated Depreciation bernama `Akumulasi Uji` ada; dua Function wajib lain punya akun Active (precondition TC-557, tidak diasersi)
17. Klik tab `Chart of Accounts`
18. Deactivate akun `Akumulasi Uji`
19. Tunggu aksi selesai
20. Klik tab `Asset Class`
21. Verifikasi Alert tampil dengan teks `No active account for Accumulated Depreciation in Chart of Accounts. Add one so asset classes can map their accounts.`

### TC-FA-FAAC-558: Alert dependensi akun muncul setelah akun Active satu-satunya dihapus

22. Atur Chart of Accounts lewat fixture BE: akun Active satu-satunya ber-Account Function Asset Cost bernama `Aset Uji` tanpa pemakaian ada; dua Function wajib lain punya akun Active (precondition TC-558, tidak diasersi)
23. Klik tab `Chart of Accounts`
24. Delete akun `Aset Uji`, lalu klik `Delete` pada dialog konfirmasi
25. Tunggu aksi selesai
26. Klik tab `Asset Class`
27. Verifikasi Alert tampil dengan teks `No active account for Asset Cost in Chart of Accounts. Add one so asset classes can map their accounts.`

### TC-FA-FAAC-561: Ubah akun menghitung ulang Used By dan kolom Accounts

28. Pulihkan lewat fixture BE: Chart of Accounts lengkap dengan akun `11001 – Machinery Cost` dan `11003 – Machinery Cost Spare` Active, dan `B-SYNC3` memakai Asset Cost `11001 – Machinery Cost` (precondition TC-561, tidak diasersi)
29. Klik tab `Chart of Accounts`
30. Buka popup Used By akun `11001 – Machinery Cost`
31. Catat Used By akun 11001 (U1a)
32. Tutup popup Used By
33. Buka popup Used By akun `11003 – Machinery Cost Spare`
34. Catat Used By akun 11003 (U3a)
35. Tutup popup Used By
36. Klik tab `Asset Class`
37. Klik link Class Code `B-SYNC3` di tabel
38. Klik tab `Accounts`
39. Ganti Asset Cost dari `11001 – Machinery Cost` ke `11003 – Machinery Cost Spare`
40. Klik `Save`
41. Tunggu aksi selesai
42. Klik tab `Chart of Accounts`
43. Buka popup Used By akun `11001 – Machinery Cost`
44. Verifikasi Used By akun 11001 berkurang satu dari U1a
45. Tutup popup Used By
46. Buka popup Used By akun `11003 – Machinery Cost Spare`
47. Verifikasi Used By akun 11003 bertambah satu dari U3a
48. Tutup popup Used By
49. Klik tab `Asset Class`
50. Verifikasi ikon Accounts baris `B-SYNC3` mencerminkan kelengkapan akun terbaru

### TC-FA-FAAC-567: Perubahan akun di Chart of Accounts tercermin di kolom Accounts dan opsi Select akun

51. Pulihkan lewat fixture BE: `B-ANCHOR` memakai akun `11001` dan `12001` (keduanya Active) (precondition TC-567, tidak diasersi)
52. Catat jumlah entri Changelog (Nc) sebagai baseline lewat kemampuan baca log
53. Klik tab `Chart of Accounts`
54. Ubah nama akun 11001 menjadi `Machinery Cost Renamed`
55. Nonaktifkan akun 12001
56. Tunggu aksi selesai
57. Klik tab `Asset Class`
58. Verifikasi ikon Accounts baris `B-ANCHOR` kuning (lengkap dengan akun Inactive)
59. Arahkan kursor ke ikon Accounts baris `B-ANCHOR`
60. Verifikasi tooltip `Account 12001 is inactive. Journals for this asset class will be held at export.`
61. Klik link Class Code `B-ANCHOR` di tabel
62. Klik tab `Accounts`
63. Verifikasi nilai terpilih Asset Cost menampilkan nama baru `11001 – Machinery Cost Renamed`
64. Buka Select Asset Cost
65. Verifikasi opsi `11001 – Machinery Cost Renamed` tampil pada Select Asset Cost
66. Tutup Select Asset Cost tanpa memilih
67. Buka Select Accumulated Depreciation
68. Verifikasi sedikitnya satu opsi akun Active lain tampil pada Select
69. Verifikasi akun 12001 tidak ditawarkan sebagai opsi baru
70. Tutup Select tanpa memilih
71. Kembali ke tabel Asset Class lewat Breadcrumb
72. Klik ikon Changelog di toolbar tabel Asset Class (modal `Changelog: Asset Class`)
73. Verifikasi jumlah entri Changelog sama dengan Nc (riwayat log tidak berubah oleh perubahan di Chart of Accounts)
74. Tutup modal Changelog

### TC-FA-FAAC-584: Mengubah akun Asset Cost menghitung ulang Used By akun lama dan baru

75. Pulihkan lewat fixture BE: `LT-VEH` memakai Asset Cost `1-2100 – Vehicles Cost` tanpa Last Exported Period; akun `1-2200 – Heavy Vehicles Cost` Active (precondition TC-584, tidak diasersi)
76. Klik tab `Chart of Accounts`
77. Buka popup Used By akun `1-2100 – Vehicles Cost`
78. Catat Used By akun lama (A1)
79. Tutup popup Used By
80. Buka popup Used By akun `1-2200 – Heavy Vehicles Cost`
81. Catat Used By akun baru (B1)
82. Tutup popup Used By
83. Klik tab `Asset Class`
84. Ketik Search `LT-VEH`, tekan Enter
85. Klik link Class Code `LT-VEH` di tabel
86. Klik tab `Accounts`
87. Ubah Asset Cost menjadi `1-2200 – Heavy Vehicles Cost`
88. Klik `[Save]`
89. Tunggu aksi selesai
90. Klik tab `Chart of Accounts`
91. Buka popup Used By akun `1-2100 – Vehicles Cost`
92. Verifikasi Used By akun `1-2100 – Vehicles Cost` berkurang satu Asset Class dari A1
93. Tutup popup Used By
94. Buka popup Used By akun `1-2200 – Heavy Vehicles Cost`
95. Verifikasi Used By akun `1-2200 – Heavy Vehicles Cost` bertambah satu Asset Class dari B1
96. Tutup popup Used By

## Notes

1. Langkah penghubung (S-03, tanpa `Verifikasi`): langkah 1, 10, 16, 22, 28, 51, dan 75 (pengaturan state Chart of Accounts lewat fixture BE sebagai precondition TC, tidak diasersi), langkah "Tunggu aksi selesai" sesudah aksi tulis di Chart of Accounts atau `Save` yang hasilnya tidak diasersi langsung sebelum pindah tab, langkah 84 (Search kode `LT-VEH` untuk menemukan baris target, R-16: tabel Asset Class memuat lebih dari 25 baris), pencatatan jumlah Used By sebelum aksi pada TC-561 dan TC-584 (baseline yang diperlukan untuk selisih; TC menyebut "berkurang/bertambah satu" tanpa langkah pencatatan), pindah tab, dan pembukaan serta penutupan popup Used By.
2. Baseline log (S-12): jumlah entri dicatat ulang sebelum aksi pemicu tiap TC lewat kemampuan baca log. Entri baru dibaca pada baris teratas urutan default Date terbaru sesudah selisih jumlah dari baseline dibuktikan (S-14); bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
3. Pengecualian kode seed literal: TC mewajibkan baris seed bernama literal; kode dan nama dipakai apa adanya tanpa suffix `{runId}` (S-06 dan S-12 dikecualikan dengan alasan ini).
4. Alasan jumlah langkah: jumlah nominal melampaui sekitar 35 langkah karena tujuh TC sinkronisasi Chart of Accounts yang tiap bloknya mengatur state Chart of Accounts sendiri; semua TC satu topik dan tiap blok berdiri sendiri dengan precondition sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
5. Temuan untuk QA: (a) TC-555 tidak menyebut teks Alert; spec memakai pola teks Alert pada TC-558. (b) TC-558 tidak menyebut dialog konfirmasi Delete akun; spec menulis `Delete` pada dialog. (c) TC-561 dan TC-584 tidak menyebut Precondition Asset Class dan jumlah Used By awal; TC-561 tidak menyebut tab asal Asset Cost dan arti "mencerminkan kelengkapan akun terbaru" untuk ikon Accounts (spec tidak mengasersi warna). (d) TC-567 tidak menyebut Select akun mana yang memuat akun 12001 dan apa isi "riwayat log tidak berubah"; spec mengasersi jumlah entri Changelog tidak bertambah dan Select Accumulated Depreciation, dengan asumsi 12001 adalah akun Accumulated Depreciation. (f) TC-555 tidak menyebut field wajib akun baru selain nama, Account Function, dan status; spec memakai nilai fixture untuk field lain. (e) Pemicu TC-556 mengubah Account Function menjadi `Gain on Disposal` sesuai LK; nilai awal fixture `Beban Uji` ada pada TC-556.
