---
id: TC-FA-CAID-E2E-006-role-matrix-visibilitas-elemen
title: "Role Matrix: Visibilitas Elemen Tab Custom Asset ID per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-22
  - TC-FA-CAID-23
  - TC-FA-CAID-24
  - TC-FA-CAID-25
  - TC-FA-CAID-26
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Tab Custom Asset ID per Role

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Total Control) di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite untuk akun itu. Akun lain login lewat langkah ganti akun eksplisit.
- Role yang diuji (Company Alpha; email `<prefix>_automated_{namaCompany}@qwertysystem.net`, password dari env, tidak ditulis di spec atau fixture):

| Blok | TC | Role | Pre-setup | Prefix email | Env password |
|---|---|---|---|---|---|
| 1 | TC-FA-CAID-22 | Total Control | No 1 | `totalControl` | `Spectra.env.FA_TC_PASSWORD` |
| 2 | TC-FA-CAID-23 | Read Only | No 2 | `readOnly` | `Spectra.env.FA_RO_PASSWORD` |
| 3 | TC-FA-CAID-24 | Config-Update (Manage asset ID configuration dengan Read dan Update) | No 3 | `configUpdate` | `Spectra.env.FA_CFGUPD_PASSWORD` |
| 4 | TC-FA-CAID-25 | Config-Read (Manage asset ID configuration hanya Read) | No 4 | `configRead` | `Spectra.env.FA_CFGREAD_PASSWORD` |
| 5 | TC-FA-CAID-26 | Master-Data-Only (Manage asset master data tanpa Manage asset ID configuration) | No 5 | `masterDataOnly` | `Spectra.env.FA_MDONLY_PASSWORD` |

  Nama env password untuk lima role adalah usulan di `suite.md` dan perlu konfirmasi tim FE.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk semua akun UI suite; konfigurasi Company Alpha dipulihkan ke baseline B1 di `beforeEach` lewat sesi API aktor. Hook `after` spec ini mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Data Pre-setup No 10: baseline B1 (Master Switch ON, Separator `/ (Slash)`, segmen tercentang Group Code, Category Code, Asset Name Code, Purchase Date, Asset Increment, tanpa Initial Company), hanya dibaca. Nilai dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Spec hanya membaca: tidak membuat data, tidak menekan `[Save]`, tidak mengubah state global. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-22: Total Control (blok 1)

1. Verifikasi Tabs Bar memuat tab `Custom Asset ID`
2. Verifikasi Master Switch, Separator, checkbox dan drag handle Daftar Segmen, input Initial Company, tombol `[Save]`, tautan `[View Code List]`, dan tombol `[Changelog]` seluruhnya tampil dan tidak ada yang berstatus Hidden
3. Verifikasi kontrol form tidak ditandai Disabled 🔖

### TC-FA-CAID-23: Read Only (blok 2)

4. Ganti akun: logout akun Total Control, lalu login sebagai Read Only (Pre-setup No 2)
5. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
6. Verifikasi Tabs Bar memuat tab `Custom Asset ID`
7. Verifikasi Master Switch, Separator, checkbox dan drag handle Daftar Segmen, dan input Initial Company tampil dengan status Disabled 🔖
8. Verifikasi tombol `[Save]` tidak tampil (Hidden)
9. Verifikasi tautan `[View Code List]` dan tombol `[Changelog]` tampil dan aktif

### TC-FA-CAID-24: Config-Update (blok 3)

10. Ganti akun: logout akun Read Only, lalu login sebagai Config-Update (Pre-setup No 3)
11. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
12. Verifikasi Tabs Bar memuat tab `Custom Asset ID`
13. Verifikasi Master Switch, Separator, Daftar Segmen, input Initial Company, `[Save]`, `[View Code List]`, dan `[Changelog]` tampil dan aktif
14. Verifikasi tidak ada kontrol yang berstatus Disabled 🔖

### TC-FA-CAID-25: Config-Read (blok 4)

15. Ganti akun: logout akun Config-Update, lalu login sebagai Config-Read (Pre-setup No 4)
16. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
17. Verifikasi Tabs Bar memuat tab `Custom Asset ID`
18. Verifikasi Master Switch, Separator, checkbox dan drag handle Daftar Segmen, dan input Initial Company tampil dengan status Disabled 🔖
19. Verifikasi tombol `[Save]` tidak tampil (Hidden)
20. Verifikasi tautan `[View Code List]` dan tombol `[Changelog]` tampil dan aktif

### TC-FA-CAID-26: Master-Data-Only (blok 5)

21. Ganti akun: logout akun Config-Read, lalu login sebagai Master-Data-Only (Pre-setup No 5)
22. Buka Fixed Asset > Settings > Asset Master
23. Verifikasi Tabs Bar memuat tab `Asset Name` dan `Labels` saja
24. Verifikasi tab `Custom Asset ID` tidak dirender sama sekali (Hidden)
25. Verifikasi tidak ada chip Upgrade dan tidak ada tab terkunci pada Tabs Bar

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ditulis per blok role (bagian 3a konvensi): langkah dan Expected tiap role berbeda, dan ganti akun menuntut langkah eksplisit karena hanya akun pertama yang login di hook `before` (langkah 4, 10, 15, 21). Langkah pembuka TC-FA-CAID-22 dipenuhi hook `beforeEach` suite.
- Langkah penghubung (tanpa `Verifikasi`): langkah 4, 10, 15, 21 (ganti akun) dan langkah 5, 11, 16, 22 (membuka halaman untuk akun yang login di tengah spec).
- Asersi absence Hidden (langkah 8, 19, 24, 25) memakai Tabs Bar atau halaman yang sudah termuat sebagai anchor permukaan (langkah 6 dan 7, 17 dan 18, 23).
- Temuan untuk QA:
  - TC-FA-CAID-22 b menyebut input Initial Company "enabled saat checkbox-nya dicentang", padahal baseline B1 tidak mencentangnya dan TC tidak memberi langkah mencentang. Spec mengasersi input tampil dan aktif tidaknya mengikuti kondisi B1; status enabled saat dicentang tidak diamati.
  - TC-FA-CAID-22 c menyebut "tidak ada tooltip izin"; TC tidak memberi langkah hover. Spec mengasersi kontrol tidak ditandai Disabled 🔖 saja.
  - Email akun Pre-setup No 1 sampai 5 hanya tertulis sebagai pola `{namaCompany}`; env var password adalah usulan (lihat `suite.md`).
