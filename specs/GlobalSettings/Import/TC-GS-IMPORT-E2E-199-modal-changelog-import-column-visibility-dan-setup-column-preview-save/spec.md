---
id: TC-GS-IMPORT-E2E-199-modal-changelog-import-column-visibility-dan-setup-column-preview-save
title: "Modal Changelog Import: Column Visibility dan Setup Column (preview, Save, Reset, F5, pemisahan dari Staging Table)"
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

# Modal Changelog Import: Column Visibility dan Setup Column (preview, Save, Reset, F5, pemisahan dari Staging Table)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena state global dibagi antar spec dan preferensi kolom tersimpan per user (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC_PASSWORD`.
- Layar awal: hook `beforeEach` membuka Import > Brand Client E.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis D-60: Changelog Import Client E berisi tepat 30 entri seed, disiapkan lewat skrip seed di hook `before` (skrip juga membersihkan entri hasil commit spec lain; mekanisme disediakan tim FE/BE). Entri ke-i bertanggal i Sep 2026 pukul 10:00 UTC+7; Data `12 records imported, 0 duplicates ignored, 0 errors remaining` ada pada tepat satu entri (i = 12). Spec hanya membaca seed.
- Draft untuk TC-GS-IMPORT-798: Data Dinamis D-50 (draft Brand 12 baris `pending` di Client E dari `brand-12.csv`), disiapkan lewat skrip seed sebelum TC itu (dipakai sebagai precondition TC, tidak diasersi). Tidak di-commit.
- General Settings Client E: Date Format `dd MMM yy`, Time Format 24 jam (`HH:mm`), Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` (Pre-setup, tidak diubah).
- State yang diubah spec ini: preferensi tampil kolom Changelog Import (dan Staging Table untuk TC-GS-IMPORT-798) milik akun Total Control Client E, tersimpan di cache browser/akun. Pemulihan antar blok lewat UI di akhir blok (langkah 46 dan 68); pemulihan hook `after` memakai kemampuan pemulihan konfigurasi kolom.
- Pemulihan konfigurasi kolom: hapus preferensi kolom Changelog Import dan Staging Table di browser akun Total Control Client E (kemampuan disediakan tim FE; didaftarkan di `suite.md`).
- Cleanup (hook `after`): hapus preferensi kolom Changelog Import dan Staging Table di browser akun Total Control Client E; entri seed D-60 dibersihkan; draft Brand Client E dibuang.
- State global: flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Isi Setup Column (TC-GS-IMPORT-503)

1. Klik `[Changelog]`
2. Klik header kolom Actions (kosong)
3. Klik item "Setup Column..."
4. Verifikasi modal Setup Column memuat tepat empat kolom: Date, Action, Data, dan Modified By
5. Verifikasi keempat kolom bercentang
6. Verifikasi tidak ada kolom Field, Old Value, New Value, maupun kolom tambahan lain yang dapat dicentang
7. Klik `[✕]` pada modal Setup Column

### Column Visibility lewat overlay (TC-GS-IMPORT-502)

8. Klik header kolom Actions (kosong)
9. Verifikasi Overlay Column Visibility memuat checkbox Date, Action, Data, dan Modified By, seluruhnya tercentang
10. Verifikasi Overlay memuat item "Setup Column..." di bagian bawah
11. Hilangkan centang kolom `Data`
12. Verifikasi kolom Data langsung hilang dari tabel tanpa tombol Save
13. Verifikasi kolom Date, Action, dan Modified By tetap tampil
14. Centang kembali kolom `Data`, lalu tekan `Esc` untuk menutup overlay

### Search tidak mencari kolom tersembunyi (TC-GS-IMPORT-779)

15. Klik header kolom Actions (kosong)
16. Hilangkan centang kolom `Data`
17. Ketik Search `12 records`, tekan Enter
18. Verifikasi tabel menampilkan Title "No results found"
19. Verifikasi tabel menampilkan Description "Try adjusting your search or filter."
20. Klik header kolom Actions (kosong)
21. Centang kembali kolom `Data`
22. Tekan Enter pada input Search
23. Verifikasi tabel menampilkan 1 entri dengan Data `12 records imported, 0 duplicates ignored, 0 errors remaining`
24. Klik `(←)` pada kotak Search

### Icon close membuang preview (TC-GS-IMPORT-796)

25. Klik header kolom Actions (kosong)
26. Klik item "Setup Column..."
27. Hilangkan centang kolom `Action` pada modal Setup Column
28. Klik icon `[✕]` pada modal Setup Column
29. Verifikasi modal Setup Column tertutup
30. Verifikasi kolom Action kembali tampil di tabel Changelog
31. Verifikasi modal Changelog tetap terbuka

### Preview, Save, dan F5 (TC-GS-IMPORT-795)

32. Klik header kolom Actions (kosong)
33. Klik item "Setup Column..."
34. Verifikasi modal Setup Column berjudul "Setup Column" dengan deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."
35. Verifikasi footer memuat `[Reset to Default]` dan `[Save]` tanpa `[Cancel]`
36. Verifikasi modal memuat icon close `[✕]`
37. Hilangkan centang kolom `Action` pada modal Setup Column
38. Verifikasi kolom Action sudah hilang dari tabel Changelog di balik modal
39. Klik `[Save]`
40. Verifikasi modal Setup Column tertutup
41. Verifikasi tabel Changelog tidak menampilkan kolom Action
42. Tekan `F5`
43. Klik `[Changelog]`
44. Verifikasi tabel Changelog menampilkan kolom Date, Data, dan Modified By
45. Verifikasi tabel Changelog masih tidak menampilkan kolom Action
46. Pulihkan: buka Setup Column, klik `[Reset to Default]`, klik `[Save]`

### Reset to Default (TC-GS-IMPORT-797)

47. Klik header kolom Actions (kosong)
48. Hilangkan centang kolom `Data`
49. Verifikasi kolom Data hilang dari tabel
50. Klik header kolom Actions (kosong)
51. Klik item "Setup Column..."
52. Klik `[Reset to Default]`
53. Verifikasi preview di balik modal menampilkan keempat kolom Date, Action, Data, dan Modified By dengan urutan default
54. Klik `[Save]`
55. Verifikasi modal Setup Column tertutup
56. Verifikasi tabel Changelog menampilkan keempat kolom

### Pemisahan Staging Table dan Changelog (TC-GS-IMPORT-798)

57. Tutup modal Changelog, lalu seed draft D-50 dan muat ulang halaman Import > Brand
58. Klik header kolom Actions (`⋯`) pada Staging Table
59. Hilangkan centang kolom `Status`
60. Klik `[Changelog]`
61. Verifikasi tabel Changelog masih menampilkan keempat kolom Date, Action, Data, dan Modified By
62. Klik header kolom Actions (kosong) pada Changelog
63. Hilangkan centang kolom `Data`
64. Verifikasi tabel Changelog tidak menampilkan kolom Data
65. Tutup modal Changelog
66. Verifikasi Staging Table masih tanpa kolom `Status`
67. Verifikasi Staging Table tetap menampilkan kolom `Brand Name`
68. Pulihkan: Reset to Default pada Staging Table dan Changelog

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 68 langkah, di atas 35 langkah. Alasan: satu surface (Setup Column dan Column Visibility) dan satu dataset seed read-only (D-60); blok berdiri sendiri dengan pemulihan eksplisit antar blok (langkah 7, 14, 24, 46, 56, 68). Urutan 503, 502, 779, 796, 795, 797, 798 mengikuti ketergantungan preferensi kolom: blok yang menyimpan preferensi (795) memulihkannya di langkah 46, dan TC-GS-IMPORT-798 yang menyentuh Staging Table paling akhir.
- Langkah 7, 14, 24, 46, 57, 65, 68 adalah langkah penghubung atau pemulihan (S-03, S-09).
- Langkah 44 (kolom Date, Data, dan Modified By tampil) adalah anchor positif untuk asersi absence kolom Action di langkah 45 (bagian 8b butir 2, S-03).
- Tombol `[Save]` Setup Column adalah aksi sisi klien (bagian 8b butir 8), sehingga tidak diikuti "Tunggu aksi selesai".
- Temuan untuk QA:
  - TC-GS-IMPORT-798 bertentangan dengan TC-GS-IMPORT-890: TC-890 menyatakan Staging Table tidak memiliki Column Visibility maupun Setup Column, sedangkan TC-798 langkah 1-2 dan Expected c mengasersi penyembunyian kolom `Status` di Staging Table. Langkah 57-68 mengikuti TC-798 apa adanya; bagian Staging Table tidak dapat diotomasi sebelum QA mengklarifikasi.
  - TC-GS-IMPORT-502, 779, 795, 798 Post Condition ("dikembalikan tampil lewat Reset to Default") ditulis sebagai langkah pemulihan antar blok lewat UI tanpa asersi; pemulihan hook `after` memakai penghapusan preferensi kolom di browser (konvensi bagian 4).
  - Asersi "di balik modal" (langkah 38 dan 53) mengamati tabel di balik modal Setup Column; TC tidak menyebut cara memastikan tabel di balik modal terlihat, spec mengasumsikan elemen tabel dapat dibaca walau tertutup overlay.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
