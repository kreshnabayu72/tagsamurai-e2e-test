---
id: TC-AC-DN-E2E-162-log-sinkron-dan-pelaku
title: "Pencatatan Sinkron Changelog/Activity Log/System Log, Entri Tetap setelah Delete, dan Pelaku Entri"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-513
  - TC-AC-DN-517
  - TC-AC-DN-516
coverage:
  web: automated
---

# Pencatatan Sinkron Changelog/Activity Log/System Log, Entri Tetap setelah Delete, dan Pelaku Entri

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (`suite.md`): `beforeEach` (membuka sub-tab Device Name, jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- General Settings entitas uji (Pre-setup #20): Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta; jam server dan jam browser sinkron.
- Data Pre-setup (hanya dibaca): #13, #14, #16, #19, #20. Pelaku kedua: Maya Putri (Pre-setup #2) `totalControlDevName2_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DN_TC2_PASSWORD` (disediakan tim FE); hanya memakai sesi API untuk memicu perubahan, tidak ada sesi UI kedua.
- Data Dinamis (milik spec, dibuat lewat sesi API akun #1 di hook `before` sehingga entri awal Modified By `Budi S`; `Unit`, tanpa SKU):

  | Kode | Nama | Measurement | Category | Keterangan | Dipakai oleh |
  |---|---|---|---|---|---|---|
  | P1 | `Pintu Antena {runId}-162` | `Unit` | `Antenna` | diedit Measurement ke `Box` | TC-AC-DN-513 |
  | M1 | `Pintu Maya {runId}-162` | `Unit` | `Antenna` | diedit oleh Maya Putri; entri awal Create oleh `Budi S` | TC-AC-DN-517 |
  | Q | `Kabel Uji {runId}-162` | `Unit` | `TAG > NFC > Accessory` | riwayat seed: Create (Category `TAG > NFC > Tag`), Edit Category `TAG > NFC > Tag` ke `TAG > NFC > Accessory`, Edit Measurement `Unit` ke `Meter`, Edit Measurement `Meter` ke `Unit` (precondition, diasersi); terhapus | TC-AC-DN-516 |
- Kemampuan teknis (disediakan tim FE/BE): seeding Device Name, SKU, dan riwayat lewat sesi API akun #1 (token tidak dihitung sebagai sesi web, lihat `suite.md`); kemampuan baca jumlah entri Changelog, Activity Log, dan System Log aktor untuk baseline (bagian 8b butir 10).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Entri audit trail yang tercipta (Changelog, Activity Log, System Log aktor) bersifat permanen dan tidak dihapus; record milik spec dihapus di hook `after` dan entri historisnya tetap, bersuffix unik `{runId}-NNN` (`{runId}` hanya digit).

## Test Steps

1. TC-AC-DN-513: Satu Edit tercatat sinkron di Changelog, Activity Log, dan System Log aktor
2. Ketik Search `Pintu Antena {runId}-162`, tekan Enter
3. Klik ikon row action `⋯` pada baris `Pintu Antena {runId}-162`, lalu klik `Edit`
4. Ubah field Measurement dari "Unit" menjadi "Box"
5. Klik `[Save]`
6. Verifikasi toast sukses "Success, device name has been updated."
7. Klik ikon Changelog di toolbar
8. Verifikasi popup `Changelog: Device Name` tampil
9. Ketik Search `Pintu Antena {runId}-162`, tekan Enter
10. Catat nilai Date baris Edit baru
11. Verifikasi baris Changelog: Action `Edit`, Device Name `Pintu Antena {runId}-162`, Field `Measurement`, Old Value `Unit`, New Value `Box`, Modified By `Budi S`
12. Klik ikon close `(X)` pada popup Changelog
13. Buka menu `Activity Log`, lalu klik tab `User Action`
14. Verifikasi halaman `Activity Log > User Action` tampil
15. Ketik Search `Pintu Antena {runId}-162`, tekan Enter
16. Verifikasi entri Activity Log tab User Action memuat Action `Edit`, Field `Measurement`, Old Value `Unit`, New Value `Box` yang sama dengan Changelog dan Date yang sama dengan nilai yang dicatat
17. Buka menu `Settings > User`, cari akun Pre-setup #1 (email dari `Fixture.settings-device-name`), lalu klik namanya
18. Verifikasi halaman `Settings > User > Detail` tampil
19. Klik tab `System Log`
20. Verifikasi tabel System Log aktor tampil
21. Verifikasi entri System Log aktor memuat Action `Edit`, Field `Measurement`, Old Value `Unit`, New Value `Box` yang sama dengan Changelog dan Date yang sama dengan nilai yang dicatat
22. TC-AC-DN-517: Entri baru mencatat pelaku Edit yang sedang login
23. Maya Putri (Pre-setup #2, sesi API) mengubah Measurement `Pintu Maya {runId}-162` dari "Unit" menjadi "Box" hingga tersimpan
24. Tunggu aksi selesai (permintaan sesi API selesai)
25. Buka halaman `Settings > Device > Device Name`
26. Ketik Search `Pintu Maya {runId}-162`, tekan Enter
27. Klik ikon Changelog di toolbar
28. Verifikasi popup `Changelog: Device Name` tampil
29. Ketik Search `Pintu Maya {runId}-162`, tekan Enter
30. Verifikasi entri Edit Field `Measurement` baru memiliki Modified By `Maya P` (Device Name `Pintu Maya {runId}-162`, Old Value `Unit`, New Value `Box`)
31. Verifikasi entri awal milik `Budi S` untuk `Pintu Maya {runId}-162` tidak berubah
32. Klik ikon close `(X)` pada popup Changelog
33. TC-AC-DN-516: Entri log tetap ada setelah Device Name dihapus
34. Ganti isi kotak Search dengan `Kabel Uji {runId}-162`, tekan Enter
35. Klik ikon row action `⋯` pada baris `Kabel Uji {runId}-162`, lalu klik `Delete`
36. Klik `[Delete]` pada dialog "Delete Device Name"
37. Verifikasi toast sukses "Success, device name has been deleted."
38. Klik ikon Changelog di toolbar
39. Verifikasi popup `Changelog: Device Name` tampil
40. Ketik Search `Kabel Uji {runId}-162`, tekan Enter
41. Verifikasi entri awal `Kabel Uji {runId}-162` (1 Create, 1 Edit Category, dan 2 Edit Measurement) tetap tampil dengan nilai semula
42. Verifikasi satu entri Delete baru untuk `Kabel Uji {runId}-162` (Field `Device Name`) tampil bersama entri awal sehingga hasil Search berjumlah 5 baris

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): Search menemukan record spec; navigasi ke Device Name sesudah aksi sesi API; 'Tunggu aksi selesai' sesudah pemicu sesi API (bagian 8b butir 8).
- Verifikasi toast sukses pada aksi pemicu ditambahkan sebagai anchor penyelesaian aksi (bagian 8b butir 2 dan 8) dan tidak ada di Expected TC. Search dengan nama record bersuffix unik menggantikan kata kunci TC (S-12); akun aktor pada System Log dirujuk lewat email Fixture (R-06).
- Urutan: 513, 517, 516 mengikuti sourceTc.
- Ukuran spec (42 langkah, di atas smell 35 langkah): satu topik, satu halaman, satu kelas harness; tiap blok TC berdiri sendiri dengan record milik spec sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal (alasan R3). Blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom) tidak dihitung dalam smell 35 langkah (bagian 3).
- Temuan untuk QA:
  - TC-AC-DN-517 menyebut Maya Putri melakukan Edit dan membaca Changelog lewat UI; spec memakai sesi API untuk aksi dan sesi Budi Santoso untuk membaca Changelog (keputusan pelaku kedua), sehingga tampilan UI sesi Maya tidak diasersi.
  - TC-AC-DN-517 mengasumsikan entri awal bermodifier `Budi S` pada record; pada record spec asumsi itu bergantung pada fixture seeding yang menulis entri atas akun #1 (disediakan tim FE/BE).
  - Post Condition tanpa langkah observasi tidak diasersi (S-01).
  - TC sumber memakai nama literal Pre-setup (`Dock Station`, `Door Antenna`, `Cable Tester`); spec memakai record milik spec bersuffix `{runId}-<NNN>` (S-06, S-12) dan Pre-setup #16 tidak diubah.
