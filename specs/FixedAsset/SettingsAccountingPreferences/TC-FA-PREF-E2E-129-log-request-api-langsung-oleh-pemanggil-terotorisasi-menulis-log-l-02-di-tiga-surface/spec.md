---
id: TC-FA-PREF-E2E-129-log-request-api-langsung-oleh-pemanggil-terotorisasi-menulis-log-l-02-di-tiga-surface
title: "Log: Request API Langsung oleh Pemanggil Terotorisasi Menulis Log L-02 di Tiga Surface"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-PREF-549
sourceRules: ["J-03", "S-01e", "L-02f", "SET-03", "§4.1.4#r7", "S-01f", "L-02b", "§8.2#p1", "S-01g", "L-02c", "L-02d"]
smoke: []
dependsOn: []
trace:
  "J-03": 3
  "S-01e": 7
  "L-02f": 8
  "SET-03": [8, 12]
  "§4.1.4#r7": 8
  "S-01f": 11
  "L-02b": 12
  "§8.2#p1": 13
  "S-01g": 15
  "L-02c": 16
  "L-02d": 16
coverage:
  web: automated
---

# Log: Request API Langsung oleh Pemanggil Terotorisasi Menulis Log L-02 di Tiga Surface

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Rina Anggraini, tampil "Rina A"; PC-8) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email Rina Anggraini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); kesamaannya dengan akun Total Control suite perlu dikonfirmasi tim FE.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture. Nama diusulkan mengikuti `<APP>_<ROLE>_PASSWORD` (perlu dikonfirmasi tim FE).
- Data: company `PT Contoh Konstruksi` (plan Growth, entitas Active) seri PC (PC-1): modul akuntansi aktif; Preferences bernilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset, dan Found Asset Credit Account kosong, Disposal Documents Sell/Scrap/Lost/Donate/Trade-in/Write-off Optional, Journal Grouping Group); bulan berjalan Oktober 2026. In-service Date Source tersimpan Activation date. Payload: In-service Date Source = Manual by Accounting.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): request langsung Save Preferences memakai sesi API Total Control Rina Anggraini (butir "Sesi API aktor" di `suite.md`). Seed dan pemulihan lewat API (Preferences ke nilai awal PC-1, Asset Class, akun Chart of Accounts, pelepasan, kunci periode, status company) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`). Pembacaan jumlah baris Changelog Preferences, System Log milik pelaku, dan Activity Log FAMS sebelum aksi lewat kemampuan baca BE (disediakan tim FE/BE; 8b.10, S-12). Jam server dan jam browser sinkron untuk asersi "Date = waktu Save" dengan toleransi satu menit (S-12).
- State yang diubah spec: Preferences company dan entri log (audit trail permanen, tidak dihapus). Preferences dipulihkan ke nilai awal PC-1 lewat seed di antara TC dan di hook `after` (hook tetap jalan bila spec gagal di tengah).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk setiap akun aktor yang dipakai dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-549: Request API langsung oleh pemanggil terotorisasi menulis log L-02 di tiga surface

1. Catat jumlah baris awal Changelog Preferences (N_cl), System Log milik Rina Anggraini (N_sl), dan Activity Log FAMS (N_al) lewat kemampuan baca BE
2. Kirim request langsung Save Preferences menggunakan sesi API Rina Anggraini, mengubah In-service Date Source menjadi Manual by Accounting hingga tersimpan
3. Verifikasi permintaan berhasil (respons server sukses)
4. Catat waktu Save (jam server dan jam browser sinkron)
5. Buka Settings > Accounting > Preferences
6. Klik ikon View history di header tab untuk membuka modal Changelog: Preferences
7. Verifikasi jumlah baris modal Changelog: Preferences bertambah tepat 1 dari N_cl
8. Verifikasi baris baru di posisi teratas modal Changelog: Preferences: Date = waktu Save (toleransi satu menit), Action = Edit, Section = Capitalization, Field = In-service Date Source, Old Value = Activation date, New Value = Manual by Accounting, Modified By = Rina A
9. Tutup modal Changelog
10. Buka Global Settings > User > Detail > Tab System Log milik Rina Anggraini
11. Verifikasi jumlah baris System Log bertambah tepat 1 dari N_sl
12. Verifikasi baris baru di posisi teratas System Log: Action = Edit, Object = Preferences, Name = —, Field = In-service Date Source, Old Value = Activation date, New Value = Manual by Accounting
13. Verifikasi header tabel System Log tidak memuat kolom Modified By
14. Buka Activity Log FAMS
15. Verifikasi jumlah baris Activity Log FAMS bertambah tepat 1 dari N_al
16. Verifikasi baris baru di posisi teratas Activity Log FAMS: Action = Edit, Object = Preferences, Name = —, Field = In-service Date Source, Old Value = Activation date, New Value = Manual by Accounting, Modified By = Rina A
17. Pulihkan Preferences company ke nilai awal PC-1 lewat seed hingga tersimpan

## Notes

- Kelas fungsional: tiap TC menyimpan Preferences lewat UI lalu membaca tiga surface log. Asersi "tepat N baris baru" adalah asersi jumlah terhadap baseline (bukan absence kelas g); S-05 tidak berlaku.
- Langkah penghubung tanpa `Verifikasi` (S-03): langkah 1, 4, 9, 17 (pencatatan baseline, pencatatan waktu Save, menutup modal Changelog, pemulihan Preferences antar-TC lewat seed). Baseline dicatat ulang sebelum pemicu tiap TC (S-12).
- Urutan baca log: jumlah baris dibuktikan bertambah dari baseline lebih dulu, baru baris teratas dibaca (S-14). Jumlah langkah nominal 17; blok baca-log berpola (buka surface, `Verifikasi` jumlah, `Verifikasi` kolom log) pada langkah 6 sampai 16 tidak dihitung ke ambang ~35 langkah (bagian 3 prinsip 13, smell). Seluruh TC berkelas sama (fungsional Save lalu log tiga surface) dan tiap blok berdiri sendiri dengan pemulihan seed di antaranya.
- P-2 (pemicu bukan objek uji): request langsung (langkah 2) hanya membentuk state Preferences dan log yang dibaca lewat UI; asersi pada request itu sendiri hanya respons sukses (langkah 3), tanpa asersi tampilan FE atas request tersebut (8b butir 1). K-1 tidak dipakai: Expected TC memuat state log, bukan respons API sebagai objek uji pertahanan.
- Pemakai sesi API adalah akun aktor itu sendiri, bukan pelaku kedua; baris rujukan suite.md "Sesi API aktor" berlaku.
- Temuan untuk QA:
  - Email Rina Anggraini (Total Control, PC-8) tidak tertulis di Pre-setup TC (kolom Kondisi "Email diatur pemilik"); spec memakai pola email akun Total Control suite dan meminta konfirmasi tim FE (S-11, S-13).
  - Expected TC menyebut baris log baru sebagai "tepat N baris baru" tanpa menyebut baseline; spec mencatat baseline jumlah baris tiap surface sebelum aksi lewat kemampuan baca BE dan mengasersi selisih (S-12, S-14).
  - Post Condition TC 549 tidak punya langkah observasi sendiri di TC; padanannya ada pada Expected yang diasersi (S-01). Post Condition "Nilai terbaru dibaca oleh ... (belum disusun)" tidak diasersi karena modul konsumen belum disusun.
  - Tipe TC-FA-PREF-549 adalah Security, sehingga caseType dipetakan Negative menurut bagian 8; alur TC sendiri adalah request sukses dengan log tercatat.
