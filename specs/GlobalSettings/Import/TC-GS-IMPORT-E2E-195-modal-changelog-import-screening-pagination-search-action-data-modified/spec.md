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
- Data Dinamis D-60: Changelog Import Client E berisi tepat 30 entri seed, disiapkan lewat skrip seed di hook `before` (skrip juga membersihkan entri hasil commit spec lain; mekanisme disediakan tim FE/BE). Entri ke-i (i = 1 sampai 30) bertanggal i Sep 2026 pukul 10:00 UTC+7; Action berulang Import Brand, Import Measurement, Import Position, Import Division, Import User Login, Import User Non Login; Data `[i] records imported, 0 duplicates ignored, 0 errors remaining` (`1 record imported` bila i = 1); Modified By Yoga Permana (i ganjil) dan Dimas Anggoro (i genap). Spec hanya membaca seed. Karena skrip seed menjamin total entri tepat 30, asersi jumlah total ("of 30 items") sah; total tidak diasersi sebagai angka absolut di spec lain yang tidak memakai seed ini (S-12).
- General Settings Client E: Date Format `dd MMM yy`, Time Format 24 jam (`HH:mm`), Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta` (Pre-setup, tidak diubah).
- Cleanup (hook `after`): entri seed D-60 dibersihkan agar tidak bocor ke spec Client E lain; preferensi kolom tidak diubah spec ini.
- Kemampuan teknis: hover tooltip, klik backdrop modal, tombol `Esc`.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Screening Modal Changelog (TC-GS-IMPORT-489)

1. Klik tombol `[Changelog]` di header halaman
2. Verifikasi judul modal `Changelog: Import`
3. Verifikasi toolbar memuat icon Search, Filter, dan Download
4. Verifikasi kolom tabel `Date | Action | Data | Modified By`
5. Verifikasi tidak ada kolom Field, Old Value, maupun New Value
6. Verifikasi baris pertama (sort default Date descending) Date `30 Sep 26` pukul `10:00`
7. Verifikasi baris pertama Action `Import User Non Login` (plain text)
8. Verifikasi baris pertama Data `30 records imported, 0 duplicates ignored, 0 errors remaining`
9. Verifikasi baris pertama Modified By `Dimas A`
10. Verifikasi pagination default 10 baris: "Showing 1 - 10 of 30 items"
11. Verifikasi header kolom Actions kosong tampil di kanan tabel
12. Klik header kolom Actions (kosong) di ujung kanan tabel
13. Verifikasi Overlay Column Visibility terbuka berisi Date, Action, Data, Modified By
14. Verifikasi Overlay memuat item "Setup Column..."
15. Tekan `Esc` untuk menutup overlay

### Pagination (TC-GS-IMPORT-501)

16. Verifikasi default 10 baris per halaman dengan teks "Showing 1 - 10 of 30 items"
17. Buka dropdown Rows per page
18. Verifikasi dropdown Rows per page memuat opsi 10, 25, 50, dan 100
19. Pilih 25
20. Verifikasi pagination menampilkan "Showing 1 - 25 of 30 items"
21. Buka dropdown Rows per page dan pilih 10

### Search (TC-GS-IMPORT-776, 777, 492, 778)

22. Ketik Search `12 records`, tekan Enter
23. Verifikasi tabel menampilkan 1 entri: Date `12 Sep 26`, Action `Import User Non Login`, Data `12 records imported, 0 duplicates ignored, 0 errors remaining`, Modified By `Dimas A`
24. Klik `(←)` pada kotak Search
25. Ketik Search `dimas`, tekan Enter
26. Verifikasi tabel menampilkan sedikitnya satu baris
27. Verifikasi seluruh baris tabel bermodified `Dimas A`
28. Verifikasi pagination menampilkan "Showing 1 - 10 of 15 items"
29. Klik `(←)` pada kotak Search
30. Ketik Search `import brand`, tekan Enter
31. Verifikasi tabel menampilkan 5 entri dengan Action `Import Brand` walau kata kunci diketik huruf kecil (Date `25 Sep 26`, `19 Sep 26`, `13 Sep 26`, `07 Sep 26`, dan `01 Sep 26`)
32. Verifikasi pagination menampilkan "Showing 1 - 5 of 5 items"
33. Klik `(←)` pada kotak Search
34. Klik halaman 3
35. Verifikasi entri dengan Date `10 Sep 26` ada pada daftar
36. Ketik Search `10 Sep`, tekan Enter
37. Verifikasi tabel menampilkan Title "No results found"
38. Verifikasi tabel menampilkan Description "Try adjusting your search or filter."
39. Klik `(←)` pada kotak Search
40. Klik halaman 1

### Hover Modified By (TC-GS-IMPORT-799)

41. Hover teks `Dimas A` pada baris pertama
42. Verifikasi tooltip menampilkan nama lengkap `Dimas Anggoro`

### Menutup modal (TC-GS-IMPORT-490)

43. Klik backdrop (area di luar modal)
44. Verifikasi modal tetap terbuka
45. Tekan `Esc`
46. Verifikasi modal tertutup
47. Klik `[Changelog]`
48. Klik `[✕]` di kanan atas modal
49. Verifikasi modal tertutup

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 49 langkah, di atas 35 langkah. Alasan: satu dataset seed read-only (D-60) dan satu surface (Modal Changelog); tiap blok berdiri sendiri dengan pemulihan eksplisit antar blok (langkah 15, 21, 24, 29, 33, 39, 40). Menutup modal (TC-GS-IMPORT-490) paling akhir sesuai prinsip menutup form di akhir.
- Langkah 15, 21, 24, 29, 33, 39, 40 adalah langkah penghubung yang mereset overlay, ukuran halaman, Search, dan nomor halaman (S-03, S-09).
- TC-GS-IMPORT-489 dan TC-GS-IMPORT-490 membuka modal lewat `[Changelog]` di langkah 1 dan 47; langkah pembukaan TC-GS-IMPORT-492/501/776/777/778/799 memakai modal yang sudah terbuka.
- Temuan untuk QA:
  - Changelog adalah audit trail permanen; asersi total "of 30 items" hanya sah bila skrip seed D-60 menyetel Changelog Import Client E ke tepat 30 entri (D-60 menyatakan skrip seed membersihkan entri lain). Mekanisme skrip disediakan tim FE/BE.
  - TC-GS-IMPORT-778 mengasersi entri Date `10 Sep 26` pada halaman 3 untuk ukuran halaman 10; spec mengikuti dan tidak menghitung ulang.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
