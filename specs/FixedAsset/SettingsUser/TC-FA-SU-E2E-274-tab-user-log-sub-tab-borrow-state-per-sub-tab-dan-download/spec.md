---
id: TC-FA-SU-E2E-274-tab-user-log-sub-tab-borrow-state-per-sub-tab-dan-download
title: "Tab User Log sub-tab Borrow: State per Sub-tab dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-831
  - TC-FA-SU-832
  - TC-FA-SU-837
coverage:
  web: automated
---

# Tab User Log sub-tab Borrow: State per Sub-tab dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso; sub-tab Borrow berisi 6 baris (`Borrowed` dan `Returned` untuk `BRW-20260205-0102`, `BRW-20260320-0188`, `BRW-20260615-0305`, `BRW-20260712-0347`) sesuai Tabel Data Uji Pre-setup TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface User Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Kemampuan teknis (disediakan tim FE): menangkap berkas unduhan (nama, ekstensi, dan isi) di browser uji serta membaca isi CSV dan XLSX; berkas unduhan dibuang setelah spec.
- Pre-setup untuk state sub-tab lain: sub-tab Assignment milik Budi Santoso (5 baris, Pre-setup #30) dipakai hanya sebagai tempat menerapkan kontrol berbeda; isinya tidak diasersi. Keyword `ASG` dipilih spec.

## Test Steps

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab User Log, lalu klik Sub-tab Borrow

### TC-FA-SU-831: Download format CSV dan XLSX, nama file, dan tanpa toast sukses

2. Hover icon Download
3. Verifikasi tooltip `Download` tampil
4. Klik icon Download
5. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
6. Pilih `Download as CSV`
7. Verifikasi tidak ada toast sukses
8. Verifikasi file `User-Log-Borrow-Budi-Santoso.csv` terunduh
9. Klik icon Download, lalu pilih `Download as XLSX`
10. Verifikasi tidak ada toast sukses
11. Verifikasi file `User-Log-Borrow-Budi-Santoso.xlsx` terunduh
12. Buka berkas CSV dan XLSX yang terunduh
13. Verifikasi CSV berencoding UTF-8 dengan BOM
14. Verifikasi nilai ber-koma, tanda kutip, atau baris baru pada CSV dibungkus tanda kutip ganda
15. Verifikasi XLSX berisi satu sheet bernama `Sheet1`

### TC-FA-SU-832: Cakupan baris dan kolom Download (Search, Filter, Sort, dan Column Visibility)

16. Unduh CSV tanpa Search dan Filter aktif (icon Download, `Download as CSV`)
17. Verifikasi berkas CSV memuat keenam baris data (bukan hanya halaman aktif)
18. Verifikasi baris pada berkas CSV mengikuti urutan sort aktif (default Date descending)
19. Ketik Search `Returned`, tekan Enter
20. Klik icon Filter, buka dropdown `PIC`, centang `Ahmad D`, lalu klik `[Apply]`
21. Unduh CSV (icon Download, `Download as CSV`)
22. Verifikasi berkas CSV hanya memuat baris yang cocok: `Returned|BRW-20260320-0188`, `Returned|BRW-20260205-0102` (2 baris)
23. Klik header `⋯`, hilangkan centang `Name`, lalu tutup overlay dengan Esc
24. Unduh CSV (icon Download, `Download as CSV`)
25. Verifikasi kolom `Name` tidak ikut berkas CSV
26. Klik header `⋯`, beri centang `Name`, lalu tutup overlay dengan Esc
27. Unduh CSV (icon Download, `Download as CSV`)
28. Verifikasi tidak ada toast peringatan
29. Verifikasi kolom `Name` ikut kembali pada berkas CSV
30. Ganti isi kotak search dengan `zzzz`, tekan Enter
31. Unduh CSV (icon Download, `Download as CSV`)
32. Verifikasi tidak ada toast
33. Verifikasi berkas CSV hanya berisi baris header kolom yang visible tanpa baris data
34. Klik `[Clear Field]` pada field `PIC`, lalu klik `[Apply]`
35. Klik `←` pada kotak Search

### TC-FA-SU-837: State sub-tab dipertahankan per sub-tab

36. Ketik Search `Returned`, tekan Enter
37. Klik icon Filter, buka dropdown `PIC`, centang `Ahmad D`, lalu klik `[Apply]`
38. Klik header `Date` satu kali
39. Ganti page size ke 25
40. Klik Sub-tab Assignment
41. Ketik Search `ASG`, klik header `Date` satu kali, lalu ganti page size ke 50
42. Klik Sub-tab Borrow
43. Verifikasi Search `Returned` tersimpan pada sub-tab Borrow
44. Verifikasi Filter `PIC` = `Ahmad D` tersimpan pada sub-tab Borrow
45. Verifikasi Sort pada kolom `Date` tersimpan pada sub-tab Borrow
46. Verifikasi page size 25 tersimpan pada sub-tab Borrow
47. Klik Sub-tab Assignment
48. Verifikasi state sub-tab Assignment (Search, Sort, dan page size 50) tidak dipengaruhi state sub-tab Borrow
49. Klik Sub-tab Borrow
50. Klik Back breadcrumb ke User List, lalu buka Detail User Budi Santoso, klik Tab User Log, dan klik Sub-tab Borrow
51. Verifikasi state sub-tab Borrow dipulihkan setelah Back breadcrumb (Search, Filter, Sort, dan page size 25)
52. Tekan F5 pada halaman Detail
53. Verifikasi state sub-tab Borrow dipulihkan setelah refresh F5 (Search, Filter, Sort, dan page size 25)
54. Klik menu Settings > User pada sidebar, lalu buka Detail User Budi Santoso, klik Tab User Log, dan klik Sub-tab Borrow
55. Verifikasi state sub-tab Borrow kembali ke default (Search kosong, tanpa Filter, sort default Date descending, page size 10)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pengosongan Search, penutupan overlay, dan perpindahan sub-tab; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Butir d TC-FA-SU-831 (BOM UTF-8, kutip ganda, dan sheet `Sheet1`) menyangkut isi berkas dan tergolong kelas f (binary buffer); butir itu diasersi di spec ini sesuai pembagian TC yang berlaku.
- TC-FA-SU-833 (transformasi data Download) ada di spec 373 dan TC-FA-SU-834 (Download gagal) ada di spec 368. Fixture sub-tab Borrow berisi enam baris dan satu halaman, sehingga "seluruh baris (bukan hanya halaman aktif)" pada TC-FA-SU-832 butir a diasersi sebagai keenam baris.
- Temuan untuk QA (S-15): (1) TC-FA-SU-831 butir d menyebut nilai ber-koma, tanda kutip, atau baris baru, tetapi seed #30 tidak memuat nilai demikian; asersi dipertahankan sesuai TC dan data uji yang memuatnya disediakan tim FE. (2) TC-FA-SU-832 Langkah Uji nomor 3 tidak menyebut keyword dan filter; spec memakai Search `Returned` dan Filter PIC `Ahmad D` (menyisakan `Returned|BRW-20260320-0188`, `Returned|BRW-20260205-0102`) dan keyword `zzzz` untuk hasil kosong. (3) TC-FA-SU-837 Langkah Uji nomor 2 tidak menyebut sub-tab lain; spec memakai Sub-tab Assignment dan keyword `ASG`. (4) TC-FA-SU-837 Langkah Uji nomor 5 tidak menyebut sub-tab aktif sesudah F5; spec mengasersi state sub-tab Borrow sesuai Expected c. (5) Nomor halaman aktif tidak diasersi (fixture satu halaman, butir a TC-FA-SU-837).
- Spec ini berjumlah 55 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
