---
id: TC-GS-IMPORT-E2E-199-modal-changelog-import-column-visibility-dan-setup-column-preview-save
title: "Modal Changelog Import: Column Visibility dan Setup Column (preview, Save, Reset, F5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-502
  - TC-GS-IMPORT-503
  - TC-GS-IMPORT-779
  - TC-GS-IMPORT-795
  - TC-GS-IMPORT-796
  - TC-GS-IMPORT-797
  - TC-GS-IMPORT-798
coverage:
  web: automated
---

# Modal Changelog Import: Column Visibility dan Setup Column (preview, Save, Reset, F5)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena state global dibagi antar spec dan preferensi kolom tersimpan per user (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC_PASSWORD`.
- Layar awal: hook `beforeEach` membuka Import > Brand Client E.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis D-60: Changelog Import Client E berisi tepat 30 entri seed, disiapkan oleh langkah 1 lewat skrip seed (skrip juga membersihkan entri hasil commit spec lain; mekanisme disediakan tim FE/BE). Entri ke-i bertanggal i Sep 2026 pukul 10:00 UTC+7; Data `12 records imported, 0 duplicates ignored, 0 errors remaining` ada pada tepat satu entri (i = 12). Spec hanya membaca seed.
- Draft untuk TC-GS-IMPORT-798: Data Dinamis D-50 (draft Brand 12 baris `pending` di Client E dari `brand-12.csv`), disiapkan lewat skrip seed sebelum TC itu (dipakai sebagai precondition TC, tidak diasersi). Tidak di-commit.
- General Settings Client E: Date Format `dd MMM yy`, Time Format 24 jam (`HH:mm`), Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` (Pre-setup, tidak diubah).
- State yang diubah spec ini: preferensi tampil kolom Changelog Import milik akun Total Control Client E, tersimpan di cache browser/akun. Pemulihan antar blok (langkah 47) dan hook `after` memakai kemampuan pemulihan konfigurasi kolom (hapus preferensi kolom di browser); TC-GS-IMPORT-798 dipulihkan lewat `[Reset to Default]` dan `[Save]` (langkah 65 sampai 68) sesuai Post Condition TC.
- Pemulihan konfigurasi kolom: hapus preferensi kolom Changelog Import di browser akun Total Control Client E (kemampuan disediakan tim FE; didaftarkan di `suite.md`).
- Cleanup (hook `after`): hapus preferensi kolom Changelog Import di browser akun Total Control Client E; entri seed D-60 dibersihkan; draft Brand Client E dibuang.
- State global: flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Isi Setup Column (TC-GS-IMPORT-503)

1. Seed Changelog Import Client E 30 entri (D-60) lewat skrip seed, lalu muat ulang halaman Import > Brand
2. Klik `[Changelog]`
3. Klik header kolom Actions (kosong)
4. Klik item "Setup Column..."
5. Verifikasi modal Setup Column memuat tepat empat kolom: Date, Action, Data, dan Modified By
6. Verifikasi keempat kolom bercentang
7. Verifikasi tidak ada kolom Field, Old Value, New Value, maupun kolom tambahan lain yang dapat dicentang
8. Klik `[✕]` pada modal Setup Column

### Column Visibility lewat overlay (TC-GS-IMPORT-502)

9. Klik header kolom Actions (kosong)
10. Verifikasi Overlay Column Visibility memuat checkbox Date, Action, Data, dan Modified By, seluruhnya tercentang
11. Verifikasi Overlay memuat item "Setup Column..." di bagian bawah
12. Hilangkan centang kolom `Data`
13. Verifikasi kolom Data langsung hilang dari tabel tanpa tombol Save
14. Verifikasi kolom Date, Action, dan Modified By tetap tampil
15. Centang kembali kolom `Data`, lalu tekan `Esc` untuk menutup overlay

### Search tidak mencari kolom tersembunyi (TC-GS-IMPORT-779)

16. Klik header kolom Actions (kosong)
17. Hilangkan centang kolom `Data`
18. Ketik Search `12 records`, tekan Enter
19. Verifikasi tabel menampilkan Title "No results found"
20. Verifikasi tabel menampilkan Description "Try adjusting your search or filter."
21. Klik header kolom Actions (kosong)
22. Centang kembali kolom `Data`
23. Tekan Enter pada input Search
24. Verifikasi tabel menampilkan 1 entri dengan Data `12 records imported, 0 duplicates ignored, 0 errors remaining`
25. Klik `(←)` pada kotak Search

### Icon close membuang preview (TC-GS-IMPORT-796)

26. Klik header kolom Actions (kosong)
27. Klik item "Setup Column..."
28. Hilangkan centang kolom `Action` pada modal Setup Column
29. Klik icon `[✕]` pada modal Setup Column
30. Verifikasi modal Setup Column tertutup
31. Verifikasi kolom Action kembali tampil di tabel Changelog
32. Verifikasi modal Changelog tetap terbuka

### Preview, Save, dan F5 (TC-GS-IMPORT-795)

33. Klik header kolom Actions (kosong)
34. Klik item "Setup Column..."
35. Verifikasi modal Setup Column berjudul "Setup Column" dengan deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."
36. Verifikasi footer memuat `[Reset to Default]` dan `[Save]` tanpa `[Cancel]`
37. Verifikasi modal memuat icon close `[✕]`
38. Hilangkan centang kolom `Action` pada modal Setup Column
39. Verifikasi kolom Action sudah hilang dari tabel Changelog di balik modal
40. Klik `[Save]`
41. Verifikasi modal Setup Column tertutup
42. Verifikasi tabel Changelog tidak menampilkan kolom Action
43. Tekan `F5`
44. Klik `[Changelog]`
45. Verifikasi tabel Changelog menampilkan kolom Date, Data, dan Modified By
46. Verifikasi tabel Changelog masih tidak menampilkan kolom Action
47. Pulihkan: hapus preferensi kolom Changelog Import di browser akun Total Control Client E lewat kemampuan pemulihan konfigurasi kolom, tekan `F5`, lalu klik `[Changelog]`

### Reset to Default (TC-GS-IMPORT-797)

48. Klik header kolom Actions (kosong)
49. Hilangkan centang kolom `Data`
50. Verifikasi kolom Data hilang dari tabel
51. Klik header kolom Actions (kosong)
52. Klik item "Setup Column..."
53. Klik `[Reset to Default]`
54. Verifikasi preview di balik modal menampilkan keempat kolom Date, Action, Data, dan Modified By dengan urutan default
55. Klik `[Save]`
56. Verifikasi modal Setup Column tertutup
57. Verifikasi tabel Changelog menampilkan keempat kolom

### Column Visibility Changelog: kolom Data disembunyikan (TC-GS-IMPORT-798)

58. Tutup modal Changelog, lalu seed draft D-50 dan muat ulang halaman Import > Brand
59. Klik `[Changelog]`
60. Verifikasi tabel Changelog menampilkan keempat kolom Date, Action, Data, dan Modified By
61. Klik header kolom Actions (kosong) pada Changelog
62. Hilangkan centang kolom `Data`
63. Verifikasi kolom Date, Action, dan Modified By tetap tampil
64. Verifikasi tabel Changelog tidak menampilkan kolom Data
65. Pulihkan: klik header kolom Actions (kosong) pada Changelog
66. Klik item "Setup Column..."
67. Klik `[Reset to Default]`
68. Klik `[Save]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 68 langkah, di atas 35 langkah. Alasan: satu surface (Setup Column dan Column Visibility) dan satu dataset seed read-only (D-60); blok berdiri sendiri dengan pemulihan eksplisit antar blok (langkah 8, 15, 25, 47, 58, 65 sampai 68). Urutan 503, 502, 779, 796, 795, 797, 798 mengikuti ketergantungan preferensi kolom: blok yang menyimpan preferensi (795) memulihkannya di langkah 47, dan TC-GS-IMPORT-798 yang menyembunyikan kolom Data Changelog paling akhir, dipulihkan lewat `[Reset to Default]`.
- Langkah 1 adalah langkah penghubung pembuka (seed D-60 lalu muat ulang halaman; S-03, K-7), tanpa `Verifikasi`.
- Langkah 8, 15, 25, 47, 58, 65, 66, 67, 68 adalah langkah penghubung atau pemulihan (S-03, S-09). Langkah 47 menghapus preferensi kolom, memuat ulang halaman, dan membuka kembali modal Changelog.
- Langkah 45 (kolom Date, Data, dan Modified By tampil) adalah anchor positif untuk asersi absence kolom Action di langkah 46 (bagian 8b butir 2, S-03).
- Tombol `[Save]` Setup Column adalah aksi sisi klien (bagian 8b butir 8), sehingga tidak diikuti "Tunggu aksi selesai".
- Temuan untuk QA:
  - TC-GS-IMPORT-798 hanya mencakup Changelog (Staging Table tidak memiliki Column Visibility, lihat TC-GS-IMPORT-890). `suite.md` masih mendaftarkan spec 199 untuk Changelog Import dan Staging Table; spec ini hanya menyentuh Changelog Import.
  - TC-GS-IMPORT-502, 779, 795 Post Condition ("dikembalikan tampil lewat Reset to Default") ditulis sebagai langkah pemulihan antar blok tanpa asersi lewat penghapusan preferensi kolom di browser (konvensi bagian 4), sedangkan `[Reset to Default]` diuji di TC-GS-IMPORT-797 (langkah 53); TC-GS-IMPORT-798 Post Condition dipenuhi langkah 65 sampai 68 tanpa asersi; hook `after` memakai kemampuan penghapusan preferensi kolom.
  - Asersi "di balik modal" (langkah 39 dan 54) mengamati tabel di balik modal Setup Column; TC tidak menyebut cara memastikan tabel di balik modal terlihat, spec mengasumsikan elemen tabel dapat dibaca walau tertutup overlay.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
