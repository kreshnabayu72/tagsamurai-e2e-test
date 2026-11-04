---
id: TC-FA-LIC-E2E-058-isi-berkas-allocation-quota-dua-blok-ditumpuk-xlsx
title: "Isi Berkas Download Allocation Quota: Dua Blok Ditumpuk (CSV dan XLSX), Nilai Sel, dan Blok Section 2 Kosong"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-551
  - TC-FA-LIC-552
  - TC-FA-LIC-560
  - TC-FA-LIC-563
coverage:
  web: automated
---

# Isi Berkas Download Allocation Quota: Dua Blok Ditumpuk (CSV dan XLSX), Nilai Sel, dan Blok Section 2 Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Akun kedua untuk TC-FA-LIC-563: Total Control client baru tanpa grup Pre-setup #21 (`Fixture.fixedAssetLicense.akunClientBaru`; pola `newClient_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_NEWCLIENT_TC_PASSWORD`, lewat langkah ganti akun eksplisit (langkah 50). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite untuk akun aktor pertama (dinyatakan sekali di `suite.md`); flag akun client baru sudah true menurut catatan TC (semua akun kecuali Pre-setup #19).
- Data Pre-setup #12 (hanya dibaca): Total Asset License 5.000, Used 4.320, Reserved 15, Unmanaged 27; ledger Add-on Audit 100/60, Tracking 50/48, Maintenance 30/12, IT Inventory 200/120, Maps belum dialokasikan; grup level 1 Produksi (`GRP-PRD`), Cabang Medan, Cabang Surabaya, dan Kantor Pusat (Divisi Logistik 500, Divisi IT, Divisi Keuangan `GRP-FIN` yang belum beralokasi); lewat `Fixture.fixedAssetLicense.kuotaHierarki` (fixture belum ada; disediakan tim FE/BE).
- Data Pre-setup #21 (TC-FA-LIC-563): client Paid tanpa grup; plan client diubah ke Paid oleh fixture BE sebelum langkah 50 dan dikembalikan di hook `after` (disediakan tim FE/BE; mekanisme tidak disebut TC).
- Kemampuan teknis (dinyatakan di `suite.md`, dirujuk satu baris): membaca isi berkas unduhan CSV dan XLSX (nama berkas, encoding dan BOM, nama sheet, baris, sel, tipe sel); berkas tiap unduhan ditangkap ke direktori bersih; fixture BE pemulih Pre-setup #12.

## Test Steps

### TC-FA-LIC-551: CSV node All Groups

1. Klik Tab `Allocation Quota`
2. Klik ikon Download pada toolbar Section 2, lalu pilih `Download as CSV`
3. Verifikasi tidak ada toast sukses
4. Verifikasi berkas `License-Allocation-Quota.csv` terunduh
5. Buka isi berkas yang terunduh
6. Verifikasi encoding berkas UTF-8 dengan BOM
7. Verifikasi baris 1 berkas adalah header `License,Asset,+ Audit,+ Tracking,+ Maintenance Routine,+ Repair Ticketing,+ Maps,+ IT Inventory`
8. Verifikasi baris 2 sampai 6 berkas berurutan Total, Used, Reserved, Remaining, Unmanaged
9. Verifikasi baris 2 berkas `Total,5000,100,50,30,30,Not Available,200`
10. Verifikasi baris 3 berkas `Used,4320,60,48,12,12,-,120`
11. Verifikasi baris 7 berkas kosong (tepat satu baris kosong)
12. Verifikasi baris 8 berkas adalah header `Group Name,Group Code,Allocated Quota,Allocated to Subgroups,Used by This Group,Reserved by This Group,Remaining Quota,+ Audit,+ Tracking,+ Maintenance Routine,+ Repair Ticketing,+ Maps,+ IT Inventory`
13. Verifikasi baris 9 sampai 12 berkas berurutan Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat
14. Verifikasi baris 9 berkas `Produksi,GRP-PRD,1500,0,1450,5,45,20,20,4,4,-,40`
15. Verifikasi baris 10 berkas `Cabang Medan,GRP-MDN,1000,0,880,0,120,15,10,3,3,-,25`
16. Verifikasi baris 11 berkas `Cabang Surabaya,GRP-SBY,800,0,780,10,10,5,6,0,0,-,15`
17. Verifikasi baris 12 berkas `Kantor Pusat,GRP-HQ,1500,600,700,0,200,10,6,2,2,-,20`
18. Verifikasi sel `—` ditulis `-` pada berkas
19. Verifikasi sel `Not Available` ditulis apa adanya pada berkas
20. Verifikasi angka pada berkas ditulis tanpa pemisah ribuan dan tanpa tanda kutip

### TC-FA-LIC-552: XLSX node Kantor Pusat

21. Klik node `Kantor Pusat` di Sidebar
22. Klik ikon Download pada toolbar Section 2, lalu pilih `Download as XLSX`
23. Verifikasi tidak ada toast sukses
24. Verifikasi berkas `License-Allocation-Quota.xlsx` terunduh
25. Buka isi berkas yang terunduh
26. Verifikasi berkas memuat satu sheet bernama `Sheet1`
27. Verifikasi baris 1 berkas adalah header Group Quota Summary `License,Asset,+ Audit,+ Tracking,+ Maintenance Routine,+ Repair Ticketing,+ Maps,+ IT Inventory`
28. Verifikasi baris 2 sampai 6 berkas berurutan Total, Allocated to Subgroups, Used by This Group, Reserved by This Group, Remaining
29. Verifikasi baris 2 berkas: `Total`, 1500, lalu enam sel `-`
30. Verifikasi baris 7 berkas kosong
31. Verifikasi baris 8 berkas adalah header Group License Allocation `Group Name,Group Code,Allocated Quota,Allocated to Subgroups,Used by This Group,Reserved by This Group,Remaining Quota,+ Audit,+ Tracking,+ Maintenance Routine,+ Repair Ticketing,+ Maps,+ IT Inventory`
32. Verifikasi baris 9 sampai 11 berkas berurutan Divisi Logistik, Divisi IT, Divisi Keuangan
33. Verifikasi sel 1500 (baris 2) dan 500 (baris 9, Allocated Quota Divisi Logistik) bertipe angka
34. Verifikasi sel `-` bertipe teks

### TC-FA-LIC-560: Nilai kosong ditulis `-` pada kedua blok

35. Klik node `Kantor Pusat` di Sidebar, klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
36. Verifikasi baris data Divisi Keuangan berkas `Divisi Keuangan,GRP-FIN,-,-,0,0,-,0,0,0,0,-,0`
37. Klik node `Divisi Keuangan` di Sidebar, klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
38. Verifikasi baris `Total` berkas `Total,-,-,-,-,-,-,-`
39. Verifikasi baris `Allocated to Subgroups` berkas `Allocated to Subgroups,-,-,-,-,-,-,-`
40. Verifikasi baris `Used by This Group` berkas `Used by This Group,0,-,-,-,-,-,-`
41. Verifikasi baris `Reserved by This Group` berkas `Reserved by This Group,0,-,-,-,-,-,-`
42. Verifikasi baris `Remaining` berkas `Remaining,200,-,-,-,-,-,-`
43. Perluas node `Divisi Logistik` di Sidebar, lalu klik node `Gudang A`, klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
44. Verifikasi baris `Total` berkas `Total,100,-,-,-,-,-,-`
45. Verifikasi baris `Allocated to Subgroups` berkas `Allocated to Subgroups,0,-,-,-,-,-,-`
46. Verifikasi baris `Used by This Group` berkas `Used by This Group,100,-,-,-,-,-,-`
47. Verifikasi baris `Reserved by This Group` berkas `Reserved by This Group,0,-,-,-,-,-,-`
48. Verifikasi baris `Remaining` berkas `Remaining,0,-,-,-,-,-,-`
49. Verifikasi tidak ada sel `—` pada ketiga berkas

### TC-FA-LIC-563: Node All Groups tanpa grup

50. Ganti akun: Logout, lalu login sebagai Total Control client baru (Pre-setup #21, plan Paid) dengan `Spectra.env.FA_NEWCLIENT_TC_PASSWORD`, lalu buka Fixed Asset > License > Tab `Allocation Quota`
51. Verifikasi Section 2 menampilkan Title `No groups yet`
52. Verifikasi ikon Download aktif
53. Klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
54. Verifikasi baris 1 berkas adalah header `License,Asset,+ Audit,+ Tracking,+ Maintenance Routine,+ Repair Ticketing,+ Maps,+ IT Inventory`
55. Verifikasi baris 2 sampai 6 berkas berurutan Total, Used, Reserved, Remaining, Unmanaged
56. Verifikasi baris 7 berkas kosong
57. Verifikasi baris 8 berkas adalah header Group License Allocation `Group Name,Group Code,Allocated Quota,Allocated to Subgroups,Used by This Group,Reserved by This Group,Remaining Quota,+ Audit,+ Tracking,+ Maintenance Routine,+ Repair Ticketing,+ Maps,+ IT Inventory`
58. Verifikasi berkas tidak memiliki baris data Section 2

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Urutan TC dalam spec: 551, 552, 560, 563 (kasus ganti akun di akhir). Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah (58 langkah). Alasan: seluruh blok satu kelas harness (f, isi berkas CSV dan XLSX dua blok ditumpuk), memakai dataset Pre-setup yang hanya dibaca, dan tiap blok berdiri sendiri: kegagalan satu blok tidak membuat blok lain kehilangan makna; setiap Verifikasi sesuai satu klausa Expected TC (S-01).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (membuka Tab `Allocation Quota`; node `All Groups` aktif saat tab pertama kali dibuka), langkah 5, 25, 35, 37, 43, dan 53 (membuka isi berkas; langkah 43 juga memperluas node `Divisi Logistik` supaya node anak `Gudang A` terlihat di Sidebar), langkah 50 (ganti akun eksplisit, S-07, dan membuka halaman License untuk akun client baru karena `beforeEach` suite hanya membukanya untuk sesi awal).
- Absence state sementara (bagian 8b butir 11 dan 5): toast sukses diasersi segera setelah pemicu dan sebelum asersi berkas (langkah 3 dan 23); pemicu menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh (langkah 4 dan 24).
- Temuan untuk QA:
  - TC-FA-LIC-560 menyebut "Divisi Keuangan belum beralokasi" pada precondition tetapi tidak menyebut cara memastikannya; spec mengandalkan keadaan Pre-setup #12.
  - TC-FA-LIC-560 langkah 3 menyebut node `Gudang A` (leaf) tanpa menyebut induknya; Pre-setup #12 menempatkannya di bawah Divisi Logistik (Kantor Pusat), dan spec mengikuti nama node dari TC.
  - TC-FA-LIC-563 menyebut "Pre-setup #21 diubah plan Paid" tanpa menyebut mekanisme pengubahan plan; disediakan tim FE/BE (S-13).
  - TC-FA-LIC-551, 552, 560, dan 563 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
