---
id: TC-GS-DIV-E2E-064-changelog-filter-panel-screening-date-dan-populated-dropdown
title: "Filter Panel Changelog: Date Range Picker, Placeholder Select Date, Multi-Select Action, Field, Serta Nilai DISTINCT pada Division Name dan Modified By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-196
  - TC-GS-DIV-197
  - TC-GS-DIV-198
  - TC-GS-DIV-199
  - TC-GS-DIV-200
  - TC-GS-DIV-201
  - TC-GS-DIV-202
  - TC-GS-DIV-203
coverage:
  web: automated
---

# Filter Panel Changelog: Date Range Picker, Placeholder Select Date, Multi-Select Action, Field, Serta Nilai DISTINCT pada Division Name dan Modified By

## Prerequisites

- Login sebagai Role: Total Control
- Buka Filter Panel pada Modal Changelog
- User berada di Global Settings > User > Division
- Riwayat Changelog Division terisi (Create dari TC-GS-DIV-30, Edit dan Delete dari TC Section 3; Modified By: Sari D, Rina M, Agus W, Dewi L)
- Division `Compliance` tidak memiliki entri Changelog; Division yang di-rename dan dihapus masih memiliki entri
- Riwayat Changelog Division terisi (Create dari TC-GS-DIV-30, Edit dan Delete dari TC Section 3; Modified By: Sari D, Rina M, Agus W, Dewi L); entri hasil TC-GS-DIV-101 dan TC-GS-DIV-102 ada

## Test Steps

### Opsi dropdown filter Changelog bersumber dari isi tabel Changelog (TC-GS-DIV-196)

1. Klik icon Changelog di Table Tools
2. Buka Filter
3. Buka dropdown Action, Division Name, Field, dan Modified By
4. Verifikasi Action: `Create`, `Edit`, `Delete` (hanya yang ada di riwayat)
5. Verifikasi Division Name: nama yang tercatat di riwayat; `Compliance` tidak muncul; nama Division yang sudah dihapus atau di-rename tetap muncul
6. Verifikasi Field: `Division Name` dan `Code`
7. Verifikasi Modified By: hanya user yang tercatat di riwayat

### Opsi filter bertambah saat entri Changelog baru tercatat (TC-GS-DIV-197)

8. Klik icon Changelog di Table Tools
9. Buka Filter dan buka dropdown Division Name
10. Admin lain membuat Division `Legal Compliance`
11. Tutup lalu buka kembali dropdown Division Name
12. Verifikasi Opsi `Legal Compliance` muncul pada dropdown Division Name tanpa reload halaman

### Filter Date Modal Changelog menyaring berdasarkan rentang tanggal (TC-GS-DIV-198)

13. Klik icon Changelog di Table Tools
14. Buka Filter, pilih rentang tanggal 1 Jan 2020 sampai 31 Jan 2020
15. Klik `[Apply]`
16. Pilih rentang yang memuat hari uji lalu `[Apply]`
17. Verifikasi Rentang 2020: `No results found`
18. Verifikasi Rentang hari uji: entri hari uji tampil

### Filter multi-select Modal Changelog: Action, Division Name, Field, dan Modified By (TC-GS-DIV-199)

19. Klik icon Changelog di Table Tools
20. Filter Action = `Delete` lalu Apply
21. Clear Field, filter Division Name = `Accounting and Tax` lalu Apply
22. Clear Field, filter Field = `Code` lalu Apply
23. Clear Field, filter Modified By = `Sari D` lalu Apply
24. Verifikasi Action: hanya baris Action `Delete`
25. Verifikasi Division Name: hanya baris `Accounting and Tax`
26. Verifikasi Field: hanya baris Field `Code`
27. Verifikasi Modified By: hanya baris `Sari D`

### Dua opsi pada satu field filter digabung OR (TC-GS-DIV-200)

28. Klik icon Changelog di Table Tools
29. Filter Action centang `Create` dan `Delete`
30. Klik `[Apply]`
31. Verifikasi Tampil baris Action `Create` atau `Delete`; tidak ada baris `Edit`

### Dua field filter berbeda digabung AND (TC-GS-DIV-201)

32. Klik icon Changelog di Table Tools
33. Filter Action = `Edit` dan Field = `Code`
34. Klik `[Apply]`
35. Verifikasi Hanya baris dengan Action `Edit` dan Field `Code` tampil

### Hapus chip filter lewat X menghapus centang opsi (TC-GS-DIV-202)

36. Klik icon Changelog di Table Tools
37. Filter Action centang `Create` dan `Edit`
38. Klik `(X)` pada chip `Create` tanpa membuka dropdown
39. Buka dropdown Action
40. Verifikasi Chip `Create` hilang, chip `Edit` tetap
41. Verifikasi Di dalam dropdown checkbox `Create` ter-uncheck dan `Edit` tetap tercentang

### Uncheck opsi di dalam dropdown menghapus chip (TC-GS-DIV-203)

42. Klik icon Changelog di Table Tools
43. Filter Action centang `Create` dan `Edit`
44. Buka dropdown Action dan uncheck `Create`
45. Verifikasi Chip `Create` hilang dari field, chip `Edit` tetap

## Notes

- Memvalidasi kelima field filter Changelog, placeholder Date "Select date" (NC-11), multi-select Action/Field, dan sumber opsi Division Name & Modified By yang dipopulasikan DISTINCT dari data riwayat murni (PRD §4.1.2, §9.5).
- Sumber pemetaan test case granular: TC-GS-DIV-196, TC-GS-DIV-197, TC-GS-DIV-198, TC-GS-DIV-199, TC-GS-DIV-200, TC-GS-DIV-201, TC-GS-DIV-202, TC-GS-DIV-203.
