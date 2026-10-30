---
id: TC-GS-IMPORT-E2E-100-edit-mode-tab-user-pilihan-use-untuk-nilai-baru-nilai-tersimpan-invalid
title: "Edit Mode Tab User: pilihan Use untuk nilai baru, nilai tersimpan Invalid, all-or-nothing Edit this page, opsi Dropdown dihapus admin lain"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-900
  - TC-GS-IMPORT-901
  - TC-GS-IMPORT-902
  - TC-GS-IMPORT-903
  - TC-GS-IMPORT-970
coverage:
  web: automated
---

# Edit Mode Tab User: pilihan Use untuk nilai baru, nilai tersimpan Invalid, all-or-nothing Edit this page, opsi Dropdown dihapus admin lain

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan spec ini mengubah opsi Custom Field `Shift` Client A (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`.
- Pelaku kedua (hanya memicu perubahan state lewat sesi API, tanpa asersi UI di sesinya, P-2): Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC2_PASSWORD`; klien HTTP disediakan tim FE/BE. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > User Login untuk Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Pre-setup Client A (tidak diubah, kecuali dinyatakan): `Logistik` bukan Division, `Seniur` bukan Position, Custom Field `Shift` (Dropdown, Optional) Active dengan opsi `Pagi`, `Siang`, `Malam`.
- Data Dinamis (nama literal karena asersi bergantung pada isi; pengecualian S-12), dipulihkan oleh skrip pemulihan (Kontrak Fixture R2) sebelum tiap TC: D-05 (Draft User Login 8 baris `pending` dari `user-login-8.csv`; baris #1 Position `Senior Developer`, Shift `Siang` pada Row # 1 dan 2, Shift `Pagi` pada Row # 3). Nilai ubahan: `Logistik`, `Seniur`, `Lembur`, Email `ahmad.fauzi@`.
- Kemampuan teknis: pengamatan jenis kontrol Select dengan pencarian dan pilihan `Use "[nilai]"`, skrip pemulihan draft D-05, sesi API Admin kedua untuk menghapus opsi Custom Field `Shift` (disediakan tim FE/BE).
- State global: opsi `Siang` pada Custom Field `Shift` Client A dihapus oleh Admin kedua pada langkah 61 dan dipulihkan (opsi dibuat kembali pada posisi semula) oleh hook `after` walau spec gagal di tengah; selama dihapus, draft atau spec lain yang memakai Shift `Siang` Client A terpengaruh (suite serial).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan opsi `Siang`, pulihkan draft User Login Client A ke D-05, lepas kunci sesi edit.

## Test Steps

### TC-GS-IMPORT-903: Edit this page, Use Division dan Email tidak valid ditolak all-or-nothing

1. Aktifkan Switch `Edit this page`
2. Pada baris #1 ketik `Logistik` di sel Division, lalu pilih `Use "Logistik"`
3. Pada baris #2 ganti sel Email dengan `ahmad.fauzi@`
4. Klik `[Save]`
5. Verifikasi `[Save]` diblokir tanpa toast sukses
6. Verifikasi sel Email baris #2 berborder `danger` dengan pesan "Invalid email format"
7. Verifikasi footer tetap `[Cancel]` dan `[Save]`
8. Verifikasi Error Summary Callout memuat "Invalid email format" dengan badge "1 row"
9. Klik `[Cancel]`, lalu klik `[Discard]` pada dialog Discard Changes
10. Verifikasi baris #1 dan baris #2 menampilkan nilai semula dan berstatus `pending`
11. Verifikasi Staging Metric Cards: Total Rows 8, Ready to Import 8, Errors 0

### TC-GS-IMPORT-900: Use Division untuk nama yang belum ada

12. Klik `⋯` pada baris #1, pilih `Edit`
13. Klik sel Division baris #1 dan ketik `Logistik`
14. Pilih `Use "Logistik"`
15. Klik `[Save]`
16. Verifikasi `[Save]` tidak diblokir: muncul toast sukses "Success, row has been updated."
17. Verifikasi sesi edit berakhir
18. Verifikasi baris #1 berstatus `error`
19. Verifikasi sel Division menampilkan `Logistik` dengan border `danger` dan pesan "Division 'Logistik' was not found. Check spelling, or create the missing division from this row."
20. Verifikasi Error Summary Callout memuat "Division not found" dengan badge "1 row"
21. Verifikasi Staging Metric Cards: Total Rows 8, Ready to Import 7, Errors 1
22. Klik `⋯` pada baris #1
23. Verifikasi menu `⋯` baris #1 memuat `Duplicate`, `Edit`, `[Create Missing Divisions]`, dan `Remove` dalam urutan tersebut
24. Tekan Esc untuk menutup menu
25. Buka Global Settings > User > Division, ketik Search `Logistik`, tekan Enter
26. Verifikasi empty state "No results found" (daftar Division tidak memuat `Logistik`; tidak ada Division dibuat oleh `[Save]`)

### TC-GS-IMPORT-901: Position dikosongkan dan nilai baru dengan Use

27. Pulihkan draft User Login Client A ke D-05 lewat skrip pemulihan; buka Import > User Login
28. Klik `⋯` pada baris #1, pilih `Edit`
29. Kosongkan sel Position baris #1
30. Klik `[Save]`
31. Verifikasi muncul toast sukses: "Success, row has been updated."
32. Verifikasi sel Position baris #1 tampil `—`
33. Verifikasi baris #1 berstatus `pending`
34. Klik `⋯` pada baris #1, pilih `Edit`, klik sel Position, lalu ketik `Seniur`
35. Pilih `Use "Seniur"`
36. Klik `[Save]`
37. Verifikasi muncul toast sukses: "Success, row has been updated."
38. Verifikasi baris #1 berstatus `error`
39. Verifikasi sel Position menampilkan `Seniur` dengan border `danger` dan pesan "Position 'Seniur' was not found. Check spelling, create the missing position from this row, or leave blank."
40. Verifikasi Error Summary Callout memuat "Position not found" dengan badge "1 row"
41. Klik `⋯` pada baris #1
42. Verifikasi menu `⋯` baris #1 memuat `Duplicate`, `Edit`, `[Create Missing Positions]`, dan `Remove`
43. Tekan Esc untuk menutup menu
44. Buka Global Settings > User > Position, ketik Search `Seniur`, tekan Enter
45. Verifikasi empty state "No results found" (daftar Position tidak memuat `Seniur`)

### TC-GS-IMPORT-902: Use opsi Custom Field Dropdown

46. Pulihkan draft User Login Client A ke D-05 lewat skrip pemulihan; buka Import > User Login
47. Klik `⋯` pada baris #1, pilih `Edit`
48. Klik sel Shift baris #1
49. Verifikasi daftar pilihan memuat `Pagi`, `Siang`, dan `Malam`
50. Ketik `Lembur`, lalu pilih `Use "Lembur"`
51. Klik `[Save]`
52. Verifikasi muncul toast sukses: "Success, row has been updated."
53. Verifikasi baris #1 berstatus `error`
54. Verifikasi sel Shift menampilkan `Lembur` dengan border `danger` dan pesan "Lembur is not a valid option for shift"
55. Verifikasi Error Summary Callout memuat "Shift: Invalid option" dengan badge "1 row"
56. Klik `⋯` pada baris #1
57. Verifikasi menu `⋯` baris #1 memuat `Duplicate`, `Edit`, `[Create Missing Options]`, dan `Remove`
58. Tekan Esc untuk menutup menu
59. Buka Global Settings > User > Custom Field dan buka Value Setting Shift
60. Verifikasi Value Setting Shift tetap `Pagi, Siang, Malam` (tidak ada opsi dibuat oleh `[Save]`)

### TC-GS-IMPORT-970: Opsi yang dihapus admin lain, nilai tersimpan tampil Invalid (paling akhir)

61. Pulihkan draft User Login Client A ke D-05 lewat skrip pemulihan; Admin kedua Client A menghapus opsi `Siang` dari Custom Field `Shift` lewat sesi API hingga tersimpan
62. Buka Import > User Login lalu tekan F5
63. Verifikasi Row # 1 dan 2 berstatus `error`
64. Verifikasi Staging Metric Cards: Errors 2
65. Klik `⋯` pada Row # 1, pilih `Edit`
66. Klik sel Shift Row # 1
67. Verifikasi sel Shift menampilkan `Siang` sebagai nilai terpilih berstatus Invalid (ikon dan teks deskriptif) dan tidak dikosongkan
68. Verifikasi daftar pilihan hanya memuat `Pagi` dan `Malam`
69. Klik `[Save]` tanpa mengubah sel Shift
70. Verifikasi `Siang` tetap tersimpan pada sel Shift Row # 1
71. Verifikasi Row # 1 tetap berstatus `error` dengan pesan "Siang is not a valid option for shift"
72. Verifikasi sesi edit berakhir

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional; Admin kedua hanya pemicu (P-2, sesi API).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: TC-903 pertama (tanpa mengubah master data), TC-970 paling akhir karena menghapus opsi Custom Field Client A.
- Langkah penghubung (tanpa `Verifikasi`): langkah 9, 24, 43, 58 (menutup sesi atau menu); langkah 25, 44, 59 membuka halaman master lain; langkah 27, 46, 61 memulihkan draft D-05; Search pada langkah 25 dan 44 untuk menemukan nama (empty state "No results found" menjadi anchor positif absence).
- Spec berisi 72 langkah. Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional) dan satu topik (pilihan Use dan nilai Invalid), tiap blok memulihkan draft dan berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-IMPORT-970 Langkah 1 tidak menyebut mekanisme Admin kedua menghapus opsi (UI atau API); spec memakai sesi API (P-2) dan mekanismenya disediakan tim FE/BE (S-13).
  - TC-GS-IMPORT-970 Post Condition ("Fixture master data dan Custom Field dipulihkan") dikerjakan hook `after` dan tidak diasersi (S-01).
  - TC-GS-IMPORT-900, 901, 902 tidak menyebut cara membuka daftar Division, Position, dan Value Setting Shift selain "Buka Global Settings > User > ..."; spec memakai Search untuk absence dan membuka Value Setting Shift pada halaman Custom Field.
  - TC-GS-IMPORT-903 Expected b ("tidak ada baris yang tersimpan, termasuk baris #1") diamati lewat langkah 10 setelah Discard (baris #1 dan #2 bernilai semula dan berstatus `pending`); kondisi server tidak dibaca langsung dan tidak diasersi sebelum Discard.
