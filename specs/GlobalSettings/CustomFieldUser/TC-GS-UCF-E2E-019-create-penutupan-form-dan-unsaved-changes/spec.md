---
id: TC-GS-UCF-E2E-019-create-penutupan-form-dan-unsaved-changes
title: "Popup Create Custom Field: Penutupan Form, Dialog Unsaved Changes, Backdrop, Navigasi, dan Konfirmasi Browser"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-76
  - TC-GS-UCF-77
  - TC-GS-UCF-78
  - TC-GS-UCF-79
  - TC-GS-UCF-452
  - TC-GS-UCF-80
  - TC-GS-UCF-81
  - TC-GS-UCF-327
  - TC-GS-UCF-82
  - TC-GS-UCF-405
coverage:
  web: automated
---

# Popup Create Custom Field: Penutupan Form, Dialog Unsaved Changes, Backdrop, Navigasi, dan Konfirmasi Browser

## Prerequisites

- Mode: FE+BE (backend nyata). Satu Create sungguhan terjadi di TC-GS-UCF-82 (Submit valid lalu F5); sisanya tidak mengirim Create.
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`; environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_<page_key>` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Layar awal: Global Settings > User > tab Custom Field, dibuka di hook `beforeEach`.
- Data Pre-setup: tidak ada yang dibaca atau diubah.
- Data dinamis: field `Reload Probe {runId}-019` (Text) dibuat TC-GS-UCF-82 lewat Submit valid (`{runId}` terdiri atas digit). Nilai `Umbra` hanya diketik dan tidak pernah tersimpan.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API field Client A yang namanya memuat `{runId}-019`.
- Kemampuan teknis (TC-GS-UCF-82 dan 405 bertanda Manual Only di TC karena dialog `beforeunload` native): penanganan dialog konfirmasi bawaan browser `beforeunload` pada muat ulang (F5) dan penutupan tab (membaca bahwa dialog muncul, lalu memilih batal atau tetap di halaman); penutupan tab browser. Bila framework tidak dapat menangani dialog ini, spec ditandai `coverage.web: unsupported` oleh tim FE (bagian 2 konvensi). Klik pada backdrop di luar popup; penekanan Esc dan F5; navigasi sidebar ke Global Settings > Activity Log.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UCF-76: Tutup Popup Create bersih lewat [✕] dan Esc tanpa dialog

1. Klik [+ Custom Field]
2. Centang checkbox `Stay on this form after submitting` (tidak dilepas)
3. Klik `[✕]`
4. Verifikasi popup tertutup langsung
5. Verifikasi dialog `Unsaved Changes` tidak muncul (checkbox Stay tidak membuat form dirty)
6. Klik [+ Custom Field]
7. Tekan Esc
8. Verifikasi popup tertutup tanpa dialog

### Form dirty `Umbra` (TC-GS-UCF-80, 77, 79, 452, 82, 405, 327)

9. Klik [+ Custom Field]

#### TC-GS-UCF-80: Klik backdrop di luar popup Create diabaikan pada form kosong maupun dirty

10. Klik backdrop di luar popup
11. Verifikasi popup tetap terbuka
12. Verifikasi dialog `Unsaved Changes` tidak muncul
13. Ketik `Umbra` di Field Name
14. Klik backdrop di luar popup lagi
15. Verifikasi popup tetap terbuka
16. Verifikasi dialog `Unsaved Changes` tidak muncul
17. Verifikasi input `Umbra` dipertahankan

#### TC-GS-UCF-77: Tutup Popup Create dirty memunculkan dialog Unsaved Changes

18. Klik `[✕]`
19. Verifikasi dialog `Unsaved Changes` (warning) tampil dengan body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning)
20. Verifikasi popup Create tetap terbuka di belakang dialog

#### TC-GS-UCF-79: Dialog Unsaved Changes Create: [Cancel] dan Esc kembali ke form dengan input dipertahankan

21. Klik [Cancel]
22. Verifikasi dialog tertutup
23. Verifikasi popup tetap terbuka dengan `Umbra`
24. Klik `[✕]` lagi
25. Tekan Esc pada dialog
26. Verifikasi dialog tertutup
27. Verifikasi popup tetap terbuka dengan `Umbra`

#### TC-GS-UCF-452: Esc pada Popup Create dirty memunculkan dialog Unsaved Changes

28. Tekan Esc pada popup
29. Verifikasi dialog `Unsaved Changes` (warning) tampil dengan body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` (text, contrast) dan `[Leave]` (filled, warning)
30. Verifikasi popup Create tetap terbuka di belakang dialog dengan `Umbra` dipertahankan
31. Klik [Cancel]

#### TC-GS-UCF-82 (bagian form dirty): Muat ulang browser saat form Create dirty memicu konfirmasi bawaan browser

32. Tekan F5 (pada konfirmasi browser pilih batal)
33. Verifikasi konfirmasi bawaan browser (`beforeunload`) muncul
34. Pilih batal pada konfirmasi browser agar tetap berada di halaman

#### TC-GS-UCF-405: Menutup tab browser saat form Create dirty memicu konfirmasi bawaan browser

35. Tutup tab browser
36. Verifikasi konfirmasi bawaan browser muncul saat tab ditutup
37. Pilih tetap di halaman pada konfirmasi bawaan browser
38. Verifikasi tab tetap terbuka
39. Verifikasi popup Create tetap terbuka dengan `Umbra` dipertahankan

#### TC-GS-UCF-327: Navigasi internal saat form Create dirty memunculkan dialog Unsaved Changes dengan [Cancel] dan [Leave]

40. Klik menu sidebar Global Settings > Activity Log
41. Verifikasi perpindahan route dicegat dan dialog `Unsaved Changes` tampil dengan body `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` dan `[Leave]`
42. Klik [Cancel]
43. Verifikasi perpindahan dibatalkan dan popup tetap terbuka dengan `Umbra` dipertahankan
44. Klik menu sidebar Global Settings > Activity Log lagi
45. Klik [Leave]
46. Verifikasi halaman Activity Log terbuka
47. Verifikasi popup Create tertutup

### TC-GS-UCF-78: Dialog Unsaved Changes Create: [Leave] menutup popup dan membuang input

48. Buka Global Settings > User > tab Custom Field
49. Klik [+ Custom Field]
50. Ketik `Umbra` di Field Name
51. Klik `[✕]`
52. Klik [Leave]
53. Verifikasi dialog tertutup
54. Verifikasi popup tertutup
55. Klik [+ Custom Field]
56. Verifikasi popup Create baru terbuka dengan Field Name kosong

### TC-GS-UCF-81: Mengembalikan isian ke kondisi awal dianggap bersih

57. Ketik `Umbra` di Field Name
58. Hapus kembali hingga kosong
59. Klik `[✕]`
60. Verifikasi popup tertutup langsung tanpa dialog `Unsaved Changes`

### Absence record `Umbra` (lanjutan TC-GS-UCF-78)

61. Ketik Search `Umbra`, tekan Enter
62. Verifikasi empty state `No results found` tampil (tidak ada record `Umbra`)
63. Klik `(←)` pada kotak Search

### TC-GS-UCF-82 (bagian form bersih dan sesudah Submit): konfirmasi browser tidak muncul

64. Klik [+ Custom Field]
65. Ketik `Umbra` di Field Name
66. Kosongkan input Field Name
67. Tekan F5
68. Verifikasi halaman Custom Field termuat ulang dan [+ Custom Field] tampil
69. Verifikasi tidak ada konfirmasi bawaan browser saat form bersih
70. Klik [+ Custom Field]
71. Isi Field Name `Reload Probe {runId}-019`, Data Type `Text`
72. Klik [Submit]
73. Verifikasi toast sukses: "Success, custom field has been created."
74. Tekan F5
75. Verifikasi halaman Custom Field termuat ulang dan [+ Custom Field] tampil
76. Verifikasi tidak ada konfirmasi bawaan browser setelah Submit sukses

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 76, 80, 77, 79, 452, 82 (bagian dirty), 405, 327, 78, 81, 82 (bagian bersih), berbeda dari urutan sumber (76 sampai 82, 405, 327, 452). Satu pembukaan form dirty `Umbra` (langkah 9) dipakai untuk TC-GS-UCF-80, 77, 79, 452, 82 (bagian dirty), 405, dan 327, yang semuanya mengembalikan atau mempertahankan form; kejadian menutup form (Leave pada TC-GS-UCF-327) ditaruh paling akhir pada form itu. TC-GS-UCF-82 terbelah dua: langkah 2 TC (F5 dirty, batal) di langkah 32 sampai 34, dan langkah 3 sampai 4 TC (F5 form bersih, F5 setelah Submit) di langkah 64 sampai 76 karena F5 pada form bersih memuat ulang halaman. Jumlah pembukaan form: 6 (langkah 1, 6, 9, 49, 55, 64) ditambah satu pembukaan Submit valid (langkah 70).
- Langkah 55 dan 56 (membuka popup baru) adalah pembukaan form yang mengasersi TC-GS-UCF-78 Expected c; popup yang sama dipakai TC-GS-UCF-81 (langkah 57 sampai 60).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2 (centang Stay), 21, 31, 34, 37, 42, 44 (menutup dialog atau konfirmasi, atau mengulang pemicu), langkah 48 (kembali ke tab Custom Field sesudah Leave pada TC-GS-UCF-327), langkah 61 dan 63 (Search `Umbra` dan reset Search), serta pengisian form dan klik tombol sebagai bagian langkah TC.
- Langkah 73 (`Verifikasi` toast sukses) tidak tertulis eksplisit sebagai Expected TC-GS-UCF-82 ("Setelah Submit sukses tidak ada konfirmasi"); ditulis sebagai anchor bahwa Submit benar sukses sebelum F5. Teks toast mengikuti toast Create pada TC lain.
- Langkah 62 (`Verifikasi` empty state `No results found`) adalah anchor positif untuk absence record `Umbra` (TC-GS-UCF-78 Expected b).
- Spec melewati sekitar 35 langkah (smell, bagian 3 prinsip 13 konvensi): 10 TC satu topik (penutupan popup Create) dengan satu akun; setiap Expected bermajemuk dipecah satu `Verifikasi` per klausa (S-01). Blok sesudah blok lain tetap bermakna bila blok sebelumnya gagal karena tiap blok mengasersi mekanisme penutupan yang berbeda.
- Temuan untuk QA:
  - TC-GS-UCF-82 dan 405 bertanda Manual Only (dialog `beforeunload` native). Kemampuan menangani dialog itu (dan menutup tab) ditulis di Prerequisites sebagai kebutuhan tim FE; bila tidak tersedia, spec ditandai `coverage.web: unsupported`.
  - TC-GS-UCF-82 langkah 3 ("Kosongkan input, tekan F5") tidak menyebut apakah popup dibuka ulang sebelum langkah 4; spec membuka ulang popup (langkah 70) karena F5 memuat ulang halaman.
  - TC-GS-UCF-82 langkah 4 membuat Custom Field sungguhan (Submit valid) tanpa menyebut nama; spec memakai `Reload Probe {runId}-019` dan menghapusnya di hook `after`.
