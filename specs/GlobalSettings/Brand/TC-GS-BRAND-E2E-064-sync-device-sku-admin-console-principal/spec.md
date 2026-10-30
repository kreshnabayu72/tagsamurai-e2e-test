---
id: TC-GS-BRAND-E2E-064-sync-device-sku-admin-console-principal
title: "Sinkronisasi Brand ke Device SKU Admin Console pada Instance Principal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-220
  - TC-GS-BRAND-245
  - TC-GS-BRAND-246
  - TC-GS-BRAND-248
coverage:
  web: automated
tags: [principal]
---

# Sinkronisasi Brand ke Device SKU Admin Console pada Instance Principal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), Hendra Wijaya, `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 8), kredensial `Spectra.env.GS_PRINCIPAL_TC_PASSWORD`. Login di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`). Halaman awal: Global Settings > Master Reference > Brand.
- Environment variable: `GS_PRINCIPAL_TC_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Tidak ada data Pre-setup bersama yang dipakai atau diubah; seluruh objek aksi tulis milik spec ini (suffix `{runId}-064`, bagian 5 konvensi).
- Data dinamis (instance Principal), di-seed lewat API di hook `before` oleh akun Total Control Principal:
  - `Sync Dev Co {runId}-064` (D-50): brand yang dipakai tepat 1 Device SKU `SKU-SD-{runId}-064` (Category `BLE Gateway`; Model/Type dan Photo dari fixture `deviceSku`). Pada TC-GS-BRAND-220 di-rename menjadi `Sync Dev Prime {runId}-064`, lalu dikembalikan ke `Sync Dev Co {runId}-064`.
  - `Beacon Co {runId}-064` (D-33): dibuat spec lewat UI pada TC-GS-BRAND-245 dan dihapus lewat UI pada TC-GS-BRAND-246.
  - Device SKU `SKU-N4-{runId}-064` (Device Name `Beacon Node N1`, lalu `Beacon Node N2`; Category `BLE Gateway`; Brand `Sync Dev Co {runId}-064`; D-37): dibuat, diubah, dan dihapus lewat UI Admin Console pada TC-GS-BRAND-248.
- Nilai field wajib lain pada form Create Device SKU (`SKU-N4-{runId}-064` adalah objek uji TC-GS-BRAND-248, sehingga nilainya harus pasti; PRD `admin-console/settings-device-sku`: Category, Device Name, Brand, Model/Type, SKU, dan minimal 1 Photo wajib; Category `BLE Gateway` tanpa field ekstra). Fixture `fixtures/brand.json` belum ada; tim FE menyediakannya:

  | Kunci fixture | Field | Nilai |
  |---|---|---|
  | `deviceSku.modelType` | Model/Type | disediakan tim FE |
  | `deviceSku.photo` | Photo (minimal 1) | berkas `fixtures/sampleImage.png` |

- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `SKU-N4-{runId}-064`, `SKU-SD-{runId}-064`, lalu `Beacon Co {runId}-064` dan `Sync Dev Co {runId}-064` atau `Sync Dev Prime {runId}-064` (nama yang masih ada) bila masih ada.
- Tidak ada state global yang diubah.
- TC-GS-BRAND-220, 245, 246, 248: login sebagai Total Control (Principal).

## Test Steps

### TC-GS-BRAND-245: Brand baru muncul di opsi Brand form Create Device SKU (pembuatan Brand)

1. Di Global Settings > Master Reference > Brand, klik [+ Brand], isi Brand Name `Beacon Co {runId}-064`, klik [Submit]
2. Verifikasi toast sukses: "Success, brand has been created."

### TC-GS-BRAND-220: Rename Brand tercermin di kolom Brand Device SKU Admin Console (sekaligus opsi TC-GS-BRAND-245)

3. Search `Sync Dev Co {runId}-064` pada tabel Brand, klik `⋯` pada baris tersebut > Edit, ubah Brand Name menjadi `Sync Dev Prime {runId}-064`, klik [Save]
4. Buka Admin Console > Settings > Device SKU
5. Search `SKU-SD-{runId}-064` pada tabel Device SKU
6. Verifikasi `SKU-SD-{runId}-064` menampilkan Brand `Sync Dev Prime {runId}-064`
7. Klik `[+ SKU]`, buka field Brand
8. Verifikasi form Create Device SKU menampilkan opsi `Sync Dev Prime {runId}-064`
9. Verifikasi opsi `Beacon Co {runId}-064` tersedia di field Brand tanpa reload (TC-GS-BRAND-245 Expected Result b)
10. Tutup form Create Device SKU lewat `✕` (form tidak berisi perubahan, tanpa dialog Unsaved Changes)
11. Buka Global Settings > Master Reference > Brand, Search `Sync Dev Prime {runId}-064`, rename kembali menjadi `Sync Dev Co {runId}-064`, klik [Save]

### TC-GS-BRAND-248: Create, Edit, dan Delete Device SKU tercermin di accordion Device SKU List

12. Search `Sync Dev Co {runId}-064` pada tabel Brand, buka Detail Sync Dev Co, catat `Total Item` (1)
13. Di Admin Console > Settings > Device SKU, klik `[+ SKU]` dan daftarkan `SKU-N4-{runId}-064` (Device Name `Beacon Node N1`, Category `BLE Gateway`, Brand `Sync Dev Co {runId}-064`, Model/Type dan Photo dari fixture `deviceSku`), klik [Submit]
14. Buka Global Settings > Master Reference > Brand, Search `Sync Dev Co {runId}-064`, buka kembali Detail Sync Dev Co, expand Device SKU List
15. Verifikasi `Total Item: 2`
16. Verifikasi baris `SKU-N4-{runId}-064` / Beacon Node N1 / BLE Gateway tampil
17. Edit `SKU-N4-{runId}-064` di Admin Console menjadi Device Name `Beacon Node N2`, klik [Save]
18. Buka Global Settings > Master Reference > Brand, Search `Sync Dev Co {runId}-064`, buka kembali Detail Sync Dev Co, expand Device SKU List
19. Verifikasi Device Name `SKU-N4-{runId}-064` adalah `Beacon Node N2`
20. Verifikasi `Total Item: 2`
21. Hapus `SKU-N4-{runId}-064` di Admin Console lewat `⋯` > Delete > [Delete]
22. Buka Global Settings > Master Reference > Brand, Search `Sync Dev Co {runId}-064`, buka kembali Detail Sync Dev Co, expand Device SKU List
23. Verifikasi `SKU-N4-{runId}-064` tidak ada
24. Verifikasi `Total Item: 1`

### TC-GS-BRAND-246: Brand terhapus hilang dari opsi Brand form Create Device SKU

25. Tutup Detail, Search `Beacon Co {runId}-064` pada tabel Brand, hapus lewat `⋯` > Delete > [Delete]
26. Verifikasi toast sukses: "Success, brand has been deleted."
27. Buka Admin Console > Settings > Device SKU, klik `[+ SKU]`
28. Buka field Brand
29. Verifikasi `Beacon Co {runId}-064` tidak ada di opsi Brand
30. Tutup form Create Device SKU lewat `✕` (form tidak berisi perubahan, tanpa dialog Unsaved Changes)

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Urutan TC di spec berbeda dari urutan sumber: 245 (hanya pembuatan Brand), 220 (opsi `Sync Dev Prime` dan `Beacon Co` diverifikasi dalam satu kali buka form Create Device SKU, sehingga Expected Result b TC-GS-BRAND-245 diverifikasi di langkah 9), 248 (siklus Device SKU), lalu 246 paling akhir karena Delete (prinsip 5). Form Create Device SKU dibuka tiga kali (langkah 7, 13, 27), masing-masing berakhir dengan penutupan atau Submit.
- Dependensi 246 terhadap 245 dipenuhi dalam spec yang sama (Beacon Co dibuat di langkah 1). Nama Brand `Beacon Co` diberi suffix `{runId}-064`.
- Kode Device SKU `SKU-N4-{runId}-064` mengikuti notasi `SKU-N4-{runId}` pada TC-GS-BRAND-248 dengan nomor spec; `SKU-SD-{runId}-064` mengikuti notasi `SKU-SD-{runId}` pada TC-GS-BRAND-220 dan 248. `Total Item: 1` dan `2` bergantung pada `Sync Dev Co` yang memiliki tepat satu Device SKU hasil seeding.
- Langkah penghubung: langkah 3, 11, 12, 25 (Search baris Brand target), langkah 5 (Search SKU pada tabel Device SKU agar baris target terlihat), langkah 14, 18, 22 (membuka Detail brand dari tabel Brand setelah aksi di Admin Console, lalu expand Device SKU List), langkah 10 dan 30 (menutup form bersih).
- Kebutuhan nilai field wajib lain (`deviceSku.modelType`, `deviceSku.photo`) di `fixtures/brand.json` yang belum ada sudah dicatat sebagai kebutuhan di Prerequisites.
