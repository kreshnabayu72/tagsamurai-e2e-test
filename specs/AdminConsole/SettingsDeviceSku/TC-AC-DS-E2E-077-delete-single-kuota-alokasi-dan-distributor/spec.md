---
id: TC-AC-DS-E2E-077-delete-single-kuota-alokasi-dan-distributor
title: "Delete SKU: Kuota Alokasi Category, Stok Dipegang Client, serta Distributor Stok 0 dan Berstok"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-264
  - TC-AC-DS-265
  - TC-AC-DS-266
  - TC-AC-DS-267
coverage:
  web: automated
---

# Delete SKU: Kuota Alokasi Category, Stok Dipegang Client, serta Distributor Stok 0 dan Berstok

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |
| Ganti akun: Total Control Distributor PT Cakra Distribusi, `Dewi Lestari`, Local Registration aktif (Pre-setup #10) | `totalControlDist_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_DIST_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU Principal `SRT-ANG-01` (stok 0, Category Asset TAG) dan `HHR-ARC-100` dari #29; kuota alokasi Category `Asset TAG` dan `Portal Reader` untuk PT Cakra Distribusi pada Device Allocation (Pre-setup #40); SKU lokal Distributor `LOC-NOR-01` (stok 14), `LOC-NOR-02`, `LOC-NOR-03` (stok 0) dari #31; Client PT Surya Logistik (#24).
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: baris `SRT-ANG-01` (dihapus TC-264) dan `LOC-NOR-03` (dihapus TC-266) dibuat ulang; `LOC-NOR-02` dikembalikan ke stok Distributor 0 tanpa unit Client. Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Kemampuan teknis: Fixture BE untuk menyetel `LOC-NOR-02` menjadi 4 unit yang hanya dipegang Client PT Surya Logistik (stok Distributor 0), diset sebelum TC-265 dan dipulihkan oleh hook `after` (Pre-setup #40).
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps


### TC-AC-DS-264: kuota alokasi Category tidak memblokir Delete

1. Ketik Search `SRT-ANG-01`, tekan Enter
2. Klik `⋯` pada baris `SRT-ANG-01`, lalu pilih `Delete`
3. Klik `[Delete]`
4. Verifikasi muncul toast sukses "Success, device SKU has been deleted."
5. Verifikasi baris `SRT-ANG-01` hilang dari List walau Category `Asset TAG` memiliki kuota alokasi di Device Allocation

### Ganti akun ke Total Control Distributor PT Cakra Distribusi

6. Logout dari akun Total Control Principal
7. Login sebagai Total Control Distributor PT Cakra Distribusi (`Spectra.env.AC_DS_DIST_PASSWORD`)
8. Buka Settings > Device > Device SKU

### TC-AC-DS-265: stok hanya dipegang Client

9. Setel `LOC-NOR-02` menjadi 4 unit yang hanya dipegang Client PT Surya Logistik lewat fixture BE hingga tersimpan
10. Ketik Search `LOC-NOR-02`, tekan Enter
11. Klik `⋯` pada baris `LOC-NOR-02`, lalu pilih `Delete`
12. Verifikasi dialog blok "Cannot Delete SKU" tampil dengan bullet `LOC-NOR-02` dan body "This SKU still has stock. Remove all stock before deleting."
13. Verifikasi tidak ada toast
14. Klik `[OK]`
15. Verifikasi baris `LOC-NOR-02` tetap ada (SKU tidak terhapus)

### TC-AC-DS-267: SKU lokal Distributor berstok

16. Ganti isi kotak search dengan `LOC-NOR-01`, tekan Enter
17. Klik `⋯` pada baris `LOC-NOR-01`, lalu pilih `Delete`
18. Verifikasi dialog blok "Cannot Delete SKU" tampil dengan bullet `LOC-NOR-01` dan tombol `[OK]`
19. Verifikasi tidak ada toast
20. Klik `[OK]`

### TC-AC-DS-266: SKU lokal Distributor stok 0

21. Ganti isi kotak search dengan `LOC-NOR-03`, tekan Enter
22. Klik `⋯` pada baris `LOC-NOR-03`, lalu pilih `Delete`
23. Klik `[Delete]`
24. Verifikasi muncul toast sukses "Success, device SKU has been deleted."
25. Verifikasi baris `LOC-NOR-03` hilang dari List Distributor
26. Ganti isi kotak search dengan `HHR-ARC-100`, tekan Enter
27. Verifikasi baris SKU Principal `HHR-ARC-100` tetap tampil (SKU Principal tidak berubah)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Penyimpangan urutan: TC-264 (akun Principal) mendahului blok Distributor untuk meminimalkan pergantian akun; TC-267 (diblok) dijalankan sebelum TC-266 (menghapus) mengikuti S-10. Ganti akun ditulis eksplisit (S-07); hook `after` mengembalikan sesi ke akun default suite.
- Langkah penghubung: Search pada langkah 1 sampai 21 menemukan baris target di luar halaman 1 (default sort SKU A-Z, Pre-setup #29, #30, dan #31); Search `HHR-ARC-100` pada langkah terakhir hanya menemukan baris pembanding.
- Temuan untuk QA: TC-264 mengubah data Pre-setup `SRT-ANG-01` (dihapus) dan TC-266 menghapus `LOC-NOR-03`; keduanya dipulihkan oleh fixture BE (S-06, belum dinyatakan di suite.md). TC-265 mensyaratkan stok khusus Client lewat fixture BE yang tidak didefinisikan di TC.
- Post Condition TC-264 dan TC-266 (entri log tiga surface) tidak diasersi karena TC tidak memberi langkah observasinya (S-01).
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
