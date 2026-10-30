---
id: TC-GS-DIV-E2E-062-setup-column-changelog-reorder-pin-dan-reset
title: "Setup Column Modal Changelog: Reorder, Pin/Unpin, dan Reset to Default"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-216
  - TC-GS-DIV-217
  - TC-GS-DIV-218
coverage:
  web: automated
---

# Setup Column Modal Changelog: Reorder, Pin/Unpin, dan Reset to Default

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > Division.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Seeding (lewat API oleh akun Sari Dewi di hook `before`): Division `Log Div {runId}-062` dibuat oleh Sari Dewi (entri Changelog Action Create oleh `Sari D`), agar riwayat Changelog terisi.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Division `Log Div {runId}-062`; pulihkan konfigurasi kolom Modal Changelog ke default lewat `[Reset to Default]` atau penghapusan key `localStorage` tabel Changelog; kembalikan viewport ke bawaan. Entri Changelog tidak bisa dihapus.
- Kapasitas: Master Data Count Limit environment automation cukup untuk Division Pre-setup (6) dan Division milik spec ini (1) (disediakan tim FE).
- Konfigurasi kolom (urutan, visibilitas, pin) tersimpan di `localStorage` browser dengan key unik per tabel (PRD division.md §4.2e; prd-conventions.md §9.3). Hook `before` mengosongkan konfigurasi kolom Modal Changelog sehingga spec mulai dari default (urutan `Date` pertama, 7 kolom tampil, tanpa pin). "Muat ulang halaman" dilakukan pada konteks browser yang sama supaya `localStorage` tetap ada.
- Kemampuan teknis: drag and drop elemen daftar kolom; mengatur lebar viewport sehingga tabel Changelog dapat di-scroll horizontal (TC tidak menyebut lebar viewport; kontainer tabel dilebarkan atau viewport diperkecil sampai overflow horizontal); scroll horizontal tabel; membaca dan menghapus key `localStorage` browser.
- Precondition TC-GS-DIV-216, 217, 218: login sebagai Total Control dan berada di Global Settings > User > Division; riwayat Changelog terisi.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite serial (`parallel: false`) karena konfigurasi kolom disimpan di browser yang sama dengan spec lain.
- State global yang dipulihkan: konfigurasi kolom Changelog (default) dan viewport dipulihkan di hook `after`.

## Test Steps

### TC-GS-DIV-216: Setup Column Modal Changelog: reorder tiap kolom lewat drag lalu Save

1. Klik icon Changelog di Table Tools
2. Klik header Actions (⋯), lalu klik `Setup Column...`
3. Seret `Date` ke posisi pertama
4. Klik `[Save]`
5. Verifikasi kolom `Date` berada di posisi pertama tabel
6. Klik header Actions (⋯), klik `Setup Column...`, lalu seret `Action` ke posisi pertama
7. Klik `[Save]`
8. Verifikasi kolom `Action` berada di posisi pertama tabel
9. Klik header Actions (⋯), klik `Setup Column...`, lalu seret `Division Name` ke posisi pertama
10. Klik `[Save]`
11. Verifikasi kolom `Division Name` berada di posisi pertama tabel
12. Klik header Actions (⋯), klik `Setup Column...`, lalu seret `Field` ke posisi pertama
13. Klik `[Save]`
14. Verifikasi kolom `Field` berada di posisi pertama tabel
15. Klik header Actions (⋯), klik `Setup Column...`, lalu seret `Old Value` ke posisi pertama
16. Klik `[Save]`
17. Verifikasi kolom `Old Value` berada di posisi pertama tabel
18. Klik header Actions (⋯), klik `Setup Column...`, lalu seret `New Value` ke posisi pertama
19. Klik `[Save]`
20. Verifikasi kolom `New Value` berada di posisi pertama tabel
21. Klik header Actions (⋯), klik `Setup Column...`, lalu seret `Modified By` ke posisi pertama
22. Klik `[Save]`
23. Verifikasi kolom `Modified By` berada di posisi pertama tabel
24. Muat ulang halaman (F5)
25. Klik icon Changelog di Table Tools
26. Verifikasi urutan terakhir tetap tersimpan: `Modified By`, `New Value`, `Old Value`, `Field`, `Division Name`, `Action`, `Date`

### TC-GS-DIV-217: Setup Column Modal Changelog: pin dan unpin tiap kolom lalu Save

27. Klik header Actions (⋯), klik `Setup Column...`, klik `[Reset to Default]`, lalu klik `[Save]`
28. Perkecil lebar viewport hingga tabel Changelog dapat di-scroll horizontal
29. Klik header Actions (⋯), klik `Setup Column...`, lalu klik icon pin pada `Date`
30. Klik `[Save]`
31. Scroll tabel Changelog secara horizontal
32. Verifikasi kolom `Date` membeku (sticky) saat scroll horizontal
33. Klik header Actions (⋯), klik `Setup Column...`, unpin `Date`, lalu klik `[Save]`
34. Klik header Actions (⋯), klik `Setup Column...`, lalu klik icon pin pada `Action`
35. Klik `[Save]`
36. Scroll tabel Changelog secara horizontal
37. Verifikasi kolom `Action` membeku (sticky) saat scroll horizontal
38. Klik header Actions (⋯), klik `Setup Column...`, unpin `Action`, lalu klik `[Save]`
39. Klik header Actions (⋯), klik `Setup Column...`, lalu klik icon pin pada `Division Name`
40. Klik `[Save]`
41. Scroll tabel Changelog secara horizontal
42. Verifikasi kolom `Division Name` membeku (sticky) saat scroll horizontal
43. Klik header Actions (⋯), klik `Setup Column...`, unpin `Division Name`, lalu klik `[Save]`
44. Klik header Actions (⋯), klik `Setup Column...`, lalu klik icon pin pada `Field`
45. Klik `[Save]`
46. Scroll tabel Changelog secara horizontal
47. Verifikasi kolom `Field` membeku (sticky) saat scroll horizontal
48. Klik header Actions (⋯), klik `Setup Column...`, unpin `Field`, lalu klik `[Save]`
49. Klik header Actions (⋯), klik `Setup Column...`, lalu klik icon pin pada `Old Value`
50. Klik `[Save]`
51. Scroll tabel Changelog secara horizontal
52. Verifikasi kolom `Old Value` membeku (sticky) saat scroll horizontal
53. Klik header Actions (⋯), klik `Setup Column...`, unpin `Old Value`, lalu klik `[Save]`
54. Klik header Actions (⋯), klik `Setup Column...`, lalu klik icon pin pada `New Value`
55. Klik `[Save]`
56. Scroll tabel Changelog secara horizontal
57. Verifikasi kolom `New Value` membeku (sticky) saat scroll horizontal
58. Klik header Actions (⋯), klik `Setup Column...`, unpin `New Value`, lalu klik `[Save]`
59. Klik header Actions (⋯), klik `Setup Column...`, lalu klik icon pin pada `Modified By`
60. Klik `[Save]`
61. Scroll tabel Changelog secara horizontal
62. Verifikasi kolom `Modified By` membeku (sticky) saat scroll horizontal
63. Muat ulang halaman (F5)
64. Klik icon Changelog di Table Tools
65. Scroll tabel Changelog secara horizontal
66. Verifikasi kolom `Modified By` tetap membeku setelah muat ulang halaman
67. Klik header Actions (⋯), klik `Setup Column...`, unpin `Modified By`, lalu klik `[Save]`

### TC-GS-DIV-218: Setup Column Modal Changelog: Reset to Default

68. Klik header Actions (⋯), klik `Setup Column...`, hilangkan centang `Modified By`, klik icon pin pada `Date`, seret `Field` ke posisi pertama, lalu klik `[Save]`
69. Klik header Actions (⋯), lalu klik `Setup Column...`
70. Klik `[Reset to Default]`
71. Klik `[Save]`
72. Verifikasi 7 kolom tampil
73. Verifikasi urutan kolom default: `Date`, `Action`, `Division Name`, `Field`, `Old Value`, `New Value`, `Modified By`
74. Scroll tabel Changelog secara horizontal
75. Verifikasi tidak ada kolom yang membeku
76. Pulihkan lebar viewport ke ukuran semula

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti TC sumber (216, 217, 218). TC-GS-DIV-218 di akhir karena reset mengembalikan konfigurasi yang diubah dua TC sebelumnya.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 25 dan 64 (klik icon Changelog untuk membuka kembali Modal Changelog sesudah muat ulang halaman pada langkah 24 dan 63, karena muat ulang menutup modal), langkah 27 (reset ke default sebelum TC-GS-DIV-217, S-09), langkah 28 (viewport diperkecil agar scroll horizontal teramati), langkah 67 (unpin `Modified By` sesudah F5, pemulihan konfigurasi tanpa pin sebelum TC-GS-DIV-218, S-09), dan langkah 76 (memulihkan viewport). Langkah unpin tiap kolom pada TC-GS-DIV-217 adalah langkah TC.
- Langkah membuka popup (klik header Actions (⋯) lalu `Setup Column...`) digabung dalam langkah aksi pertama di popup tersebut, karena `[Save]` menutup popup dan tabel diamati sesudahnya.
- Pembagian TC Setup Column Changelog: screening, hide/unhide, X, dan kolom visible terakhir ada di spec 061.
- Spec melewati sekitar 35 langkah (76 langkah) karena TC-GS-DIV-216 dan 217 masing-masing menguji tujuh kolom dengan `Verifikasi` per kolom (S-01); semua blok satu kelas harness (Setup Column Modal Changelog), satu akun, satu dataset, dan tiap blok berdiri sendiri karena konfigurasi dikembalikan di tiap kolom (TC-GS-DIV-217) atau di-reset (TC-GS-DIV-218).
- Temuan untuk QA: (1) TC-GS-DIV-216 langkah 3 menyeret `Date` ke posisi pertama padahal `Date` sudah di posisi pertama pada konfigurasi default; Expected a tidak membedakan kasus ini dari kolom lain. (2) TC-GS-DIV-217 tidak menyebut lebar viewport atau cara membuat tabel overflow agar "scroll horizontal" teramati. (3) TC-GS-DIV-216 Expected h tidak menyebut urutan yang diamati; spec mengasersi urutan hasil seret berturut-turut (`Modified By` sampai `Date`). (4) TC-GS-DIV-218 tidak menyebut cara mengamati "tanpa pin"; spec memakai scroll horizontal.
