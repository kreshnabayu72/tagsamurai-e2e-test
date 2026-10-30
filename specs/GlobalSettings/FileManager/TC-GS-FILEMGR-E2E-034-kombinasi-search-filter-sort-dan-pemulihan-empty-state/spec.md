---
id: TC-GS-FILEMGR-E2E-034-kombinasi-search-filter-sort-dan-pemulihan-empty-state
title: "Kombinasi Search, Filter, dan Sort Tabel Utama: Irisan, Independensi Clear, Reset Halaman, dan Pemulihan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-129
  - TC-GS-FILEMGR-130
  - TC-GS-FILEMGR-131
  - TC-GS-FILEMGR-132
  - TC-GS-FILEMGR-133
  - TC-GS-FILEMGR-140
  - TC-GS-FILEMGR-141
coverage:
  web: automated
---

# Kombinasi Search, Filter, dan Sort Tabel Utama: Irisan, Independensi Clear, Reset Halaman, dan Pemulihan Empty State

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data File Manager.
- Akun: Total Control `Sinta Maharani`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login akun ini dilakukan sekali di hook `before`; layar awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (Tabel A2): 33 file aktif (F01 `budi-avatar.jpg` s.d. F08 `Prof-Photo-Of-Hendra-Gunawan-Kusuma-Wijaya-For-Annual-Report-2026.jpg`, F09-F33 `staff-photo-01.jpg` s.d. `staff-photo-25.jpg`), 4 halaman pada ukuran halaman 10, format tanggal General Settings default `dd/MM/yy HH:mm`. Hook `before` memastikan dataset File Manager client sama dengan Tabel A2 (tanpa sisa file, Recycle Bin, atau Changelog dari spec lain) lewat fixture BE yang disediakan tim FE/BE (mekanisme tidak tertulis di TC; lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); hitungan baris dalam spec ini mengasumsikan dataset Tabel A2 segar tanpa sisa dari spec lain.
- Flag Guided Tooltip halaman File Manager: mengikuti pernyataan hook suite di `suite.md` (flag `guided_tooltip_seen_<page_key>` true untuk akun aktor); spec ini tidak mengubahnya.
- Data uji: kata kunci Search `photo` (27 baris: `alex-photo.jpeg`, `Prof-Photo-Of-Hendra-Gunawan-Kusuma-Wijaya-For-Annual-Report-2026.jpg`, `staff-photo-01.jpg` s.d. `staff-photo-25.jpg`), `avatar`, `staff-photo`; File Format `JPEG`, `JPG`, `PNG`; Uploaded By `System`; Sort Size Ascending dan Descending.
- Kemampuan teknis: Column Visibility lewat header kolom Actions (`⋯`); membaca info pagination tabel utama.
- Cleanup: hook `after` mengosongkan Search, Filter, dan Sort, serta menampilkan semua kolom tabel utama (preferensi UI).

## Test Steps

### TC-GS-FILEMGR-129: Search lebih dulu lalu Filter menghasilkan irisan

1. Ketik Search `photo`, tekan Enter
2. Verifikasi tabel memuat tepat 27 baris: `alex-photo.jpeg`, `Prof-Photo-Of-Hendra-Gunawan-Kusuma-Wijaya-For-Annual-Report-2026.jpg`, dan `staff-photo-01.jpg` s.d. `staff-photo-25.jpg` (diperiksa lintas halaman)
3. Klik ikon Filter di toolbar
4. Pilih `JPEG` pada `File Format`
5. Klik `[Apply]`
6. Verifikasi tabel hanya memuat satu baris `alex-photo.jpeg`
7. Verifikasi kata kunci `photo` tetap terisi di Search
8. Klik `[Clear Field]`
9. Klik `[Apply]`
10. Klik `(←)` pada kotak Search

### TC-GS-FILEMGR-130: Filter lebih dulu lalu Search menghasilkan irisan yang sama

11. Pilih `JPEG` pada `File Format`
12. Klik `[Apply]`
13. Verifikasi tabel hanya memuat satu baris `alex-photo.jpeg`
14. Ketik Search `photo`, tekan Enter
15. Verifikasi tabel hanya memuat satu baris `alex-photo.jpeg` (irisan identik dengan urutan Search lalu Filter)
16. Verifikasi filter `JPEG` tetap aktif di Filter Panel

### TC-GS-FILEMGR-131: Clear Field pada Filter Panel mempertahankan Search dan Sort aktif

17. Klik header kolom Size sekali (Ascending); Search `photo` dan Filter `JPEG` sudah aktif dari langkah sebelumnya
18. Klik `[Clear Field]`
19. Klik `[Apply]`
20. Verifikasi field `File Format` kosong
21. Verifikasi kata kunci `photo` tetap terisi di Search
22. Verifikasi tabel tetap tersaring 27 baris
23. Verifikasi Sort Size Ascending tetap aktif dengan urutan dimulai `staff-photo-01.jpg` (`200.0 KB`)

### TC-GS-FILEMGR-132: Mengosongkan Search mempertahankan Filter dan Sort aktif

24. Pilih `JPG` pada `File Format`
25. Klik `[Apply]`
26. Ganti isi kotak search dengan `photo`, tekan Enter
27. Klik header kolom Size sekali lagi (Descending)
28. Klik ikon `(✕)` di input Search, tekan Enter
29. Verifikasi input Search kosong
30. Verifikasi tabel menampilkan sedikitnya satu baris
31. Verifikasi filter `JPG` tetap aktif: tidak ada baris `PNG` maupun `JPEG`
32. Verifikasi Sort Size Descending tetap aktif dengan baris pertama `Prof-Photo-Of-Hendra-Gunawan-Kusuma-Wijaya-For-Annual-Report-2026.jpg` (`3.0 MB`)

### TC-GS-FILEMGR-133: Pemulihan dari empty state saat salah satu kontrol dilepas

33. Klik header kolom Size sekali lagi (indikator sort hilang)
34. Klik `[Clear Field]`
35. Pilih `PNG` pada `File Format`
36. Klik `[Apply]`
37. Ketik Search `avatar`, tekan Enter
38. Verifikasi empty state `No results found` tampil
39. Klik ikon `(✕)` di input Search, tekan Enter
40. Verifikasi tabel memuat tepat 3 baris PNG: `siti-profile.png`, `rudi-hartono.png`, `big-banner.png`

### TC-GS-FILEMGR-140: Filter tetap tersedia dan aktif walau kolomnya disembunyikan

41. Klik `[Clear Field]`
42. Pilih `JPEG` pada `File Format`
43. Klik `[Apply]`
44. Klik ikon Filter untuk menutup panel
45. Sembunyikan kolom `File Format` lewat Column Visibility (header kolom Actions `⋯`)
46. Verifikasi tabel tetap menampilkan satu baris `alex-photo.jpeg`
47. Klik ikon Filter untuk membuka Filter Panel
48. Verifikasi field `File Format` tetap ada di Filter Panel dengan nilai `JPEG`
49. Tampilkan kembali kolom `File Format` lewat Column Visibility
50. Klik `[Clear Field]`
51. Klik `[Apply]`
52. Klik ikon Filter untuk menutup panel

### TC-GS-FILEMGR-141: Search dan Apply Filter dari halaman lebih dari 1 mereset ke halaman 1

53. Klik `(←)` pada kotak Search
54. Pindah ke halaman 3 tabel utama
55. Ketik Search `staff-photo`, tekan Enter
56. Verifikasi tabel berada di halaman 1
57. Verifikasi baris pertama tabel adalah baris pertama hasil Search (`staff-photo-25.jpg`, urutan default Upload Date terbaru)
58. Pindah ke halaman 3
59. Klik ikon Filter
60. Pilih `System` pada `Uploaded By`
61. Klik `[Apply]`
62. Verifikasi tabel berada di halaman 1
63. Klik `[Clear Field]`
64. Klik `[Apply]`
65. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC mengikuti sumber (129, 130, 131, 132, 133, 140, 141).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8 (menghapus Filter dan Search sebelum TC-GS-FILEMGR-130), langkah 17, langkah 27, dan langkah 33 (klik header Size berturut-turut: Ascending untuk TC-GS-FILEMGR-131, Descending untuk TC-GS-FILEMGR-132, dan menghapus indikator sort sebelum TC-GS-FILEMGR-133), langkah 41 dan langkah 49 (menyiapkan dan memulihkan Filter dan visibilitas kolom), serta langkah 63 (pemulihan state; hook `after` menjadi cadangan). Search `photo` dan Filter `JPEG` yang menjadi langkah 1 TC-GS-FILEMGR-131 sudah terbentuk pada TC-GS-FILEMGR-130 dan tidak diulang; Search `photo` pada TC-GS-FILEMGR-132 diulang eksplisit karena TC sumber menulisnya sebagai langkah.
- Alasan spec melewati sekitar 35 langkah (ekspansi sekitar 65 langkah): tujuh TC memakai kombinasi kontrol (Search, Filter, Sort, halaman) pada tabel utama dan dataset Tabel A2 yang sama, hanya membaca, satu akun, satu topik (kombinasi kontrol); state dibangun berurutan oleh TC sumber (TC-GS-FILEMGR-131 dan 132 bergantung pada 130) dan dipisah dengan pemulihan eksplisit sehingga tiap blok tidak bergantung pada hasil asersi blok sebelumnya.
- Temuan untuk QA:
  - TC-GS-FILEMGR-141: TC tidak menyebut nama baris pertama hasil Search; spec menurunkan `staff-photo-25.jpg` dari urutan default Upload Date terbaru Tabel A2 (`01/07/26` s.d. `25/07/26`).
  - TC-GS-FILEMGR-131, 132: TC menyebut precondition dibangun dari TC sebelumnya (dependensi 130); spec melanjutkan state yang setara dan menulis langkah penghubung.
  - TC-GS-FILEMGR-129 butir a: 27 baris tersebar di tiga halaman (ukuran halaman 10); TC tidak menyebut cara memeriksa seluruh baris. Spec mengasersi jumlah dan komposisi lintas halaman.
  - Seeding Tabel A2 dan reset dataset antar spec tidak punya mekanisme tertulis di TC (lihat spec 031).
