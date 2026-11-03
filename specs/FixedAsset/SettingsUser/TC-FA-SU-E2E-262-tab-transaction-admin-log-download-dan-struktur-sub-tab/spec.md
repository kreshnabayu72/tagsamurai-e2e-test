---
id: TC-FA-SU-E2E-262-tab-transaction-admin-log-download-dan-struktur-sub-tab
title: "Tab Transaction Admin Log: Download dan Struktur Sub-tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-790
  - TC-FA-SU-791
  - TC-FA-SU-797
coverage:
  web: automated
---

# Tab Transaction Admin Log: Download dan Struktur Sub-tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrowing & Assignment berisi 5 baris (`BRW-20260712-0311`, `BRW-20260713-0312`, `BRW-20260715-0313`, `BRW-20260716-0314`, `BRW-20260718-0315`) dengan nilai Group, Role, Action Taken, Date, dan Transaction Status per baris sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Kemampuan teknis (disediakan tim FE): menangkap berkas unduhan (nama, ekstensi, dan isi) di browser uji serta membaca isi CSV dan XLSX; berkas unduhan dibuang setelah spec.
- Kemampuan seed (disediakan tim FE): sub-tab Transfer milik Budi Santoso memuat sedikitnya satu baris supaya klik sel `Transaction ID` dapat dilakukan; Pre-setup #29 tidak menjamin hal itu (lihat Temuan untuk QA). Pengguna tanpa data transaksi: Hana Kusuma (Pre-setup #20); tidak ada Transaction Admin Log untuknya.

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrowing & Assignment

### TC-FA-SU-790: Download format CSV dan XLSX, nama file, dan tanpa toast sukses

2. Hover icon Download
3. Verifikasi tooltip `Download` tampil
4. Klik icon Download
5. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
6. Pilih `Download as CSV`
7. Verifikasi tidak ada toast sukses
8. Verifikasi file `Transaction-Admin-Log-Budi-Santoso-Borrowing-Assignment.csv` terunduh
9. Klik icon Download, lalu pilih `Download as XLSX`
10. Verifikasi tidak ada toast sukses
11. Verifikasi file `Transaction-Admin-Log-Budi-Santoso-Borrowing-Assignment.xlsx` terunduh
12. Buka berkas CSV dan XLSX yang terunduh
13. Verifikasi CSV berencoding UTF-8 dengan BOM
14. Verifikasi nilai ber-koma, tanda kutip, atau baris baru pada CSV dibungkus tanda kutip ganda
15. Verifikasi XLSX berisi satu sheet bernama `Sheet1`

### TC-FA-SU-791: Cakupan baris dan kolom Download (Search, Filter, Sort, dan Column Visibility)

16. Unduh CSV tanpa Search dan Filter aktif (icon Download, `Download as CSV`)
17. Verifikasi berkas CSV memuat kelima baris data (bukan hanya halaman aktif)
18. Verifikasi baris pada berkas CSV mengikuti urutan sort aktif (default Date descending)
19. Ketik Search `Approver`, tekan Enter
20. Klik icon Filter, buka dropdown `Group`, centang `Branch Surabaya`, lalu klik `[Apply]`
21. Unduh CSV (icon Download, `Download as CSV`)
22. Verifikasi berkas CSV hanya memuat baris yang cocok: `BRW-20260716-0314` (1 baris)
23. Klik header `⋯`, hilangkan centang `Role`, lalu tutup overlay dengan Esc
24. Unduh CSV (icon Download, `Download as CSV`)
25. Verifikasi kolom `Role` tidak ikut berkas CSV
26. Klik header `⋯`, beri centang `Role`, lalu tutup overlay dengan Esc
27. Unduh CSV (icon Download, `Download as CSV`)
28. Verifikasi tidak ada toast peringatan
29. Verifikasi kolom `Role` ikut kembali pada berkas CSV
30. Ganti isi kotak search dengan `zzzz`, tekan Enter
31. Unduh CSV (icon Download, `Download as CSV`)
32. Verifikasi tidak ada toast
33. Verifikasi berkas CSV hanya berisi baris header kolom yang visible tanpa baris data
34. Klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`
35. Klik `←` pada kotak Search

### TC-FA-SU-797: Struktur Sub-tab Transfer (Budi Santoso)

36. Klik Sub-tab Transfer
37. Verifikasi Sub-tab Transfer tampil pada switcher Tab Transaction Admin Log dengan urutan katalog Jenis Transaksi
38. Verifikasi Table Tools `Search`, `Filter`, dan `Download` tampil
39. Klik icon Search
40. Verifikasi placeholder Search `Search transaction ID, group, or role...` tampil
41. Klik `←` pada kotak Search
42. Verifikasi Table Tools tanpa icon Changelog dan tanpa aksi tulis
43. Verifikasi kolom berurutan `Transaction ID`, `Group`, `Role`, `Action Taken`, `Date`, `Transaction Status`
44. Klik sel `Transaction ID` pada baris pertama
45. Verifikasi klik `Transaction ID` tidak melakukan apa pun (halaman tetap dan tidak ada dialog)
46. Verifikasi header `Date` menunjukkan sort descending (↓) sebagai default sort
47. Klik icon Filter
48. Verifikasi panel Filter berisi field `Group`, `Role`, `Action Taken`, `Date`, dan `Transaction Status`
49. Klik icon Filter untuk menutup panel
50. Klik icon Download
51. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
52. Pilih `Download as CSV`
53. Verifikasi file `Transaction-Admin-Log-Budi-Santoso-Transfer.csv` terunduh
54. Klik Back breadcrumb ke User List, cari Hana Kusuma lewat Search, buka Detail User Hana Kusuma, lalu klik Tab Transaction Admin Log

### TC-FA-SU-797: Struktur Sub-tab Transfer (pengguna tanpa transaksi)

55. Klik Sub-tab Transfer
56. Verifikasi empty state `No transaction log yet` dengan deskripsi `Transactions this user has processed as PIC will appear here.` tampil
57. Ketik Search `zzzz`, tekan Enter
58. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
59. Kosongkan isi kotak search, tekan Enter

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pengosongan Search, penutupan overlay, panel Filter, dan perpindahan sub-tab; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Butir d TC-FA-SU-790 (BOM UTF-8, kutip ganda, dan sheet `Sheet1`) menyangkut isi berkas dan tergolong kelas f (binary buffer); butir itu diasersi di spec ini sesuai pembagian TC yang berlaku.
- TC-FA-SU-792 (transformasi data Download) ada di spec 373 dan TC-FA-SU-793 (Download gagal) ada di spec 368.
- Fixture sub-tab Borrowing & Assignment berisi lima baris dan satu halaman, sehingga "seluruh baris (bukan hanya halaman aktif)" pada TC-FA-SU-791 butir a diasersi sebagai kelima baris.
- Temuan untuk QA (S-15): (1) TC-FA-SU-790 butir d menyebut nilai ber-koma, tanda kutip, atau baris baru, tetapi seed #29 tidak memuat nilai demikian pada kolom yang terlihat; asersi dipertahankan sesuai TC dan data uji yang memuatnya disediakan tim FE. (2) TC-FA-SU-791 Langkah Uji nomor 3 tidak menyebut keyword dan filter; spec memakai Search `Approver` dan Filter Group `Branch Surabaya` (menyisakan `BRW-20260716-0314`) dan keyword `zzzz` untuk hasil kosong. (3) TC-FA-SU-791 butir a tidak menyebut sort aktif selain default; spec mengasersi default Date descending. (4) Klausa "klik Transaction ID tidak melakukan apa pun" pada TC-FA-SU-797 membutuhkan sedikitnya satu baris pada sub-tab Transfer yang tidak dijamin Pre-setup #29. (5) Expected "Search atau Filter tanpa hasil" pada TC-FA-SU-797 hanya diasersi lewat Search.
- Spec ini berjumlah 59 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
