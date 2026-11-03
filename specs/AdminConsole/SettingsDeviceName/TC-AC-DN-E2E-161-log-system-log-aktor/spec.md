---
id: TC-AC-DN-E2E-161-log-system-log-aktor
title: "System Log Aktor: Entri Edit, Create, dan Delete Device Name"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-509
  - TC-AC-DN-510
  - TC-AC-DN-511
coverage:
  web: automated
---

# System Log Aktor: Entri Edit, Create, dan Delete Device Name

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (`suite.md`): `beforeEach` (membuka sub-tab Device Name, jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- General Settings entitas uji (Pre-setup #20): Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta; jam server dan jam browser sinkron.
- Data Pre-setup (hanya dibaca): #13, #14, #16.
- Data Dinamis (milik spec): `Pintu Antena {runId}-161` (`Unit`, `Antenna`, dibuat lewat API, diedit Measurement ke `Box`, TC-AC-DN-509); `Dock Station {runId}-161` (`Unit`, `Accessory`, dibuat lewat form, TC-AC-DN-510); `Kabel Uji {runId}-161` (`Unit`, `Accessory`, dibuat lewat API, terhapus, TC-AC-DN-511).
- Kemampuan teknis (disediakan tim FE/BE): seeding Device Name, SKU, dan riwayat lewat sesi API akun #1 (token tidak dihitung sebagai sesi web, lihat `suite.md`); kemampuan baca jumlah entri Changelog, Activity Log, dan System Log aktor untuk baseline (bagian 8b butir 10).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Entri audit trail yang tercipta (Changelog, Activity Log, System Log aktor) bersifat permanen dan tidak dihapus; record milik spec dihapus di hook `after` dan entri historisnya tetap, bersuffix unik `{runId}-NNN` (`{runId}` hanya digit).

## Test Steps

1. Catat jumlah total entri System Log aktor sebagai baseline S0 (kemampuan baca)
2. TC-AC-DN-509: System Log aktor memuat entri Edit Device Name
3. Ketik Search `Pintu Antena {runId}-161`, tekan Enter
4. Klik ikon row action `⋯` pada baris `Pintu Antena {runId}-161`, lalu klik `Edit`
5. Ubah field Measurement dari "Unit" menjadi "Box"
6. Klik `[Save]`
7. Verifikasi toast sukses "Success, device name has been updated."
8. Buka menu `Settings > User`, cari akun Pre-setup #1 (email dari `Fixture.settings-device-name`), lalu klik namanya
9. Verifikasi halaman `Settings > User > Detail` tampil
10. Klik tab `System Log`
11. Verifikasi tabel System Log aktor tampil
12. Verifikasi total entri System Log aktor bertambah tepat 1 dari S0 dengan entri Action `Edit`, Object `Device Name`, Name `Pintu Antena {runId}-161`, Field `Measurement`, Old Value `Unit`, New Value `Box`
13. Verifikasi tabel System Log tidak memiliki kolom Modified By
14. TC-AC-DN-510: System Log aktor memuat entri Create Device Name
15. Buka halaman `Settings > Device > Device Name`
16. Klik `+ Device Name`
17. Ketik "Dock Station {runId}-161" pada field Device Name
18. Pilih "Unit" pada field Measurement
19. Pada field Category, expand `TAG` lalu `NFC` dan pilih leaf `Accessory` pada TreeSelect
20. Klik `[Submit]`
21. Verifikasi toast sukses "Success, device name has been created."
22. Buka menu `Settings > User`, cari akun Pre-setup #1 (email dari `Fixture.settings-device-name`), lalu klik namanya
23. Verifikasi halaman `Settings > User > Detail` tampil
24. Klik tab `System Log`
25. Verifikasi tabel System Log aktor tampil
26. Verifikasi total entri System Log aktor bertambah tepat 1 dari entri sebelumnya (S0 + 2) dan memuat satu entri Action `Create`, Object `Device Name`, Name `Dock Station {runId}-161`
27. Verifikasi entri Field `Device Name`: Old Value `—`, New Value `Dock Station {runId}-161`
28. Verifikasi tidak ada entri Field `Measurement` atau `Category` untuk `Dock Station {runId}-161` (selisih tepat 1 entri)
29. TC-AC-DN-511: System Log aktor memuat entri Delete Device Name
30. Buka halaman `Settings > Device > Device Name`
31. Ketik Search `Kabel Uji {runId}-161`, tekan Enter
32. Klik ikon row action `⋯` pada baris `Kabel Uji {runId}-161`, lalu klik `Delete`
33. Klik `[Delete]` pada dialog "Delete Device Name"
34. Verifikasi toast sukses "Success, device name has been deleted."
35. Buka menu `Settings > User`, cari akun Pre-setup #1 (email dari `Fixture.settings-device-name`), lalu klik namanya
36. Verifikasi halaman `Settings > User > Detail` tampil
37. Klik tab `System Log`
38. Verifikasi tabel System Log aktor tampil
39. Verifikasi total entri System Log aktor bertambah tepat 1 dari entri sebelumnya (S0 + 3) dan memuat satu entri Action `Delete`, Object `Device Name`, Name `Kabel Uji {runId}-161`
40. Verifikasi entri Field `Device Name`: Old Value `Kabel Uji {runId}-161`, New Value `—`
41. Verifikasi tidak ada entri Field `Measurement` atau `Category` untuk `Kabel Uji {runId}-161` (selisih tepat 1 entri)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): baseline S0 dicatat sebelum aksi pertama; asersi jumlah memakai selisih kumulatif (S0 + 1, S0 + 2, S0 + 3) karena aksi berurutan.
- Verifikasi toast sukses pada aksi pemicu ditambahkan sebagai anchor penyelesaian aksi (bagian 8b butir 2 dan 8) dan tidak ada di Expected TC. Search dengan nama record bersuffix unik menggantikan kata kunci TC (S-12); akun aktor pada System Log dirujuk lewat email Fixture (R-06).
- Ukuran spec (41 langkah, di atas smell 35 langkah): satu topik, satu halaman, satu kelas harness; tiap blok TC berdiri sendiri dengan record milik spec sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal (alasan R3). Blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom) tidak dihitung dalam smell 35 langkah (bagian 3).
- Temuan untuk QA:
  - TC sumber tidak memberi cara mencari entri tertentu pada tabel System Log; spec mengasersi entri baru lewat selisih jumlah terhadap baseline S0 dan isi entri terbaru (S-13).
  - Post Condition tanpa langkah observasi tidak diasersi (S-01).
  - TC sumber memakai nama literal Pre-setup (`Dock Station`, `Door Antenna`, `Cable Tester`); spec memakai record milik spec bersuffix `{runId}-<NNN>` (S-06, S-12) dan Pre-setup #16 tidak diubah.
