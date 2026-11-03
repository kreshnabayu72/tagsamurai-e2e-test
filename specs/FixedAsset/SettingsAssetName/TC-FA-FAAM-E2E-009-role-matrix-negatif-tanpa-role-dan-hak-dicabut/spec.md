---
id: TC-FA-FAAM-E2E-009-role-matrix-negatif-tanpa-role-dan-hak-dicabut
title: "Role Matrix Negatif: Tanpa Role Ini dan Hak Dicabut Saat Modal Terbuka"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-51
  - TC-FA-FAAM-617
  - TC-FA-FAAM-618
coverage:
  web: automated
---

# Role Matrix Negatif: Tanpa Role Ini dan Hak Dicabut Saat Modal Terbuka

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji (Pre-setup #5 dan #8):

| Role | Akun (Pre-setup) | Env password | Dipakai di |
|---|---|---|---|
| Update-Only | `updateOnly_automated_{namaCompany}@qwertysystem.net` (#5) | `Spectra.env.FA_UO_PASSWORD` | TC-FA-FAAM-618 (akun pertama, login di hook `before`) |
| Tanpa Role Ini | `noAssetMasterRole_automated_{namaCompany}@qwertysystem.net` (#8) | `Spectra.env.FA_NR_PASSWORD` | TC-FA-FAAM-51 dan TC-FA-FAAM-617 (ganti akun eksplisit, langkah 13) |

- Login akun pertama (Update-Only) di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture. Semua nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, `after`, dan sesi API aktor dirujuk apa adanya.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.catalog`): `Dell Latitude` (#10) sebagai target Edit yang tidak tersimpan (Save ditolak); nilai Code baru `DLAT-REV` adalah pilihan spec (TC hanya menulis "Ubah Code"). URL halaman Settings > Asset Master dirujuk lewat fixture baru `Fixture.faAssetName.assetMasterUrl` (tidak tertulis di TC).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor Total Control yang mencabut permission Update dari akun Update-Only (langkah 3). Pemulihan: hook `after` memulihkan permission Update akun Update-Only ke keadaan Pre-setup #5 supaya spec lain yang memakai akun itu tidak terpengaruh.
- State global: permission akun Update-Only dicabut pada langkah 3 dan dipulihkan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-618: Hak aktor dicabut saat modal terbuka: Save ditolak, modal ditutup dan tabel di-refresh

1. Ketik Search `Dell Latitude`, tekan Enter
2. Klik `⋯` baris `Dell Latitude` lalu `Edit`
3. Sesi API aktor Total Control mencabut permission Update akun Update-Only hingga tersimpan
4. Tunggu aksi selesai (pencabutan permission tersimpan)
5. Ubah Code menjadi `DLAT-REV`
6. Klik `[Save]`
7. Verifikasi toast `You don't have permission to do this.`
8. Verifikasi modal ditutup otomatis
9. Verifikasi tabel di-refresh
10. Klik `⋯` baris `Dell Latitude`
11. Verifikasi menu `⋯` baris `Dell Latitude` memuat `Detail`
12. Verifikasi aksi `Edit` Hidden
13. Ganti akun: Logout, login sebagai Tanpa Role Ini (`noAssetMasterRole_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_NR_PASSWORD`), lalu buka halaman utama FAMS

### TC-FA-FAAM-51: Pemegang tanpa Role ini tidak melihat menu Asset Master

14. Verifikasi sedikitnya satu item menu lain pada sidebar FAMS tampil
15. Verifikasi item `Settings > Asset Master` tidak tampil di sidebar (Hidden)
16. Verifikasi tidak ada akses ke tab Asset Name sehingga tidak ada notice Category Locked

### TC-FA-FAAM-617: Direct URL tanpa Role ini memunculkan toast 403 dan refresh UI

17. Ketik URL halaman Settings > Asset Master langsung di address bar
18. Verifikasi toast `You don't have permission to do this.`
19. Verifikasi UI di-refresh
20. Verifikasi tidak ada redirect ke halaman unauthorized

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 618, 51, 617. Hook `beforeEach` suite membuka tab Asset Name, yang tidak dapat dibuka akun Tanpa Role Ini; karena itu akun pertama adalah Update-Only (TC-618) dan ganti akun ke Tanpa Role Ini terjadi sesudahnya (S-07, S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 (Search untuk menemukan baris target, R-16), langkah 4 (menunggu aksi pelaku kedua selesai, bagian 8b butir 8), langkah 13 (ganti akun eksplisit dan membuka halaman utama FAMS sebagai precondition TC-51).
- Pelaku kedua memakai sesi API (bukan konteks UI kedua): tidak memakai `P-2`. Langkah pemicu ditulis "... hingga ... tersimpan" (R-20).
- Langkah 11 adalah anchor positif untuk asersi absence `Edit` pada langkah 12 (bagian 8b butir 2); langkah 14 adalah anchor positif untuk absence item menu pada langkah 15.
- Langkah 16 adalah kesimpulan dari langkah 15 (tanpa item menu tidak ada jalur ke tab Asset Name) dan tidak teramati terpisah (S-03).
- Temuan untuk QA:
  - TC-618 Langkah 2 "Di sesi lain cabut permission Update aktor" tidak menyebut siapa pelaku dan mekanismenya; spec menuliskannya sebagai kemampuan sesi API aktor Total Control yang disediakan tim FE/BE, dengan pemulihan di hook `after`.
  - TC-618 Expected a "tabel di-refresh" tidak menyebut cara mengamatinya; spec mengasersi tabel dimuat ulang tanpa menyebut request.
  - TC-618 Langkah 3 "Ubah Code" tidak menyebut nilai Code baru; spec memakai `DLAT-REV`.
  - TC-617 Langkah 1 tidak menyebut URL halaman; spec merujuk fixture `Fixture.faAssetName.assetMasterUrl` yang disediakan tim FE.
  - TC-617 Expected a menyebut toast tetapi tidak menyebut apakah halaman Asset Master sempat terbuka; spec mengasersi toast, UI di-refresh, dan tidak ada redirect sesuai Expected.
  - TC-51 Expected b ("tidak ada akses ke tab Asset Name sehingga tidak ada notice Category Locked") adalah kesimpulan tanpa Langkah observasi tersendiri; akses langsung diuji di TC-617.
