---
id: TC-GS-FILEMGR-E2E-032-filter-panel-opsi-chip-dan-opsi-setelah-delete
title: "Filter Panel Tabel Utama: Screening, Opsi Dropdown, Chip, Indikator, dan Opsi Setelah File JPEG Dihapus"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-122
  - TC-GS-FILEMGR-123
  - TC-GS-FILEMGR-124
  - TC-GS-FILEMGR-135
  - TC-GS-FILEMGR-136
  - TC-GS-FILEMGR-137
  - TC-GS-FILEMGR-138
  - TC-GS-FILEMGR-142
coverage:
  web: automated
---

# Filter Panel Tabel Utama: Screening, Opsi Dropdown, Chip, Indikator, dan Opsi Setelah File JPEG Dihapus

## Prerequisites

- Mode: FE+BE. Spec menghapus satu file (`alex-photo.jpeg`) pada langkah terakhir; semua langkah lain hanya membaca.
- Akun: Total Control `Sinta Maharani`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login akun ini dilakukan sekali di hook `before`; layar awal Global Settings > File Manager dibuka di hook `beforeEach`.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (Tabel A2): 33 file aktif (F01 `budi-avatar.jpg` s.d. F08 `Prof-Photo-Of-Hendra-Gunawan-Kusuma-Wijaya-For-Annual-Report-2026.jpg`, F09-F33 `staff-photo-01.jpg` s.d. `staff-photo-25.jpg`), 4 halaman pada ukuran halaman 10, format tanggal General Settings default `dd/MM/yy HH:mm`. Hook `before` memastikan dataset File Manager client sama dengan Tabel A2 (tanpa sisa file, Recycle Bin, atau Changelog dari spec lain) lewat fixture BE yang disediakan tim FE/BE (mekanisme tidak tertulis di TC; lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); hitungan baris dalam spec ini mengasumsikan dataset Tabel A2 segar tanpa sisa dari spec lain.
- Flag Guided Tooltip halaman File Manager: mengikuti pernyataan hook suite di `suite.md` (flag `guided_tooltip_seen_<page_key>` true untuk akun aktor); spec ini tidak mengubahnya.
- Target Delete (TC-GS-FILEMGR-142): `alex-photo.jpeg` (F03) milik data seed spec ini (bukan data bersama dengan spec lain, S-06); satu-satunya file berformat JPEG di Tabel A2.
- Cleanup: hook `after` mengembalikan file `alex-photo.jpeg` ke tabel utama (seeding ulang lewat fixture BE yang disediakan tim FE/BE), mengembalikan Recycle Bin dan Changelog ke Tabel A3 dan A4 (entri yang dibuat Delete pada langkah langkah 54 tidak dapat dihapus lewat UI), serta mengosongkan Filter, Search, dan Sort tabel utama.
- Kemampuan teknis: membaca badge titik pada ikon Filter; seeding dan reset dataset File Manager lewat fixture BE.
- TC-GS-FILEMGR-122, 123, 124, 135, 136, 137, 138: Tabel A2 tersedia; enam nilai Uploaded By berbeda (`Alexander Graham Bell`, `Budi Santoso`, `Hendra Gunawan`, `Maya Wijaya`, `Sinta Maharani`, `System`); tiga nilai File Format (JPG, PNG, JPEG).
- TC-GS-FILEMGR-142: `alex-photo.jpeg` adalah satu-satunya file berformat JPEG.

## Test Steps

### TC-GS-FILEMGR-122: Screening Filter Panel tabel utama

1. Klik ikon Filter di toolbar
2. Verifikasi ikon Filter berubah gelap saat panel terbuka
3. Verifikasi field berurutan: `File Format`, `Size (KB)`, `Uploaded By`, `Upload Date`
4. Verifikasi field `File Format` adalah multi-select searchable dengan placeholder "All formats"
5. Verifikasi field `Size (KB)` adalah Range Min–Max dengan placeholder "Min" dan "Max"
6. Verifikasi field `Uploaded By` adalah multi-select searchable dengan placeholder "All users"
7. Verifikasi field `Upload Date` adalah date range picker dengan placeholder "Select date"
8. Verifikasi tombol `[Clear Field]` di kiri dan `[Apply]` di kanan

### TC-GS-FILEMGR-123: Opsi dropdown File Format berasal dari data tabel saat ini

9. Buka dropdown `File Format`
10. Verifikasi opsi tepat tiga: `JPEG`, `JPG`, `PNG`
11. Verifikasi `JPG` dan `JPEG` tampil sebagai dua opsi terpisah

### TC-GS-FILEMGR-124: Opsi dropdown Uploaded By memakai nama lengkap

12. Tutup dropdown `File Format`
13. Buka dropdown `Uploaded By`
14. Verifikasi opsi tepat enam: `Alexander Graham Bell`, `Budi Santoso`, `Hendra Gunawan`, `Maya Wijaya`, `Sinta Maharani`, `System`
15. Verifikasi nama user tampil sebagai nama lengkap (bukan `[First Name] [Last Initial]`)

### TC-GS-FILEMGR-138: Overflow chip pada field filter multi-select

16. Pilih seluruh enam opsi pada dropdown `Uploaded By`
17. Tutup dropdown `Uploaded By`
18. Verifikasi field `Uploaded By` menampilkan chip sebanyak yang muat pada lebar field
19. Verifikasi sisa chip diringkas dalam satu chip `+N more` dengan N sama dengan jumlah chip yang tersembunyi
20. Verifikasi field `Uploaded By` tidak melebar keluar panel
21. Verifikasi field `Uploaded By` tidak digulir horizontal
22. Klik `[Clear Field]` tanpa `[Apply]`

### TC-GS-FILEMGR-136: Hapus chip lewat ikon (✕) meng-uncheck opsi di dropdown dan chip lain bertahan

23. Buka dropdown `File Format`
24. Pilih `JPG` dan `PNG` pada `File Format`
25. Verifikasi dua chip `JPG` dan `PNG` tampil di dalam field `File Format`
26. Klik ikon `(✕)` pada chip `JPG`
27. Verifikasi chip `JPG` hilang
28. Verifikasi chip `PNG` tetap ada
29. Buka dropdown `File Format`
30. Verifikasi opsi `JPG` tidak tercentang
31. Verifikasi opsi `PNG` tetap tercentang

### TC-GS-FILEMGR-137: Uncheck opsi di dalam dropdown menghapus chip yang bersangkutan

32. Tutup dropdown `File Format`
33. Klik `[Clear Field]`
34. Buka dropdown `File Format`
35. Pilih `JPG` dan `PNG` pada `File Format`
36. Hapus centang `JPG` di dalam dropdown `File Format`
37. Verifikasi chip `JPG` hilang dari field `File Format`
38. Verifikasi chip `PNG` tetap ada
39. Verifikasi opsi `PNG` tetap tercentang

### TC-GS-FILEMGR-135: Indikator titik pada ikon Filter muncul saat ada filter ter-Apply

40. Tutup dropdown `File Format`
41. Klik `[Clear Field]`
42. Verifikasi ikon Filter tanpa badge titik
43. Pilih `JPEG` pada `File Format`
44. Klik `[Apply]`
45. Klik ikon Filter untuk menutup panel
46. Verifikasi badge titik tampil pada ikon Filter walau panel tertutup
47. Klik ikon Filter untuk membuka panel
48. Klik `[Clear Field]`
49. Klik `[Apply]`
50. Verifikasi badge titik hilang dari ikon Filter
51. Klik ikon Filter untuk menutup panel

### TC-GS-FILEMGR-142: Opsi File Format mengikuti data tabel setelah satu-satunya file JPEG dihapus

52. Klik ikon elipsis `(⋯)` pada baris `alex-photo.jpeg`
53. Pilih `Delete`
54. Klik `[Delete]` pada dialog konfirmasi
55. Tunggu aksi selesai
56. Klik ikon Filter
57. Buka dropdown `File Format`
58. Verifikasi opsi `File Format` hanya `JPG` dan `PNG`
59. Verifikasi opsi `JPEG` tidak ada

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`. Semua TC sumber spec ini dikerjakan di sini; tidak ada TC yang terbelah lintas spec.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-FILEMGR-122 (screening) pertama, lalu 123, 124, 138, 136, 137, 135, dan TC-GS-FILEMGR-142 paling akhir (urutan sumber 122, 123, 124, 135, 136, 137, 138, 142). TC-GS-FILEMGR-138 didahulukan dari 136, 137, dan 135 karena dropdown `Uploaded By` masih terbuka dari TC-GS-FILEMGR-124; TC-GS-FILEMGR-135 ditaruh sesudah 136 dan 137 supaya `[Clear Field]` tanpa `[Apply]` dari TC-GS-FILEMGR-138 hingga 137 tidak pernah mengubah hasil tabel. TC-GS-FILEMGR-142 menghapus data sehingga ditaruh paling akhir (prinsip 5).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 12 (menutup dropdown), langkah 17 (menutup dropdown `Uploaded By`), langkah 22 (mengosongkan enam pilihan tanpa Apply sebelum TC-GS-FILEMGR-136), langkah 32 dan langkah sesudahnya (menutup dropdown dan mengosongkan sisa pilihan TC-GS-FILEMGR-136), langkah 40 dan langkah sesudahnya (menutup dropdown dan mengosongkan pilihan sebelum TC-GS-FILEMGR-135), serta langkah "Tunggu aksi selesai" setelah langkah 54 (sebelum berpindah ke Filter Panel).
- Alasan spec melewati sekitar 35 langkah (ekspansi sekitar 59 langkah): seluruh blok memakai Filter Panel tabel utama yang sama pada dataset Tabel A2, satu akun, satu topik (opsi dan tampilan Filter Panel); blok sebelum TC-GS-FILEMGR-142 hanya membaca. Kegagalan keras pada langkah membuka Filter Panel (TC-GS-FILEMGR-122) menghentikan blok sesudahnya; risiko ini diterima karena panel yang sama dipakai semua blok. Nilai filter yang diterapkan (hasil tabel) diuji di spec 033 dan 034.
- Temuan untuk QA:
  - TC-GS-FILEMGR-142: TC tidak menyebut label tombol konfirmasi dan teks dialog Delete untuk file foto profil aktif (F03); spec memakai `[Delete]` dan tidak mengasersi isi dialog (diasersi di spec Delete). Pemulihan `alex-photo.jpeg` dan penghapusan entri Recycle Bin dan Changelog hasil Delete tidak punya mekanisme tertulis; ditulis sebagai fixture BE "disediakan tim FE/BE" (S-13).
  - TC-GS-FILEMGR-138: nilai N pada chip `+N more` bergantung lebar field dan viewport yang tidak disebut TC; spec mengasersi N sama dengan jumlah chip tersembunyi tanpa angka.
  - TC-GS-FILEMGR-136 langkah 3 "Buka dropdown File Format" tidak menyebut apakah dropdown masih terbuka setelah klik (✕) pada chip; ditulis sebagai langkah buka dropdown.
  - Selector badge titik dan chip "disediakan tim FE"; TC tidak menyebut label aksesibilitasnya.
  - Seeding Tabel A2 dan reset dataset antar spec tidak punya mekanisme tertulis di TC (lihat spec 031); jumlah baris `33` mengasumsikan tidak ada baris D05, D06, atau D08 dari spec lain.
