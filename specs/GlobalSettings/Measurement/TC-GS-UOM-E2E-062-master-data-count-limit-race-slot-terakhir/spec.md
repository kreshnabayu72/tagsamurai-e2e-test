---
id: TC-GS-UOM-E2E-062-master-data-count-limit-race-slot-terakhir
title: "Master Data Count Limit: Dua Admin Rebutan Slot Terakhir"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UOM-247
coverage:
  web: automated
---

# Master Data Count Limit: Dua Admin Rebutan Slot Terakhir

## Prerequisites

- Mode: FE+BE. Spec membuat race antar-sesi (kelas multi-konteks) di atas tenant Client Limit; kuota Master Data Count Limit menjadi pemicu state, bukan kelas volume data (P-2, keputusan 2026-10-21).
- Akun admin pertama: Total Control Client Limit, Wulan Sari (`Wulan S`), `totalControl_automated_qaTeam4@qwertysystem.net`, kredensial `Spectra.env.GS_LIMIT_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Measurement dilakukan sekali di hook `before` spec ini.
- Akun admin kedua: Total Control Client Limit kedua, `totalControlSecond_automated_qaTeam4@qwertysystem.net`, kredensial `Spectra.env.GS_LIMIT_TC2_PASSWORD`. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); fixture baru disediakan tim FE. Hook `before` membuka sesi browser kedua (konteks terpisah), login dengan akun ini, dan membuka Global Settings > Master Reference > Measurement.
- Environment variable: `GS_LIMIT_TC_PASSWORD`, `GS_LIMIT_TC2_PASSWORD`, dan `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip halaman Measurement: disetel `seen` oleh hook suite untuk setiap akun aktor, yaitu Total Control Client Limit dan Total Control Client Limit kedua (lihat `suite.md`, bagian Hook suite).
- Pemulihan sesi: hook `after` menutup sesi browser kedua dan mengembalikan sesi ke akun default suite (Total Control Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`).
- Fixture Client Limit yang disediakan tim FE: Master Data Count Limit 1.000 dan Selection Limit 100 (nilai minimum); 999 unit `Lim 001` sampai `Lim 999` (D-28, lewat Import Type Measurement). Hook `before` memastikan jumlah unit 999 dan limit 1.000, lalu men-seed lewat API satu unit `Slot {runId}-062` / `sl` (milik spec) sehingga tabel berisi 1.000 unit sebelum langkah 1 (precondition TC).
- Data dinamis (suffix per run dan nomor spec): `Race A {runId}-062` / `ra` dan `Race B {runId}-062` / `rb` (dibuat satu di antaranya oleh spec lewat UI); `Slot {runId}-062` dihapus spec lewat UI pada langkah 1 sebagai pengganti `Lim 998` (S-06).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Race A {runId}-062`, `Race B {runId}-062`, dan `Slot {runId}-062` bila ada, sehingga jumlah unit kembali 999 (state awal Client Limit).
- State global bersama: tenant Client Limit dipakai spec lain dengan jumlah unit sebagai syarat; suite berjalan serial (`parallel: false`).
- Kemampuan teknis: dua sesi browser paralel dan pemicu klik [Submit] hampir bersamaan di kedua sesi.
- TC-GS-UOM-247: Master Data Count Limit 1.000, tabel berisi 1.000 unit sebelum langkah 1; admin kedua siap.

## Test Steps

### TC-GS-UOM-247: Dua admin membuat unit pada slot terakhir ceiling

1. [Admin pertama] Ketik Search `Slot {runId}-062`, tekan Enter, klik `⋯` pada baris tersebut > Delete, klik [Delete] pada dialog
2. [Admin pertama] Tunggu aksi selesai (toast sukses tampil)
3. [Admin pertama] Klik [+ Unit], isi Unit Name `Race A {runId}-062` dan Symbol `ra`
4. [Admin kedua] Klik [+ Unit], isi Unit Name `Race B {runId}-062` dan Symbol `rb`
5. Klik [Submit] di kedua sesi hampir bersamaan
6. Verifikasi salah satu admin mendapat toast sukses: "Success, unit has been created."
7. Verifikasi admin lainnya mendapat dialog `Cannot Add Unit`
8. Di sesi admin yang mendapat dialog `Cannot Add Unit`: klik [OK]
9. Di sesi admin yang mendapat dialog `Cannot Add Unit`: klik `✕` pada form Create
10. Di sesi admin yang mendapat dialog `Cannot Add Unit`: Verifikasi dialog `Unsaved Changes` tampil dengan tombol `[Cancel]` dan `[Leave]`
11. Di sesi admin yang mendapat dialog `Cannot Add Unit`: klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`. Kelas harness: multi-konteks (race dua sesi) dengan kuota Master Data Count Limit sebagai pemicu state (P-2, keputusan 2026-10-21); spec tidak dipindah ke kelas volume data.
- Langkah penghubung: langkah 2 (menunggu Delete selesai; langkah 1 adalah Langkah Uji TC), langkah 8 sampai 11 (menutup dialog dan form Create dirty sesi yang kalah lewat `✕`, dialog `Unsaved Changes`, dan `[Leave]` sebagai pembersihan state; S-08). Tombol penutup dialog `Cannot Add Unit` tidak disebut Langkah Uji TC-GS-UOM-247; langkah 8 memakai `[OK]` sesuai TC-GS-UOM-64 (Esc tidak menutup dialog, `[OK]` menutup) dan spec 022.
- Pemenang race tidak deterministik, sehingga langkah 7 sampai 11 merujuk "admin yang mendapat dialog `Cannot Add Unit`" sesuai hasil langkah 6 dan 7.
- Langkah 1 memakai unit milik spec `Slot {runId}-062` sebagai pengganti `Lim 998` (D-28) agar baris Pre-setup Client Limit tidak berubah (S-06).
- Pembagian TC lintas spec: TC-GS-UOM-63 sampai 66 (Create di batas dan dialog `Cannot Add Unit`) ada di spec 022.
- Temuan untuk QA:
  - Precondition TC-GS-UOM-247 menyebut tabel berisi 1.000 unit, sedangkan Pre-setup menyebut Client Limit berisi 999 unit `Lim 001` sampai `Lim 999` (D-28); unit ke-1.000 tidak didefinisikan. Spec men-seed `Slot {runId}-062` sebagai unit ke-1.000.
  - Akun admin kedua Client Limit tidak ada di Pre-setup TC; spec memakai fixture baru yang disediakan tim FE (S-13).
  - TC-GS-UOM-247 tidak menyebut teks toast sukses; spec memakai toast Create standar `Success, unit has been created.` dari TC-GS-UOM-36. Post Condition TC tidak ada.
