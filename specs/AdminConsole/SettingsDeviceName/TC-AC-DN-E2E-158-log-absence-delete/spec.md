---
id: TC-AC-DN-E2E-158-log-absence-delete
title: "Absence Log: Delete Tidak Mencatat Field Measurement atau Category"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-497
  - TC-AC-DN-498
coverage:
  web: automated
---

# Absence Log: Delete Tidak Mencatat Field Measurement atau Category

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (`suite.md`): `beforeEach` (membuka sub-tab Device Name, jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- General Settings entitas uji (Pre-setup #20): Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta; jam server dan jam browser sinkron.
- Data Pre-setup (hanya dibaca): #13, #14, #16, #19, #20.
- Data Dinamis (milik spec, dibuat lewat API di hook `before`, tanpa SKU dan unit BYO, terhapus oleh aksi): `Kabel Uji {runId}-158` (`Unit`, `TAG > NFC > Accessory`, TC-AC-DN-497) dan `Kabel Dua {runId}-158` (`Unit`, `TAG > NFC > Accessory`, TC-AC-DN-498). Aksi Delete adalah pemicu absence (P-5 butir a); baseline berasal dari Search nama bersuffix unik (S-12).
- Kemampuan teknis (disediakan tim FE/BE): seeding Device Name, SKU, dan riwayat lewat sesi API akun #1 (token tidak dihitung sebagai sesi web, lihat `suite.md`); kemampuan baca jumlah entri Changelog, Activity Log, dan System Log aktor untuk baseline (bagian 8b butir 10).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Entri audit trail yang tercipta (Changelog, Activity Log, System Log aktor) bersifat permanen dan tidak dihapus; record milik spec dihapus di hook `after` dan entri historisnya tetap, bersuffix unik `{runId}-NNN` (`{runId}` hanya digit).

## Test Steps

1. TC-AC-DN-497: Delete tidak mencatat entri Field Measurement
2. Ketik Search `Kabel Uji {runId}-158`, tekan Enter
3. Klik ikon row action `⋯` pada baris `Kabel Uji {runId}-158`, lalu klik `Delete`
4. Klik `[Delete]` pada dialog "Delete Device Name"
5. Verifikasi toast sukses "Success, device name has been deleted."
6. Klik ikon Changelog di toolbar
7. Verifikasi popup `Changelog: Device Name` tampil
8. Ketik Search `Kabel Uji {runId}-158`, tekan Enter
9. Verifikasi hasil Search `Kabel Uji {runId}-158` memuat baris Action `Delete` ber-Field `Device Name`
10. Verifikasi hasil Search `Kabel Uji {runId}-158` tidak memuat baris Action `Delete` ber-Field `Measurement`
11. Klik ikon close `(X)` pada popup Changelog
12. Buka menu `Activity Log`, lalu klik tab `User Action`
13. Verifikasi halaman `Activity Log > User Action` tampil
14. Ketik Search `Kabel Uji {runId}-158`, tekan Enter
15. Verifikasi hasil Search `Kabel Uji {runId}-158` memuat satu entri Action `Delete`, Object `Device Name`, Name `Kabel Uji {runId}-158`, Field `Device Name`
16. Verifikasi tidak ada entri Field `Measurement` pada hasil Search `Kabel Uji {runId}-158`
17. TC-AC-DN-498: Delete tidak mencatat entri Field Category
18. Buka halaman `Settings > Device > Device Name`
19. Ketik Search `Kabel Dua {runId}-158`, tekan Enter
20. Klik ikon row action `⋯` pada baris `Kabel Dua {runId}-158`, lalu klik `Delete`
21. Klik `[Delete]` pada dialog "Delete Device Name"
22. Verifikasi toast sukses "Success, device name has been deleted."
23. Klik ikon Changelog di toolbar
24. Verifikasi popup `Changelog: Device Name` tampil
25. Ketik Search `Kabel Dua {runId}-158`, tekan Enter
26. Verifikasi hasil Search `Kabel Dua {runId}-158` memuat baris Action `Delete` ber-Field `Device Name`
27. Verifikasi hasil Search `Kabel Dua {runId}-158` tidak memuat baris Action `Delete` ber-Field `Category`
28. Klik ikon close `(X)` pada popup Changelog
29. Buka menu `Activity Log`, lalu klik tab `User Action`
30. Verifikasi halaman `Activity Log > User Action` tampil
31. Ketik Search `Kabel Dua {runId}-158`, tekan Enter
32. Verifikasi hasil Search `Kabel Dua {runId}-158` memuat satu entri Action `Delete`, Object `Device Name`, Name `Kabel Dua {runId}-158`, Field `Device Name`
33. Verifikasi tidak ada entri Field `Category` pada hasil Search `Kabel Dua {runId}-158`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): Search menemukan record spec pada List, Changelog, dan Activity Log.
- Verifikasi toast sukses pada aksi pemicu ditambahkan sebagai anchor penyelesaian aksi (bagian 8b butir 2 dan 8) dan tidak ada di Expected TC. Search dengan nama record bersuffix unik menggantikan kata kunci TC (S-12); akun aktor pada System Log dirujuk lewat email Fixture (R-06).
- Ukuran spec (33 langkah): satu topik, satu halaman, satu kelas harness; tiap blok TC berdiri sendiri dengan record milik spec sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal (alasan R3). Blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom) tidak dihitung dalam smell 35 langkah (bagian 3).
- Anchor absence (bagian 8b butir 2): toast sukses Delete dan baris Delete Field `Device Name` milik record spec tampil sebelum asersi absence.
- Temuan untuk QA:
  - TC sumber mencari kata kunci `Delete` dan menghitung baris awal `Retired Gateway`; spec membatasi hasil dengan nama record bersuffix unik (S-12).
  - TC sumber memakai nama literal Pre-setup (`Dock Station`, `Door Antenna`, `Cable Tester`); spec memakai record milik spec bersuffix `{runId}-<NNN>` (S-06, S-12) dan Pre-setup #16 tidak diubah.
