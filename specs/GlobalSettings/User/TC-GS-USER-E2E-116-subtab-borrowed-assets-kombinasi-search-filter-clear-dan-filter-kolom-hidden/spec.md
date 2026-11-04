---
id: TC-GS-USER-E2E-116-subtab-borrowed-assets-kombinasi-search-filter-clear-dan-filter-kolom-hidden
title: "Sub-tab Borrowed Assets: kombinasi Search dan Filter, Clear, filter kolom hidden, nol baris"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-731
  - TC-GS-USER-732
  - TC-GS-USER-733
  - TC-GS-USER-734
  - TC-GS-USER-735
coverage:
  web: automated
---

# Sub-tab Borrowed Assets: kombinasi Search dan Filter, Clear, filter kolom hidden, nol baris

## Prerequisites

- Mode: FE+BE. Spec hanya membaca data user; tidak ada data user yang diubah.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun: Total Control, Siti Nurhaliza, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > User > User List dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): `Joko Susilo` (No. 19; Access Fixed Asset + Supply Asset) sebagai pemilik tabel Borrowed Assets; `Andi Wijaya`, `Doni Pratama` (No. 10 dan 11) sebagai PIC seed. Client FAMS aktif. `Joko Susilo` (Tabel Pre-setup No. 19) sudah punya borrowed asset Pre-setup (`B0` baris, nilainya tidak disebut TC). Baris itu tidak diubah dan ikut tampil di tabel. Asersi memakai nilai bersuffix `{runId}-116` (Name, Brand, Model / Type) sehingga tidak bentrok dengan `B0`; jumlah baris tabel = `B0` + baris seed.
- Data Dinamis (seeding FAMS atas `Joko Susilo`, 26 baris aset pinjaman; seluruhnya tanpa foto sehingga kolom Photo menampilkan `—`):
  - Grup L (8 baris): Name `Laptop 1 {runId}-116` sampai `Laptop 8 {runId}-116`; Brand `Lenovo {runId}-116`; Model / Type `ThinkPad {runId}-116`; PIC `Andi Wijaya` (tampil `Andi W`); Due Return Date = hari uji + 10 hari (`{tglL}`).
  - Grup P (10 baris): Name `Proyektor 1 {runId}-116` sampai `Proyektor 10 {runId}-116`; Brand `Epson {runId}-116`; Model / Type `EB-X06 {runId}-116`; PIC `Doni Pratama` (tampil `Doni P`); Due Return Date = hari uji + 20 hari (`{tglP}`).
  - Grup K (8 baris): Name `Kamera 1 {runId}-116` sampai `Kamera 8 {runId}-116`; Brand `Canon {runId}-116`; Model / Type `EOS-R10 {runId}-116`; PIC `Andi Wijaya` (tampil `Andi W`); Due Return Date = hari uji + 30 hari (`{tglK}`).
  - Seluruh nilai Name, Brand, dan Model / Type unik per spec dan per run; setiap kolom yang diuji punya sedikitnya dua nilai distinct (Brand dan Model / Type tiga nilai, PIC dua nilai, Due Return Date tiga nilai) (S-11). `{tglL}`, `{tglP}`, `{tglK}` adalah tanggal Due Return Date grup tersebut dalam Date Format General Settings client, dihitung di hook `before` dari hasil seeding. PIC memakai user Pre-setup `Andi Wijaya` dan `Doni Pratama` yang hanya dibaca.
- Data uji per TC: TC-GS-USER-731 Search `Wijaya` dan Filter Brand `Canon {runId}-116`; TC-GS-USER-732 Filter Brand `Lenovo {runId}-116` dan Search `Wijaya`; TC-GS-USER-733 sort Name ascending; TC-GS-USER-734 Filter Brand `Epson {runId}-116` dan kolom `Brand` di-hide lalu di-unhide; TC-GS-USER-735 Search `Laptop` dan Filter Brand `Canon {runId}-116` (tidak beririsan).
- Kemampuan teknis (HK8, disediakan tim FE/BE; endpoint tidak disebut di TC, PRD, atau LLD): seeding FAMS yang membuat aset beserta transaksi peminjaman atas `Joko Susilo` dengan Name, Brand, Model / Type, PIC, dan Due Return Date yang ditentukan; membaca Transaction ID dan Asset ID hasil seeding; membaca jumlah borrowed asset Pre-setup `Joko Susilo` sebelum seeding (disebut `B0` di bawah); menghapus atau mengembalikan aset dan transaksi seed di hook `after`.
- Kemampuan teknis tambahan: memilih opsi dropdown multi-select; menyetel page size Pagination.
- State yang diubah dan dipulihkan: Search dikosongkan dan ditutup, Filter dikosongkan, sort dikembalikan ke default, kolom `Brand` ditampilkan kembali, dan page size dikembalikan ke 10 di akhir spec; preferensi kolom tabel Borrowed Assets dikembalikan ke default di hook `after` sebagai cadangan. Aset dan transaksi seed dibersihkan di hook `after` tanpa mengandalkan seeding berhasil penuh.
- Hook `beforeEach`: kembali ke layar Global Settings > User > User List.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-USER-731: Search lalu Filter menghasilkan irisan

1. Klik icon Search di User List, ketik `Joko Susilo`, tekan Enter
2. Klik Name `Joko Susilo` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Borrowed Assets`
5. Pilih 100 baris per halaman pada Pagination
6. Klik icon Search, ketik `Wijaya`, tekan Enter
7. Verifikasi baris `Laptop 1 {runId}-116` dan `Kamera 1 {runId}-116` tampil (hasil Search sebelum Filter)
8. Klik icon Filter
9. Buka dropdown Brand, pilih opsi `Canon {runId}-116`
10. Klik `[Apply]`
11. Verifikasi hasil = Search ∩ Filter: tabel hanya menampilkan 8 baris `Kamera 1` sampai `Kamera 8`
12. Verifikasi baris `Laptop 1 {runId}-116` (cocok Search, tidak cocok Filter) tidak tampil
13. Verifikasi keyword tidak ter-reset: input Search tetap berisi `Wijaya`

### TC-GS-USER-732: Filter lalu Search menghasilkan irisan

14. Klik icon `(✕)` pada input Search, tekan Enter pada input kosong
15. Klik icon Filter
16. Klik `[Clear Field]`
17. Klik `[Apply]`
18. Klik icon Filter
19. Buka dropdown Brand, pilih opsi `Lenovo {runId}-116`
20. Klik `[Apply]`
21. Isi Search dengan `Wijaya`, tekan Enter
22. Verifikasi hasil = Filter ∩ Search: tabel hanya menampilkan 8 baris `Laptop 1` sampai `Laptop 8`
23. Verifikasi baris `Kamera 1 {runId}-116` (cocok Search, tidak cocok Filter) tidak tampil

### TC-GS-USER-733: Clear filter saat Search dan Sort aktif

24. Klik header Name
25. Klik icon Filter
26. Klik `[Clear Field]`
27. Klik `[Apply]`
28. Verifikasi keyword tetap aktif: input Search berisi `Wijaya`
29. Verifikasi arah sort tetap aktif: baris tabel terurut Name ascending A-Z
30. Verifikasi filter terlepas: baris `Kamera 1 {runId}-116` tampil
31. Klik header Name dua kali sampai kembali ke default sort tabel

### TC-GS-USER-734: Filter tetap tersedia untuk kolom yang di-hide

32. Klik icon `(✕)` pada input Search, tekan Enter pada input kosong
33. Klik icon Filter
34. Buka dropdown Brand, pilih opsi `Epson {runId}-116`
35. Klik `[Apply]`
36. Klik header kolom Column Visibility (⋯)
37. Hilangkan centang kolom `Brand` pada Overlay Column Visibility
38. Verifikasi filter tetap aktif menyaring: baris `Proyektor 1 {runId}-116` tampil
39. Verifikasi filter tetap aktif menyaring: baris `Laptop 1 {runId}-116` tidak tampil
40. Klik icon Filter
41. Verifikasi field `Brand` tetap ada di Filter Panel walau kolom `Brand` di-hide
42. Klik `[Clear Field]`
43. Klik `[Apply]`
44. Klik header kolom Column Visibility (⋯)
45. Centang kembali kolom `Brand` pada Overlay Column Visibility

### TC-GS-USER-735: Kombinasi Search dan Filter menghasilkan 0 baris lalu pulih saat filter dilepas

46. Isi Search dengan `Laptop`, tekan Enter
47. Verifikasi baris `Laptop 1 {runId}-116` tampil (hasil Search keyword A)
48. Klik icon Filter
49. Buka dropdown Brand, pilih opsi `Canon {runId}-116`
50. Klik `[Apply]`
51. Verifikasi teks `No results found` tampil (empty filtered state)
52. Verifikasi teks `Try adjusting your search or filter.` tampil
53. Klik icon Filter
54. Klik `[Clear Field]`
55. Klik `[Apply]`
56. Verifikasi baris `Laptop 1 {runId}-116` tampil kembali (hasil search)
57. Klik icon panah `(←)` untuk menutup Search dan mereset tabel
58. Pilih 10 baris per halaman pada Pagination

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (731 sampai 735) dipertahankan.
- Data target: TC sumber memakai `Ahmad Fauzi`; spec memakai `Joko Susilo` (Tabel Pre-setup No. 19) dengan populasi aset pinjaman milik spec (lebih dari satu halaman), sehingga asersi memakai nilai seed bersuffix.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (mencari user target di User List); langkah 5 (100 baris per halaman supaya seluruh baris seed berada di satu halaman); langkah 14, 32 (mengosongkan Search); langkah 15, 16, 17, 42, 43, 53, 54, 55 (mengosongkan Filter); langkah 31 (mengembalikan sort ke default); langkah 44, 45 (menampilkan kembali kolom Brand); langkah 57 (menutup Search); langkah 58 (memulihkan page size 10). Search yang masih terbuka dari TC sebelumnya dipakai ulang: "Isi Search dengan" untuk kotak terbuka dan kosong (bagian 8b butir 9).
- Prasyarat berantai dipenuhi di dalam spec: langkah "Terapkan filter lalu `[Clear Field]` + `[Apply]`" TC-GS-USER-733 memakai Filter Brand `Lenovo` yang sudah aktif dari TC-GS-USER-732 dan Search `Wijaya` yang sudah aktif; langkah "Search keyword, Enter" TC-GS-USER-733 dipenuhi Search yang masih aktif dari TC-GS-USER-732, dan langkah "Sort salah satu kolom" ditulis sebagai klik header Name.
- Asersi tambahan (S-03): `Verifikasi` hasil Search sebelum Filter di TC-GS-USER-731 dan 735 serta `Verifikasi` baris yang tersaring keluar adalah anchor positif bagi asersi absence (bagian 8b butir 2).
- Spec melewati sekitar 35 langkah (58 langkah) karena lima TC kombinasi satu kelas harness (fungsional, baca saja) berbagi satu layar dan satu dataset seed, serta saling berantai lewat state Search, Filter, dan Sort; memisahkannya mengulang login, seeding, dan pembukaan sub-tab.
- Pembagian TC lintas spec: TC-GS-USER-387, 388, 716 sampai 721 ada di spec 114; TC-GS-USER-722 sampai 730 (Filter Panel) ada di spec 115; TC-GS-USER-736, 737, 738, 753, 754 (Sort, Pagination, kombinasi lengkap) ada di spec 117; TC-GS-USER-739 sampai 747 ada di spec 118; TC-GS-USER-389 dan 748 sampai 752 ada di spec 119.
- Temuan untuk QA:
  - TC-GS-USER-731 sampai 735: TC menulis "keyword" dan "filter" tanpa nilai; spec memakai Search `Wijaya` (PIC `Andi W`, cocok nama lengkap) dan Filter Brand yang menghasilkan irisan tertentu.
  - TC-GS-USER-733: "Sort salah satu kolom" tidak menyebut kolom; spec memakai Name.
  - TC-GS-USER-734: "filter salah satu kolom" tidak menyebut kolom; spec memakai Brand. Aktifnya filter pada kolom hidden diasersi lewat isi tabel.
  - TC-GS-USER-735: "Filter yang tidak beririsan" tidak menyebut nilai; spec memakai Brand `Canon` terhadap Search `Laptop`.
  - Mekanisme menandai Guided Tooltip sebagai sudah dilihat dan seeding FAMS tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
