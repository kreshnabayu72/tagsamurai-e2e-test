---
id: TC-FA-SU-E2E-465-tab-transaction-admin-log-assignment-download-csv-xlsx-dan-cakupan-baris-kolom
title: "Tab Transaction Admin Log Sub-tab Assignment: Download CSV dan XLSX dan Cakupan Baris dan Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1167
  - TC-FA-SU-1168
coverage:
  web: automated
---

# Tab Transaction Admin Log Sub-tab Assignment: Download CSV dan XLSX dan Cakupan Baris dan Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Assignment berisi 4 baris (`ASG-20260720-0071`, `ASG-20260719-0070`, `ASG-20260717-0069`, `ASG-20260715-0068`) dengan nilai Date, Activity, Name, Assignee (satu baris dengan Assignee Division `General Affairs`), dan Group per baris sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Kemampuan teknis (disediakan tim FE): menangkap berkas unduhan (nama, ekstensi, dan isi) di browser uji serta membaca isi CSV dan XLSX; berkas unduhan dibuang setelah spec.

## Test Steps

### TC-FA-SU-1167: Download format CSV dan XLSX, nama file, dan tanpa toast sukses

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Assignment
2. Hover icon Download
3. Verifikasi tooltip `Download` tampil
4. Klik icon Download
5. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
6. Pilih `Download as CSV`
7. Verifikasi tidak ada toast sukses
8. Verifikasi file `Transaction-Admin-Log-Budi-Santoso-Assignment.csv` terunduh
9. Klik icon Download, lalu pilih `Download as XLSX`
10. Verifikasi tidak ada toast sukses
11. Verifikasi file `Transaction-Admin-Log-Budi-Santoso-Assignment.xlsx` terunduh
12. Buka berkas CSV dan XLSX yang terunduh
13. Verifikasi CSV berencoding UTF-8 dengan BOM
14. Verifikasi nilai ber-koma, tanda kutip, atau baris baru pada CSV dibungkus tanda kutip ganda
15. Verifikasi XLSX berisi satu sheet bernama `Sheet1`

### TC-FA-SU-1168: Cakupan baris dan kolom Download (Search, Filter, Sort, dan Column Visibility)

16. Unduh CSV tanpa Search dan Filter aktif (icon Download, `Download as CSV`)
17. Verifikasi berkas CSV memuat keempat baris data (bukan hanya halaman aktif)
18. Verifikasi baris pada berkas CSV mengikuti urutan sort aktif (default Date descending)
19. Klik icon Search, ketik Search `Laptop`, tekan Enter
20. Klik icon Filter, buka dropdown `Group`, centang `Branch Surabaya`, lalu klik `[Apply]`
21. Unduh CSV (icon Download, `Download as CSV`)
22. Verifikasi berkas CSV hanya memuat baris yang cocok: `ASG-20260720-0071` (1 baris)
23. Klik header `⋯`, hilangkan centang `Assignee`, lalu tutup overlay dengan Esc
24. Unduh CSV (icon Download, `Download as CSV`)
25. Verifikasi kolom `Assignee` tidak ikut berkas CSV
26. Klik header `⋯`, beri centang `Assignee`, lalu tutup overlay dengan Esc
27. Unduh CSV (icon Download, `Download as CSV`)
28. Verifikasi tidak ada toast peringatan
29. Verifikasi kolom `Assignee` ikut kembali pada berkas CSV
30. Ganti isi kotak search dengan `zzzz`, tekan Enter
31. Unduh CSV (icon Download, `Download as CSV`)
32. Verifikasi tidak ada toast
33. Verifikasi berkas CSV hanya berisi baris header kolom yang visible tanpa baris data
34. Klik `[Clear Field]` pada field `Group`, lalu klik `[Apply]`
35. Klik `←` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pembukaan icon Search dan Filter, pengosongan Search, `[Clear Field]`, serta hide dan unhide kolom; semuanya hanya mengembalikan state (S-09).
- `P-10`: butir d TC-FA-SU-1167 (BOM UTF-8, kutip ganda, dan sheet `Sheet1`) menyangkut isi berkas (kelas f, binary buffer) dan diasersi di spec ini setelah seluruh klausa UI TC itu, satu `Verifikasi` per klausa; alur unduh tidak dapat dipisah dari asersi UI nama berkas dan ketiadaan toast.
- Pembagian TC lintas spec: transformasi data Download TC-FA-SU-1169 ada di spec 373; Download gagal TC-FA-SU-1170 ada di spec 368; empty state, loading, dan error load TC-FA-SU-1172 ada di spec 364.
- Fixture sub-tab Assignment berisi empat baris dan satu halaman, sehingga "seluruh baris (bukan hanya halaman aktif)" pada TC-FA-SU-1168 butir a diasersi sebagai keempat baris.
- Temuan untuk QA (S-15): (1) TC-FA-SU-1167 butir d menyebut nilai ber-koma, tanda kutip, atau baris baru, tetapi seed #29 tidak memuat nilai demikian pada kolom yang terlihat; asersi dipertahankan sesuai TC dan data uji yang memuatnya disediakan tim FE. (2) TC-FA-SU-1168 Langkah Uji nomor 3 tidak menyebut keyword dan filter; spec memakai Search `Laptop` dan Filter Group `Branch Surabaya` (menyisakan `ASG-20260720-0071`) dan keyword `zzzz` untuk hasil kosong. (3) TC-FA-SU-1168 butir a tidak menyebut sort aktif selain default; spec mengasersi default Date descending.
