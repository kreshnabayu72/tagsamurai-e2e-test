---
id: TC-GS-POS-E2E-023-bulk-select-all-lintas-halaman-dan-retensi
title: "Bulk Selection Position: Select All (N records), Unselect All, Uncheck dari 100%, Retensi Seleksi, dan Seleksi yang Tidak Tampil karena Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-129
  - TC-GS-POS-131
  - TC-GS-POS-132
  - TC-GS-POS-133
  - TC-GS-POS-134
coverage:
  web: automated
---

# Bulk Selection Position: Select All (N records), Unselect All, Uncheck dari 100%, Retensi Seleksi, dan Seleksi yang Tidak Tampil karena Filter

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`).
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position; langkah 1 tidak mengulang pembukaan layar.
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, tanpa suffix): Position 10 sampai 16 (7 record), yang ikut terhitung dalam jumlah total baris tabel N.
- Data Dinamis (di-seed lewat API di hook `before`; fixture baru `Fixture.position.bulkSelect023`): 15 Position bersuffix `{runId}-023`: `Account Executive`, `Business Analyst`, `Content Writer`, `Customer Support Agent`, `Facility Manager`, `Graphic Designer`, `Network Engineer`, `Product Designer`, `Project Coordinator`, `Research Analyst`, `Sales Representative`, `Software Tester`, `System Administrator`, `Technical Writer`, dan `UX Researcher`, masing-masing diikuti ` {runId}-023`; tidak dipakai user. N diturunkan dari seeding (7 Pre-setup + 15 seeding = 22, lebih dari 10, sehingga ada halaman 2) dan ditetapkan pada langkah 1, bukan dibaca dari tabel yang hanya menampilkan satu halaman.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API semua Position bersuffix `{runId}-023` yang masih ada. Spec ini tidak menghapus data lewat UI; Bulk Delete pada TC-GS-POS-134 hanya dibuka sampai dialog lalu dibatalkan.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` menjadi true untuk akun aktor spec ini (Total Control) dan hook `after` memulihkannya (lihat `suite.md`).
- Kemampuan teknis: Search tabel, Sort header, Filter Last Updated, dan pemilihan halaman; pembacaan state checkbox dan teks Bulk Action Bar.
- State global: Selection Limit di Admin Console > Plans & Licensing > Lifecycle Settings > System Limits berada pada nilai default (lebih besar dari N) dan tidak diubah spec ini. Flag Guided Tooltip diatur hook suite.

## Test Steps

### TC-GS-POS-129: Select All (N records) memilih seluruh baris lintas halaman

1. Tetapkan N = 22 (7 Position Pre-setup ditambah 15 Position seeding)
2. Centang baris `Account Executive {runId}-023`
3. Klik "Select All (N records)"
4. Verifikasi counter berubah menjadi "N Positions selected"
5. Verifikasi tombol berubah menjadi "Unselect All"
6. Pindah ke halaman 2
7. Verifikasi baris di halaman 2 tercentang
8. Klik icon `✕` pada Bulk Action Bar
9. Kembali ke halaman 1

### TC-GS-POS-131: Unselect All membatalkan seluruh seleksi lintas halaman

10. Centang baris `Account Executive {runId}-023`
11. Klik "Select All (N records)"
12. Klik "Unselect All"
13. Verifikasi Bulk Action Bar tertutup
14. Verifikasi seluruh baris halaman 1 ter-uncheck
15. Pindah ke halaman 2
16. Verifikasi seluruh baris halaman 2 ter-uncheck
17. Kembali ke halaman 1

### TC-GS-POS-132: Uncheck 1 baris dari kondisi 100% terpilih

18. Centang baris `Account Executive {runId}-023`
19. Klik "Select All (N records)"
20. Hapus centang baris `Account Executive {runId}-023`
21. Verifikasi counter menjadi "(N-1) Positions selected" (N dikurangi 1)
22. Verifikasi Bulk Action Bar tetap tampil
23. Verifikasi tombol kembali menjadi "Select All (N records)"
24. Klik icon `✕` pada Bulk Action Bar

### TC-GS-POS-133: Seleksi dipertahankan saat pindah halaman, Search, Filter, dan Sort

25. Centang baris `Account Executive {runId}-023`
26. Ketik Search `UX Researcher {runId}-023`, tekan Enter
27. Centang baris `UX Researcher {runId}-023`
28. Klik `(←)` pada kotak Search
29. Verifikasi counter "2 Positions selected"
30. Verifikasi baris `Account Executive {runId}-023` tercentang
31. Pindah ke halaman 2
32. Kembali ke halaman 1
33. Verifikasi counter tetap "2 Positions selected"
34. Verifikasi baris `Account Executive {runId}-023` tetap tercentang
35. Ketik Search `Analyst`, tekan Enter
36. Verifikasi counter tetap "2 Positions selected"
37. Klik `(←)` pada kotak Search
38. Verifikasi counter tetap "2 Positions selected"
39. Verifikasi baris `Account Executive {runId}-023` tetap tercentang
40. Klik header Name
41. Klik header Name sekali lagi (Z-A)
42. Verifikasi counter tetap "2 Positions selected"
43. Verifikasi baris `UX Researcher {runId}-023` tetap tercentang
44. Klik ikon Filter untuk membuka Filter Panel
45. Pilih rentang Last Updated hari ini
46. Klik `[Apply]`
47. Klik ikon Filter untuk menutup Filter Panel
48. Verifikasi counter tetap "2 Positions selected"
49. Verifikasi baris `UX Researcher {runId}-023` tetap tercentang
50. Klik ikon Filter untuk membuka Filter Panel
51. Klik `[Clear Field]`
52. Klik `[Apply]`
53. Klik ikon Filter untuk menutup Filter Panel
54. Verifikasi counter tetap "2 Positions selected"
55. Verifikasi baris `UX Researcher {runId}-023` tetap tercentang
56. Klik icon `✕` pada Bulk Action Bar
57. Klik menu sidebar Global Settings > User
58. Klik sub-tab Position

### TC-GS-POS-134: Bulk Delete berlaku untuk seluruh seleksi termasuk yang tidak tampil karena filter

59. Ketik Search `Graphic Designer {runId}-023`, tekan Enter
60. Centang baris `Graphic Designer {runId}-023`
61. Ganti isi kotak search dengan `Network Engineer {runId}-023`, tekan Enter
62. Centang baris `Network Engineer {runId}-023`
63. Ganti isi kotak search dengan `Product Designer {runId}-023`, tekan Enter
64. Centang baris `Product Designer {runId}-023`
65. Ganti isi kotak search dengan `Graphic`, tekan Enter
66. Verifikasi counter tetap "3 Positions selected"
67. Buka `Bulk Action` pada Bulk Action Bar
68. Pilih `Delete`
69. Verifikasi Dialog Delete Position memuat bullet `• Graphic Designer {runId}-023`, `• Network Engineer {runId}-023`, `• Product Designer {runId}-023`
70. Klik `[Cancel]`
71. Klik icon `✕` pada Bulk Action Bar
72. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan: 129, 131, 132, 133, 134. TC-GS-POS-134 paling akhir karena membuka dialog Delete; dialog dibatalkan dengan `[Cancel]` (langkah 70) sehingga tidak ada data yang dihapus oleh spec ini.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (menetapkan N dari seeding), langkah 8, 24, 56, 71 (menutup seleksi dengan `✕`), langkah 9 dan 17 (kembali ke halaman 1), langkah 15 (pindah ke halaman 2 untuk memeriksa seleksi di sana), langkah 26, 59, 61, dan 63 (Search agar baris target tampil di halaman aktif), langkah 28 (menutup input Search `UX Researcher` lewat `(←)`), langkah 47 dan 53 (menutup Filter Panel lewat ikon Filter), langkah 57 dan 58 (klik menu sidebar lalu sub-tab Position agar Sort kembali ke default), langkah 70 (menutup dialog Delete Position), dan langkah 72 (menutup input Search lewat `(←)`).
- Filter Panel tetap terbuka sesudah `[Apply]` dan hanya tertutup lewat klik ikon Filter; karena itu langkah 47 dan 53 menutup panel sebelum asersi baris, dan langkah 44 serta 50 membukanya kembali.
- Baris `Network Engineer` dan `Product Designer` pada TC-GS-POS-134 dipilih lewat Search nama lengkap bersuffix karena berada di halaman 2 pada urutan default.
- TC-GS-POS-133 memilih `UX Researcher` lewat Search (langkah 26 sampai 28) karena baris berada di halaman terakhir pada urutan default; pada urutan Z-A baris itu tampil di halaman 1 sehingga dapat diperiksa tercentang pada langkah 43, 49, dan 55. Baris `Account Executive` diperiksa pada langkah di halaman 1 urutan A-Z.
- Spec melewati sekitar 35 langkah (72 langkah). Seluruhnya satu kelas (Bulk Selection pada tabel utama) dengan satu akun dan satu dataset milik spec yang di-seed lewat API; tiap blok TC memulai dari seleksi bersih dan tetap bermakna bila blok lain gagal.
- Temuan untuk QA:
  - TC-GS-POS-129 sampai 134 mencantumkan dependensi TC-GS-POS-123 (populasi data); spec men-seed 15 Position bersuffix `{runId}-023` lewat API.
  - TC-GS-POS-133 langkah 2 ("Pindah ke halaman 2 lalu kembali") mensyaratkan lebih dari satu halaman tanpa menyebut jumlah Position; terpenuhi oleh N = 22. Expected b ("Kedua baris tetap tercentang setiap kali tampil") tidak menyebut baris mana yang tampil di tiap langkah; spec memeriksa baris yang tampil pada halaman aktif (`Account Executive` pada urutan A-Z dan `UX Researcher` pada urutan Z-A).
  - TC-GS-POS-133 langkah 5 ("Apply Filter Last Updated rentang hari ini") tidak menyebut cara memilih rentang; spec memakai rentang hari ini seperti pada TC.
  - TC-GS-POS-132 Expected a menulis "N−1"; spec mengasersi angka N dikurangi 1.
  - TC-GS-POS-134 langkah 2 menyebut Search `Graphic` (hanya 1 tampil); spec mengikuti TC. Asersi spec (counter dan isi dialog) tidak bergantung pada jumlah baris yang tampil.
  - TC-GS-POS-134 tidak menyebut tindak lanjut sesudah dialog Delete Position; spec membatalkannya dengan `[Cancel]` dan tidak menghapus.
