---
id: TC-AC-DS-E2E-072-edit-penutupan-popup-ikon-esc-backdrop-dan-unsaved
title: "Edit SKU: Penutupan Popup Tanpa Perubahan dan Setelah Perubahan, Esc, Backdrop, dan Dialog Unsaved Changes"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-243
  - TC-AC-DS-244
  - TC-AC-DS-245
  - TC-AC-DS-246
  - TC-AC-DS-247
coverage:
  web: automated
---

# Edit SKU: Penutupan Popup Tanpa Perubahan dan Setelah Perubahan, Esc, Backdrop, dan Dialog Unsaved Changes

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU inti dan seed (#29, #30), pohon Category (#25), Device Name (#26), Brand (#27), file foto (#37).
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: baris `HHR-ARC-200` ke Model/Type `H200`; spec tidak menyimpan perubahan. Spec ini tidak menyimpan perubahan data.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps


### TC-AC-DS-243: tutup popup tanpa perubahan

1. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
2. Klik ikon close `[✕]` pada header popup Edit SKU
3. Verifikasi popup Edit langsung tertutup lewat ikon close
4. Verifikasi dialog Unsaved Changes tidak muncul setelah ikon close
5. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
6. Tekan Esc
7. Verifikasi popup Edit langsung tertutup lewat Esc
8. Verifikasi dialog Unsaved Changes tidak muncul setelah Esc

### TC-AC-DS-244: tutup popup yang diubah

9. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
10. Ubah Model/Type menjadi `H-DIRTY`
11. Klik ikon close `[✕]` pada header popup Edit SKU
12. Verifikasi dialog tampil dengan teks "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]`
13. Klik `[Cancel]`
14. Verifikasi popup Edit tetap terbuka
15. Verifikasi input `H-DIRTY` dipertahankan
16. Klik ikon close `[✕]` pada header popup Edit SKU
17. Verifikasi dialog Unsaved Changes tampil
18. Klik `[Leave]`
19. Verifikasi popup Edit tertutup tanpa menyimpan
20. Verifikasi baris `HHR-ARC-200` menampilkan Model/Type tersimpan `H200`

### TC-AC-DS-245: Esc pada popup yang diubah

21. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
22. Ubah Model/Type menjadi `H-DIRTY2`
23. Tekan Esc
24. Verifikasi dialog Unsaved Changes tampil setelah Esc pertama
25. Tekan Esc
26. Verifikasi dialog tertutup seperti `[Cancel]`
27. Verifikasi popup Edit tetap terbuka
28. Klik `✕` pada header popup Edit SKU
29. Verifikasi dialog Unsaved Changes tampil
30. Klik `[Leave]`

### TC-AC-DS-246: klik backdrop

31. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
32. Klik area backdrop
33. Verifikasi popup Edit tetap terbuka tanpa perubahan
34. Ubah Model/Type menjadi `H-BACK`
35. Klik area backdrop
36. Verifikasi popup Edit tetap terbuka setelah perubahan
37. Verifikasi dialog Unsaved Changes tidak muncul
38. Verifikasi input `H-BACK` dipertahankan
39. Klik `✕` pada header popup Edit SKU
40. Verifikasi dialog Unsaved Changes tampil
41. Klik `[Leave]`

### TC-AC-DS-247: mengubah lalu mengembalikan nilai

42. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
43. Ubah Model/Type menjadi `H-REV`
44. Ubah Model/Type kembali menjadi `H200`
45. Klik ikon close `[✕]` pada header popup Edit SKU
46. Verifikasi popup Edit langsung tertutup
47. Verifikasi dialog Unsaved Changes tidak muncul karena nilai identik dengan nilai tersimpan

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Alasan di atas sekitar 35 langkah (47 langkah; bagian 3, prinsip 13): kelima TC menguji penutupan popup Edit yang sama pada baris yang sama tanpa menyimpan data; tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah berlebih berasal dari pembukaan ulang popup per blok, pemecahan Expected per klausa (S-01), dan penutupan form dirty (S-08).
- Langkah penghubung: langkah 28 sampai 30 dan 39 sampai 41 menutup form dirty (S-08) setelah asersi blok TC-245 dan TC-246.
- Temuan untuk QA: TC-245 langkah 5 menekan Esc kedua pada dialog tanpa menyebut hasil pada popup; spec mengasersi dialog tertutup dan popup tetap terbuka sesuai Expected b. Post Condition TC-243 sampai TC-247 kosong.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
