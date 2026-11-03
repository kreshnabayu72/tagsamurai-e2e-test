---
id: TC-FA-TAG-E2E-143-report-tag-screening-dialog-dan-opsi-tag-bagian-2
title: "Report TAG: Menu Aksi pada Aset dengan Laporan Terbuka Sebagian (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-604
coverage:
  web: automated
---

# Report TAG: Menu Aksi pada Aset dengan Laporan Terbuka Sebagian (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor:

| Kode | Role (teks `Role:` TC) | Email | Env password |
|---|---|---|---|
| SA_NOTAG | Staff Auditor (tidak memegang Manage asset & TAG) | `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD` |

- Akun aktor pertama: Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG]. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Aksi spec ini dijalankan dari modul Audit, sehingga langkah pertama berpindah ke modul Audit. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, task Existence Audit, serta laporan Tag (laporan terbuka Damaged, Missing, atau Unreadable dan pembatalan laporan); tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Task Existence Audit | Task milik spec berstatus In Audit dengan item AST-0020 dan AST-0044 | `taskExistenceAudit` |
| Aset 'Excavator 20 Ton - 44' | AST-0044, Group Plant B; Tag RFID `RF-00132` dan Tag QR `QR-00232` keduanya Paired | `aset44` |
| Laporan terbuka awal | Tag `RF-00132` punya laporan terbuka Missing; Tag `QR-00232` tanpa laporan terbuka | `laporan132Missing` |

- State yang diubah dan pemulihannya: laporan terbuka pada `RF-00132` dibatalkan dan data dipulihkan lewat fixture backend di hook `after`.

## Test Steps

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
2. Buka menu aksi baris Excavator 20 Ton - 44
3. Verifikasi menu aksi memuat "Report TAG" dan "Cancel Report TAG" bersamaan
4. Tutup menu aksi dengan menekan Esc

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-604). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik dialog Report TAG dan menu aksi aset ber-laporan ada juga di spec 142 (TC-FA-TAG-598 s.d. 603).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 4 (menutup menu aksi).
- Temuan untuk QA:
  - Hook suite `beforeEach` membuka Fixed Asset > TAG untuk akun aktor pertama, sedangkan Staff Auditor tanpa Manage asset & TAG tidak berhak atas halaman itu; hook perlu dikecualikan untuk spec ini di tahap script.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
