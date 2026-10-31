---
id: TC-GS-UOM-E2E-061-konflik-in-use-saat-confirm-delete
title: "Konflik Unit Menjadi In-Use Saat Confirm Delete (Single dan Bulk)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UOM-102
  - TC-GS-UOM-123
coverage:
  web: automated
---

# Konflik Unit Menjadi In-Use Saat Confirm Delete (Single dan Bulk)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Master Reference > Measurement.
- Pelaku pemicu (hanya lewat sesi API, tanpa login UI): Admin FAMS Client A, `famsAdmin_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.FA_ADMIN_PASSWORD`. Email akun ini tidak tertulis di Pre-setup TC Measurement (lihat Temuan untuk QA); fixture disediakan tim FE. Admin FAMS berhak membuat dan menghapus Asset Name FAMS.
- Environment variable: `GS_TC_PASSWORD`, `FA_ADMIN_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel `seen` oleh hook suite (lihat `suite.md`, bagian Hook suite).
- Data dinamis (suffix per run dan nomor spec, bagian 5 konvensi), di-seed lewat API di hook `before`, milik spec ini:
  - `Kilowatt Hour {runId}-061` / `kWh-meter1` (D-06): bebas relasi sampai Asset Name `Water Tank {runId}-061` dibuat pada TC-GS-UOM-102; unit tidak terhapus.
  - `Foot {runId}-061` / `ft` dan `Inch {runId}-061` / `in`: bebas relasi; `Foot` menjadi dipakai Asset Name `Foot Item {runId}-061` pada TC-GS-UOM-123; `Inch` terhapus.
- Nilai field wajib lain Asset Name FAMS yang dibuat lewat API (`Water Tank` dan `Foot Item`): Category (kategori daun) dan TAG Type (minimal 1 opsi). Fixture `fixtures/measurement.json` belum ada; tim FE menyediakannya:

  | Kunci fixture | Field | Nilai |
  |---|---|---|
  | `assetName.category` | Category | disediakan tim FE |
  | `assetName.tagType` | TAG Type | disediakan tim FE |

  Field Measurement Asset Name diisi unit yang dirujuk langkah.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Asset Name `Water Tank {runId}-061` dan `Foot Item {runId}-061` bila ada, lalu unit `Kilowatt Hour`, `Foot`, `Inch` bersuffix `{runId}-061` bila masih ada (Asset Name dihapus sebelum unitnya).
- Kemampuan teknis: sesi API aktor (lihat `suite.md`, bagian Hook suite) untuk Admin FAMS membuat Asset Name FAMS yang memakai Measurement tertentu dan menunggu hasil tersimpan.
- Tidak ada state global yang diubah.
- Jeda nyata (bagian 6 konvensi, jeda pendek ±30 detik): langkah 8 menunggu toast sebelumnya hilang otomatis; lama hilang otomatis mengikuti perilaku aplikasi dan tidak ditetapkan TC.
- TC-GS-UOM-102, 123: login sebagai Total Control dan berada di Global Settings > Master Reference > Measurement.

## Test Steps

### TC-GS-UOM-102: Referensi baru muncul di antara cek awal dan Confirm memblokir Delete

1. Ketik Search `Kilowatt Hour {runId}-061`, tekan Enter, klik `⋯` pada baris tersebut > Delete
2. [Admin FAMS, sesi API] Buat Asset Name `Water Tank {runId}-061` dengan Measurement `Kilowatt Hour {runId}-061` hingga tersimpan
3. Klik [Delete] pada dialog `Delete Unit`
4. Verifikasi dialog `Cannot Delete Data` tampil dengan sub-bullet `FAMS (1 asset name)`
5. Verifikasi tidak ada toast sukses
6. Klik [OK]
7. Verifikasi `Kilowatt Hour {runId}-061` tidak terhapus (tetap ada di tabel)

### TC-GS-UOM-123: Unit menjadi in-use setelah cek awal dilewati saat Confirm

8. Tunggu toast sebelumnya hilang otomatis, klik `(←)` pada kotak Search lalu ketik Search `{runId}-061`, tekan Enter
9. Centang baris `Foot {runId}-061` dan `Inch {runId}-061`
10. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
11. [Admin FAMS, sesi API] Buat Asset Name `Foot Item {runId}-061` dengan Measurement `Foot {runId}-061` hingga tersimpan
12. Klik [Delete] pada dialog Bulk Delete homogen
13. Verifikasi toast: "Success, unit has been deleted. Some items were skipped."
14. Verifikasi `Inch {runId}-061` terhapus
15. Verifikasi `Foot {runId}-061` dilewati dan tetap ada di tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Kelas harness: fungsional (pemicu state oleh Admin FAMS lewat sesi API, bukan konteks kedua). Pembagian TC lintas spec: skenario single dan bulk dengan pemicu di luar sesi aktor berada di spec ini.
- Langkah penghubung: langkah 1 dan 8 (Search baris target; tabel memuat lebih dari satu halaman; langkah 8 sekaligus menunggu toast sebelumnya hilang), langkah 6 (menutup dialog `Cannot Delete Data`).
- Langkah 5 (tidak ada toast sukses) berasal dari Expected b TC-GS-UOM-102 dan didahului dialog `Cannot Delete Data` sebagai anchor positif (butir 11 bagian 8b).
- Alasan spec ini terpisah dari `TC-GS-UOM-E2E-060-konflik-delete-dua-admin`: pelaku pemicu dan dataset berbeda. Pemicu spec ini adalah Admin FAMS (`FA_ADMIN_PASSWORD`) yang membuat Asset Name FAMS sehingga unit menjadi in-use, dengan fixture `assetName.*` dan cleanup Asset Name sebelum unit; spec 060 memakai admin kedua yang menghapus unit lewat sesi API. Gabungan kedua spec 55 langkah (15 + 40), sehingga kegagalan fixture Asset Name FAMS di spec ini tidak ikut menutupi hasil konflik Delete di spec 060. TC-GS-UOM-102 bergantung TC-GS-UOM-50 (pembuatan Kilowatt Hour); seeding lewat API karena pembuatannya bukan objek uji.
- Temuan untuk QA:
  - Akun yang membuat Asset Name di FAMS tidak disebut TC Measurement; spec memakai Admin FAMS Client A yang disediakan tim FE (S-13). Nilai field wajib Asset Name FAMS selain Measurement juga disediakan tim FE.
  - TC-GS-UOM-123 menyebut "Asset Name di-assign Measurement Foot" tanpa menyebut Asset Name yang dipakai; spec membuat `Foot Item {runId}-061`.
  - TC-GS-UOM-102 dan 123 tidak punya Post Condition di luar Expected.
