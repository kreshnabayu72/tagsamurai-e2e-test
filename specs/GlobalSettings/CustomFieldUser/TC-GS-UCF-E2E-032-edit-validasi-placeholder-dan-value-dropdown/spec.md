---
id: TC-GS-UCF-E2E-032-edit-validasi-placeholder-dan-value-dropdown
title: "Edit Custom Field: Validasi Placeholder dan Value Dropdown (Batas Panjang, Trim, Hanya Spasi, Emoji, Duplikat, Pemulihan setelah Error Dropdown Kosong)"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UCF-97
  - TC-GS-UCF-458
  - TC-GS-UCF-333
  - TC-GS-UCF-470
  - TC-GS-UCF-332
  - TC-GS-UCF-334
  - TC-GS-UCF-335
  - TC-GS-UCF-471
  - TC-GS-UCF-472
coverage:
  web: automated
---

# Edit Custom Field: Validasi Placeholder dan Value Dropdown (Batas Panjang, Trim, Hanya Spasi, Emoji, Duplikat, Pemulihan setelah Error Dropdown Kosong)

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`).
- Akun aktor (login di hook `before`; password hanya lewat env var): Total Control Client A (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), `Spectra.env.GS_TC_PASSWORD`.
- Layar awal Global Settings > User > Custom Field dibuka hook `beforeEach`; `## Test Steps` tidak mengulang langkah buka.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Data Pre-setup tidak dipakai.
- Data Dinamis milik spec (seeding lewat API di hook `before`, bersuffix `{runId}-032`; fixture baru `Fixture.customFieldUser.edit032`; Active, Required No, tanpa nilai User):
  - `Edit Meta Renamed {runId}-032`: Text, Placeholder kosong (TC-GS-UCF-97).
  - `Edit Trim Probe {runId}-032`: Text, Placeholder kosong (TC-GS-UCF-458).
  - `Edit Ph Space {runId}-032`: Text, Placeholder `Hint` (TC-GS-UCF-333).
  - `Ph Clear Probe {runId}-032`: Text, Placeholder `Hint` (TC-GS-UCF-470).
  - `Edit Emoji DD {runId}-032`: Dropdown `Alpha`, `Beta` (TC-GS-UCF-332).
  - `Edit Val Probe {runId}-032`: Dropdown `Alpha`, `Beta` (TC-GS-UCF-334).
  - `Recover DD {runId}-032`: Dropdown `Solo` (TC-GS-UCF-335).
  - `Edit Trim DD {runId}-032`: Dropdown `Alpha`, `Beta` (TC-GS-UCF-471).
  - `Edit Dup DD {runId}-032`: Dropdown `Alpha`, `Beta` (TC-GS-UCF-472).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API semua Custom Field bersuffix `{runId}-032` (termasuk nama hasil perubahan).
- Kemampuan teknis: mengetik dan menempel (paste) karakter emoji pada input; membaca Changelog Custom Field (Modal Changelog) dengan Search; menghitung karakter string uji (120 dan 121 karakter); membaca daftar request jaringan yang terekam sejak popup dibuka (asersi "tidak memuat request tulis ke server").
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### Persiapan tabel

1. Ketik Search `{runId}-032`, tekan Enter

### TC-GS-UCF-97: Placeholder 120 karakter diterima dan 121 karakter menampilkan error

2. Klik `⋯` pada baris `Edit Meta Renamed {runId}-032`, pilih `Edit`
3. Isi Placeholder 120 karakter `A`
4. Verifikasi tidak ada error pada Placeholder
5. Tambahkan 1 karakter `A` pada Placeholder
6. Verifikasi error inline `Max. 120 characters` tampil
7. Klik `[Save]`
8. Verifikasi error inline `Max. 120 characters` tetap tampil
9. Verifikasi popup tetap terbuka
10. Verifikasi tidak ada toast sukses
11. Klik `[✕]`
12. Verifikasi dialog `Unsaved Changes` tampil
13. Klik `[Leave]`

### TC-GS-UCF-334: Value Dropdown pada Edit, kosong, hanya spasi, 120, dan 121 karakter pada tambah dan rename

14. Klik `⋯` pada baris `Edit Val Probe {runId}-032`, pilih `Edit`
15. Tekan Enter pada input value kosong
16. Verifikasi error inline `Option name must not be empty` tampil pada Dropdown Values
17. Verifikasi tidak ada badge baru
18. Ketik 3 spasi pada input value, tekan Enter
19. Verifikasi error inline `Option name must not be empty` tampil pada Dropdown Values
20. Verifikasi tidak ada badge baru
21. Ketik 120 karakter `A`, tekan Enter
22. Verifikasi badge 120 karakter `A` ditambahkan
23. Ketik 121 karakter `A`, tekan Enter
24. Verifikasi error inline `Max. 120 characters` tampil
25. Verifikasi Enter tidak menambah badge
26. Klik teks badge `Beta`, ganti dengan 120 karakter `B`, tekan Enter
27. Verifikasi rename `Beta` menjadi 120 karakter `B` diterima sebagai badge
28. Klik teks badge 120 karakter `B`, tambahkan 1 karakter `B`, tekan Enter
29. Verifikasi error inline `Max. 120 characters` tampil
30. Verifikasi badge kembali ke teks 120 karakter `B` sebelum diedit
31. Klik `[✕]`
32. Verifikasi dialog `Unsaved Changes` tampil
33. Klik `[Leave]`

### TC-GS-UCF-472: Rename value Dropdown ke label yang sama setelah trim ditolak sebagai duplikat

34. Klik `⋯` pada baris `Edit Dup DD {runId}-032`, pilih `Edit`
35. Klik teks badge `Beta` di Dropdown Values, ubah menjadi ` ALPHA ` (spasi di kedua tepi), tekan Enter
36. Verifikasi error inline `Option name already exists`
37. Verifikasi perubahan dibatalkan dan badge kembali `Beta`
38. Klik `[✕]`

### TC-GS-UCF-458: Placeholder 120 karakter dengan spasi di tepi diterima dan disimpan ter-trim

39. Klik `⋯` pada baris `Edit Trim Probe {runId}-032`, pilih `Edit`
40. Isi Placeholder dengan 2 spasi, lalu 120 karakter `A`, lalu 2 spasi
41. Verifikasi tidak ada error `Max. 120 characters` (panjang dihitung setelah trim: 120 karakter)
42. Klik `[Save]`
43. Verifikasi toast sukses: "Success, custom field has been updated."
44. Perhatikan kolom Placeholder baris `Edit Trim Probe {runId}-032`
45. Verifikasi kolom Placeholder menampilkan 120 karakter `A` tanpa spasi tepi

### TC-GS-UCF-333: Placeholder hanya berisi spasi pada Edit disimpan kosong

46. Klik `⋯` pada baris `Edit Ph Space {runId}-032`, pilih `Edit`
47. Hapus isi Placeholder, ketik 3 spasi
48. Klik `[Save]`
49. Verifikasi tidak ada error
50. Verifikasi toast sukses: "Success, custom field has been updated."
51. Verifikasi kolom Placeholder baris `Edit Ph Space {runId}-032` menampilkan nilai efektif default `Enter edit ph space {runId}-032`
52. Klik `⋯` pada baris `Edit Ph Space {runId}-032`, pilih `Edit`
53. Verifikasi Placeholder pada popup Edit kosong
54. Klik `[✕]`

### TC-GS-UCF-470: Placeholder dikosongkan pada Edit mencatat New Value `-` dan List memakai placeholder default

55. Klik `⋯` pada baris `Ph Clear Probe {runId}-032`, pilih `Edit`
56. Hapus seluruh isi Placeholder
57. Klik `[Save]`
58. Verifikasi toast sukses: "Success, custom field has been updated."
59. Perhatikan kolom Placeholder baris `Ph Clear Probe {runId}-032`
60. Verifikasi kolom Placeholder menampilkan nilai efektif default `Enter ph clear probe {runId}-032`
61. Buka Changelog Custom Field, Search `Ph Clear Probe {runId}-032`
62. Verifikasi Changelog memuat 1 entri Edit dengan Field `Ph Clear Probe {runId}-032 — Placeholder`, Old Value `Hint`, New Value `-`
63. Tutup Modal Changelog

### TC-GS-UCF-332: Emoji pada Field Name, rename value, dan Placeholder diblok saat Edit

64. Klik `⋯` pada baris `Edit Emoji DD {runId}-032`, pilih `Edit`
65. Kosongkan Field Name, ketik `😊`
66. Verifikasi Field Name tetap kosong (emoji tidak masuk lewat keystroke)
67. Tempel `Name {runId}-032 😊` pada Field Name
68. Verifikasi isi Field Name tidak memuat emoji (emoji tidak masuk lewat paste)
69. Klik teks badge `Alpha`, hapus isinya, ketik `😊`
70. Verifikasi input badge tetap kosong (emoji tidak masuk lewat keystroke)
71. Tempel `Alpha 🔥`, tekan Enter
72. Verifikasi badge tidak memuat emoji
73. Kosongkan Placeholder, ketik `😊`
74. Verifikasi Placeholder tetap kosong (emoji tidak masuk lewat keystroke)
75. Tempel `Hint 🌟` pada Placeholder
76. Verifikasi isi Placeholder tidak memuat emoji (emoji tidak masuk lewat paste)
77. Verifikasi tidak ada pesan error pada Field Name, Dropdown Values, dan Placeholder
78. Klik `[Save]`
79. Verifikasi toast sukses: "Success, custom field has been updated."
80. Verifikasi baris tampil dengan Field Name `Name {runId}-032`
81. Verifikasi Value Setting baris tersebut `Alpha`, `Beta`
82. Verifikasi Placeholder baris tersebut `Hint`

### TC-GS-UCF-335: Menambah value baru setelah error nilai Dropdown kosong membuat Save diterima

83. Klik `⋯` pada baris `Recover DD {runId}-032`, pilih `Edit`
84. Klik `×` pada badge `Solo`
85. Klik `[Save]`
86. Verifikasi error inline `Dropdown values must not be empty`
87. Periksa daftar request jaringan yang terekam sejak popup dibuka
88. Verifikasi daftar request tidak memuat request tulis ke server
89. Ketik `Duo`, tekan Enter
90. Klik `[Save]`
91. Verifikasi toast sukses: "Success, custom field has been updated."
92. Verifikasi Value Setting baris `Recover DD {runId}-032` menampilkan `Duo`

### TC-GS-UCF-471: Rename value Dropdown dengan spasi di tepi disimpan ter-trim

93. Klik `⋯` pada baris `Edit Trim DD {runId}-032`, pilih `Edit`
94. Klik teks badge `Beta` di Dropdown Values, ubah menjadi `  Gamma  ` (spasi di kedua tepi), tekan Enter
95. Verifikasi badge `Gamma` diterapkan di form tanpa spasi tepi
96. Verifikasi tidak ada error
97. Klik `[Save]`
98. Verifikasi toast sukses: "Success, custom field has been updated."
99. Verifikasi kolom Value Setting baris `Edit Trim DD {runId}-032` menampilkan badge `Alpha`, `Gamma`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (99 langkah). Seluruhnya satu kelas (fungsional, validasi popup Edit), satu akun, dan satu dataset; tiap blok memakai seed bersuffix sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain, dan jumlah langkah muncul dari satu baris per aksi dan satu `Verifikasi` per klausa Expected.
- Urutan TC: validasi yang diblokir lebih dulu (TC-GS-UCF-97, 334, 472), lalu aksi yang menyimpan (TC-GS-UCF-458, 333, 470, 332, 335, 471). Urutan berbeda dari TC sumber. TC-GS-UCF-97 memakai field seed sendiri (`Edit Meta Renamed {runId}-032`) sebagai pengganti hasil TC-GS-UCF-95 (S-04).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search `{runId}-032`, menutup popup lewat `✕` (pada form dirty ditulis `✕`, `Verifikasi` dialog `Unsaved Changes`, lalu `[Leave]`, S-08), membuka dan menutup Modal Changelog, serta membuka ulang popup Edit.
- Nama uji TC (`Edit Meta Renamed`, `Edit Trim Probe`, `Edit Ph Space`, `Ph Clear Probe`, `Edit Emoji DD`, `Edit Val Probe`, `Recover DD`, `Edit Trim DD`, `Edit Dup DD`) ditulis bersuffix `{runId}-032` (S-12). Pada TC-GS-UCF-332 teks tempel `Name 😊` ditulis `Name {runId}-032 😊` agar nama hasil tersimpan unik; hasil tersimpan `Name {runId}-032` setara dengan Expected `Name`.
- Pembagian TC lintas spec: TC-GS-UCF-98, 125 (Clear Field, penutupan popup Edit) ada di spec 034; Changelog pencatatan perubahan Placeholder lain ada di spec 067.
- Temuan untuk QA:
  - TC-GS-UCF-333 dan 470: Expected menulis nilai default `Enter edit ph space` dan `Enter ph clear probe` (turunan Field Name tanpa suffix). Spec memakai Field Name bersuffix sehingga nilai default yang diharapkan ditulis `Enter edit ph space {runId}-032` dan `Enter ph clear probe {runId}-032` (turunan Field Name lengkap). Perlu konfirmasi QA bahwa aturan default placeholder memakai seluruh Field Name termasuk bagian setelah angka atau tanda hubung.
  - TC-GS-UCF-458, 333, 470, 471: hasil simpan diasersi lewat kolom tabel sesuai Expected TC.
  - Keputusan NC-04 (Placeholder hanya-spasi di-trim dan disimpan kosong; nilai Dropdown kosong `Option name must not be empty`) dan NC-03 (emoji diblok) berbeda dari API/LLD; asersi mengikuti TC dan backend nyata dapat gagal sampai LLD diselaraskan.
  - TC-GS-UCF-332: Expected b menulis baris tampil sebagai `Name`; tidak ada Post Condition.
