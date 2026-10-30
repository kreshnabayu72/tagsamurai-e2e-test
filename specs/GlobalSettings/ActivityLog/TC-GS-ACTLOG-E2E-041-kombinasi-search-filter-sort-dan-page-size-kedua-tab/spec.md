---
id: TC-GS-ACTLOG-E2E-041-kombinasi-search-filter-sort-dan-page-size-kedua-tab
title: "Kombinasi Search, Filter, Sort, dan Page Size Kedua Tab"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-104
  - TC-GS-ACTLOG-105
  - TC-GS-ACTLOG-106
  - TC-GS-ACTLOG-107
coverage:
  web: automated
---

# Kombinasi Search, Filter, Sort, dan Page Size Kedua Tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (seed BE bersuffix `{runId}-041`, disediakan tim FE/BE; log bersifat append-only sehingga tidak dihapus dan spec tidak mengubahnya). Kata Search dan nilai Filter ditulis literal sesuai TC dan dipenuhi lewat nama bersuffix yang memuat kata itu:
  - Tab Session, irisan TC-GS-ACTLOG-104 (Search `password`, Activity `Login` atau `Change Password`): lebih dari 25 baris dengan sedikitnya dua User berbeda (asersi urutan User A-Z).
  - Tab User Action, irisan TC-GS-ACTLOG-104 (Search `Finance`, Action `Edit` atau `Create`): lebih dari 25 baris dengan sedikitnya dua Object berbeda (asersi urutan Object A-Z).
  - Tab Session: baris User `Budi Anwar {runId}-041` dengan Activity `Login` (TC-GS-ACTLOG-105 sampai 107, Search `Budi` dan Filter `Login`).
  - Tab User Action: baris Name `Acme Corp {runId}-041` dengan Action `Edit` (TC-GS-ACTLOG-105 sampai 107, Search `Acme` dan Filter `Edit`).
  - Irisan Search `password` dengan Activity `Login` (Tab Session) dan Search `Finance` dengan Action `Edit` (Tab User Action) memuat baris (TC-GS-ACTLOG-107).
- Kemampuan teknis (disediakan tim FE/BE): seed BE volume baris log Session dan User Action yang memenuhi syarat di atas; volume lebih dari 25 baris cocok irisan tidak dapat dihasilkan lewat aksi nyata modul sumber dalam satu run.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- State global yang diubah: tidak ada di backend. State Search, Filter, Sort, dan page size tiap tab dibersihkan lewat langkah pemulihan dengan klik ulang menu sidebar Activity Log. Spec tidak membuat atau mengubah data backend. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ACTLOG-104: Kombinasi Search, Filter, Sort, dan page size aktif bersamaan

1. Buka Global Settings > Activity Log > Tab "Session", ketik Search `password`, tekan Enter
2. Klik icon Filter, pilih Activity `Login` dan `Change Password`, klik [Apply]
3. Klik header kolom User satu kali
4. Ubah page size menjadi `25`
5. Verifikasi tabel Tab Session menampilkan irisan Search dan Filter
6. Verifikasi tabel Tab Session terurut User A-Z
7. Verifikasi tabel Tab Session menampilkan maksimal 25 baris per halaman
8. Verifikasi Search `password` tetap aktif di Tab Session
9. Verifikasi Filter Activity `Login` dan `Change Password` tetap aktif di Tab Session
10. Verifikasi sort User `(↑)` tetap aktif di Tab Session
11. Klik tab "User Action", ketik Search `Finance`, tekan Enter
12. Klik icon Filter, pilih Action `Edit` dan `Create`, klik [Apply]
13. Klik header kolom Object satu kali
14. Ubah page size menjadi `25`
15. Verifikasi tabel Tab User Action menampilkan irisan Search dan Filter
16. Verifikasi tabel Tab User Action terurut Object A-Z
17. Verifikasi tabel Tab User Action menampilkan maksimal 25 baris per halaman
18. Verifikasi Search `Finance` tetap aktif di Tab User Action
19. Verifikasi Filter Action `Edit` dan `Create` tetap aktif di Tab User Action
20. Verifikasi sort Object `(↑)` tetap aktif di Tab User Action

### Pemulihan state antar TC

21. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default

### TC-GS-ACTLOG-105: Clear Field Filter saat Search dan Sort aktif

22. Pada Tab Session ketik Search `Budi`, tekan Enter; klik icon Filter, pilih Activity `Login`, klik [Apply]; klik header kolom Date satu kali sehingga sort Date `(↑)` aktif
23. Klik icon Filter, klik [Clear Field], klik [Apply]
24. Verifikasi kriteria Filter terlepas di Tab Session
25. Verifikasi Search `Budi` tetap aktif menyaring tabel Tab Session
26. Verifikasi sort Date `(↑)` tetap aktif di Tab Session
27. Klik tab "User Action", ketik Search `Acme`, tekan Enter; klik icon Filter, pilih Action `Edit`, klik [Apply]; klik header kolom Date satu kali sehingga sort Date `(↑)` aktif
28. Klik icon Filter, klik [Clear Field], klik [Apply]
29. Verifikasi kriteria Filter terlepas di Tab User Action
30. Verifikasi Search `Acme` tetap aktif menyaring tabel Tab User Action
31. Verifikasi sort Date `(↑)` tetap aktif di Tab User Action

### Pemulihan state antar TC

32. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default

### TC-GS-ACTLOG-106: Kosongkan Search saat Filter dan Sort aktif

33. Pada Tab Session ketik Search `Budi`, tekan Enter; klik icon Filter, pilih Activity `Login`, klik [Apply]; klik header kolom Date satu kali sehingga sort Date `(↑)` aktif
34. Klik icon `(✕)` di kotak Search lalu tekan Enter pada kotak kosong
35. Verifikasi kotak Search Tab Session kosong
36. Verifikasi Filter Activity `Login` tetap aktif di Tab Session
37. Verifikasi sort Date `(↑)` tetap aktif di Tab Session
38. Klik tab "User Action", ketik Search `Acme`, tekan Enter; klik icon Filter, pilih Action `Edit`, klik [Apply]; klik header kolom Date satu kali sehingga sort Date `(↑)` aktif
39. Klik icon `(✕)` di kotak Search lalu tekan Enter pada kotak kosong
40. Verifikasi kotak Search Tab User Action kosong
41. Verifikasi Filter Action `Edit` tetap aktif di Tab User Action
42. Verifikasi sort Date `(↑)` tetap aktif di Tab User Action

### Pemulihan state antar TC

43. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default

### TC-GS-ACTLOG-107: Ganti kolom sort saat Search dan Filter aktif

44. Pada Tab Session ketik Search `password`, tekan Enter; klik icon Filter, pilih Activity `Login`, klik [Apply]; klik header kolom Date satu kali sehingga sort Date `(↑)` aktif; klik header kolom User
45. Verifikasi sort berpindah ke kolom User `(↑)` di Tab Session
46. Verifikasi indikator Date tidak aktif di Tab Session
47. Verifikasi Search `password` tetap aktif di Tab Session
48. Verifikasi Filter Activity `Login` tetap aktif di Tab Session
49. Klik tab "User Action", ketik Search `Finance`, tekan Enter; klik icon Filter, pilih Action `Edit`, klik [Apply]; klik header kolom Date satu kali sehingga sort Date `(↑)` aktif; klik header kolom Object
50. Verifikasi sort berpindah ke kolom Object `(↑)` di Tab User Action
51. Verifikasi indikator Date tidak aktif di Tab User Action
52. Verifikasi Search `Finance` tetap aktif di Tab User Action
53. Verifikasi Filter Action `Edit` tetap aktif di Tab User Action

### Pemulihan state akhir

54. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md`. Urutan TC-GS-ACTLOG-104, 105, 106, 107 dipertahankan.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah pemulihan 21, 32, 43, dan 54 (klik ulang menu sidebar mengembalikan kedua tab ke default sesuai aturan reset state tab).
- Spec di atas smell 35 langkah (54 langkah nominal, tanpa perulangan). Alasan: keempat blok memakai dataset, tab, dan kontrol yang sama (kombinasi Search, Filter, Sort, page size) dan berdiri sendiri, karena tiap blok dimulai dari state default hasil klik ulang menu; kegagalan satu blok tidak menghilangkan makna blok lain. Sebagian besar langkah adalah `Verifikasi` yang dipecah per klausa (Search, Filter, sort) untuk dua tab (S-01).
- Sort Date `(↑)` dicapai dengan satu klik pada header Date (default Date terbaru di atas).
- Temuan untuk QA:
  - TC tidak menyebut jumlah baris cocok irisan di TC-105 sampai 107 dan nilai distinct kolom User dan Object untuk asersi A-Z TC-104; kebutuhan seed ditulis di Prerequisites.
  - TC-107 menulis "sort kolom Date" tanpa menyebut arah; spec mengaktifkan sort Date `(↑)` dengan satu klik.
  - Apakah [Apply] menutup Filter Panel atau panel tetap terbuka belum ditetapkan PRD dan TC; langkah "klik icon Filter" sesudah [Apply] (langkah 23, 28) mengikuti pola TC.
  - Post Condition semua TC bernilai `-`; tidak diasersi.
