---
id: TC-GS-UCF-E2E-065-changelog-column-visibility-dan-setup-column
title: "Modal Changelog Custom Field: Setup Column (Overlay, Hide dan Unhide, Reorder, Pin, Tutup Tanpa Simpan, Kolom Terakhir, Persistensi, dan Isolasi dari Tabel Utama)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-270
  - TC-GS-UCF-271
  - TC-GS-UCF-528
  - TC-GS-UCF-529
  - TC-GS-UCF-357
  - TC-GS-UCF-358
  - TC-GS-UCF-359
  - TC-GS-UCF-360
coverage:
  web: automated
---

# Modal Changelog Custom Field: Setup Column (Overlay, Hide dan Unhide, Reorder, Pin, Tutup Tanpa Simpan, Kolom Terakhir, Persistensi, dan Isolasi dari Tabel Utama)

## Prerequisites

- Mode: FE+BE (backend nyata; konfigurasi Setup Column tersimpan di cache browser).
- Akun aktor: Total Control Client A Sari Dewi (Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup TC). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Custom Field; `## Test Steps` tidak mengulang langkah buka kecuali sesudah muat ulang halaman.
- Data Pre-setup (baca-saja, tidak diubah spec ini): 6 Custom Field Pre-setup Client A dan Changelog Pre-setup 8 entri bertanggal 8 sampai 11 Sep 2026 (fixture backend). Data Population (8 Custom Field, 8 entri Create) dibuat lewat API oleh Sari Dewi di hook `before` bila belum ada (seeding idempotent); dipakai sebagai precondition TC, tidak diasersi.
- Setup Column default (precondition TC): Modal Changelog 6 kolom terlihat, urutan default, tanpa pin; tabel utama 8 kolom terlihat (`Active`, `Field Name`, `Data Type`, `Value Setting`, `Placeholder`, `Required`, `Modified By`, `Last Updated`), urutan default, tanpa pin. Hook `beforeEach` membersihkan cache browser; tiap TC yang mengubah konfigurasi memulihkannya lewat `[Reset to Default]` dan `[Save]` sebagai langkah eksplisit, dan hook `after` mengulangnya sebagai cadangan.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_<page_key>` true untuk akun aktor dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: drag and drop kolom pada Modal Setup Column; menggeser tabel secara horizontal; muat ulang halaman (F5); hover untuk tooltip.
- State global: tidak ada yang diubah selain flag Guided Tooltip dan konfigurasi Setup Column Changelog (dipulihkan seperti di atas).

## Test Steps

### TC-GS-UCF-270: Setup Column Modal Changelog: overlay dan modal enam kolom

1. Klik icon Changelog
2. Klik header Column Visibility (⋯)
3. Verifikasi overlay memuat enam kolom tercentang: `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
4. Verifikasi overlay memuat item `Setup Column...`
5. Klik `Setup Column...`
6. Verifikasi Title `Setup Column`
7. Verifikasi subtitle `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
8. Verifikasi enam kolom memiliki drag handle
9. Verifikasi enam kolom memiliki checkbox
10. Verifikasi enam kolom memiliki Pin
11. Verifikasi footer `[Reset to Default]` dan `[Save]` tanpa `[Cancel]`

### TC-GS-UCF-357: Tutup lewat [✕] atau Esc membuang perubahan

12. Uncheck `Old Value`
13. Klik `[✕]`
14. Verifikasi tabel Changelog tetap menampilkan kolom `Old Value`
15. Klik header Column Visibility (⋯), klik `Setup Column...`
16. Uncheck `Old Value`
17. Tekan Esc
18. Verifikasi tabel Changelog tetap menampilkan kolom `Old Value`

### TC-GS-UCF-358: Kolom terakhir yang tersisa tidak dapat di-uncheck

19. Klik header Column Visibility (⋯), klik `Setup Column...`
20. Uncheck satu per satu `Date`, `Action`, `Field`, `Old Value`, dan `New Value` sampai tersisa `Modified By`
21. Hover checkbox `Modified By`
22. Verifikasi checkbox `Modified By` Disabled
23. Verifikasi tooltip `At least one column must remain visible.`
24. Klik `[✕]`
25. Verifikasi modal tertutup tanpa menyimpan
26. Verifikasi tabel Changelog menampilkan kolom `Date`, `Action`, `Field`, `Old Value`, `New Value`, dan `Modified By`

### TC-GS-UCF-271: Hide dan unhide enam kolom lalu Reset to Default

27. Klik header Column Visibility (⋯), klik `Setup Column...`
28. Uncheck `Date`
29. Verifikasi `Date` hilang dari Live Preview
30. Uncheck `Action`
31. Verifikasi `Action` hilang dari Live Preview
32. Uncheck `Field`
33. Verifikasi `Field` hilang dari Live Preview
34. Uncheck `Old Value`
35. Verifikasi `Old Value` hilang dari Live Preview
36. Uncheck `New Value`
37. Verifikasi `New Value` hilang dari Live Preview
38. Centang kembali `Date`
39. Verifikasi `Date` muncul lagi pada Live Preview
40. Centang kembali `Action`
41. Verifikasi `Action` muncul lagi pada Live Preview
42. Centang kembali `Field`
43. Verifikasi `Field` muncul lagi pada Live Preview
44. Centang kembali `Old Value`
45. Verifikasi `Old Value` muncul lagi pada Live Preview
46. Centang kembali `New Value`
47. Verifikasi `New Value` muncul lagi pada Live Preview
48. Uncheck `Modified By`, klik `[Save]`
49. Verifikasi tabel Changelog menampilkan `Date`, `Action`, `Field`, `Old Value`, dan `New Value` tanpa `Modified By`
50. Klik header Column Visibility (⋯), klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`
51. Verifikasi tabel Changelog menampilkan `Date`, `Action`, `Field`, `Old Value`, `New Value`, dan `Modified By` dengan urutan default

### TC-GS-UCF-528: Drag reorder enam kolom lalu Save

52. Klik header Column Visibility (⋯), klik `Setup Column...`
53. Seret `Action` ke posisi pertama
54. Verifikasi `Action` menjadi kolom pertama pada Live Preview
55. Seret `Field` ke posisi pertama
56. Verifikasi `Field` menjadi kolom pertama pada Live Preview
57. Seret `Old Value` ke posisi pertama
58. Verifikasi `Old Value` menjadi kolom pertama pada Live Preview
59. Seret `New Value` ke posisi pertama
60. Verifikasi `New Value` menjadi kolom pertama pada Live Preview
61. Seret `Modified By` ke posisi pertama
62. Verifikasi `Modified By` menjadi kolom pertama pada Live Preview
63. Seret `Date` (kolom pada posisi terakhir) ke posisi ketiga
64. Verifikasi urutan Live Preview: `Modified By`, `New Value`, `Date`, `Old Value`, `Field`, `Action`
65. Klik `[Save]`
66. Verifikasi tabel Changelog menampilkan urutan `Modified By`, `New Value`, `Date`, `Old Value`, `Field`, `Action`
67. Muat ulang halaman (F5), klik icon Changelog
68. Verifikasi urutan kolom bertahan: `Modified By`, `New Value`, `Date`, `Old Value`, `Field`, `Action`
69. Klik header Column Visibility (⋯), klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`

### TC-GS-UCF-529: Pin dan unpin enam kolom dengan batas tiga kolom

70. Klik header Column Visibility (⋯), klik `Setup Column...`
71. Pin `Date`, `Action`, dan `Field`
72. Hover icon Pin kolom `Old Value`
73. Verifikasi icon Pin `Old Value` Disabled
74. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
75. Klik `[Save]`, geser tabel horizontal
76. Verifikasi `Date`, `Action`, dan `Field` membeku di kiri dan tetap saat tabel digeser horizontal
77. Muat ulang halaman (F5), klik icon Changelog
78. Verifikasi `Date`, `Action`, dan `Field` tetap membeku di kiri setelah muat ulang
79. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Date`
80. Hover icon Pin kolom `Old Value`
81. Verifikasi icon Pin `Old Value` kembali aktif
82. Unpin `Action` dan `Field`, klik `[Save]`
83. Verifikasi tidak ada kolom yang membeku
84. Klik header Column Visibility (⋯), klik `Setup Column...`, pin `Old Value`, `New Value`, dan `Modified By`, klik `[Save]`, geser tabel horizontal
85. Verifikasi `Old Value`, `New Value`, dan `Modified By` membeku di kiri dan tetap saat tabel digeser horizontal
86. Muat ulang halaman (F5), klik icon Changelog
87. Verifikasi `Old Value`, `New Value`, dan `Modified By` tetap membeku di kiri setelah muat ulang
88. Klik header Column Visibility (⋯), klik `Setup Column...`, unpin `Old Value`, `New Value`, dan `Modified By`, klik `[Save]`
89. Verifikasi tidak ada kolom yang membeku
90. Klik header Column Visibility (⋯), klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`

### TC-GS-UCF-359: Konfigurasi tersimpan setelah muat ulang

91. Klik header Column Visibility (⋯), klik `Setup Column...`, uncheck `Old Value` dan `New Value`, klik `[Save]`
92. Muat ulang halaman (F5), klik icon Changelog
93. Verifikasi tabel Changelog tidak menampilkan kolom `Old Value`
94. Verifikasi tabel Changelog tidak menampilkan kolom `New Value`
95. Klik header Column Visibility (⋯), klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`

### TC-GS-UCF-360: Konfigurasi kolom Modal Changelog tidak memengaruhi tabel utama

96. Klik header Column Visibility (⋯), klik `Setup Column...`, uncheck `Modified By`, klik `[Save]`
97. Tutup Modal Changelog dengan klik `[✕]`
98. Verifikasi header tabel utama menampilkan delapan kolom: `Active`, `Field Name`, `Data Type`, `Value Setting`, `Placeholder`, `Required`, `Modified By`, `Last Updated`
99. Klik icon Changelog, klik header Column Visibility (⋯), klik `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`
100. Klik `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 270, 357, 358, 271, 528, 529, 359, 360. Urutan menyimpang dari urutan TC sumber: screening overlay (270) di awal, kasus yang menutup tanpa menyimpan (357, 358) sebelum kasus yang menyimpan, dan kasus yang memuat ulang halaman (528, 529, 359) sesudahnya; TC-GS-UCF-360 di akhir karena memeriksa tabel utama. Tiap TC yang menyimpan perubahan memulihkan konfigurasi lewat `[Reset to Default]` dan `[Save]` sebagai langkah tanpa `Verifikasi` (langkah 50, 69, 90, 95, 99), sehingga TC berikutnya mulai dari default (S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka modal), langkah 12, 16 (mengubah checkbox sebelum menutup tanpa menyimpan), langkah 67, 77, 86, 92 (muat ulang lalu membuka modal), langkah 97 dan 100 (menutup modal lewat `[✕]`; tanpa dialog), langkah 99 (pemulihan konfigurasi Changelog).
- Langkah 28 sampai 47 mengulang satu pola per kolom (uncheck atau centang, lalu `Verifikasi` Live Preview) untuk lima kolom; `Verifikasi` tetap satu per klausa (S-01) karena Expected a dan b TC-GS-UCF-271 menuntut hilang dan muncul "satu per satu".
- Spec melewati sekitar 35 langkah (100 langkah). Seluruhnya satu kelas (Setup Column Modal Changelog, satu dataset baca-saja); tiap blok TC dimulai dari konfigurasi default sehingga berdiri sendiri, dan kegagalan satu blok tidak menghilangkan makna blok lain.
- Topik satu dataset Changelog dipertahankan sebagai spec terpisah (lihat Notes spec 061).
- Temuan untuk QA:
  - TC-GS-UCF-270 menyebut item overlay `Setup Column...` tanpa menyatakan apakah overlay menyertakan checkbox yang sama dengan modal; spec mengasersi enam kolom tercentang dan item `Setup Column...` sesuai TC.
  - TC-GS-UCF-529 langkah 5, 8: menggeser tabel horizontal bergantung pada lebar viewport; tidak ada ukuran viewport yang disebut TC sehingga kemampuan menggeser horizontal dinyatakan sebagai kemampuan teknis tim FE.
  - TC-GS-UCF-358 menguji kolom terakhir dengan `[✕]` setelah seluruh uncheck; TC tidak menyebut hover pada checkbox, sedangkan Expected a memerlukan tooltip. Spec menambahkan hover sebagai langkah penghubung (langkah 21).
  - TC-GS-UCF-360 memiliki dua precondition konfigurasi default (tabel utama dan Modal Changelog); dipenuhi hook `beforeEach` (cache dibersihkan).
