---
id: TC-AC-DN-E2E-156-log-bulk-delete-campuran
title: "Pencatatan Bulk Delete Campuran di Activity Log dan System Log Aktor"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DN-615
coverage:
  web: automated
---

# Pencatatan Bulk Delete Campuran di Activity Log dan System Log Aktor

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 `totalControlDevName_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`, entitas Principal); email dirujuk lewat `Fixture.settings-device-name` (fixture belum ada, disediakan tim FE); password `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite (`suite.md`): `beforeEach` (membuka sub-tab Device Name, jaring pengaman `beforeunload` dan dialog `Unsaved Changes`) dan flag Guided Tooltip `guided_tooltip_seen_ac-settings-device` dinyatakan di `suite.md`; spec ini tidak mengulangnya.
- General Settings entitas uji (Pre-setup #20): Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta; jam server dan jam browser sinkron.
- Data Pre-setup (hanya dibaca): #13, #14, #22 (relasi SKU dan unit BYO disiapkan fixture BE).
- Data Dinamis (milik spec, dibuat lewat API di hook `before`):

  | Kode | Nama | Measurement | Category | Keterangan | Dipakai oleh |
  |---|---|---|---|---|---|---|
  | C1 | `Kabel Uji {runId}-156` | `Unit` | `Accessory` | tanpa SKU, tanpa unit BYO; terhapus | TC-AC-DN-615 |
  | C2 | `Pintu Antena {runId}-156` | `Unit` | `Antenna` | tanpa SKU, tanpa unit BYO; terhapus | TC-AC-DN-615 |
  | C3 | `Pembaca RFID {runId}-156` | `Unit` | `UHF Handheld` | memiliki satu SKU (seed) sehingga di-skip | TC-AC-DN-615 |
- Kemampuan teknis (disediakan tim FE/BE): seeding Device Name, SKU, dan riwayat lewat sesi API akun #1 (token tidak dihitung sebagai sesi web, lihat `suite.md`); kemampuan baca jumlah entri Changelog, Activity Log, dan System Log aktor untuk baseline (bagian 8b butir 10).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`). Entri audit trail yang tercipta (Changelog, Activity Log, System Log aktor) bersifat permanen dan tidak dihapus; record milik spec dihapus di hook `after` dan entri historisnya tetap, bersuffix unik `{runId}-NNN` (`{runId}` hanya digit).

## Test Steps

1. Catat jumlah total entri System Log aktor sebagai baseline Sb0 (kemampuan baca)
2. TC-AC-DN-615: Bulk Delete campuran tercatat di Activity Log dan System Log aktor hanya untuk item yang terhapus
3. Ketik Search `{runId}-156`, tekan Enter
4. Centang checkbox baris `Kabel Uji {runId}-156`
5. Centang checkbox baris `Pintu Antena {runId}-156`
6. Centang checkbox baris `Pembaca RFID {runId}-156`
7. Klik tombol `Bulk Action` pada Bulk Action Bar
8. Klik `Delete`
9. Klik `[Continue]`
10. Verifikasi toast sukses sebagian "Success, device name has been deleted. Some items were skipped (still has SKUs or registered devices)."
11. Buka menu `Activity Log`, lalu klik tab `User Action`
12. Verifikasi halaman `Activity Log > User Action` tampil
13. Ketik Search `Kabel Uji {runId}-156`, tekan Enter
14. Verifikasi entri Activity Log: Action `Delete`, Object `Device Name`, Name `Kabel Uji {runId}-156`, Field `Device Name`, Old Value `Kabel Uji {runId}-156`, New Value `—`, Modified By `Budi S`
15. Ganti isi kotak Search dengan `Pintu Antena {runId}-156`, tekan Enter
16. Verifikasi entri Activity Log: Action `Delete`, Object `Device Name`, Name `Pintu Antena {runId}-156`, Field `Device Name`, Old Value `Pintu Antena {runId}-156`, New Value `—`, Modified By `Budi S`
17. Ganti isi kotak Search dengan `Pembaca RFID {runId}-156`, tekan Enter
18. Verifikasi hasil Search `Pembaca RFID {runId}-156` tidak memuat entri Action `Delete`
19. Buka menu `Settings > User`, cari akun Pre-setup #1 (email dari `Fixture.settings-device-name`), lalu klik namanya
20. Verifikasi halaman `Settings > User > Detail` tampil
21. Klik tab `System Log`
22. Verifikasi tabel System Log aktor tampil
23. Verifikasi total entri System Log aktor bertambah tepat 2 dari baseline Sb0 dengan dua entri Action `Delete`, Object `Device Name`: satu untuk Name `Kabel Uji {runId}-156` dan satu untuk Name `Pintu Antena {runId}-156`, Field `Device Name`, Old Value sama dengan Name, New Value `—`
24. Verifikasi tabel System Log tidak memiliki kolom Modified By
25. Verifikasi System Log aktor tidak memuat entri Delete untuk `Pembaca RFID {runId}-156` (selisih tepat 2)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): Search menemukan record spec; baseline Sb0 dicatat sebelum aksi.
- Verifikasi toast sukses pada aksi pemicu ditambahkan sebagai anchor penyelesaian aksi (bagian 8b butir 2 dan 8) dan tidak ada di Expected TC. Search dengan nama record bersuffix unik menggantikan kata kunci TC (S-12); akun aktor pada System Log dirujuk lewat email Fixture (R-06).
- P-1: asersi bahwa item yang di-skip tidak tercatat (Activity Log dan System Log) berada di spec ini bersama pencatatannya karena state berat (record ber-SKU dan Bulk Delete campuran) dibangun oleh aksi TC yang sama; setiap asersi absence didahului anchor positif (entri item terhapus dan toast sukses sebagian).
- Temuan untuk QA:
  - Precondition TC-AC-DN-615 tidak menyebut Pre-setup #20 meskipun asersi memakai Activity Log; tidak memengaruhi asersi.
  - TC sumber memakai nama literal Pre-setup (`Dock Station`, `Door Antenna`, `Cable Tester`); spec memakai record milik spec bersuffix `{runId}-<NNN>` (S-06, S-12) dan Pre-setup #16 tidak diubah.
