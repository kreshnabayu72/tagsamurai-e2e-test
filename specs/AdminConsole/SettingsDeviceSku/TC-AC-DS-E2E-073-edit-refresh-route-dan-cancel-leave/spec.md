---
id: TC-AC-DS-E2E-073-edit-refresh-route-dan-cancel-leave
title: "Edit SKU: Refresh Browser, Berpindah Route, dan Cancel pada Dialog Unsaved Changes"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-248
  - TC-AC-DS-249
  - TC-AC-DS-573
coverage:
  web: automated
---

# Edit SKU: Refresh Browser, Berpindah Route, dan Cancel pada Dialog Unsaved Changes

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU inti dan seed (#29, #30), pohon Category (#25), Device Name (#26), Brand (#27), file foto (#37).
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: baris `HHR-ARC-200` ke Model/Type `H200`; spec tidak menyimpan perubahan. Spec ini tidak menyimpan perubahan data.
- Kemampuan teknis: Penanganan dialog bawaan browser `beforeunload` (konfirmasi dan pembatalan) pada langkah F5 disediakan tim FE; kemampuan ini dibutuhkan karena TC-248 mengasersi konfirmasi bawaan browser (S-08).
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps


### TC-AC-DS-248: refresh browser

1. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
2. Ubah Model/Type menjadi `H-RELOAD`
3. Muat ulang halaman dengan F5
4. Verifikasi konfirmasi bawaan browser muncul karena form berbeda dari nilai tersimpan
5. Batalkan konfirmasi bawaan browser sehingga tetap di halaman
6. Ubah Model/Type kembali menjadi `H200`
7. Muat ulang halaman dengan F5
8. Verifikasi List Device SKU tampil
9. Verifikasi tidak ada konfirmasi bawaan browser karena form identik dengan nilai tersimpan

### TC-AC-DS-249: berpindah route lalu Leave

10. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
11. Ubah Model/Type menjadi `H-ROUTE`
12. Klik item sidebar `Settings`
13. Verifikasi dialog tampil dengan teks "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]`
14. Klik `[Leave]`
15. Verifikasi navigasi dilanjutkan ke halaman Settings
16. Buka Settings > Device > Device SKU
17. Verifikasi baris `HHR-ARC-200` menampilkan Model/Type tersimpan `H200` (perubahan tidak disimpan)

### TC-AC-DS-573: berpindah route lalu Cancel

18. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
19. Ubah Model/Type menjadi `H-ROUTE3`
20. Klik item sidebar `Settings`
21. Verifikasi dialog tampil dengan teks "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]`
22. Klik `[Cancel]`
23. Verifikasi navigasi dibatalkan: popup Edit tetap terbuka
24. Verifikasi input `H-ROUTE3` dipertahankan
25. Klik `✕` pada header popup Edit SKU
26. Verifikasi dialog Unsaved Changes tampil
27. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung: membatalkan konfirmasi bawaan browser setelah F5 pertama, mengembalikan Model/Type ke `H200` sebelum F5 kedua, membuka lagi Settings > Device > Device SKU sesudah navigasi, dan menutup form dirty (langkah 25 sampai 27, S-08).
- Anchor absence F5: asersi "tidak ada konfirmasi bawaan browser" didahului Verifikasi List Device SKU tampil (R-21).
- Temuan untuk QA: TC-248 mengharapkan konfirmasi bawaan browser tetapi isi konfirmasi ditentukan browser dan tidak dapat diasersi teksnya. Post Condition TC-248, TC-249, dan TC-573 kosong.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
