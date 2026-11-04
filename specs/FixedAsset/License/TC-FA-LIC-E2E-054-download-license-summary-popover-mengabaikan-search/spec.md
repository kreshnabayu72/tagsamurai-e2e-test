---
id: TC-FA-LIC-E2E-054-download-license-summary-popover-mengabaikan-search
title: "Download License Summary: Popover Dua Format, Kolom yang Tampil, dan Tidak Terpengaruh Search, Filter, serta Setup Column Riwayat"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-180
  - TC-FA-LIC-183
  - TC-FA-LIC-187
  - TC-FA-LIC-588
coverage:
  web: automated
---

# Download License Summary: Popover Dua Format, Kolom yang Tampil, dan Tidak Terpengaruh Search, Filter, serta Setup Column Riwayat

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email di Pre-setup `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup (hanya dibaca, tidak diubah): #12 (kuota PT Sejahtera: Total Asset License 5.000, Used 4.320, Reserved 15, Unmanaged 27; ledger Add-on Audit 100/60, Tracking 50/48, Maintenance 30/12, IT Inventory 200/120, Maps belum dialokasikan; hierarki grup) dan #13 (data riwayat Allocation History untuk TC-FA-LIC-183), lewat `Fixture.fixedAssetLicense.kuotaHierarki` dan `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE).
- Kemampuan teknis: mengirim tombol `Esc` untuk menutup popover (langkah 3).
- Kemampuan teknis (dinyatakan di `suite.md`, dirujuk satu baris): membaca isi berkas unduhan CSV dan XLSX (nama berkas, baris header, jumlah dan isi baris); berkas tiap unduhan ditangkap ke direktori bersih sehingga nama sama tidak tertimpa.
- Kolom yang disembunyikan lewat Column Visibility (tabel License Summary pada langkah 6 dan tabel Allocation History pada langkah 16) dipulihkan pada langkah 13 dan 25; hook `after` menghapus preferensi kolom di browser sebagai cadangan (pernyataan di `suite.md`).

## Test Steps

### TC-FA-LIC-180: Popover Download License Summary

1. Klik ikon Download pada header SectionCard `License Summary`
2. Verifikasi popover menampilkan `Download as CSV` dan `Download as XLSX`
3. Tekan Esc untuk menutup popover

### TC-FA-LIC-588: Column Visibility License Summary dan Download mengikuti kolom yang tampil

4. Verifikasi header kolom Actions `⋯` tampil pada tabel License Summary sebagai pemicu Column Visibility
5. Verifikasi kolom Actions tidak berisi konten
6. Klik header kolom Actions `⋯`, hilangkan centang `+ Maps` dan `+ IT Inventory` pada overlay Column Visibility, lalu tutup overlay
7. Verifikasi kolom `+ Maps` dan `+ IT Inventory` hilang dari tabel License Summary
8. Verifikasi kolom `License`, `Asset`, `+ Audit`, `+ Tracking`, `+ Maintenance Routine`, dan `+ Repair Ticketing` tetap tampil
9. Klik ikon Download pada header SectionCard `License Summary`, pilih `Download as CSV`, lalu buka berkas yang terunduh
10. Verifikasi berkas `License-Summary.csv` terunduh
11. Verifikasi header berkas memuat kolom `License` dan kolom yang tampil saja (`Asset`, `+ Audit`, `+ Tracking`, `+ Maintenance Routine`, `+ Repair Ticketing`), tanpa `+ Maps` dan `+ IT Inventory`
12. Verifikasi tabel License Summary tidak menyediakan Search dan Filter
13. Klik header kolom Actions `⋯`, centang kembali `+ Maps` dan `+ IT Inventory` pada overlay Column Visibility, lalu tutup overlay

### TC-FA-LIC-183: Download License Summary mengabaikan Search, Filter, dan Setup Column riwayat

14. Klik sub-tab `Allocation History`
15. Ketik Search `Audit`, tekan Enter
16. Klik header kolom Actions `⋯` pada tabel Allocation History, hilangkan centang `Plan Owner` dan `Last Updated`, lalu tutup overlay
17. Klik ikon Download pada header SectionCard `License Summary`, pilih `Download as CSV`, lalu buka berkas yang terunduh
18. Verifikasi berkas `License-Summary.csv` terunduh
19. Verifikasi header berkas memuat delapan kolom `License,Asset,+ Audit,+ Tracking,+ Maintenance Routine,+ Repair Ticketing,+ Maps,+ IT Inventory`
20. Verifikasi baris `Total` berkas `Total,5000,100,50,30,30,Not Available,200`
21. Verifikasi baris `Used` berkas `Used,4320,60,48,12,12,-,120`
22. Verifikasi baris `Reserved` berkas `Reserved,15,-,-,-,-,-,-`
23. Verifikasi baris `Remaining` berkas `Remaining,665,40,2,18,18,-,80`
24. Verifikasi baris `Unmanaged` berkas `Unmanaged,27,-,-,-,-,-,-`
25. Klik `(←)` pada kotak Search, lalu klik header kolom Actions `⋯` pada tabel Allocation History, centang kembali `Plan Owner` dan `Last Updated`, dan tutup overlay

### TC-FA-LIC-187: Tab Allocation Quota tanpa ikon Download pada Section 1

26. Klik Tab `Allocation Quota`
27. Verifikasi Section 1 `All License` tampil dengan tabel License Summary
28. Verifikasi tabel License Summary tampil tanpa ikon Download dan tanpa aksi Edit

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. TC-FA-LIC-186 (Download untuk Read Only dan Group Manager) ada di spec 135. Urutan TC dalam spec: 180, 588, 183, 187 (kasus yang mengubah visibilitas kolom dipulihkan sebelum kasus berikutnya). Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 3 (menutup popover dengan Esc), langkah 6, 13, 16, dan 25 (menutup overlay Column Visibility dan memulihkan kolom; S-09), langkah 9 dan 17 (membuka isi berkas), langkah 14 (`Klik sub-tab Allocation History` sebagai aksi deterministik), langkah 26 (membuka Tab `Allocation Quota`; node `All Groups` adalah node aktif saat tab pertama kali dibuka, TC-FA-LIC-220).
- P-10: TC-FA-LIC-588 dan TC-FA-LIC-183 (spec fungsional) memuat klausa isi berkas yang diletakkan sesudah klausa UI TC itu (langkah 11 dan 19 sampai 24); alur unduh tidak dapat dipisah dari asersi UI karena Expected berkas bergantung pada kolom yang disembunyikan dan Search yang diterapkan pada langkah sebelumnya.
- Asersi di luar Expected TC (S-03): langkah 10 dan 18 (berkas `License-Summary.csv` terunduh) adalah anchor positif sebelum asersi isi berkas; langkah 27 (Section 1 `All License` tampil) adalah anchor positif untuk asersi absence langkah 28 (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-LIC-183 menyebut "sembunyikan beberapa kolom" tanpa menyebut kolom mana; spec menyembunyikan `Plan Owner` dan `Last Updated` pada Allocation History. TC-FA-LIC-588 menyebut `Setup Column` pada judul tetapi langkahnya memakai overlay Column Visibility; spec mengikuti langkah.
  - TC-FA-LIC-588 tidak menyebut cara menutup overlay Column Visibility; spec menulis "tutup overlay" sebagai langkah penghubung.
  - TC-FA-LIC-180, 183, 187, dan 588 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
