---
id: TC-AC-DC-E2E-024-defense-bypass-filter-fe-dan-markup
title: "Defense-in-Depth: Bypass Filter FE (Emoji) dan Markup pada Nama Category"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DC-85
  - TC-AC-DC-106
  - TC-AC-DC-254
coverage:
  web: automated
---
# Defense-in-Depth: Bypass Filter FE (Emoji) dan Markup pada Nama Category

## Prerequisites

- Mode: FE+BE.
- Aktor: Total Control (Pre-setup #1); Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > Device > Device Name).

| Role yang diuji | Akun (Pre-setup) | Password |
|---|---|---|
| Total Control (`Budi Santoso`) | #1 `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Data Dinamis (dibuat spec ini lewat API di hook `before` oleh Total Control #1 lewat sesi API aktor, di bawah `Handheld Reader`): node `Pemindai Induk {runId}-024` (parent untuk Add) dan `Pemindai Ubah {runId}-024` (target Edit). Nama yang diketik atau disuntikkan: "Scanner 😊 {runId}-024", "Pemindai Ubah 😊 {runId}-024", dan "<img src=x onerror=alert(1)> Scanner {runId}-024".
- Data Pre-setup: #14 (Pohon Uji Kategori, hanya dibaca), #17 (Riwayat Changelog Uji, hanya dibaca; precondition TC-AC-DC-254, tidak diasersi). Nilai data mengacu ke fixture `settingsDeviceCategory` (belum ada; disediakan tim FE). Nama node Pre-setup #14 ditulis sebagaimana di TC.
- Kemampuan teknis: menyuntikkan value langsung ke DOM input Category Name tanpa melewati filter keystroke FE (cara teknis tidak dirinci TC; disediakan tim FE). sesi API aktor (login API password untuk akun yang sama dengan sesi UI, tidak dihitung sebagai sesi web) dan klien HTTP; disediakan tim BE/FE dan dinyatakan di `suite.md`.
- Kemampuan membaca jumlah entri Changelog Category (disediakan tim FE/BE); jumlah dicatat sebagai baseline di hook `before` sesudah seeding, dan asersi memakai perbandingan terhadap baseline itu.
- Hook `after`: menghapus semua node (dan Device Name) yang dibuat spec ini, termasuk node hasil aksi UI yang dikenali dari sufiks `{runId}-024`, lewat API dari anak ke induk; cleanup tidak berasumsi seeding berhasil penuh.
- Seeding dan cleanup menambah entri Changelog dan log audit permanen (Create dan Delete atas node bersufiks); entri itu tidak diasersi.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`): pohon Category, Changelog, dan log audit adalah state bersama.

## Test Steps

### TC-AC-DC-85: Fallback safety net: emoji yang lolos filter FE ditolak saat Add

1. Expand `Hardware`
2. Expand `Handheld Reader`
3. Hover node `Pemindai Induk {runId}-024`
4. Klik aksi `+ Subcategory`
5. Injeksi value "Scanner 😊 {runId}-024" langsung ke DOM input Category Name (bypass filter keystroke FE, simulasi browser lama atau drag-drop)
6. Klik `[Submit]`
7. Verifikasi pesan error inline "Category name contains invalid characters" tampil
8. Verifikasi tidak ada node baru "Scanner 😊 {runId}-024" di bawah `Pemindai Induk {runId}-024`
9. Verifikasi jumlah entri Changelog Category sama dengan baseline
10. Klik `[×]` pada form Add
11. Verifikasi dialog Unsaved Changes tampil
12. Klik `[Leave]`

### TC-AC-DC-106: Fallback safety net: emoji yang lolos filter FE ditolak saat Edit

13. Hover node `Pemindai Ubah {runId}-024`
14. Klik aksi Edit
15. Injeksi value "Pemindai Ubah 😊 {runId}-024" langsung ke DOM input Category Name (bypass filter keystroke FE, simulasi browser lama atau drag-drop)
16. Klik `[Save]`
17. Verifikasi pesan error inline "Category name contains invalid characters" tampil
18. Klik `[×]` pada form Edit
19. Verifikasi dialog Unsaved Changes tampil
20. Klik `[Leave]`
21. Verifikasi nama node tidak berubah: `Pemindai Ubah {runId}-024`
22. Verifikasi jumlah entri Changelog Category sama dengan baseline

### TC-AC-DC-254: Nama Category berisi markup dirender sebagai teks di tree, dialog, dan Changelog

23. Hover node `Pemindai Induk {runId}-024`
24. Klik aksi `+ Subcategory`
25. Ketik "<img src=x onerror=alert(1)> Scanner {runId}-024"
26. Klik `[Submit]`
27. Verifikasi node dibuat di bawah `Pemindai Induk {runId}-024`
28. Verifikasi nama node tampil sebagai teks literal "<img src=x onerror=alert(1)> Scanner {runId}-024" di tree
29. Hover node baru
30. Klik aksi Delete
31. Verifikasi dialog Delete menampilkan nama node sebagai teks literal
32. Klik `[Cancel]`
33. Klik ikon Changelog pada header Sidebar Category
34. Ketik Search "Scanner {runId}-024", tekan Enter
35. Verifikasi entri Changelog menampilkan nama node sebagai teks literal
36. Verifikasi tidak ada skrip yang tereksekusi
37. Verifikasi tidak ada elemen gambar yang dirender
38. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini melewati sekitar 35 langkah karena tiga TC kelas a yang berdiri sendiri; tiap blok memakai node milik spec sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah menutup form dirty (S-08) menambah enam langkah.
- TC-AC-DC-85 dan 106 memicu bypass filter keystroke FE dengan menyuntikkan value ke DOM input (langkah 5 dan 15); objek uji adalah penolakan server atas value tersebut, yang tampil sebagai pesan error inline.
- Langkah penghubung: langkah 1 (expand tree), 10 sampai 12 dan 18 sampai 20 (menutup form dirty deterministik, S-08; dialog Unsaved Changes diverifikasi menurut S-08), 29 (hover node baru hasil Add), 34 (Search sufiks nama untuk menemukan entri Changelog, R-16), 38 (menutup modal Changelog).
- Asersi "tidak ada entri log" pada TC-AC-DC-85 dan 106 ditulis sebagai asersi jumlah dengan baseline Changelog (S-12), bukan asersi absence kelas g; log lain (System Log dan Activity Log) tidak diasersi di spec ini.
- Temuan untuk QA:
  - Target aksi tulis dan hapus memakai node milik spec bersufiks `{runId}-024` (S-06, S-12); TC memakai node literal Pre-setup #14 (`Rugged Scanner` pada TC-AC-DC-85, 106, dan 254; nama yang diketik diberi sufiks `{runId}-024`) sebagai target. Hasil TC identik karena node milik spec adalah node user-created dengan perilaku yang sama; node literal Pre-setup hanya dibaca.
  - TC-AC-DC-85 dan 106 tidak menyebut cara teknis menyuntikkan value ke DOM selain "injeksi langsung ke DOM input"; kemampuan itu dinyatakan sebagai kebutuhan yang disediakan tim FE, tanpa mekanisme karangan (S-13). Alternatif yang tidak ditulis di TC: mengubah body request lewat `Spectra.intercept()`.
  - TC-AC-DC-85 dan 106 Expected b ("tidak ada node baru dan tidak ada entri log") memuat dua klausa; keduanya diasersi terpisah.
  - TC-AC-DC-254 tidak menyebut kolom Changelog tempat nama tampil, dan tidak menyebut cara menemukan entri; entri ditemukan lewat Search sufiks nama (kolom yang dicari Search tidak dijelaskan TC). Pre-setup #17 dipakai sebagai precondition, tidak diasersi.
  - Post Condition TC-AC-DC-85, 106, dan 254 ('-') tidak punya langkah observasi dan tidak diasersi.
