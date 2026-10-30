---
id: TC-GS-POS-E2E-052-multi-konteks-edit-dan-delete-antar-admin
title: "Multi-Konteks: Edit Bersamaan Last-Write-Wins serta Record yang Dihapus atau Menjadi In-Use di Antara Dialog dan Konfirmasi (Single dan Bulk)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-POS-109
  - TC-GS-POS-118
  - TC-GS-POS-119
  - TC-GS-POS-147
  - TC-GS-POS-148
  - TC-GS-POS-271
  - TC-GS-POS-300
coverage:
  web: automated
---

# Multi-Konteks: Edit Bersamaan Last-Write-Wins serta Record yang Dihapus atau Menjadi In-Use di Antara Dialog dan Konfirmasi (Single dan Bulk)

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`).
- Akun Sesi A (Admin A): Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`.
- Akun Sesi B (Admin B): Admin B Total Control (Andi Wijaya) `superAdminGlobalSettingsB_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC2_PASSWORD`.
- Dua sesi browser (kelas multi-konteks): Sesi A dan Sesi B berjalan di konteks browser terpisah dengan sesi login sendiri. Keduanya login di hook `before` dan berada di Global Settings > User > Position pada entitas yang sama. Password tidak ditulis di spec atau fixture.
- Data Dinamis (seeding lewat API di hook `before`, bersuffix per run, bebas relasi saat dibuat), sepuluh Position:
  - `Payroll Specialist {runId}-052` (TC-GS-POS-271; nama akhir `Payroll Supervisor {runId}-052`, nama antara `Payroll Officer {runId}-052`).
  - `Finance Analyst {runId}-052` (TC-GS-POS-118; tetap ada).
  - `Audit Trainee {runId}-052` dan `Audit Intern {runId}-052` (TC-GS-POS-300; tetap ada).
  - `Logistics Coordinator {runId}-052` (TC-GS-POS-109; nama `Logistics Lead {runId}-052` tidak pernah tersimpan).
  - `Quality Assurance Analyst {runId}-052` (TC-GS-POS-119).
  - `Sales Representative {runId}-052` dan `Software Tester {runId}-052` (TC-GS-POS-148).
  - `Project Coordinator {runId}-052` dan `Research Analyst {runId}-052` (TC-GS-POS-147; `Research Analyst` tetap ada).
- Data Dinamis user (seeding lewat API di hook `before`): tiga user Login aktif milik tes (Data Dinamis No. 36), `User Uji In-Use {runId}-052` (`Fixture.position.userUjiInUse052`; TC-GS-POS-118 dan TC-GS-POS-147), `User Uji In-Use 1 {runId}-052` (`Fixture.position.userUjiInUse1052`) dan `User Uji In-Use 2 {runId}-052` (`Fixture.position.userUjiInUse2052`) (TC-GS-POS-300), masing-masing dengan Position awal `Warehouse Supervisor` (Pre-setup 12, hanya dirujuk, tidak diubah atau dihapus). Email tiap user unik dan bersuffix `{runId}-052`, dipakai untuk mencari user di User List. Fixture baru; mekanisme seeding user disediakan tim FE/BE (lihat Temuan untuk QA).
- Seluruh Position spec ini memuat suffix `{runId}-052`; Search `{runId}-052` menampilkan paling banyak sepuluh baris sehingga muat satu halaman (ukuran halaman default 10).
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-position` untuk akun aktor spec ini (Sesi A dan Sesi B) dan hook `after` memulihkannya; lihat `suite.md`.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): hapus lewat API tiga user spec ini lebih dulu, lalu semua Position bersuffix `{runId}-052` yang masih ada (termasuk nama hasil perubahan); tutup konteks Sesi B; kembalikan sesi ke akun default suite.
- Hook `beforeEach`: tutup dialog atau modal yang terbuka di kedua sesi lalu kembali ke Global Settings > User > Position; layar awal dibuka di hook ini sehingga `## Test Steps` tidak mengulang langkah buka.
- Kemampuan teknis: dua konteks browser paralel dalam satu spec; dialog `beforeunload` ditangani otomatis saat memuat ulang (langkah 59); langkah dijalankan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]`.
- State global yang diubah: tidak ada selain Position dan user milik spec.

## Test Steps

### TC-GS-POS-271: Edit bersamaan record yang sama, last-write-wins

1. [Sesi A] Ketik `{runId}-052` pada Search tabel lalu tekan Enter
2. [Sesi B] Ketik `{runId}-052` pada Search tabel lalu tekan Enter
3. [Sesi A] Klik `⋯` pada baris `Payroll Specialist {runId}-052`, pilih `Edit`
4. [Sesi B] Klik `⋯` pada baris `Payroll Specialist {runId}-052`, pilih `Edit`
5. [Sesi A] Ganti isi field Position Name menjadi `Payroll Officer {runId}-052`
6. [Sesi A] Klik `[Save]`
7. [Sesi A] Verifikasi toast sukses: "Success, position has been updated."
8. [Sesi A] Verifikasi tidak ada dialog konflik
9. [Sesi B] Ganti isi field Position Name menjadi `Payroll Supervisor {runId}-052`
10. [Sesi B] Klik `[Save]`
11. [Sesi B] Verifikasi toast sukses: "Success, position has been updated."
12. [Sesi B] Verifikasi tidak ada dialog konflik
13. [Sesi B] Verifikasi tabel menampilkan baris `Payroll Supervisor {runId}-052` sebagai nilai akhir

### TC-GS-POS-118: Delete single, jabatan menjadi in-use di antara buka dialog dan Confirm

14. [Sesi A] Klik `⋯` pada baris `Finance Analyst {runId}-052`, pilih `Delete`
15. [Sesi A] Verifikasi Dialog Delete Position tampil
16. [Sesi B] Buka Global Settings > User > User List lalu ketik Search email user `User Uji In-Use {runId}-052` (email bersuffix `{runId}-052`), tekan Enter
17. [Sesi B] Klik `⋯` pada baris user tersebut, pilih `Edit`
18. [Sesi B] Ubah Position menjadi `Finance Analyst {runId}-052`
19. [Sesi B] Klik `[Save]` pada form Edit User
20. [Sesi B] Tunggu hingga penyimpanan selesai (toast sukses tampil)
21. [Sesi A] Klik `[Delete]` pada Dialog Delete Position
22. [Sesi A] Verifikasi dialog "Cannot Delete Data" tampil dengan `• Finance Analyst {runId}-052`
23. [Sesi A] Verifikasi tidak ada toast sukses maupun toast tambahan
24. [Sesi A] Klik `[OK]`

### TC-GS-POS-300: Bulk Delete, seluruh item menjadi in-use di antara buka dialog dan Confirm

25. [Sesi A] Centang baris `Audit Trainee {runId}-052`
26. [Sesi A] Centang baris `Audit Intern {runId}-052`
27. [Sesi A] Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
28. [Sesi A] Verifikasi Dialog Delete Position tampil
29. [Sesi B] Buka Global Settings > User > User List lalu ketik Search email user `User Uji In-Use 1 {runId}-052` (email bersuffix `{runId}-052`), tekan Enter
30. [Sesi B] Klik `⋯` pada baris user tersebut, pilih `Edit`
31. [Sesi B] Ubah Position menjadi `Audit Trainee {runId}-052`
32. [Sesi B] Klik `[Save]` pada form Edit User
33. [Sesi B] Tunggu hingga penyimpanan selesai (toast sukses tampil)
34. [Sesi B] Ganti isi kotak search dengan email user `User Uji In-Use 2 {runId}-052` (email bersuffix `{runId}-052`), tekan Enter, klik `⋯` pada baris user tersebut, pilih `Edit`
35. [Sesi B] Ubah Position menjadi `Audit Intern {runId}-052`
36. [Sesi B] Klik `[Save]` pada form Edit User
37. [Sesi B] Tunggu hingga penyimpanan selesai (toast sukses tampil)
38. [Sesi B] Buka Global Settings > User > Position lalu ketik `{runId}-052` pada Search tabel dan tekan Enter
39. [Sesi A] Klik `[Delete]` pada Dialog Delete Position
40. [Sesi A] Verifikasi dialog "Cannot Delete Data" tampil dengan `• Audit Trainee {runId}-052` dan `• Audit Intern {runId}-052`
41. [Sesi A] Verifikasi dialog menampilkan teks "These positions are still in use. Remove the references before deleting."
42. [Sesi A] Verifikasi dialog menampilkan tombol `[OK]`
43. [Sesi A] Verifikasi tidak ada toast sukses maupun toast "Some items were skipped"
44. [Sesi A] Klik `[OK]`
45. [Sesi A] Verifikasi baris `Audit Trainee {runId}-052` dan `Audit Intern {runId}-052` tetap ada di tabel
46. [Sesi A] Verifikasi kedua baris tetap tercentang
47. [Sesi A] Verifikasi counter Bulk Action Bar menampilkan "2 Positions selected"
48. [Sesi A] Klik `[✕]` pada Bulk Action Bar untuk mengosongkan seleksi

### TC-GS-POS-109: Edit, record sudah dihapus admin lain saat Save

49. [Sesi A] Klik `⋯` pada baris `Logistics Coordinator {runId}-052`, pilih `Edit`
50. [Sesi A] Verifikasi Popup Edit Position terbuka
51. [Sesi A] Ganti isi field Position Name menjadi `Logistics Lead {runId}-052`
52. [Sesi B] Klik `⋯` pada baris `Logistics Coordinator {runId}-052`, pilih `Delete`
53. [Sesi B] Klik `[Delete]` pada Dialog Delete Position
54. [Sesi B] Tunggu hingga Delete selesai (toast sukses tampil)
55. [Sesi A] Klik `[Save]`
56. [Sesi A] Verifikasi toast netral: "This position is no longer available."
57. [Sesi A] Verifikasi baris `Logistics Coordinator {runId}-052` tidak tampil di tabel setelah daftar di-refresh otomatis tanpa memuat ulang halaman
58. [Sesi A] Verifikasi tidak ada baris `Logistics Lead {runId}-052`
59. [Sesi A] Muat ulang halaman Position (dialog `beforeunload` ditangani) lalu ketik `{runId}-052` pada Search tabel dan tekan Enter

### TC-GS-POS-119: Delete single, record sudah dihapus admin lain sebelum Confirm

60. [Sesi A] Klik `⋯` pada baris `Quality Assurance Analyst {runId}-052`, pilih `Delete`
61. [Sesi B] Klik `⋯` pada baris `Quality Assurance Analyst {runId}-052`, pilih `Delete`
62. [Sesi B] Klik `[Delete]` pada Dialog Delete Position
63. [Sesi B] Tunggu hingga Delete selesai (toast sukses tampil)
64. [Sesi A] Klik `[Delete]` pada Dialog Delete Position
65. [Sesi A] Verifikasi tidak ada toast error maupun dialog error
66. [Sesi A] Verifikasi Dialog Delete Position tertutup
67. [Sesi A] Verifikasi baris `Finance Analyst {runId}-052` tampil di tabel
68. [Sesi A] Verifikasi baris `Quality Assurance Analyst {runId}-052` tidak tampil di tabel setelah daftar di-refresh

### TC-GS-POS-148: Bulk Delete, item sudah dihapus admin lain sebelum Confirm

69. [Sesi A] Centang baris `Sales Representative {runId}-052`
70. [Sesi A] Centang baris `Software Tester {runId}-052`
71. [Sesi A] Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
72. [Sesi B] Klik `⋯` pada baris `Software Tester {runId}-052`, pilih `Delete`
73. [Sesi B] Klik `[Delete]` pada Dialog Delete Position
74. [Sesi B] Tunggu hingga Delete selesai (toast sukses tampil)
75. [Sesi A] Klik `[Delete]` pada dialog Delete Position
76. [Sesi A] Verifikasi toast sukses: "Success, position has been deleted."
77. [Sesi A] Verifikasi toast tidak memuat "Some items were skipped"
78. [Sesi A] Verifikasi baris `Sales Representative {runId}-052` dan `Software Tester {runId}-052` tidak tampil di tabel
79. [Sesi A] Verifikasi Bulk Action Bar hilang

### TC-GS-POS-147: Bulk Delete, item menjadi in-use di antara buka dialog dan Confirm

80. [Sesi A] Centang baris `Project Coordinator {runId}-052`
81. [Sesi A] Centang baris `Research Analyst {runId}-052`
82. [Sesi A] Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
83. [Sesi A] Verifikasi Dialog Delete Position tampil
84. [Sesi B] Buka Global Settings > User > User List lalu ketik Search email user `User Uji In-Use {runId}-052` (email bersuffix `{runId}-052`), tekan Enter
85. [Sesi B] Klik `⋯` pada baris user tersebut, pilih `Edit`
86. [Sesi B] Ubah Position menjadi `Research Analyst {runId}-052`
87. [Sesi B] Klik `[Save]` pada form Edit User
88. [Sesi B] Tunggu hingga penyimpanan selesai (toast sukses tampil)
89. [Sesi A] Klik `[Delete]` pada Dialog Delete Position
90. [Sesi A] Verifikasi toast sukses: "Success, position has been deleted. Some items were skipped."
91. [Sesi A] Verifikasi baris `Project Coordinator {runId}-052` tidak tampil di tabel
92. [Sesi A] Verifikasi baris `Research Analyst {runId}-052` tetap ada di tabel
93. [Sesi A] Verifikasi tidak ada error crash batch (tidak ada toast error maupun dialog error)

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`. Kelas harness: multi-konteks (dua sesi admin), bagian 3 prinsip 13c. Spec serial.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Alasan spec memuat 93 langkah (di atas smell sekitar 35 langkah): seluruh blok satu kelas harness (dua sesi admin pada entitas yang sama), tiap blok memakai Position bersuffix sendiri yang di-seed di hook `before` sehingga blok berdiri sendiri, dan kegagalan satu blok tidak menghilangkan makna blok lain; jumlah langkah muncul dari satu baris per aksi per sesi dan satu `Verifikasi` per klausa Expected.
- Urutan TC: TC-GS-POS-271 (edit tanpa penghapusan), TC-GS-POS-118 dan TC-GS-POS-300 (penghapusan diblokir, tidak ada record terhapus) lebih dulu; TC-GS-POS-109, TC-GS-POS-119, TC-GS-POS-148, TC-GS-POS-147 (aksi yang menghapus data) paling akhir (prinsip 5). TC-GS-POS-147 paling akhir karena seleksi `Research Analyst` tidak dikosongkan setelahnya (PRD §8 mereset seleksi setelah aksi, tidak diasersi). Urutan ini berbeda dari urutan nomor TC sumber.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 2 (Search `{runId}-052` supaya sepuluh Position spec ini muat satu halaman); langkah 16 sampai 20, 29 sampai 38, 84 sampai 88 (Sesi B mengubah Position user lewat form Edit User, serta langkah 38 yang mengembalikan Sesi B ke tab Position); langkah 24 dan 44 (menutup dialog `Cannot Delete Data` dengan `[OK]`); langkah 48 (mengosongkan seleksi); langkah 54, 63, dan 74 (menunggu Delete Sesi B selesai); langkah 59 (memuat ulang Sesi A sesudah asersi TC-GS-POS-109 supaya state Popup Edit Sesi A, yang tidak didefinisikan TC sesudah toast netral, tidak memengaruhi TC berikutnya).
- Langkah 15, 28, 50, dan 83 (`Verifikasi` dialog atau popup tampil) memastikan keadaan sebelum Sesi B bertindak, mengikuti panah "→" di langkah TC-GS-POS-109, TC-GS-POS-118, dan keterangan "(Dialog Delete Position)" di TC-GS-POS-147 dan TC-GS-POS-300.
- Langkah 57 dan 58 membaca tabel Sesi A tanpa memuat ulang halaman, sesuai TC-GS-POS-109 butir b ("di-refresh otomatis (tanpa reload manual)"). Frasa "di-refresh otomatis" teramati lewat hilangnya baris `Logistics Coordinator {runId}-052` dari tabel dan tidak punya observasi terpisah. Spec tidak menutup Popup Edit karena state-nya sesudah toast netral tidak didefinisikan TC.
- Asersi "tidak ada entri log" TC-GS-POS-109 dan TC-GS-POS-119 tidak ditulis di spec ini karena berada di Post Condition tanpa langkah observasi (lihat Temuan untuk QA).
- Langkah 56 (toast netral "This position is no longer available.") menjadi anchor absence baris untuk langkah 57 dan 58 (butir 2 konvensi 8b).
- Langkah 67 (`Verifikasi` baris `Finance Analyst {runId}-052` tampil) adalah asersi tambahan di luar Expected TC-GS-POS-119 dan berfungsi sebagai anchor pembanding: TC-GS-POS-119 tidak punya toast sukses sebagai sinyal bahwa daftar sudah di-refresh, sehingga langkah 68 (baris `Quality Assurance Analyst {runId}-052` tidak tampil) didahului bukti bahwa tabel Sesi A sudah termuat dengan Search `{runId}-052` (S-03, butir 2 konvensi 8b). Dialog tertutup (langkah 66) bukan bukti tabel termuat.
- Temuan untuk QA:
  - TC-GS-POS-109, 118, 119, 147, 148, 271, dan 300 memuat Post Condition tentang Changelog dan Activity Log ("tidak ada entri Edit", "Changelog mencatat 2 entri Edit terpisah", "1 entri Delete untuk Sales Representative", dan sejenisnya) tanpa langkah observasi di TC; tidak diasersi.
  - TC-GS-POS-118, 147, dan 300 memakai user milik tes `User Uji In-Use` (TC-GS-POS-300: `User Uji In-Use 1` dan `User Uji In-Use 2`; Data Dinamis No. 36) sebagai pihak yang Position-nya diubah Admin B; spec memakai versi bersuffix `{runId}-052`. Mekanisme seeding user tidak didefinisikan di TC, PRD, atau LLD sehingga ditulis sebagai kemampuan tim FE/BE.
  - TC-GS-POS-118 memakai `Finance Analyst` (Pre-setup 11) dan TC-GS-POS-119 memakai `Quality Assurance Analyst` (Data Dinamis 4 sampai 13); spec memakai versi bersuffix milik spec karena Position diubah atau dihapus.
  - TC-GS-POS-109 tidak mendefinisikan state Popup Edit Position Sesi A sesudah toast netral (tertutup atau tetap terbuka); asersi tabel di langkah 57 dan 58 membaca daftar tanpa menutup popup dan reload di langkah 59 hanya penghubung. Perlu dilengkapi TC agar state popup teramati.
  - TC-GS-POS-300 butir c mensyaratkan seleksi tetap tercentang dengan counter "2 Positions selected"; PRD EC-14 menyatakan seleksi dipertahankan sehingga konsisten.
  - TC-GS-POS-118 butir a tidak menyebut body dialog; spec hanya mengasersi bullet `• Finance Analyst {runId}-052` sesuai TC.
  - Sesi Admin B pada blok TC-GS-POS-118, 300, 109, 119, 148, dan 147 memakai sesi UI mengikuti TC, padahal hanya memicu state; konvensi P-2 meminta pelaku kedua semacam itu memakai sesi API (sesi UI hanya bila hasilnya diasersi, seperti TC-GS-POS-271). Perlu konfirmasi QA sebelum langkah itu dipindah ke sesi API yang disediakan tim FE/BE.
  - Toast sukses form Edit User pada langkah 20, 33, 37, dan 88 tidak didefinisikan di TC Position; hanya dinyatakan "toast sukses tampil" sebagai langkah penghubung.
