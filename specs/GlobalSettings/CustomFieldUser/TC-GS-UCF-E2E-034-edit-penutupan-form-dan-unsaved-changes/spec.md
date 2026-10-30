---
id: TC-GS-UCF-E2E-034-edit-penutupan-form-dan-unsaved-changes
title: "Edit Custom Field: Penutupan Popup Edit, Dialog Unsaved Changes, Clear Field, Backdrop, Esc, Navigasi Internal, dan Konfirmasi beforeunload"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-121
  - TC-GS-UCF-125
  - TC-GS-UCF-122
  - TC-GS-UCF-124
  - TC-GS-UCF-462
  - TC-GS-UCF-123
  - TC-GS-UCF-98
  - TC-GS-UCF-329
  - TC-GS-UCF-330
  - TC-GS-UCF-407
coverage:
  web: automated
---

# Edit Custom Field: Penutupan Popup Edit, Dialog Unsaved Changes, Clear Field, Backdrop, Esc, Navigasi Internal, dan Konfirmasi beforeunload

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`).
- Akun aktor (login di hook `before`; password hanya lewat env var): Total Control Client A (Sari Dewi, Modified By `Sari D`) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup 1), `Spectra.env.GS_TC_PASSWORD`.
- Layar awal Global Settings > User > Custom Field dibuka hook `beforeEach`; langkah TC-GS-UCF-330 membentuk riwayat navigasi lewat langkah eksplisit karena navigasi itu objek uji.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-custom-field-user` true untuk akun aktor dan hook `after` memulihkannya, lihat `suite.md`.
- Data Pre-setup Client A (hanya dibuka, tidak pernah disimpan; Last Updated dan Modified By barisnya tidak berubah; 14 field di-seed hook `before` lewat API dengan `Fixture.customFieldUser.preset14`): `Cost Center` (Dropdown: Finance, Operations, Marketing; Placeholder `Select cost center`) untuk TC-GS-UCF-121, 125, 122, 124, 462, 123, 98, 407. Tidak ada Save pada `Cost Center` (S-06).
- Data Dinamis milik spec (seeding lewat API di hook `before`, bersuffix `{runId}-034`; fixture baru `Fixture.customFieldUser.edit034`; Text, Active, Required No):
  - `Edit Revert Probe {runId}-034`: Placeholder `Hint` (TC-GS-UCF-329).
  - `Nav Probe {runId}-034`: Placeholder kosong (TC-GS-UCF-330).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API Custom Field bersuffix `{runId}-034`; tutup popup atau dialog yang masih terbuka.
- Kemampuan teknis: dialog `beforeunload` native browser ditangani framework (konfirmasi bawaan browser pada muat ulang F5 dan penutupan tab dapat dibaca dan dijawab "batal"/"tetap di halaman"); kemampuan ini diminta tim FE untuk TC-GS-UCF-330 dan 407 (TC bertanda Manual Only (b)). Bila kemampuan tidak tersedia, langkah dua TC itu ditandai `unsupported` tanpa menghapus spec. Navigasi Back browser dan menekan `Esc`.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dikelola hook suite).

## Test Steps

### Persiapan tabel

1. Ketik Search `Cost Center`, tekan Enter

### TC-GS-UCF-121: Tutup Popup Edit tanpa perubahan langsung tertutup

2. Klik `⋯` pada baris `Cost Center`, pilih `Edit`
3. Klik `[✕]`
4. Verifikasi popup tertutup tanpa dialog `Unsaved Changes`
5. Klik `⋯` pada baris `Cost Center`, pilih `Edit`
6. Tekan Esc
7. Verifikasi popup tertutup tanpa dialog `Unsaved Changes`

### TC-GS-UCF-125: Klik backdrop di luar popup Edit diabaikan pada form bersih maupun dirty

8. Klik `⋯` pada baris `Cost Center`, pilih `Edit`
9. Klik backdrop
10. Verifikasi popup tetap terbuka
11. Verifikasi dialog `Unsaved Changes` tidak muncul
12. Ubah Placeholder menjadi `Pick`, klik backdrop
13. Verifikasi popup tetap terbuka
14. Verifikasi dialog `Unsaved Changes` tidak muncul
15. Verifikasi Placeholder `Pick` dipertahankan

### TC-GS-UCF-122: Tutup Popup Edit dirty memunculkan dialog Unsaved Changes

16. Klik `[✕]`
17. Verifikasi dialog `Unsaved Changes` (warning) tampil dengan body `You have unsaved changes. Are you sure you want to leave?`
18. Verifikasi dialog memuat tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning)
19. Verifikasi popup Edit tetap terbuka di belakang dialog

### TC-GS-UCF-124: Dialog Unsaved Changes Edit, [Cancel] kembali ke form dengan perubahan dipertahankan

20. Klik `[Cancel]`
21. Verifikasi dialog tertutup
22. Verifikasi popup tetap terbuka dengan Placeholder `Pick`

### TC-GS-UCF-462: Esc pada Popup Edit dirty memunculkan dialog Unsaved Changes

23. Tekan Esc
24. Verifikasi dialog `Unsaved Changes` (warning) tampil dengan body `You have unsaved changes. Are you sure you want to leave?`
25. Verifikasi dialog memuat tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning)
26. Verifikasi popup Edit tetap terbuka di belakang dialog
27. Verifikasi Placeholder `Pick` dipertahankan

### TC-GS-UCF-123: Dialog Unsaved Changes Edit, [Leave] menutup popup dan membuang perubahan

28. Klik `[Leave]`
29. Verifikasi popup tertutup
30. Verifikasi Placeholder `Cost Center` di tabel tetap `Select cost center`

### TC-GS-UCF-98: Clear Field pada Edit mengosongkan seluruh isian bukan mengembalikan nilai tersimpan

31. Klik `⋯` pada baris `Cost Center`, pilih `Edit`
32. Ubah Placeholder menjadi `x`
33. Klik `[Clear Field]`
34. Verifikasi Field Name kosong
35. Verifikasi Data Type kosong
36. Verifikasi Dropdown Values kosong
37. Verifikasi Placeholder kosong
38. Verifikasi Required kembali No
39. Verifikasi input Field Name menampilkan placeholder `Enter field name`
40. Verifikasi field Data Type menampilkan placeholder `Select data type`
41. Verifikasi input Placeholder menampilkan placeholder `Enter placeholder`
42. Verifikasi helper Placeholder `Optional guide text for user profile input. If empty, default placeholder will be applied.`
43. Verifikasi kursor fokus berada di field Field Name
44. Verifikasi tidak ada dialog konfirmasi
45. Verifikasi popup tetap terbuka
46. Klik `[Save]`
47. Verifikasi error `Field name must not be empty`
48. Verifikasi error `Data type must not be empty`
49. Verifikasi tidak ada perubahan tersimpan (tidak ada toast sukses)
50. Klik `[✕]`
51. Verifikasi dialog `Unsaved Changes` tampil
52. Klik `[Leave]`
53. Verifikasi popup tertutup
54. Verifikasi `Cost Center` tidak berubah

### TC-GS-UCF-329: Mengembalikan isian Edit ke nilai tersimpan dianggap bersih

55. Ganti isi kotak search dengan `Edit Revert Probe {runId}-034`, tekan Enter
56. Klik `⋯` pada baris `Edit Revert Probe {runId}-034`, pilih `Edit`
57. Ubah Placeholder `Hint` menjadi `Hint 2`
58. Kembalikan Placeholder menjadi `Hint`
59. Klik `[✕]`
60. Verifikasi popup tertutup langsung tanpa dialog `Unsaved Changes`
61. Verifikasi Placeholder `Edit Revert Probe {runId}-034` tetap `Hint`

### TC-GS-UCF-330: Navigasi internal dan muat ulang saat form Edit dirty memunculkan konfirmasi

62. Buka Global Settings > User > User List, lalu klik tab Custom Field (membentuk riwayat navigasi)
63. Ketik Search `Nav Probe {runId}-034`, tekan Enter
64. Klik `⋯` pada baris `Nav Probe {runId}-034`, pilih `Edit`
65. Ubah Placeholder menjadi `Draft`
66. Klik tombol Back browser
67. Verifikasi Back dicegat dan dialog `Unsaved Changes` tampil dengan `[Cancel]` dan `[Leave]`
68. Klik `[Cancel]`
69. Verifikasi perpindahan dibatalkan dan popup tetap terbuka dengan Placeholder `Draft`
70. Tekan F5
71. Verifikasi konfirmasi bawaan browser muncul saat F5 dalam keadaan dirty
72. Jawab konfirmasi bawaan browser dengan batal
73. Klik `[✕]`
74. Verifikasi dialog `Unsaved Changes` tampil
75. Klik `[Leave]`

### TC-GS-UCF-407: Menutup tab browser saat form Edit dirty memicu konfirmasi bawaan browser

76. Ketik Search `Cost Center`, tekan Enter
77. Klik `⋯` pada baris `Cost Center`, pilih `Edit`
78. Ubah Placeholder menjadi `Draft`
79. Tutup tab browser
80. Verifikasi konfirmasi bawaan browser muncul saat tab ditutup
81. Pilih tetap di halaman pada konfirmasi bawaan browser
82. Verifikasi tab tetap terbuka
83. Verifikasi popup Edit tetap terbuka dengan Placeholder `Draft` dipertahankan
84. Klik `[✕]`
85. Verifikasi dialog `Unsaved Changes` tampil
86. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 86 langkah (di atas smell sekitar 35 langkah): seluruhnya satu kelas (fungsional, penutupan popup Edit), satu akun, dan tiap blok membuka form sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain; jumlah langkah muncul dari satu baris per aksi dan satu `Verifikasi` per klausa Expected.
- Urutan TC: TC-GS-UCF-121 dan 125 (form bersih lebih dulu), lalu TC-GS-UCF-122, 124, 462, 123 yang berurutan pada satu form dirty yang sama dari TC-GS-UCF-125 (Placeholder `Pick`), diakhiri `[Leave]` pada TC-GS-UCF-123 (prinsip 6; form dirty dipakai ulang). Tiap TC sumber memulai dari pembukaan form baru dengan Placeholder `Pick`; keadaan yang diamati sama. Urutan ini berbeda dari urutan TC sumber (98, 329, 330, 407 menyusul dengan pembukaan form masing-masing).
- Jumlah pembukaan popup Edit: 7 (TC-GS-UCF-121 dua kali, 125, 98, 329, 330, 407); jumlah kejadian menutup: 7 (TC-GS-UCF-121 dua kali, rangkaian TC-GS-UCF-125 sampai 123 sekali, 98, 329, 330, 407).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target, membuka tab Custom Field dari User List pada TC-GS-UCF-330 (membentuk riwayat navigasi), menutup form dirty lewat `✕`, `Verifikasi` dialog `Unsaved Changes`, lalu `[Leave]` setelah TC-GS-UCF-330 dan 407 (pembersih agar popup tidak mewarisi state, S-08/S-09).
- Pada TC-GS-UCF-98 Expected b-c-d dipecah menjadi `Verifikasi` per klausa: kosong per field (Field Name, Data Type, Dropdown Values, Placeholder), Required No, placeholder tiap input, fokus, dan tidak ada dialog.
- Pembagian TC lintas spec: TC-GS-UCF-408 (klik backdrop pada dialog Change Data Type, Remove Value, Decimal Places Locked) ada di spec 036; TC-GS-UCF-76 sampai 82, 327, 405, dan 452 (penutupan form Create) ada di spec 019.
- Temuan untuk QA:
  - TC-GS-UCF-330 dan 407 bertanda Manual Only (b) karena dialog `beforeunload` native; kemampuan menangani dialog native browser ditulis sebagai prasyarat (S-08). Cara framework menjawab konfirmasi (batal atau tetap di halaman) tidak didefinisikan di TC; disediakan tim FE.
  - TC-GS-UCF-330: langkah 6 ("Tekan F5, konfirmasi bawaan browser: batal") tidak menyebut keadaan popup sesudah konfirmasi dibatalkan; spec menambah penutupan deterministik (`✕`, `[Leave]`) sebagai penghubung.
  - TC-GS-UCF-98, 121, 122, 123, 124, 462, 125, 329: tidak ada Post Condition.
