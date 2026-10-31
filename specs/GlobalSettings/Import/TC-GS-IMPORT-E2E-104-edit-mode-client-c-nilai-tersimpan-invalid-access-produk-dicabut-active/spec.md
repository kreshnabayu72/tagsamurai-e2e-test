---
id: TC-GS-IMPORT-E2E-104-edit-mode-client-c-nilai-tersimpan-invalid-access-produk-dicabut-active
title: "Edit Mode Client C: nilai tersimpan Invalid (Access produk dicabut, Active Period lampau, opsi Shift), keyboard Select, tombol Create Missing Options Disabled"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-894
  - TC-GS-IMPORT-896
  - TC-GS-IMPORT-904
  - TC-GS-IMPORT-905
  - TC-GS-IMPORT-906
coverage:
  web: automated
---

# Edit Mode Client C: nilai tersimpan Invalid (Access produk dicabut, Active Period lampau, opsi Shift), keyboard Select, tombol Create Missing Options Disabled

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena spec mengubah produk organisasi dan opsi Custom Field `Shift` Client C serta draft Import dibagikan ke seluruh admin satu client (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTC_TC_PASSWORD`.
- Pelaku kedua (hanya memicu penambahan opsi, tanpa asersi UI di sesinya, P-2): Admin kedua Client C (Oki Setiawan) `totalControlSecond_automated_qaTeam3@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTC_TC2_PASSWORD` (nama env baru); klien HTTP disediakan tim FE/BE. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > User Login untuk Client C.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Pre-setup Client C: produk organisasi Global Settings dan Fixed Asset; Custom Field `Shift` (Dropdown) Active dengan opsi `Pagi`, `Siang`, `Malam` (`Lembur` dan `Piket` belum menjadi opsi); Division `Engineering`.
- Data Dinamis (berkas fixture uji; nilai literal karena asersi bergantung pada isi; draft dibuat ulang sebelum tiap blok dan dibuang sesudahnya, Kontrak Fixture R1 dan R2):
  - D-79 `user-login-shift-lembur.csv`: header `First Name,Last Name,Email,Division,Position,Access,Shift`; #1 Siti Rahmawati (`siti.rahmawati@example.com`) Shift `Lembur`; #2 Budi Santoso (`budi.santoso@example.com`) Shift `lembur ` (huruf kecil dengan spasi di akhir); #3 Andi Pratama (`andi.pratama@example.com`) Shift `Siang`; Division `Engineering`, Position kosong, Access `Global Settings`. Hasil staging: #1 dan #2 `error` (opsi tidak ditemukan), #3 `pending`. Dibuat lewat UI (unggah) pada TC-905 dan TC-904.
  - D-88 `user-login-access-fa.csv`: header `First Name,Last Name,Email,Division,Position,Access`; #1 Siti Rahmawati Access `Global Settings;Fixed Asset`; #2 Budi Santoso Access `Global Settings`; Division `Engineering`, Position kosong. Sesudah draft dibuat, produk `Fixed Asset` dicabut dari organisasi Client C lewat fixture Admin Console (disediakan tim FE) sehingga #1 `error`; produk dipulihkan sesudah blok.
  - D-89 `user-login-active-period.csv`: header `First Name,Last Name,Email,Division,Position,Access,Active Period`; #1 Siti Rahmawati Active Period tanggal dua hari dari hari uji, #2 Budi Santoso kosong; Division `Engineering`, Position kosong, Access `Global Settings`. Sesudah draft dibuat, Active Period #1 dimundurkan ke kemarin lewat fixture Active Period baris staging (NC-08) sehingga #1 `error` dengan pesan "Please select a future date.". Tanggal "besok" dihitung menurut zona waktu Client C.
- Kemampuan teknis: fixture cabut dan pulihkan produk Fixed Asset (Admin Console), fixture Active Period baris staging, sesi API Admin kedua untuk menambah dan menghapus opsi Custom Field, navigasi keyboard (Tab, panah bawah, Enter, Esc), pembacaan nama aksesibel elemen sel Access (disediakan tim FE/BE).
- State global: produk organisasi Client C dan opsi `Lembur` pada Custom Field `Shift` Client C diubah oleh spec; hook `after` memulihkan produk `Fixed Asset`, menghapus opsi `Lembur` dari `Shift` Client C, dan membuang draft Client C walau spec gagal di tengah.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan produk dan opsi seperti di atas, buang draft User Login Client C, lepas kunci sesi edit.

## Test Steps

### TC-GS-IMPORT-905: Tombol Create Missing Options Disabled

1. Klik `[Upload File]` di toolbar dan pilih berkas `user-login-shift-lembur.csv`
2. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
3. Klik `⋯` pada baris #3, pilih `Edit`
4. Arahkan kursor ke tombol `[Create Missing Options]` pada baris pesan "Shift: Invalid option" di Error Summary Callout
5. Verifikasi tombol `[Create Missing Options]` tampil Disabled
6. Verifikasi tooltip pada tombol: "Finish or cancel the current edit first."
7. Klik tombol `[Create Missing Options]`
8. Verifikasi tidak ada dialog maupun toast
9. Verifikasi footer tetap `[Cancel]` dan `[Save]`
10. Klik `[Cancel]`; buka Global Settings > User > Custom Field dan buka Value Setting Shift
11. Verifikasi Value Setting Shift tetap `Pagi, Siang, Malam` (tidak ada opsi dibuat)

### TC-GS-IMPORT-906: Select dan MultiSelect lewat keyboard

12. Buang draft User Login Client C lewat skrip reset; muat ulang halaman Import > User Login
13. Klik `[Upload File]` di toolbar dan pilih berkas `user-login-access-fa.csv`
14. Klik `[Confirm Mapping]`
15. Tunggu aksi selesai (Modal Column Mapping tertutup)
16. Cabut produk `Fixed Asset` dari organisasi Client C lewat fixture Admin Console
17. Muat ulang halaman Import > User Login
18. Klik `⋯` pada baris #1, pilih `Edit`
19. Pindahkan fokus ke sel Access baris #1 dengan Tab
20. Verifikasi nama aksesibel sel Access mengumumkan nilai terpilih beserta status Invalid pada chip `Fixed Asset`
21. Tekan Arrow Down untuk menyorot pilihan dan Enter untuk memilih
22. Verifikasi pilihan yang disorot terpilih sebagai chip
23. Verifikasi tidak ada toast (`[Save]` tidak terpicu)
24. Tekan Esc
25. Verifikasi panel pilihan tertutup
26. Verifikasi sesi edit tetap aktif
27. Pindahkan fokus dengan Tab ke tombol hapus chip `Fixed Asset` dan tekan Enter
28. Verifikasi chip Invalid `Fixed Asset` terhapus
29. Verifikasi footer tetap `[Cancel]` dan `[Save]`
30. Verifikasi tidak ada toast
31. Klik `[Cancel]`, lalu klik `[Discard]` pada dialog Discard Changes

### TC-GS-IMPORT-894: Access tersimpan di luar produk organisasi memblokir Save sampai chip dihapus

32. Muat ulang halaman Import > User Login
33. Verifikasi baris #1 berstatus `error`
34. Verifikasi Error Summary Callout memuat "Access must only contain the following values: Global Settings" dengan badge "1 row"
35. Klik `⋯` pada baris #1, pilih `Edit`
36. Verifikasi chip `Global Settings` tampil normal
37. Verifikasi chip `Fixed Asset` tampil berstatus Invalid (ikon dan teks deskriptif) dan tidak dihapus diam-diam
38. Klik `[Save]` tanpa mengubah sel Access
39. Verifikasi `[Save]` diblokir tanpa toast sukses
40. Verifikasi sel Access berborder `danger` dengan pesan "Access must only contain the following values: Global Settings"
41. Verifikasi footer tetap `[Cancel]` dan `[Save]`
42. Hapus chip `Fixed Asset` dengan tombol hapus pada chip
43. Verifikasi chip `Fixed Asset` hilang dan hanya `Global Settings` tersisa
44. Klik `[Save]`
45. Verifikasi muncul toast sukses: "Success, row has been updated."
46. Verifikasi baris #1 berstatus `pending`
47. Verifikasi baris #1 Access `Global Settings`
48. Pulihkan produk `Fixed Asset` ke organisasi Client C lewat fixture Admin Console; buang draft User Login Client C

### TC-GS-IMPORT-896: Active Period lampau tampil Invalid

49. Muat ulang halaman Import > User Login
50. Klik `[Upload File]` di toolbar dan pilih berkas `user-login-active-period.csv`
51. Klik `[Confirm Mapping]`
52. Tunggu aksi selesai (Modal Column Mapping tertutup)
53. Mundurkan Active Period baris #1 ke kemarin lewat fixture Active Period baris staging
54. Muat ulang halaman Import > User Login
55. Verifikasi baris #1 berstatus `error`
56. Verifikasi Error Summary Callout memuat "Active Period: Please select a future date." dengan badge "1 row"
57. Klik `⋯` pada baris #1, pilih `Edit`
58. Verifikasi DatePicker Active Period menampilkan tanggal lampau tersimpan sebagai nilai berstatus Invalid (ikon dan teks deskriptif) dan tidak dikosongkan
59. Klik `[Save]` tanpa mengubah sel Active Period
60. Verifikasi `[Save]` diblokir tanpa toast sukses
61. Verifikasi sel Active Period berborder `danger` dengan pesan "Please select a future date."
62. Verifikasi footer tetap `[Cancel]` dan `[Save]`
63. Pilih tanggal besok pada DatePicker
64. Klik `[Save]`
65. Verifikasi muncul toast sukses: "Success, row has been updated."
66. Verifikasi baris #1 berstatus `pending`
67. Verifikasi baris #1 Active Period tanggal besok
68. Buang draft User Login Client C lewat skrip reset
69. Muat ulang halaman Import > User Login

### TC-GS-IMPORT-904: Opsi Shift ditambahkan admin lain saat sesi edit berjalan

70. Klik `[Upload File]` di toolbar dan pilih berkas `user-login-shift-lembur.csv`
71. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
72. Klik `⋯` pada baris #3, pilih `Edit`
73. Klik sel Shift baris #3
74. Verifikasi daftar pilihan memuat `Pagi`, `Siang`, dan `Malam` tanpa `Lembur`
75. Admin kedua Client C menambahkan opsi `Lembur` ke Custom Field `Shift` lewat sesi API hingga tersimpan
76. Ketik `Lembur` pada sel Shift baris #3, lalu pilih `Use "Lembur"` (sesi edit belum ditutup)
77. Klik `[Save]`
78. Verifikasi `[Save]` tidak diblokir dan muncul toast sukses: "Success, row has been updated."
79. Verifikasi baris #3 berstatus `pending`
80. Verifikasi baris #3 Shift `Lembur`
81. Muat ulang halaman Import > User Login
82. Verifikasi baris #1 dan #2 (Shift `Lembur`) berstatus `pending`
83. Verifikasi Staging Metric Cards: Total Rows 3, Ready to Import 3, Errors 0

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional; Admin kedua hanya pemicu (P-2, sesi API); fixture Admin Console dan fixture Active Period hanya penyiap state (P-2).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: TC-905 dan TC-906 (tanpa menyimpan) mendahului TC-894 dan TC-896 yang menyimpan; TC-904 paling akhir karena mengubah opsi Custom Field Client C.
- Langkah penghubung (tanpa `Verifikasi`): langkah 10 (membuka Value Setting Shift untuk mengamati bahwa tidak ada opsi dibuat), langkah 12, 16, 17, 48, 49, 53, 54, 68, 69 menyiapkan atau memulihkan state atau memuat ulang halaman (Kontrak Fixture R1 dan R2; skrip fixture sinkron, `suite.md`).
- Langkah penghubung "Tunggu aksi selesai" (aksi tanpa `Verifikasi`): langkah 15 dan 52 menunggu `[Confirm Mapping]` selesai (Modal Column Mapping tertutup) sebelum fixture Admin Console atau fixture Active Period baris staging pada langkah 16 dan 53.
- Spec berisi 83 langkah. Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional) dan satu topik (nilai tersimpan Invalid pada Edit Mode Client C), tiap blok membuat draft dan memulihkan state sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-GS-IMPORT-205, 659, 665, 835, 899, dan 907 ada di spec 103.
- Temuan untuk QA:
  - TC-GS-IMPORT-905 Expected b menyebut "tidak ada opsi dibuat" tanpa langkah observasi; spec mengamatinya dengan membuka Value Setting Shift sesudah `[Cancel]` (langkah 10 dan 11), tambahan yang dicatat di sini.
  - TC-GS-IMPORT-906 Expected d ("nama aksesibel memuat teks Invalid") diasersi sebelum chip dihapus (langkah 20) karena setelah penghapusan chip itu tidak ada lagi; urutan Expected TC tidak diikuti.
  - Penanda "Tunggu aksi selesai (Modal Column Mapping tertutup)" pada langkah 15 dan 52 tidak ada di TC-GS-IMPORT-906 maupun TC-GS-IMPORT-896; spec menambahkannya sebagai langkah penghubung agar fixture berjalan sesudah `[Confirm Mapping]` selesai.
  - TC-GS-IMPORT-894 dan 906 bergantung pada fixture Admin Console untuk mencabut produk `Fixed Asset`; TC-GS-IMPORT-896 bergantung pada fixture Active Period baris staging. Mekanisme tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
  - Post Condition semua TC ("Draft Client C dihapus", "Produk dipulihkan", "Opsi dihapus dari Custom Field") adalah pemulihan oleh fixture dan dikerjakan langkah 48, 68 dan hook `after`; tidak diasersi (S-01).
