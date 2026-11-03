---
id: TC-AC-DS-E2E-071-edit-clear-field-saving-state-dan-klik-ganda
title: "Edit SKU: Clear Field (Stok Berisi dan Stok 0) dan Reset Validasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-240
  - TC-AC-DS-241
  - TC-AC-DS-242
coverage:
  web: automated
---

# Edit SKU: Clear Field (Stok Berisi dan Stok 0) dan Reset Validasi

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU inti dan seed (#29, #30), pohon Category (#25), Device Name (#26), Brand (#27), file foto (#37).
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: baris `HHR-ARC-100` dan `HHR-ARC-200` ke nilai Pre-setup #29; spec tidak menekan Save sukses sehingga tidak ada data tersimpan yang berubah. Spec ini tidak menyimpan perubahan data.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (lihat Notes).
- Sumber nilai data: Pre-setup TC (#25 sampai #43); berkas `fixtures/settings-device-sku.json` belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps


### TC-AC-DS-240: Clear Field pada SKU berstok 120

1. Klik `⋯` pada baris `HHR-ARC-100`, lalu pilih `Edit`
2. Klik `[Clear Field]`
3. Verifikasi field Brand kembali ke placeholder "Select brand"
4. Verifikasi field Model/Type kosong
5. Verifikasi slot Photo dikosongkan
6. Verifikasi Category tetap `UHF Handheld` (selalu terkunci)
7. Verifikasi SKU tetap `HHR-ARC-100`
8. Verifikasi Device Name tetap `UHF Handheld Reader`
9. Verifikasi Range Type tetap `Long Range` (terkunci karena stok 120)
10. Verifikasi tidak ada dialog konfirmasi
11. Verifikasi popup Edit tetap terbuka
12. Verifikasi fokus berada pada field editable pertama
13. Klik `✕` pada header popup Edit SKU
14. Verifikasi dialog Unsaved Changes tampil
15. Klik `[Leave]`

### TC-AC-DS-241: Clear Field pada SKU stok 0

16. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
17. Klik `[Clear Field]`
18. Verifikasi field SKU kosong
19. Verifikasi field Model/Type kosong
20. Verifikasi field Brand kosong
21. Verifikasi field Device Name kosong
22. Verifikasi field Range Type kosong
23. Verifikasi slot Photo kosong
24. Verifikasi Category tetap `UHF Handheld`
25. Verifikasi popup Edit tetap terbuka
26. Verifikasi tidak ada dialog konfirmasi
27. Klik `✕` pada header popup Edit SKU
28. Verifikasi dialog Unsaved Changes tampil
29. Klik `[Leave]`

### TC-AC-DS-242: Clear Field mereset status validasi

30. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
31. Hapus seluruh teks Model/Type
32. Klik `[Save]`
33. Verifikasi pesan inline "Model/type must not be empty" tampil
34. Klik `[Clear Field]`
35. Verifikasi semua pesan error dihapus
36. Verifikasi border merah dihapus
37. Verifikasi popup Edit tetap terbuka
38. Klik `✕` pada header popup Edit SKU
39. Verifikasi dialog Unsaved Changes tampil
40. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Alasan di atas sekitar 35 langkah (40 langkah; bagian 3, prinsip 13): ketiga TC Clear Field memakai popup Edit yang sama, tidak menyimpan data, dan berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); langkah tambahan berasal dari penutupan form dirty tiga kali (langkah 13 sampai 15, 27 sampai 29, 38 sampai 40, S-08) dan pemecahan Expected per field (S-01).
- Anchor positif TC-242: langkah 33 membuktikan pesan error tampil sebelum asersi absence pesan error dan border merah dihapus (bagian 8b butir 2); pesan itu berasal dari Langkah Uji TC-242.
- Temuan untuk QA: TC-240 menyebut "fokus pada field editable pertama" tanpa menyatakan field mana; spec mengasersi field editable pertama pada popup. Post Condition TC-240 sampai TC-242 kosong.
- Temuan untuk QA (S-12): Lampiran A tidak punya butir untuk modul ini, padahal asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-200`, `SEED-001`, total 129 SKU). Spec memakai nama literal itu sesuai TC; syarat seeding idempotent, cleanup oleh spec, dan suite serial dipenuhi lewat Pemulihan di Prerequisites. Pengecualian S-12 dan S-06 untuk modul ini belum diputuskan; suite.md belum menyatakan fixture pemulihan Pre-setup.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
