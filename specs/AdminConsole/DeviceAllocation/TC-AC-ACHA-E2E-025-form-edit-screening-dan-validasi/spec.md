---
id: TC-AC-ACHA-E2E-025-form-edit-screening-dan-validasi
title: "Form Edit Allocation: Screening, Field Terkunci, Validasi Quantity dan Notes, Save Disabled, dan Notes Di-trim"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-182
  - TC-AC-ACHA-183
  - TC-AC-ACHA-184
  - TC-AC-ACHA-185
  - TC-AC-ACHA-186
  - TC-AC-ACHA-187
  - TC-AC-ACHA-188
  - TC-AC-ACHA-189
  - TC-AC-ACHA-190
  - TC-AC-ACHA-191
  - TC-AC-ACHA-192
  - TC-AC-ACHA-193
  - TC-AC-ACHA-194
  - TC-AC-ACHA-195
coverage:
  web: automated
---

# Form Edit Allocation: Screening, Field Terkunci, Validasi Quantity dan Notes, Save Disabled, dan Notes Di-trim

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Group Member Distributor toggle ON (MB_ON, Pre-setup #32) `memberOnDistributor_automated_qaTeam1@qwertysystem.net`, nama pengguna Budi Santoso (PIC pada Allocation Log = Budi Santoso), password `Spectra.env.AC_DA_MB_ON_PASSWORD`. Login di hook `before` spec ini; halaman Allocation > Device Allocation dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun di tengah spec: Group Member Partner CV Karya Mandiri toggle ON (MB_P2, Pre-setup #47) `memberOnPartner2_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_MB_P2_PASSWORD`; Group Member Principal toggle ON (MB_PRIN, Pre-setup #24) `memberOnPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_MB_PRIN_PASSWORD`. Nama env var didaftarkan di `spectra.config.ts` dan `.env.example` oleh tahap script.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor, flag Guided Tooltip `guided_tooltip_seen_<page_key>` true untuk akun aktor, fixture API Pre-setup #20, dan pemulihan preferensi Setup Column di hook `after`.
- Data milik spec (dibuat di hook `before` lewat fixture seeding "disediakan tim FE/BE", dibersihkan di hook `after`): satu transaksi Waiting for Approval dibuat MB_ON yang mereplikasi Pre-setup #49 (RFID Object TAG, Quantity 100, Client PT Sejahtera Logistik, Pay From `PT ABC (Principal)`, Notes `Batch uji`, Total Cost $250.00, Reserve $250.00 pada kantong PT Global Distribusi saldo $20,000.00). Allocation ID dibaca saat seeding (Dynamic Reference) dan dipakai sebagai kata kunci Search; Notes `Batch uji` literal karena diasersi TC (pengecualian nama literal S-12, Lampiran A butir A-11).
- Data Pre-setup yang dibaca saja (tanpa Save): transaksi Pre-setup #50 (MB_P2; kantong A saldo $1,000.00 Reserved $60.00 dan kantong B saldo $3,000.00, Pre-setup #18 dan #19) dan transaksi Pre-setup #51 (MB_PRIN). Allocation ID transaksi #50 dan #51 tidak ditulis literal: dibaca lewat kemampuan baca fixture API Pre-setup #20 (disediakan tim FE/BE) sebagai Dynamic Reference dan dipakai sebagai kata kunci Search pada langkah 79 (#50) dan langkah 87 (#51).
- Kemampuan teknis: (1) fixture API penyetel saldo kantong dan pemulih ke keadaan awal (Pre-setup #20); (2) kemampuan menempel 361 dan 360 karakter pada Notes dan menempel teks ke input; (3) saldo kantong PT Global Distribusi disetel $5,000,000.00 hanya pada blok TC-AC-ACHA-189 dan dipulihkan ke $20,000.00 dengan Reserved $250.00 pada akhir blok (dan di hook `after`).
- State global: saldo kantong PT Global Distribusi (diubah pada blok TC-AC-ACHA-189, dipulihkan); suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `AC_DA_MB_ON_PASSWORD`, `AC_DA_MB_P2_PASSWORD`, `AC_DA_MB_PRIN_PASSWORD` (satu nama satu arti).

## Test Steps

### TC-AC-ACHA-182: Screening form Edit Allocation transaksi Distributor

1. Ketik Search Allocation ID transaksi milik spec, tekan Enter
2. Buka menu row action `⋯` transaksi itu, klik `Edit`
3. Verifikasi header form: judul `Edit Allocation` dan ikon close `[×]` tampil
4. Verifikasi From: label read-only `PT Global Distribusi (Distributor)`
5. Verifikasi Category `RFID`, Type `Object TAG`, dan Client `PT Sejahtera Logistik` tampil read-only (tidak bisa diubah)
6. Verifikasi Quantity `100` pre-filled dan dapat diubah
7. Verifikasi Pay From `PT ABC (Principal)` pre-filled dan disabled (satu kantong sumber)
8. Verifikasi Notes `Batch uji` pre-filled dan dapat diubah
9. Verifikasi Preview tiga baris: `Unit Price (Snapshot)` `$2.50/unit`, `Estimated Cost` `$250.00 (100 × $2.50/unit)`, dan `Your Pocket Balance` `$20,000.00`
10. Verifikasi footer: `[Clear Field]` dan `[Save]` (filled, success) tampil
11. Verifikasi `[Save]` disabled karena belum ada perubahan
12. Verifikasi tidak ada `[Cancel]` dan tidak ada checkbox "Stay on this form after submitting"

### TC-AC-ACHA-185: Category, Type, dan Client terkunci pada Edit

13. Klik field Category
14. Verifikasi dropdown Category tidak terbuka dan nilai tetap `RFID`
15. Klik field Type
16. Verifikasi dropdown Type tidak terbuka dan nilai tetap `Object TAG`
17. Klik field Client
18. Verifikasi dropdown Client tidak terbuka dan nilai tetap `PT Sejahtera Logistik`
19. Coba mengubah isi Category, Type, dan Client lewat keyboard
20. Verifikasi nilai Category `RFID`, Type `Object TAG`, dan Client `PT Sejahtera Logistik` tidak berganti
21. Verifikasi hanya Quantity dan Notes yang dapat diubah pada form ini
22. Verifikasi Pay From tetap disabled (pengirim Distributor hanya punya satu kantong sumber)

### TC-AC-ACHA-186: Quantity dikosongkan dievaluasi saat klik Save

23. Kosongkan Quantity
24. Verifikasi `[Save]` tidak disabled oleh Quantity yang kosong
25. Klik `[Save]`
26. Verifikasi pesan "Quantity must not be empty" tampil

### TC-AC-ACHA-187: Quantity 0 ditolak real-time pada Edit

27. Isi Quantity `0`
28. Verifikasi pesan real-time "Quantity must be a positive whole number" tampil
29. Verifikasi `[Save]` disabled
30. Verifikasi Preview tidak dirender

### TC-AC-ACHA-188: Quantity di atas 1.000.000 ditolak pada Edit

31. Isi Quantity `1000001`
32. Verifikasi pesan real-time "Quantity must not exceed 1,000,000" tampil
33. Verifikasi `[Save]` disabled

### TC-AC-ACHA-190: Quantity lebih dari 15 digit pada Edit

34. Isi Quantity `1000000000000000` (16 digit)
35. Verifikasi pesan real-time "Max. 15 characters" tampil
36. Verifikasi `[Save]` disabled

### TC-AC-ACHA-191: Input Quantity pada Edit hanya menerima digit

37. Kosongkan Quantity lalu ketik `1-2.5e`
38. Verifikasi nilai Quantity menjadi `125` (ketikan non-digit diblokir)
39. Kosongkan Quantity lalu tempel `12abc3`
40. Verifikasi nilai Quantity menjadi `123` (nilai tempel dibersihkan)

### TC-AC-ACHA-192: Notes 361 karakter ditolak pada Edit

41. Isi Notes dengan 361 karakter
42. Verifikasi pesan real-time "Max. 360 characters" tampil di bawah Notes
43. Verifikasi `[Save]` disabled

### TC-AC-ACHA-193: Notes 360 karakter diterima pada Edit

44. Isi Notes dengan 360 karakter
45. Verifikasi tidak ada pesan error
46. Verifikasi `[Save]` enabled
47. Klik `[×]`
48. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
49. Klik `[Leave]`
50. Verifikasi baris transaksi di List menampilkan Quantity `100` (data transaksi tidak berubah oleh submit yang diblokir pada TC-AC-ACHA-186)

### TC-AC-ACHA-189: Batas atas Quantity diterima pada Edit

51. Setel saldo kantong PT Global Distribusi menjadi $5,000,000.00 lewat fixture hingga tersimpan
52. Buka menu row action `⋯` transaksi itu, klik `Edit`
53. Isi Quantity `1000000`
54. Verifikasi tidak ada pesan error Quantity (nilai tepat 1.000.000 diterima)
55. Verifikasi `[Save]` enabled
56. Klik `[×]`
57. Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
58. Klik `[Leave]`
59. Pulihkan saldo kantong PT Global Distribusi menjadi $20,000.00 dengan Reserved $250.00 lewat fixture hingga tersimpan

### TC-AC-ACHA-195: Save disabled sampai ada perubahan nilai (kapitalisasi dan spasi tepi bukan perubahan)

60. Buka menu row action `⋯` transaksi itu, klik `Edit`
61. Verifikasi `[Save]` disabled saat form dibuka tanpa perubahan
62. Ubah Quantity menjadi `101`
63. Verifikasi `[Save]` enabled setelah Quantity berubah
64. Ubah Quantity menjadi `100`
65. Verifikasi `[Save]` kembali disabled setelah nilai dikembalikan identik dengan nilai tersimpan
66. Arahkan kursor ke `[Save]` yang disabled
67. Verifikasi tidak ada tooltip pada `[Save]` yang disabled karena belum ada perubahan
68. Ubah Notes dari `Batch uji` menjadi `BATCH UJI`
69. Verifikasi `[Save]` tetap disabled (hanya kapitalisasi yang berubah)
70. Ubah Notes menjadi `  Batch uji  ` (dua spasi di awal dan akhir)
71. Verifikasi `[Save]` tetap disabled (hanya spasi tepi yang berubah)

### TC-AC-ACHA-194: Notes di-trim saat disimpan pada Edit

72. Ubah Notes menjadi `  Revisi catatan  ` (dua spasi di awal dan akhir)
73. Klik `[Save]`
74. Tunggu form Edit tertutup
75. Buka menu row action `⋯` transaksi itu, klik `Allocation Log`
76. Verifikasi entri `Allocation edited by [PIC]` memuat `Notes: Revisi catatan` tanpa spasi tepi
77. Tutup modal Allocation Log

### TC-AC-ACHA-183: Screening form Edit Partner dua kantong: Pay From dapat diubah

78. Ganti akun: Logout, login sebagai MB_P2 (Pre-setup #47), buka Allocation > Device Allocation
79. Ketik Search Allocation ID transaksi Pre-setup #50, tekan Enter
80. Buka menu row action `⋯` transaksi itu, klik `Edit`
81. Verifikasi Pay From dropdown dapat diubah dan terisi `PT Global Distribusi (Distributor)`
82. Verifikasi Category `NFC`, Type tidak ada, dan Client `PT Cipta Kreasi` read-only
83. Verifikasi Quantity `40`
84. Verifikasi Preview: `Unit Price (Snapshot)` `$1.50/unit`, `Estimated Cost` `$60.00 (40 × $1.50/unit)`, dan `Your Pocket Balance` `$1,000.00`
85. Klik `[×]` (form belum diubah sehingga langsung tertutup)

### TC-AC-ACHA-184: Screening form Edit Principal tanpa Pay From dan Preview

86. Ganti akun: Logout, login sebagai MB_PRIN (Pre-setup #24), buka Allocation > Device Allocation
87. Ketik Search Allocation ID transaksi Pre-setup #51, tekan Enter
88. Buka menu row action `⋯` transaksi itu, klik `Edit`
89. Verifikasi tidak ada field Pay From
90. Verifikasi tidak ada Preview
91. Verifikasi Category `Handheld Reader`, Type `Long Range`, dan Client `PT Manufaktur Unggul` read-only
92. Verifikasi Quantity `10` dan Notes dapat diubah
93. Klik `[×]` (form belum diubah sehingga langsung tertutup)

## Notes

- Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan TC (S-05, S-10): blok TC-AC-ACHA-183 dan TC-AC-ACHA-184 ada di akhir karena butuh ganti akun (dua kali); blok TC-AC-ACHA-195 dan TC-AC-ACHA-194 dijalankan sesudah semua validasi tanpa submit, dan TC-AC-ACHA-189 dipisah dari TC-AC-ACHA-186 s.d. 193 karena butuh saldo kantong $5,000,000.00 yang tidak boleh mengubah nilai `Your Pocket Balance` `$20,000.00` pada TC-AC-ACHA-182. TC-AC-ACHA-186 s.d. 193 memakai satu pembukaan form dengan field diganti nilainya di antara kasus (prinsip 8, "halaman yang sama dipakai berulang"); form ditutup dirty lewat `[×]`, dialog `Unsaved Changes`, `[Leave]` (S-08), sehingga langkah 48 dan 57 adalah `Verifikasi` yang diwajibkan S-08. Blok TC-AC-ACHA-194 melanjutkan form dari TC-AC-ACHA-195 (Quantity `100` dan Notes ternormalisasi identik dengan nilai tersimpan) tanpa membuka ulang.
- Langkah penghubung (S-03, R-16): langkah 1, 79, 87 (Search Allocation ID untuk menemukan baris target); langkah 13, 15, 17, 19 hanyalah aksi pemicu bagi `Verifikasi` TC-AC-ACHA-185; langkah 47, 49, 56, 58 (menutup form dirty); langkah 51 dan 59 (pengaturan dan pemulihan saldo kantong); langkah 74 (menunggu form tertutup); langkah 77 (menutup modal Allocation Log); langkah 78 dan 86 (ganti akun); langkah 85 dan 93 (menutup form yang belum diubah).
- Spec ini melewati sekitar 35 langkah. Alasan: seluruhnya satu topik (form Edit Allocation, satu dataset transaksi milik spec, tanpa submit sukses kecuali blok terakhir MB_ON) dengan `Verifikasi` dipecah per klausa (S-01); validasi TC-AC-ACHA-186 s.d. 193 berbagi satu pembukaan form dan memecahnya hanya menambah login, hook, dan seeding. Blok ganti akun (langkah 78 s.d. 93) tetap bermakna walau blok MB_ON gagal keras.
- Pengecualian S-12: Notes `Batch uji` dan nama entitas Pre-setup bernilai literal karena diasersi TC (Lampiran A butir A-11).
- Langkah 21 mengikuti TC-185 butir b: Pay From disabled karena pengirim Distributor hanya punya satu kantong sumber; varian Pay From dapat diubah untuk Partner dua kantong berada di luar TC-185 dan diuji TC-183 (langkah 81). `Verifikasi` Pay From disabled dipisah dari `Verifikasi` Quantity dan Notes (S-01).
- Temuan untuk QA:
  - Kontrak fixture seeding transaksi milik spec, baca Reserved atau saldo kantong, dan pemulih saldo (Pre-setup #20) tidak tertulis di TC, PRD, atau LLD; ditulis "disediakan tim FE/BE" (R-19, S-13).
  - TC-AC-ACHA-190: Expected hanya "Max. 15 characters" dan `[Save]` disabled, padahal 16 digit juga melewati batas 1.000.000 (TC-AC-ACHA-188); TC tidak menyatakan apakah pesan "Quantity must not exceed 1,000,000" ikut tampil. Spec hanya mengasersi pesan yang disebut TC.
  - TC-AC-ACHA-186 Expected b ("data transaksi tidak berubah") tidak punya langkah observasi di TC; spec mengasersinya lewat baris List (Quantity `100`) sesudah form ditutup.
  - TC-AC-ACHA-189: nilai uji `1000000` pada harga $2.50 menghasilkan biaya $2,500,000.00, sehingga TC menyetel saldo $5,000,000.00; TC tidak menyatakan efeknya pada `Your Pocket Balance` di Preview, jadi tidak diasersi.
  - TC-AC-ACHA-194 Post Condition ("Approvals Active Tab (data subject terbaru); Wallet tidak berubah") dan Post Condition TC lain yang tanpa langkah observasi: tidak diasersi.
