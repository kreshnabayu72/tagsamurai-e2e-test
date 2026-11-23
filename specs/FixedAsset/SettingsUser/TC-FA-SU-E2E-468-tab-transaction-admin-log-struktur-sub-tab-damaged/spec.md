---
id: TC-FA-SU-E2E-468-tab-transaction-admin-log-struktur-sub-tab-damaged
title: "Tab Transaction Admin Log: Struktur Sub-tab Damaged"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1174
coverage:
  web: automated
---

# Tab Transaction Admin Log: Struktur Sub-tab Damaged

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan Transaction Admin Log (#29). Pengguna target: Budi Santoso; sub-tab Damaged berisi 4 baris (Name `Laptop Dell Latitude - 9` Source `Manual` Group `IT Infrastructure`, Name `Projector Epson - 2` Source `Borrowed asset` Group `General Affairs`, Name `Tablet Samsung Tab - 5` Source `Reported by scan` Group `Logistics Warehouse`, Name `Camera Sony A7 - 4` Source `Transfer receive` Group `Finance & Accounting`) dengan nilai Date, Activity, Source, dan Group per baris (Source = Source record, sama untuk setiap baris record itu; Group = grup aset saat tindakan dieksekusi) sesuai Pre-setup #29 TC. Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE). Spec ini hanya membaca surface Transaction Admin Log dan tidak menambah atau mengubah data Pre-setup.
- Spec bersifat baca saja pada data bersama (tanpa mutasi); state yang diubah hanya filter, sort, Search, dan preferensi tampilan sisi klien.
- Kemampuan teknis (disediakan tim FE): menangkap berkas unduhan (nama, ekstensi, dan isi) di browser uji serta membaca isi CSV dan XLSX; berkas unduhan dibuang setelah spec.
- Pengguna tanpa data transaksi: Hana Kusuma (Pre-setup #20); tidak ada Transaction Admin Log untuknya.

## Test Steps

### TC-FA-SU-1174: Struktur Sub-tab Damaged (Budi Santoso)

1. Cari Budi Santoso lewat Search di User List, buka Detail User Budi Santoso, klik Tab Transaction Admin Log, lalu klik Sub-tab Damaged
2. Verifikasi Sub-tab Damaged tampil pada switcher Tab Transaction Admin Log di posisi keempat, setelah `Transfer` dan sebelum `Missing`
3. Verifikasi Table Tools `Search`, `Filter`, dan `Download` tampil
4. Klik icon Search
5. Verifikasi placeholder Search `Search activity, asset name, source, or group...` tampil
6. Klik `←` pada kotak Search
7. Verifikasi Table Tools tanpa icon Changelog dan tanpa aksi tulis
8. Verifikasi kolom berurutan `Date`, `Activity`, `Name`, `Source`, `Group`, dan header `⋯` (Column Visibility)
9. Verifikasi kolom `Date`, `Name`, `Source`, dan `Group` sortable (memiliki icon sort)
10. Verifikasi kolom `Activity` unsortable (tanpa icon sort)
11. Verifikasi kolom `Transaction ID`, `Role`, dan `Transaction Status` tidak ada (aset tidak memiliki nomor transaksi)
12. Verifikasi Activity dan Source tampil sebagai teks biasa tanpa badge berwarna
13. Verifikasi kolom `Source` berada di antara kolom `Name` dan `Group`
14. Verifikasi Group tampil sebagai badge
15. Hover badge Group pada baris pertama
16. Verifikasi hover menampilkan hierarki lengkap `[Parent] > [Child]` untuk grup `IT Infrastructure`
17. Verifikasi default sort Date newest first: `22/07/26` `Marked as repaired` `Laptop Dell Latitude - 9` `Manual` `IT Infrastructure`; `20/07/26` `Report confirmed` `Projector Epson - 2` `Borrowed asset` `General Affairs`; `16/07/26` `Reported damaged` `Tablet Samsung Tab - 5` `Reported by scan` `Logistics Warehouse`; `14/07/26` `Report rejected` `Camera Sony A7 - 4` `Transfer receive` `Finance & Accounting`
18. Klik icon Filter
19. Verifikasi field `Date` berupa date range picker dengan placeholder `Select date`
20. Verifikasi field `Activity` berupa multi-select searchable dengan placeholder `All activities`
21. Verifikasi field `Name` berupa multi-select searchable dengan placeholder `All assets`
22. Verifikasi field `Source` berupa multi-select searchable dengan placeholder `All sources`
23. Verifikasi field `Group` berupa multi-select searchable dengan placeholder `All groups`
24. Verifikasi label field `Date`, `Activity`, `Name`, `Source`, dan `Group`
25. Verifikasi footer panel menampilkan `[Clear Field]` di kiri dan `[Apply]` di kanan
26. Klik icon Filter untuk menutup panel
27. Klik icon Download
28. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
29. Pilih `Download as CSV`
30. Verifikasi file `Transaction-Admin-Log-Budi-Santoso-Damaged.csv` terunduh
31. Verifikasi footer pagination menampilkan 10 data per halaman
32. Klik dropdown page size
33. Verifikasi pilihan page size 10, 25, 50, 100
34. Tutup dropdown page size dengan Esc
35. Klik Back breadcrumb ke User List, cari Hana Kusuma lewat Search, buka Detail User Hana Kusuma, lalu klik Tab Transaction Admin Log
36. Klik Sub-tab Damaged
37. Verifikasi empty state `No transaction log yet` dengan deskripsi `Transactions this user has processed as PIC will appear here.` tampil
38. Ketik Search `zzzz`, tekan Enter
39. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
40. Kosongkan isi kotak search, tekan Enter


## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): langkah 1 (mencari pengguna dan membuka sub-tab; pencarian pengguna di User List adalah langkah penghubung, R-16), pembukaan dan penutupan Search, panel Filter, dan dropdown page size, serta perpindahan ke Detail Hana Kusuma; semuanya hanya mengembalikan state (S-09).
- Pembagian TC lintas spec: Search, guard, Sort, dan Filter sub-tab Damaged ada di spec 469; Download ada di spec 470; routing antar sub-tab ada di spec 474.
- Kolom `Date` mengikuti General Settings; baris diurutkan Date newest first sesuai Expected d TC-FA-SU-1174; Group dibaca dari grup aset saat tindakan dieksekusi (Pre-setup #29 TC).
- Temuan untuk QA (S-15): (1) TC-FA-SU-1174 butir f menyebut "CSV atau XLSX" sedangkan Langkah Uji hanya memilih CSV; spec mengasersi overlay menampilkan kedua format dan nama berkas CSV; format XLSX diasersi di spec 470. (2) Butir h (empty state pengguna tanpa transaksi) memakai Hana Kusuma (Pre-setup #20); Search `zzzz` dipilih spec untuk hasil kosong. (3) Post Condition tidak ada.
- Spec ini berjumlah 40 langkah dan di atas sekitar 35 langkah. Alasan: seluruh klausa Expected TC-FA-SU-1174 (toolbar, kolom, filter, sort, Download, pagination, empty state) berada pada satu surface dengan data seed yang sama, berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
