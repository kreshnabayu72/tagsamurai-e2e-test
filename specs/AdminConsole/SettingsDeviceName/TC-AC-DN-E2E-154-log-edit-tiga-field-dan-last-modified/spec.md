---
id: TC-AC-DN-E2E-154-log-edit-tiga-field-dan-last-modified
title: "Pencatatan Edit: Tiga Field Sekaligus dan Last Modified Diperbarui atau Tetap"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-495
  - TC-AC-DN-507
  - TC-AC-DN-508
coverage:
  web: automated
---

# Pencatatan Edit: Tiga Field Sekaligus dan Last Modified Diperbarui atau Tetap

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (`suite.md`): `beforeEach` (membuka sub-tab Device Name, jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- General Settings entitas uji (Pre-setup #20): Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta; jam server dan jam browser sinkron.
- Data Pre-setup (hanya dibaca): #13, #14, #16 (`Cable Tester` hanya dibaca untuk pembanding), #19 (Last Modified `Cable Tester` `10/09/26 12:25`), #20.
- Data Dinamis (milik spec, dibuat lewat API di hook `before`, tanpa SKU; Last Modified seed berisi waktu pembuatan):

  | Kode | Nama | Measurement | Category | Keterangan | Dipakai oleh |
  |---|---|---|---|---|---|---|
  | F1 | `Cable Tester {runId}-154` | `Unit` | `Accessory` | diubah tiga field | TC-AC-DN-495 |
  | F2 | `Door Antenna {runId}-154` | `Unit` | `Antenna` | diubah nama | TC-AC-DN-507 |
  | F3 | `Door Statis {runId}-154` | `Unit` | `Antenna` | disimpan tanpa perubahan | TC-AC-DN-508 |
- Kemampuan teknis (disediakan tim FE/BE): seeding Device Name, SKU, dan riwayat lewat sesi API akun #1 (token tidak dihitung sebagai sesi web, lihat `suite.md`); kemampuan baca jumlah entri Changelog, Activity Log, dan System Log aktor untuk baseline (bagian 8b butir 10).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Entri audit trail yang tercipta (Changelog, Activity Log, System Log aktor) bersifat permanen dan tidak dihapus; record milik spec dihapus di hook `after` dan entri historisnya tetap, bersuffix unik `{runId}-NNN` (`{runId}` hanya digit).

## Test Steps

1. TC-AC-DN-495: Edit tiga field sekaligus
2. Ketik Search `Cable Tester {runId}-154`, tekan Enter
3. Klik ikon row action `⋯` pada baris `Cable Tester {runId}-154`, lalu klik `Edit`
4. Ubah field Device Name menjadi "Cable Tester Pro {runId}-154"
5. Ubah field Measurement menjadi "Meter"
6. Ubah field Category menjadi "Tag" (expand `TAG` lalu `NFC`)
7. Klik `[Save]`
8. Verifikasi toast sukses "Success, device name has been updated."
9. Klik ikon Changelog di toolbar
10. Verifikasi popup `Changelog: Device Name` tampil
11. Ketik Search `Cable Tester Pro {runId}-154`, tekan Enter
12. Verifikasi 3 baris Edit baru: Field `Device Name` (Old Value `Cable Tester {runId}-154`, New Value `Cable Tester Pro {runId}-154`), Field `Measurement` (Old Value `Unit`, New Value `Meter`), dan Field `Category` (Old Value `TAG > NFC > Accessory`, New Value `TAG > NFC > Tag`)
13. Verifikasi hasil Search berjumlah tepat 3 baris tanpa baris ganda untuk field yang sama dan tanpa baris Device Name lain
14. Verifikasi Modified By ketiga baris adalah `Budi S`
15. Klik ikon close `(X)` pada popup Changelog
16. TC-AC-DN-507: Last Modified diperbarui setelah Edit dengan perubahan
17. Ganti isi kotak Search dengan `Door Antenna {runId}-154`, tekan Enter
18. Klik ikon row action `⋯` pada baris `Door Antenna {runId}-154`, lalu klik `Edit`
19. Ubah field Device Name menjadi "Door Antenna Pro {runId}-154"
20. Klik `[Save]`
21. Verifikasi toast sukses "Success, device name has been updated."
22. Catat nilai kolom Last Modified baris `Door Antenna Pro {runId}-154`
23. Ganti isi kotak Search dengan `Cable Tester`, tekan Enter
24. Catat nilai kolom Last Modified baris `Cable Tester`
25. Klik ikon Changelog di toolbar
26. Verifikasi popup `Changelog: Device Name` tampil
27. Ketik Search `Door Antenna Pro {runId}-154`, tekan Enter
28. Catat nilai kolom Date baris Edit baru
29. Verifikasi nilai Last Modified baris yang dicatat sama dengan nilai Date entri Edit baru pada Changelog dalam format `dd/MM/yy` dan 24 jam
30. Verifikasi nilai Last Modified baris `Cable Tester` yang dicatat tetap `10/09/26 12:25`
31. Klik ikon close `(X)` pada popup Changelog
32. TC-AC-DN-508: Last Modified tidak berubah setelah Edit tanpa perubahan
33. Ganti isi kotak Search dengan `Door Statis {runId}-154`, tekan Enter
34. Catat nilai kolom Last Modified baris `Door Statis {runId}-154` sebelum aksi
35. Klik ikon row action `⋯` pada baris `Door Statis {runId}-154`, lalu klik `Edit`
36. Klik `[Save]` tanpa mengubah field apa pun
37. Verifikasi popup form tertutup
38. Verifikasi nilai kolom Last Modified baris `Door Statis {runId}-154` sama dengan nilai yang dicatat sebelum aksi

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): Search menemukan record spec dan baris pembanding `Cable Tester` (Search `Cable Tester` juga menampilkan record spec F1; baris pembanding adalah yang bernama persis `Cable Tester`).
- Verifikasi toast sukses pada aksi pemicu ditambahkan sebagai anchor penyelesaian aksi (bagian 8b butir 2 dan 8) dan tidak ada di Expected TC. Search dengan nama record bersuffix unik menggantikan kata kunci TC (S-12); akun aktor pada System Log dirujuk lewat email Fixture (R-06).
- Urutan: mengikuti sourceTc.
- Ukuran spec (38 langkah, di atas smell 35 langkah): satu topik, satu halaman, satu kelas harness; tiap blok TC berdiri sendiri dengan record milik spec sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal (alasan R3). Blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom) tidak dihitung dalam smell 35 langkah (bagian 3).
- Temuan untuk QA:
  - TC-AC-DN-508 memakai nilai literal `01/09/26 06:00`; record spec memakai Last Modified seed sehingga spec membandingkan dengan nilai yang dicatat sebelum aksi (S-12).
  - TC-AC-DN-507 Expected b memakai Pre-setup `Cable Tester` hanya untuk dibaca; nilainya bergantung fixture #19 tidak berubah.
  - TC sumber memakai nama literal Pre-setup (`Dock Station`, `Door Antenna`, `Cable Tester`); spec memakai record milik spec bersuffix `{runId}-<NNN>` (S-06, S-12) dan Pre-setup #16 tidak diubah.
