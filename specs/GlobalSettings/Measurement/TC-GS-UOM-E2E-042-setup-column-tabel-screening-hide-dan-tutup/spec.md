---
id: TC-GS-UOM-E2E-042-setup-column-tabel-screening-hide-dan-tutup
title: "Setup Column Tabel Measurement: Screening, Hide/Unhide, Guard Kolom Terakhir, Tutup Modal, dan Preferensi Per User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-157
  - TC-GS-UOM-158
  - TC-GS-UOM-162
  - TC-GS-UOM-163
  - TC-GS-UOM-164
  - TC-GS-UOM-295
  - TC-GS-UOM-385
coverage:
  web: automated
---

# Setup Column Tabel Measurement: Screening, Hide/Unhide, Guard Kolom Terakhir, Tutup Modal, dan Preferensi Per User

## Prerequisites

- Mode: mock (spec hanya-FE, dijalankan tim FE sebagai integration test; API di-mock, tanpa backend nyata).
- Flag Guided Tooltip halaman Measurement mengikuti pernyataan hook suite di `suite.md`.
- Respons daftar Brand dan API pendukung halaman Master Reference: disediakan tim FE (lihat `suite.md`, bagian Data bersama).
- Akun: Total Control Client A, Sari Dewi (Sari D), `totalControl_automated_qaTeam1@qwertysystem.net`. Sesi login disuntikkan lewat seedSession di hook `before` tanpa memanggil backend, sehingga tidak ada password yang dipakai di spec ini.
- Kebutuhan mock (endpoint dan respons yang dipaksa):
  - `POST /v2/enterprise-management/measurements/list` mengembalikan sedikitnya tiga unit (mis. Box / box, Dozen / dz, Gram / g) beserta Used By (Items) dan Last Updated, supaya kolom tabel Measurement terbaca; path berasal dari `tc-measurement-backend.md`.
  - Endpoint daftar Changelog Measurement (dipakai TC-GS-UOM-164 saat Modal Changelog dibuka) mengembalikan sedikitnya satu baris dengan seluruh kolom default Modal Changelog. Path endpoint ini: disediakan tim FE sesuai kontrak modul activity-log; rujukan `openapi.yaml` dan `low-level-design.md`: disediakan tim FE.
  - API pendukung di luar modul (identitas pengguna, menu, flag Guided Tooltip) disediakan tim FE.
- Preferensi kolom tabel (visibilitas, urutan, pin) "tersimpan per user" (PRD §4.2i, `prd-conventions.md` §9.3); mekanisme penyimpanannya tidak disebut PRD dan TC sehingga tidak ada endpoint yang di-mock untuknya. "Muat ulang halaman" (F5) dilakukan pada konteks browser yang sama supaya penyimpanan sisi klien tetap ada.
- Data: tidak ada data dinamis; tidak ada seeding backend.
- Tabel "Kolom tabel Measurement" (parameter langkah berulang): `Unit Name`, `Symbol`, `Used By (Items)`, `Last Updated`.
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom tabel Measurement dikembalikan ke default (Unit Name, Symbol, Used By (Items), Last Updated, semua tampil, tanpa pin) lewat penghapusan preferensi kolom tabel Measurement di browser (kemampuan disediakan tim FE, lihat Kemampuan teknis).
- Hook `beforeEach`: buka Global Settings > Master Reference > Measurement.
- Kemampuan teknis: `Spectra.intercept()` untuk respons daftar Measurement dan daftar Changelog; arahkan kursor ke checkbox disabled untuk membaca tooltip; muat ulang halaman; menghapus preferensi kolom tabel Measurement di browser (disediakan tim FE).

## Test Steps

### TC-GS-UOM-157: Screening Overlay Column Visibility tabel Measurement

1. Klik header kolom Actions (`⋯`)
2. Verifikasi panel Column Visibility berisi daftar kolom `Unit Name`, `Symbol`, `Used By (Items)`, `Last Updated`
3. Verifikasi checkbox keempat kolom tercentang dan enabled (Hideable)
4. Verifikasi keempat kolom memiliki drag handle
5. Verifikasi item `Setup Column...` tampil di bawah daftar
6. Verifikasi kolom Checkbox dan Actions tidak muncul sebagai baris pada daftar

### TC-GS-UOM-295: Screening Popup Setup Column tabel Measurement

7. Klik `Setup Column...`
8. Verifikasi **Header**: Title `Setup Column`, subtitle `Manage column visibility, reorder, and freeze columns.`, dan icon close `[✕]`
9. Verifikasi **Body**: kolom search `Search column name...`
10. Verifikasi **Body**: daftar kolom `Unit Name`, `Symbol`, `Used By (Items)`, `Last Updated`, masing-masing dengan checkbox tercentang dan enabled (Hideable)
11. Verifikasi **Body**: masing-masing kolom memiliki drag handle `⠿`
12. Verifikasi **Body**: masing-masing kolom memiliki icon Pin
13. Verifikasi **Footer** (rata kanan): `[Reset to Default]` (text, primary) dan `[Save]` (filled, success)
14. Verifikasi tidak ada tombol `[Cancel]`
15. Klik `[✕]`

### TC-GS-UOM-158: Hide dan unhide tiap kolom tabel Measurement lewat panel dan modal

16. Klik header kolom Actions (`⋯`)
17. Untuk setiap kolom pada tabel "Kolom tabel Measurement" (langkah 18 sampai 21):
18. Uncheck kolom di panel Column Visibility
19. Verifikasi kolom langsung hilang dari tabel tanpa tombol simpan
20. Check kembali kolom di panel Column Visibility
21. Verifikasi kolom kembali tampil di tabel
22. Klik `Setup Column...`
23. Untuk setiap kolom pada tabel "Kolom tabel Measurement" (langkah 24 sampai 27):
24. Uncheck kolom di modal Setup Column
25. Verifikasi kolom hilang pada preview tabel
26. Check kembali kolom di modal
27. Verifikasi kolom kembali tampil pada preview tabel
28. Uncheck `Symbol` di modal, klik [Save]
29. Verifikasi modal tertutup
30. Verifikasi kolom Symbol tidak tampil di tabel
31. Muat ulang halaman (F5)
32. Verifikasi kolom Unit Name tampil di tabel
33. Verifikasi kolom Symbol tetap tidak tampil setelah muat ulang
34. Klik header kolom Actions (`⋯`), klik `Setup Column...`
35. Check `Symbol`, klik [Save]
36. Verifikasi kolom Symbol tampil kembali

### TC-GS-UOM-385: Hide dan unhide kolom Used By (Items)

37. Klik header kolom Actions (`⋯`)
38. Verifikasi checkbox `Used By (Items)` enabled (Hideable)
39. Uncheck `Used By (Items)` di panel Column Visibility
40. Verifikasi kolom Used By (Items) langsung hilang dari tabel tanpa tombol simpan
41. Check kembali `Used By (Items)`
42. Verifikasi kolom Used By (Items) kembali tampil
43. Klik `Setup Column...`, uncheck `Used By (Items)`, klik [Save]
44. Muat ulang halaman (F5)
45. Verifikasi kolom Unit Name tampil di tabel
46. Verifikasi kolom Used By (Items) tetap tersembunyi
47. Klik header kolom Actions (`⋯`), klik `Setup Column...`
48. Check `Used By (Items)`, klik [Save]
49. Verifikasi kolom Used By (Items) tampil kembali

### TC-GS-UOM-163: Kolom visible terakhir tidak dapat di-uncheck

50. Klik header kolom Actions (`⋯`)
51. Uncheck `Symbol`, `Used By (Items)`, dan `Last Updated` di panel Column Visibility sehingga hanya `Unit Name` visible
52. Arahkan kursor ke checkbox `Unit Name` di panel
53. Verifikasi checkbox `Unit Name` disabled (tetap tampil) di panel Column Visibility
54. Verifikasi tooltip `At least one column must remain visible.` tampil pada checkbox `Unit Name` di panel Column Visibility
55. Klik `Setup Column...`
56. Arahkan kursor ke checkbox `Unit Name` di modal
57. Verifikasi checkbox `Unit Name` pada modal Setup Column disabled
58. Verifikasi tooltip `At least one column must remain visible.` tampil pada checkbox `Unit Name` pada modal Setup Column
59. Klik `[✕]`
60. Klik header kolom Actions (`⋯`)
61. Check kembali `Symbol`, `Used By (Items)`, dan `Last Updated` di panel
62. Verifikasi kolom Unit Name, Symbol, dan Last Updated tampil di tabel

### TC-GS-UOM-164: Preferensi kolom tersimpan per user dan tidak memengaruhi tabel Changelog

63. Klik Changelog
64. Baca daftar kolom Modal Changelog sebagai pembanding
65. Tutup Modal Changelog lewat `[✕]`
66. Klik header kolom Actions (`⋯`), uncheck `Symbol` di panel Column Visibility
67. Muat ulang halaman (F5)
68. Verifikasi kolom Unit Name tampil di tabel
69. Verifikasi kolom Symbol tetap ter-hide setelah muat ulang
70. Klik Changelog
71. Verifikasi kolom Modal Changelog tidak berubah dari pembanding
72. Tutup Modal Changelog lewat `[✕]`
73. Klik header kolom Actions (`⋯`), check kembali `Symbol`

### TC-GS-UOM-162: Menutup modal Setup Column tanpa Save membuang perubahan preview

74. Klik header kolom Actions (`⋯`), klik `Setup Column...`
75. Uncheck `Symbol`
76. Verifikasi preview tabel tanpa kolom Symbol
77. Klik `[✕]`
78. Verifikasi kolom Symbol kembali tampil di tabel
79. Klik header kolom Actions (`⋯`), klik `Setup Column...`
80. Uncheck `Symbol`
81. Verifikasi preview tabel tanpa kolom Symbol
82. Tekan Esc
83. Verifikasi kolom Symbol kembali tampil di tabel (hasil sama dengan `[✕]`)

## Notes

- Mode: mock. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (83 nominal; langkah 18 sampai 21 diulang 4 kali dan langkah 24 sampai 27 diulang 4 kali sesuai tabel "Kolom tabel Measurement", sehingga ekspansi lebih besar). Alasan: semua blok satu layar (Column Visibility dan Setup Column tabel utama) pada data mock yang sama, hanya kelas mock, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC dalam spec: 157, 295 (screening), 158, 385, 163, 164, 162 (urutan sumber 157, 158, 162, 163, 164, 295, 385). TC-GS-UOM-162 (menutup modal) di akhir spec.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 61 memulihkan visibilitas kolom; langkah 64 membaca daftar kolom Modal Changelog sebelum Symbol di-hide sebagai pembanding "tidak berubah" (TC-GS-UOM-164 tidak menyediakan baseline); langkah terakhir TC-GS-UOM-164 (check kembali `Symbol`) memulihkan state; langkah "Klik `Setup Column...`" dan "Klik header kolom Actions" membuka panel dan modal.
- TC-GS-UOM-158: Expected butir e menyebut modal untuk kolom Unit Name, Symbol, dan Last Updated, sedangkan langkah TC menyebut empat kolom; spec memakai keempat kolom pada langkah (Used By (Items) juga dicakup TC-GS-UOM-385) dan mengasersi preview untuk keempatnya.
- Langkah "Verifikasi preview tabel tanpa kolom Symbol" pada TC-GS-UOM-162 adalah asersi tambahan sebagai anchor positif bagi asersi "Symbol kembali tampil" (S-03). Langkah "Verifikasi kolom Unit Name tampil di tabel" sebelum asersi kolom lain yang tetap tersembunyi sesudah F5 adalah anchor positif absence (butir 2 bagian 8b).
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-UOM-163: Langkah 2 meng-uncheck `Symbol` dan `Last Updated` "sehingga hanya `Unit Name` visible", tetapi tabel memiliki empat kolom (Unit Name, Symbol, Used By (Items), Last Updated); `Used By (Items)` tetap visible sehingga syarat "kolom visible terakhir" tidak tercapai. Spec juga meng-uncheck `Used By (Items)` (langkah 51) dan mengembalikannya di langkah 61; Expected butir c hanya menyebut tiga kolom.
  - TC-GS-UOM-164: Expected "Kolom Modal Changelog tidak berubah" tidak menyebut baseline; spec membaca daftar kolom sebelum aksi hide sebagai pembanding.
  - Mekanisme penyimpanan preferensi kolom per user (penyimpanan klien atau API) tidak disebut PRD maupun TC; bila disimpan lewat API, spec mock ini perlu daftar endpoint penyimpanan dari `openapi.yaml` / `low-level-design.md`.
