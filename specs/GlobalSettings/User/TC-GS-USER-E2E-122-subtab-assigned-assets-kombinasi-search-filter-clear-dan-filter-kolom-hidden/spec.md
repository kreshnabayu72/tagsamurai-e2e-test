---
id: TC-GS-USER-E2E-122-subtab-assigned-assets-kombinasi-search-filter-clear-dan-filter-kolom-hidden
title: "Sub-tab Assigned Assets: Kombinasi Search dan Filter, Clear Filter, Filter Kolom Hidden, dan Nol Baris"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-769
  - TC-GS-USER-770
  - TC-GS-USER-771
  - TC-GS-USER-772
  - TC-GS-USER-773
coverage:
  web: automated
---

# Sub-tab Assigned Assets: Kombinasi Search dan Filter, Clear Filter, Filter Kolom Hidden, dan Nol Baris

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup user; hanya dataset Assigned Assets milik spec yang ditambahkan lalu dibersihkan.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`.
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22, hanya dibaca): Ahmad Fauzi (No. 13; Assigned Assets berisi K1).
- Data Dinamis, dataset Assigned Assets milik Ahmad Fauzi (27 baris; dengan page size 10 menjadi tiga halaman: 10, 10, 7 baris). K1 adalah data Pre-setup (hanya dibaca, tidak dihapus); K2 sampai K27 di-seed milik spec lewat kemampuan seeding data Responsibilities/FAMS (HK8) di hook `before` (disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Saat spec mulai, Assigned Assets Ahmad Fauzi hanya berisi K1 sampai K27. Transaction ID `ASG-{runId}-122-kk` dan Asset ID `AST-{runId}-122-kk` dengan kk = nomor K dua digit:
  - K1 (Pre-setup, literal dari TC-GS-USER-390): Transaction ID `ASG-20260505-0001`, Name `Company Vehicle B1234XY`, Asset ID `AST-0001`, Brand `Toyota`, Model / Type `Hilux`, PIC `Citra Wulandari`.
  - K2 sampai K4: Name `Company Vehicle V1 {runId}-122` sampai `Company Vehicle V3 {runId}-122`, Brand `Toyota`, Model / Type `Hilux`, PIC `Rudi Hartanto {runId}-122`.
  - K5 sampai K7: Name `Company Vehicle V4 {runId}-122` sampai `Company Vehicle V6 {runId}-122`, Brand `Honda`, Model / Type `Civic`, PIC `Sinta Dewi {runId}-122`.
  - K8 sampai K12: Name `Laptop L1 {runId}-122` sampai `Laptop L5 {runId}-122`, Brand `Dell`, Model / Type `Latitude 5440`, PIC `Bambang Susanto {runId}-122`.
  - K13 sampai K17: Name `Laptop L6 {runId}-122` sampai `Laptop L10 {runId}-122`, Brand `Lenovo`, Model / Type `ThinkPad T14`, PIC `Rudi Hartanto {runId}-122`.
  - K18 sampai K22: Name `Printer P1 {runId}-122` sampai `Printer P5 {runId}-122`, Brand `Canon`, Model / Type `PIXMA G3010`, PIC `Sinta Dewi {runId}-122`.
  - K23 sampai K27: Name `Printer P6 {runId}-122` sampai `Printer P10 {runId}-122`, Brand `Epson`, Model / Type `EcoTank L3250`, PIC `Bambang Susanto {runId}-122`.
  - Ringkasan: Name 27 nilai distinct; Brand 6 nilai (Toyota 4 baris, Honda 3, Dell 5, Lenovo 5, Canon 5, Epson 5); PIC 4 nilai (Citra Wulandari 1 baris, Rudi Hartanto 8, Sinta Dewi 8, Bambang Susanto 10); baris ber-Name memuat `Vehicle`: 7 (K1 sampai K7). Nilai distinct pada kolom yang di-sort, di-search, dan di-filter dipenuhi (S-11).
  - Nama literal tanpa suffix hanya K1 (Pre-setup); seluruh nilai Name, Transaction ID, Asset ID, dan PIC milik spec bersuffix `{runId}-122`. Nama Brand dan Model / Type adalah nilai master tanpa suffix.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus aset seed K2 sampai K27 lewat kemampuan seeding yang sama; data Pre-setup (K1 dan record user) tidak diubah. Seeding aset tidak mengubah record user Ahmad Fauzi.
- Data uji per TC: TC-GS-USER-769 keyword `Vehicle` dan Filter Brand `Toyota`; TC-GS-USER-770 Filter PIC `Sinta Dewi {runId}-122` dan keyword `Printer`; TC-GS-USER-771 Sort kolom Brand; TC-GS-USER-772 Filter Brand `Lenovo` dan kolom Brand di-hide; TC-GS-USER-773 keyword `Printer` dan Filter Brand `Toyota` (tidak beririsan dengan hasil search).
- Kemampuan teknis: seeding Assigned Assets (HK8) (disediakan tim FE/BE); membaca status gelap icon Filter dan indikator sort pada header.
- State yang diubah dan dipulihkan: Search (ditutup lewat `(←)`), Filter (dikosongkan lewat `[Clear Field]` dan `[Apply]`), Sort kolom Brand (dikembalikan ke default pada langkah 32 dan 33), dan visibilitas kolom `Brand` (dipulihkan pada langkah 48); hook `after` mengembalikan visibilitas kolom sub-tab Assigned Assets ke default sebagai cadangan. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik icon Search, ketik `Ahmad Fauzi`, tekan Enter
2. Klik Name `Ahmad Fauzi` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Assigned Assets`

### TC-GS-USER-769: Search lalu Filter menghasilkan irisan

5. Klik icon Search, ketik `Vehicle`, tekan Enter
6. Verifikasi tabel tersaring: 7 baris dengan Name memuat `Vehicle` (pembanding sebelum Filter)
7. Klik icon Filter
8. Pilih opsi `Toyota` pada dropdown Brand
9. Klik `[Apply]`
10. Verifikasi hasil = Search dan Filter: tepat 4 baris, yaitu `Company Vehicle B1234XY`, `Company Vehicle V1 {runId}-122`, `Company Vehicle V2 {runId}-122`, dan `Company Vehicle V3 {runId}-122`
11. Verifikasi keyword tidak ter-reset: kotak Search tetap berisi `Vehicle`

### TC-GS-USER-770: Filter lalu Search menghasilkan irisan

12. Klik icon panah `(←)` di kiri toolbar
13. Klik icon Filter
14. Klik `[Clear Field]`
15. Klik `[Apply]`
16. Klik icon Filter
17. Pilih opsi `Sinta Dewi {runId}-122` pada dropdown PIC
18. Klik `[Apply]`
19. Verifikasi tabel tersaring: 8 baris dengan PIC `Sinta Dewi {runId}-122` (pembanding sebelum Search)
20. Klik icon Search, ketik `Printer`, tekan Enter
21. Verifikasi hasil = Filter dan Search: tepat 5 baris, yaitu `Printer P1 {runId}-122` sampai `Printer P5 {runId}-122`
22. Verifikasi Filter tetap aktif: icon Filter berwarna gelap

### TC-GS-USER-771: Clear filter saat Search dan Sort aktif

23. Klik header Brand
24. Klik icon Filter
25. Klik `[Clear Field]`
26. Klik `[Apply]`
27. Verifikasi Filter terlepas: icon Filter tidak berwarna gelap
28. Verifikasi baris dengan PIC `Bambang Susanto {runId}-122` (`Printer P6 {runId}-122` sampai `Printer P10 {runId}-122`) tampil kembali
29. Verifikasi keyword tetap aktif: kotak Search berisi `Printer` dan 10 baris tampil dengan Name memuat `Printer`
30. Verifikasi arah sort tetap aktif: header Brand ascending dan baris terurut `Canon` (5 baris) lalu `Epson` (5 baris)

### TC-GS-USER-772: Filter tetap tersedia untuk kolom yang di-hide

31. Klik icon panah `(←)` di kiri toolbar
32. Klik header Brand
33. Klik header Brand
34. Klik icon Filter
35. Pilih opsi `Lenovo` pada dropdown Brand
36. Klik `[Apply]`
37. Verifikasi tabel tersaring: 5 baris dengan Brand `Lenovo`
38. Klik header kolom Actions (⋯)
39. Hilangkan centang kolom `Brand` pada Overlay Column Visibility
40. Tutup Overlay Column Visibility dengan menekan Esc
41. Verifikasi kolom `Brand` tidak tampil di tabel
42. Verifikasi Filter tetap aktif menyaring: tabel tetap menampilkan 5 baris `Laptop L6 {runId}-122` sampai `Laptop L10 {runId}-122`
43. Klik icon Filter
44. Verifikasi field `Brand` tetap ada di Filter Panel
45. Klik `[Clear Field]`
46. Klik `[Apply]`
47. Klik header kolom Actions (⋯)
48. Centang kembali kolom `Brand` pada Overlay Column Visibility
49. Tutup Overlay Column Visibility dengan menekan Esc

### TC-GS-USER-773: Kombinasi Search dan Filter menghasilkan 0 baris lalu pulih saat Filter dilepas

50. Klik icon Search, ketik `Printer`, tekan Enter
51. Verifikasi tabel menampilkan 10 baris dengan Name memuat `Printer` (pembanding sebelum Filter)
52. Klik icon Filter
53. Pilih opsi `Toyota` pada dropdown Brand
54. Klik `[Apply]`
55. Verifikasi empty filtered state: ilustrasi, `No results found`, dan `Try adjusting your search or filter.`
56. Klik icon Filter
57. Klik `[Clear Field]`
58. Klik `[Apply]`
59. Verifikasi baris hasil search tampil kembali: 10 baris dengan Name memuat `Printer`
60. Klik icon panah `(←)` di kiri toolbar

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Dataset 27 baris (lebih dari satu halaman) dipenuhi spec lewat seeding di hook `before`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (769 sampai 773) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 4 (pembukaan layar bersama untuk Ahmad Fauzi), langkah 12 beserta tiga langkah sesudahnya (menutup Search dan mengosongkan Filter dari TC-GS-USER-769 sebelum TC-GS-USER-770), langkah 31, 32, dan 33 (menutup Search dan mengembalikan Sort Brand ke default sebelum TC-GS-USER-772), tiga langkah pengosongan Filter dan dua langkah pemulihan kolom `Brand` di akhir TC-GS-USER-772, serta langkah terakhir (menutup Search).
- Anchor positif (bagian 8b butir 2): verifikasi 7 baris hasil Search `Vehicle` (TC-GS-USER-769), 8 baris hasil Filter PIC (TC-GS-USER-770), dan 10 baris hasil Search `Printer` (TC-GS-USER-773) mendahului asersi irisan dan empty filtered state pada surface yang sama. Verifikasi kolom `Brand` tidak tampil mendahului asersi Filter Panel pada kolom hidden (S-14).
- State dipakai ulang antar TC: langkah Uji 6 TC-GS-USER-771 (`Terapkan filter lalu [Clear Field] + [Apply]`) memakai Filter PIC `Sinta Dewi {runId}-122` dan Search `Printer` yang masih aktif dari TC-GS-USER-770; langkah pembersihnya adalah `[Clear Field]` + `[Apply]` yang dinilai Expected b.
- Spec melewati sekitar 35 langkah (60 langkah) karena lima TC berbagi satu layar, satu dataset 27 baris, dan satu kelas harness (fungsional); blok kombinasi saling melanjutkan state Search, Filter, dan Sort sehingga memisahkannya mengulang login, seeding, dan pembukaan layar yang sama.
- Pembagian TC lintas spec: TC-GS-USER-390, 391, 755 sampai 760 ada di spec 120; TC-GS-USER-761 sampai 768 (Filter Panel) ada di spec 121; TC-GS-USER-774, 775, 790, 791 ada di spec 123; TC-GS-USER-776 sampai 784 ada di spec 124; TC-GS-USER-392 dan 785 sampai 789 ada di spec 125.
- Temuan untuk QA:
  - TC-GS-USER-769 sampai 773: Data Uji kosong dan langkah menyebut `keyword` dan `filter` tanpa nilai; spec menetapkan keyword dan opsi filter dari dataset spec. TC-GS-USER-771 menyebut `Sort salah satu kolom`; spec memakai Brand.
  - TC-GS-USER-771: `Sort` diamati lewat indikator header dan urutan Brand pada 10 baris hasil; TC tidak menyebut kolom yang disort.
  - TC-GS-USER-772: kolom yang di-hide tidak disebut (`salah satu kolom`); spec memakai Brand, dan Expected b hanya menyebut field Brand ada di Filter Panel tanpa menyatakan opsi terpilih tetap tercentang.
  - Mekanisme menandai Guided Tooltip sebagai sudah dilihat dan menyiapkan data FAMS tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
