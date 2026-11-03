---
id: TC-AC-DS-E2E-074-edit-referensi-stale-dan-stok-masuk-setelah-form-terbuka
title: "Edit SKU: Device Name dan Brand Dihapus Pelaku Lain serta Stok Masuk setelah Form Terbuka"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-231
  - TC-AC-DS-232
  - TC-AC-DS-237
coverage:
  web: automated
---

# Edit SKU: Device Name dan Brand Dihapus Pelaku Lain serta Stok Masuk setelah Form Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun (password hanya lewat env; semua nama env `AC_DS_*` belum terdaftar di `spectra.config.ts` dan `.env.example`, disediakan tim FE; email akun berbeda dari akun Admin Console lain):

| Peran dalam spec | Email | Env var password |
|---|---|---|
| Aktor utama: Total Control Principal PT Arunika Prima, `Jane Setiawan` (Pre-setup #1) | `totalControlSku_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC_PASSWORD` |
| Pelaku kedua lewat sesi API: Total Control Principal `Budi Kurniawan` (Pre-setup #2) | `totalControlSku2_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DS_TC2_PASSWORD` |

- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite (`before`, `beforeEach`, `after`) dinyatakan di `suite.md`; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Data Pre-setup: SKU inti dan seed (#29, #30), pohon Category (#25), Device Name (#26), Brand (#27), file foto (#37).
- Data khusus (Pre-setup #40): Device Name `Perangkat Sementara` (Category Asset TAG) dan Brand `Brand Sementara`; modul stok Hardware Stock (Pre-setup #39) untuk Add Stock `HHR-ARC-200`.
- Pemulihan: hook `before` menyiapkan secara idempotent (dilewati bila sudah ada) dan hook `after` memulihkan ke keadaan awal Pre-setup lewat fixture BE yang disediakan tim FE/BE: Device Name `Perangkat Sementara` dan Brand `Brand Sementara` dibuat ulang (dihapus pelaku kedua selama spec); baris `HHR-ARC-200` ke stok 0 dan nilai Pre-setup #29; baris `TAG-ARC-OBJ` ke Device Name `Asset TAG`. Efek yang tidak dapat dipulihkan: entri audit trail (Changelog, System Log, Activity Log) bertambah permanen.
- Kemampuan teknis: Sesi API aktor kedua (login API password, tidak dihitung sebagai sesi web; disediakan tim BE/FE) untuk menghapus Device Name, menghapus Brand, dan menambah stok lewat Add Stock Hardware Stock; mekanisme API tidak disebut TC, PRD, atau LLD.
- Suite berjalan serial (`parallel: false`) karena spec memakai data SKU bersama dan nama literal Pre-setup (pengecualian S-12 A-11, lihat Notes).
- Sumber nilai data: `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan tim FE dengan kunci mengikuti Pre-setup #29 dan #30 (ditandai di Notes).

## Test Steps


### TC-AC-DS-232: Brand dihapus pelaku lain

1. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
2. Ubah Brand menjadi `Brand Sementara`
3. Melalui sesi API aktor kedua (`Budi Kurniawan`), hapus Brand `Brand Sementara` hingga penghapusan tersimpan
4. Klik `[Save]`
5. Verifikasi pesan inline pada field Brand "This brand no longer exists. Please select another."
6. Verifikasi field Brand dikosongkan otomatis
7. Buka dropdown Brand
8. Verifikasi opsi Brand lain (mis. `Arcturus`) tampil pada dropdown Brand
9. Verifikasi opsi Brand dimuat ulang tanpa `Brand Sementara`
10. Verifikasi field lain termasuk Photo dipertahankan
11. Klik `✕` pada header popup Edit SKU
12. Verifikasi dialog Unsaved Changes tampil
13. Klik `[Leave]`

### TC-AC-DS-237: stok masuk setelah form terbuka

14. Klik `⋯` pada baris `HHR-ARC-200`, lalu pilih `Edit`
15. Melalui sesi API aktor kedua (`Budi Kurniawan`), tambahkan 1 unit `HHR-ARC-200` lewat Add Stock Hardware Stock hingga Current Stock menjadi 1 tersimpan
16. Ubah SKU menjadi `HHR-ARC-201`
17. Ubah Model/Type menjadi `H201`
18. Klik `[Save]`
19. Verifikasi muncul toast error "Error, failed to update device SKU."
20. Verifikasi field SKU tetap berisi `HHR-ARC-200` pada form yang dimuat ulang
21. Verifikasi field Model/Type tetap berisi `H200` pada form yang dimuat ulang
22. Verifikasi field SKU, Device Name, dan Range Type terkunci dengan tooltip
23. Klik ikon close `[✕]` pada header popup Edit SKU

### TC-AC-DS-231: Device Name dihapus pelaku lain

24. Ketik Search `TAG-ARC-OBJ`, tekan Enter
25. Klik `⋯` pada baris `TAG-ARC-OBJ`, lalu pilih `Edit`
26. Ubah Device Name dari `Asset TAG` menjadi `Perangkat Sementara`
27. Melalui sesi API aktor kedua (`Budi Kurniawan`), hapus Device Name `Perangkat Sementara` hingga penghapusan tersimpan
28. Klik `[Save]`
29. Verifikasi pesan inline pada field Device Name "This device name no longer exists. Please select another."
30. Verifikasi field Device Name dikosongkan otomatis
31. Buka dropdown Device Name
32. Verifikasi opsi Device Name lain (mis. `Asset TAG`) tampil pada dropdown Device Name
33. Verifikasi opsi Device Name dimuat ulang tanpa `Perangkat Sementara`
34. Verifikasi field lain termasuk Photo dipertahankan
35. Klik `✕` pada header popup Edit SKU
36. Verifikasi dialog Unsaved Changes tampil
37. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`; subjudul `###` memetakan langkah ke id TC granular.
- Spec berisi 37 langkah, sedikit di atas sekitar 35 langkah (35 langkah sebelum dua pembanding absence langkah 8 dan 32). Alasan: tiga TC satu topik (referensi stale pada form Edit yang terbuka) berbagi akun, pelaku kedua lewat sesi API, dan fixture pemulihan; memecahnya menggandakan Prerequisites tanpa mengurangi langkah, dan tiap blok tetap berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna).
- Pelaku kedua memakai sesi API (bukan konteks kedua kelas c), sehingga tanpa butir `P-2`. Langkah pemicu pelaku kedua ditulis "... hingga ... tersimpan" (R-20).
- Penyimpangan urutan: TC-232 dan TC-237 (baris `HHR-ARC-200` pada halaman 1) mendahului TC-231 (`TAG-ARC-OBJ` memakai Search, langkah 24 sebagai langkah penghubung ke baris di luar halaman 1) supaya Search tidak mengubah baris yang dicari blok sebelumnya.
- Langkah penghubung: menutup form dirty (langkah 11 sampai 13 dan 35 sampai 37, S-08); "Klik ikon close" setelah TC-237 menutup form yang sudah dimuat ulang ke nilai tersimpan.
- Langkah 8 dan 32 adalah asersi tambahan di luar Expected TC (S-03): opsi lain pada dropdown yang sama tampil sebagai pembanding sebelum asersi absence `Brand Sementara` dan `Perangkat Sementara` (langkah 9 dan 33), supaya dropdown yang belum dimuat tidak meloloskan absence (8b butir 2).
- Temuan untuk QA: TC-237 menyebut field terkunci "dengan tooltip" tanpa teks tooltip; spec mengasersi keadaan terkunci beserta tooltip tanpa teks. TC-231 dan TC-232 diberi Automation Manual Only (dua sesi paralel) di TC, tetapi pelaku kedua dijalankan lewat sesi API di spec ini.
- Post Condition TC-231, TC-232, dan TC-237 kosong.
- Temuan untuk QA (S-12/S-06): baris Pre-setup #29 (`HHR-ARC-200`, `TAG-ARC-OBJ`) dipakai sebagai target aksi sesuai pengecualian S-12 A-11; semua `[Save]` pada spec ini ditolak atau diblok (tidak ada perubahan tersimpan), dan fixture BE pemulih dinyatakan di `suite.md`.
- Temuan untuk QA (fixture): `fixtures/settings-device-sku.json`, akun Pre-setup #1 dan #2, dan env `AC_DS_*` belum terverifikasi ada di environment; ketersediaannya dipastikan tim FE.
