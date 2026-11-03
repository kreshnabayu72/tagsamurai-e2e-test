---
id: TC-AC-DN-E2E-163-log-snapshot-immutability
title: "Snapshot Immutability: Rename Dua Kali dan Rename Tidak Mengubah Entri Lama"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-514
  - TC-AC-DN-515
coverage:
  web: automated
---

# Snapshot Immutability: Rename Dua Kali dan Rename Tidak Mengubah Entri Lama

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (`suite.md`): `beforeEach` (membuka sub-tab Device Name, jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- General Settings entitas uji (Pre-setup #20): Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta; jam server dan jam browser sinkron.
- Data Pre-setup (hanya dibaca): #13, #14, #16, #19, #20.
- Data Dinamis (milik spec, dibuat lewat API di hook `before`, `Unit`, `Antenna`, tanpa SKU): `Pintu Antena {runId}-163` (diubah nama dua kali, TC-AC-DN-514) dan `Pintu Snapshot {runId}-163` (diedit Measurement ke `Box` lalu diubah nama, TC-AC-DN-515).
- Kemampuan teknis (disediakan tim FE/BE): seeding Device Name, SKU, dan riwayat lewat sesi API akun #1 (token tidak dihitung sebagai sesi web, lihat `suite.md`); kemampuan baca jumlah entri Changelog, Activity Log, dan System Log aktor untuk baseline (bagian 8b butir 10).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Entri audit trail yang tercipta (Changelog, Activity Log, System Log aktor) bersifat permanen dan tidak dihapus; record milik spec dihapus di hook `after` dan entri historisnya tetap, bersuffix unik `{runId}-NNN` (`{runId}` hanya digit).

## Test Steps

1. Catat jumlah total entri System Log aktor sebagai baseline S0 (kemampuan baca)
2. TC-AC-DN-514: Rename dua kali tidak mengubah entri rename pertama
3. Ketik Search `Pintu Antena {runId}-163`, tekan Enter
4. Klik ikon row action `⋯` pada baris `Pintu Antena {runId}-163`, lalu klik `Edit`
5. Ubah field Device Name menjadi "Pintu Antena {runId}-163 A"
6. Klik `[Save]`
7. Verifikasi toast sukses "Success, device name has been updated."
8. Ketik Search `Pintu Antena {runId}-163 A`, tekan Enter
9. Klik ikon row action `⋯` pada baris `Pintu Antena {runId}-163 A`, lalu klik `Edit`
10. Ubah field Device Name menjadi "Pintu Antena {runId}-163 B"
11. Klik `[Save]`
12. Verifikasi toast sukses "Success, device name has been updated."
13. Klik ikon Changelog di toolbar
14. Verifikasi popup `Changelog: Device Name` tampil
15. Ketik Search `Pintu Antena {runId}-163`, tekan Enter
16. Verifikasi baris Changelog: Action `Edit`, Device Name `Pintu Antena {runId}-163 A`, Field `Device Name`, Old Value `Pintu Antena {runId}-163`, New Value `Pintu Antena {runId}-163 A`, Modified By `Budi S` (entri rename pertama tetap)
17. Verifikasi baris Changelog: Action `Edit`, Device Name `Pintu Antena {runId}-163 B`, Field `Device Name`, Old Value `Pintu Antena {runId}-163 A`, New Value `Pintu Antena {runId}-163 B`, Modified By `Budi S` (entri rename kedua)
18. Klik ikon close `(X)` pada popup Changelog
19. TC-AC-DN-515: Rename tidak mengubah entri lama di Activity Log dan System Log
20. Buka halaman `Settings > Device > Device Name`
21. Ketik Search `Pintu Snapshot {runId}-163`, tekan Enter
22. Klik ikon row action `⋯` pada baris `Pintu Snapshot {runId}-163`, lalu klik `Edit`
23. Ubah field Measurement dari "Unit" menjadi "Box"
24. Klik `[Save]`
25. Verifikasi toast sukses "Success, device name has been updated."
26. Ketik Search `Pintu Snapshot {runId}-163`, tekan Enter
27. Klik ikon row action `⋯` pada baris `Pintu Snapshot {runId}-163`, lalu klik `Edit`
28. Ubah field Device Name menjadi "Pintu Snapshot {runId}-163 Pro"
29. Klik `[Save]`
30. Verifikasi toast sukses "Success, device name has been updated."
31. Buka menu `Activity Log`, lalu klik tab `User Action`
32. Verifikasi halaman `Activity Log > User Action` tampil
33. Ketik Search `Pintu Snapshot {runId}-163`, tekan Enter
34. Verifikasi entri Edit Field `Measurement` tetap memuat Name `Pintu Snapshot {runId}-163` dan tidak berubah menjadi `Pintu Snapshot {runId}-163 Pro`
35. Buka menu `Settings > User`, cari akun Pre-setup #1 (email dari `Fixture.settings-device-name`), lalu klik namanya
36. Verifikasi halaman `Settings > User > Detail` tampil
37. Klik tab `System Log`
38. Verifikasi tabel System Log aktor tampil
39. Verifikasi total entri System Log aktor bertambah 4 dari baseline S0 (dua Edit pada blok sebelumnya dan dua Edit pada blok ini)
40. Verifikasi entri System Log Edit Field `Measurement` tetap memuat Name `Pintu Snapshot {runId}-163` dan tidak berubah menjadi `Pintu Snapshot {runId}-163 Pro`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): Search menemukan record spec; nama hasil rename memakai akhiran ` A`, ` B`, dan ` Pro` sesudah suffix supaya Search `Pintu Antena {runId}-163` mencakup nama lama dan baru.
- Verifikasi toast sukses pada aksi pemicu ditambahkan sebagai anchor penyelesaian aksi (bagian 8b butir 2 dan 8) dan tidak ada di Expected TC. Search dengan nama record bersuffix unik menggantikan kata kunci TC (S-12); akun aktor pada System Log dirujuk lewat email Fixture (R-06).
- Ukuran spec (40 langkah, di atas smell 35 langkah): satu topik, satu halaman, satu kelas harness; tiap blok TC berdiri sendiri dengan record milik spec sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal (alasan R3). Blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom) tidak dihitung dalam smell 35 langkah (bagian 3).
- Temuan untuk QA:
  - TC-AC-DN-515 mengasersi Name entri lama di Activity Log dan System Log; entri System Log ditemukan lewat selisih jumlah terhadap baseline S0 karena TC tidak memberi cara mencari entri (S-13).
  - Post Condition tanpa langkah observasi tidak diasersi (S-01).
  - TC sumber memakai nama literal Pre-setup (`Dock Station`, `Door Antenna`, `Cable Tester`); spec memakai record milik spec bersuffix `{runId}-<NNN>` (S-06, S-12) dan Pre-setup #16 tidak diubah.
