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
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Akun kedua untuk TC-FA-LIC-563: Total Control client baru tanpa grup Pre-setup #21 (`Fixture.fixedAssetLicense.akunClientBaru`; pola `newClient_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_NEWCLIENT_TC_PASSWORD`, lewat langkah ganti akun eksplisit (langkah 37). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite untuk akun aktor pertama (dinyatakan sekali di `suite.md`); flag akun client baru sudah true menurut catatan TC (semua akun kecuali Pre-setup #19).
- Data Pre-setup #12 (hanya dibaca): Total Asset License 5.000, Used 4.320, Reserved 15, Unmanaged 27; ledger Add-on Audit 100/60, Tracking 50/48, Maintenance 30/12, IT Inventory 200/120, Maps belum dialokasikan; grup level 1 Produksi (`GRP-PRD`), Cabang Medan, Cabang Surabaya, dan Kantor Pusat (Divisi Logistik 500, Divisi IT, Divisi Keuangan `GRP-FIN` yang belum beralokasi); lewat `Fixture.fixedAssetLicense.kuotaHierarki` (fixture belum ada; disediakan tim FE/BE).
- Data Pre-setup #21 (TC-FA-LIC-563): client Paid tanpa grup; plan client diubah ke Paid oleh fixture BE sebelum langkah 37 dan dikembalikan di hook `after` (disediakan tim FE/BE; mekanisme tidak disebut TC).
- Kemampuan teknis (dinyatakan di `suite.md`, dirujuk satu baris): membaca isi berkas unduhan CSV dan XLSX (nama berkas, encoding dan BOM, nama sheet, baris, sel, tipe sel); berkas tiap unduhan ditangkap ke direktori bersih; fixture BE pemulih Pre-setup #12.

## Test Steps

### TC-FA-LIC-551: CSV node All Groups

1. Klik Tab `Allocation Quota` (node `All Groups` aktif)
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
15. Verifikasi sel `—` ditulis `-` pada berkas
16. Verifikasi sel `Not Available` ditulis apa adanya pada berkas
17. Verifikasi angka pada berkas ditulis tanpa pemisah ribuan dan tanpa tanda kutip

### TC-FA-LIC-552: XLSX node Kantor Pusat

18. Klik node `Kantor Pusat` di Sidebar
19. Klik ikon Download pada toolbar Section 2, lalu pilih `Download as XLSX`
20. Verifikasi tidak ada toast sukses
21. Verifikasi berkas `License-Allocation-Quota.xlsx` terunduh
22. Buka isi berkas yang terunduh
23. Verifikasi berkas memuat satu sheet bernama `Sheet1`
24. Verifikasi baris 1 berkas adalah header Group Quota Summary delapan kolom
25. Verifikasi baris 2 sampai 6 berkas berurutan Total, Allocated to Subgroups, Used by This Group, Reserved by This Group, Remaining
26. Verifikasi baris 2 berkas: `Total`, 1500, lalu enam sel `-`
27. Verifikasi baris 7 berkas kosong
28. Verifikasi baris 8 berkas adalah header Group License Allocation tiga belas kolom
29. Verifikasi baris 9 sampai 11 berkas berurutan Divisi Logistik, Divisi IT, Divisi Keuangan
30. Verifikasi sel 1500 (baris 2) dan 500 (baris 9, Allocated Quota Divisi Logistik) bertipe angka
31. Verifikasi sel `-` bertipe teks

### TC-FA-LIC-560: Nilai kosong ditulis `-` pada kedua blok

32. Klik node `Kantor Pusat` di Sidebar, klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
33. Verifikasi baris data Divisi Keuangan berkas `Divisi Keuangan,GRP-FIN,-,-,0,0,-,0,0,0,0,-,0`
34. Klik node `Divisi Keuangan` di Sidebar, klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
35. Verifikasi lima baris berkas `Total,-,-,-,-,-,-,-`, `Allocated to Subgroups,-,-,-,-,-,-,-`, `Used by This Group,0,-,-,-,-,-,-`, `Reserved by This Group,0,-,-,-,-,-,-`, dan `Remaining,200,-,-,-,-,-,-`
36. Verifikasi tidak ada sel `—` pada kedua berkas

### TC-FA-LIC-563: Node All Groups tanpa grup

37. Ganti akun: Logout, lalu login sebagai Total Control client baru (Pre-setup #21, plan Paid) dengan `Spectra.env.FA_NEWCLIENT_TC_PASSWORD`, lalu buka Fixed Asset > License > Tab `Allocation Quota`
38. Verifikasi Section 2 menampilkan Title `No groups yet`
39. Verifikasi ikon Download aktif
40. Klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
41. Verifikasi berkas memuat header dan lima baris berurutan Total, Used, Reserved, Remaining, Unmanaged
42. Verifikasi baris 7 berkas kosong
43. Verifikasi baris 8 berkas adalah header tiga belas kolom Group License Allocation
44. Verifikasi berkas tidak memiliki baris data Section 2

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Urutan TC dalam spec: 551, 552, 560, 563 (kasus ganti akun di akhir). Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah (44 langkah). Alasan: seluruh blok satu kelas harness (f, isi berkas CSV dan XLSX dua blok ditumpuk), memakai dataset Pre-setup yang hanya dibaca, dan tiap blok berdiri sendiri: kegagalan satu blok tidak membuat blok lain kehilangan makna; setiap Verifikasi sesuai satu klausa Expected TC (S-01).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (membuka Tab `Allocation Quota`; node `All Groups` aktif saat tab pertama kali dibuka), langkah 5, 22, 32, 34, dan 40 (membuka isi berkas), langkah 37 (ganti akun eksplisit, S-07, dan membuka halaman License untuk akun client baru karena `beforeEach` suite hanya membukanya untuk sesi awal).
- Absence state sementara (bagian 8b butir 11 dan 5): toast sukses diasersi segera setelah pemicu dan sebelum asersi berkas (langkah 3 dan 20); pemicu menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh (langkah 4 dan 21).
- Temuan untuk QA:
  - TC-FA-LIC-552 tidak menyebut nama kolom header Group Quota Summary dan Group License Allocation selain "delapan kolom" dan "tiga belas kolom"; spec mengasersi jumlah kolom sesuai TC.
  - TC-FA-LIC-560 menyebut "Divisi Keuangan belum beralokasi" pada precondition tetapi tidak menyebut cara memastikannya; spec mengandalkan keadaan Pre-setup #12.
  - TC-FA-LIC-563 menyebut "Pre-setup #21 diubah plan Paid" tanpa menyebut mekanisme pengubahan plan; disediakan tim FE/BE (S-13).
  - TC-FA-LIC-551, 552, 560, dan 563 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.
