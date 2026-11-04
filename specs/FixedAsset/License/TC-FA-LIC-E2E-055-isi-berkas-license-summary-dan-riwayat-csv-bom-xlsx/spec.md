---
id: TC-FA-LIC-E2E-055-isi-berkas-license-summary-dan-riwayat-csv-bom-xlsx
title: "Isi Berkas Download: License Summary dan Riwayat (CSV UTF-8 BOM, XLSX Sheet1, Nilai Sel, dan Urutan Sort)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-181
  - TC-FA-LIC-182
  - TC-FA-LIC-184
  - TC-FA-LIC-188
  - TC-FA-LIC-225
  - TC-FA-LIC-229
coverage:
  web: automated
---

# Isi Berkas Download: License Summary dan Riwayat (CSV UTF-8 BOM, XLSX Sheet1, Nilai Sel, dan Urutan Sort)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Akun kedua untuk TC-FA-LIC-184: Total Control client Starter Pre-setup #9 (`Fixture.fixedAssetLicense.akunStarterTotalControl`; pola `totalControlStarter_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_STARTER_TC_PASSWORD`, lewat langkah ganti akun eksplisit (langkah 43). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite untuk akun aktor pertama (dinyatakan sekali di `suite.md`); flag akun Starter sudah true menurut catatan TC (semua akun kecuali Pre-setup #19).
- Data Pre-setup (hanya dibaca, tidak diubah):
  - #12 untuk License Summary client Paid: Total Asset License 5.000, Used 4.320, Reserved 15, Unmanaged 27; ledger Add-on Audit 100/60, Tracking 50/48, Maintenance 30/12 (Repair Ticketing identik dengan Maintenance Routine), IT Inventory 200/120, Maps belum dialokasikan. Lewat `Fixture.fixedAssetLicense.kuotaHierarki` (fixture belum ada; disediakan tim FE/BE).
  - #13 untuk riwayat: 4 term Subscription (SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001, SUBS-20241201-00001) dan 7 alokasi (LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001, LALC-20241205-00001), lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE).
  - #9 untuk TC-FA-LIC-184: client Starter dengan cap plan Asset 500, Used 120, Reserved 0, Unmanaged 3, lewat `Fixture.fixedAssetLicense.starter` (fixture belum ada; disediakan tim FE/BE).
- Date Format General Settings `dd/MM/yy` (Pre-setup #1; spec ini tidak mengubahnya) untuk asersi tanggal pada langkah 29 dan 40.
- Kemampuan teknis (dinyatakan di `suite.md`, dirujuk satu baris): membaca isi berkas unduhan CSV dan XLSX (nama berkas, encoding dan BOM, pemisah, nama sheet, baris, sel, tipe sel); berkas tiap unduhan ditangkap ke direktori bersih sehingga nama sama tidak tertimpa; berkas dihapus di hook `after`.
- State yang diubah dan dipulihkan: sort kolom pertama tabel Subscription History dan Allocation History (dinetralkan kembali pada langkah 31 dan 42).

## Test Steps

### TC-FA-LIC-181: License Summary CSV

1. Klik ikon Download pada header SectionCard `License Summary`, lalu pilih `Download as CSV`
2. Verifikasi tidak ada toast sukses
3. Verifikasi berkas `License-Summary.csv` terunduh
4. Buka isi berkas yang terunduh
5. Verifikasi encoding berkas UTF-8 dengan BOM
6. Verifikasi header berkas `License,Asset,+ Audit,+ Tracking,+ Maintenance Routine,+ Repair Ticketing,+ Maps,+ IT Inventory`
7. Verifikasi berkas memuat lima baris berurutan Total, Used, Reserved, Remaining, Unmanaged
8. Verifikasi baris Total berkas `Total,5000,100,50,30,30,Not Available,200`
9. Verifikasi sel `—` ditulis `-` (baris `Used` kolom `+ Maps` bernilai `-`)
10. Verifikasi angka pada berkas ditulis tanpa pemisah ribuan dan tanpa tanda kutip

### TC-FA-LIC-182: License Summary XLSX

11. Klik ikon Download pada header SectionCard `License Summary`, pilih `Download as XLSX`, lalu buka berkas yang terunduh
12. Verifikasi berkas `License-Summary.xlsx` terunduh
13. Verifikasi berkas memuat satu sheet bernama `Sheet1`
14. Verifikasi sel angka (5000 dan 4320) bertipe angka
15. Verifikasi sel `Not Available` bertipe teks
16. Verifikasi sel `—` ditulis `-`

### TC-FA-LIC-188: Nilai Reserved, Unmanaged, dan Remaining pada berkas

17. Klik ikon Download pada header SectionCard `License Summary`, pilih `Download as CSV`, lalu buka berkas yang terunduh
18. Verifikasi baris `Reserved` berkas `Reserved,15,-,-,-,-,-,-`
19. Verifikasi baris `Unmanaged` berkas `Unmanaged,27,-,-,-,-,-,-`
20. Verifikasi baris `Remaining` berkas `Remaining,665,40,2,18,18,-,80`

### TC-FA-LIC-225: Berkas Subscription History

21. Klik sub-tab `Subscription History`
22. Klik header kolom `Subscription ID` sekali (Ascending)
23. Klik ikon Download pada toolbar tabel Subscription History, pilih `Download as CSV`, lalu buka berkas yang terunduh
24. Klik ikon Download pada toolbar tabel Subscription History, pilih `Download as XLSX`, lalu buka berkas yang terunduh
25. Verifikasi CSV berencoding UTF-8 dengan BOM
26. Verifikasi CSV memakai pemisah koma
27. Verifikasi XLSX memuat satu sheet bernama `Sheet1`
28. Verifikasi urutan baris CSV dan XLSX mengikuti sort aktif (Subscription ID Ascending): SUBS-20241201-00001, SUBS-20250101-00001, SUBS-20260101-00001, SUBS-20270101-00001
29. Verifikasi tanggal pada berkas berformat General Settings (`dd/MM/yy`)
30. Verifikasi angka pada berkas bernilai numerik tanpa pemisah ribuan
31. Klik header kolom `Subscription ID` dua kali lagi hingga netral

### TC-FA-LIC-229: Berkas Allocation History

32. Klik sub-tab `Allocation History`
33. Klik header kolom `Allocation ID` sekali (Ascending)
34. Klik ikon Download pada toolbar tabel Allocation History, pilih `Download as CSV`, lalu buka berkas yang terunduh
35. Klik ikon Download pada toolbar tabel Allocation History, pilih `Download as XLSX`, lalu buka berkas yang terunduh
36. Verifikasi CSV berencoding UTF-8 dengan BOM
37. Verifikasi CSV memakai pemisah koma
38. Verifikasi XLSX memuat satu sheet bernama `Sheet1`
39. Verifikasi urutan baris CSV dan XLSX mengikuti sort aktif (Allocation ID Ascending): LALC-20241205-00001, LALC-20250210-00001, LALC-20260101-00001, LALC-20260312-00002, LALC-20260515-00002, LALC-20260720-00003, LALC-20260801-00004
40. Verifikasi tanggal pada berkas berformat General Settings (`dd/MM/yy`)
41. Verifikasi angka pada berkas (kolom `Quantity`) bernilai numerik tanpa pemisah ribuan
42. Klik header kolom `Allocation ID` dua kali lagi hingga netral

### TC-FA-LIC-184: License Summary plan Starter

43. Ganti akun: Logout, lalu login sebagai Total Control client Starter (Pre-setup #9) dengan `Spectra.env.FA_STARTER_TC_PASSWORD`, lalu buka Fixed Asset > License > Tab `All License`
44. Verifikasi tombol Download License Summary tampil dan aktif
45. Verifikasi tidak ada toolbar Download riwayat
46. Klik ikon Download pada header SectionCard `License Summary`, pilih `Download as CSV`, lalu buka berkas yang terunduh
47. Verifikasi baris `Total` berkas `Total,500,Not Available,Not Available,Not Available,Not Available,Not Available,Not Available`
48. Verifikasi baris `Used` berkas `Used,120,-,-,-,-,-,-`

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Urutan TC dalam spec: 181, 182, 188, 225, 229, 184 (kasus ganti akun di akhir). Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah (48 langkah). Alasan: seluruh blok satu kelas harness (f, isi berkas CSV dan XLSX), memakai dataset Pre-setup yang hanya dibaca, dan tiap blok berdiri sendiri: kegagalan satu blok tidak membuat blok lain kehilangan makna; setiap langkah Verifikasi sesuai satu klausa Expected TC (S-01) sehingga tidak ada pengulangan yang dapat diringkas.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 4, 11, 17, 23, 24, 34, 35, dan 46 (membuka isi berkas), langkah 21 dan 32 (klik sub-tab sebagai aksi deterministik), langkah 31 dan 42 (menetralkan sort; S-09), langkah 43 (ganti akun eksplisit, S-07, dan membuka halaman License untuk akun Starter karena `beforeEach` suite hanya membukanya untuk sesi awal).
- Absence state sementara (bagian 8b butir 11 dan 5): toast sukses diasersi segera setelah pemicu dan sebelum asersi berkas (langkah 2); pemicu menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh (langkah 3).
- Asersi di luar Expected TC (S-03): langkah 22, 33 (sort Ascending kolom pertama) mengikuti langkah TC-FA-LIC-225 dan TC-FA-LIC-229; urutan baris pada langkah 28 dan 39 diturunkan dari data TC-FA-LIC-195 dan TC-FA-LIC-236 untuk sort Ascending kolom pertama.
- Temuan untuk QA:
  - Judul TC-FA-LIC-225 dan TC-FA-LIC-229 menyebut "nilai kosong ditulis `-`" tetapi Expected tidak memuat klausa itu; tidak diasersi pada kedua riwayat.
  - TC-FA-LIC-225 mensyaratkan "angka bernilai numerik tanpa pemisah ribuan", sedangkan tabel Subscription History tidak memiliki kolom angka (kolom: Subscription ID, Plan, Type, Status, Start Date, End Date, Plan Owner); asersi langkah 30 tidak memiliki objek sel angka yang terbaca.
  - TC-FA-LIC-225 dan TC-FA-LIC-229 tidak menyebut nama berkas dan cara memilih tombol Download tabel riwayat (toolbar tabel); spec memakai ikon Download pada toolbar tabel.
  - TC-FA-LIC-184 mensyaratkan login Total Control Pre-setup #9; TC-FA-LIC-184 tidak menyebut Post Condition (`-`), demikian pula TC lain di spec ini; tidak ada yang diasersi.
