---
id: TC-FA-TAG-E2E-158-cancel-report-tag-screening-dan-validasi
title: "Cancel Report TAG: Screening Dialog dan Validasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-658
  - TC-FA-TAG-659
  - TC-FA-TAG-660
  - TC-FA-TAG-661
  - TC-FA-TAG-1486
coverage:
  web: automated
---

# Cancel Report TAG: Screening Dialog dan Validasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor:

| Kode | Role (teks `Role:` TC) | Email | Env password |
|---|---|---|---|
| SA_NOTAG | Staff Auditor (tidak memegang Manage asset & TAG) | `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD` |

- Akun aktor pertama: Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG]. Login di hook `before` spec ini; halaman dibuka di langkah pertama (hook suite `beforeEach` dikecualikan, lihat `suite.md`). Aksi spec ini dijalankan dari modul Audit, sehingga langkah pertama berpindah ke modul Audit. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, task Existence Audit, serta laporan Tag (laporan terbuka Damaged, Missing, atau Unreadable dan pembatalan laporan); tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Task Existence Audit | Task milik spec berstatus In Audit dengan item AST-0020 dan AST-0044 | `taskExistenceAudit` |
| Aset 'Excavator 20 Ton - 20' dengan laporan | AST-0020, Group Plant B; Tag tunggal RFID `RF-00130` punya laporan terbuka Damaged dari Staff Auditor | `aset20Laporan` |
| Aset 'Excavator 20 Ton - 44' dengan laporan | AST-0044, Group Plant B; Tag RFID `RF-00132` laporan terbuka Missing dan Tag QR `QR-00232` laporan terbuka Unreadable | `aset44Laporan` |
| Aset 'Excavator 20 Ton - 44' dengan dua Tag RFID | AST-0044, Group Plant B; dua Tag RFID Paired `RF-00132` (laporan terbuka Missing) dan `RF-00133` (laporan terbuka Damaged) | `aset44DuaRfid` |

- State yang diubah dan pemulihannya: laporan yang diatur ulang pada langkah 26 dipulihkan lewat fixture backend di hook `after`; tidak ada laporan yang dibatalkan oleh spec ini.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 11, 20 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log. Fixture backend (langkah 26) hanya menyiapkan atau memulihkan state.

## Test Steps

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit

### Screening dialog pada aset satu Tag berlaporan (TC-FA-TAG-658)

2. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 20
3. Verifikasi dialog "Cancel Report" (Size MD) terbuka
4. Verifikasi Summary menampilkan "AST-0020 — Excavator 20 Ton"
5. Verifikasi bagian "TAG to cancel" bertanda wajib (*) menampilkan satu opsi tanpa checkbox
6. Verifikasi opsi pada bagian "TAG to cancel" otomatis terpilih
7. Verifikasi opsi berlabel tipe Tag "RFID" dan Report Type "Damaged"
8. Verifikasi Textarea "Reason" bertanda wajib (*) kosong
9. Verifikasi footer berisi tombol [Keep Report] dan [Cancel Report]
10. Verifikasi tombol [Cancel Report] bergaya Danger

### Submit tanpa Reason (TC-FA-TAG-660)

11. Klik tombol [Cancel Report] dengan Textarea "Reason" dibiarkan kosong
12. Verifikasi pesan error "Reason must not be empty" tampil pada Textarea "Reason"
13. Verifikasi dialog "Cancel Report" tetap terbuka
14. Klik tombol [Keep Report]

### Screening dialog pada aset dua Tag berlaporan (TC-FA-TAG-659)

15. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 44
16. Verifikasi bagian "TAG to cancel" menampilkan dua checkbox tersusun mendatar
17. Verifikasi tiap opsi berlabel tipe Tag dan Report Type-nya (RFID dengan Missing, QR dengan Unreadable)
18. Verifikasi kedua checkbox belum tercentang

### Submit multi-Tag tanpa mencentang Tag (TC-FA-TAG-661)

19. Isi Textarea "Reason" dengan "Tag ternyata terbaca"
20. Klik tombol [Cancel Report]
21. Verifikasi pesan error "TAG must not be empty" tampil pada bagian "TAG to cancel"
22. Verifikasi dialog "Cancel Report" tetap terbuka
23. Klik ikon close pada header dialog "Cancel Report"
24. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
25. Klik [Leave]

### Label opsi pada aset dengan dua Tag bertipe sama (TC-FA-TAG-1486)

26. Atur ulang data lewat fixture backend: Aset AST-0044 dengan dua Tag RFID Paired, RF-00132 laporan terbuka Missing dan RF-00133 laporan terbuka Damaged, hingga tersimpan, lalu muat ulang halaman Task Detail
27. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 44
28. Verifikasi bagian "TAG to cancel" menampilkan dua checkbox tersusun mendatar
29. Verifikasi label tiap opsi memuat tipe Tag RFID, TAG Code (`RF-00132` dan `RF-00133`), dan Report Type-nya (Missing dan Damaged) sehingga kedua opsi dapat dibedakan
30. Verifikasi kedua checkbox belum tercentang
31. Klik tombol [Keep Report]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-658 s.d. 661, 1486). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: Cancel Report TAG yang berhasil ada di spec 159 dan spec 160.
- Urutan TC di dalam spec: TC-658, TC-660, TC-659, TC-661, TC-1486. TC-660 melanjutkan dialog TC-658 (aset dan state identik) dan TC-661 melanjutkan dialog TC-659; TC-1486 terakhir karena membutuhkan state laporan berbeda pada AST-0044.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 14 dan 31 (menutup dialog yang belum diisi dengan [Keep Report]), 23 sampai 25 (menutup form dirty: ikon close, `Verifikasi` dialog "Unsaved Changes", [Leave]), dan 26 (mengatur ulang state laporan lewat fixture backend).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 11, 20 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log. Fixture backend (langkah 26) hanya menyiapkan atau memulihkan state.
- Temuan untuk QA:
  - Hook suite `beforeEach` membuka Fixed Asset > TAG untuk akun aktor pertama, sedangkan Staff Auditor tanpa Manage asset & TAG tidak berhak atas halaman itu; spec ini dikecualikan di `suite.md` bagian Hook sehingga halaman yang diuji dibuka di langkahnya sendiri.
  - Post Condition TC-FA-TAG-660 dan TC-FA-TAG-661 ("Laporan ... tetap terbuka") tanpa langkah observasi di TC tidak diasersi.
  - TC-FA-TAG-1486 menulis kondisi dua Tag RFID pada AST-0044 yang berbeda dengan precondition TC-FA-TAG-659 (RFID dan QR); spec menyiapkan state masing-masing lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
