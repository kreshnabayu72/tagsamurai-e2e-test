---
id: TC-AC-DN-E2E-157-log-absence-create
title: "Absence Log: Create Tidak Mencatat Field Measurement atau Category"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-489
  - TC-AC-DN-490
coverage:
  web: automated
---

# Absence Log: Create Tidak Mencatat Field Measurement atau Category

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (`suite.md`): `beforeEach` (membuka sub-tab Device Name, jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- General Settings entitas uji (Pre-setup #20): Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta; jam server dan jam browser sinkron.
- Data Pre-setup (hanya dibaca): #13, #14, #16, #19 (komparator: entri Edit Measurement `NFC Tag`/`Cable Tester` dan entri Edit Category), #20.
- Data Dinamis (milik spec, dibuat lewat form Create): `Dock Station {runId}-157` (`Unit`, `Accessory`, TC-AC-DN-489) dan `Dock Kategori {runId}-157` (`Unit`, `Accessory`, TC-AC-DN-490); aksi Create adalah pemicu absence (P-5 butir a), tiap TC punya record dan Search sendiri; baseline nol berasal dari nama bersuffix unik (S-12).
- Kemampuan teknis (disediakan tim FE/BE): seeding Device Name, SKU, dan riwayat lewat sesi API akun #1 (token tidak dihitung sebagai sesi web, lihat `suite.md`); kemampuan baca jumlah entri Changelog, Activity Log, dan System Log aktor untuk baseline (bagian 8b butir 10).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Entri audit trail yang tercipta (Changelog, Activity Log, System Log aktor) bersifat permanen dan tidak dihapus; record milik spec dihapus di hook `after` dan entri historisnya tetap, bersuffix unik `{runId}-NNN` (`{runId}` hanya digit).

## Test Steps

1. TC-AC-DN-489: Create tidak mencatat entri Field Measurement
2. Klik `+ Device Name`
3. Ketik "Dock Station {runId}-157" pada field Device Name
4. Pilih "Unit" pada field Measurement
5. Pada field Category, expand `TAG` lalu `NFC` dan pilih leaf `Accessory` pada TreeSelect
6. Klik `[Submit]`
7. Verifikasi toast sukses "Success, device name has been created."
8. Klik ikon Changelog di toolbar
9. Verifikasi popup `Changelog: Device Name` tampil
10. Ketik Search `Dock Station {runId}-157`, tekan Enter
11. Verifikasi hasil Search `Dock Station {runId}-157` memuat tepat 1 baris Create ber-Field `Device Name`
12. Ganti isi kotak Search dengan `Measurement`, tekan Enter
13. Verifikasi hasil Search `Measurement` memuat sedikitnya satu baris Edit Field `Measurement` milik fixture (`NFC Tag` atau `Cable Tester`)
14. Verifikasi hasil Search `Measurement` tidak memuat baris dengan Device Name `Dock Station {runId}-157`
15. Klik ikon close `(X)` pada popup Changelog
16. Buka menu `Activity Log`, lalu klik tab `User Action`
17. Verifikasi halaman `Activity Log > User Action` tampil
18. Ketik Search `Dock Station {runId}-157`, tekan Enter
19. Verifikasi hasil Search `Dock Station {runId}-157` memuat satu entri Action `Create`, Object `Device Name`, Name `Dock Station {runId}-157`, Field `Device Name`
20. Verifikasi tidak ada entri Field `Measurement` pada hasil Search `Dock Station {runId}-157`
21. TC-AC-DN-490: Create tidak mencatat entri Field Category
22. Buka halaman `Settings > Device > Device Name`
23. Klik `+ Device Name`
24. Ketik "Dock Kategori {runId}-157" pada field Device Name
25. Pilih "Unit" pada field Measurement
26. Pada field Category, expand `TAG` lalu `NFC` dan pilih leaf `Accessory` pada TreeSelect
27. Klik `[Submit]`
28. Verifikasi toast sukses "Success, device name has been created."
29. Klik ikon Changelog di toolbar
30. Verifikasi popup `Changelog: Device Name` tampil
31. Ketik Search `Dock Kategori {runId}-157`, tekan Enter
32. Verifikasi hasil Search `Dock Kategori {runId}-157` memuat tepat 1 baris Create ber-Field `Device Name`
33. Ganti isi kotak Search dengan `Category`, tekan Enter
34. Verifikasi hasil Search `Category` memuat sedikitnya satu baris Edit Field `Category` milik fixture (`NFC Tag` atau `Cable Tester`)
35. Verifikasi hasil Search `Category` tidak memuat baris dengan Device Name `Dock Kategori {runId}-157`
36. Klik ikon close `(X)` pada popup Changelog
37. Buka menu `Activity Log`, lalu klik tab `User Action`
38. Verifikasi halaman `Activity Log > User Action` tampil
39. Ketik Search `Dock Kategori {runId}-157`, tekan Enter
40. Verifikasi hasil Search `Dock Kategori {runId}-157` memuat satu entri Action `Create`, Object `Device Name`, Name `Dock Kategori {runId}-157`, Field `Device Name`
41. Verifikasi tidak ada entri Field `Category` pada hasil Search `Dock Kategori {runId}-157`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): Search pada Changelog dan Activity Log menemukan entri milik record spec.
- Verifikasi toast sukses pada aksi pemicu ditambahkan sebagai anchor penyelesaian aksi (bagian 8b butir 2 dan 8) dan tidak ada di Expected TC. Search dengan nama record bersuffix unik menggantikan kata kunci TC (S-12); akun aktor pada System Log dirujuk lewat email Fixture (R-06).
- Ukuran spec (41 langkah, di atas smell 35 langkah): satu topik, satu halaman, satu kelas harness; tiap blok TC berdiri sendiri dengan record milik spec sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal (alasan R3). Blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom) tidak dihitung dalam smell 35 langkah (bagian 3).
- Anchor absence (bagian 8b butir 2): entri Create Field `Device Name` milik record spec dan baris Edit milik fixture pada surface yang sama tampil sebelum asersi absence.
- Temuan untuk QA:
  - TC sumber mengharapkan tepat 3 baris Edit Measurement (dan 2 Edit Category) milik fixture; spec memakai komparator 'sedikitnya satu baris' karena riwayat fixture bertambah oleh spec lain (S-12).
  - TC sumber memakai nama literal Pre-setup (`Dock Station`, `Door Antenna`, `Cable Tester`); spec memakai record milik spec bersuffix `{runId}-<NNN>` (S-06, S-12) dan Pre-setup #16 tidak diubah.
