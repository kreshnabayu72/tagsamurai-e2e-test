---
id: TC-AC-DS-E2E-021-role-matrix-positif-delete-sku
title: "Role Matrix Positif: Delete-Only Principal dan Distributor Menyelesaikan Delete Single dan Bulk Delete"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-72
  - TC-AC-DS-73
  - TC-AC-DS-76
coverage:
  web: automated
---

# Role Matrix Positif: Delete-Only Principal dan Distributor Menyelesaikan Delete Single dan Bulk Delete

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (akun blok 1 login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun blok 2 diganti lewat langkah eksplisit; hook `after` mengembalikan sesi ke akun default suite):

| Blok | TC | Role | Akun | Env var |
|---|---|---|---|---|
| 1 | TC-AC-DS-72, TC-AC-DS-73 | Delete-Only Principal PT Arunika Prima (Pre-setup #6) | `manageSkuD_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_D_PASSWORD` |
| 2 | TC-AC-DS-76 | Delete-Only Distributor PT Cakra Distribusi (Pre-setup #14) | `manageSkuDistD_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_DIST_D_PASSWORD` |

- Data Pre-setup (dibaca saja, tidak diubah): SKU inti #29 dan seed #30 (SKU Principal), SKU Distributor #31. Dirujuk lewat `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`, disediakan tim FE, belum ada). Total SKU pada Pagination akun Distributor dicatat sebelum Delete (langkah 18) dan dipakai sebagai pembanding relatif pada langkah 30; angka absolut tidak diturunkan dari seeding.
- Data milik spec (hook `before`, lewat sesi API aktor Principal dan Distributor serta fixture BE yang disediakan tim BE/FE; menggantikan `TAG-ARC-OBJ`, `SRT-ANG-01`, `SRT-APL-01`, `LOC-NOR-02`, `LOC-NOR-03`, dan `LOC-NOR-01` agar data Pre-setup tidak berubah, S-06; semua berstok 0 dan 1 foto):
  - SKU Principal (Device Name `Asset TAG`, Category `Asset TAG`, Brand `Arcturus`): `DEL1-{runId}-021` (TC-72), `DEL2-{runId}-021` dan `DEL3-{runId}-021` (TC-73).
  - SKU Distributor PT Cakra Distribusi (Device Name `Asset TAG`, Category `Asset TAG`, Brand `Nordik`): `DDEL1-{runId}-021` (Delete single), `DDEL2-{runId}-021` (Bulk Delete), dan `DKEEP-{runId}-021` (tidak dicentang pada Bulk Delete, menggantikan `LOC-NOR-01`).
  - Hook `after` menghapus SKU yang masih ada (termasuk `DKEEP-{runId}-021`) lewat fixture BE.
- Env var `AC_DS_D_PASSWORD` dan `AC_DS_DIST_D_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Suite berjalan serial (`parallel: false`); hook suite sesuai `suite.md`. Tidak ada state global yang diubah.

## Test Steps

### Blok 1: Delete-Only Principal (TC-AC-DS-72 dan TC-AC-DS-73)

1. Ketik Search `DEL1-{runId}-021`, tekan Enter
2. Klik ⋯ baris `DEL1-{runId}-021` lalu pilih `Delete`
3. Klik `[Delete]` pada dialog konfirmasi
4. Verifikasi toast sukses: "Success, device SKU has been deleted."
5. Verifikasi baris `DEL1-{runId}-021` hilang dari List
6. Ganti isi kotak search dengan `-{runId}-021`, tekan Enter
7. Centang checkbox baris `DEL2-{runId}-021`
8. Centang checkbox baris `DEL3-{runId}-021`
9. Pilih aksi Delete dari Bulk Action
10. Klik `[Delete]` pada dialog konfirmasi
11. Verifikasi toast sukses: "Success, device SKU has been deleted."
12. Verifikasi baris `DEL2-{runId}-021` dan `DEL3-{runId}-021` hilang dari List
13. Verifikasi bar bulk tertutup
14. Klik `(←)` pada kotak Search

### Blok 2: Delete-Only Distributor (TC-AC-DS-76)

15. Ganti akun: Logout dari akun Delete-Only Principal
16. Login sebagai Delete-Only Distributor `manageSkuDistD_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DS_DIST_D_PASSWORD`
17. Buka halaman `Settings > Device > Device SKU`
18. Catat total SKU pada Pagination sebagai N
19. Ketik Search `-{runId}-021`, tekan Enter
20. Klik ⋯ baris `DDEL1-{runId}-021` lalu pilih `Delete`
21. Klik `[Delete]` pada dialog konfirmasi
22. Verifikasi toast sukses Delete single: "Success, device SKU has been deleted."
23. Verifikasi baris `DDEL1-{runId}-021` hilang dari List
24. Centang checkbox baris `DDEL2-{runId}-021`
25. Pilih aksi Delete dari Bulk Action
26. Klik `[Delete]` pada dialog konfirmasi
27. Verifikasi toast sukses Delete bulk: "Success, device SKU has been deleted."
28. Verifikasi baris `DDEL2-{runId}-021` hilang dari List
29. Klik `(←)` pada kotak Search
30. Verifikasi total SKU pada Pagination sama dengan N dikurangi 2 (hanya `DDEL1-{runId}-021` dan `DDEL2-{runId}-021` yang terhapus), sehingga baris SKU Principal tidak berubah

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (akun blok 1 login di hook `before`, bagian 3a). Urutan TC dalam spec: TC-72, TC-73, TC-76. Aksi menghapus data berada di akhir tiap blok (S-10).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 6, 19 (Search untuk menemukan baris target; langkah 6 dan 19 memakai fragmen suffix agar semua baris milik spec tampil bersama, R-16), 2, 3, 7 sampai 10, 20, 21, 24 sampai 26 (aksi Delete dan Bulk Delete yang hasilnya diasersi pada langkah berikutnya), 14 dan 29 (mengosongkan Search, S-09), 15 sampai 17 (ganti akun dan membuka halaman), 18 (mencatat total N sebelum Delete, S-12).
- Langkah 5, 12, dan 23, 28 (absence baris sesudah Delete) memakai toast sukses langkah 4, 11, 22, dan 27 sebagai anchor (8b butir 2).
- Langkah 30 membandingkan total Pagination dengan N yang dicatat pada langkah 18 (selisih tepat 2), bukan dengan angka dari seeding, karena total yang tampil bagi Distributor dipengaruhi SKU milik spec dan tidak dapat diturunkan dari seeding (S-12, 8b butir 10). Selisih itu mewujudkan Expected TC-76 c (baris SKU Principal tidak berubah). Baris `DKEEP-{runId}-021` tetap ada sebagai SKU yang tidak dicentang.
- Temuan untuk QA:
  - S-12/S-06: TC menghapus `TAG-ARC-OBJ`, `SRT-ANG-01`, `SRT-APL-01`, `LOC-NOR-02`, dan `LOC-NOR-03` pada data Pre-setup; spec memakai SKU milik spec bersuffix dengan atribut setara (stok 0).
  - Fixture rancangan: ketersediaan Pre-setup #6 dan #14 di environment belum diverifikasi; seeding SKU Principal dan Distributor bergantung pada sesi API aktor yang disediakan tim BE/FE.
  - TC-73 dan TC-76 menyebut bar bulk dengan "2 SKUs selected" atau "1 SKU selected" pada langkah, tetapi Expected tidak mengasersi counter; spec tidak mengasersinya.
  - Post Condition TC-72 dan TC-73 (SKU terhapus permanen, entri Delete di tiga surface log) tidak punya langkah observasi di TC, sehingga tidak diasersi.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
