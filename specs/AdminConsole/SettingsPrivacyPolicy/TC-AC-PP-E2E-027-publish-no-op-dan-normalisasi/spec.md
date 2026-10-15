---
id: TC-AC-PP-E2E-027-publish-no-op-dan-normalisasi
title: "Publish Tanpa Perubahan (No-Op) dan Normalisasi Pembanding Konten"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PP-89
  - TC-AC-PP-90
  - TC-AC-PP-195
  - TC-AC-PP-196
  - TC-AC-PP-211
coverage:
  web: automated
---

# Publish Tanpa Perubahan (No-Op) dan Normalisasi Pembanding Konten

## Prerequisites

- Mode: FE+BE. `Spectra.intercept()` dipakai di atas backend nyata untuk mengganti body permintaan Publish dengan konten tertentu (TC-AC-PP-90, 195, 196, 211); intercept dilepas segera setelah permintaan Publish terkirim dan dipulihkan di hook `after` bila spec gagal di tengah. Konten body yang diganti ditulis di langkah.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Hook `before` login akun ini dan membuka Settings > Privacy Policy; hook `after` mengembalikan sesi ke akun default suite yang sama (Total Control). Nama env `AC_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat A (Version 3 Active diterbitkan `John Doe` 10 Aug 2026 20:30 UTC dengan H1 `Privacy Policy`, paragraf `This Privacy Policy describes how we collect, use, and protect your information.`, H3 `1. Information We Collect`; Version 2 `John Doe` 02 Jul 2026; Version 1 `Jane Smith` 15 Jan 2026, akun sudah dihapus). Hook `before` men-seed Riwayat A lewat Fixture BE (riwayat versi append-only dan tidak dapat dihapus lewat UI); Fixture BE yang sama membuat ulang dataset di antara TC.
- Varian isi Riwayat A untuk TC-AC-PP-90 (Fixture BE): paragraf Version 3 memuat `This Privacy Policy describes how we collect, use, and protect your information.` dan teks tebal `Important` memakai tag `strong`. Varian ini disiapkan oleh Fixture BE sebelum blok TC-AC-PP-90; Riwayat A standar dipulihkan sebelum blok TC-AC-PP-211.
- Dokumen Privacy Policy bersifat tunggal platform-wide dan spec ini mem-publish tiga versi; suite berjalan serial (`parallel: false`); hook `after` mengembalikan dataset ke Riwayat A.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Kemampuan teknis: Fixture BE (termasuk varian isi di atas); `Spectra.intercept()` untuk mengganti body Publish.

## Test Steps

### TC-AC-PP-89: Publish tanpa perubahan (konten identik dengan versi Active) menutup dialog dan modal dengan toast netral

1. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
2. Tunggu konten editor termuat (tanpa mengubah konten)
3. Klik `[Publish New Version]`
4. Klik `[Publish]`
5. Verifikasi Dialog Publish Confirm tertutup
6. Verifikasi Modal tertutup
7. Verifikasi kembali ke tabel Version History
8. Verifikasi muncul toast netral "No changes to save."
9. Verifikasi toast sukses "Success, Privacy Policy has been published." tidak tampil
10. Verifikasi tabel tetap menampilkan 3 baris
11. Verifikasi `Version 3` berbadge `Active`
12. Verifikasi tidak ada `Version 4`

### TC-AC-PP-90: Publish dengan perbedaan hanya tag setara (`b` dan `strong`) atau spasi dianggap tidak ada perubahan

13. Siapkan varian isi Riwayat A untuk TC ini lewat Fixture BE (Version 3 memuat teks tebal `Important` memakai tag `strong`) lalu muat ulang tabel
14. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
15. Tunggu konten editor termuat
16. Atur intercept agar body permintaan Publish diganti dengan konten Version 3 yang memakai tag `b` sebagai pengganti `strong` untuk teks `Important`
17. Klik `[Publish New Version]`
18. Klik `[Publish]`
19. Lepas intercept body Publish
20. Verifikasi Dialog Publish Confirm tertutup
21. Verifikasi Modal tertutup
22. Verifikasi muncul toast netral "No changes to save."
23. Verifikasi toast sukses tidak tampil
24. Verifikasi tabel tetap menampilkan 3 baris
25. Verifikasi `Version 3` berbadge `Active`
26. Verifikasi tidak ada `Version 4`
27. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
28. Tunggu konten editor termuat
29. Atur intercept agar body permintaan Publish diganti dengan konten Version 3 yang memuat dua spasi berurutan di tengah kalimat `describes how` serta satu spasi di awal dan akhir paragraf itu
30. Klik `[Publish New Version]`
31. Klik `[Publish]`
32. Lepas intercept body Publish
33. Verifikasi Dialog Publish Confirm tertutup
34. Verifikasi Modal tertutup
35. Verifikasi muncul toast netral "No changes to save."
36. Verifikasi toast sukses tidak tampil
37. Verifikasi tabel tetap menampilkan 3 baris
38. Verifikasi `Version 3` berbadge `Active`
39. Verifikasi tidak ada `Version 4`
40. Kembalikan dataset ke Riwayat A standar lewat Fixture BE lalu muat ulang tabel

### TC-AC-PP-211: Perbedaan huruf besar-kecil adalah perubahan sedangkan tab dan baris baru antar kata dinormalisasi menjadi satu spasi

41. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
42. Tunggu konten editor termuat
43. Atur intercept agar body permintaan Publish diganti dengan konten Version 3 yang paragrafnya memuat tab dan baris baru sebagai pengganti spasi antara kata `describes` dan `how`
44. Klik `[Publish New Version]`
45. Klik `[Publish]`
46. Lepas intercept body Publish
47. Verifikasi Dialog Publish Confirm tertutup
48. Verifikasi Modal tertutup
49. Verifikasi muncul toast netral "No changes to save."
50. Verifikasi tidak ada `Version 4`
51. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
52. Tunggu konten editor termuat
53. Atur intercept agar body permintaan Publish diganti dengan konten Version 3 yang H1 `Privacy Policy` menjadi `privacy Policy`
54. Klik `[Publish New Version]`
55. Klik `[Publish]`
56. Lepas intercept body Publish
57. Verifikasi muncul toast sukses "Success, Privacy Policy has been published."
58. Verifikasi tabel menampilkan `Version 4` berbadge `Active`
59. Klik teks tautan `Version 4`
60. Verifikasi Modal View `Version 4` menampilkan H1 `privacy Policy`
61. Klik `✕` di header untuk menutup Modal View
62. Kembalikan dataset ke Riwayat A standar lewat Fixture BE lalu muat ulang tabel

### TC-AC-PP-195: Publish dengan satu paragraf kosong tambahan dianggap perubahan dan membuat versi baru

63. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
64. Tunggu konten editor termuat
65. Atur intercept agar body permintaan Publish diganti dengan konten Version 3 ditambah `<p></p>` di akhir
66. Klik `[Publish New Version]`
67. Klik `[Publish]`
68. Lepas intercept body Publish
69. Verifikasi muncul toast sukses "Success, Privacy Policy has been published." (bukan toast "No changes to save.")
70. Verifikasi tabel menampilkan `Version 4` berbadge `Active` di baris teratas
71. Kembalikan dataset ke Riwayat A standar lewat Fixture BE lalu muat ulang tabel

### TC-AC-PP-196: Publish yang mengubah heading menjadi paragraf pada teks yang sama dianggap perubahan

72. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
73. Tunggu konten editor termuat
74. Atur intercept agar body permintaan Publish diganti dengan konten Version 3 yang elemen `h3` untuk `1. Information We Collect` diganti menjadi `p` dengan teks yang sama
75. Klik `[Publish New Version]`
76. Klik `[Publish]`
77. Lepas intercept body Publish
78. Verifikasi muncul toast sukses "Success, Privacy Policy has been published." (bukan toast "No changes to save.")
79. Verifikasi tabel menampilkan `Version 4` berbadge `Active`
80. Klik teks tautan `Version 4`
81. Verifikasi Modal View `Version 4` menampilkan `1. Information We Collect` sebagai paragraf biasa
82. Klik `✕` di header untuk menutup Modal View

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC berubah dari urutan nomor (89, 90, 211, 195, 196): TC no-op (89, 90, TC-AC-PP-211 langkah 2) ditaruh sebelum TC yang membuat versi, dan TC-AC-PP-211 (yang berakhir dengan membuat `Version 4`) ditaruh di batas antara keduanya, mengikuti prinsip 3 konvensi (aksi tanpa dampak data lebih dulu) dan karena TC-AC-PP-90 membutuhkan varian isi Riwayat A yang berbeda dari TC lain.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 13 (menyiapkan varian isi TC-AC-PP-90 lewat Fixture BE), langkah 19, 32, 46, 56, 68, 77 (melepas intercept body segera setelah permintaan Publish terkirim, S-09), langkah 40, 62, 71 (mengembalikan Riwayat A standar lewat Fixture BE agar TC berikutnya mulai dari `Version 3` Active), langkah 61 dan 82 (menutup Modal View).
- Post Condition TC ("Tidak ada versi baru dan tidak ada record audit", "Version 4 tersimpan dengan satu record audit") tanpa langkah observasi tidak diasersi; Expected "tidak ada `Version 4`" pada tabel tetap diasersi (langkah 12, 39, 50). Expected b TC-AC-PP-90 ("tabel tetap 3 baris, tidak ada Version 4") adalah satu butir untuk dua variasi; spec mengasersinya setelah tiap variasi (langkah 24-26 setelah variasi tag setara, langkah 37-39 setelah variasi spasi) supaya tiap variasi punya bukti sendiri, dan tidak hanya sekali setelah variasi kedua.
- Alasan penggabungan TC tanpa pembuatan data dan TC pembuat data: kelima TC satu topik (pembanding no-op dan normalisasi pada Publish) dan satu kelas harness; TC no-op (89, 90, TC-AC-PP-211 langkah 2) berjalan lebih dulu sehingga kegagalan keras blok pembuat versi (211 langkah 4, 195, 196) tidak menutupi hasilnya, dan dataset dipulihkan ke Riwayat A standar lewat Fixture BE antar blok.
- Jumlah langkah (82) melewati sekitar 35 langkah karena satu `Verifikasi` per klausa Expected (S-01), setiap variasi body membutuhkan siklus Edit, intercept, dan Publish sendiri, dan lima TC satu topik; tiap blok `###` tetap bermakna walau blok sebelumnya gagal karena dataset di-reseed, sehingga spec tidak dipecah.
- Temuan untuk QA:
  - TC-AC-PP-90 Precondition menyebut "variasi isi Riwayat A untuk TC ini" (teks tebal `Important` memakai `strong`) tetapi Data Uji dan Pre-setup 9 hanya menyebut isi Version 3 secara garis besar; struktur HTML persis varian tidak dinyatakan.
  - TC-AC-PP-90 langkah 2 dan 4 hanya menyebut konten body setelah penggantian; konten Edit yang tampil di editor (apakah ada ketikan) tidak disebut. Spec tidak mengetik apa pun di editor sebelum intercept.
  - TC-AC-PP-195 langkah 2, TC-AC-PP-196 langkah 2, dan TC-AC-PP-211 langkah 2 dan 4 mengandalkan penggantian body lewat intercept; bentuk HTML persis konten Version 3 (termasuk `<h1>`, `<p>`, `<h3>`) tidak dituliskan di TC dan perlu diambil dari Fixture BE oleh script.
