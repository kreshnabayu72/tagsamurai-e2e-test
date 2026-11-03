---
id: TC-AC-DN-E2E-173-sinkron-rename-master-data-pada-list
title: "Rename Master Data (Measurement, Category, Brand): Baris Device Name Tetap Tampil dengan Nama Terkini"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-532
  - TC-AC-DN-533
  - TC-AC-DN-624
coverage:
  web: automated
---

# Rename Master Data (Measurement, Category, Brand): Baris Device Name Tetap Tampil dengan Nama Terkini

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Budi Santoso`, entitas Principal; email dirujuk lewat `Fixture.settings-device-name.akunTotalControl`), password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Settings > Device > Device Name pada sub-tab Device Name dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes`; flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` disetel `seen` oleh hook `before` suite dan dipulihkan hook `after` suite.
- Fixture: `Fixture.settings-device-name` (belum ada, disediakan tim FE) menyimpan nilai tetap: email akun Pre-setup #1 dan nama master `Unit`, `Accessory`, `Brand A`. Nama pengganti dibentuk `<nama> {runId}-173` (`{runId}` hanya digit).
- Data Pre-setup (dibaca saja): #13 Measurement `Unit`; #14 Pohon Category (`TAG` > `NFC` > `Accessory`, `Tag`); #15 Brand `Brand A`; #16 Device Name `Cable Tester` (Accessory, Unit) dan `NFC Tag` (Tag, SKU Brand A/Model N1); #19 riwayat Changelog (entri seed berdate 01/09/26 sampai 15/09/26, Date Format `dd/MM/yy`, 24 jam). Record Device Name tidak diubah.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah entri Changelog Device Name (baseline N0, S-12).
- State global (S-06, pengecualian 2026-10-30): nama master Measurement `Unit`, node Category `Accessory`, dan Brand `Brand A` di-rename sementara oleh langkah spec; fixture backend yang disediakan tim FE/BE memulihkan ketiganya ke nama awal setelah tiap blok (langkah penghubung) dan di hook `before` dan `after`. Efeknya (Last Modified dan audit trail modul Measurement, Category, Brand) dicatat di sini. Suite berjalan serial (`parallel: false`).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-DN-532: Rename Measurement

1. Catat jumlah entri Changelog Device Name sebagai N0 lewat kemampuan baca Changelog
2. Buka halaman `Master Reference > Measurement`
3. Buka menu aksi pada baris "Unit", klik `Edit`, ubah Unit Name menjadi "Piece {runId}-173", klik `[Save]`
4. Tunggu aksi selesai (Measurement "Unit" berubah menjadi "Piece {runId}-173")
5. Buka halaman `Settings > Device > Device Name`, ketik Search `Cable Tester`, tekan Enter
6. Verifikasi baris "Cable Tester" menampilkan Measurement "Piece {runId}-173"
7. Verifikasi baris "Cable Tester" menampilkan Category "Accessory"
8. Verifikasi baris "Cable Tester" menampilkan Brand `—` dan Model/Type `—`
9. Klik nama "Cable Tester"
10. Verifikasi grid dialog "Device Name Detail" menampilkan Measurement "Piece {runId}-173"
11. Klik icon `(✕)` pada dialog
12. Klik ikon Changelog
13. Verifikasi modal "Changelog: Device Name" memuat jumlah entri sama dengan N0
14. Klik ikon Search, ketik "Measurement", tekan Enter, lalu klik header kolom Date sekali
15. Verifikasi entri pertama hasil Search (08/09/26 15:40, Edit NFC Tag, Field Measurement) menampilkan Old Value "Box" dan New Value "Unit"
16. Verifikasi entri ketiga hasil Search (10/09/26 12:25, Edit Cable Tester, Field Measurement) menampilkan Old Value "Meter" dan New Value "Unit"
17. Klik icon `(✕)` pada modal
18. Pulihkan nama Measurement `Unit` lewat fixture BE

### TC-AC-DN-533: Rename node Category

19. Catat jumlah entri Changelog Device Name sebagai N1 lewat kemampuan baca Changelog
20. Pada Category Sidebar, expand `TAG` lalu `NFC`, hover node "Accessory", klik aksi `Edit`, ubah nama menjadi "Accessories {runId}-173", klik `[Save]`
21. Verifikasi node pada Category Sidebar bernama "Accessories {runId}-173"
22. Ketik Search `Cable Tester`, tekan Enter
23. Verifikasi baris "Cable Tester" menampilkan badge Category "Accessories {runId}-173"
24. Verifikasi baris "Cable Tester" menampilkan Measurement "Unit"
25. Verifikasi baris "Cable Tester" menampilkan Brand `—` dan Model/Type `—`
26. Klik nama "Cable Tester"
27. Verifikasi grid dialog "Device Name Detail" menampilkan Category berupa badge "Accessories {runId}-173"
28. Klik icon `(✕)` pada dialog
29. Klik ikon Changelog
30. Verifikasi modal "Changelog: Device Name" memuat jumlah entri sama dengan N1
31. Klik ikon Search, ketik "Category", tekan Enter, lalu klik header kolom Date sekali
32. Verifikasi entri pertama hasil Search (06/09/26 09:30, Edit Cable Tester, Field Category) menampilkan Old Value "TAG > NFC > Tag" dan New Value "TAG > NFC > Accessory"
33. Verifikasi entri kedua hasil Search (07/09/26 14:05, Edit NFC Tag, Field Category) menampilkan Old Value "TAG > NFC > Accessory" dan New Value "TAG > NFC > Tag"
34. Klik icon `(✕)` pada modal
35. Pulihkan nama node `Accessory` lewat fixture BE

### TC-AC-DN-624: Rename Brand

36. Catat jumlah entri Changelog Device Name sebagai N2 lewat kemampuan baca Changelog
37. Buka halaman `Master Reference > Brand`
38. Buka menu aksi pada baris "Brand A", klik `Edit`, ubah Brand Name menjadi "Brand Alpha {runId}-173", klik `[Save]`
39. Tunggu aksi selesai (Brand "Brand A" berubah menjadi "Brand Alpha {runId}-173")
40. Buka halaman `Settings > Device > Device Name`, ketik Search `NFC Tag`, tekan Enter
41. Verifikasi kolom Brand baris "NFC Tag" menampilkan satu chip "Brand Alpha {runId}-173"
42. Verifikasi kolom Model/Type baris "NFC Tag" menampilkan "Model N1"
43. Klik ikon Filter, klik field `Brand`
44. Verifikasi daftar opsi filter Brand memuat "Brand Alpha {runId}-173"
45. Verifikasi daftar opsi filter Brand tidak memuat opsi bernama persis "Brand A"
46. Tutup Filter Panel, klik ikon Changelog
47. Verifikasi modal "Changelog: Device Name" memuat jumlah entri sama dengan N2
48. Klik icon `(✕)` pada modal
49. Pulihkan nama Brand `Brand A` lewat fixture BE

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 5, 22, 40 (Search) menemukan baris Pre-setup #16 yang hanya dibaca; langkah 11, 17, 28, 34, 48 menutup dialog atau modal; langkah 18, 35, 49 memulihkan nama master lewat fixture BE (S-06); langkah 1, 19, 36 mencatat baseline Changelog; langkah 4 dan 39 (`Tunggu aksi selesai`) menunggu `[Save]` rename Measurement dan Brand selesai sebelum halaman berpindah, tanpa `Verifikasi` karena hasilnya diverifikasi di List.
- Rename master memakai suffix `{runId}-173` (S-12). Pada langkah 45 yang diasersi absence adalah opsi bernama persis "Brand A"; langkah 44 menjadi anchor positif (8b butir 2).
- Urutan: mengikuti sourceTc. Asersi Changelog (S-12, S-14): jumlah entri dibandingkan dengan baseline, bukan angka absolut "11 entri"; entri seed dibaca dengan sort Oldest First sehingga berada di atas entri yang ditambah spec lain. Angka "3 entri Field Measurement" dan "2 entri Field Category" TC tidak diasersi karena audit trail tumbuh.
- Ukuran spec (49 langkah, di atas smell 35 langkah): satu topik (rename master data tercermin di List), satu dataset (Pre-setup #16 dibaca saja), satu kelas harness; tiap blok memulihkan master sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA:
  - Post Condition tanpa langkah observasi di TC tidak diasersi (S-01): TC-AC-DN-532, TC-AC-DN-533, TC-AC-DN-624 (pemulihan master dilakukan fixture BE).
  - TC-AC-DN-532 butir e dan TC-AC-DN-533 butir f: "tidak ada entri log yang menampilkan nama baru" tidak teramati lewat satu Search yang menjamin ketiadaan (Search mencocokkan nama baru hanya bila entri itu ada, sehingga hasil kosong tidak membedakan sebab); spec mengasersi nilai Old Value dan New Value entri seed tetap dan jumlah entri sama dengan baseline.
  - TC-AC-DN-533: Expected a mensyaratkan Sidebar sudah di-expand; langkah 20 mencakup expand sesuai TC.
