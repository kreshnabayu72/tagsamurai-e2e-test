---
id: TC-GS-UOM-E2E-068-unit-hasil-import-edit-dan-hapus
title: "Unit Hasil Import Type Measurement Dapat Diedit dan Dihapus seperti Unit Manual"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-332
coverage:
  web: automated
---

# Unit Hasil Import Type Measurement Dapat Diedit dan Dihapus seperti Unit Manual

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Master Reference > Measurement.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel `seen` oleh hook suite (lihat `suite.md`, bagian Hook suite).
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi): `Rack {runId}-068` / `rk` (D-20), bebas relasi, dibuat lewat job Import Type `Measurement` yang dijalankan lewat API di hook `before` (sesi uji ini). Unit di-edit menjadi `Rack Unit {runId}-068` / `ru`, lalu dihapus oleh spec lewat UI.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Rack {runId}-068` atau `Rack Unit {runId}-068` (nama yang masih ada) bila masih ada.
- Kemampuan teknis: menjalankan job Import Type Measurement lewat API (disediakan tim FE; mekanisme dan berkas impor tidak disebut TC) dan menunggu job selesai.
- Tidak ada state global yang diubah.
- TC-GS-UOM-332: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement.

## Test Steps

### TC-GS-UOM-332: Unit hasil Import dapat di-Edit dan di-Delete identik dengan unit buatan manual

1. Ketik Search `Rack {runId}-068`, tekan Enter, klik `⋯` pada baris tersebut > Edit, ubah Unit Name menjadi `Rack Unit {runId}-068` dan Symbol menjadi `ru`, klik [Save]
2. Verifikasi toast sukses: "Success, unit has been updated."
3. Verifikasi baris tampil `Rack Unit {runId}-068` / `ru`
4. Klik icon Changelog, ketik Search `Rack {runId}-068`, tekan Enter
5. Verifikasi Changelog: baris Edit dengan Field `Unit Name`, Old Value `Rack {runId}-068`, New Value `Rack Unit {runId}-068`
6. Verifikasi Changelog: baris Edit dengan Field `Symbol`, Old Value `rk`, New Value `ru`
7. Tutup Changelog
8. Klik `⋯` pada baris `Rack Unit {runId}-068` > Delete
9. Verifikasi dialog `Delete Unit` tampil (bukan `Cannot Delete Data`)
10. Klik [Delete] pada dialog
11. Verifikasi toast sukses: "Success, unit has been deleted."
12. Verifikasi `Rack Unit {runId}-068` hilang dari tabel
13. Klik icon Changelog, ketik Search `Rack Unit {runId}-068`, tekan Enter
14. Verifikasi Changelog memuat baris Delete untuk `Rack Unit {runId}-068`

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Kelas harness: lintas modul (Import sebagai pembuat data; Import hanya pemicu seeding).
- Langkah penghubung: langkah 1 (Search baris target; tabel memuat lebih dari satu halaman), langkah 4 dan 13 (Search entri log milik unit), langkah 7 (menutup Changelog).
- Sumber memakai `Rack` / `rk` dan `Rack Unit` / `ru` literal; spec memakai nama bersuffix `{runId}-068` (S-12). Search Changelog pada langkah 4 memakai nama awal `Rack {runId}-068` karena entri Edit memuat Old Value itu; entri Edit dikenali lewat nama bersuffix.
- Entri Import tidak diasersi di spec ini (bukan Expected TC-GS-UOM-332).
- Temuan untuk QA:
  - TC-GS-UOM-332 tidak menyebut mekanisme dan berkas job Import Type Measurement untuk membuat `Rack`; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa endpoint karangan (S-13).
  - TC-GS-UOM-332 Expected b menyebut "dua baris Edit"; spec mengasersi satu baris per Field (langkah 5 dan 6), sesuai isi TC.
