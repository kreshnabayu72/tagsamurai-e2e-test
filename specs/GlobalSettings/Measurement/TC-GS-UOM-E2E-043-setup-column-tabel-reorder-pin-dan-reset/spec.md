---
id: TC-GS-UOM-E2E-043-setup-column-tabel-reorder-pin-dan-reset
title: "Setup Column Tabel Measurement: Reorder (Modal dan Panel), Pin, dan Reset to Default"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-159
  - TC-GS-UOM-160
  - TC-GS-UOM-161
  - TC-GS-UOM-349
coverage:
  web: automated
---

# Setup Column Tabel Measurement: Reorder (Modal dan Panel), Pin, dan Reset to Default

## Prerequisites

- Mode: mock (spec hanya-FE, dijalankan tim FE sebagai integration test; API di-mock, tanpa backend nyata).
- Flag Guided Tooltip halaman Measurement mengikuti pernyataan hook suite di `suite.md`.
- Respons daftar Brand dan API pendukung halaman Master Reference: disediakan tim FE (lihat `suite.md`, bagian Data bersama).
- Akun: Total Control Client A, Sari Dewi (Sari D), `totalControl_automated_qaTeam1@qwertysystem.net`. Sesi login disuntikkan lewat seedSession di hook `before` tanpa memanggil backend, sehingga tidak ada password yang dipakai di spec ini.
- Kebutuhan mock (endpoint dan respons yang dipaksa): `POST /v2/enterprise-management/measurements/list` mengembalikan sedikitnya tiga unit (mis. Box / box, Dozen / dz, Gram / g) beserta Used By (Items) dan Last Updated, supaya kolom tabel Measurement terbaca; path berasal dari `tc-measurement-backend.md`. Rujukan ke `openapi.yaml` dan `low-level-design.md`: disediakan tim FE. API pendukung di luar modul (identitas pengguna, menu, flag Guided Tooltip) disediakan tim FE.
- Preferensi kolom tabel (urutan, visibilitas, pin) "tersimpan per user" (PRD §4.2i, `prd-conventions.md` §9.3); mekanisme penyimpanannya tidak disebut PRD dan TC sehingga tidak ada endpoint yang di-mock untuknya. "Muat ulang halaman" (F5) dilakukan pada konteks browser yang sama supaya penyimpanan sisi klien tetap ada.
- Data: tidak ada data dinamis; tidak ada seeding backend.
- Tabel "Kolom tabel Measurement" (parameter langkah berulang pada TC-GS-UOM-160): `Unit Name`, `Symbol`, `Used By (Items)`, `Last Updated`.
- Lebar konten tabel melebihi lebar viewport (overflow horizontal) agar scroll horizontal teramati (TC-GS-UOM-160): viewport diperkecil sampai tabel dapat di-scroll horizontal dan dikembalikan ke ukuran awal sesudahnya (hook `after` sebagai cadangan).
- State global yang dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom tabel Measurement dikembalikan ke default (urutan Unit Name, Symbol, Used By (Items), Last Updated, semua tampil, tanpa pin) lewat penghapusan preferensi kolom tabel Measurement di browser (kemampuan disediakan tim FE, lihat Kemampuan teknis); viewport dikembalikan.
- Hook `beforeEach`: buka Global Settings > Master Reference > Measurement.
- Kemampuan teknis: `Spectra.intercept()` untuk respons daftar Measurement; drag and drop elemen (baris di panel Column Visibility dan di modal Setup Column); mengatur viewport; scroll horizontal tabel; muat ulang halaman; menghapus preferensi kolom tabel Measurement di browser (disediakan tim FE).

## Test Steps

### TC-GS-UOM-349: Reorder kolom lewat drag di panel Column Visibility ter-apply langsung dan tersimpan

1. Klik header kolom Actions (`⋯`) sehingga panel Column Visibility terbuka
2. Geser `Last Updated` ke atas `Unit Name` di panel
3. Verifikasi urutan header tabel langsung `Last Updated`, `Unit Name`, `Symbol`, `Used By (Items)` tanpa tombol Save
4. Geser `Symbol` ke posisi paling bawah di panel
5. Verifikasi urutan header `Last Updated`, `Unit Name`, `Used By (Items)`, `Symbol` dengan `Symbol` paling bawah
6. Muat ulang halaman (F5)
7. Verifikasi urutan header tetap `Last Updated`, `Unit Name`, `Used By (Items)`, `Symbol`
8. Klik header kolom Actions (`⋯`), klik `Setup Column...`
9. Klik [Reset to Default]
10. Klik [Save]
11. Verifikasi urutan header kembali `Unit Name`, `Symbol`, `Used By (Items)`, `Last Updated`

### TC-GS-UOM-159: Reorder tiap kolom lewat drag dan persist setelah F5

12. Klik header kolom Actions (`⋯`), klik `Setup Column...`
13. Geser `Symbol` ke atas `Unit Name`
14. Verifikasi urutan `Symbol`, `Unit Name`, `Used By (Items)`, `Last Updated`
15. Geser `Last Updated` ke posisi paling atas
16. Verifikasi urutan `Last Updated`, `Symbol`, `Unit Name`, `Used By (Items)`
17. Geser `Unit Name` ke posisi paling bawah
18. Verifikasi urutan `Last Updated`, `Symbol`, `Used By (Items)`, `Unit Name` dengan `Unit Name` paling bawah
19. Klik [Save]
20. Verifikasi urutan header kolom tabel `Last Updated`, `Symbol`, `Used By (Items)`, `Unit Name`
21. Muat ulang halaman (F5)
22. Verifikasi urutan header kolom tabel tetap `Last Updated`, `Symbol`, `Used By (Items)`, `Unit Name`
23. Klik header kolom Actions (`⋯`), klik `Setup Column...`
24. Klik [Reset to Default]
25. Klik [Save]
26. Verifikasi urutan kembali `Unit Name`, `Symbol`, `Used By (Items)`, `Last Updated`

### TC-GS-UOM-160: Pin tiap kolom membekukan posisinya saat scroll horizontal

27. Perkecil viewport hingga tabel dapat di-scroll horizontal
28. Untuk setiap kolom pada tabel "Kolom tabel Measurement" (langkah 29 sampai 38):
29. Klik header kolom Actions (`⋯`), klik `Setup Column...`
30. Klik icon Pin kolom
31. Klik [Save]
32. Scroll tabel horizontal
33. Verifikasi kolom tetap di posisinya saat tabel di-scroll horizontal
34. Klik header kolom Actions (`⋯`), klik `Setup Column...`
35. Klik icon Pin kolom untuk unpin
36. Klik [Save]
37. Scroll tabel horizontal
38. Verifikasi kolom kembali ikut bergeser saat tabel di-scroll horizontal
39. Klik header kolom Actions (`⋯`), klik `Setup Column...`
40. Klik icon Pin `Unit Name`
41. Klik [Save]
42. Muat ulang halaman (F5)
43. Scroll tabel horizontal
44. Verifikasi kolom Unit Name tetap di posisinya setelah F5
45. Klik header kolom Actions (`⋯`), klik `Setup Column...`
46. Klik icon Pin `Unit Name` untuk unpin
47. Klik [Save]
48. Scroll tabel horizontal
49. Verifikasi tidak ada kolom ter-pin (seluruh kolom ikut bergeser saat di-scroll)
50. Kembalikan viewport ke ukuran awal

### TC-GS-UOM-161: Reset to Default mengembalikan susunan default

51. Klik header kolom Actions (`⋯`), klik `Setup Column...`
52. Geser `Last Updated` ke posisi paling atas
53. Uncheck `Symbol`
54. Klik [Save]
55. Klik header kolom Actions (`⋯`), klik `Setup Column...`
56. Klik [Reset to Default]
57. Klik [Save]
58. Verifikasi kolom Unit Name, Symbol, Used By (Items), Last Updated semua tampil
59. Verifikasi urutan kolom Unit Name, Symbol, Used By (Items), Last Updated sama dengan urutan default
60. Muat ulang halaman (F5)
61. Verifikasi kolom Unit Name, Symbol, Used By (Items), Last Updated semua tampil setelah muat ulang
62. Verifikasi urutan kolom Unit Name, Symbol, Used By (Items), Last Updated sama dengan urutan default setelah muat ulang

## Notes

- Mode: mock. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec melewati sekitar 35 langkah (62 nominal; langkah 29 sampai 38 diulang 4 kali sesuai tabel "Kolom tabel Measurement", sehingga ekspansi lebih besar). Alasan: semua blok satu layar (Setup Column tabel utama: urutan, pin, reset) pada data mock yang sama dan hanya kelas mock; tiap blok diakhiri `[Reset to Default]` atau unpin sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC dalam spec: 349, 159, 160, 161 (urutan sumber 159, 160, 161, 349); reorder lewat panel (ter-apply langsung) mendahului reorder lewat modal, `[Reset to Default]` TC-GS-UOM-161 di akhir.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 27 dan 50 (memperkecil dan mengembalikan viewport supaya scroll horizontal teramati, precondition TC-GS-UOM-160); langkah "Klik header kolom Actions (`⋯`), klik `Setup Column...`" membuka panel dan modal; langkah "Geser `Last Updated` ... `Uncheck Symbol` ... [Save]" pada TC-GS-UOM-161 membentuk precondition "Ubah urutan dan visibilitas" (TC memakai satu butir "Ubah urutan dan visibilitas" tanpa nilai; spec memilih geser Last Updated ke atas dan uncheck Symbol).
- Pin diverifikasi lewat scroll horizontal tabel; kolom ter-pin tetap di posisinya, kolom tidak ter-pin ikut bergeser.
- Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-UOM-161 langkah 1 "Ubah urutan dan visibilitas" tanpa Data Uji; spec memilih perubahan (Last Updated ke atas dan Symbol di-hide) agar keadaan awal berbeda dari default.
  - Mekanisme penyimpanan preferensi kolom per user (penyimpanan klien atau API) tidak disebut PRD maupun TC; bila disimpan lewat API, spec mock ini perlu daftar endpoint penyimpanan dari `openapi.yaml` / `low-level-design.md`.
  - TC-GS-UOM-160 tidak menyebut ukuran viewport; spec hanya menulis "diperkecil hingga tabel dapat di-scroll horizontal".
