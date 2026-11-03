---
id: TC-AC-DS-E2E-080-bulk-delete-select-all-unselect-all-dan-retensi-seleksi
title: "Bulk Action Bar: Select All Lintas Halaman, Unselect All, dan Seleksi Dipertahankan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-275
  - TC-AC-DS-276
  - TC-AC-DS-280
coverage:
  web: automated
---

# Bulk Action Bar: Select All Lintas Halaman, Unselect All, dan Seleksi Dipertahankan

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU seed `SEED-001` sampai `SEED-119` dan SKU inti (#29, #30); Selection Limit entitas uji bernilai 1000 (Pre-setup #36, tidak diubah spec ini); total SKU Principal 129 (10 inti + 119 seed, Pre-setup #29 dan #30).
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: tidak ada data tersimpan yang berubah (spec hanya memilih baris). Spec ini tidak menyimpan perubahan data.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps


### TC-AC-DS-275: Select All lintas halaman

1. Centang checkbox baris `SEED-001`
2. Klik tombol "Select All (129 records)"
3. Verifikasi counter menampilkan "129 SKUs selected"
4. Verifikasi tombol berubah menjadi "Unselect All"
5. Pindah ke halaman 2
6. Verifikasi seluruh baris halaman 2 tetap tercentang
7. Pindah ke halaman 13
8. Verifikasi seluruh baris halaman 13 tetap tercentang

### TC-AC-DS-276: Unselect All dan kembali ke Select All

9. Klik "Unselect All"
10. Pindah ke halaman 1, lalu centang checkbox baris `SEED-001`
11. Klik tombol "Select All (129 records)"
12. Verifikasi tombol berubah menjadi "Unselect All" pada seleksi penuh
13. Hilangkan centang satu baris pada halaman 1
14. Verifikasi tombol kembali menjadi "Select All (129 records)"
15. Verifikasi bar bulk tetap tampil
16. Verifikasi counter menampilkan "128 SKUs selected"
17. Klik tombol "Select All (129 records)"
18. Klik "Unselect All"
19. Verifikasi seluruh seleksi dibatalkan
20. Verifikasi bar bulk hilang

### TC-AC-DS-280: seleksi dipertahankan

21. Centang checkbox baris `SEED-001` dan `SEED-002`
22. Pindah ke halaman 2, lalu kembali ke halaman 1
23. Verifikasi counter tetap "2 SKUs selected" setelah pindah halaman
24. Verifikasi baris `SEED-001` dan `SEED-002` tetap tercentang saat tampil kembali
25. Ketik Search `HHR`, tekan Enter
26. Verifikasi counter tetap "2 SKUs selected" setelah Search diubah
27. Klik `(←)` pada kotak Search
28. Urutkan kolom SKU descending
29. Verifikasi counter tetap "2 SKUs selected" setelah Sort diganti
30. Klik ikon `(✕)` pada bar

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: "Unselect All", memilih ulang `SEED-001`, dan ikon `(✕)` pada langkah terakhir membersihkan seleksi antar blok (S-09). TC-276 menyebut klik "Select All (129 records)" sebagai langkah pertama tanpa seleksi awal; tombol itu hanya ada pada bar bulk sehingga satu baris dicentang lebih dulu.
- Temuan untuk QA: TC-276 Expected b menyebut "jumlah total baris terfilter" sebagai nilai 129 tanpa filter aktif; spec tidak memakai filter. Post Condition TC-275, TC-276, dan TC-280 kosong.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
