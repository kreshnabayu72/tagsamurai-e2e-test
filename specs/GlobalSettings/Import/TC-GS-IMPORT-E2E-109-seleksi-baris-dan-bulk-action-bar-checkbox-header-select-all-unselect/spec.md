---
id: TC-GS-IMPORT-E2E-109-seleksi-baris-dan-bulk-action-bar-checkbox-header-select-all-unselect
title: "Seleksi baris dan Bulk Action Bar: checkbox header, Select All, Unselect All, N-1, seleksi bertahan lintas halaman, Cancel dialog Bulk Delete"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-262
  - TC-GS-IMPORT-263
  - TC-GS-IMPORT-266
  - TC-GS-IMPORT-268
  - TC-GS-IMPORT-269
  - TC-GS-IMPORT-688
  - TC-GS-IMPORT-689
  - TC-GS-IMPORT-690
coverage:
  web: automated
---

# Seleksi baris dan Bulk Action Bar: checkbox header, Select All, Unselect All, N-1, seleksi bertahan lintas halaman, Cancel dialog Bulk Delete

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > Brand untuk Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Dinamis (nama literal karena asersi bergantung pada isi dan jumlah baris; pengecualian S-12): D-01 (Draft Brand 12 baris `pending`: #1 `Acme Corp`, #2 `Lenovo`, #3 `Zebra Technologies`, #4 `Honeywell`, #5 `Dell`, ..., #12 `Asus`; ukuran halaman bawaan 10 baris) dan D-08 (Draft Brand 18 baris `pending` hasil Append, dibuat ulang lewat skrip fixture sebelum TC-269), dipulihkan oleh hook `beforeEach` (D-01) dan langkah 52 (D-08), Kontrak Fixture R2.
- Kemampuan teknis: skrip pemulihan draft D-01 dan seed D-08 (disediakan tim FE/BE). Tidak ada baris yang dihapus sungguhan oleh spec ini.
- State global: tidak ada yang diubah selain draft Client A dan flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan draft Client A ke D-01.

## Test Steps

### TC-GS-IMPORT-263: Bulk Action dropdown hanya berisi Delete

1. Centang baris #1
2. Klik `[Bulk Action ▾]`
3. Verifikasi overlay hanya berisi satu item `[Delete]`
4. Tekan Esc untuk menutup overlay; klik `[×]` pada Bulk Action Bar untuk membersihkan seleksi

### TC-GS-IMPORT-266: Cancel pada dialog Bulk Delete

5. Centang baris #2 dan #5
6. Klik `[Bulk Action ▾]`
7. Klik `[Delete]` pada overlay
8. Klik `[Cancel]`
9. Verifikasi dialog tertutup
10. Verifikasi baris #2 `Lenovo` dan #5 `Dell` tetap ada
11. Verifikasi Bulk Action Bar menampilkan "2 Rows selected"
12. Klik `[×]` pada Bulk Action Bar

### TC-GS-IMPORT-688: Checkbox header memilih baris halaman aktif

13. Klik checkbox header kolom Checkbox
14. Verifikasi checkbox header tercentang dan baris #1 sampai #10 tercentang
15. Verifikasi Bulk Action Bar menampilkan "10 Rows selected"
16. Klik tombol halaman 2 pada paginator
17. Verifikasi checkbox baris #11 dan #12 tidak tercentang
18. Klik tombol halaman 1 pada paginator
19. Hapus centang baris #10
20. Verifikasi checkbox header berstatus indeterminate
21. Verifikasi Bulk Action Bar menampilkan "9 Rows selected"
22. Klik `[×]` pada Bulk Action Bar

### TC-GS-IMPORT-689: Select All lintas halaman, Unselect All

23. Centang baris #1
24. Klik `[Select All (12 records)]`
25. Verifikasi Bulk Action Bar menampilkan "12 Rows selected"
26. Verifikasi tombol `[Select All (12 records)]` berganti `[Unselect All]`
27. Klik tombol halaman 2 pada paginator
28. Verifikasi checkbox baris #11 dan #12 tercentang
29. Klik `[Unselect All]`
30. Verifikasi Bulk Action Bar hilang
31. Klik tombol halaman 1 pada paginator
32. Verifikasi tidak ada baris tercentang

### TC-GS-IMPORT-690: Hapus centang satu baris dari seleksi penuh

33. Centang baris #1
34. Klik `[Select All (12 records)]`
35. Hapus centang baris #3 pada halaman 1
36. Verifikasi Bulk Action Bar menampilkan "11 Rows selected"
37. Verifikasi tombol `[Unselect All]` berganti kembali menjadi `[Select All (12 records)]`
38. Klik `[×]` pada Bulk Action Bar

### TC-GS-IMPORT-268: Tombol [×] membersihkan seleksi

39. Centang baris #1 dan #2
40. Klik `[×]` pada Bulk Action Bar
41. Verifikasi Bulk Action Bar hilang
42. Verifikasi checkbox baris #1 dan #2 tidak tercentang

### TC-GS-IMPORT-262: Bulk Action Bar muncul saat baris dicentang

43. Set Rows per page menjadi 25
44. Centang baris #1
45. Verifikasi Bulk Action Bar standar tampil: `[Bulk Action ▾]`, "1 Row selected", `[Select All (12 records)]`, dan `[×]`
46. Centang checkbox baris #n untuk n = 2 sampai 12 secara berurutan (11 klik, satu per baris)
47. Verifikasi counter menjadi "12 Rows selected"
48. Verifikasi tombol `[Select All (12 records)]` berganti `[Unselect All]`
49. Klik `[Unselect All]`
50. Verifikasi Bulk Action Bar hilang
51. Pulihkan Rows per page ke 10 (aksi tanpa `Verifikasi`)

### TC-GS-IMPORT-269: Berpindah halaman atau filter tidak mereset seleksi

52. Seed draft D-08 (Brand 18 baris) di Client A lewat skrip fixture, lalu muat ulang halaman
53. Centang baris #1 di halaman 1
54. Klik tombol halaman 2 pada paginator
55. Verifikasi Bulk Action Bar menampilkan "1 Row selected"
56. Klik kartu Ready to Import
57. Verifikasi Bulk Action Bar tetap menampilkan "1 Row selected"

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: TC-262 (mengubah Rows per page) dijalankan sesudah TC-688 sampai TC-268 yang memakai ukuran halaman bawaan 10; TC-269 terakhir karena memakai draft D-08. Tiap blok membersihkan seleksi (`[×]` atau Unselect All) sebagai langkah penghubung tanpa `Verifikasi` (S-09).
- Spec berisi 57 langkah. Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional) dan satu topik (seleksi dan Bulk Action Bar), tiap blok berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-GS-IMPORT-264, 265, 267, dan 687 (Bulk Delete yang menghapus) ada di spec 110; TC-GS-IMPORT-266 (Cancel dialog) ada di spec ini.
- Temuan untuk QA:
  - TC-GS-IMPORT-262 Langkah 4 menyebut 11 klik berurutan; spec menuliskannya sebagai satu langkah perulangan (n = 2 sampai 12) karena parameternya jelas dan tanpa langkah bersyarat.
  - Post Condition semua TC kosong; tidak ada yang diasersi.
