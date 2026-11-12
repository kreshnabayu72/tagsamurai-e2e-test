---
id: TC-FA-TAG-E2E-150-report-tag-unsaved-changes-dan-penutupan-dialog-bagian-3
title: "Report TAG: Esc pada Unsaved Changes dan Klik Backdrop (Bagian 3)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-633
  - TC-FA-TAG-634
coverage:
  web: automated
---

# Report TAG: Esc pada Unsaved Changes dan Klik Backdrop (Bagian 3)

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
| Aset 'Excavator 20 Ton - 44' | AST-0044, Group Plant B; Tag RFID `RF-00132` dan Tag QR `QR-00232` keduanya Paired | `aset44` |

- State yang diubah dan pemulihannya: tidak ada laporan yang dibuat spec ini; data dipulihkan lewat fixture backend di hook `after`.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
2. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 44
3. Pilih Report Type "Damaged"
4. Klik ikon close pada header dialog "Report TAG"
5. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]

### Esc pada dialog Unsaved Changes (TC-FA-TAG-633)

6. Pada dialog "Unsaved Changes" tekan Esc
7. Verifikasi dialog "Unsaved Changes" menutup
8. Verifikasi dialog "Report TAG" tetap terbuka dengan Report Type "Damaged" masih terpilih

### Klik backdrop (TC-FA-TAG-634)

9. Klik area backdrop di luar dialog
10. Verifikasi dialog "Report TAG" tetap terbuka
11. Verifikasi dialog "Unsaved Changes" tidak tampil
12. Klik ikon close pada header dialog "Report TAG"
13. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
14. Klik [Leave]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-633, 634). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Unsaved Changes dialog Report TAG ada juga di spec 148 dan spec 149.
- Satu dialog "Report TAG" dengan Report Type "Damaged" dipakai berurutan oleh TC-633 dan TC-634 (precondition dan isian identik); sesudah TC-633 dialog "Unsaved Changes" tertutup dan isian tetap, sehingga TC-634 melanjutkan state itu.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 4 (ikon close yang memunculkan dialog "Unsaved Changes" untuk TC-633) serta langkah 12 sampai 14 (menutup form dirty di akhir spec: ikon close, `Verifikasi` dialog "Unsaved Changes", [Leave]).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - Hook suite `beforeEach` membuka Fixed Asset > TAG untuk akun aktor pertama, sedangkan Staff Auditor tanpa Manage asset & TAG tidak berhak atas halaman itu; spec ini dikecualikan di `suite.md` bagian Hook sehingga halaman yang diuji dibuka di langkahnya sendiri.
  - Post Condition TC-FA-TAG-633 dan TC-FA-TAG-634 ("Tidak ada laporan baru untuk RF-00132 maupun QR-00232") tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
