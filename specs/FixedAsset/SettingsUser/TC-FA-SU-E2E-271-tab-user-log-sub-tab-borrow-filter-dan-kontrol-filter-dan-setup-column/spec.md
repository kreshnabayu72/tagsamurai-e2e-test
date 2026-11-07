---
id: TC-FA-SU-E2E-271-tab-user-log-sub-tab-borrow-filter-dan-kontrol-filter-dan-setup-column
title: "Tab User Log sub-tab Borrow: Filter dan Kontrol Filter dan Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-822
  - TC-FA-SU-823
  - TC-FA-SU-824
  - TC-FA-SU-825
coverage:
  web: automated
---

# Tab User Log sub-tab Borrow: Filter dan Kontrol Filter dan Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso; sub-tab Borrow berisi 6 baris (`Borrowed` dan `Returned` untuk `BRW-20260205-0102`, `BRW-20260320-0188`, `BRW-20260615-0305`, `BRW-20260712-0347`) sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface User Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab User Log, lalu klik Sub-tab Borrow

### TC-FA-SU-822: Perilaku Filter Panel (tutup tanpa Apply, indikator titik, dan nilai kosong)

2. Klik icon Filter, buka dropdown `Activity`, lalu centang `Borrowed` tanpa klik `[Apply]`
3. Klik di luar panel Filter
4. Klik icon Filter untuk membuka panel
5. Verifikasi field `Activity` tidak berisi pilihan (nilai ter-Apply terakhir: kosong)
6. Verifikasi tabel tidak berubah dan menampilkan enam baris
7. Buka dropdown `Activity`, lalu centang `Borrowed`
8. Klik `[Apply]`
9. Verifikasi icon Filter menampilkan badge titik saat panel terbuka
10. Klik icon Filter untuk menutup panel
11. Verifikasi icon Filter menampilkan badge titik saat panel tertutup
12. Klik icon Filter untuk membuka panel
13. Klik `[Clear Field]` pada field `Activity`, lalu klik `[Apply]`
14. Verifikasi badge titik pada icon Filter hilang
15. Buka dropdown `Activity`
16. Verifikasi dropdown `Activity` memuat opsi `Borrowed` dan `Returned`
17. Verifikasi dropdown `Activity` tidak memiliki opsi untuk nilai kosong
18. Centang `Borrowed`
19. Klik `[Apply]`
20. Klik header `⋯`, hilangkan centang `Activity`, lalu tutup overlay dengan Esc
21. Verifikasi field `Activity` tetap ada pada panel Filter
22. Verifikasi Filter Activity `Borrowed` tetap berlaku (tabel menyisakan `Borrowed|BRW-20260712-0347`, `Borrowed|BRW-20260320-0188`, `Borrowed|BRW-20260205-0102`)
23. Klik header `⋯`, beri centang `Activity`, lalu tutup overlay dengan Esc
24. Klik `[Clear Field]` pada field `Activity`, lalu klik `[Apply]`
25. Klik icon Filter untuk menutup panel

### TC-FA-SU-823: Chip dan checkbox dropdown Filter sinkron dua arah, logika OR dalam field

26. Klik icon Filter, lalu buka dropdown `Activity`
27. Centang `Borrowed` dan `Returned`
28. Klik `[Apply]`
29. Verifikasi dua chip `Borrowed` dan `Returned` tampil di dalam field `Activity`
30. Verifikasi hasil adalah gabungan (OR) kedua opsi: seluruh enam baris
31. Klik `✕` pada chip `Returned` tanpa membuka dropdown
32. Verifikasi chip `Returned` hilang
33. Verifikasi chip `Borrowed` tetap tampil
34. Buka dropdown `Activity`
35. Verifikasi checkbox opsi `Returned` ter-uncheck
36. Centang kembali `Returned`
37. Hilangkan centang `Borrowed`
38. Verifikasi chip `Borrowed` hilang
39. Verifikasi chip `Returned` tetap tampil
40. Ketik `RET` di kotak cari dropdown
41. Verifikasi opsi dropdown menyempit menjadi `Returned` (substring, tidak case-sensitive)
42. Ganti keyword di kotak cari dropdown dengan `zzzz`
43. Verifikasi dropdown menampilkan `No results found`
44. Tutup dropdown, klik `[Clear Field]` pada field `Activity`, lalu klik `[Apply]`
45. Klik icon Filter untuk menutup panel

### TC-FA-SU-824: Screening Overlay Column Visibility

46. Klik header kolom `⋯` (Actions)
47. Verifikasi overlay tampil dengan tooltip `Column Visibility` pada header
48. Verifikasi daftar kolom berurutan `Date`, `Activity`, `Transaction ID`, `Name`, `PIC` dengan checkbox Hideable terpilih dan enabled serta drag handle
49. Verifikasi item `Setup Column...` di bagian bawah overlay
50. Tutup overlay Column Visibility dengan Esc

### TC-FA-SU-825: Screening Popup Setup Column dan Preview Table

51. Klik header kolom `⋯`, lalu klik item `Setup Column...`
52. Verifikasi Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan icon close `✕` tampil
53. Verifikasi body: daftar kolom `Date`, `Activity`, `Transaction ID`, `Name`, `PIC` dengan checkbox, drag handle, icon Pin, dan Live Preview tabel
54. Verifikasi footer: `[Reset to Default]` dan `[Save]` rata kanan tanpa `[Cancel]`
55. Klik `✕` untuk menutup popup Setup Column

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), semua `[Clear Field]` lalu `[Apply]`, penutupan panel Filter, overlay, dan popup; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Hasil gabungan (OR) pada TC-FA-SU-823 butir a (`Borrowed` dan `Returned`) adalah seluruh enam baris Pre-setup #30. Sub-tab hanya punya dua opsi Activity, sehingga pada butir c opsi `Returned` dicentang kembali sebelum `Borrowed` di-uncheck supaya klausa "chip lain tetap" teramati (TC hanya menyebut "uncheck opsi yang tersisa"). Keyword dropdown `RET` dan `zzzz` dipilih spec karena TC tidak menyebutnya.
- Temuan untuk QA (S-15): (1) TC-FA-SU-822 butir a tidak menyebut cara mengasersi "nilai ter-Apply terakhir"; spec mengasersi field `Activity` kosong karena belum ada filter ter-Apply. (2) TC-FA-SU-822 butir c menyebut "menyaring keluar baris yang nilainya kosong", tetapi seed #30 tidak memiliki nilai kosong; hanya ketiadaan opsi nilai kosong yang diasersi. (3) TC-FA-SU-823 Langkah Uji nomor 6 hanya menyebut "keyword tanpa hasil" sedangkan Expected butir d juga meminta penyempitan opsi; spec menguji keduanya dengan dua keyword.
- Spec ini berjumlah 55 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Langkah 16 (`Verifikasi` dropdown `Activity` memuat opsi `Borrowed` dan `Returned`) adalah asersi tambahan di luar Expected TC-FA-SU-822 dan menjadi anchor positif untuk asersi absence opsi nilai kosong pada langkah 17 (bagian 8b butir 2, S-03).
