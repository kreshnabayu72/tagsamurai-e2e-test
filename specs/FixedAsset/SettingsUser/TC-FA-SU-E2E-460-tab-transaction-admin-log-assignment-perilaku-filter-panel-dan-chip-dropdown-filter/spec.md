---
id: TC-FA-SU-E2E-460-tab-transaction-admin-log-assignment-perilaku-filter-panel-dan-chip-dropdown-filter
title: "Tab Transaction Admin Log Sub-tab Assignment: Perilaku Filter Panel dan Chip Dropdown Filter"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1158
  - TC-FA-SU-1159
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Assignment: Perilaku Filter Panel dan Chip Dropdown Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Assignment berisi 4 baris (`ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`) dengan nilai Date, Activity, Name, Assignee (satu baris dengan Assignee Division `General Affairs`), dan Group per baris sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Spec tidak menyimpan konfigurasi kolom; hide dan unhide kolom `Group` lewat Column Visibility dikembalikan oleh langkah di spec ini.

## Test Steps

### TC-FA-SU-1158: Perilaku Filter Panel (tutup tanpa Apply, indikator titik, dan nilai kosong)

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Assignment
2. Klik icon Filter
3. Buka dropdown `Group`, lalu centang `Branch Surabaya` tanpa klik `[Apply]`
4. Klik di luar panel Filter
5. Klik icon Filter untuk membuka panel
6. Verifikasi field `Group` tidak berisi pilihan (nilai ter-Apply terakhir: kosong)
7. Verifikasi tabel tidak berubah dan menampilkan empat baris
8. Buka dropdown `Group`, lalu centang `Branch Surabaya`
9. Klik `[Apply]`
10. Verifikasi icon Filter menampilkan badge titik saat panel terbuka
11. Klik icon Filter untuk menutup panel
12. Verifikasi icon Filter menampilkan badge titik saat panel tertutup
13. Klik icon Filter untuk membuka panel
14. Klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`
15. Verifikasi badge titik pada icon Filter hilang
16. Verifikasi dropdown `Group` tidak memiliki opsi untuk nilai kosong
17. Buka dropdown `Group`, lalu centang `Branch Surabaya`
18. Klik `[Apply]`
19. Klik header `⋯`, hilangkan centang `Group`, lalu tutup overlay dengan Esc
20. Verifikasi field `Group` tetap ada pada panel Filter
21. Verifikasi Filter Group `Branch Surabaya` tetap berlaku (tabel menyisakan `ASG-20260720-0071`)
22. Klik header `⋯`, beri centang `Group`, lalu tutup overlay dengan Esc
23. Klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`
24. Klik icon Filter untuk menutup panel

### TC-FA-SU-1159: Chip dan checkbox dropdown Filter sinkron dua arah, logika OR dalam field

25. Klik icon Filter, lalu buka dropdown `Group`
26. Centang `Branch Surabaya` dan `Finance & Accounting`
27. Klik `[Apply]`
28. Verifikasi dua chip `Branch Surabaya` dan `Finance & Accounting` tampil di dalam field `Group`
29. Verifikasi hasil adalah gabungan (OR) kedua opsi: `ASG-20260720-0071`, `ASG-20260715-0068`
30. Klik `✕` pada chip `Finance & Accounting` tanpa membuka dropdown
31. Verifikasi chip `Finance & Accounting` hilang
32. Verifikasi chip `Branch Surabaya` tetap tampil
33. Buka dropdown `Group`
34. Verifikasi checkbox opsi `Finance & Accounting` ter-uncheck
35. Centang kembali `Finance & Accounting`
36. Hilangkan centang `Branch Surabaya`
37. Verifikasi chip `Branch Surabaya` hilang
38. Verifikasi chip `Finance & Accounting` tetap tampil
39. Ketik `ACC` di kotak cari dropdown
40. Verifikasi opsi dropdown menyempit menjadi `Finance & Accounting` (substring, tidak case-sensitive)
41. Ganti keyword di kotak cari dropdown dengan `zzzz`
42. Verifikasi dropdown menampilkan `No results found`
43. Tutup dropdown, klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`
44. Klik icon Filter untuk menutup panel

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), penutupan dropdown dan panel Filter, `[Clear Field]`, serta hide dan unhide kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Hasil gabungan (OR) pada TC-FA-SU-1159 butir a ditulis `ASG-20260720-0071` dan `ASG-20260715-0068`, diturunkan dari opsi dropdown TC-FA-SU-1152 (`Branch Surabaya` pada `ASG-20260720-0071`, `Finance & Accounting` pada `ASG-20260715-0068`).
- Opsi kedua pada TC-FA-SU-1159 butir c dipulihkan dengan mencentang kembali `Finance & Accounting` sebelum `Branch Surabaya` di-uncheck, supaya klausa "chip lain tetap" teramati; TC hanya menyebut "uncheck opsi yang tersisa". Keyword dropdown `ACC` dan `zzzz` dipilih spec karena TC tidak menyebutnya.
- Temuan untuk QA (S-15): (1) TC-FA-SU-1158 Langkah Uji nomor 5 tidak menyebut kolom yang di-hide; spec memakai `Group`. (2) TC-FA-SU-1159 Langkah Uji nomor 6 hanya menyebut "keyword tanpa hasil" sedangkan Expected butir d juga meminta penyempitan opsi; spec menguji keduanya dengan dua keyword.
- Spec ini berjumlah 44 langkah (dihitung dengan ekspansi langkah berulang) dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
