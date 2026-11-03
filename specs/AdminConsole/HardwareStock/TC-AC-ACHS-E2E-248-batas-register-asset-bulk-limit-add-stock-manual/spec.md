---
id: TC-AC-ACHS-E2E-248-batas-register-asset-bulk-limit-add-stock-manual
title: "Batas Register Asset Bulk Limit pada Add Stock Manual"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACHS-85
  - TC-AC-ACHS-86
  - TC-AC-ACHS-87
coverage:
  web: automated
---

# Batas Register Asset Bulk Limit pada Add Stock Manual

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Pre-setup #1; `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip halaman Stock List, sesi API aktor, seeding Population Stock Pre-setup #16 s.d. #20 dan #27. Suite serial (`parallel: false`).
- Kelas harness: e (volume data, 100 sampai 101 baris Serial Number dalam satu Submit).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuFx}` | #16 Tabel A baris 3; #27 | kode SKU Smart Fixed Reader, 8 Available | `Fixture.hardwareStock.p16.a[3].sku` |

- Data Pre-setup: SKU `{skuFx}` (Pre-setup #16, #27). Pre-setup #26: System Limits `register_asset_bulk_limit` default 1.000; nilai minimum 100 dipakai TC batas.
- Data Dinamis: 100 unit pada SKU {skuFx} dengan Serial Number `SN-LIM-{runId}-248-0001` sampai `SN-LIM-{runId}-248-0100` (dibuat langkah 30). Baris `SN-LIM-1001` sampai `SN-LIM-1101` dan `SN-LIM-2001` sampai `SN-LIM-2101` selalu diblokir dan tidak disimpan sehingga literal seperti di TC.
- State global: System Limit `register_asset_bulk_limit` diubah ke 100, lalu 150, lalu 100, lalu dikembalikan ke nilai awal (langkah 1, 14, 20, 33). Suite berjalan serial; hook `before` mencatat nilai awal dan hook `after` memulihkannya walau spec gagal di tengah. Kemampuan mengubah System Limit (Lifecycle Settings > System Limits) disediakan tim FE/BE; aktor pengubah tidak disebut TC, PRD, atau LLD (lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor untuk mengubah limit (langkah 14 dan 20); menempel 101 baris ke textarea; konfirmasi dialog `beforeunload` bawaan browser saat memuat ulang halaman dirty (langkah 15); fixture BE yang menghapus unit bersuffix `-{runId}-248` di hook `after` (mekanismenya tidak didefinisikan di TC, PRD, atau LLD, lihat Temuan untuk QA).
- Efek pada Pre-setup: Total Registered, Available, dan Last Updated baris SKU {skuFx} berubah selama spec berjalan; 100 unit dihapus hook `after`.

## Test Steps

### Persiapan

1. Atur System Limits > Register Asset Bulk Limit = 100 (nilai minimum, Pre-setup #26)
2. Ketik Search `{skuFx}`, tekan Enter
3. Catat Total Registered dan Available baris SKU `{skuFx}` sebagai baseline
4. Klik `(⋯)` pada baris SKU `{skuFx}`
5. Klik opsi `Add Stock`

### TC-AC-ACHS-86: limit+1 baris memblokir Submit seluruhnya

6. Tempel 101 baris `SN-LIM-1001` sampai `SN-LIM-1101`
7. Verifikasi error banner real-time V-03 "You've reached the maximum of 100 assets per submission. Submit this batch first, then continue with a new one."
8. Klik `[Submit]`
9. Verifikasi `[Submit]` diblokir dan form tetap terbuka
10. Verifikasi textarea tetap berisi 101 baris (tidak ada baris dipotong)

### TC-AC-ACHS-87: nilai limit dibaca live tanpa snapshot

11. Kosongkan isi textarea
12. Tempel 101 baris `SN-LIM-2001` sampai `SN-LIM-2101`
13. Verifikasi banner V-03 menyebut maksimum 100 ("You've reached the maximum of 100 assets per submission. Submit this batch first, then continue with a new one.")
14. Ubah Register Asset Bulk Limit menjadi 150 lewat sesi API aktor hingga nilai 150 tersimpan
15. Muat ulang halaman Add Stock (F5) dan konfirmasi dialog `beforeunload` bawaan browser
16. Tempel 101 baris `SN-LIM-2001` sampai `SN-LIM-2101` yang sama
17. Verifikasi banner V-03 tidak tampil (101 baris diterima)
18. Verifikasi `[Submit]` aktif
19. Verifikasi batas mengikuti nilai limit terkini: banner pada langkah 13 menyebut maksimum 100 dan tidak ada banner pada langkah 17 setelah limit menjadi 150

### Menutup form dirty dan memulihkan limit

20. Ubah Register Asset Bulk Limit menjadi 100 lewat sesi API aktor hingga nilai 100 tersimpan
21. Klik `[Cancel]`
22. Verifikasi dialog Unsaved Changes dengan pesan "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
23. Klik `[Leave]`
24. Verifikasi Summary bar Stock Detail SKU {skuFx}: Total Registered dan Available sama dengan baseline langkah 3 (tidak ada unit tersimpan untuk TC-86 dan TC-87)

### TC-AC-ACHS-85: tepat limit dan limit-1 baris diterima

25. Klik `[Add Stock]` pada toolbar Tab Available SKU `{skuFx}` (form baru)
26. Tempel 99 baris `SN-LIM-{runId}-248-0001` sampai `SN-LIM-{runId}-248-0099`
27. Verifikasi banner V-03 tidak tampil dengan 99 baris
28. Tambahkan baris ke-100 `SN-LIM-{runId}-248-0100`
29. Verifikasi banner V-03 tidak tampil dan counter menampilkan "100 serial numbers detected"
30. Klik `[Submit]`
31. Verifikasi toast sukses "Success, unit has been added to stock."
32. Verifikasi 100 unit Available tersimpan: Available pada Summary bar Stock Detail sama dengan baseline langkah 3 ditambah 100
33. Kembalikan Register Asset Bulk Limit ke nilai awal lewat sesi API aktor hingga nilai awal tersimpan

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-85, 86, 87). Tidak ada TC hanya-BE di spec ini.
- Urutan di dalam spec berbeda dari nomor TC: TC-86 dan TC-87 (diblokir, tidak membuat data) lebih dulu, lalu TC-85 yang membuat 100 unit (prinsip 3 bagian 3). Buka form 2 kali untuk 2 kejadian menutup form (langkah 21 sampai 23 dan Submit pada langkah 30).
- TC-87: "sesi lain" untuk mengubah limit dijalankan lewat sesi API aktor (pelaku kedua yang hanya mengubah state; bukan konteks kedua kelas c dan tanpa `P-2`). Kata "Manual Only" pada kolom Automation TC-87 bukan alasan mengeluarkan TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search (langkah 2), baseline (langkah 3), pengosongan textarea (langkah 11), pemulihan limit (langkah 20 dan 33), `[Cancel]` dan `[Leave]` (langkah 21, 23), dan klik `[Submit]` yang diblokir pada langkah 8 mengikuti langkah 6 TC-86. Post Condition TC-85 "Limit dikembalikan ke nilai awal" dijalankan sebagai aksi pada langkah 33 dan hook `after`.
- Expected TC-87 butir c ("angka tidak di-hardcode") adalah kesimpulan dari butir a dan b; ditulis satu `Verifikasi` pada langkah 19 yang merujuk langkah 13 dan 17.
- Temuan untuk QA:
  - TC-85 Post Condition a ("Total Registered SKU bertambah 100") tidak punya langkah observasi di TC dan tidak diasersi; Expected b ("100 unit Available tersimpan") diasersi lewat Available pada Summary bar.
  - Aktor dan mekanisme mengubah System Limit `register_asset_bulk_limit` tidak disebut TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
  - TC-86 dan TC-87 menempel banner V-03 dengan teks berbahasa Inggris; TC-87 butir a hanya menyebut "banner V-03 menyebut maksimum 100", spec memakai teks lengkap dari TC-86.
