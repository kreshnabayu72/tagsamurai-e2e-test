---
id: TC-GS-DIV-E2E-022-konflik-create-dua-admin-code-auto-generate-name-dan-code-sama
title: "Konflik Create Dua Admin: Code Auto-Generate Identik, Name Sama, dan Code Manual Sama"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-DIV-272
  - TC-GS-DIV-273
  - TC-GS-DIV-80
  - TC-GS-DIV-79
coverage:
  web: automated
---

# Konflik Create Dua Admin: Code Auto-Generate Identik, Name Sama, dan Code Manual Sama

## Prerequisites

- Mode: FE+BE.
- Akun Sesi A (admin utama): Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`.
- Akun Sesi B (admin kedua): Total Control (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC2_PASSWORD`. Tabel Pre-setup TC Division tidak mencantumkan akun ini; disediakan tim FE (cara yang sama dengan suite Brand).
- Dua sesi browser (kelas multi-konteks): Sesi A dan Sesi B berjalan di konteks browser terpisah dengan sesi login sendiri. Keduanya login di hook `before` spec ini (seedSession, kredensial dari env var) dan berada di Global Settings > User > Division. Hook `after` menutup konteks Sesi B dan mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` dan `GS_TC2_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Data dinamis TC-GS-DIV-272 dan 273: Name bersuffix per run, Code memakai nilai literal TC: `Shared Services {runId}-022` (Code `SHS` dan `SSV`, D-17), `Operations X {runId}-022` (Code `OPX`) dan `Operations Y {runId}-022` (Code `OPX`, D-18).
- Data dinamis TC-GS-DIV-80 dan 79: `Quality Review Team` dan `Quality Resource Team` memakai Name literal karena Code hasil auto-generate diturunkan dari Name (kandidat `QRT`, hasil `QRT` dan `QRT2`); pengecualian S-12 `[KEPUTUSAN 2026-10-21]` untuk Name literal penentu hasil auto-generate Code: seeding idempotent, cleanup hanya milik spec ini, suite berjalan serial (`parallel: false`).
- Hook `before` dan `after` menghapus lewat API sisa data spec ini bila ada, tanpa berasumsi langkah spec berhasil penuh: Division bernama `Quality Review Team` dan `Quality Resource Team`, serta Division ber-Name bersuffix `-022` dari run sebelumnya (`Shared Services`, `Operations X`, `Operations Y`, `Quality Seed`, `Quality Rival`); penghapusan tidak berdasarkan Code saja.
- Data prasyarat TC-GS-DIV-80 (bukan objek uji): `Quality Seed {runId}-022` dengan Code `QRT` (membuat Code `QRT` sudah dipakai) di-seed lewat API pada langkah penghubung, dan `Quality Rival {runId}-022` dengan Code `QRT2` dibuat oleh pemicu (admin lain) tepat di antara percobaan pertama dan retry Create Sesi A. Keduanya dihapus lewat API pada langkah penghubung sebelum TC-GS-DIV-79, dan sekali lagi di hook `after` bila masih ada.
- Hook `beforeEach`: tutup dialog atau modal yang terbuka di kedua sesi lalu kembali ke Global Settings > User > Division.
- Kemampuan teknis: dua konteks browser paralel dalam satu spec; klik `[Submit]` hampir bersamaan di dua sesi (TC-GS-DIV-79); seeding dan penghapusan Division lewat API; kemampuan memasang pemicu sebelum `[Submit]` yang bereaksi tepat di antara percobaan pertama dan retry otomatis server pada Create Sesi A (TC-GS-DIV-80) dengan membuat Division berkode `QRT2` atas nama admin lain, disediakan tim FE/BE karena TC tidak menyebut caranya; langkah ditandai `[Sesi A]` dan `[Sesi B]`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang diubah: tidak ada.

## Test Steps

### TC-GS-DIV-272: Dua admin membuat Division dengan Name sama bersamaan: yang kedua ditolak duplicate

1. [Sesi A] Klik `[+ Division]`
2. [Sesi B] Klik `[+ Division]`
3. [Sesi A] Isi Division Name `Shared Services {runId}-022`
4. [Sesi A] Isi Code `SHS`
5. [Sesi B] Isi Division Name `Shared Services {runId}-022`
6. [Sesi B] Isi Code `SSV`
7. [Sesi A dan Sesi B] Tunggu ±500 ms (debounce pengecekan keunikan)
8. [Sesi A] Klik `[Submit]`
9. [Sesi A] Verifikasi toast sukses: `Success, division has been created.`
10. [Sesi B] Klik `[Submit]`
11. [Sesi B] Verifikasi error inline `Division Name already exists`
12. [Sesi B] Verifikasi modal Create tetap terbuka
13. [Sesi A] Ketik Search `Shared Services {runId}-022`, tekan Enter
14. [Sesi A] Verifikasi hanya ada satu baris Division `Shared Services {runId}-022` di tabel
15. [Sesi A] Klik `(←)` pada kotak Search
16. [Sesi B] Klik `✕` di header modal Create
17. [Sesi B] Verifikasi dialog `Unsaved Changes` tampil
18. [Sesi B] Verifikasi body dialog: `You have unsaved changes. Are you sure you want to leave?`
19. [Sesi B] Verifikasi tombol `[Cancel]` dan `[Leave]` tampil pada dialog
20. [Sesi B] Klik `[Leave]`

### TC-GS-DIV-273: Dua admin membuat Division dengan Code manual sama bersamaan: yang kedua ditolak duplicate

21. [Sesi A] Klik `[+ Division]`
22. [Sesi B] Klik `[+ Division]`
23. [Sesi A] Isi Division Name `Operations X {runId}-022`
24. [Sesi A] Isi Code `OPX`
25. [Sesi B] Isi Division Name `Operations Y {runId}-022`
26. [Sesi B] Isi Code `OPX`
27. [Sesi A dan Sesi B] Tunggu ±500 ms (debounce pengecekan keunikan)
28. [Sesi A] Klik `[Submit]`
29. [Sesi A] Verifikasi toast sukses: `Success, division has been created.`
30. [Sesi B] Klik `[Submit]`
31. [Sesi B] Verifikasi error inline `Code already exists`
32. [Sesi B] Verifikasi modal Create tetap terbuka
33. [Sesi A] Ketik Search `OPX`, tekan Enter
34. [Sesi A] Verifikasi tabel hanya memuat satu baris Division dengan Code `OPX` (`Operations X {runId}-022`)
35. [Sesi A] Verifikasi Division Sesi B `Operations Y {runId}-022` tidak tersimpan (tidak ada di tabel)
36. [Sesi A] Klik `(←)` pada kotak Search
37. [Sesi B] Klik `✕` di header modal Create
38. [Sesi B] Verifikasi dialog `Unsaved Changes` tampil
39. [Sesi B] Verifikasi body dialog: `You have unsaved changes. Are you sure you want to leave?`
40. [Sesi B] Verifikasi tombol `[Cancel]` dan `[Leave]` tampil pada dialog
41. [Sesi B] Klik `[Leave]`

### TC-GS-DIV-80: Retry otomatis Code bentrok lagi diperlakukan sebagai kegagalan biasa

42. Seed lewat API Division `Quality Seed {runId}-022` dengan Code `QRT` sehingga Code `QRT` sudah dipakai
43. [Sesi A] Klik `[+ Division]`
44. [Sesi A] Isi Division Name `Quality Resource Team` (Code dikosongkan)
45. Pasang pemicu (disediakan tim FE/BE) sebelum `[Submit]`: saat Create Sesi A memakai kandidat Code `QRT2`, Division `Quality Rival {runId}-022` dengan Code `QRT2` dibuat oleh admin lain, sehingga bentrok terjadi tepat di antara percobaan pertama dan retry otomatis
46. [Sesi A] Klik `[Submit]`
47. [Sesi A] Verifikasi toast error: `Error, failed to create division.`
48. [Sesi A] Verifikasi modal Create tetap terbuka
49. [Sesi A] Verifikasi Division Name `Quality Resource Team` dipertahankan
50. [Sesi A] Verifikasi Code tetap kosong
51. [Sesi A] Verifikasi tombol `[Submit]` aktif sehingga dapat diklik lagi
52. [Sesi A] Klik `✕` di header modal Create
53. [Sesi A] Verifikasi dialog `Unsaved Changes` tampil
54. [Sesi A] Verifikasi body dialog: `You have unsaved changes. Are you sure you want to leave?`
55. [Sesi A] Verifikasi tombol `[Cancel]` dan `[Leave]` tampil pada dialog
56. [Sesi A] Klik `[Leave]`
57. [Sesi A] Ketik Search `Quality`, tekan Enter
58. [Sesi A] Verifikasi baris `Quality Seed {runId}-022` (Code `QRT`) tampil di tabel
59. [Sesi A] Verifikasi baris `Quality Rival {runId}-022` (Code `QRT2`) tampil di tabel
60. [Sesi A] Verifikasi tidak ada baris `Quality Resource Team` di tabel (Create gagal setelah retry otomatis sekali)
61. [Sesi A] Verifikasi tidak ada Division dengan Code `QRT3` di tabel (tidak ada retry ketiga yang berhasil)
62. [Sesi A] Klik `(←)` pada kotak Search
63. Hapus lewat seeding API `Quality Seed {runId}-022` dan `Quality Rival {runId}-022` sehingga Code `QRT` dan `QRT2` kembali belum dipakai

### TC-GS-DIV-79: Dua Create bersamaan menghasilkan kandidat Code identik: yang kedua retry sekali dan berhasil

64. [Sesi A dan Sesi B] Klik `[+ Division]`
65. [Sesi A] Isi Division Name `Quality Review Team` (Code dikosongkan)
66. [Sesi B] Isi Division Name `Quality Resource Team` (Code dikosongkan)
67. [Sesi A dan Sesi B] Klik `[Submit]` hampir bersamaan
68. [Sesi A] Verifikasi toast sukses: `Success, division has been created.`
69. [Sesi B] Verifikasi toast sukses: `Success, division has been created.`
70. [Sesi A] Verifikasi tidak ada toast error
71. [Sesi A] Verifikasi tidak ada error inline
72. [Sesi B] Verifikasi tidak ada toast error
73. [Sesi B] Verifikasi tidak ada error inline
74. [Sesi A] Muat ulang halaman Division
75. [Sesi A] Ketik Search `Quality R`, tekan Enter
76. [Sesi A] Verifikasi salah satu dari `Quality Review Team` dan `Quality Resource Team` memiliki Code `QRT` dan yang lain memiliki Code `QRT2`
77. [Sesi A] Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md` (TC-GS-DIV-272, 273, 80, 79). Mode: FE+BE. Kelas harness: multi-konteks (dua admin, bagian 3 prinsip 13c).
- Subjudul `###` memetakan langkah ke id TC sumber. Urutan TC berbeda dari urutan nomor TC sumber: TC-GS-DIV-272 dan 273 (tanpa seeding) lebih dulu, TC-GS-DIV-80 sebelum TC-GS-DIV-79. TC-GS-DIV-80 tidak membuat Division `Quality Resource Team` dan butuh Code `QRT` sudah dipakai, sedangkan TC-GS-DIV-79 butuh Code `QRT` belum dipakai dan membuat Division itu; langkah 63 membersihkan data TC-GS-DIV-80 sebelum TC-GS-DIV-79.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 dan 27 (menunggu debounce agar kedua form tidak menampilkan error sebelum Submit); langkah 15, 36, 62, dan 77 (klik `(←)` pada kotak Search setelah diperiksa, menutup input dan mereset tabel); langkah 13, 33, 57, dan 75 (Ketik Search untuk mengamati hasil di tabel Sesi A); langkah 16 sampai 20, 37 sampai 41, dan 52 sampai 56 (menutup form Create yang dirty lewat `✕`, verifikasi dialog `Unsaved Changes`, lalu `[Leave]`); langkah 42 dan 63 (seeding dan pembersihan Division lewat API); langkah 45 (memasang pemicu bentrok retry, mewujudkan langkah 2 TC-GS-DIV-80); langkah 74 (muat ulang agar tabel Sesi A memuat Division hasil kedua sesi).
- Pada TC-GS-DIV-272 dan 273, asersi "hanya satu Division tersimpan" (Expected c TC-GS-DIV-272 dan c TC-GS-DIV-273) diperiksa dari Sesi A (langkah 13 sampai 14 dan 33 sampai 35), karena form Sesi B masih terbuka dan menutup tabelnya.
- Langkah 57 sampai 61 membuktikan Expected a TC-GS-DIV-80 bagian "tidak ada retry ketiga" lewat hasil yang teramati di UI: bila ada retry ketiga, Create akan berhasil dengan Code `QRT3` dan baris `Quality Resource Team` akan ada. Dua baris `Quality Seed` dan `Quality Rival` pada hasil Search `Quality` menjadi anchor bahwa tabel sudah dimuat.
- Sesi B memakai sesi UI karena toast, error inline, dan dialog di Sesi B diasersi.
- Pemenang race pada TC-GS-DIV-79 tidak deterministik, sehingga langkah 76 tidak menetapkan Division mana yang menerima `QRT` dan mana yang menerima `QRT2`.
- Temuan untuk QA:
  - TC-GS-DIV-80 langkah 2 ("Saat retry otomatis pertama ... dibuat bentrok lagi") tidak menyebut cara memicu bentrok di antara percobaan pertama dan retry, dan retry berjalan di server (`EC-09`, `EC-26` pada PRD), sehingga teramati hanya lewat hasil akhir. Spec meminta tim FE/BE menyediakan pemicunya (Prerequisites).
  - TC-GS-DIV-80 tidak menyebut Division mana yang memegang Code `QRT` dan `QRT2`; spec memakai seeding Division `Quality Seed {runId}-022` dan `Quality Rival {runId}-022`.
  - Post Condition TC-GS-DIV-79 ("Dua Division dengan Code QRT dan QRT2 tersimpan") dan TC-GS-DIV-80 ("Record tidak dibuat pada percobaan itu") memiliki padanan di Expected (langkah 76 dan 60). Post Condition TC-GS-DIV-272 dan 273 ("Tepat 1 Division") memiliki padanan di Expected c TC-GS-DIV-272 (langkah 14) dan Expected c TC-GS-DIV-273 (langkah 34 dan 35).
- Spec melewati sekitar 35 langkah karena memuat empat kasus konflik dua admin yang masing-masing butuh aksi dua sesi dan penutupan form dirty di Sesi pihak yang ditolak; seluruhnya satu kelas harness (multi-konteks) dan blok TC-GS-DIV-272 dan 273 memakai data sendiri, sedangkan TC-GS-DIV-80 dan TC-GS-DIV-79 berurutan karena berbagi Code `QRT` dan `QRT2` (langkah 63 membersihkan sebelum TC-GS-DIV-79).
