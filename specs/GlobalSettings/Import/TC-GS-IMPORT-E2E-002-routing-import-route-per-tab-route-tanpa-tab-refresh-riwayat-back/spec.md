---
id: TC-GS-IMPORT-E2E-002-routing-import-route-per-tab-route-tanpa-tab-refresh-riwayat-back
title: "Routing Import: Route per Tab, Route Tanpa Tab, Refresh, Riwayat Back, Breadcrumb Non-Klik, dan Detail Notifikasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-9
  - TC-GS-IMPORT-10
  - TC-GS-IMPORT-11
  - TC-GS-IMPORT-12
  - TC-GS-IMPORT-13
  - TC-GS-IMPORT-14
coverage:
  web: automated
---

# Routing Import: Route per Tab, Route Tanpa Tab, Refresh, Riwayat Back, Breadcrumb Non-Klik, dan Detail Notifikasi

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`); lihat `suite.md`.
- Akun aktor:
  - Total Control (Client A, Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-9 sampai 13. Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`.
  - Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net` (Pre-setup) untuk TC-GS-IMPORT-14: login lewat langkah ganti akun eksplisit dengan `Spectra.env.GS_CLIENTE_TC_PASSWORD` (env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Hook `after` mengembalikan sesi ke Total Control Client A.
  - Password tidak ditulis di spec atau fixture.
- Layar awal: spec ini menguji navigasi sehingga membuka menu Import lewat langkah sendiri; hook `beforeEach` suite hanya mereset client dan draft.
- Data Dinamis (disiapkan oleh langkah 1 lewat skrip fixture; nama literal Population):
  - D-01: draft Brand 12 baris `pending` (`brand-12.csv`) pada Client A.
  - D-04: draft Division 6 baris `pending` (`division-6.csv`, baris pertama `Finance & Accounting`) pada Client A.
  - D-19 (b): notifikasi lonceng akun Total Control Client E berjudul "Import Division completed" dengan isi "6 records imported." dan tombol `[Detail]`, disiapkan skrip fixture tanpa menjalankan commit lewat UI; Client E dalam keadaan commit tuntas tanpa draft Brand (D-19 a).
- Reset dan cleanup: hook `beforeEach` mereset draft dasar Client A (Kontrak Fixture R2) dan Client E sebelum langkah 1; langkah 1 menyiapkan seed D-01, D-04, dan D-19 sesudah reset itu; hook `after` menghapus notifikasi seed bila masih ada (tidak berasumsi seeding berhasil penuh).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: salin URL dan buka di tab browser baru; tombol Back browser; muat ulang (F5); buka alamat route tanpa segmen tab; skrip seed draft dan notifikasi (disediakan tim FE/BE); ganti akun.
- State global: tidak ada yang diubah selain draft/notifikasi seed (dipulihkan hook).

## Test Steps

### TC-GS-IMPORT-9: Membuka URL tab Division langsung menampilkan Sub-Tab Division

1. Reset Client A dan Client E; seed draft Brand D-01 dan draft Division D-04 pada Client A, serta notifikasi lonceng D-19 (b) dan keadaan commit tuntas tanpa draft Brand (D-19 a) pada Client E, lewat skrip fixture
2. Buka menu Import dari sidebar
3. Klik Sub-Tab Division
4. Salin URL halaman
5. Buka URL itu di tab browser baru
6. Perhatikan halaman pada tab baru
7. Verifikasi Sub-Tab `Division` aktif
8. Verifikasi Breadcrumb `Import > Division`
9. Verifikasi Staging Metric Cards menampilkan Total Rows 6
10. Verifikasi Staging Metric Cards menampilkan Ready to Import 6
11. Verifikasi Staging DataTable menampilkan 6 baris Division
12. Verifikasi `Finance & Accounting` berada pada `Row #` 1 (bukan baris Brand)
13. Tutup tab baru dan kembali ke tab asal (Import > Division)

### TC-GS-IMPORT-13: Segmen Breadcrumb dua segmen tidak ada yang dapat diklik

14. Klik segmen `Import` pada Breadcrumb
15. Perhatikan halaman, Sub-Tab aktif, dan URL
16. Verifikasi klik segmen `Import` tidak berpindah halaman atau tab: Sub-Tab `Division` tetap aktif
17. Verifikasi URL tidak berubah setelah klik segmen `Import`
18. Klik segmen `Division` pada Breadcrumb
19. Perhatikan halaman, Sub-Tab aktif, dan URL
20. Verifikasi klik segmen `Division` tidak berpindah halaman atau tab: Sub-Tab `Division` tetap aktif
21. Verifikasi URL tidak berubah setelah klik segmen `Division`

### TC-GS-IMPORT-11: Refresh pada URL tab Measurement memuat tab Measurement

22. Klik Sub-Tab Measurement
23. Muat ulang halaman (F5)
24. Perhatikan Sub-Tab aktif, Breadcrumb, dan URL
25. Verifikasi Sub-Tab `Measurement` tetap aktif
26. Verifikasi Breadcrumb `Import > Measurement`
27. Verifikasi URL tetap route tab Measurement

### TC-GS-IMPORT-10: Route tanpa tab membuka Sub-Tab Brand

28. Buka alamat route halaman Import tanpa segmen tab (URL menu Import dengan akhiran nama tab dihapus)
29. Perhatikan Sub-Tab aktif, Breadcrumb, dan URL
30. Verifikasi Sub-Tab `Brand` aktif
31. Verifikasi Breadcrumb `Import > Brand`
32. Verifikasi URL beralih ke route tab Brand

### TC-GS-IMPORT-12: Berpindah Sub-Tab menambah riwayat browser sehingga Back kembali ke tab sebelumnya

33. Klik Sub-Tab Division
34. Klik Sub-Tab Position
35. Tekan tombol Back browser
36. Perhatikan Sub-Tab aktif dan Breadcrumb
37. Verifikasi Sub-Tab `Division` aktif
38. Verifikasi Breadcrumb `Import > Division`
39. Tekan tombol Back browser lagi
40. Perhatikan Sub-Tab aktif dan Breadcrumb
41. Verifikasi Sub-Tab `Brand` aktif
42. Verifikasi Breadcrumb `Import > Brand`

### TC-GS-IMPORT-14: Tombol Detail pada notifikasi membuka route tab Import Type yang bersangkutan

43. Ganti akun: logout dari Total Control Client A
44. Login sebagai Total Control Client E dengan `Spectra.env.GS_CLIENTE_TC_PASSWORD`
45. Buka menu Import dari sidebar (User berada di Import > Brand)
46. Buka notifikasi lonceng
47. Klik `[Detail]` pada "Import Division completed"
48. Perhatikan halaman Import
49. Verifikasi halaman Import terbuka pada route tab Division: Sub-Tab `Division` aktif
50. Verifikasi Breadcrumb `Import > Division`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 9, 13, 11, 10, 12, 14. Urutan ini menyimpang dari urutan TC sumber supaya state perantara terpakai ulang tanpa navigasi tambahan: TC-GS-IMPORT-13 membutuhkan user di Import > Division (state akhir TC-GS-IMPORT-9 di tab asal), TC-GS-IMPORT-10 mengembalikan ke Brand yang dibutuhkan precondition TC-GS-IMPORT-12, dan TC-GS-IMPORT-14 terakhir karena ganti akun ke Client E.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (reset dan seed lewat skrip fixture sinkron, tanpa penanda tunggu), langkah 13 (tutup tab baru), langkah 15, 19, 24, 29, 36, 40, dan 48 (mengamati sesuai Langkah Uji TC), langkah 43 dan 44 (ganti akun).
- Spec melewati sekitar 35 langkah (50 langkah). Seluruhnya satu topik (routing halaman Import, tanpa aksi yang mengubah data); tiap blok TC berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain; blok pada akun lain (TC-GS-IMPORT-14) berada di akhir dengan langkah ganti akun eksplisit.
- Kelas campur: spec ini berkelas a (fungsional routing), tetapi TC-GS-IMPORT-9 membuka tab browser baru dan mengasersi isinya (langkah 6 sampai 12), sehingga konteks kedua (kelas c) menjadi objek asersi. Belum ada id pengecualian: konteks kedua beraksi di spec kelas a; usulan aturan baru menunggu batch konvensi. Tab baru ditutup di langkah 13 dan hanya TC-GS-IMPORT-9 yang memakainya.
- Temuan untuk QA:
  - TC-GS-IMPORT-9, 14 memerlukan seed draft dan notifikasi lonceng (D-19) lewat skrip fixture yang tidak didefinisikan di TC, PRD, atau LLD; mekanismenya disediakan tim FE/BE (S-13).
  - TC-GS-IMPORT-14 tidak menyebut password/env akun Total Control Client E; env `GS_CLIENTE_TC_PASSWORD` baru.
  - Draft memakai nama literal Population tanpa suffix `{runId}`; keunikan dijaga lewat reset draft di hook.
