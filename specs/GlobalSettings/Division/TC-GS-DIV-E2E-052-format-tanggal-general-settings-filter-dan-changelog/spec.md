---
id: TC-GS-DIV-E2E-052-format-tanggal-general-settings-filter-dan-changelog
title: "Format Tanggal General Settings pada Filter Tabel dan Modal Changelog"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-151
  - TC-GS-DIV-212
coverage:
  web: automated
---

# Format Tanggal General Settings pada Filter Tabel dan Modal Changelog

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `Sari Dewi (Sari D)`, `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (tetap di environment, hanya dibaca): Finance (FIN), Human Resources (HR), Legal (LGL), Operations (OPS), Compliance (CMP), Treasury (TRS). Asersi spec ini menyangkut format tanggal, bukan kumpulan nama atau jumlah baris, sehingga Population D-02 tidak di-seed.
- Tanggal pre-setup (`{tanggal pre-setup}`): teks tanggal pada sel Last Updated baris Finance, dibaca di langkah 3 (sesudah Date Format disetel di langkah 1) dan dipakai untuk memilih rentang tanggal pada Filter tabel. Last Updated keenam Division Pre-setup identik dan tidak diubah TC mana pun (Tabel Data Uji Pre-setup TC).
- Rentang tanggal Filter Modal Changelog (langkah 14): hari uji sampai hari uji (tanggal hari ini menurut timezone entitas), yang memuat entri Create dari Division seeding spec ini.
- Data Dinamis milik spec: Division `Format Tanggal {runId}-052` (Code auto-generate, tidak diasersi) dibuat lewat kemampuan seeding Division lewat API di hook `before` oleh akun Total Control (Sari D) agar Riwayat Changelog Division terisi (precondition TC-GS-DIV-212). Hook `after` menghapus Division tersebut lewat API tanpa berasumsi seeding berhasil penuh. Entri Changelog tidak dihapus (immutable).
- State global yang diubah: Date Format dan Time Format General Settings. Nilai awal dibaca di hook `before`; spec menyetel Date Format `DD/MM/YY` dan Time Format 24-jam (langkah 1) sesuai precondition TC; hook `after` memulihkan nilai awal walau spec gagal di tengah. Suite berjalan serial (`parallel: false`) karena state ini dipakai bersama spec lain.
- Kemampuan teknis: membaca dan mengubah Date Format dan Time Format General Settings (disediakan tim FE/BE; TC dan PRD tidak menyebut caranya); memilih rentang tanggal pada date range picker Filter tabel dan Filter Modal Changelog; membaca teks sel Date dan teks input Date filter.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: kembali ke layar Global Settings > User > Division.

## Test Steps

1. Atur General Settings: Date Format `DD/MM/YY` dan Time Format 24-jam
2. Buka layar Global Settings > User > Division
3. Baca teks tanggal pada sel Last Updated baris Finance sebagai `{tanggal pre-setup}`

### TC-GS-DIV-151: Teks tanggal pada input Date filter mengikuti format General Settings

4. Klik icon Filter
5. Pilih rentang tanggal `{tanggal pre-setup}` sampai `{tanggal pre-setup}` pada field `Last Updated`
6. Verifikasi teks nilai tanggal pada input `Last Updated` mengikuti Date Format General Settings (`DD/MM/YY`)
7. Klik `[Clear Field]`
8. Klik `[Apply]`

### TC-GS-DIV-212: Format tanggal Modal Changelog dan input Date filter mengikuti General Settings

9. Klik icon Changelog di Table Tools
10. Verifikasi kolom `Date` menampilkan tanggal dengan format `DD/MM/YY`
11. Verifikasi kolom `Date` menampilkan jam dengan format 24-jam
12. Verifikasi kolom `Date` menampilkan timezone entitas
13. Klik icon Filter pada Modal Changelog
14. Pilih rentang tanggal hari uji sampai hari uji pada field `Date`
15. Verifikasi teks tanggal pada input `Date` filter mengikuti Date Format General Settings (`DD/MM/YY`)
16. Tutup Modal Changelog lewat `[✕]`
17. Pulihkan Date Format dan Time Format General Settings ke nilai awal yang dibaca di hook `before`

## Notes

- Sumber TC: `global-settings/division/TestCases/tc-division.md`. Mode: FE+BE. Kelas harness state global (kelas h, serial).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (151, 212) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (menyetel General Settings sesuai precondition TC), langkah 2 (membuka layar setelah format berlaku), langkah 3 (membaca `{tanggal pre-setup}` setelah format berlaku), langkah 7 dan 8 (mengosongkan Filter tabel yang tidak di-Apply sebelum membuka Changelog), langkah 16 (menutup Modal Changelog), dan langkah 17 (memulihkan General Settings; hook `after` sebagai cadangan).
- Pembagian TC lintas spec: format tanggal pada isi berkas Download (TC-GS-DIV-187) ada di spec 050; TC-GS-DIV-188 dan 224 (Modal Changelog) ada di spec 053.
- Temuan untuk QA:
  - TC-GS-DIV-151 dan 212: kedua TC memakai Date Format `DD/MM/YY` (default) dan Time Format 24-jam sehingga asersi tidak membedakan format default dari format yang disetel; TC tidak menyebut format non-default untuk membuktikan Date Format benar-benar diikuti. Usulan TC: ulangi dengan Date Format non-default.
  - TC-GS-DIV-212 Expected a ("tanggal, jam, timezone entitas"): TC tidak menyebut pola konkret jam dan timezone; spec mengasersi tiap bagian secara terpisah tanpa nilai pola tertentu selain `DD/MM/YY` dan 24-jam.
  - TC-GS-DIV-151: tanggal pre-setup tidak disebut konkret di TC; spec membacanya dari sel Last Updated baris Finance karena keenam Division Pre-setup berbagi tanggal yang sama (Tabel Data Uji Pre-setup TC).
  - TC-GS-DIV-212: mekanisme mengubah General Settings dan Time Format tidak didefinisikan di TC, PRD, atau LLD; disediakan tim FE/BE.
