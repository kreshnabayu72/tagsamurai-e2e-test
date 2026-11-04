---
id: TC-FA-LIC-E2E-136-role-matrix-download-allocation-quota-read-only-group-manager-manage-asset-license
title: "Role Matrix: Download Allocation Quota Tersedia untuk Read Only, Group Manager, dan Manage Asset License"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-562
coverage:
  web: automated
---

# Role Matrix: Download Allocation Quota Tersedia untuk Read Only, Group Manager, dan Manage Asset License

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (spec positif, bagian 3a):

  | Role | Pre-setup | Akun (fixture) | Password (env) |
  |---|---|---|---|
  | Read Only | #2 | `Fixture.fixedAssetLicense.akunReadOnly` (pola `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net`) | `Spectra.env.FA_RO_PASSWORD` |
  | Group Manager | #6 | `Fixture.fixedAssetLicense.akunGroupManagerHq` (pola `groupManagerHQ_automated_{namaCompany}@qwertysystem.net`; Kantor Pusat) | `Spectra.env.FA_GM_HQ_PASSWORD` |
  | Manage asset license | #4 | `Fixture.fixedAssetLicense.akunManageAssetLicenseHq` (pola `manageAssetLicenseHQ_automated_{namaCompany}@qwertysystem.net`; Group Role Manage asset license pada Kantor Pusat) | `Spectra.env.FA_MAL_HQ_PASSWORD` |

- Akun aktor pertama: Read Only. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control Pre-setup #1). Akun kedua dan ketiga lewat langkah ganti akun eksplisit. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite untuk akun aktor pertama (dinyatakan sekali di `suite.md`); flag akun lain sudah true menurut catatan TC (semua akun kecuali Pre-setup #19).
- Data Pre-setup (hanya dibaca): #12 (kuota dan hierarki PT Sejahtera, client Paid), lewat `Fixture.fixedAssetLicense.kuotaHierarki` (fixture belum ada; disediakan tim FE/BE).
- Kemampuan teknis (dinyatakan di `suite.md`, dirujuk satu baris): membaca isi berkas unduhan CSV; berkas tiap unduhan ditangkap ke direktori bersih.

## Test Steps

### Role Read Only

1. Klik Tab `Allocation Quota`
2. Verifikasi ikon Download aktif pada toolbar Section 2
3. Klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
4. Verifikasi berkas `License-Allocation-Quota.csv` terunduh
5. Verifikasi baris 1 berkas `License-Allocation-Quota.csv` Read Only adalah header `License,Asset,+ Audit,+ Tracking,+ Maintenance Routine,+ Repair Ticketing,+ Maps,+ IT Inventory`
6. Verifikasi baris 2 berkas `License-Allocation-Quota.csv` Read Only adalah `Total,5000,100,50,30,30,Not Available,200`
7. Verifikasi baris 3 berkas `License-Allocation-Quota.csv` Read Only adalah `Used,4320,60,48,12,12,-,120`
8. Verifikasi baris 4 berkas `License-Allocation-Quota.csv` Read Only adalah `Reserved,15,-,-,-,-,-,-`
9. Verifikasi baris 5 berkas `License-Allocation-Quota.csv` Read Only adalah `Remaining,665,40,2,18,18,-,80`
10. Verifikasi baris 6 berkas `License-Allocation-Quota.csv` Read Only adalah `Unmanaged,27,-,-,-,-,-,-`
11. Verifikasi baris 7 berkas `License-Allocation-Quota.csv` Read Only kosong
12. Verifikasi baris 8 berkas `License-Allocation-Quota.csv` Read Only adalah header `Group Name,Group Code,Allocated Quota,Allocated to Subgroups,Used by This Group,Reserved by This Group,Remaining Quota,+ Audit,+ Tracking,+ Maintenance Routine,+ Repair Ticketing,+ Maps,+ IT Inventory`
13. Verifikasi baris 9 berkas `License-Allocation-Quota.csv` Read Only adalah `Produksi,GRP-PRD,1500,0,1450,5,45,20,20,4,4,-,40`
14. Verifikasi baris 10 berkas `License-Allocation-Quota.csv` Read Only adalah `Cabang Medan,GRP-MDN,1000,0,880,0,120,15,10,3,3,-,25`
15. Verifikasi baris 11 berkas `License-Allocation-Quota.csv` Read Only adalah `Cabang Surabaya,GRP-SBY,800,0,780,10,10,5,6,0,0,-,15`
16. Verifikasi baris 12 berkas `License-Allocation-Quota.csv` Read Only adalah `Kantor Pusat,GRP-HQ,1500,600,700,0,200,10,6,2,2,-,20`

### Role Group Manager

17. Ganti akun: Logout, lalu login sebagai Group Manager (Pre-setup #6) dengan `Spectra.env.FA_GM_HQ_PASSWORD`, lalu buka Fixed Asset > License > Tab `Allocation Quota`
18. Verifikasi ikon Download aktif pada toolbar Section 2
19. Klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
20. Verifikasi berkas `License-Allocation-Quota.csv` terunduh

### Role Manage asset license

21. Ganti akun: Logout, lalu login sebagai Manage asset license (Pre-setup #4) dengan `Spectra.env.FA_MAL_HQ_PASSWORD`, lalu buka Fixed Asset > License > Tab `Allocation Quota`
22. Verifikasi ikon Download aktif pada toolbar Section 2
23. Klik ikon Download pada toolbar Section 2, pilih `Download as CSV`, lalu buka berkas yang terunduh
24. Verifikasi berkas `License-Allocation-Quota.csv` terunduh
25. Verifikasi isi ketiga berkas (Read Only, Group Manager, Manage asset license) sama

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke role. Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`): langkah 1 (membuka Tab `Allocation Quota`), langkah 3, 19, dan 23 (membuka isi berkas), langkah 17 dan 21 (ganti akun eksplisit, S-07, dan membuka halaman untuk akun baru).
- Asersi nilai sel (S-03): nilai sel berkas pada langkah 5 sampai 16 disalin dari Expected TC-FA-LIC-562 dan diasersi pada berkas Read Only; isi berkas Group Manager dan Manage asset license dibandingkan identik pada langkah 25. Pemilik nilai sel Allocation Quota tetap TC-FA-LIC-551 (spec lain).
- Temuan untuk QA:
  - TC-FA-LIC-562 tidak menyebut email dan Pre-setup akun Read Only, Group Manager, dan Manage asset license; spec memakai Pre-setup #2, #6, dan #4 (Manage asset license pada Kantor Pusat) sesuai tabel Pre-setup.
  - TC mensyaratkan isi berkas sama untuk ketiga akun. Group Manager #6 dan Manage asset license #4 hanya ditugaskan pada Kantor Pusat sedangkan Read Only melihat node `All Groups`; TC tidak menyebut apakah cakupan data berkas berbeda per akun. Spec mengikuti TC (isi sama).
  - TC-FA-LIC-562 tidak memiliki Post Condition (`-`); tidak ada yang diasersi.
