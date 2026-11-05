---
id: TC-FA-TAG-E2E-144-report-tag-validasi-submit-report-type-note-dan-tag
title: "Report TAG: Validasi Submit Report Type, Note, dan Tag"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-605
  - TC-FA-TAG-606
  - TC-FA-TAG-607
  - TC-FA-TAG-608
coverage:
  web: automated
---

# Report TAG: Validasi Submit Report Type, Note, dan Tag

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
| Aset 'Excavator 20 Ton - 20' | AST-0020, Group Plant B, status Assigned; Tag tunggal RFID `RF-00130` Paired | `aset20` |
| Aset 'Excavator 20 Ton - 44' | AST-0044, Group Plant B; Tag RFID `RF-00132` dan Tag QR `QR-00232` keduanya Paired | `aset44` |

- State yang diubah dan pemulihannya: tidak ada laporan yang dibuat spec ini (seluruh submit ditolak); data dipulihkan lewat fixture backend di hook `after`.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 3, 10, 16, 25 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log.

## Test Steps

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit

### Submit dialog kosong pada aset satu Tag (TC-FA-TAG-608)

2. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
3. Klik [Submit] tanpa mengisi apa pun
4. Verifikasi pesan error "Report type must not be empty" tampil
5. Verifikasi pesan error "Note must not be empty" tampil
6. Verifikasi tidak ada pesan "TAG must not be empty" karena Tag tunggal otomatis terpilih
7. Klik [Cancel] pada dialog "Report TAG"

### Submit tanpa Report Type (TC-FA-TAG-605)

8. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
9. Isi Textarea "Note" dengan "Label retak"
10. Klik [Submit]
11. Verifikasi pesan error "Report type must not be empty" tampil pada Radio "Report Type"
12. Verifikasi dialog "Report TAG" tetap terbuka
13. Verifikasi tidak ada toast sukses

### Submit tanpa Note (TC-FA-TAG-606)

14. Pilih Report Type "Damaged"
15. Kosongkan Textarea "Note"
16. Klik [Submit]
17. Verifikasi pesan error "Note must not be empty" tampil pada Textarea "Note"
18. Verifikasi dialog "Report TAG" tetap terbuka

### Submit pada aset dua Tag tanpa mencentang Tag (TC-FA-TAG-607)

19. Klik ikon close pada header dialog "Report TAG"
20. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
21. Klik [Leave]
22. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 44
23. Pilih Report Type "Damaged"
24. Isi Textarea "Note" dengan "Label retak"
25. Klik [Submit]
26. Verifikasi pesan error "TAG must not be empty" tampil pada bagian "TAG to report"
27. Verifikasi dialog "Report TAG" tetap terbuka
28. Klik ikon close pada header dialog "Report TAG"
29. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
30. Klik [Leave]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-605 s.d. 608). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: validasi Note melebihi batas karakter pada dialog Report TAG ada di spec 163.
- Urutan TC di dalam spec: TC-608, TC-605, TC-606, TC-607. TC-608 (dialog kosong) dijalankan pertama agar dialog yang belum diisi dapat ditutup dengan [Cancel]; dialog dibuka ulang sebelum TC-605 sehingga error "Report type must not be empty" TC-605 tidak berimpit dengan error TC-608 (R-12). TC-606 melanjutkan dialog TC-605 setelah Report Type dipilih dan Note dikosongkan.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 7 (menutup dialog yang belum diisi dengan [Cancel]) serta langkah 19 sampai 21 dan 28 sampai 30 (menutup form dirty: ikon close, `Verifikasi` dialog "Unsaved Changes", [Leave]).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada; aksi tulis pada langkah 3, 10, 16, 25 ditolak dan tidak menambah entri Changelog, Event Log, maupun TAG Log.
- Temuan untuk QA:
  - Hook suite `beforeEach` membuka Fixed Asset > TAG untuk akun aktor pertama, sedangkan Staff Auditor tanpa Manage asset & TAG tidak berhak atas halaman itu; spec ini dikecualikan di `suite.md` bagian Hook sehingga halaman yang diuji dibuka di langkahnya sendiri.
  - TC tidak menyatakan apakah satu-satunya Tag yang terpilih otomatis membuat dialog dianggap terisi saat ditutup; spec menutup dialog yang belum diisi pengguna dengan [Cancel] atau [Keep Report] tanpa dialog Unsaved Changes, mengikuti TC-FA-TAG-666 dan TC-FA-TAG-675.
  - Post Condition TC-FA-TAG-605 s.d. 608 ("Tidak ada laporan baru untuk RF-00130" dan "Tidak ada laporan baru untuk RF-00132 maupun QR-00232") tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
