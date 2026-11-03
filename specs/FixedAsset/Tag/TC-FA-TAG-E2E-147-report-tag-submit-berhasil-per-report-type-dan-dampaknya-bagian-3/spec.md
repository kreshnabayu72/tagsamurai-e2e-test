---
id: TC-FA-TAG-E2E-147-report-tag-submit-berhasil-per-report-type-dan-dampaknya-bagian-3
title: "Report TAG: Laporan Konflik, Dialog dari Modul Borrow, dan Changelog (Bagian 3)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-618
  - TC-FA-TAG-620
  - TC-FA-TAG-621
  - TC-FA-TAG-1377
  - TC-FA-TAG-1459
coverage:
  web: automated
---

# Report TAG: Laporan Konflik, Dialog dari Modul Borrow, dan Changelog (Bagian 3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor:

| Kode | Role (teks `Role:` TC) | Email | Env password |
|---|---|---|---|
| SA_NOTAG | Staff Auditor (tidak memegang Manage asset & TAG) | `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD` |
| TC | Total Control | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Akun aktor pertama: Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG]. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Aksi spec ini dijalankan dari modul Audit, sehingga langkah pertama berpindah ke modul Audit. Langkah ganti akun ditulis eksplisit (Logout lalu Login). Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Sesi API aktor: pelaku kedua memakai login API (password) yang tidak dihitung sebagai sesi web (lihat `suite.md`), tanpa asersi di sesinya; akun Staff Auditor kedua disediakan tim FE (akun pelaku tidak tertulis di Pre-setup TC).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, task Existence Audit, serta laporan Tag (laporan terbuka Damaged, Missing, atau Unreadable dan pembatalan laporan); tidak ada endpoint yang dikarang di spec ini.
- Kemampuan teknis (disediakan tim FE/BE): transaksi Borrow milik spec dengan aset AST-0020 berstatus Borrowed (seed lewat fixture backend); pembacaan jumlah entri Changelog Paired TAG sebelum aksi (baseline, karena Changelog adalah audit trail permanen).
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Task Existence Audit | Task milik spec berstatus In Audit dengan item AST-0020 dan AST-0044 | `taskExistenceAudit` |
| Aset 'Excavator 20 Ton - 20' | AST-0020, Group Plant B, status Assigned; Tag tunggal RFID `RF-00130` Paired | `aset20` |
| Transaksi Borrow | Transaksi milik spec dengan aset AST-0020 berstatus Borrowed | `borrowAst20` |
| Laporan oleh pelaku kedua | Laporan Missing dengan Note "Hilang" pada `RF-00130` | `laporan130MissingB` |

- State yang diubah dan pemulihannya: laporan terbuka pada `RF-00130` (dibuat pelaku kedua, hasil seeding, dan hasil submit langkah 23 sampai 28) dibatalkan dan data dipulihkan lewat fixture backend di hook `after`; spec selesai di akun Total Control (akun default suite).

## Test Steps

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit

### Tag dilaporkan pengguna lain saat dialog terbuka (TC-FA-TAG-618)

2. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
3. Pilih Report Type "Damaged"
4. Isi Textarea "Note" dengan "Label retak"
5. Pelaku kedua lewat sesi API melaporkan RF-00130 sebagai "Missing" dengan Note "Hilang" hingga laporan tersimpan
6. Klik [Submit]
7. Verifikasi toast "Error, failed to report TAG." tampil untuk pengguna A
8. Klik ikon close pada header dialog "Report TAG"
9. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
10. Klik [Leave]

### Dialog Report TAG dari modul Borrow (TC-FA-TAG-620)

11. Atur ulang data lewat fixture backend: Tag RF-00130 tanpa laporan terbuka hingga tersimpan
12. Buka modul Borrow dan buka transaksi aset Excavator 20 Ton - 20
13. Pilih row action "Report TAG"
14. Verifikasi dialog "Report TAG" terbuka dengan Checkbox "TAG to report", Radio "Report Type", Textarea "Note", dan footer [Cancel] [Submit]
15. Klik [Cancel] pada dialog "Report TAG"

### Aksi Report TAG di Borrow Hidden (TC-FA-TAG-621)

16. Atur ulang data lewat fixture backend: Tag RF-00130 punya laporan terbuka Damaged hingga tersimpan, lalu muat ulang halaman transaksi Borrow
17. Buka menu aksi baris transaksi aset Excavator 20 Ton - 20
18. Verifikasi aksi "Report TAG" Hidden

### Aksi Report TAG di Audit Hidden (TC-FA-TAG-1377)

19. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
20. Buka menu aksi baris Excavator 20 Ton - 20
21. Verifikasi aksi "Report TAG" Hidden karena satu-satunya Tag aset sudah punya laporan terbuka

### Note Report TAG tidak masuk Changelog (TC-FA-TAG-1459)

22. Atur ulang data lewat fixture backend: Tag RF-00130 tanpa laporan terbuka hingga tersimpan, lalu muat ulang halaman Task Detail
23. Catat jumlah entri Report TAG untuk Excavator 20 Ton - 20 pada Changelog Paired TAG sebagai baseline (kemampuan baca lewat fixture backend)
24. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
25. Pilih Report Type "Damaged"
26. Isi Textarea "Note" dengan "Label retak"
27. Klik [Submit]
28. Tunggu aksi selesai (dialog "Report TAG" tertutup dan tombol aktif kembali)
29. Ganti akun: logout dari akun Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG], login dengan akun Total Control [TC], lalu buka Fixed Asset > TAG tab Paired
30. Klik tombol "Changelog"
31. Verifikasi modal "Changelog: Paired TAG" memuat satu entri Report TAG baru (selisih +1 dari baseline) untuk Excavator 20 Ton - 20 dengan Field "Report Type" dan New Value "Damaged"
32. Verifikasi tabel modal tidak memiliki kolom Note
33. Verifikasi teks "Label retak" tidak tampil pada baris entri mana pun

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-618, 620, 621, 1377, 1459). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: konflik dua pengguna pada dua Tag (TC-FA-TAG-1472) ada di spec 168. Dampak Report TAG lain ada di spec 145 dan 146.
- Pengecualian pengguna kedua (TC-FA-TAG-618): pelaku kedua memakai sesi API; bukan konteks kedua kelas c dan tidak memakai `P-2`; langkah pemicunya ditulis "... hingga ... tersimpan" (langkah 5).
- Urutan TC di dalam spec: TC-618, TC-620, TC-621, TC-1377, TC-1459. TC-1459 diletakkan terakhir karena menutup dengan ganti akun ke Total Control; seluruh TC akun Staff Auditor berurutan sebelum ganti akun.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 8 sampai 10 (menutup form dirty), 11, 16, dan 22 (mengatur ulang state laporan `RF-00130` lewat fixture backend; muat ulang halaman juga menghilangkan toast sebelumnya), 12 dan 19 (membuka modul tujuan), 15 (menutup dialog yang belum diisi), 23 (baseline Changelog), 28 (menunggu aksi selesai), dan 29 (ganti akun eksplisit).
- Temuan untuk QA:
  - Hook suite `beforeEach` membuka Fixed Asset > TAG untuk akun aktor pertama, sedangkan Staff Auditor tanpa Manage asset & TAG tidak berhak atas halaman itu; hook perlu dikecualikan untuk spec ini di tahap script.
  - TC tidak menyatakan apakah satu-satunya Tag yang terpilih otomatis membuat dialog dianggap terisi saat ditutup; spec menutup dialog yang belum diisi pengguna dengan [Cancel] atau [Keep Report] tanpa dialog Unsaved Changes, mengikuti TC-FA-TAG-666 dan TC-FA-TAG-675.
  - TC-FA-TAG-618 menulis dua pengguna tanpa menyebut akun pengguna B selain "akses Report TAG di modul Audit"; spec menulisnya sebagai akun kedua yang disediakan tim FE lewat sesi API.
  - TC-FA-TAG-620 dan TC-FA-TAG-621 tidak menyebut halaman asal row action "Report TAG" di Borrow selain "transaksi aset"; spec membukanya dari transaksi aset yang dibuka.
  - Post Condition TC-FA-TAG-618 ("RF-00130 hanya punya satu laporan terbuka") tanpa langkah observasi di TC tidak diasersi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
