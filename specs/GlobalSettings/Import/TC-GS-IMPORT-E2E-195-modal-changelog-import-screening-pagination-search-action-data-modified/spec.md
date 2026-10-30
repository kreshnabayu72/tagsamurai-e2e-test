---
id: TC-GS-IMPORT-E2E-195-modal-changelog-import-screening-pagination-search-action-data-modified
title: "Modal Changelog Import: screening, pagination, Search (Action, Data, Modified By, bukan Date), hover Modified By, dan menutup modal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-489
  - TC-GS-IMPORT-490
  - TC-GS-IMPORT-492
  - TC-GS-IMPORT-501
  - TC-GS-IMPORT-776
  - TC-GS-IMPORT-777
  - TC-GS-IMPORT-778
  - TC-GS-IMPORT-799
coverage:
  web: automated
---

# Modal Changelog Import: screening, pagination, Search (Action, Data, Modified By, bukan Date), hover Modified By, dan menutup modal

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena state global dibagi antar spec dan Changelog Import Client E disetel ulang oleh skrip seed (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client E (Yoga Permana) `totalControl_automated_qaTeam5@qwertysystem.net`, password `Spectra.env.GS_CLIENTE_TC_PASSWORD`.
- Layar awal: hook `beforeEach` membuka Import > Brand Client E.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis D-60: Changelog Import Client E berisi tepat 30 entri seed, disiapkan lewat skrip seed di hook `before` (skrip juga membersihkan entri hasil commit spec lain; mekanisme disediakan tim FE/BE). Entri ke-i (i = 1 sampai 30) bertanggal i Sep 2026 pukul 10:00 UTC+7; Action berulang Import Brand, Import Measurement, Import Position, Import Division, Import User Login, Import User Non Login; Data `[i] records imported, 0 duplicates ignored, 0 errors remaining` (`1 record imported` bila i = 1); Modified By Yoga Permana (i ganjil) dan Dimas Anggoro (i genap). Spec hanya membaca seed. Total entri Changelog tidak diasersi sebagai angka absolut: N dibaca lewat kemampuan baca sebelum aksi dan asersi total tanpa Search memakai selisih terhadap N (bagian 8b butir 10, S-12); hitungan yang dibatasi Search ("of 15", "of 5") dijelaskan di Temuan untuk QA.
- General Settings Client E: Date Format `dd MMM yy`, Time Format 24 jam (`HH:mm`), Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` (Pre-setup, tidak diubah).
- Cleanup (hook `after`): entri seed D-60 dibersihkan agar tidak bocor ke spec Client E lain; preferensi kolom tidak diubah spec ini.
- Kemampuan teknis (disediakan tim FE/BE): hover tooltip, klik backdrop modal, tombol `Esc`; kemampuan baca jumlah entri Changelog Import Client E (total entri, dibaca sebelum aksi sebagai N untuk `Verifikasi` selisih).
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Screening Modal Changelog (TC-GS-IMPORT-489)

1. Baca jumlah entri Changelog Import Client E sebagai N lewat kemampuan baca jumlah entri
2. Klik tombol `[Changelog]` di header halaman
3. Verifikasi judul modal `Changelog: Import`
4. Verifikasi toolbar memuat icon Search, Filter, dan Download
5. Verifikasi kolom tabel `Date | Action | Data | Modified By`
6. Verifikasi tidak ada kolom Field, Old Value, maupun New Value
7. Verifikasi baris pertama (sort default Date descending) Date `30 Sep 26` pukul `10:00`
8. Verifikasi baris pertama Action `Import User Non Login` (plain text)
9. Verifikasi baris pertama Data `30 records imported, 0 duplicates ignored, 0 errors remaining`
10. Verifikasi baris pertama Modified By `Dimas A`
11. Verifikasi pagination default 10 baris: "Showing 1 - 10 of N items" dan selisih total terhadap N yang dibaca pada langkah 1 adalah 0
12. Verifikasi header kolom Actions kosong tampil di kanan tabel
13. Klik header kolom Actions (kosong) di ujung kanan tabel
14. Verifikasi Overlay Column Visibility terbuka berisi Date, Action, Data, Modified By
15. Verifikasi Overlay memuat item "Setup Column..."
16. Tekan `Esc` untuk menutup overlay

### Pagination (TC-GS-IMPORT-501)

17. Verifikasi default 10 baris per halaman dengan teks "Showing 1 - 10 of N items" dan selisih total terhadap N yang dibaca pada langkah 1 adalah 0
18. Buka dropdown Rows per page
19. Verifikasi dropdown Rows per page memuat opsi 10, 25, 50, dan 100
20. Pilih 25
21. Verifikasi pagination menampilkan "Showing 1 - 25 of N items" dan selisih total terhadap N yang dibaca pada langkah 1 adalah 0
22. Buka dropdown Rows per page dan pilih 10

### Search (TC-GS-IMPORT-776, 777, 492, 778)

23. Ketik Search `12 records`, tekan Enter
24. Verifikasi tabel menampilkan 1 entri: Date `12 Sep 26`, Action `Import User Non Login`, Data `12 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Dimas A`
25. Klik `(←)` pada kotak Search
26. Ketik Search `dimas`, tekan Enter
27. Verifikasi tabel menampilkan sedikitnya satu baris
28. Verifikasi seluruh baris tabel bermodified `Dimas A`
29. Verifikasi pagination menampilkan "Showing 1 - 10 of 15 items"
30. Klik `(←)` pada kotak Search
31. Ketik Search `import brand`, tekan Enter
32. Verifikasi tabel menampilkan 5 entri dengan Action `Import Brand` walau kata kunci diketik huruf kecil (Date `25 Sep 26`, `19 Sep 26`, `13 Sep 26`, `07 Sep 26`, dan `01 Sep 26`)
33. Verifikasi pagination menampilkan "Showing 1 - 5 of 5 items"
34. Klik `(←)` pada kotak Search
35. Klik halaman 3
36. Verifikasi entri dengan Date `10 Sep 26` ada pada daftar
37. Ketik Search `10 Sep`, tekan Enter
38. Verifikasi tabel menampilkan Title "No results found"
39. Verifikasi tabel menampilkan Description "Try adjusting your search or filter."
40. Klik `(←)` pada kotak Search
41. Klik halaman 1

### Hover Modified By (TC-GS-IMPORT-799)

42. Hover teks `Dimas A` pada baris pertama
43. Verifikasi tooltip menampilkan nama lengkap `Dimas Anggoro`

### Menutup modal (TC-GS-IMPORT-490)

44. Klik backdrop (area di luar modal)
45. Verifikasi modal tetap terbuka
46. Tekan `Esc`
47. Verifikasi modal tertutup
48. Klik `[Changelog]`
49. Klik `[✕]` di kanan atas modal
50. Verifikasi modal tertutup

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 50 langkah, di atas 35 langkah. Alasan: satu dataset seed read-only (D-60) dan satu surface (Modal Changelog); tiap blok berdiri sendiri dengan pemulihan eksplisit antar blok (langkah 16, 22, 25, 30, 34, 40, 41). Menutup modal (TC-GS-IMPORT-490) paling akhir sesuai prinsip menutup form di akhir.
- Langkah 16, 22, 25, 30, 34, 40, 41 adalah langkah penghubung yang mereset overlay, ukuran halaman, Search, dan nomor halaman (S-03, S-09). Langkah 1 membaca N lewat kemampuan baca (penghubung tanpa `Verifikasi`, sebelum aksi apa pun).
- TC-GS-IMPORT-489 dan TC-GS-IMPORT-490 membuka modal lewat `[Changelog]` di langkah 2 dan 48; langkah pembukaan TC-GS-IMPORT-492/501/776/777/778/799 memakai modal yang sudah terbuka.
- Temuan untuk QA:
  - Jumlah 30 entri adalah keadaan seed D-60 yang dijamin skrip seed di hook `before`, bukan total audit trail yang tumbuh; TC-GS-IMPORT-489 dan 501 Expected menulis total "of 30 items" absolut, sedangkan spec mengasersi selisih 0 terhadap N yang dibaca sebelum aksi (langkah 1, 11, 17, 21; S-12). Hitungan yang dibatasi Search ("of 15" pada langkah 29, "of 5" pada langkah 33) dipertahankan sebagai angka dari keadaan seed D-60 dan tidak dijadikan selisih karena kemampuan baca hanya memberi total entri tanpa Search; Expected TC menulis angka itu absolut. Mekanisme skrip seed dan kemampuan baca disediakan tim FE/BE.
  - TC-GS-IMPORT-778 mengasersi entri Date `10 Sep 26` pada halaman 3 untuk ukuran halaman 10; spec mengikuti dan tidak menghitung ulang.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
