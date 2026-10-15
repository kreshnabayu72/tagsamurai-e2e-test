---
id: TC-AC-PP-E2E-008-resilience-baca-modal-view-edit
title: "Resilience Baca Konten di Modal View dan Edit: Loading, Error Load, Try Again, dan Penutupan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PP-31
  - TC-AC-PP-32
  - TC-AC-PP-44
  - TC-AC-PP-45
  - TC-AC-PP-46
  - TC-AC-PP-70
coverage:
  web: automated
---

# Resilience Baca Konten di Modal View dan Edit: Loading, Error Load, Try Again, dan Penutupan

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; dataset Riwayat A dari backend nyata diasersi).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (`Andi Wijaya`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Dataset Riwayat A (Version 3 Active, John Doe, 10 Aug 2026; Version 2; Version 1). Hook `before` men-seed lewat Fixture BE; hook `after` mengembalikan dataset ke Riwayat A. Spec tidak membuat atau mengubah data.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah).
- Kebutuhan intercept (kelas b, `Spectra.intercept()`), semuanya pada respons konten versi (endpoint konten versi):
  - TC-AC-PP-31 dan TC-AC-PP-44: respons konten versi ditahan 5 detik (delay network).
  - TC-AC-PP-32, TC-AC-PP-45, TC-AC-PP-46: respons konten versi dipaksa 500, lalu dipulihkan.
  - TC-AC-PP-46: pada langkah 2, 500 dipasang hanya setelah Modal View terbuka dan konten termuat.
  - TC-AC-PP-70: respons konten versi Active ditahan 5 detik.
  Intercept dilepas segera setelah pemicu selesai dan dipulihkan di hook `after` bila spec gagal di tengah.
- Riwayat browser: TC-AC-PP-70 memerlukan halaman sebelumnya di riwayat browser (pengguna membuka Settings > Privacy Policy dari halaman lain, lalu Browser Back berpindah ke halaman itu).
- Suite berjalan serial (`parallel: false`).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-PP-31: Loading konten versi di Modal View menyembunyikan [Edit] sampai konten termuat

1. Klik menu Settings > Privacy Policy di sidebar
2. Tahan respons konten versi selama 5 detik (delay network)
3. Klik teks tautan `Version 3`
4. Amati modal selama 5 detik
5. Verifikasi Loading component tampil di dalam modal
6. Verifikasi tombol `[Edit]` Hidden
7. Verifikasi hanya `[✕]` yang aktif
8. Lepaskan respons
9. Verifikasi konten rendered tampil
10. Verifikasi tombol `[Edit]` tampil di footer
11. Klik `[✕]` untuk menutup Modal View

### TC-AC-PP-32: Error load konten versi di Modal View menampilkan S-04 dan pulih lewat [Try Again]

12. Atur respons konten versi menjadi 500
13. Klik teks tautan `Version 3`
14. Amati modal
15. Verifikasi di dalam modal tampil "Unable to load this data."
16. Verifikasi di dalam modal tampil button [Try Again]
17. Verifikasi `[Edit]` Hidden
18. Verifikasi hanya `[Try Again]` dan `[✕]` yang aktif
19. Pulihkan respons konten versi menjadi normal (lepas intercept)
20. Klik [Try Again]
21. Verifikasi konten rendered tampil
22. Verifikasi tombol `[Edit]` tampil di footer
23. Klik `[✕]` untuk menutup Modal View

### TC-AC-PP-44: Loading konten saat state Edit dibuka menonaktifkan editor dan tombol sampai konten termuat

24. Tahan respons konten versi Active selama 5 detik (delay network)
25. Klik `[⋯]` pada baris `Version 3`
26. Pilih `Edit`
27. Amati modal selama 5 detik
28. Verifikasi Loading component tampil di area editor
29. Verifikasi editor disabled
30. Verifikasi `[Clear Field]` disabled
31. Verifikasi `[Publish New Version]` disabled
32. Verifikasi hanya `[✕]` yang aktif
33. Verifikasi Title modal "Edit Privacy Policy" tidak tampil
34. Verifikasi info bar tidak tampil (nomor versi belum diketahui)
35. Lepaskan respons
36. Verifikasi editor terisi konten versi Active
37. Verifikasi `[Clear Field]` dan `[Publish New Version]` enabled
38. Verifikasi info bar `Version 3 · Published At 10 Aug 26 · Published By John D` tampil
39. Klik `[✕]` untuk menutup modal (konten belum diubah, tanpa dialog)

### TC-AC-PP-45: Error load konten saat state Edit dibuka menampilkan S-04 dan pulih lewat [Try Again]

40. Atur respons konten versi Active menjadi 500
41. Klik `[⋯]` pada baris `Version 3`
42. Pilih `Edit`
43. Amati modal
44. Verifikasi di dalam modal tampil "Unable to load this data."
45. Verifikasi di dalam modal tampil button [Try Again]
46. Verifikasi editor disabled
47. Verifikasi `[Clear Field]` dan `[Publish New Version]` disabled
48. Verifikasi hanya `[Try Again]` dan `[✕]` yang aktif
49. Verifikasi Title modal "Edit Privacy Policy" tidak tampil
50. Verifikasi info bar tidak tampil
51. Pulihkan respons konten versi menjadi normal (lepas intercept)
52. Klik [Try Again]
53. Verifikasi editor terisi konten versi Active
54. Verifikasi tombol footer `[Clear Field]` dan `[Publish New Version]` enabled
55. Verifikasi info bar `Version 3 · Published At 10 Aug 26 · Published By John D` tampil
56. Verifikasi error state tidak tampil lagi
57. Klik `[✕]` untuk menutup modal (konten belum diubah, tanpa dialog)

### TC-AC-PP-46: [✕] dan Esc saat state Edit masih Loading atau Error load menutup tanpa Dialog Unsaved Changes sesuai titik masuk

58. Tahan respons konten versi
59. Klik `[⋯]` pada baris `Version 3`
60. Pilih `Edit`
61. Klik `[✕]` saat Loading
62. Verifikasi modal tertutup sepenuhnya
63. Verifikasi tabel tampil
64. Verifikasi tidak ada dialog
65. Lepaskan respons yang ditahan
66. Klik teks tautan `Version 3` sehingga Modal View terbuka
67. Tunggu konten termuat sampai `[Edit]` tampil
68. Atur respons konten versi Active menjadi 500
69. Klik `[Edit]` di footer
70. Verifikasi Error load tampil
71. Klik `[✕]`
72. Verifikasi modal kembali ke state View `Version 3`
73. Verifikasi konten versi yang ditampilkan masih tersedia
74. Verifikasi tidak ada dialog
75. Pulihkan respons konten versi (lepas intercept)
76. Klik `[✕]` untuk menutup Modal View
77. Klik teks tautan `Version 3` sehingga Modal View terbuka
78. Tunggu konten termuat sampai `[Edit]` tampil
79. Atur respons konten versi Active menjadi 500
80. Klik `[Edit]` di footer
81. Verifikasi Error load tampil
82. Tekan Esc
83. Verifikasi modal kembali ke state View `Version 3`
84. Verifikasi konten versi yang ditampilkan masih tersedia
85. Verifikasi tidak ada dialog
86. Pulihkan respons konten versi (lepas intercept)
87. Klik `[✕]` untuk menutup Modal View

### TC-AC-PP-70: Browser Back saat state Edit masih Loading berpindah halaman tanpa Dialog Unsaved Changes

88. Buka halaman sebelumnya di riwayat browser (halaman utama setelah login), lalu buka Settings > Privacy Policy lewat sidebar
89. Tahan respons konten versi Active selama 5 detik
90. Klik `[⋯]` pada baris `Version 3`
91. Pilih `Edit`
92. Saat Loading tampil, klik Browser Back
93. Verifikasi halaman langsung berpindah ke halaman sebelumnya
94. Verifikasi Dialog Unsaved Changes tidak tampil (snapshot belum ada)
95. Lepaskan respons yang ditahan

## Notes

- Mode: FE+BE (kelas b, fault injection). Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Spec melewati batas ukuran sekitar 35 langkah (95 langkah, banyak penghubung) karena tiap klausa Expected menjadi satu Verifikasi (S-01) dan enam TC satu kelas dan satu dataset; tiap blok tetap berdiri sendiri bila blok sebelumnya gagal (modal ditutup dan intercept dilepas di akhir tiap blok).
- Langkah penghubung (tanpa awalan Verifikasi, S-03/S-09): langkah 1 (buka halaman), langkah 11, 23, 39, 57, 76, 87 (tutup modal), langkah 19, 51, 65, 75, 86 dan 95 (lepas intercept atau respons yang ditahan), langkah 88 (membuat riwayat browser untuk Browser Back).
- Verifikasi langkah 70 dan 81 (Error load tampil) diturunkan dari tanda "→" di kolom Langkah Uji TC-AC-PP-46 langkah 2 dan 3, bukan dari kolom Expected Result; ditambahkan sebagai penanda state sebelum menutup modal (S-03).
- Penyimpangan urutan: TC-AC-PP-70 ditaruh paling akhir karena Browser Back meninggalkan halaman Privacy Policy.
- Temuan untuk QA:
  - TC-AC-PP-46 langkah 3 berbunyi "Pulihkan respons, ulangi langkah 2 lalu tekan Esc": langkah 2 dimulai dari Modal View yang sudah terbuka (state View) sehingga "ulangi langkah 2" ambigu; spec menutup Modal View lalu membuka ulang dan memasang 500 lagi sebelum menekan Esc (S-04, tidak ditulis "ulangi langkah 2").
  - TC-AC-PP-46 langkah 1 tidak menyebut nasib respons yang ditahan setelah modal ditutup; spec melepasnya (langkah 60).
  - TC-AC-PP-70 precondition ("riwayat browser") tidak menyebut halaman sebelumnya; spec memakai halaman utama setelah login.
