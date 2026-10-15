---
id: TC-AC-PP-E2E-023-edit-penutupan-modal-esc-klik-luar-navigasi
title: "Edit: Penutupan Modal lewat Esc, Klik Luar, Navigasi Sidebar, Browser Back, dan Reload"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PP-64
  - TC-AC-PP-67
  - TC-AC-PP-68
  - TC-AC-PP-69
  - TC-AC-PP-71
coverage:
  web: automated
---

# Edit: Penutupan Modal lewat Esc, Klik Luar, Navigasi Sidebar, Browser Back, dan Reload

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Hook `before` login akun ini; hook `after` mengembalikan sesi ke akun default suite yang sama (Total Control). Nama env `AC_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Dataset: Riwayat A (Version 3 Active diterbitkan `John Doe` 10 Aug 2026 20:30 UTC dengan H1 `Privacy Policy`, paragraf `This Privacy Policy describes how we collect, use, and protect your information.`, H3 `1. Information We Collect`; Version 2 `John Doe` 02 Jul 2026; Version 1 `Jane Smith` 15 Jan 2026, akun sudah dihapus). Hook `before` men-seed Riwayat A lewat Fixture BE; hook `after` mengembalikan dataset ke Riwayat A. Spec ini tidak mem-publish versi.
- Dokumen Privacy Policy bersifat tunggal platform-wide; suite berjalan serial (`parallel: false`).
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Riwayat browser: hook `before` membuka halaman lain (mis. halaman awal setelah login) sebelum Settings > Privacy Policy sehingga Browser Back punya halaman tujuan (TC-AC-PP-69).
- Kemampuan teknis: klik pada area gelap di luar modal/dialog; tombol Esc dan Backspace; Browser Back; penanganan dialog `beforeunload` browser (menerima konfirmasi reload) untuk TC-AC-PP-71, teks konfirmasi ditentukan browser dan tidak diasersi.

## Test Steps

### TC-AC-PP-64: Menutup state Edit yang belum diubah lewat [✕] dan Esc langsung tanpa dialog sesuai titik masuk

1. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
2. Tunggu konten editor termuat
3. Klik `✕` di header
4. Verifikasi Modal tertutup sepenuhnya
5. Verifikasi tabel tampil
6. Verifikasi tidak ada dialog yang tampil
7. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
8. Tunggu konten editor termuat
9. Tekan Esc
10. Verifikasi Modal tertutup sepenuhnya
11. Verifikasi tabel tampil
12. Verifikasi tidak ada dialog yang tampil
13. Klik teks tautan `Version 3`
14. Klik `[Edit]` di footer
15. Tunggu konten editor termuat
16. Klik `✕` di header
17. Verifikasi Modal kembali ke state View `Version 3`
18. Verifikasi tidak ada dialog yang tampil
19. Klik `✕` di header untuk menutup Modal View
20. Klik teks tautan `Version 3`
21. Klik `[Edit]` di footer
22. Tunggu konten editor termuat
23. Tekan Esc
24. Verifikasi Modal kembali ke state View `Version 3`
25. Verifikasi tidak ada dialog yang tampil
26. Klik `✕` di header untuk menutup Modal View

### TC-AC-PP-67: Klik di luar modal state Edit dan di luar Dialog Unsaved Changes diabaikan pada kondisi clean maupun dirty

27. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
28. Tunggu konten editor termuat
29. Klik area gelap di luar modal (kondisi clean)
30. Verifikasi Modal tetap terbuka
31. Verifikasi tidak ada dialog yang tampil
32. Ketik " Dirty." di akhir konten
33. Klik area gelap di luar modal
34. Verifikasi Modal tetap terbuka
35. Verifikasi Dialog Unsaved Changes tidak muncul
36. Klik `✕` di header
37. Verifikasi Dialog Unsaved Changes tampil
38. Klik area gelap di luar dialog
39. Verifikasi dialog tetap terbuka
40. Verifikasi Modal tetap terbuka
41. Klik `[Leave]`

### TC-AC-PP-68: Berpindah halaman lewat sidebar saat state Edit berubah memunculkan Dialog Unsaved Changes

42. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
43. Tunggu konten editor termuat
44. Ketik " Nav change." di akhir konten
45. Klik item sidebar lain (mis. Settings > User)
46. Verifikasi Dialog "Unsaved Changes" tampil
47. Verifikasi navigasi belum dieksekusi
48. Klik `[Cancel]` pada dialog
49. Verifikasi dialog tertutup
50. Verifikasi halaman tetap di Settings > Privacy Policy
51. Verifikasi Modal tetap di state Edit
52. Verifikasi " Nav change." dipertahankan
53. Klik item sidebar Settings > User lagi
54. Verifikasi Dialog "Unsaved Changes" tampil
55. Klik `[Leave]`
56. Verifikasi navigasi dilanjutkan ke halaman tujuan (Settings > User)
57. Verifikasi perubahan dibuang
58. Buka Settings > Privacy Policy lewat sidebar sehingga halaman sebelumnya (Settings > User) tercatat di riwayat browser

### TC-AC-PP-69: Browser Back saat state Edit berubah memunculkan Dialog Unsaved Changes, saat clean langsung berpindah halaman

59. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
60. Tunggu konten editor termuat
61. Ketik " Back change." di akhir konten
62. Klik Browser Back
63. Verifikasi Dialog "Unsaved Changes" tampil
64. Verifikasi halaman belum berpindah
65. Klik `[Cancel]`
66. Verifikasi dialog tertutup
67. Verifikasi Modal tetap di state Edit
68. Verifikasi " Back change." dipertahankan di editor
69. Tekan Backspace 13 kali di editor sehingga teks " Back change." terhapus dan konten identik dengan konten awal
70. Klik Browser Back
71. Verifikasi halaman langsung berpindah ke halaman sebelumnya
72. Verifikasi tidak ada dialog yang tampil
73. Verifikasi Modal tidak menjadi entri history
74. Buka Settings > Privacy Policy lewat sidebar

### TC-AC-PP-71: Reload atau tutup tab saat state Edit berubah memunculkan konfirmasi bawaan browser, saat clean tidak

75. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
76. Tunggu konten editor termuat
77. Tekan F5
78. Verifikasi halaman dimuat ulang tanpa konfirmasi bawaan browser
79. Klik `[⋯]` pada baris `Version 3` → pilih `Edit`
80. Tunggu konten editor termuat
81. Ketik " Reload change." di akhir konten
82. Tekan F5
83. Verifikasi muncul konfirmasi bawaan browser (`beforeunload`)
84. Konfirmasi reload pada dialog `beforeunload`
85. Verifikasi halaman dimuat ulang
86. Verifikasi perubahan hilang

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan nomor. TC-AC-PP-64 (penutupan bersih) ditaruh pertama sesuai prinsip 3 konvensi.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 19 dan 26 (menutup Modal View), 41 (`[Leave]` menutup modal dirty pada akhir TC-AC-PP-67), 58 dan 74 (membuka Settings > Privacy Policy lewat sidebar agar ada riwayat browser untuk Browser Back dan agar TC berikutnya mulai dari halaman yang benar).
- Asersi tambahan yang dicatat: langkah 40 (Modal tetap terbuka saat klik luar dialog) mengikuti Expected c TC-AC-PP-67 ("dialog dan modal tetap terbuka"); langkah 47 dan 64 memverifikasi "navigasi/halaman belum berpindah" dari Expected a TC-AC-PP-68 dan TC-AC-PP-69.
- Asersi tambahan yang dicatat (S-08, S-03): langkah 54 memverifikasi Dialog "Unsaved Changes" tampil sebelum `[Leave]` pada navigasi sidebar (dialog yang sama sudah muncul di langkah 46, tetapi penutupan kedua dilakukan lewat klik sidebar baru). Klausa majemuk Expected dipecah satu `Verifikasi` per klausa (S-01), mis. "Modal tertutup sepenuhnya" dan "tabel tampil" menjadi dua langkah.
- Jumlah langkah (86) melewati sekitar 35 langkah karena satu `Verifikasi` per klausa Expected (S-01) dan lima TC satu topik (penutupan modal state Edit) dalam satu kelas harness; tiap blok `###` membuka sesi Edit sendiri dan tetap bermakna walau blok sebelumnya gagal, sehingga spec tidak dipecah. Saran untuk tim FE bila satu `it()` sepanjang itu menyulitkan: pecah di batas `###` menjadi dua spec (TC-AC-PP-64, 67 dan TC-AC-PP-68, 69, 71).
- Post Condition TC ("Tidak ada versi baru dan tidak ada record audit", "Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Temuan untuk QA:
  - TC-AC-PP-71 langkah 2-3 memicu reload tanpa menyebut penanganan konfirmasi `beforeunload`; spec menambah langkah 84 (konfirmasi reload) dan kemampuan teknis menangani dialog `beforeunload` di Prerequisites. Teks konfirmasi ditentukan browser dan tidak diasersi.
  - TC-AC-PP-71 Expected a menyebut "tutup tab" pada judul skenario tetapi langkah dan Expected hanya mencakup reload (F5); penutupan tab tidak diuji.
  - TC-AC-PP-69 Expected c menyebut "modal tidak menjadi entri history" tanpa cara mengamatinya; spec memverifikasi lewat hasil Browser Back berpindah ke halaman sebelumnya (langkah 71-73).
