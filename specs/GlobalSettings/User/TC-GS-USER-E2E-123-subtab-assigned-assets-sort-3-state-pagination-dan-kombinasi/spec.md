---
id: TC-GS-USER-E2E-123-subtab-assigned-assets-sort-3-state-pagination-dan-kombinasi
title: "Sub-tab Assigned Assets: Sort 3-State, Pagination, dan Kombinasi Search, Filter, Sort, Pagination"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-774
  - TC-GS-USER-775
  - TC-GS-USER-790
  - TC-GS-USER-791
coverage:
  web: automated
---

# Sub-tab Assigned Assets: Sort 3-State, Pagination, dan Kombinasi Search, Filter, Sort, Pagination

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Pre-setup user; hanya dataset Assigned Assets milik spec yang ditambahkan lalu dibersihkan.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login dan navigasi ke Global Settings > User > User List (sub-tab Login User) dilakukan sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`.
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22, hanya dibaca): Ahmad Fauzi (No. 13; Assigned Assets berisi K1).
- Data Dinamis, dataset Assigned Assets milik Ahmad Fauzi (27 baris; dengan page size 10 menjadi tiga halaman: 10, 10, 7 baris). K1 adalah data Pre-setup (hanya dibaca, tidak dihapus); K2 sampai K27 di-seed milik spec lewat kemampuan seeding data Responsibilities/FAMS (HK8) di hook `before` (disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). Saat spec mulai, Assigned Assets Ahmad Fauzi hanya berisi K1 sampai K27. Transaction ID `ASG-{runId}-123-kk` dan Asset ID `AST-{runId}-123-kk` dengan kk = nomor K dua digit:
  - K1 (Pre-setup, literal dari TC-GS-USER-390): Transaction ID `ASG-20260505-0001`, Name `Company Vehicle B1234XY`, Asset ID `AST-0001`, Brand `Toyota`, Model / Type `Hilux`, PIC `Citra Wulandari`.
  - K2 sampai K4: Name `Company Vehicle V1 {runId}-123` sampai `Company Vehicle V3 {runId}-123`, Brand `Toyota`, Model / Type `Hilux`, PIC `Rudi Hartanto {runId}-123`.
  - K5 sampai K7: Name `Company Vehicle V4 {runId}-123` sampai `Company Vehicle V6 {runId}-123`, Brand `Honda`, Model / Type `Civic`, PIC `Sinta Dewi {runId}-123`.
  - K8 sampai K12: Name `Laptop L1 {runId}-123` sampai `Laptop L5 {runId}-123`, Brand `Dell`, Model / Type `Latitude 5440`, PIC `Bambang Susanto {runId}-123`.
  - K13 sampai K17: Name `Laptop L6 {runId}-123` sampai `Laptop L10 {runId}-123`, Brand `Lenovo`, Model / Type `ThinkPad T14`, PIC `Rudi Hartanto {runId}-123`.
  - K18 sampai K22: Name `Printer P1 {runId}-123` sampai `Printer P5 {runId}-123`, Brand `Canon`, Model / Type `PIXMA G3010`, PIC `Sinta Dewi {runId}-123`.
  - K23 sampai K27: Name `Printer P6 {runId}-123` sampai `Printer P10 {runId}-123`, Brand `Epson`, Model / Type `EcoTank L3250`, PIC `Bambang Susanto {runId}-123`.
  - Ringkasan: Name 27 nilai distinct; Brand 6 nilai (Toyota 4 baris, Honda 3, Dell 5, Lenovo 5, Canon 5, Epson 5); PIC 4 nilai (Citra Wulandari 1 baris, Rudi Hartanto 8, Sinta Dewi 8, Bambang Susanto 10); baris ber-Name memuat `Vehicle`: 7 (K1 sampai K7). Nilai distinct pada kolom yang di-sort, di-search, dan di-filter dipenuhi (S-11).
  - Nama literal tanpa suffix hanya K1 (Pre-setup); seluruh nilai Name, Transaction ID, Asset ID, dan PIC milik spec bersuffix `{runId}-123`. Nama Brand dan Model / Type adalah nilai master tanpa suffix.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus aset seed K2 sampai K27 lewat kemampuan seeding yang sama; data Pre-setup (K1 dan record user) tidak diubah. Seeding aset tidak mengubah record user Ahmad Fauzi.
- Data uji per TC: TC-GS-USER-774 enam kolom kelas teks (Transaction ID, Name, Asset ID, Brand, Model / Type, PIC); TC-GS-USER-790 page size 25 dan 10 (27 baris, lebih dari 21 baris); TC-GS-USER-791 keyword `{runId}-123` (mencocokkan K2 sampai K27), Filter PIC `Bambang Susanto {runId}-123` dan `Sinta Dewi {runId}-123` (18 baris), Sort Brand descending, page size 25.
- Urutan yang diasersi: nilai Transaction ID dan Asset ID memuat `{runId}-123` (runId tidak berformat tetap), sehingga urutan kolom itu diasersi sebagai terurut ascending atau descending tanpa menyebut baris tertentu; kolom Name, Brand, Model / Type, dan PIC diasersi dengan komposisi baris yang tetap.
- Kemampuan teknis: seeding Assigned Assets (HK8) (disediakan tim FE/BE); membaca indikator sort pada header dan nilai kolom 10 baris halaman 1; mengubah page size lewat Pagination; mengetik nomor halaman.
- State yang diubah dan dipulihkan: Sort kembali ke default (klik ketiga tiap kolom), Search, Filter, dan page size (dikembalikan pada langkah 71 sampai 76); hook `after` sebagai cadangan. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik icon Search, ketik `Ahmad Fauzi`, tekan Enter
2. Klik Name `Ahmad Fauzi` di User List
3. Klik Tab `Responsibilities`
4. Klik sub-tab `Assigned Assets`

### TC-GS-USER-775: Kolom non-sortable tidak punya ikon sort

5. Verifikasi header Name menampilkan indikator sort aktif A-Z (pembanding kolom sortable)
6. Arahkan kursor ke header Photo
7. Verifikasi header Photo tanpa ikon sort
8. Klik header Photo
9. Verifikasi urutan tidak berubah: 10 baris halaman 1 tetap terurut Name A-Z dengan baris pertama `Company Vehicle B1234XY`

### TC-GS-USER-774: Sort 3-state kolom kelas teks A-Z

10. Klik header Transaction ID
11. Verifikasi klik 1: 10 baris halaman 1 terurut ascending (A-Z) menurut Transaction ID
12. Klik header Transaction ID
13. Verifikasi klik 2: 10 baris halaman 1 terurut descending (Z-A) menurut Transaction ID
14. Klik header Transaction ID
15. Verifikasi klik 3 kembali ke default sort tabel: 10 baris halaman 1 terurut Name A-Z dengan baris pertama `Company Vehicle B1234XY`
16. Klik header Name
17. Verifikasi klik 1: 10 baris halaman 1 terurut ascending (A-Z) menurut Name dengan baris pertama `Company Vehicle B1234XY`
18. Klik header Name
19. Verifikasi klik 2: 10 baris halaman 1 terurut descending (Z-A) menurut Name dengan baris pertama `Printer P9 {runId}-123`
20. Klik header Name
21. Verifikasi klik 3 kembali ke default sort tabel: 10 baris halaman 1 terurut Name A-Z dengan baris pertama `Company Vehicle B1234XY`
22. Klik header Asset ID
23. Verifikasi klik 1: 10 baris halaman 1 terurut ascending (A-Z) menurut Asset ID
24. Klik header Asset ID
25. Verifikasi klik 2: 10 baris halaman 1 terurut descending (Z-A) menurut Asset ID
26. Klik header Asset ID
27. Verifikasi klik 3 kembali ke default sort tabel: 10 baris halaman 1 terurut Name A-Z dengan baris pertama `Company Vehicle B1234XY`
28. Klik header Brand
29. Verifikasi klik 1: halaman 1 terurut ascending (A-Z) menurut Brand: `Canon` (5 baris) lalu `Dell` (5 baris)
30. Klik header Brand
31. Verifikasi klik 2: halaman 1 terurut descending (Z-A) menurut Brand: `Toyota` (4 baris), `Lenovo` (5 baris), lalu `Honda` (1 baris)
32. Klik header Brand
33. Verifikasi klik 3 kembali ke default sort tabel: 10 baris halaman 1 terurut Name A-Z dengan baris pertama `Company Vehicle B1234XY`
34. Klik header Model / Type
35. Verifikasi klik 1: halaman 1 terurut ascending (A-Z) menurut Model / Type: `Civic` (3 baris), `EcoTank L3250` (5 baris), lalu `Hilux` (2 baris)
36. Klik header Model / Type
37. Verifikasi klik 2: halaman 1 terurut descending (Z-A) menurut Model / Type: `ThinkPad T14` (5 baris) lalu `PIXMA G3010` (5 baris)
38. Klik header Model / Type
39. Verifikasi klik 3 kembali ke default sort tabel: 10 baris halaman 1 terurut Name A-Z dengan baris pertama `Company Vehicle B1234XY`
40. Klik header PIC
41. Verifikasi klik 1: halaman 1 terurut ascending (A-Z) menurut PIC: 10 baris `Bambang Susanto {runId}-123`
42. Klik header PIC
43. Verifikasi klik 2: halaman 1 terurut descending (Z-A) menurut PIC: `Sinta Dewi {runId}-123` (8 baris) lalu `Rudi Hartanto {runId}-123` (2 baris)
44. Klik header PIC
45. Verifikasi klik 3 kembali ke default sort tabel: 10 baris halaman 1 terurut Name A-Z dengan baris pertama `Company Vehicle B1234XY`

### TC-GS-USER-790: Pagination ubah page size dan input nomor halaman

46. Ubah page size ke 25 lewat pilihan jumlah baris per halaman pada Pagination
47. Verifikasi tabel menampilkan 25 baris (maksimal 25, dari 27 baris data)
48. Ubah page size kembali ke 10
49. Verifikasi tabel menampilkan 10 baris pada halaman 1 dari 3 halaman
50. Ketik `2` pada input nomor halaman, tekan Enter
51. Verifikasi tabel langsung berpindah ke halaman 2 (10 baris)
52. Klik tombol next
53. Verifikasi tabel berpindah ke halaman 3 (7 baris)
54. Klik tombol prev
55. Verifikasi tabel berpindah kembali ke halaman 2 (10 baris)

### TC-GS-USER-791: Kombinasi Search, Filter, Sort, dan Pagination berjalan bersamaan

56. Klik icon Search, ketik `{runId}-123`, tekan Enter
57. Verifikasi hasil Search: 26 baris dalam 3 halaman (K1 tidak tercakup)
58. Klik icon Filter
59. Pilih opsi `Bambang Susanto {runId}-123` pada dropdown PIC
60. Pilih opsi `Sinta Dewi {runId}-123` pada dropdown PIC
61. Klik `[Apply]`
62. Verifikasi hasil Search dan Filter: 18 baris dalam 2 halaman
63. Klik header Brand
64. Klik header Brand
65. Verifikasi halaman 1 terurut descending (Z-A) menurut Brand: `Honda` (3 baris), `Epson` (5 baris), lalu `Dell` (2 baris)
66. Ubah page size ke 25
67. Verifikasi kotak Search tetap berisi `{runId}-123`
68. Verifikasi Filter tetap aktif: icon Filter berwarna gelap
69. Verifikasi header Brand tetap descending (Z-A)
70. Verifikasi 18 baris tampil dalam satu halaman terurut Brand descending: `Honda` (3 baris), `Epson` (5 baris), `Dell` (5 baris), lalu `Canon` (5 baris)
71. Klik icon panah `(←)` di kiri toolbar
72. Klik icon Filter
73. Klik `[Clear Field]`
74. Klik `[Apply]`
75. Klik header Brand
76. Ubah page size kembali ke 10

## Notes

- Sumber TC: `global-settings/user/TestCases/tc-user.md`. Mode: FE+BE. Dataset 27 baris (lebih dari 21 baris) dipenuhi spec lewat seeding di hook `before`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 775, 774, 790, 791. TC-GS-USER-775 (Negative, tanpa aksi pengubah state) ditaruh di awal mengikuti prinsip screening di awal; urutan di `tc-user.md`: 774, 775, 790, 791.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 sampai 4 (pembukaan layar bersama untuk Ahmad Fauzi), klik header ketiga tiap kolom pada TC-GS-USER-774 (mengembalikan sort ke default; hasilnya tetap diasersi), langkah 71 sampai 76 (menutup Search, mengosongkan Filter, mengembalikan Sort dan page size), serta pengembalian page size ke 10 di TC-GS-USER-790 (langkah Uji 5).
- Anchor positif (bagian 8b butir 2): verifikasi indikator sort pada header Name mendahului asersi ketiadaan ikon sort pada header Photo (TC-GS-USER-775).
- Spec melewati sekitar 35 langkah (76 langkah) karena TC-GS-USER-774 menguji enam kolom dengan blok identik (klik 3 kali, amati tiap klik) ditambah tiga TC yang berbagi satu layar, satu dataset 27 baris, dan satu kelas harness (fungsional). Tiap blok kolom berdiri sendiri dan kembali ke default sort; TC-GS-USER-791 memakai Search, Filter, Sort, dan page size yang dibentuk berurutan, sehingga memisahkannya mengulang login, seeding, dan pembukaan layar yang sama.
- Pembagian TC lintas spec: TC-GS-USER-390, 391, 755 sampai 760 ada di spec 120; TC-GS-USER-761 sampai 768 ada di spec 121; TC-GS-USER-769 sampai 773 ada di spec 122; TC-GS-USER-776 sampai 784 ada di spec 124; TC-GS-USER-392 dan 785 sampai 789 ada di spec 125.
- Temuan untuk QA:
  - TC-GS-USER-774: `default sort tabel` adalah Name A-Z (TC-GS-USER-390 butir b), sehingga klik 1 dan klik 3 pada kolom Name menghasilkan urutan yang sama; keduanya dibedakan lewat langkah klik yang bernomor. Urutan antar baris bernilai sama (tie) tidak ditentukan TC, sehingga hanya komposisi nilai per halaman yang diasersi.
  - TC-GS-USER-775: Expected `tanpa ikon sort` tidak menyebut cara pembedaannya; spec membandingkan dengan indikator pada header kolom sortable.
  - TC-GS-USER-790: Expected `Next/prev berpindah halaman` tidak menyebut halaman tujuan; spec memakai halaman 3 lalu halaman 2 (dari halaman 2 hasil input).
  - TC-GS-USER-791: Data Uji `Terapkan filter bila tersedia` bersyarat; Filter Panel tersedia (TC-GS-USER-761), sehingga spec menerapkannya. Keyword, filter, dan kolom sort tidak disebut; spec menetapkan `{runId}-123`, PIC, dan Brand.
  - Mekanisme menandai Guided Tooltip sebagai sudah dilihat dan menyiapkan data FAMS tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
