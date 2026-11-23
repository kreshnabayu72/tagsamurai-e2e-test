---
id: TC-FA-SU-E2E-281-tab-user-log-sub-tab-assignment-filter-dan-kontrol-filter-dan-setup-column
title: "Tab User Log sub-tab Assignment: Filter dan Kontrol Filter dan Setup Column"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-855
  - TC-FA-SU-856
  - TC-FA-SU-857
  - TC-FA-SU-858
coverage:
  web: automated
---

# Tab User Log sub-tab Assignment: Filter dan Kontrol Filter dan Setup Column

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab User Log sub-tab Assignment Budi Santoso (Pre-setup #30, 5 baris; urutan default Date descending). Label baris = `Activity|Transaction ID`; alias dipakai langkah:
  - A-1: `Unassigned|ASG-20260618-0089`, Date `30/06/26`, PIC `Eka W` (keyword `Wulandari`)
  - A-2: `Handed over|ASG-20260625-0102`, Name `Lemari`, PIC `Ahmad D`
  - A-3: `Handed over|ASG-20260618-0089`, PIC `Eka W` (keyword `Wulandari`)
  - A-4: `Handed over|ASG-20260512-0067`, PIC `Ahmad D`, Date di dalam rentang 05/05/26 sampai 12/05/26
  - A-5: `Handed over|ASG-20260505-0045`, PIC `Ahmad D`, Date di dalam rentang 05/05/26 sampai 12/05/26
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed User Log #30 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface User Log dan tidak menambah entri pada Budi Santoso.
- Pemulihan preferensi kolom: kemampuan menghapus preferensi kolom tabel di browser (bukan `[Reset to Default]`) disediakan tim FE; dijalankan sebagai langkah penghubung dan di hook `after`. Preferensi kolom disimpan per perangkat (browser) sehingga spec ini tidak memengaruhi tabel lain.

## Test Steps

### TC-FA-SU-855: Perilaku Filter Panel: tutup tanpa Apply, indikator titik, dan nilai kosong

1. Ketik Search `Budi Santoso`, tekan Enter, buka Detail pengguna Budi Santoso lalu klik tab User Log, sub-tab Assignment
2. Klik icon Filter, buka dropdown Activity, centang `Handed over` tanpa `[Apply]`
3. Klik di luar panel Filter
4. Klik icon Filter
5. Verifikasi panel yang dibuka lagi menampilkan nilai ter-Apply terakhir (field Activity kosong)
6. Verifikasi tabel tidak berubah
7. Buka dropdown Activity, centang `Handed over`, klik `[Apply]`
8. Verifikasi panel Filter tetap terbuka setelah `[Apply]`
9. Klik icon Filter untuk menutup panel
10. Verifikasi panel Filter tertutup
11. Verifikasi ikon Filter menampilkan badge titik saat panel tertutup
12. Klik icon Filter untuk membuka panel
13. Verifikasi ikon Filter menampilkan badge titik saat panel terbuka
14. Klik `[Clear Field]`, lalu klik `[Apply]`
15. Verifikasi badge titik hilang
16. Buka dropdown Activity
17. Verifikasi dropdown menampilkan opsi `Handed over` dan `Unassigned`
18. Verifikasi dropdown tidak memiliki opsi untuk nilai kosong
19. Centang `Handed over`, klik `[Apply]`
20. Klik header kolom Column Visibility (⋯), hilangkan centang Activity, tekan Esc
21. Verifikasi field Activity pada Filter Panel tidak hilang
22. Verifikasi filter Activity `Handed over` yang ter-Apply tetap berlaku
23. Klik `[Clear Field]`, lalu klik `[Apply]`
24. Klik header kolom Column Visibility (⋯), centang kembali Activity, tekan Esc

### TC-FA-SU-856: Chip dan checkbox dropdown Filter sinkron dua arah, logika OR dalam field

25. Buka dropdown Activity
26. Centang `Handed over` dan `Unassigned`
27. Verifikasi dua chip `Handed over` dan `Unassigned` tampil di dalam field Activity
28. Klik `[Apply]`
29. Verifikasi hasil adalah gabungan (OR) kedua opsi: A-1, A-2, A-3, A-4, A-5
30. Klik ✕ pada chip `Unassigned` tanpa membuka dropdown
31. Verifikasi chip `Unassigned` hilang
32. Verifikasi chip `Handed over` tetap
33. Buka dropdown Activity
34. Verifikasi checkbox opsi `Unassigned` ter-uncheck
35. Centang kembali `Unassigned`
36. Hilangkan centang `Handed over`
37. Verifikasi chip `Handed over` hilang
38. Verifikasi chip `Unassigned` tetap tampil
39. Ketik `assi` pada kotak cari dropdown Activity
40. Verifikasi opsi dropdown dipersempit menjadi `Handed over` dan `Unassigned` (substring, tidak case-sensitive)
41. Ganti isi kotak cari dropdown Activity dengan `zzzz`
42. Verifikasi dropdown menampilkan `No results found`
43. Tutup dropdown, klik `[Clear Field]`, lalu klik `[Apply]`
44. Klik icon Filter untuk menutup panel

### TC-FA-SU-857: Screening Overlay Column Visibility

45. Klik header kolom Actions (⋯)
46. Verifikasi overlay tampil dengan tooltip `Column Visibility` pada header
47. Verifikasi daftar kolom berurutan Date, Activity, Transaction ID, Name, PIC
48. Verifikasi tiap kolom memiliki checkbox Hideable terpilih dan enabled serta drag handle
49. Verifikasi item `Setup Column...` di bagian bawah overlay

### TC-FA-SU-858: Screening Popup Setup Column dan Preview Table

50. Klik item `Setup Column...` pada overlay Column Visibility yang masih terbuka
51. Verifikasi Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan icon close ✕ tampil
52. Verifikasi body: daftar kolom Date, Activity, Transaction ID, Name, PIC dengan checkbox, drag handle, icon Pin, dan Live Preview tabel
53. Verifikasi footer: `[Reset to Default]` dan `[Save]` rata kanan tanpa `[Cancel]`
54. Klik ✕ untuk menutup popup Setup Column

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung pencarian baris (S-03, R-16, bagian 8b butir 13): langkah 1 mencari pengguna lewat Search nama persis `Budi Santoso` (nama Pre-setup) sebelum membuka Detail, karena User List dapat memuat lebih dari satu halaman (25 pengguna, 3 halaman) sehingga spec tidak mengandalkan posisi baris di halaman.
- Panel Filter tetap terbuka sesudah `[Apply]` dan baru tertutup bila icon Filter diklik (keputusan produk); karena itu `[Clear Field]` + `[Apply]` dijalankan tanpa mengklik icon Filter lagi. Langkah 9, 12 dan 44 (`Klik icon Filter untuk menutup panel`) adalah langkah penghubung yang menutup panel sebelum blok berikutnya (S-03, S-09).
- Langkah 35 (Centang kembali `Unassigned`) adalah langkah penghubung: TC-FA-SU-856 butir b dan c meminta chip lain tetap sesudah satu chip hilang; dengan hanya dua opsi, `Unassigned` dicentang kembali dahulu supaya chip itu teramati tetap tampil saat `Handed over` dihilangkan (langkah 36 sampai 38, pola yang sama dengan spec 259 dan 271). Langkah 9 dan 12 mengikuti Langkah Uji 3 TC-FA-SU-855 (menutup panel lewat icon Filter) dan langkah 8 serta 10 adalah `Verifikasi` Expected e (panel tetap terbuka sesudah `[Apply]` dan tertutup setelah icon Filter diklik).
- Spec ini berjumlah 54 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Temuan untuk QA (S-15): (1) TC mengasersi isi dan urutan baris seed tanpa Filter pembatas pada surface User Log yang dapat bertambah entri; spec mengikuti TC dan mengandalkan seed #30 yang disediakan ulang di hook `before` dan `after` (S-12, S-14). (2) TC-FA-SU-855: Expected c kalimat kedua (memilih opsi menyaring keluar baris bernilai kosong) tidak teramati karena seed tidak punya baris dengan Activity kosong; spec mengasersi tidak adanya opsi kosong dan menjalankan filter `Handed over` tanpa klaim tambahan; klausa penyaringan baris kosong tidak diasersi karena akan lulus tanpa menguji (8b butir 2). TC-FA-SU-856: keyword kotak cari dropdown (`assi`, `zzzz`) dipilih spec karena TC tidak menyebutnya; "chip lain tetap" pada Expected c diamati dengan mencentang kembali `Unassigned` lebih dulu (lihat butir langkah penghubung).
