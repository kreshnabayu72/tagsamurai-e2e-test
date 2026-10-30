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
- Data Dinamis (skrip fixture di hook `before`; nama literal Population):
  - D-01: draft Brand 12 baris `pending` (`brand-12.csv`) pada Client A.
  - D-04: draft Division 6 baris `pending` (`division-6.csv`, baris pertama `Finance & Accounting`) pada Client A.
  - D-19 (b): notifikasi lonceng akun Total Control Client E berjudul "Import Division completed" dengan isi "6 records imported." dan tombol `[Detail]`, disiapkan skrip fixture tanpa menjalankan commit lewat UI; Client E dalam keadaan commit tuntas tanpa draft Brand (D-19 a).
- Reset dan cleanup: hook `beforeEach` mereset draft dasar Client A (Kontrak Fixture R2) dan Client E; hook `after` menghapus notifikasi seed bila masih ada (tidak berasumsi seeding berhasil penuh).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Kemampuan teknis: salin URL dan buka di tab browser baru; tombol Back browser; muat ulang (F5); buka alamat route tanpa segmen tab; skrip seed draft dan notifikasi (disediakan tim FE/BE); ganti akun.
- State global: tidak ada yang diubah selain draft/notifikasi seed (dipulihkan hook).

## Test Steps

### TC-GS-IMPORT-9: Membuka URL tab Division langsung menampilkan Sub-Tab Division

1. Buka menu Import dari sidebar
2. Klik Sub-Tab Division
3. Salin URL halaman
4. Buka URL itu di tab browser baru
5. Perhatikan halaman pada tab baru
6. Verifikasi Sub-Tab `Division` aktif
7. Verifikasi Breadcrumb `Import > Division`
8. Verifikasi Staging Metric Cards menampilkan Total Rows 6
9. Verifikasi Staging Metric Cards menampilkan Ready to Import 6
10. Verifikasi Staging DataTable menampilkan 6 baris Division
11. Verifikasi `Finance & Accounting` berada pada `Row #` 1 (bukan baris Brand)
12. Tutup tab baru dan kembali ke tab asal (Import > Division)

### TC-GS-IMPORT-13: Segmen Breadcrumb dua segmen tidak ada yang dapat diklik

13. Klik segmen `Import` pada Breadcrumb
14. Perhatikan halaman, Sub-Tab aktif, dan URL
15. Verifikasi klik segmen `Import` tidak berpindah halaman atau tab: Sub-Tab `Division` tetap aktif
16. Verifikasi URL tidak berubah setelah klik segmen `Import`
17. Klik segmen `Division` pada Breadcrumb
18. Perhatikan halaman, Sub-Tab aktif, dan URL
19. Verifikasi klik segmen `Division` tidak berpindah halaman atau tab: Sub-Tab `Division` tetap aktif
20. Verifikasi URL tidak berubah setelah klik segmen `Division`

### TC-GS-IMPORT-11: Refresh pada URL tab Measurement memuat tab Measurement

21. Klik Sub-Tab Measurement
22. Muat ulang halaman (F5)
23. Perhatikan Sub-Tab aktif, Breadcrumb, dan URL
24. Verifikasi Sub-Tab `Measurement` tetap aktif
25. Verifikasi Breadcrumb `Import > Measurement`
26. Verifikasi URL tetap route tab Measurement

### TC-GS-IMPORT-10: Route tanpa tab membuka Sub-Tab Brand

27. Buka alamat route halaman Import tanpa segmen tab (URL menu Import dengan akhiran nama tab dihapus)
28. Perhatikan Sub-Tab aktif, Breadcrumb, dan URL
29. Verifikasi Sub-Tab `Brand` aktif
30. Verifikasi Breadcrumb `Import > Brand`
31. Verifikasi URL beralih ke route tab Brand

### TC-GS-IMPORT-12: Berpindah Sub-Tab menambah riwayat browser sehingga Back kembali ke tab sebelumnya

32. Klik Sub-Tab Division
33. Klik Sub-Tab Position
34. Tekan tombol Back browser
35. Perhatikan Sub-Tab aktif dan Breadcrumb
36. Verifikasi Sub-Tab `Division` aktif
37. Verifikasi Breadcrumb `Import > Division`
38. Tekan tombol Back browser lagi
39. Perhatikan Sub-Tab aktif dan Breadcrumb
40. Verifikasi Sub-Tab `Brand` aktif
41. Verifikasi Breadcrumb `Import > Brand`

### TC-GS-IMPORT-14: Tombol Detail pada notifikasi membuka route tab Import Type yang bersangkutan

42. Ganti akun: logout dari Total Control Client A
43. Login sebagai Total Control Client E dengan `Spectra.env.GS_CLIENTE_TC_PASSWORD`
44. Buka menu Import dari sidebar (User berada di Import > Brand)
45. Buka notifikasi lonceng
46. Klik `[Detail]` pada "Import Division completed"
47. Perhatikan halaman Import
48. Verifikasi halaman Import terbuka pada route tab Division: Sub-Tab `Division` aktif
49. Verifikasi Breadcrumb `Import > Division`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC: 9, 13, 11, 10, 12, 14. Urutan ini menyimpang dari urutan TC sumber supaya state perantara terpakai ulang tanpa navigasi tambahan: TC-GS-IMPORT-13 membutuhkan user di Import > Division (state akhir TC-GS-IMPORT-9 di tab asal), TC-GS-IMPORT-10 mengembalikan ke Brand yang dibutuhkan precondition TC-GS-IMPORT-12, dan TC-GS-IMPORT-14 terakhir karena ganti akun ke Client E.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 12 (tutup tab baru), langkah 14, 18, 23, 28, 35, 39, dan 47 (mengamati sesuai Langkah Uji TC), langkah 42 dan 43 (ganti akun).
- Spec melewati sekitar 35 langkah (49 langkah). Seluruhnya satu topik (routing halaman Import, tanpa aksi yang mengubah data); tiap blok TC berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain; blok pada akun lain (TC-GS-IMPORT-14) berada di akhir dengan langkah ganti akun eksplisit.
- Temuan untuk QA:
  - TC-GS-IMPORT-9, 14 memerlukan seed draft dan notifikasi lonceng (D-19) lewat skrip fixture yang tidak didefinisikan di TC, PRD, atau LLD; mekanismenya disediakan tim FE/BE (S-13).
  - TC-GS-IMPORT-14 tidak menyebut password/env akun Total Control Client E; env `GS_CLIENTE_TC_PASSWORD` baru.
  - Draft memakai nama literal Population tanpa suffix `{runId}`; keunikan dijaga lewat reset draft di hook.
