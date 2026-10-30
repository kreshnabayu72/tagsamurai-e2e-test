---
id: TC-GS-UCF-E2E-013-defense-in-depth-input-emoji-markup-dan-bypass-dropdown
title: "Defense-in-Depth Input: Emoji Lolos Filter FE Ditolak Server, Markup Ditampilkan sebagai Teks, dan Dropdown Tanpa Value Ditolak Server"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UCF-308
  - TC-GS-UCF-309
  - TC-GS-UCF-310
  - TC-GS-UCF-467
  - TC-GS-UCF-468
  - TC-GS-UCF-469
coverage:
  web: automated
---

# Defense-in-Depth Input: Emoji Lolos Filter FE Ditolak Server, Markup Ditampilkan sebagai Teks, dan Dropdown Tanpa Value Ditolak Server

## Prerequisites

- Mode: FE+BE (backend nyata).
- Kelas a (defense-in-depth): nilai yang lolos filter keystroke FE diinjeksi ke DOM, dan satu request dikirim langsung ke server (TC-GS-UCF-310). Asersi memakai tampilan FE atas penolakan server (error inline) dan, untuk request langsung, hanya respons server dan state data (bagian 8b butir 1).
- Akun aktor: Total Control (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup, Client A). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` suite membuka Global Settings > User > Custom Field; spec ini tidak menguji navigasi sehingga tidak mengulang langkah buka kecuali berpindah ke User List (langkah form Create User).
- Data Dinamis (bersuffix `{runId}-013`; fixture baru `Fixture.customFieldUser.defense013`). Seed lewat API di hook `before`:
  - D-92: `Bypass DD {runId}-013` (Dropdown, satu value `Solo`); id field dan id opsi `Solo` dicatat dari respons seeding sebagai `{id Bypass DD}` dan `{id opsi Solo}`.
  - D-198: `Edit Bypass DD {runId}-013` (Dropdown: `Alpha`, `Beta`; Placeholder kosong sehingga nilai efektif `Select edit bypass dd {runId}-013`).
  - Dibuat lewat UI oleh spec: D-91 `<b>Bold</b> Probe {runId}-013` (Dropdown: `<img src=x>`, `Beta`, `Gamma`; TC-GS-UCF-308). Nilai uji penolakan server (tidak boleh tersimpan): Field Name `Bad😊Name {runId}-013`, `Red Probe {runId}-013`, `Hint Probe {runId}-013` (TC-GS-UCF-309), serta `Bad😊Name`, `Red🔥`, `Hint🌟` pada Edit (TC-GS-UCF-467, 468, 469). Nama bersuffix agar cleanup deterministik bila server ternyata menerimanya.
- Data Pre-setup: tidak ada yang dipakai langkah (6 field Pre-setup hanya membentuk isi tabel; tidak diubah). Population D-01 tidak di-seed karena tidak ada asersi yang bergantung pada jumlah atau urutannya.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua field bersuffix `{runId}-013` yang masih ada (termasuk `<b>Bold</b> Probe {runId}-013` dan bila ada `Bad😊Name {runId}-013`, `Red Probe {runId}-013`, `Hint Probe {runId}-013`); kosongkan Search tabel.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun Total Control dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: menyetel value field Field Name, input badge Dropdown Values, dan Placeholder langsung pada DOM (menjalankan script pada halaman) lalu memicu event `input`, untuk mensimulasikan emoji yang lolos filter keystroke FE; klien HTTP lewat console browser sesi Total Control (mengirim `PATCH` ke `/v2/iam/user-custom-fields/{id}` dengan token sesi) dan pembacaan status serta isi respons; pembacaan struktur DOM sel tabel, popup, Changelog, dan form Create User untuk memastikan tidak ada elemen markup hasil render; muat ulang halaman.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan hook suite `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UCF-309: Emoji yang lolos filter FE ditolak server (Create)

1. Klik `[+ Custom Field]`
2. Injeksi `Bad😊Name {runId}-013` langsung ke DOM field Field Name (bypass filter keystroke FE) dan picu event `input`
3. Pilih Data Type `Text`
4. Klik `[Submit]`
5. Verifikasi error inline `Field name contains invalid characters` pada Field Name
6. Klik `[Clear Field]`
7. Isi Field Name `Red Probe {runId}-013`, pilih Data Type `Dropdown`
8. Injeksi `Red🔥` langsung ke DOM input Dropdown Values (bypass filter keystroke FE), picu event `input`, tekan Enter
9. Klik `[Submit]`
10. Verifikasi error inline `Option name contains invalid characters` pada Dropdown Values
11. Klik `[Clear Field]`
12. Isi Field Name `Hint Probe {runId}-013`, pilih Data Type `Text`
13. Injeksi `Hint🌟` langsung ke DOM field Placeholder (bypass filter keystroke FE) dan picu event `input`
14. Klik `[Submit]`
15. Verifikasi error inline `Placeholder contains invalid characters` pada Placeholder
16. Klik `✕` di header popup
17. Verifikasi dialog `Unsaved Changes` muncul
18. Klik `[Leave]`
19. Ketik Search `Bad`, tekan Enter
20. Verifikasi record `Bad😊Name {runId}-013` tidak dibuat (empty state `No results found` tampil sebagai anchor hasil Search)
21. Klik `(←)` pada kotak Search
22. Ketik Search `Red Probe`, tekan Enter
23. Verifikasi record `Red Probe {runId}-013` tidak dibuat (empty state `No results found` tampil sebagai anchor hasil Search)
24. Klik `(←)` pada kotak Search
25. Ketik Search `Hint Probe`, tekan Enter
26. Verifikasi record `Hint Probe {runId}-013` tidak dibuat (empty state `No results found` tampil sebagai anchor hasil Search)
27. Klik `(←)` pada kotak Search

### TC-GS-UCF-467: Emoji yang lolos filter FE pada Field Name Edit ditolak server

28. Ketik Search `Edit Bypass DD`, tekan Enter
29. Klik `⋯` pada baris `Edit Bypass DD {runId}-013`, pilih `Edit`
30. Injeksi `Bad😊Name` langsung ke DOM field Field Name (bypass keystroke filter FE) dan picu event `input`
31. Klik `[Save]`
32. Verifikasi error inline `Field name contains invalid characters`
33. Verifikasi popup Edit tetap terbuka
34. Verifikasi tidak ada toast sukses
35. Klik `✕` di header popup
36. Verifikasi dialog `Unsaved Changes` muncul
37. Klik `[Leave]`
38. Verifikasi baris `Edit Bypass DD {runId}-013` tetap dengan Field Name `Edit Bypass DD {runId}-013`
39. Verifikasi Value Setting baris tersebut tetap `Alpha` dan `Beta`
40. Verifikasi Placeholder baris tersebut tetap `Select edit bypass dd {runId}-013`

### TC-GS-UCF-468: Emoji yang lolos filter FE pada rename value Dropdown Edit ditolak server

41. Klik `⋯` pada baris `Edit Bypass DD {runId}-013`, pilih `Edit`
42. Klik teks badge `Alpha`, injeksi `Red🔥` langsung ke DOM input badge (bypass keystroke filter FE), picu event `input`, tekan Enter
43. Klik `[Save]`
44. Verifikasi error inline `Option name contains invalid characters`
45. Verifikasi popup Edit tetap terbuka
46. Verifikasi tidak ada toast sukses
47. Klik `✕` di header popup
48. Verifikasi dialog `Unsaved Changes` muncul
49. Klik `[Leave]`
50. Verifikasi baris `Edit Bypass DD {runId}-013` tetap dengan Field Name `Edit Bypass DD {runId}-013`
51. Verifikasi Value Setting baris tersebut tetap `Alpha` dan `Beta`
52. Verifikasi Placeholder baris tersebut tetap `Select edit bypass dd {runId}-013`

### TC-GS-UCF-469: Emoji yang lolos filter FE pada Placeholder Edit ditolak server

53. Klik `⋯` pada baris `Edit Bypass DD {runId}-013`, pilih `Edit`
54. Injeksi `Hint🌟` langsung ke DOM field Placeholder (bypass keystroke filter FE) dan picu event `input`
55. Klik `[Save]`
56. Verifikasi error inline `Placeholder contains invalid characters`
57. Verifikasi popup Edit tetap terbuka
58. Verifikasi tidak ada toast sukses
59. Klik `✕` di header popup
60. Verifikasi dialog `Unsaved Changes` muncul
61. Klik `[Leave]`
62. Verifikasi baris `Edit Bypass DD {runId}-013` tetap dengan Field Name `Edit Bypass DD {runId}-013`
63. Verifikasi Value Setting baris tersebut tetap `Alpha` dan `Beta`
64. Verifikasi Placeholder baris tersebut tetap `Select edit bypass dd {runId}-013`
65. Klik `(←)` pada kotak Search

### TC-GS-UCF-310: Server menolak Dropdown tanpa value walau UI di-bypass

66. Kirim `PATCH /v2/iam/user-custom-fields/{id Bypass DD}` untuk `Bypass DD {runId}-013` dengan body `{"fieldName":"Bypass DD {runId}-013","dataType":"dropdown","removeDropdownValue":["{id opsi Solo}"]}` (menghapus opsi `Solo`, satu-satunya opsi) lewat console browser
67. Verifikasi respons server `422`
68. Verifikasi respons memuat error field `dropdownValues`: `Dropdown values must not be empty`
69. Muat ulang tab Custom Field (F5)
70. Ketik Search `Bypass DD {runId}-013`, tekan Enter
71. Klik `⋯` pada baris `Bypass DD {runId}-013`, pilih `Edit`
72. Verifikasi definisi field tetap memuat `Solo` pada Dropdown Values
73. Klik `✕` di header popup (form belum diubah sehingga tertutup tanpa dialog `Unsaved Changes`)
74. Klik `(←)` pada kotak Search

### TC-GS-UCF-308: Payload script pada Field Name dan value Dropdown ditampilkan sebagai teks

75. Klik `[+ Custom Field]`
76. Isi Field Name `<b>Bold</b> Probe {runId}-013`, pilih Data Type `Dropdown`
77. Ketik value `<img src=x>`, tekan Enter; ketik value `Beta`, tekan Enter; ketik value `Gamma`, tekan Enter
78. Klik `[Submit]`
79. Verifikasi toast sukses: "Success, custom field has been created."
80. Ketik Search `Bold`, tekan Enter
81. Verifikasi kolom Field Name tabel menampilkan teks literal `<b>Bold</b> Probe {runId}-013`
82. Verifikasi sel Field Name tidak memuat elemen `b` hasil render
83. Verifikasi kolom Value Setting menampilkan badge dengan teks literal `<img src=x>`
84. Verifikasi sel Value Setting tidak memuat elemen `img` hasil render
85. Klik chip `+1 more` pada sel Value Setting
86. Verifikasi popup All Values menampilkan teks literal `<img src=x>`
87. Verifikasi popup All Values tidak memuat elemen `img` hasil render dan tidak ada script yang dieksekusi
88. Klik icon close pada popup
89. Klik icon Changelog
90. Ketik Search `Bold`, tekan Enter
91. Verifikasi Changelog menampilkan teks literal `<b>Bold</b> Probe {runId}-013` pada entri Create
92. Verifikasi Changelog tidak memuat elemen `b` hasil render dan tidak ada script yang dieksekusi
93. Tutup popup Changelog dengan `✕`
94. Klik `(←)` pada kotak Search
95. Buka Global Settings > User > User List, klik `[+ User]`
96. Verifikasi form Create User menampilkan label field `<b>Bold</b> Probe {runId}-013` sebagai teks literal
97. Buka dropdown field `<b>Bold</b> Probe {runId}-013` pada form Create User
98. Verifikasi opsi dropdown menampilkan teks literal `<img src=x>`
99. Verifikasi form Create User tidak memuat elemen `b` atau `img` hasil render dan tidak ada script yang dieksekusi
100. Tutup dropdown, lalu klik `✕` di header popup Create User (form belum diisi sehingga tertutup tanpa dialog `Unsaved Changes`)

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`. Spec ini kelas a (defense-in-depth): nilai yang lolos filter keystroke FE diinjeksi ke DOM (TC-GS-UCF-309, 467, 468, 469), satu request dikirim lewat klien HTTP (TC-GS-UCF-310), dan payload markup dirender sebagai teks (TC-GS-UCF-308).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di spec: 309, 467, 468, 469, 310, 308. Kasus penolakan yang tidak membuat atau mengubah data (309, 467, 468, 469, 310) ditaruh sebelum TC-GS-UCF-308 yang membuat record (bagian 3 prinsip 7). TC-GS-UCF-467, 468, dan 469 memakai satu Search `Edit Bypass DD` (langkah penghubung) dan tiga pembukaan popup Edit, masing-masing ditutup lewat `✕` dan `[Leave]` (S-08). Form Create dibuka dua kali (TC-GS-UCF-309 dan 308, masing-masing ditutup sekali), form Edit empat kali (467, 468, 469 ditutup lewat `✕` dan `[Leave]`; 310 sekali tanpa perubahan), dan form Create User sekali (308); `[Clear Field]` di antara tiga percobaan TC-GS-UCF-309 membersihkan error inline sebelum percobaan berikutnya (S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target, `(←)` untuk mengosongkan Search, membuka popup, `[Clear Field]`, menutup popup, dan muat ulang halaman (F5; tidak ada form terbuka sehingga tidak ada dialog `beforeunload`).
- Asersi absence "record tidak dibuat" (TC-GS-UCF-309 d) beranchor empty state `No results found` yang diproses Search (bagian 8b butir 2). Asersi baris tetap dengan nilai awal (TC-GS-UCF-467 sampai 469) membaca baris yang tampil sesudah `[Leave]`.
- Verifikasi toast sukses pada TC-GS-UCF-308 adalah asersi tambahan di luar Expected TC itu yang menjadi anchor bahwa record tercipta sebelum surface diperiksa (S-03).
- Spec melewati sekitar 35 langkah (100 langkah). Seluruhnya satu kelas (defense-in-depth input) dan satu akun; tiap TC penolakan berdiri sendiri dan TC-GS-UCF-308 yang membuat record ada di akhir sehingga kegagalannya tidak menghilangkan makna TC penolakan.
- Penolakan 422 dengan error field `dropdownValues` (TC-GS-UCF-310) mengikuti keputusan NC-19 (422 field-level); LLD PATCH menulis 409 dengan pesan khusus dan belum diselaraskan (dilacak di `nc-followups.md`). Asersi mengikuti TC dan bisa gagal pada backend nyata sampai LLD diselaraskan.
- Temuan untuk QA:
  - TC-GS-UCF-309 langkah 4 ("Ulangi dengan value Dropdown `Red🔥` dan Placeholder `Hint🌟`") tidak menyebut apakah ketiga nilai dikirim dalam satu Submit atau tiga Submit terpisah, padahal Expected a-c menyebut tiga pesan; spec menjalankan tiga percobaan terpisah (Field Name, value Dropdown, Placeholder) dengan `[Clear Field]` di antaranya.
  - TC-GS-UCF-309 tidak menyebut isi Field Name dan Data Type untuk percobaan value Dropdown dan Placeholder; spec memakai `Red Probe` bertipe `Dropdown` dan `Hint Probe` bertipe `Text`, masing-masing dengan suffix.
  - TC-GS-UCF-308 meminta pengamatan popup All Values Preview, tetapi Dropdown dengan satu value (`<img src=x>`) tidak menampilkan chip `+N more` (TC-GS-UCF-440); spec menambah value `Beta` dan `Gamma` pada field uji sehingga chip `+1 more` muncul. Nilai tambahan itu tidak ada di Data Uji TC.
  - TC-GS-UCF-308 meminta pengamatan "form Create User" tanpa menyebut bagian form tempat field Custom Field tampil dan cara membuka dropdown-nya; teks UI dan struktur form Create User milik modul User (belum ditelusuri sampai teks persis). Spec memakai `[+ User]` dan dropdown field Custom Field tanpa asersi posisi.
  - TC-GS-UCF-308 Expected b ("tidak ada script yang dieksekusi") tidak menyebut cara mengamatinya; spec mengasersi tidak ada elemen `b` atau `img` hasil render pada tiap surface.
  - TC-GS-UCF-310 langkah 2 ("buka Edit Bypass DD") tidak memberi Expected eksplisit selain Expected b; spec mengasersi `Solo` tetap ada di Dropdown Values.
  - TC-GS-UCF-467 sampai 469 menyebut nilai dasar `Edit Bypass DD`, `Alpha`, `Beta`, dan Placeholder `Select edit bypass dd`; spec memakai nama bersuffix sehingga nilai efektif Placeholder menjadi `Select edit bypass dd {runId}-013`.
  - Post Condition TC-GS-UCF-308 ("Field `<b>Bold</b> Probe` (D-91)") tidak punya langkah observasi selain Expected; record dihapus hook `after`.
