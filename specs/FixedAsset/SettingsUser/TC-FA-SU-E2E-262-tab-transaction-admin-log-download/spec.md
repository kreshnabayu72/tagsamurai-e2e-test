---
id: TC-FA-SU-E2E-262-tab-transaction-admin-log-download
title: "Tab Transaction Admin Log: Download Sub-tab Borrow"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-790
  - TC-FA-SU-791
coverage:
  web: automated
---

# Tab Transaction Admin Log: Download Sub-tab Borrow

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Borrow berisi 5 baris (`BRW-2026-0315`, `BRW-2026-0314`, `BRW-2026-0313`, `BRW-2026-0312`, dan satu baris Draft dengan Transaction ID `—`) dengan nilai Date, Activity, Name, Borrower, dan Group per baris sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Kemampuan teknis (disediakan tim FE): tombol keyboard `Esc`, hover, dan muat ulang halaman (`F5`).
- Kemampuan teknis (disediakan tim FE): menangkap berkas unduhan (nama, ekstensi, dan isi) di browser uji serta membaca isi CSV (encoding, BOM, pembungkus tanda kutip) dan XLSX (nama sheet, kolom, baris); berkas unduhan dibuang setelah spec.
- Perubahan tampilan yang dipulihkan di dalam spec: visibilitas kolom `Borrower` (di-hide lalu di-unhide lewat overlay Column Visibility), filter Group, dan Search.

## Test Steps

### TC-FA-SU-790: Download format CSV dan XLSX, nama file, dan tanpa toast sukses

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Borrow
2. Hover icon Download
3. Verifikasi tooltip `Download` tampil
4. Klik icon Download
5. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
6. Pilih `Download as CSV`
7. Verifikasi tidak ada toast sukses
8. Verifikasi file `Transaction-Admin-Log-Budi-Santoso-Borrow.csv` terunduh
9. Klik icon Download, lalu pilih `Download as XLSX`
10. Verifikasi tidak ada toast sukses
11. Verifikasi file `Transaction-Admin-Log-Budi-Santoso-Borrow.xlsx` terunduh
12. Buka berkas CSV
13. Verifikasi berkas CSV berencoding UTF-8 dengan BOM
14. Verifikasi nilai yang memuat koma, tanda kutip, atau baris baru pada berkas CSV dibungkus tanda kutip ganda
15. Buka berkas XLSX
16. Verifikasi berkas XLSX memuat satu sheet bernama `Sheet1`

### TC-FA-SU-791: Cakupan baris dan kolom Download: Search, Filter, Sort, dan Column Visibility

17. Klik icon Download, lalu pilih `Download as CSV`
18. Verifikasi berkas memuat seluruh 5 baris data
19. Verifikasi baris berkas mengikuti urutan sort aktif (Date terbaru lebih dulu)
20. Ketik Search `Projector`, tekan Enter
21. Klik icon Filter
22. Buka dropdown Group lalu centang `Branch Surabaya`
23. Klik `[Apply]`
24. Klik icon Download, lalu pilih `Download as CSV`
25. Verifikasi berkas hanya memuat baris `BRW-2026-0314` (1 baris data)
26. Klik `[Clear Field]`, lalu klik `[Apply]`
27. Klik `←` pada kotak Search
28. Klik icon Filter untuk menutup panel
29. Klik header kolom `⋯`, hilangkan centang `Borrower`, lalu tekan `Esc`
30. Klik icon Download, lalu pilih `Download as CSV`
31. Verifikasi berkas memuat kolom `Date`, `Activity`, `Transaction ID`, `Name`, dan `Group`
32. Verifikasi berkas tidak memuat kolom `Borrower`
33. Verifikasi tidak ada toast peringatan
34. Klik header kolom `⋯`, centang kembali `Borrower`, lalu tekan `Esc`
35. Klik icon Download, lalu pilih `Download as CSV`
36. Verifikasi berkas memuat kembali kolom `Borrower`
37. Ketik Search `zzzz`, tekan Enter
38. Verifikasi tabel menampilkan `No results found`
39. Klik icon Download, lalu pilih `Download as CSV`
40. Verifikasi berkas hanya memuat baris header kolom yang visible tanpa baris data
41. Verifikasi tidak ada toast
42. Klik `←` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pembukaan berkas unduhan, `Esc` pada overlay Column Visibility, serta pemulihan Search, Filter, dan visibilitas kolom (`[Clear Field]` lalu `[Apply]`, klik `←`, penutupan panel Filter, centang kembali `Borrower`) dalam blok TC-FA-SU-791 (S-09, bagian 8b butir 14).
- P-10: TC-FA-SU-790 butir d (encoding UTF-8 dengan BOM, pembungkus tanda kutip ganda, sheet `Sheet1`) adalah klausa isi berkas (kelas f) pada alur unduh yang sama dengan butir a sampai c, sehingga tidak dapat dipisah dari asersi UI; klausa itu ditulis sesudah seluruh klausa UI TC itu (langkah 13 sampai 16), satu `Verifikasi` per klausa.
- Pembagian TC lintas spec: transformasi data per tipe kolom Download Borrow (TC-FA-SU-792) ada di spec 373; kegagalan Download Borrow (TC-FA-SU-793) ada di spec 368.
- Pilihan spec: Search `Projector` dengan Filter Group `Branch Surabaya` (irisan `BRW-2026-0314`), kolom `Borrower` sebagai kolom yang di-hide, dan keyword tanpa hasil `zzzz`; TC-FA-SU-791 tidak menyebut nilainya. Search dan Filter dibersihkan sebelum langkah berikutnya bergantung pada tabel penuh.
- Temuan untuk QA (S-15): (1) TC-FA-SU-790 dan TC-FA-SU-791 menulis ACC `#20; Role Total Control`; `#20` adalah Client `FaUserMain`, bukan akun. Aktor memakai Total Control Lina Marlina (#1) dari hook suite. (2) TC-FA-SU-790 butir d dan TC-FA-SU-791 butir a menyebut nilai ber-koma/kutip/baris baru dan "bukan hanya halaman aktif", tetapi Pre-setup #29 (5 baris, satu halaman, tanpa koma atau tanda kutip pada nilai) tidak memuat data yang menguji keduanya; asersi yang bersangkutan tidak dapat gagal pada data ini. (3) TC-FA-SU-791 butir b menyebut Search dan Filter tanpa nilai; spec memilih nilai sendiri. (4) Post Condition tidak ada.
- Spec ini berjumlah 42 langkah (dihitung dengan ekspansi langkah berulang) dan di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional baca) pada satu surface yang sama dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01) dan dari empat unduhan berbeda pada TC-FA-SU-791, bukan dari langkah tambahan.
