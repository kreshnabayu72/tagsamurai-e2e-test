---
id: TC-FA-CF-E2E-155-konflik-record-dihapus-aktor-lain
title: "Konflik: Field Dihapus Aktor Lain Saat Edit, Delete, Deactivate, atau Activate"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CF-594
  - TC-FA-CF-595
  - TC-FA-CF-596
  - TC-FA-CF-660
coverage:
  web: automated
---

# Konflik: Field Dihapus Aktor Lain Saat Edit, Delete, Deactivate, atau Activate

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor UI sesi 1: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (pengguna Sarah Johnson). Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Akun pelaku sesi 2 (Pre-setup #10 dan #28): Total Control sesi 2 Company Alpha `totalControlSecond_automated_{namaCompany}@qwertysystem.net` (pengguna Rina Putri). Dipakai dua cara: sesi API (login API dengan `Spectra.env.FA_TC2_PASSWORD`, token tidak dihitung sebagai sesi web) untuk menghapus field, dan login UI sesudah semua aksi untuk membaca System Log `Rina Putri` (ganti akun eksplisit di langkah 74 dan 75). Nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup Company Alpha (Pre-setup #11 dan #12): field `Storage Capacity`, `Legacy Tag`, dan `Depreciated Ratio` (Inactive) dihapus oleh sesi API pada spec ini (data bersama). Tidak dapat dimiliki spec karena TC menyebut nama literal field; pemulihan: seed reset Company Alpha (disediakan tim FE/BE) di hook `before` dan `after` serta pada langkah 39 (field `Legacy Tag` dipakai dua TC), efeknya pada field tercatat di sini dan suite berjalan serial (S-06). Nilai data mengacu `Fixture.faCustomFields.baselineGeneral` (fixture disediakan tim FE).
- Data Dinamis: Field Name hasil Edit yang ditolak `Storage Capacity Edit {runId}-155`.
- Kemampuan teknis: sesi API aktor untuk menghapus field (kemampuan disediakan tim BE/FE); kemampuan baca Modal Changelog, Activity Log, System Log `Sarah Johnson`, dan System Log `Rina Putri` dengan Search nama field (TC tidak menyebut path System Log dan Activity Log; disediakan tim FE); baseline jumlah entri tiga surface sesi 1 dicatat sebelum aksi tiap TC (S-12).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun sesi 1 dan sesi 2 dan hook `after` memulihkannya (lihat `suite.md`).
- State global: field Pre-setup dihapus (dipulihkan seed reset). Hook `after` mengembalikan sesi UI ke akun default suite (Total Control Company Alpha). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-594: Edit field yang sudah dihapus aktor lain

1. Catat jumlah entri Modal Changelog, Activity Log, dan System Log `Sarah Johnson` untuk Search `Storage Capacity` sebagai baseline
2. Klik row action `⋯` > `Edit` pada baris `Storage Capacity`
3. Sesi API (Rina Putri) menghapus `Storage Capacity` hingga penghapusan tersimpan
4. Ubah Field Name menjadi `Storage Capacity Edit {runId}-155`
5. Klik `[Save]`
6. Verifikasi toast netral `This custom field is no longer available.` tampil
7. Verifikasi modal Edit tertutup otomatis
8. Verifikasi tabel di-refresh tanpa baris `Storage Capacity`
9. Verifikasi tidak ada error 500
10. Buka Modal Changelog, ketik Search `Storage Capacity`, tekan Enter
11. Verifikasi Modal Changelog memuat entri Delete `Storage Capacity` dari sesi 2
12. Verifikasi jumlah entri Modal Changelog bertambah tepat satu dibanding baseline (tidak ada entri Edit dari Save sesi 1)
13. Tutup Modal Changelog
14. Buka Activity Log, ketik Search `Storage Capacity`, tekan Enter
15. Verifikasi Activity Log memuat entri Delete `Storage Capacity` dari sesi 2
16. Verifikasi jumlah entri Activity Log bertambah tepat satu dibanding baseline (tidak ada entri Edit dari Save sesi 1)
17. Tutup Activity Log
18. Buka System Log `Sarah Johnson`, ketik Search `Storage Capacity`, tekan Enter
19. Verifikasi System Log `Sarah Johnson` tidak memuat entri baru untuk `Storage Capacity` (jumlah entri sama dengan baseline)
20. Tutup System Log `Sarah Johnson`

### TC-FA-CF-595: Delete field yang sudah dihapus aktor lain

21. Catat jumlah entri Modal Changelog, Activity Log, dan System Log `Sarah Johnson` untuk Search `Legacy Tag` sebagai baseline
22. Klik row action `⋯` > `Delete` pada baris `Legacy Tag` sampai dialog Delete tampil
23. Sesi API (Rina Putri) menghapus `Legacy Tag` hingga penghapusan tersimpan
24. Klik `[Delete]` pada dialog
25. Verifikasi toast `This custom field is no longer available.` tampil
26. Verifikasi tabel di-refresh
27. Verifikasi tidak ada error 500
28. Buka Modal Changelog, ketik Search `Legacy Tag`, tekan Enter
29. Verifikasi Modal Changelog memuat entri Delete `Legacy Tag` dari sesi 2
30. Verifikasi jumlah entri Modal Changelog bertambah tepat satu dibanding baseline (tidak ada entri Delete tambahan dari klik sesi 1)
31. Tutup Modal Changelog
32. Buka Activity Log, ketik Search `Legacy Tag`, tekan Enter
33. Verifikasi Activity Log memuat entri Delete `Legacy Tag` dari sesi 2
34. Verifikasi jumlah entri Activity Log bertambah tepat satu dibanding baseline (tidak ada entri Delete tambahan dari klik sesi 1)
35. Tutup Activity Log
36. Buka System Log `Sarah Johnson`, ketik Search `Legacy Tag`, tekan Enter
37. Verifikasi System Log `Sarah Johnson` tidak memuat entri baru untuk `Legacy Tag` (jumlah entri sama dengan baseline)
38. Tutup System Log `Sarah Johnson`
39. Pulihkan Company Alpha ke baseline lewat seed reset sehingga `Legacy Tag` ada kembali, lalu muat ulang Settings > Custom Fields

### TC-FA-CF-596: Deactivate field yang sudah dihapus aktor lain

40. Catat jumlah entri Modal Changelog, Activity Log, dan System Log `Sarah Johnson` untuk Search `Legacy Tag` sebagai baseline
41. Geser switch Active baris `Legacy Tag` ke OFF sampai dialog Deactivate tampil
42. Sesi API (Rina Putri) menghapus `Legacy Tag` hingga penghapusan tersimpan
43. Klik `[Deactivate]` pada dialog
44. Verifikasi toast `This custom field is no longer available.` tampil
45. Verifikasi tabel di-refresh
46. Buka Modal Changelog, ketik Search `Legacy Tag`, tekan Enter
47. Verifikasi Modal Changelog memuat entri Delete `Legacy Tag` dari sesi 2
48. Verifikasi jumlah entri Modal Changelog bertambah tepat satu dibanding baseline (tidak ada entri Deactivate dari klik sesi 1)
49. Tutup Modal Changelog
50. Buka Activity Log, ketik Search `Legacy Tag`, tekan Enter
51. Verifikasi Activity Log memuat entri Delete `Legacy Tag` dari sesi 2
52. Verifikasi jumlah entri Activity Log bertambah tepat satu dibanding baseline (tidak ada entri Deactivate dari klik sesi 1)
53. Tutup Activity Log
54. Buka System Log `Sarah Johnson`, ketik Search `Legacy Tag`, tekan Enter
55. Verifikasi System Log `Sarah Johnson` tidak memuat entri baru untuk `Legacy Tag` (jumlah entri sama dengan baseline)
56. Tutup System Log `Sarah Johnson`

### TC-FA-CF-660: Activate field yang sudah dihapus aktor lain

57. Catat jumlah entri Modal Changelog, Activity Log, dan System Log `Sarah Johnson` untuk Search `Depreciated Ratio` sebagai baseline
58. Geser switch Active baris `Depreciated Ratio` ke ON sampai dialog Activate terbuka
59. Sesi API (Rina Putri) menghapus `Depreciated Ratio` hingga penghapusan tersimpan
60. Klik `[Activate]` pada dialog
61. Verifikasi toast netral `This custom field is no longer available.` tampil
62. Verifikasi tabel di-refresh
63. Buka Modal Changelog, ketik Search `Depreciated Ratio`, tekan Enter
64. Verifikasi Modal Changelog memuat entri Delete `Depreciated Ratio` dari sesi 2
65. Verifikasi jumlah entri Modal Changelog bertambah tepat satu dibanding baseline (tidak ada entri Activate dari klik sesi 1)
66. Tutup Modal Changelog
67. Buka Activity Log, ketik Search `Depreciated Ratio`, tekan Enter
68. Verifikasi Activity Log memuat entri Delete `Depreciated Ratio` dari sesi 2
69. Verifikasi jumlah entri Activity Log bertambah tepat satu dibanding baseline (tidak ada entri Activate dari klik sesi 1)
70. Tutup Activity Log
71. Buka System Log `Sarah Johnson`, ketik Search `Depreciated Ratio`, tekan Enter
72. Verifikasi System Log `Sarah Johnson` tidak memuat entri baru untuk `Depreciated Ratio` (jumlah entri sama dengan baseline)
73. Tutup System Log `Sarah Johnson`

### System Log `Rina Putri` untuk keempat TC

74. Ganti akun: `Logout` dari Total Control Company Alpha (Sarah Johnson)
75. Login sebagai Total Control sesi 2 Company Alpha (Rina Putri) dengan `Spectra.env.FA_TC2_PASSWORD`
76. Buka System Log `Rina Putri`, ketik Search `Storage Capacity`, tekan Enter
77. Verifikasi System Log `Rina Putri` memuat entri Delete `Storage Capacity`
78. Ganti isi kotak search dengan `Legacy Tag`, tekan Enter
79. Verifikasi System Log `Rina Putri` memuat entri Delete `Legacy Tag`
80. Ganti isi kotak search dengan `Depreciated Ratio`, tekan Enter
81. Verifikasi System Log `Rina Putri` memuat entri Delete `Depreciated Ratio`
82. Tutup System Log `Rina Putri`
83. `Logout` dari Total Control sesi 2 Company Alpha (Rina Putri)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini 83 langkah, di atas smell 35 langkah. Alasan: semua blok satu kelas harness (konflik state antar aktor dengan pelaku kedua lewat sesi API), berdiri sendiri, dan 55 langkah adalah blok baca-log berpola dan baseline-nya (buka surface, cari entri, `Verifikasi`) yang tidak dihitung (bagian 3), sehingga sisa 28 langkah.
- Pelaku sesi 2 memicu perubahan state lewat sesi API (bukan konteks kedua kelas c); hasilnya diasersi di sesi UI pertama dan di sesi UI kedua (System Log `Rina Putri`). Langkah pemicu ditulis "... hingga ... tersimpan" (R-20); `P-2` tidak dipakai (keputusan 2026-10-30). Sesi UI kedua dipakai berurutan sesudah semua aksi sesi 1, sehingga satu akun web aktif pada satu waktu.
- P-1: klausa "tidak ada entri dari klik sesi 1" TC-FA-CF-594 sampai 596 dan 660 menempel pada state konflik yang dibangun alur ini (field dihapus sesi 2 saat modal atau dialog sesi 1 terbuka) dan diasersi dengan baseline jumlah entri (S-12, langkah 12, 16, 19, 30, 34, 37, 48, 52, 55, 65, 69, 72); tidak ada spec absence yang memuat aksi nyata untuk TC ini (S-05).
- Perubahan urutan: pulihan baseline pada langkah 39 diperlukan karena `Legacy Tag` dipakai TC-FA-CF-595 dan TC-FA-CF-596 (aksi tanpa `Verifikasi`).
- Langkah penghubung (aksi tanpa `Verifikasi`): baseline (langkah 1, 21, 40, 57), pembukaan, Search, dan penutupan surface log (R-16), langkah 39 (seed reset), langkah 74 dan 75 (ganti akun eksplisit), langkah 83 (logout; hook `after` mengembalikan sesi ke akun default suite).
- Temuan untuk QA:
  - TC-FA-CF-594 sampai 596 dan 660 bertanda Manual Only (dua sesi paralel) tetapi sesi 2 hanya memicu state; spec memakai sesi API (keputusan 2026-10-21 dan 2026-10-30).
  - Cara membuka System Log aktor, System Log `Rina Putri`, dan Activity Log tidak dijelaskan di TC (menu atau jalur navigasi); spec menulisnya persis seperti TC.
  - Ekspektasi "hanya memuat satu entri Delete" pada TC-FA-CF-595 dan 596 tidak dapat berupa angka absolut karena audit trail permanen tumbuh; spec memakai selisih satu terhadap baseline (S-12).
  - TC-FA-CF-595 dan 596 memakai field `Legacy Tag` yang sama tanpa menyebut pemulihan di antaranya; spec menambah langkah penghubung 39.
