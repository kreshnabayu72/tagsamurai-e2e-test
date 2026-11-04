---
id: TC-FA-LIC-E2E-135-role-matrix-download-license-summary-read-only-group-manager
title: "Role Matrix: Download License Summary Tersedia untuk Read Only dan Group Manager"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-186
coverage:
  web: automated
---

# Role Matrix: Download License Summary Tersedia untuk Read Only dan Group Manager

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (spec positif, bagian 3a):

  | Role | Pre-setup | Akun (fixture) | Password (env) |
  |---|---|---|---|
  | Read Only | #2 | `Fixture.fixedAssetLicense.akunReadOnly` (pola `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net`) | `Spectra.env.FA_RO_PASSWORD` |
  | Group Manager | #6 | `Fixture.fixedAssetLicense.akunGroupManagerHq` (pola `groupManagerHQ_automated_{namaCompany}@qwertysystem.net`; Group Manager pada Kantor Pusat) | `Spectra.env.FA_GM_HQ_PASSWORD` |

- Akun aktor pertama: Read Only. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control Pre-setup #1). Akun kedua (Group Manager) lewat langkah ganti akun eksplisit. Password tidak ditulis di spec atau fixture. TC tidak menyebut Pre-setup akun Read Only dan Group Manager pada precondition; Pre-setup #2 dan #6 dipakai sesuai tabel Pre-setup.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite untuk akun aktor pertama (dinyatakan sekali di `suite.md`); flag akun Group Manager sudah true menurut catatan TC (semua akun kecuali Pre-setup #19).
- Data Pre-setup (hanya dibaca): #12 (kuota dan hierarki PT Sejahtera, client Paid), lewat `Fixture.fixedAssetLicense.kuotaHierarki` (fixture belum ada; disediakan tim FE/BE).
- Kemampuan teknis (dinyatakan di `suite.md`, dirujuk satu baris): membaca isi berkas unduhan CSV; berkas tiap unduhan ditangkap ke direktori bersih.

## Test Steps

### Role Read Only

1. Klik ikon Download pada header SectionCard `License Summary`, pilih `Download as CSV`, lalu buka berkas yang terunduh
2. Verifikasi berkas `License-Summary.csv` terunduh
3. Verifikasi baris 1 berkas `License-Summary.csv` Read Only adalah header `License,Asset,+ Audit,+ Tracking,+ Maintenance Routine,+ Repair Ticketing,+ Maps,+ IT Inventory`
4. Verifikasi baris 2 berkas `License-Summary.csv` Read Only adalah `Total,5000,100,50,30,30,Not Available,200`
5. Verifikasi baris 3 berkas `License-Summary.csv` Read Only adalah `Used,4320,60,48,12,12,-,120`
6. Verifikasi baris 4 berkas `License-Summary.csv` Read Only adalah `Reserved,15,-,-,-,-,-,-`
7. Verifikasi baris 5 berkas `License-Summary.csv` Read Only adalah `Remaining,665,40,2,18,18,-,80`
8. Verifikasi baris 6 berkas `License-Summary.csv` Read Only adalah `Unmanaged,27,-,-,-,-,-,-`

### Role Group Manager

9. Ganti akun: Logout, lalu login sebagai Group Manager (Pre-setup #6) dengan `Spectra.env.FA_GM_HQ_PASSWORD`, lalu buka Fixed Asset > License > Tab `All License`
10. Klik ikon Download pada header SectionCard `License Summary`, pilih `Download as CSV`, lalu buka berkas yang terunduh
11. Verifikasi berkas `License-Summary.csv` terunduh
12. Verifikasi isi berkas Group Manager sama dengan isi berkas Read Only (header dan seluruh baris)

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke role. Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`): langkah 1 dan 10 membuka isi berkas; langkah 9 adalah ganti akun eksplisit (S-07) dan membuka halaman License untuk akun kedua karena `beforeEach` suite hanya membukanya untuk sesi awal.
- Asersi nilai sel (S-03): nilai sel berkas pada langkah 3 sampai 8 disalin dari Expected TC-FA-LIC-186 dan diasersi pada berkas Read Only; isi berkas Group Manager dibandingkan identik dengan berkas Read Only pada langkah 12. Pemilik nilai sel License Summary tetap TC-FA-LIC-181 dan TC-FA-LIC-551 (spec lain); spec ini tidak memakai nilai selain yang tertulis di TC-FA-LIC-186.
- Temuan untuk QA:
  - TC-FA-LIC-186 tidak memuat baris `Login sbg Role:` pada precondition dan tidak menyebut email Read Only dan Group Manager; spec memakai Pre-setup #2 dan #6.
  - TC mensyaratkan "isi sama" untuk Read Only dan Group Manager. Group Manager Pre-setup #6 ditugaskan hanya pada Kantor Pusat; TC tidak menyebut apakah License Summary tenant (bukan per grup) dapat berbeda untuk Group Manager. Spec mengikuti TC (isi sama).
  - TC-FA-LIC-186 tidak memiliki Post Condition (`-`); tidak ada yang diasersi.
