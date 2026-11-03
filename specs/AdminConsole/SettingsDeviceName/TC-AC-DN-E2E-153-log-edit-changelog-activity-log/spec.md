---
id: TC-AC-DN-E2E-153-log-edit-changelog-activity-log
title: "Pencatatan Edit: Satu Entri per Field yang Berubah di Changelog dan Activity Log"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-492
  - TC-AC-DN-493
  - TC-AC-DN-494
coverage:
  web: automated
---

# Pencatatan Edit: Satu Entri per Field yang Berubah di Changelog dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (`suite.md`): `beforeEach` (membuka sub-tab Device Name, jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- General Settings entitas uji (Pre-setup #20): Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta; jam server dan jam browser sinkron.
- Data Pre-setup (hanya dibaca): #13, #14 (jalur penuh `TAG > NFC > Accessory` dan `TAG > NFC > Tag`), #16, #19, #20.
- Data Dinamis (milik spec, dibuat lewat API di hook `before`, tanpa SKU):

  | Kode | Nama | Measurement | Category | Keterangan | Dipakai oleh |
  |---|---|---|---|---|---|---|
  | E1 | `Door Antenna {runId}-153` | `Unit` | `Antenna` | diubah menjadi `Door Antenna Pro {runId}-153` | TC-AC-DN-492 |
  | E2 | `Door Ukur {runId}-153` | `Unit` | `Antenna` | Measurement diubah ke `Box` | TC-AC-DN-493 |
  | E3 | `Cable Tester {runId}-153` | `Unit` | `Accessory` (jalur `TAG > NFC > Accessory`) | Category diubah ke `Tag` | TC-AC-DN-494 |
- Kemampuan teknis (disediakan tim FE/BE): seeding Device Name, SKU, dan riwayat lewat sesi API akun #1 (token tidak dihitung sebagai sesi web, lihat `suite.md`); kemampuan baca jumlah entri Changelog, Activity Log, dan System Log aktor untuk baseline (bagian 8b butir 10).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Entri audit trail yang tercipta (Changelog, Activity Log, System Log aktor) bersifat permanen dan tidak dihapus; record milik spec dihapus di hook `after` dan entri historisnya tetap, bersuffix unik `{runId}-NNN` (`{runId}` hanya digit).

## Test Steps

1. TC-AC-DN-492: Edit rename mencatat satu entri Field Device Name
2. Ketik Search `Door Antenna {runId}-153`, tekan Enter
3. Klik ikon row action `⋯` pada baris `Door Antenna {runId}-153`, lalu klik `Edit`
4. Ubah field Device Name menjadi "Door Antenna Pro {runId}-153" tanpa mengubah field lain
5. Klik `[Save]`
6. Verifikasi toast sukses "Success, device name has been updated."
7. Klik ikon Changelog di toolbar
8. Verifikasi popup `Changelog: Device Name` tampil
9. Ketik Search `Door Antenna Pro {runId}-153`, tekan Enter
10. Verifikasi baris Changelog: Action `Edit`, Device Name `Door Antenna Pro {runId}-153`, Field `Device Name`, Old Value `Door Antenna {runId}-153`, New Value `Door Antenna Pro {runId}-153`, Modified By `Budi S`
11. Verifikasi hasil Search hanya memuat 1 baris Field `Device Name` (jumlah baris 1, tanpa baris Field `Measurement` atau `Category`)
12. Klik ikon close `(X)` pada popup Changelog
13. Buka menu `Activity Log`, lalu klik tab `User Action`
14. Verifikasi halaman `Activity Log > User Action` tampil
15. Ketik Search `Door Antenna Pro {runId}-153`, tekan Enter
16. Verifikasi entri Activity Log: Action `Edit`, Object `Device Name`, Name `Door Antenna Pro {runId}-153`, Field `Device Name`, Old Value `Door Antenna {runId}-153`, New Value `Door Antenna Pro {runId}-153`, Modified By `Budi S`
17. TC-AC-DN-493: Edit Measurement mencatat satu entri Field Measurement
18. Buka halaman `Settings > Device > Device Name`
19. Ketik Search `Door Ukur {runId}-153`, tekan Enter
20. Catat jumlah entri Changelog yang memuat `Door Ukur {runId}-153` sebagai baseline B2 (kemampuan baca)
21. Klik ikon row action `⋯` pada baris `Door Ukur {runId}-153`, lalu klik `Edit`
22. Ubah field Measurement dari "Unit" menjadi "Box" tanpa mengubah field lain
23. Klik `[Save]`
24. Verifikasi toast sukses "Success, device name has been updated."
25. Klik ikon Changelog di toolbar
26. Verifikasi popup `Changelog: Device Name` tampil
27. Ketik Search `Door Ukur {runId}-153`, tekan Enter
28. Verifikasi jumlah entri Changelog untuk `Door Ukur {runId}-153` bertambah tepat 1 dari baseline B2
29. Verifikasi baris Changelog: Action `Edit`, Device Name `Door Ukur {runId}-153`, Field `Measurement`, Old Value `Unit`, New Value `Box`, Modified By `Budi S`
30. Klik ikon close `(X)` pada popup Changelog
31. Buka menu `Activity Log`, lalu klik tab `User Action`
32. Verifikasi halaman `Activity Log > User Action` tampil
33. Ketik Search `Door Ukur {runId}-153`, tekan Enter
34. Verifikasi entri Activity Log: Action `Edit`, Object `Device Name`, Name `Door Ukur {runId}-153`, Field `Measurement`, Old Value `Unit`, New Value `Box`, Modified By `Budi S`
35. TC-AC-DN-494: Edit Category mencatat satu entri Field Category
36. Buka halaman `Settings > Device > Device Name`
37. Ketik Search `Cable Tester {runId}-153`, tekan Enter
38. Catat jumlah entri Changelog yang memuat `Cable Tester {runId}-153` sebagai baseline B3 (kemampuan baca)
39. Klik ikon row action `⋯` pada baris `Cable Tester {runId}-153`, lalu klik `Edit`
40. Ubah field Category dari "Accessory" menjadi "Tag" tanpa mengubah field lain
41. Klik `[Save]`
42. Verifikasi toast sukses "Success, device name has been updated."
43. Klik ikon Changelog di toolbar
44. Verifikasi popup `Changelog: Device Name` tampil
45. Ketik Search `Cable Tester {runId}-153`, tekan Enter
46. Verifikasi jumlah entri Changelog untuk `Cable Tester {runId}-153` bertambah tepat 1 dari baseline B3
47. Verifikasi baris Changelog: Action `Edit`, Device Name `Cable Tester {runId}-153`, Field `Category`, Old Value `TAG > NFC > Accessory`, New Value `TAG > NFC > Tag`, Modified By `Budi S`
48. Klik ikon close `(X)` pada popup Changelog
49. Buka menu `Activity Log`, lalu klik tab `User Action`
50. Verifikasi halaman `Activity Log > User Action` tampil
51. Ketik Search `Cable Tester {runId}-153`, tekan Enter
52. Verifikasi entri Activity Log: Action `Edit`, Object `Device Name`, Name `Cable Tester {runId}-153`, Field `Category`, Old Value `TAG > NFC > Accessory`, New Value `TAG > NFC > Tag`, Modified By `Budi S`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): Search pada Changelog dan Activity Log menemukan entri milik record spec; baseline B2 dan B3 dicatat sebelum aksi karena seeding via API dapat menulis entri Create.
- Verifikasi toast sukses pada aksi pemicu ditambahkan sebagai anchor penyelesaian aksi (bagian 8b butir 2 dan 8) dan tidak ada di Expected TC. Search dengan nama record bersuffix unik menggantikan kata kunci TC (S-12); akun aktor pada System Log dirujuk lewat email Fixture (R-06).
- Ukuran spec (52 langkah, di atas smell 35 langkah): satu topik, satu halaman, satu kelas harness; tiap blok TC berdiri sendiri dengan record milik spec sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal (alasan R3). Blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom) tidak dihitung dalam smell 35 langkah (bagian 3).
- Temuan untuk QA:
  - TC-AC-DN-492 Expected b ('tidak ada baris Field Measurement atau Category') ditulis sebagai asersi jumlah baris (tepat 1), bukan absence kelas g (S-05).
  - TC-AC-DN-493 dan TC-AC-DN-494 memakai Search kata kunci `Door Antenna`/`Category`; spec memakai nama record unik. Post Condition tanpa langkah observasi tidak diasersi (S-01).
  - TC sumber memakai nama literal Pre-setup (`Dock Station`, `Door Antenna`, `Cable Tester`); spec memakai record milik spec bersuffix `{runId}-<NNN>` (S-06, S-12) dan Pre-setup #16 tidak diubah.
