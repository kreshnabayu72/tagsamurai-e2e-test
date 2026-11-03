---
id: TC-AC-DS-E2E-088-search-list-kolom-hidden-tanggal-photo-trim-dan-reset-paginasi
title: "Search List: Kolom Hidden, Kolom Tanggal dan Photo Tidak Dapat Dicari, Trim Spasi, dan Reset Paginasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-302
  - TC-AC-DS-303
  - TC-AC-DS-304
  - TC-AC-DS-308
  - TC-AC-DS-310
coverage:
  web: automated
---

# Search List: Kolom Hidden, Kolom Tanggal dan Photo Tidak Dapat Dicari, Trim Spasi, dan Reset Paginasi

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU inti dan seed (#29, #30), pohon Category (#25), Device Name (#26), Brand (#27), file foto (#37).
- General Settings entitas uji: Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta (Pre-setup #35, tidak diubah).
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: tidak ada data tersimpan yang berubah; pemulihan konfigurasi kolom List yang diubah spec dilakukan dengan menghapus preferensi kolom di browser pada hook `after` (kemampuan disediakan tim FE, bagian 4). Spec ini tidak menyimpan perubahan data.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps


### TC-AC-DS-302: kolom curated Hidden lalu di-unhide

1. Ketik Search `Smart Fixed`, tekan Enter
2. Verifikasi "No results found" tampil karena kolom Hardware Type Hidden
3. Klik header kolom Actions `(⋯)`, lalu centang `Hardware Type` pada Column Visibility
4. Tekan Enter pada kotak Search yang sama
5. Verifikasi baris `SFR-VEL-4P` dan `SFR-ZERO-01` tampil
6. Klik header kolom Actions `(⋯)`, lalu hilangkan centang `Hardware Type`
7. Tekan Enter pada kotak Search yang sama
8. Verifikasi "No results found" tampil kembali (reversibel)

### TC-AC-DS-303: kolom tampil yang di-hide

9. Klik header kolom Actions `(⋯)`, lalu hilangkan centang `Brand`
10. Ganti isi kotak search dengan `Veltrix`, tekan Enter
11. Verifikasi "No results found" tampil karena kolom Brand Hidden
12. Ganti isi kotak search dengan `SF-4`, tekan Enter
13. Verifikasi baris `SFR-VEL-4P` tampil (kolom Model/Type yang tampil tetap dapat dicari)
14. Klik header kolom Actions `(⋯)`, lalu centang `Brand`

### TC-AC-DS-304: kolom tanggal dan Photo tidak searchable

15. Ganti isi kotak search dengan `01/10/26`, tekan Enter
16. Verifikasi "No results found" tampil untuk kata kunci `01/10/26`
17. Ganti isi kotak search dengan `28/09/26 14:40`, tekan Enter
18. Verifikasi "No results found" tampil untuk kata kunci `28/09/26 14:40`
19. Ganti isi kotak search dengan `foto`, tekan Enter
20. Verifikasi "No results found" tampil untuk kata kunci `foto`

### TC-AC-DS-308: spasi tepi kata kunci

21. Ganti isi kotak search dengan `  HHR-ARC-100  `, tekan Enter
22. Verifikasi hasil Search memuat baris `HHR-ARC-100`, sama dengan kata kunci `HHR-ARC-100`
23. Verifikasi isi kotak pencarian tetap apa adanya (spasi tepi tetap terlihat)
24. Ganti isi kotak search dengan `   `, tekan Enter
25. Verifikasi tabel kembali menampilkan seluruh SKU (kata kunci spasi saja diperlakukan sebagai kosong)

### TC-AC-DS-310: Search dari halaman lebih dari 1

26. Klik nomor halaman 3
27. Ganti isi kotak search dengan `SEED`, tekan Enter
28. Verifikasi hasil Search tampil pada halaman 1
29. Verifikasi indikator halaman menunjukkan 1

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: menghidupkan kembali kolom `Brand` sesudah TC-303 (S-09); kolom `Hardware Type` kembali Hidden pada TC-302 sehingga tidak perlu pemulihan lain. Pemulihan preferensi kolom pada hook `after`.
- Anchor: "No results found" hasil Search adalah anchor positif absence hasil Search (bagian 8b butir 2); TC-303 Expected b memakai baris `SFR-VEL-4P` sebagai pembanding; TC-308 Expected c memakai tampilnya seluruh SKU.
- Temuan untuk QA: TC-304 Expected c ("Penyaringan menurut tanggal dilakukan lewat Filter Panel") adalah pernyataan yang tidak dapat diasersi sebagai kondisi UI dan tidak diasersi; TC-310 menyebut "nomor halaman 3" sehingga Search tanpa filter dengan 129 SKU (13 halaman) dipakai. Post Condition TC-302 sampai TC-310 kosong.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
