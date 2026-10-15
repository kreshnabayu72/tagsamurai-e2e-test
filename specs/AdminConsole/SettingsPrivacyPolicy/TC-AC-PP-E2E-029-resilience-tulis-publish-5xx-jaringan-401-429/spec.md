---
id: TC-AC-PP-E2E-029-resilience-tulis-publish-5xx-jaringan-401-429
title: "Resilience Tulis Publish: Gangguan Jaringan, 429, 400, 413, Sesi Berakhir 401, dan Server Error 5xx"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PP-82
  - TC-AC-PP-83
  - TC-AC-PP-204
  - TC-AC-PP-205
coverage:
  web: automated
---

# Resilience Tulis Publish: Gangguan Jaringan, 429, 400, 413, Sesi Berakhir 401, dan Server Error 5xx

## Prerequisites

- Mode: FE+BE. Kelas harness b (fault injection): `Spectra.intercept()` dipakai di atas backend nyata untuk memaksa respons Publish: kegagalan permintaan di level jaringan tanpa sampai ke server (TC-AC-PP-83), 429, 400, dan 413 (TC-AC-PP-205), 401 (TC-AC-PP-204), dan 500 (TC-AC-PP-82). Intercept dilepas segera setelah permintaan terkirim dan dipulihkan di hook `after` bila spec gagal di tengah.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Hook `before` login akun ini dan membuka Settings > Privacy Policy; langkah login di `## Test Steps` hanya untuk TC-AC-PP-204 (sesi berakhir). Hook `after` mengembalikan sesi ke akun default suite yang sama (Total Control). Nama env `AC_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat A (Version 3 Active diterbitkan `John Doe` 10 Aug 2026 20:30 UTC dengan H1 `Privacy Policy`, paragraf `This Privacy Policy describes how we collect, use, and protect your information.`, H3 `1. Information We Collect`; Version 2 `John Doe` 02 Jul 2026; Version 1 `Jane Smith` 15 Jan 2026, akun sudah dihapus). Hook `before` men-seed Riwayat A lewat Fixture BE (riwayat versi append-only dan tidak dapat dihapus lewat UI); hook `after` mengembalikan dataset ke Riwayat A. Hanya TC-AC-PP-82 yang menghasilkan versi baru (`Version 4`, di akhir spec).
- Dokumen Privacy Policy bersifat tunggal platform-wide; suite berjalan serial (`parallel: false`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Kemampuan teknis: `Spectra.intercept()` (status 500, 401, 429, 400, 413; pembatalan request di level jaringan); tunggu 10 detik nyata untuk toast persisten (jeda pendek, TC-AC-PP-82); penanganan dialog `beforeunload` browser (menerima konfirmasi reload) untuk langkah "Muat ulang halaman" pada TC-AC-PP-205; alur login Total Control untuk TC-AC-PP-204 (email akun di atas dan password dari `Spectra.env.AC_TC_PASSWORD`).

## Test Steps

### TC-AC-PP-83: Publish gagal karena gangguan jaringan atau timeout: form dipertahankan dan retry manual tersedia

1. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
2. Tunggu konten editor termuat
3. Ketik " Timeout case." di akhir konten
4. Klik `[Publish New Version]`
5. Atur intercept agar permintaan Publish digagalkan di level jaringan sebelum sampai ke server (tanpa respons)
6. Klik `[Publish]`
7. Lepas intercept Publish setelah permintaan gagal
8. Verifikasi toast "Connection problem. Please try again." tampil
9. Verifikasi toast tidak memiliki tombol aksi
10. Verifikasi toast "Error, failed to publish Privacy Policy." tidak tampil
11. Verifikasi Dialog Publish Confirm tertutup
12. Verifikasi Modal tetap di state Edit
13. Verifikasi " Timeout case." dipertahankan di editor
14. Verifikasi `[Publish New Version]` enabled
15. Klik `✕` di header
16. Verifikasi Dialog "Unsaved Changes" tampil
17. Klik `[Leave]`
18. Verifikasi tabel tidak menampilkan versi baru (tetap 3 baris, tanpa `Version 4`)

### TC-AC-PP-205: Publish ditolak 429 dan 400 dan status lain di luar daftar

19. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
20. Tunggu konten editor termuat
21. Ketik " Status case." di akhir konten
22. Klik `[Publish New Version]`
23. Atur respons Publish menjadi 429
24. Klik `[Publish]`
25. Lepas intercept Publish
26. Verifikasi toast "Too many requests. Please wait a moment." tampil
27. Verifikasi Dialog Publish Confirm tertutup
28. Verifikasi Modal tetap di state Edit
29. Verifikasi " Status case." dipertahankan di editor
30. Verifikasi `[Publish New Version]` tetap enabled (tanpa cooldown)
31. Verifikasi tidak ada toast sukses
32. Muat ulang halaman dengan F5 dan konfirmasi dialog `beforeunload`
33. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
34. Tunggu konten editor termuat
35. Ketik " Status case." di akhir konten
36. Klik `[Publish New Version]`
37. Atur respons Publish menjadi 400
38. Klik `[Publish]`
39. Lepas intercept Publish
40. Verifikasi error inline "Invalid request. Please check your input." tampil di bawah editor
41. Verifikasi Dialog Publish Confirm tertutup
42. Verifikasi Modal tetap di state Edit
43. Verifikasi " Status case." dipertahankan di editor
44. Verifikasi tidak ada toast sukses
45. Muat ulang halaman dengan F5 dan konfirmasi dialog `beforeunload`
46. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
47. Tunggu konten editor termuat
48. Ketik " Status case." di akhir konten
49. Klik `[Publish New Version]`
50. Atur respons Publish menjadi 413
51. Klik `[Publish]`
52. Lepas intercept Publish
53. Verifikasi toast "Error, failed to publish Privacy Policy." tampil
54. Verifikasi Dialog Publish Confirm tertutup
55. Verifikasi Modal tetap di state Edit
56. Verifikasi " Status case." dipertahankan di editor
57. Verifikasi tidak ada toast sukses
58. Klik `✕` di header
59. Verifikasi Dialog "Unsaved Changes" tampil
60. Klik `[Leave]`
61. Verifikasi tabel tidak menampilkan versi baru (tetap 3 baris, tanpa `Version 4`)

### TC-AC-PP-204: Publish ditolak 401 karena sesi berakhir: redirect ke halaman login dan konten editor tidak dipulihkan

62. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
63. Tunggu konten editor termuat
64. Ketik " Session case." di akhir konten
65. Klik `[Publish New Version]`
66. Atur respons Publish menjadi 401
67. Klik `[Publish]`
68. Lepas intercept Publish
69. Verifikasi halaman berpindah ke halaman login
70. Verifikasi toast "Your session has expired. Please sign in again." tampil
71. Verifikasi tidak ada toast sukses
72. Login kembali sbg Role: Total Control (email akun Total Control dan password dari `Spectra.env.AC_TC_PASSWORD`)
73. Buka Settings > Privacy Policy
74. Verifikasi tabel menampilkan 3 baris Riwayat A
75. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
76. Tunggu konten editor termuat
77. Verifikasi editor terisi konten Version 3 asli tanpa " Session case." (konten editor tidak dipulihkan)
78. Klik `✕` di header (konten tidak diubah, modal tertutup tanpa dialog)

### TC-AC-PP-82: Publish gagal karena server error 5xx: toast error persisten, dialog menutup, modal dan konten dipertahankan, retry manual berhasil

79. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
80. Tunggu konten editor termuat
81. Ketik " Retry me." di akhir konten
82. Klik `[Publish New Version]`
83. Atur respons Publish menjadi 500
84. Klik `[Publish]`
85. Lepas intercept Publish
86. Verifikasi toast error "Error, failed to publish Privacy Policy." tampil
87. Tunggu 10 detik
88. Verifikasi toast "Error, failed to publish Privacy Policy." tetap tampil setelah 10 detik sampai di-dismiss manual
89. Verifikasi Dialog Publish Confirm tertutup
90. Verifikasi Modal tetap di state Edit
91. Verifikasi " Retry me." dipertahankan di editor
92. Verifikasi `[Publish New Version]` enabled
93. Verifikasi tabel di belakang Modal belum menampilkan `Version 4`
94. Dismiss toast secara manual
95. Klik `[Publish New Version]`
96. Klik `[Publish]`
97. Verifikasi toast sukses "Success, Privacy Policy has been published."
98. Verifikasi `Version 4` berbadge `Active`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`. Kelas harness b (fault injection); intercept parsial di atas backend nyata dan asersi state tabel menjadikannya FE+BE (bagian 6 konvensi).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC berubah dari urutan nomor (83, 205, 204, 82): TC yang tidak menghasilkan versi baru lebih dulu dan TC-AC-PP-82 (yang berakhir dengan Publish berhasil dan membuat `Version 4`) di akhir, mengikuti prinsip 3 dan 5 konvensi.
- Login ulang pada TC-AC-PP-204 (langkah 72) adalah langkah pemulihan biasa: TC-AC-PP-204 langkah 3 mewajibkannya setelah sesi berakhir, sebelum langkah verifikasi konten editor. Spec ini seluruhnya kelas b (fault injection) sehingga login ulang tidak memerlukan pengecualian prinsip 13 dan tidak memakai label P-1, P-2, atau P-3.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 7, 25, 39, 52, 68, 85 (melepas intercept Publish segera setelah permintaan terkirim, S-09), langkah 15-17 dan 58-60 (menutup modal dirty lewat `✕`, Verifikasi Dialog "Unsaved Changes" tampil, lalu `[Leave]`; Verifikasi dialog di langkah 16 dan 59 adalah asersi tambahan untuk penutupan deterministik, S-08 dan S-03), langkah 32 dan 45 (reload sesuai langkah TC-AC-PP-205 "Muat ulang halaman dan ulangi langkah 1"), langkah 78 (menutup editor tanpa perubahan), langkah 94 (dismiss toast manual agar `[Publish New Version]` dapat diklik).
- Asersi tambahan yang dicatat: langkah 18 dan 61 mengamati tabel tanpa versi baru untuk Expected "tidak ada versi baru" (TC-AC-PP-83 Expected c dan TC-AC-PP-205 Expected d); langkah 31, 44, 57 memecah "tidak ada toast sukses" per kasus; langkah 10 memverifikasi klausa dalam kurung Expected a TC-AC-PP-83. Klausa majemuk Expected dipecah satu `Verifikasi` per klausa (S-01), mis. langkah 8-9 (toast tampil dan tanpa tombol aksi) dan "Modal tetap di state Edit" terpisah dari "konten dipertahankan".
- Alasan penggabungan TC tanpa pembuatan data dan TC pembuat data: keempat TC satu topik (kegagalan Publish) dan satu kelas harness (b); TC-AC-PP-83, 205, 204 (tanpa pembuatan data) berjalan lebih dulu dan TC-AC-PP-82 (yang berakhir dengan Publish berhasil dan membuat `Version 4`) di akhir, sehingga kegagalan keras blok pembuat data tidak menutupi hasil blok sebelumnya.
- Jumlah langkah (98) jauh melewati sekitar 35 langkah karena satu `Verifikasi` per klausa Expected (S-01) dan tiga status berbeda pada TC-AC-PP-205 (429, 400, 413) yang masing-masing membutuhkan siklus Edit, intercept, dan Publish sendiri; tiap blok `###` membuka sesi Edit sendiri dan tetap bermakna walau blok sebelumnya gagal, sehingga spec tidak dipecah. Saran untuk tim FE bila satu `it()` sepanjang itu menyulitkan: pecah di batas `###` menjadi resilience tanpa data (TC-AC-PP-83, 205, 204) dan satu spec TC-AC-PP-82.
- Post Condition TC ("Tidak ada versi baru dan tidak ada record audit", "Hanya satu versi baru (Version 4) tersimpan setelah retry berhasil") tanpa langkah observasi di TC tidak diasersi.
- Temuan untuk QA:
  - TC-AC-PP-205 langkah 3-4 menulis "Muat ulang halaman" saat modal Edit dirty tanpa menyebut konfirmasi `beforeunload` (lihat TC-AC-PP-71); spec menambah penanganan konfirmasi di langkah 32 dan 45.
  - TC-AC-PP-204 langkah 3 ("Login kembali sbg Role: Total Control") tidak merinci alur login (OTP atau password); spec menulis satu langkah login generik dengan password dari env `AC_TC_PASSWORD`.
  - TC-AC-PP-82 Expected c "Tidak ada versi baru setelah langkah 2" tidak menyebut cara mengamatinya selagi modal terbuka; spec memverifikasi tabel di belakang Modal (langkah 93).
  - TC-AC-PP-205 Expected a memuat pesan 429 "Too many requests. Please wait a moment." yang berasal dari peta status global; spec menulisnya persis seperti TC.
