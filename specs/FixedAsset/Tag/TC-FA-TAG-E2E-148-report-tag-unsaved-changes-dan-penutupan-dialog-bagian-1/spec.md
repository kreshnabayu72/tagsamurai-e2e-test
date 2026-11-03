---
id: TC-FA-TAG-E2E-148-report-tag-unsaved-changes-dan-penutupan-dialog-bagian-1
title: "Report TAG: Unsaved Changes dan Penutupan Dialog (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-622
  - TC-FA-TAG-623
  - TC-FA-TAG-624
  - TC-FA-TAG-625
  - TC-FA-TAG-626
coverage:
  web: automated
---

# Report TAG: Unsaved Changes dan Penutupan Dialog (Bagian 1)

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

- State yang diubah dan pemulihannya: tidak ada laporan yang dibuat spec ini; data dipulihkan lewat fixture backend di hook `after`.

## Test Steps

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
2. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 44
3. Pilih Report Type "Damaged"

### Cancel pada dialog terisi (TC-FA-TAG-622)

4. Klik [Cancel] pada dialog "Report TAG"
5. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
6. Verifikasi dialog "Report TAG" tetap terbuka di bawahnya
7. Klik [Cancel] pada dialog "Unsaved Changes"

### Ikon close pada dialog terisi (TC-FA-TAG-623)

8. Klik ikon close pada header dialog "Report TAG"
9. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
10. Verifikasi dialog "Report TAG" tetap terbuka di bawahnya
11. Klik [Cancel] pada dialog "Unsaved Changes"

### Esc pada dialog terisi (TC-FA-TAG-624)

12. Tekan tombol Esc
13. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
14. Verifikasi dialog "Report TAG" tetap terbuka di bawahnya
15. Klik [Cancel] pada dialog "Unsaved Changes"

### Cancel pada Unsaved Changes mempertahankan isian (TC-FA-TAG-625)

16. Klik ikon close pada header dialog "Report TAG"
17. Pada dialog "Unsaved Changes" klik [Cancel]
18. Verifikasi dialog "Unsaved Changes" menutup
19. Verifikasi dialog "Report TAG" tetap terbuka dengan isian yang sama (Report Type "Damaged" masih terpilih)

### Leave pada Unsaved Changes (TC-FA-TAG-626)

20. Klik ikon close pada header dialog "Report TAG"
21. Pada dialog "Unsaved Changes" klik [Leave]
22. Verifikasi dialog "Unsaved Changes" dan dialog "Report TAG" menutup
23. Verifikasi tidak ada toast

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-622 s.d. 626). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Unsaved Changes dialog Report TAG ada juga di spec 149 (TC-FA-TAG-627 s.d. 632) dan spec 150 (TC-FA-TAG-633, 634).
- Satu dialog "Report TAG" dipakai berurutan oleh TC-622 sampai TC-626: Report Type "Damaged" dipilih sekali (langkah 3) karena precondition dan isian ketiga TC pertama identik, lalu dialog "Unsaved Changes" ditutup dengan [Cancel] antar-TC (langkah 7, 11, 15) supaya isian tetap terpertahankan (S-09). TC-626 menutup dialog dengan [Leave] sebagai langkah terakhir spec.
- Temuan untuk QA:
  - Hook suite `beforeEach` membuka Fixed Asset > TAG untuk akun aktor pertama, sedangkan Staff Auditor tanpa Manage asset & TAG tidak berhak atas halaman itu; hook perlu dikecualikan untuk spec ini di tahap script.
  - Post Condition TC-FA-TAG-622 s.d. 626 ("Tidak ada laporan baru untuk RF-00132 maupun QR-00232") tanpa langkah observasi di TC tidak diasersi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
