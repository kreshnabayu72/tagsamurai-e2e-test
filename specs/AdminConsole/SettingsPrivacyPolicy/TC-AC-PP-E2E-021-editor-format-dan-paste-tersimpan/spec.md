---
id: TC-AC-PP-E2E-021-editor-format-dan-paste-tersimpan
title: "Editor: Format Teks, Daftar, dan Paste Tersimpan serta Dirender Setelah Publish"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PP-49
  - TC-AC-PP-50
  - TC-AC-PP-51
  - TC-AC-PP-59
  - TC-AC-PP-60
coverage:
  web: automated
---

# Editor: Format Teks, Daftar, dan Paste Tersimpan serta Dirender Setelah Publish

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Hook `before` login akun ini; hook `after` mengembalikan sesi ke akun default suite yang sama (Total Control). Nama env `AC_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat A (Version 3 Active diterbitkan `John Doe` 10 Aug 2026 20:30 UTC dengan H1 `Privacy Policy`, paragraf `This Privacy Policy describes how we collect, use, and protect your information.`, H3 `1. Information We Collect`; Version 2 `John Doe` 02 Jul 2026; Version 1 `Jane Smith` 15 Jan 2026, akun sudah dihapus). Hook `before` men-seed Riwayat A lewat Fixture BE (riwayat versi append-only dan tidak dapat dihapus lewat UI, sehingga dataset dibuat ulang lewat Fixture BE); hook `after` mengembalikan dataset ke Riwayat A.
- Dokumen Privacy Policy bersifat tunggal platform-wide dan spec ini mem-publish empat versi; suite berjalan serial (`parallel: false`) dan dataset dikembalikan ke Riwayat A di hook `after` serta di langkah penghubung antar-TC.
- Kemampuan teknis: Fixture BE untuk membuat ulang Riwayat A di antara TC; menempel (paste) konten HTML dari clipboard ke editor (izin clipboard browser atau penyuntikan event paste dengan HTML), dengan dua muatan HTML: (a) tabel 1 baris 2 sel (`Cell A`, `Cell B`) dan satu gambar (TC-AC-PP-60), (b) paragraf dengan teks tebal `Pasted bold` dan daftar bertanda butir `Pasted item` (TC-AC-PP-59).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).

## Test Steps

### TC-AC-PP-60: Paste elemen di luar whitelist (tabel, gambar) ke editor

1. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
2. Tunggu konten editor termuat
3. Klik `[Clear Field]`
4. Tempel konten HTML dari clipboard berisi tabel 1 baris 2 sel (`Cell A`, `Cell B`) dan satu gambar
5. Verifikasi teks `Cell A` dan `Cell B` tampil sebagai teks biasa di editor
6. Verifikasi tidak ada struktur tabel di editor (tanpa garis sel atau kolom)
7. Verifikasi gambar tidak dirender (tidak ada elemen gambar di editor)
8. Verifikasi tidak ada dialog yang tampil
9. Verifikasi tidak ada pesan error yang tampil

### TC-AC-PP-49: Format heading H1, H2, H3 pada editor tersimpan dan dirender sebagai heading setelah Publish

10. Klik `[Clear Field]`
11. Ketik "Heading One"
12. Pilih baris itu lalu klik tombol H1
13. Tekan Enter lalu ketik "Heading Two"
14. Pilih baris itu lalu klik tombol H2
15. Tekan Enter lalu ketik "Heading Three"
16. Pilih baris itu lalu klik tombol H3
17. Verifikasi ketiga baris tampil dengan gaya heading level berbeda di editor
18. Klik `[Publish New Version]`
19. Klik `[Publish]`
20. Verifikasi muncul toast sukses "Success, Privacy Policy has been published."
21. Klik teks tautan `Version 4`
22. Verifikasi Modal View `Version 4` menampilkan `Heading One` sebagai heading level 1
23. Verifikasi Modal View `Version 4` menampilkan `Heading Two` sebagai heading level 2
24. Verifikasi Modal View `Version 4` menampilkan `Heading Three` sebagai heading level 3
25. Klik `✕` di header untuk menutup Modal View
26. Kembalikan dataset ke Riwayat A lewat Fixture BE lalu muat ulang tabel

### TC-AC-PP-50: Format Bold, Italic, Underline pada editor tersimpan dan dirender setelah Publish

27. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
28. Tunggu konten editor termuat
29. Klik `[Clear Field]`
30. Ketik "Bold text"
31. Pilih teksnya lalu klik B
32. Tekan Enter lalu ketik "Italic text"
33. Pilih teksnya lalu klik I
34. Tekan Enter lalu ketik "Underline text"
35. Pilih teksnya lalu klik U
36. Klik `[Publish New Version]`
37. Klik `[Publish]`
38. Klik teks tautan `Version 4`
39. Verifikasi `Bold text` tampil tebal di Modal View `Version 4`
40. Verifikasi `Italic text` tampil miring di Modal View `Version 4`
41. Verifikasi `Underline text` tampil bergaris bawah di Modal View `Version 4`
42. Verifikasi ketiga teks tampil sebagai paragraf terpisah
43. Klik `✕` di header untuk menutup Modal View
44. Kembalikan dataset ke Riwayat A lewat Fixture BE lalu muat ulang tabel

### TC-AC-PP-51: List bullet dan list numbered pada editor tersimpan dan dirender setelah Publish

45. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
46. Tunggu konten editor termuat
47. Klik `[Clear Field]`
48. Klik `• List`
49. Ketik "Bullet item A"
50. Tekan Enter
51. Ketik "Bullet item B"
52. Keluarkan kursor dari daftar bertanda butir
53. Klik `1. List`
54. Ketik "Number item A"
55. Tekan Enter
56. Ketik "Number item B"
57. Klik `[Publish New Version]`
58. Klik `[Publish]`
59. Klik teks tautan `Version 4`
60. Verifikasi `Bullet item A` dan `Bullet item B` tampil sebagai daftar bertanda butir
61. Verifikasi `Number item A` dan `Number item B` tampil sebagai daftar bernomor 1 dan 2
62. Klik `✕` di header untuk menutup Modal View
63. Kembalikan dataset ke Riwayat A lewat Fixture BE lalu muat ulang tabel

### TC-AC-PP-59: Paste konten ber-format yang termasuk whitelist dipertahankan sebagai rich text dan tersimpan

64. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
65. Tunggu konten editor termuat
66. Klik `[Clear Field]`
67. Tempel konten HTML dari clipboard berisi paragraf dengan teks tebal `Pasted bold` dan daftar bertanda butir `Pasted item`
68. Verifikasi editor menampilkan `Pasted bold` tebal
69. Verifikasi editor menampilkan `Pasted item` sebagai item daftar
70. Klik `[Publish New Version]`
71. Klik `[Publish]`
72. Klik teks tautan `Version 4`
73. Verifikasi Modal View `Version 4` menampilkan `Pasted bold` tebal
74. Verifikasi Modal View `Version 4` menampilkan `Pasted item` sebagai item daftar
75. Klik `✕` di header untuk menutup Modal View

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC berubah dari urutan nomor: TC-AC-PP-60 (tidak menyimpan data) ditaruh pertama mengikuti prinsip 3 konvensi (aksi tanpa dampak data sebelum aksi yang membuat versi). TC-AC-PP-60 dan TC-AC-PP-49 berbagi satu sesi modal Edit: langkah 1-2 TC-AC-PP-49 ("Klik `[⋯]` → Edit, tunggu konten termuat, lalu klik `[Clear Field]`") sudah dipenuhi sesi TC-AC-PP-60, sehingga TC-AC-PP-49 melanjutkan dari `[Clear Field]` (langkah 10) tanpa membuka ulang modal. Tiap TC lain membuka sesi Edit sendiri dan menutup modalnya lewat Publish.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 25, 43, 62, 75 (menutup Modal View yang ditutup bersih tanpa dialog), langkah 26, 44, 63 (mengembalikan Riwayat A lewat Fixture BE karena TC berikutnya mengharapkan `Version 3` Active dan menerbitkan `Version 4`; dikembalikan juga di hook `after`).
- Alasan penggabungan TC tanpa pembuatan data dan TC pembuat data: kelima TC satu topik (format dan paste pada Rich Text Editor) dan satu kelas harness; TC-AC-PP-60 (tanpa data) dijalankan lebih dulu agar kegagalan keras pada blok pembuat data (Publish) tidak menutupi hasilnya, sedangkan state tiap blok pembuat data dipisah dengan langkah penghubung reseed Riwayat A (langkah 26, 44, 63).
- Jumlah langkah (75) melewati sekitar 35 langkah karena satu `Verifikasi` per klausa Expected (S-01) dan lima blok TC; tiap blok `###` berdiri sendiri setelah reseed Riwayat A sehingga bagian sesudahnya tetap bermakna walau blok sebelumnya gagal, dan spec tidak dipecah.
- Post Condition TC ("Version 4 tersimpan dengan ...; Version 3 tidak berubah") tanpa langkah observasi tidak diasersi.
- Temuan untuk QA:
  - TC-AC-PP-49, 50, 51, 59 mengasumsikan dataset kembali ke Riwayat A sebelum tiap TC (Catatan TC: dataset dibuat ulang lewat fixture BE) tetapi tidak menuliskannya di Precondition; spec menuliskannya sebagai langkah penghubung.
  - TC-AC-PP-51 langkah 2 ("keluarkan dari list") tidak menyebut caranya; spec menuliskan kalimat TC apa adanya (langkah 52) dan implementasi script perlu menentukan aksi keluar daftar (mis. Enter dua kali).
  - TC-AC-PP-49 langkah 2 dan TC-AC-PP-50 langkah 2 memakai "pilih baris itu / pilih teksnya"; cara seleksi (triple-click atau keyboard) diserahkan ke script.
