---
id: TC-FA-LIC-E2E-057-download-allocation-quota-column-visibility-sort-node
title: "Download Allocation Quota: Mengikuti Column Visibility dan Sort, Node Leaf, serta Search Tanpa Hasil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-556
  - TC-FA-LIC-557
  - TC-FA-LIC-558
  - TC-FA-LIC-559
coverage:
  web: automated
---

# Download Allocation Quota: Mengikuti Column Visibility dan Sort, Node Leaf, serta Search Tanpa Hasil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #12 (hanya dibaca): hierarki PT Sejahtera dengan grup level 1 Produksi (`GRP-PRD`), Cabang Medan, Cabang Surabaya, dan Kantor Pusat (Divisi Logistik, Divisi IT, Divisi Keuangan), dan Gudang A (leaf) di bawah Divisi Logistik dengan alokasi 100 (Used 100); lewat `Fixture.fixedAssetLicense.kuotaHierarki` (fixture belum ada; disediakan tim FE/BE).
- Kemampuan teknis (dinyatakan di `suite.md`, dirujuk satu baris): membaca isi berkas unduhan CSV (nama berkas, header, baris, sel); berkas tiap unduhan ditangkap ke direktori bersih.
- State yang diubah dan dipulihkan: konfigurasi kolom Setup Column Section 2 (`Group Code` dan `+ Audit`, dipulihkan pada langkah 11; didaftarkan di `suite.md`, hook `after` menghapus preferensi kolom di browser sebagai cadangan), Sort `Group Name` (dinetralkan pada langkah 16), dan Search Section 2 (dibersihkan pada langkah 37).

## Test Steps

### TC-FA-LIC-556: Download mengikuti Column Visibility

1. Klik Tab `Allocation Quota`
2. Buka Setup Column Section 2, hilangkan centang `Group Code` dan `+ Audit`, lalu klik `[Save]`
3. Klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
4. Verifikasi header Section 2 berkas `Group Name,Allocated Quota,Allocated to Subgroups,Used by This Group,Reserved by This Group,Remaining Quota,+ Tracking,+ Maintenance Routine,+ Repair Ticketing,+ Maps,+ IT Inventory`
5. Verifikasi baris Produksi berkas `Produksi,1500,0,1450,5,45,20,4,4,-,40`
6. Verifikasi blok Section 1 berkas tetap memuat delapan kolom termasuk `+ Audit`
7. Buka Setup Column Section 2, centang kembali `Group Code`, lalu klik `[Save]`
8. Klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
9. Verifikasi header Section 2 berkas memuat kembali `Group Code`
10. Verifikasi header Section 2 berkas tetap tanpa `+ Audit`
11. Buka Setup Column Section 2, centang kembali `+ Audit`, lalu klik `[Save]`

### TC-FA-LIC-557: Urutan baris berkas mengikuti Sort aktif

12. Klik header `Group Name` sekali (Ascending)
13. Verifikasi tabel Section 2 berurutan: Cabang Medan, Cabang Surabaya, Kantor Pusat, Produksi
14. Klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
15. Verifikasi baris data blok Section 2 berkas berurutan sama: Cabang Medan, Cabang Surabaya, Kantor Pusat, Produksi
16. Klik header `Group Name` dua kali lagi hingga netral

### TC-FA-LIC-558: Download pada node leaf

17. Perluas node `Kantor Pusat` dan `Divisi Logistik` di Sidebar, lalu klik node `Gudang A`
18. Verifikasi Section 2 menampilkan Title `No subgroup yet`
19. Verifikasi ikon Download tampil dan aktif
20. Klik ikon Download pada toolbar Section 2, pilih `Download as CSV`
21. Verifikasi tidak ada toast
22. Buka berkas yang terunduh
23. Verifikasi baris 1 berkas adalah header `License,Asset,+ Audit,+ Tracking,+ Maintenance Routine,+ Repair Ticketing,+ Maps,+ IT Inventory`
24. Verifikasi baris 2 sampai 6 berkas `Total,100,-,-,-,-,-,-`, `Allocated to Subgroups,0,-,-,-,-,-,-`, `Used by This Group,100,-,-,-,-,-,-`, `Reserved by This Group,0,-,-,-,-,-,-`, `Remaining,0,-,-,-,-,-,-`
25. Verifikasi baris 7 berkas kosong
26. Verifikasi baris 8 berkas adalah header Group License Allocation `Group Name,Group Code,Allocated Quota,Allocated to Subgroups,Used by This Group,Reserved by This Group,Remaining Quota,+ Audit,+ Tracking,+ Maintenance Routine,+ Repair Ticketing,+ Maps,+ IT Inventory`
27. Verifikasi berkas tidak memiliki baris 9

### TC-FA-LIC-559: Download saat Search tidak menghasilkan baris

28. Klik node `All Groups` di Sidebar
29. Ketik Search `zzzz` pada Search Section 2, tekan Enter
30. Verifikasi Section 2 menampilkan Title `No results found`
31. Verifikasi ikon Download tetap aktif
32. Klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
33. Verifikasi berkas memuat lima baris License Summary penuh
34. Verifikasi baris 7 berkas kosong
35. Verifikasi baris 8 berkas adalah header Group License Allocation `Group Name,Group Code,Allocated Quota,Allocated to Subgroups,Used by This Group,Reserved by This Group,Remaining Quota,+ Audit,+ Tracking,+ Maintenance Routine,+ Repair Ticketing,+ Maps,+ IT Inventory`
36. Verifikasi berkas tidak memiliki baris data Section 2
37. Klik `(←)` pada kotak Search Section 2

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. TC-FA-LIC-562 (Download untuk Read Only, Group Manager, dan Manage asset license) ada di spec 136. Urutan TC dalam spec: 556, 557, 558, 559 (kasus yang mengubah Setup Column di awal dan dipulihkan sebelum kasus berikutnya). Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (membuka Tab `Allocation Quota`), langkah 3, 8, 14, 22, dan 32 (membuka isi berkas), langkah 11 (memulihkan `+ Audit`; S-09), langkah 16 (menetralkan Sort; S-09), langkah 17 (memperluas node pohon sampai `Gudang A`), langkah 28 (kembali ke node `All Groups`), langkah 37 (pemulihan Search).
- Spec di atas 35 langkah (37 langkah): seluruh blok satu topik (Download Allocation Quota pada dataset Pre-setup #12 yang sama) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; kelebihan dua langkah berasal dari pemecahan Expected TC-FA-LIC-559 b per klausa (lima baris ringkasan, baris 7 kosong, baris 8 header).
- Absence state sementara (bagian 8b butir 11): toast diasersi segera setelah pemicu dan sebelum asersi berkas (langkah 21); pemicu (langkah 20) menjadi anchor positif yang buktinya menyusul pada langkah 23.
- P-10 (isi berkas pada spec fungsional, bagian 3 prinsip 13f): spec ini mengasersi nama kolom (header), jumlah baris, dan urutan baris sebagai asersi fungsional. Langkah 5 (satu baris data lengkap) dan langkah 24 (lima baris summary leaf) mengasersi nilai sel karena Expected TC-FA-LIC-556 dan TC-FA-LIC-558 menuliskannya; asersi nilai sel dua blok ada di spec 058.
- Temuan untuk QA:
  - TC-FA-LIC-556 menyebut "Buka Setup Column Section 2" tanpa menyebut kontrol pembukanya; spec membukanya lewat header kolom Actions `⋯` > `Setup Column...` seperti tabel lain di modul ini.
  - TC-FA-LIC-558 menyebut node `Gudang A` tanpa menyebut bahwa pohon harus diperluas; spec memperluas `Kantor Pusat` dan `Divisi Logistik` terlebih dahulu.
  - TC-FA-LIC-556, 557, 558, dan 559 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
