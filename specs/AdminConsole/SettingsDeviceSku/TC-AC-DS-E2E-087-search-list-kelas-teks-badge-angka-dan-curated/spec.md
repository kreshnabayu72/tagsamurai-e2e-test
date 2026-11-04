---
id: TC-AC-DS-E2E-087-search-list-kelas-teks-badge-angka-dan-curated
title: "Search List: Pencocokan per Kelas Teks, Badge, Angka, dan Kolom Curated"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-298
  - TC-AC-DS-299
  - TC-AC-DS-300
  - TC-AC-DS-301
coverage:
  web: automated
---

# Search List: Pencocokan per Kelas Teks, Badge, Angka, dan Kolom Curated

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU inti dan seed (#29, #30), pohon Category (#25), Device Name (#26), Brand (#27), file foto (#37).
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: tidak ada data tersimpan yang berubah; pemulihan konfigurasi kolom List yang diubah spec dilakukan pada langkah 31 sampai 33 dan, sebagai cadangan, dengan menghapus preferensi kolom di browser pada hook `after` (kemampuan disediakan tim FE, bagian 4). Spec ini tidak menyimpan perubahan data.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps


### TC-AC-DS-298: kelas teks

1. Ketik Search `Industrial`, tekan Enter
2. Verifikasi baris `HHR-BIG-01` (Device Name `Industrial Handheld Reader`) tampil
3. Verifikasi hasil Search hanya memuat baris `HHR-BIG-01`
4. Ganti isi kotak search dengan `BLE-KIN`, tekan Enter
5. Verifikasi baris `BLE-KIN-GW1` tampil
6. Verifikasi hasil Search hanya memuat baris `BLE-KIN-GW1`
7. Ganti isi kotak search dengan `T-USR`, tekan Enter
8. Verifikasi baris `TAG-ARC-USR` tampil
9. Verifikasi hasil Search hanya memuat baris `TAG-ARC-USR`

### TC-AC-DS-299: kelas badge Category dan Brand

10. Ganti isi kotak search dengan `Portal`, tekan Enter
11. Verifikasi baris `SFR-VEL-4P` (badge Category `Portal Reader`) tampil
12. Verifikasi hasil Search hanya memuat baris `SFR-VEL-4P`
13. Ganti isi kotak search dengan `Veltrix`, tekan Enter
14. Verifikasi baris `SFR-VEL-4P` dan `SFR-ZERO-01` tampil
15. Verifikasi hasil Search hanya memuat baris `SFR-VEL-4P` dan `SFR-ZERO-01`

### TC-AC-DS-300: kelas angka

16. Ganti isi kotak search dengan `12500`, tekan Enter
17. Verifikasi baris `HHR-BIG-01` tampil
18. Verifikasi hasil Search hanya memuat baris `HHR-BIG-01`

### TC-AC-DS-301: kolom curated setelah di-unhide

19. Klik header kolom Actions `(⋯)`, lalu centang `Hardware Type` pada Column Visibility
20. Klik header kolom Actions `(⋯)`, lalu centang `Range Type` pada Column Visibility
21. Klik header kolom Actions `(⋯)`, lalu centang `TAG Type` pada Column Visibility
22. Ganti isi kotak search dengan `Smart Fixed`, tekan Enter
23. Verifikasi baris `SFR-VEL-4P` dan `SFR-ZERO-01` tampil
24. Verifikasi hasil Search hanya memuat baris `SFR-VEL-4P` dan `SFR-ZERO-01`
25. Ganti isi kotak search dengan `Long Range`, tekan Enter
26. Verifikasi baris `HHR-ARC-100` tampil
27. Verifikasi hasil Search hanya memuat baris `HHR-ARC-100`
28. Ganti isi kotak search dengan `User`, tekan Enter
29. Verifikasi baris `TAG-ARC-USR` tampil
30. Verifikasi hasil Search hanya memuat baris `TAG-ARC-USR`

### Pemulihan state akhir

31. Klik header kolom Actions `(⋯)`, lalu hilangkan centang `Hardware Type` pada Column Visibility
32. Klik header kolom Actions `(⋯)`, lalu hilangkan centang `Range Type` pada Column Visibility
33. Klik header kolom Actions `(⋯)`, lalu hilangkan centang `TAG Type` pada Column Visibility

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Asersi "hanya menampilkan baris" adalah asersi universal: tiap Search didahului Verifikasi yang membuktikan baris target tampil sebagai pembanding (bagian 8b butir 2). Search kedua dan seterusnya memakai "ganti isi kotak search" (bagian 8b butir 9).
- Langkah penghubung pemulihan (tanpa `Verifikasi`, S-03, S-09): langkah 31 sampai 33 menyembunyikan kembali kolom curated yang di-unhide pada langkah 19 sampai 21; hook `after` tetap menghapus preferensi kolom sebagai cadangan.
- Temuan untuk QA: TC-298 sampai TC-301 menyebut hasil "hanya" baris tertentu bergantung pada data seed 129 SKU yang tidak mengandung kata kunci yang sama; Post Condition TC-298 sampai TC-301 kosong.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
