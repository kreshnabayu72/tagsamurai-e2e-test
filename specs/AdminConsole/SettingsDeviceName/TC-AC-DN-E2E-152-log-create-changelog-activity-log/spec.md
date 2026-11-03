---
id: TC-AC-DN-E2E-152-log-create-changelog-activity-log
title: "Pencatatan Create: Changelog dan Activity Log (Satu Entri Field Device Name, Tanpa Duplikat, Object Non-entitas)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-488
  - TC-AC-DN-491
  - TC-AC-DN-506
coverage:
  web: automated
---

# Pencatatan Create: Changelog dan Activity Log (Satu Entri Field Device Name, Tanpa Duplikat, Object Non-entitas)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (`suite.md`): `beforeEach` (membuka sub-tab Device Name, jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- General Settings entitas uji (Pre-setup #20): Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta; jam server dan jam browser sinkron.
- Data Pre-setup (hanya dibaca): #13 Measurement `Unit`, `Meter`, `Box`; #14 pohon Category (`TAG` > `NFC` > `Accessory`; `Hardware` > `Smart Fixed Reader` > `Antenna`); #16 Device Name inti; #19 riwayat Changelog; #20 General Settings.
- Data Dinamis (milik spec):

  | Kode | Nama | Measurement | Category | Keterangan | Dipakai oleh |
  |---|---|---|---|---|---|---|
  | R1 | `Dock Station {runId}-152` | `Unit` | `Accessory` | dibuat lewat form Create | TC-AC-DN-488 |
  | R2 | `Dock Station Dua {runId}-152` | `Unit` | `Accessory` | dibuat lewat form Create | TC-AC-DN-491 |
  | R3 | `Door Antenna {runId}-152` | `Unit` | `Antenna` | dibuat lewat API di hook `before`, tanpa SKU | TC-AC-DN-506 |
- Kemampuan teknis (disediakan tim FE/BE): seeding Device Name, SKU, dan riwayat lewat sesi API akun #1 (token tidak dihitung sebagai sesi web, lihat `suite.md`); kemampuan baca jumlah entri Changelog, Activity Log, dan System Log aktor untuk baseline (bagian 8b butir 10).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Entri audit trail yang tercipta (Changelog, Activity Log, System Log aktor) bersifat permanen dan tidak dihapus; record milik spec dihapus di hook `after` dan entri historisnya tetap, bersuffix unik `{runId}-NNN` (`{runId}` hanya digit).

## Test Steps

1. Catat jumlah total entri Changelog sebagai baseline N0 (kemampuan baca)
2. TC-AC-DN-488: Create mencatat entri Field Device Name
3. Klik `+ Device Name`
4. Ketik "Dock Station {runId}-152" pada field Device Name
5. Pilih "Unit" pada field Measurement
6. Pada field Category, expand `TAG` lalu `NFC` dan pilih leaf `Accessory` pada TreeSelect
7. Klik `[Submit]`
8. Verifikasi toast sukses "Success, device name has been created."
9. Klik ikon Changelog di toolbar
10. Verifikasi popup `Changelog: Device Name` tampil
11. Ketik Search `Dock Station {runId}-152`, tekan Enter
12. Verifikasi baris Changelog: Action `Create`, Device Name `Dock Station {runId}-152`, Field `Device Name`, Old Value `—`, New Value `Dock Station {runId}-152`, Modified By `Budi S`
13. Klik ikon close `(X)` pada popup Changelog
14. Buka menu `Activity Log`, lalu klik tab `User Action`
15. Verifikasi halaman `Activity Log > User Action` tampil
16. Ketik Search `Dock Station {runId}-152`, tekan Enter
17. Verifikasi entri Activity Log: Action `Create`, Object `Device Name`, Name `Dock Station {runId}-152`, Field `Device Name`, Old Value `—`, New Value `Dock Station {runId}-152`, Modified By `Budi S`
18. TC-AC-DN-491: Create menghasilkan tepat satu entri tanpa duplikat dan tanpa entri nyasar
19. Buka halaman `Settings > Device > Device Name`
20. Klik `+ Device Name`
21. Ketik "Dock Station Dua {runId}-152" pada field Device Name
22. Pilih "Unit" pada field Measurement
23. Pada field Category, expand `TAG` lalu `NFC` dan pilih leaf `Accessory` pada TreeSelect
24. Klik `[Submit]`
25. Verifikasi toast sukses "Success, device name has been created."
26. Klik ikon Changelog di toolbar
27. Verifikasi popup `Changelog: Device Name` tampil
28. Ketik Search `Dock Station Dua {runId}-152`, tekan Enter
29. Verifikasi hasil Search `Dock Station Dua {runId}-152` menampilkan tepat 1 baris Create: Field `Device Name`, Old Value `—`, New Value `Dock Station Dua {runId}-152`
30. Klik ikon `(✕)` pada Search lalu tekan Enter pada input kosong
31. Klik tombol halaman terakhir pada pagination
32. Verifikasi total entri Changelog bertambah tepat 2 dari baseline N0 (satu dari TC-AC-DN-488 dan satu dari TC-AC-DN-491) dan baris pada halaman terakhir pagination sesuai total itu
33. Klik ikon close `(X)` pada popup Changelog
34. TC-AC-DN-506: Activity Log mencatat Device Name sebagai Object non-entitas
35. Buka halaman `Settings > Device > Device Name`
36. Ketik Search `Door Antenna {runId}-152`, tekan Enter
37. Klik ikon row action `⋯` pada baris `Door Antenna {runId}-152`, lalu klik `Edit`
38. Ubah field Measurement dari "Unit" menjadi "Box"
39. Klik `[Save]`
40. Verifikasi toast sukses "Success, device name has been updated."
41. Buka menu `Activity Log`, lalu klik tab `User Action`
42. Verifikasi halaman `Activity Log > User Action` tampil
43. Ketik Search `Door Antenna {runId}-152`, tekan Enter
44. Verifikasi entri Activity Log tab User Action: kolom Object `Device Name`, Name `Door Antenna {runId}-152`, Modified By `Budi S`
45. Verifikasi entri tampil pada Activity Log Admin Console milik Principal

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah pertama mencatat baseline N0 (S-12); Search pada Changelog dan Activity Log menemukan entri milik record spec; `(✕)` pada Search mengosongkan Search.
- Verifikasi toast sukses pada aksi pemicu ditambahkan sebagai anchor penyelesaian aksi (bagian 8b butir 2 dan 8) dan tidak ada di Expected TC. Search dengan nama record bersuffix unik menggantikan kata kunci TC (S-12); akun aktor pada System Log dirujuk lewat email Fixture (R-06).
- Urutan: mengikuti sourceTc.
- Ukuran spec (45 langkah, di atas smell 35 langkah): satu topik, satu halaman, satu kelas harness; tiap blok TC berdiri sendiri dengan record milik spec sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal (alasan R3). Blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom) tidak dihitung dalam smell 35 langkah (bagian 3).
- Temuan untuk QA:
  - TC-AC-DN-491 Expected b memakai total absolut 12 entri dan 2 halaman; spec memakai selisih terhadap baseline N0 karena audit trail permanen (S-12).
  - TC-AC-DN-506 berjenis Edit tetapi berada di bagian Create karena topiknya Object Activity Log; spec mengikuti TC.
  - Post Condition tanpa langkah observasi tidak diasersi (S-01): TC-AC-DN-488, 491, 506.
  - TC sumber memakai nama literal Pre-setup (`Dock Station`, `Door Antenna`, `Cable Tester`); spec memakai record milik spec bersuffix `{runId}-<NNN>` (S-06, S-12) dan Pre-setup #16 tidak diubah.
