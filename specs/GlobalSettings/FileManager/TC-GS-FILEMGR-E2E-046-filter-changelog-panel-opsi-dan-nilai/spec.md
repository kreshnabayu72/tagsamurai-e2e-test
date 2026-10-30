---
id: TC-GS-FILEMGR-E2E-046-filter-changelog-panel-opsi-dan-nilai
title: "Filter Modal Changelog: Panel, Tanpa Field Field, Opsi Dropdown, Multi-Select, Rentang Date, dan AND"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-158
  - TC-GS-FILEMGR-159
  - TC-GS-FILEMGR-160
  - TC-GS-FILEMGR-161
  - TC-GS-FILEMGR-162
  - TC-GS-FILEMGR-163
  - TC-GS-FILEMGR-266
coverage:
  web: automated
---

# Filter Modal Changelog: Panel, Tanpa Field Field, Opsi Dropdown, Multi-Select, Rentang Date, dan AND

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Sinta Maharani (Tabel A1 TC) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi.
- Data Pre-setup: Tabel A4 (14 entri Changelog File Manager; format tanggal General Settings default `dd/MM/yy HH:mm`). Dataset disiapkan lewat fixture BE di hook `before` (kemampuan "disediakan tim FE/BE"; mekanisme dan endpoint seeding tidak didefinisikan di TC, lihat Temuan untuk QA). Entri literal sesuai Tabel A4 karena asersi filter bergantung pada Action, File Name, Modified By, dan Date (pengecualian setara S-12: seeding idempotent, suite serial). Spec hanya membaca data; tidak ada aksi tulis dan tidak ada data dinamis.
- Suite serial (`parallel: false`): hitungan entri hasil filter hanya valid bila tidak ada spec lain yang menghasilkan entri Changelog bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_gs-file-manager` disetel true oleh hook suite `before` dan dipulihkan di `after` (dinyatakan di `suite.md`).
- Hook `beforeEach`: buka Global Settings > File Manager.
- State global yang dipulihkan: tidak ada.
- Kemampuan teknis: kontrol date range picker yang dapat memilih tanggal tetap 10/09/26 sampai 12/09/26 (Date entri Tabel A4 tetap, bukan relatif); mengetik di kotak search di dalam dropdown filter; membaca placeholder field.

## Test Steps

1. Klik ikon Changelog di toolbar
2. Verifikasi tabel Changelog memuat sedikitnya satu entri
3. Klik ikon Filter di toolbar modal

### TC-GS-FILEMGR-158: Screening Filter Panel modal Changelog

4. Verifikasi ikon Filter berubah gelap saat panel terbuka
5. Verifikasi field pertama `Date` berupa date range picker dengan placeholder `Select date`
6. Verifikasi field kedua `Action` berupa multi-select searchable dengan placeholder `All actions`
7. Verifikasi field ketiga `File Name` berupa multi-select searchable dengan placeholder `All files`
8. Verifikasi field keempat `Modified By` berupa multi-select searchable dengan placeholder `All users`
9. Verifikasi tidak ada field `Field` (entitas hanya mencatat satu nilai Field `File Name`)
10. Verifikasi tombol `[Clear Field]` di kiri dan `[Apply]` di kanan

### TC-GS-FILEMGR-159: Filter Field tidak ada karena hanya satu nilai Field tercatat, kolom Field tetap searchable

11. Tutup Filter Panel dengan klik ikon Filter
12. Ketik Search `File Name`, tekan Enter
13. Verifikasi kolom `Field` tetap tampil dengan nilai `File Name` pada seluruh entri
14. Verifikasi Search `File Name` mengembalikan seluruh 14 entri
15. Klik ikon panah (←) di kiri input Search

### TC-GS-FILEMGR-160: Opsi dropdown filter Action dan Modified By berasal dari data Changelog

16. Klik ikon Filter di toolbar modal
17. Buka dropdown `Action`
18. Verifikasi opsi tepat dua: `Delete` dan `Permanently Delete`
19. Verifikasi opsi tidak memuat Action yang tidak tercatat di Changelog
20. Tutup dropdown `Action`, lalu buka dropdown `Modified By`
21. Verifikasi opsi tepat tiga nama lengkap: `Agus Wibowo`, `Sinta Maharani`, `System`
22. Tutup dropdown `Modified By`

### TC-GS-FILEMGR-266: Filter File Name multi-select

23. Buka dropdown `File Name`
24. Verifikasi dropdown memuat tepat 14 opsi (satu per File Name yang tercatat di Changelog)
25. Pilih `archive-photo-01.jpg`, klik `[Apply]`
26. Verifikasi tabel hanya memuat 1 entri
27. Klik `[Clear Field]`
28. Pilih `archive-photo-01.jpg` dan `retired-photo.jpg`, klik `[Apply]`
29. Verifikasi tabel memuat 2 entri (logika OR dalam satu field)

### TC-GS-FILEMGR-161: Filter multi-select Action dan Modified By

30. Klik `[Clear Field]`
31. Pilih `Delete` pada Action, klik `[Apply]`
32. Verifikasi tabel memuat 2 entri: C04 dan C05
33. Klik `[Clear Field]`, klik `[Apply]`
34. Pilih `Delete` dan `Permanently Delete` pada Action, klik `[Apply]`
35. Verifikasi tabel memuat 14 entri
36. Klik `[Clear Field]`, klik `[Apply]`
37. Pilih `System` pada Modified By, klik `[Apply]`
38. Verifikasi tabel memuat 5 entri: C01, C05, `archive-photo-03.jpg`, `archive-photo-06.jpg`, `archive-photo-09.jpg`

### TC-GS-FILEMGR-163: Kombinasi filter Action dan Modified By dengan logika AND

39. Klik `[Clear Field]`
40. Pilih `Permanently Delete` pada Action dan `System` pada Modified By, klik `[Apply]`
41. Verifikasi tabel memuat 4 entri: C01, `archive-photo-03.jpg`, `archive-photo-06.jpg`, `archive-photo-09.jpg`
42. Verifikasi entri C05 (Delete oleh System) tidak tampil

### TC-GS-FILEMGR-162: Filter rentang Date dengan batas inklusif satu hari

43. Klik `[Clear Field]`
44. Pilih Date 12/09/26 sampai 12/09/26, klik `[Apply]`
45. Verifikasi tabel hanya memuat entri C02
46. Klik `[Clear Field]`
47. Pilih Date 10/09/26 sampai 12/09/26, klik `[Apply]`
48. Verifikasi tabel memuat 2 entri: C02 dan C03

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC dalam spec: 158, 159, 160, 266, 161, 163, 162. Screening dan opsi di awal, lalu nilai filter dengan kemajuan dari satu field ke gabungan (266 dan 161 satu field, 163 AND), rentang Date di akhir. TC-GS-FILEMGR-266 diletakkan sebelum 161 karena dropdown File Name dibuka dari panel yang sama dengan TC-GS-FILEMGR-160.
- Panjang spec: 48 langkah, di atas sekitar 35 langkah. Alasan dipertahankan: seluruh blok berkelas sama (filter satu panel, satu dataset Tabel A4, tanpa aksi tulis), setiap blok memulai dari `[Clear Field]` sehingga berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; memecahnya hanya menambah buka modal dan login ulang tanpa pemisah nyata (bagian 3, ukuran batas spec). Blok screening dan opsi (langkah 4 sampai 22) tidak memuat aksi tulis atau pembuat data.
- Pembagian lintas spec: TC-GS-FILEMGR-159 butir a (Filter Panel tidak memuat field `Field`) sudah terasersi pada langkah 9 (TC-GS-FILEMGR-158 butir c), dan tidak diasersi ulang. Kombinasi Search dan Filter Changelog ada di spec `TC-GS-FILEMGR-E2E-047-kombinasi-search-filter-changelog`.
- Anchor: langkah 2 membuktikan tabel Changelog termuat sebelum asersi universal "hanya ...". Langkah 14 memakai total 14 entri pada pagination sebagai pembanding.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 11, 15, 16, 20, 22, 27, 30, 33, 36, 39, 43, 46 (menutup/membuka panel atau dropdown, membersihkan Search, dan membersihkan filter dari blok sebelumnya). Filter Panel diasumsikan tetap terbuka setelah `[Apply]` mengikuti langkah TC.
- Temuan untuk QA:
  - TC tidak menyatakan apakah Filter Panel tetap terbuka setelah `[Apply]`; spec mengikuti langkah TC (langsung `[Clear Field]` setelah `[Apply]`). Perlu konfirmasi perilaku panel agar skrip menulis langkah buka-ulang yang benar.
  - TC-GS-FILEMGR-160 menyebut opsi Action "tepat dua" (`Delete`, `Permanently Delete`) sesuai Tabel A4; opsi dropdown bergantung pada Changelog seluruh client, sehingga bila spec lain menambah Action lain (mis. `Edit`) sebelum spec ini berjalan, langkah 18 dan 21 tidak stabil. Suite serial tidak menjamin urutan spec; dataset di-seed ulang per spec (Q-7).
  - Mekanisme dan endpoint seeding Tabel A4 tidak didefinisikan di TC (Q-4).
