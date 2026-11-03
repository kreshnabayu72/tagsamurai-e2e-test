---
id: TC-FA-TAG-E2E-160-cancel-report-tag-submit-berhasil-keep-report-dan-modul-borrow-bagian-2
title: "Cancel Report TAG: Keep Report, Konflik Pengguna Lain, dan Dialog Borrow (Bagian 2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-667
  - TC-FA-TAG-670
  - TC-FA-TAG-1440
  - TC-FA-TAG-1458
  - TC-FA-TAG-1471
coverage:
  web: automated
---

# Cancel Report TAG: Keep Report, Konflik Pengguna Lain, dan Dialog Borrow (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor:

| Kode | Role (teks `Role:` TC) | Email | Env password |
|---|---|---|---|
| SA_NOTAG | Staff Auditor (tidak memegang Manage asset & TAG) | `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD` |
| ABR | Administrator Borrow dengan hak aksi Cancel Report | `administratorBorrowDenganHakAksiCancelReport_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_ABR_PASSWORD` |

- Akun aktor pertama: Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG]. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Aksi spec ini dijalankan dari modul Audit, sehingga langkah pertama berpindah ke modul Audit. Langkah ganti akun ditulis eksplisit (Logout lalu Login). Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Sesi API aktor: pelaku kedua memakai login API (password) yang tidak dihitung sebagai sesi web (lihat `suite.md`), tanpa asersi di sesinya; akun Staff Auditor kedua disediakan tim FE (akun pelaku tidak tertulis di Pre-setup TC).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, task Existence Audit, serta laporan Tag (laporan terbuka Damaged, Missing, atau Unreadable dan pembatalan laporan); tidak ada endpoint yang dikarang di spec ini.
- Kemampuan teknis (disediakan tim FE/BE): transaksi Borrow milik spec dengan aset AST-0020 berstatus TAG Issue (seed lewat fixture backend).
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Task Existence Audit | Task milik spec berstatus In Audit dengan item AST-0020 dan AST-0044 | `taskExistenceAudit` |
| Aset 'Excavator 20 Ton - 20' dengan laporan | AST-0020, Group Plant B; Tag tunggal RFID `RF-00130` punya laporan terbuka Damaged dari Staff Auditor | `aset20Laporan` |
| Aset 'Excavator 20 Ton - 44' dengan laporan | AST-0044, Group Plant B; Tag RFID `RF-00132` laporan terbuka Missing dan Tag QR `QR-00232` laporan terbuka Unreadable | `aset44Laporan` |
| Transaksi Borrow | Transaksi milik spec dengan aset AST-0020 berstatus TAG Issue dan Tag `RF-00130` laporan terbuka Damaged | `borrowAst20TagIssue` |

- State yang diubah dan pemulihannya: laporan yang dibatalkan pelaku kedua, laporan yang diatur ulang, dan transaksi Borrow dipulihkan lewat fixture backend di hook `after`; spec selesai di akun ABR dan hook `after` mengembalikan sesi ke akun default suite (Total Control).

## Test Steps

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit

### Klik backdrop (TC-FA-TAG-1440)

2. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 20
3. Klik area backdrop di luar dialog
4. Verifikasi dialog "Cancel Report" tetap terbuka

### Keep Report pada dialog terisi (TC-FA-TAG-667)

5. Isi Textarea "Reason" dengan "Tag ternyata terbaca"
6. Klik tombol [Keep Report]
7. Verifikasi dialog "Cancel Report" menutup langsung
8. Verifikasi dialog "Unsaved Changes" tidak tampil walau Textarea "Reason" sudah terisi

### Laporan sudah dibatalkan pengguna lain (TC-FA-TAG-1458)

9. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 20
10. Isi Textarea "Reason" dengan "Salah laporan"
11. Pelaku kedua lewat sesi API melakukan Cancel Report TAG pada RF-00130 dengan Reason "Laporan ganda" hingga pembatalan laporan tersimpan
12. Klik tombol [Cancel Report]
13. Verifikasi toast "Error, failed to cancel report." tampil untuk pengguna A
14. Verifikasi dialog "Cancel Report" pengguna A tetap terbuka
15. Klik ikon close pada header dialog "Cancel Report"
16. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
17. Klik [Leave]

### Dua Tag ketika laporan salah satu Tag sudah dibatalkan pengguna lain (TC-FA-TAG-1471)

18. Atur ulang data lewat fixture backend: Tag RF-00132 laporan terbuka Missing dan Tag QR-00232 laporan terbuka Unreadable hingga tersimpan, lalu muat ulang halaman Task Detail
19. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 44
20. Centang kedua Tag pada bagian "TAG to cancel"
21. Isi Textarea "Reason" dengan "Salah laporan"
22. Pelaku kedua lewat sesi API melakukan Cancel Report TAG pada RF-00132 saja dengan Reason "Laporan ganda" hingga pembatalan laporan tersimpan
23. Klik tombol [Cancel Report]
24. Verifikasi toast "Error, failed to cancel report." tampil untuk pengguna A
25. Verifikasi dialog "Cancel Report" pengguna A tetap terbuka
26. Verifikasi (baca lewat fixture backend) laporan QR-00232 tidak ditutup oleh Submit pengguna A (semua-atau-tidak)
27. Klik ikon close pada header dialog "Cancel Report"
28. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
29. Klik [Leave]

### Cancel Report lewat dialog milik Borrow (TC-FA-TAG-670)

30. Atur ulang data lewat fixture backend: transaksi Borrow aset AST-0020 berstatus TAG Issue dan Tag RF-00130 laporan terbuka Damaged hingga tersimpan
31. Ganti akun: logout dari akun Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG], login dengan akun Administrator Borrow dengan hak aksi Cancel Report [ABR], lalu buka modul Borrow dan transaksi aset Excavator 20 Ton - 20
32. Pilih aksi "Cancel Report"
33. Verifikasi dialog yang tampil adalah dialog Cancel Report milik Borrow (bukan Dialog "Cancel Report" modul TAG)
34. Isi alasan pembatalan pada dialog Borrow
35. Klik tombol [Cancel Report] pada dialog Borrow

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-667, 670, 1440, 1458, 1471). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: Cancel Report TAG yang berhasil dan laporan ulang ada di spec 159. Report TAG konflik dua Tag (TC-FA-TAG-1472) ada di spec 168.
- Pengecualian pelaku kedua: pelaku kedua memakai sesi API; bukan konteks kedua kelas c dan tidak memakai `P-2`; langkah pemicunya ditulis "... hingga ... tersimpan" (langkah 11 dan 22). Hasil di sesi pelaku kedua tidak diasersi.
- Urutan TC di dalam spec: TC-1440, TC-667, TC-1458, TC-1471, TC-670. TC-670 terakhir karena menutup dengan ganti akun ke ABR; seluruh TC akun Staff Auditor berurutan sebelum ganti akun. TC-1440 dan TC-667 memakai dialog yang sama (aset dan state identik).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 15 sampai 17 dan 27 sampai 29 (menutup form dirty), 18 dan 30 (mengatur ulang state laporan dan transaksi lewat fixture backend), serta 31 (ganti akun eksplisit).
- Temuan untuk QA:
  - Hook suite `beforeEach` membuka Fixed Asset > TAG untuk akun aktor pertama, sedangkan Staff Auditor tanpa Manage asset & TAG tidak berhak atas halaman itu; hook perlu dikecualikan untuk spec ini di tahap script.
  - TC-FA-TAG-670 menulis "Isi alasan pembatalan" tanpa nilai di kolom Data Uji dan tanpa teks dialog Borrow; spec memakai kalimat langkah apa adanya dan nilai alasan ditentukan tahap script.
  - Post Condition TC-FA-TAG-1440, 1458, 1471, dan 670 (laporan tetap terbuka atau Canceled, Changelog satu entri, status Tag Reported dicabut) tanpa langkah observasi di TC tidak diasersi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
