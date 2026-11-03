---
id: TC-FA-TAG-E2E-161-cancel-report-tag-unsaved-changes-dan-penutupan-bagian-1
title: "Cancel Report TAG: Unsaved Changes dan Penutupan Dialog (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-671
  - TC-FA-TAG-672
  - TC-FA-TAG-673
  - TC-FA-TAG-674
  - TC-FA-TAG-675
coverage:
  web: automated
---

# Cancel Report TAG: Unsaved Changes dan Penutupan Dialog (Bagian 1)

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
| Aset 'Excavator 20 Ton - 44' dengan laporan | AST-0044, Group Plant B; Tag RFID `RF-00132` laporan terbuka Missing dan Tag QR `QR-00232` laporan terbuka Unreadable | `aset44Laporan` |

- State yang diubah dan pemulihannya: tidak ada laporan yang dibatalkan oleh spec ini; data dipulihkan lewat fixture backend di hook `after`.

## Test Steps

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
2. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 44
3. Isi Textarea "Reason" dengan "Tag ternyata terbaca"

### Ikon close pada dialog terisi (TC-FA-TAG-671)

4. Klik ikon close pada header dialog "Cancel Report TAG"
5. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
6. Verifikasi dialog "Cancel Report TAG" tetap terbuka di bawahnya
7. Klik [Cancel] pada dialog "Unsaved Changes"

### Esc pada dialog terisi (TC-FA-TAG-672)

8. Tekan tombol Esc
9. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
10. Verifikasi dialog "Cancel Report TAG" tetap terbuka di bawahnya
11. Klik [Cancel] pada dialog "Unsaved Changes"

### Cancel pada Unsaved Changes mempertahankan isian (TC-FA-TAG-673)

12. Klik ikon close pada header dialog "Cancel Report TAG"
13. Pada dialog "Unsaved Changes" klik [Cancel]
14. Verifikasi dialog "Unsaved Changes" menutup
15. Verifikasi dialog "Cancel Report TAG" tetap terbuka dengan isian yang sama (Reason "Tag ternyata terbaca")

### Leave pada Unsaved Changes (TC-FA-TAG-674)

16. Klik ikon close pada header dialog "Cancel Report TAG"
17. Pada dialog "Unsaved Changes" klik [Leave]
18. Verifikasi dialog "Unsaved Changes" dan dialog "Cancel Report TAG" menutup
19. Verifikasi tidak ada toast

### Ikon close pada dialog yang belum terisi (TC-FA-TAG-675)

20. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 44
21. Klik ikon close pada header dialog "Cancel Report TAG"
22. Verifikasi dialog "Cancel Report TAG" menutup langsung
23. Verifikasi dialog "Unsaved Changes" tidak tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-671 s.d. 675). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Unsaved Changes dialog Cancel Report TAG ada juga di spec 162 (TC-FA-TAG-676 s.d. 679).
- Satu dialog "Cancel Report TAG" pada AST-0044 dengan Reason "Tag ternyata terbaca" dipakai berurutan oleh TC-671 sampai TC-674 (precondition dan isian identik); dialog "Unsaved Changes" ditutup dengan [Cancel] antar-TC supaya isian terpertahankan (S-09). TC-674 menutup dialog dengan [Leave] sehingga TC-675 membuka dialog baru yang belum terisi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 7 dan 11 (menutup dialog "Unsaved Changes" dengan [Cancel]).
- Temuan untuk QA:
  - Hook suite `beforeEach` membuka Fixed Asset > TAG untuk akun aktor pertama, sedangkan Staff Auditor tanpa Manage asset & TAG tidak berhak atas halaman itu; hook perlu dikecualikan untuk spec ini di tahap script.
  - Post Condition TC-FA-TAG-671 s.d. 675 ("Kedua laporan tetap terbuka") tanpa langkah observasi di TC tidak diasersi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
