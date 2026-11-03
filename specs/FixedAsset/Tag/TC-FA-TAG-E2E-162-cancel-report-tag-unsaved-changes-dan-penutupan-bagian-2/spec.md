---
id: TC-FA-TAG-E2E-162-cancel-report-tag-unsaved-changes-dan-penutupan-bagian-2
title: "Cancel Report TAG: Unsaved Changes dan Penutupan Dialog (Bagian 2)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-676
  - TC-FA-TAG-677
  - TC-FA-TAG-678
  - TC-FA-TAG-679
coverage:
  web: automated
---

# Cancel Report TAG: Unsaved Changes dan Penutupan Dialog (Bagian 2)

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
- Kemampuan teknis (disediakan tim FE/BE): penanganan dialog `beforeunload` browser (konfirmasi bawaan saat F5).
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Task Existence Audit | Task milik spec berstatus In Audit dengan item AST-0020 dan AST-0044 | `taskExistenceAudit` |
| Aset 'Excavator 20 Ton - 44' dengan laporan | AST-0044, Group Plant B; Tag RFID `RF-00132` laporan terbuka Missing dan Tag QR `QR-00232` laporan terbuka Unreadable | `aset44Laporan` |

- State yang diubah dan pemulihannya: tidak ada laporan yang dibatalkan oleh spec ini; data dipulihkan lewat fixture backend di hook `after`.

## Test Steps

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit

### Isian dikosongkan kembali (TC-FA-TAG-676)

2. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 44
3. Isi Textarea "Reason" dengan "Tag ternyata terbaca"
4. Kosongkan kembali isian yang tadi diisi
5. Klik ikon close pada header dialog "Cancel Report TAG"
6. Verifikasi dialog "Cancel Report TAG" menutup langsung
7. Verifikasi dialog "Unsaved Changes" tidak tampil

### Refresh halaman pada dialog terisi (TC-FA-TAG-677)

8. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 44
9. Isi Textarea "Reason" dengan "Tag ternyata terbaca"
10. Tekan F5 untuk memuat ulang halaman
11. Verifikasi konfirmasi bawaan browser (beforeunload) muncul sebelum halaman dimuat ulang
12. Konfirmasi dialog beforeunload sehingga halaman dimuat ulang

### Dialog terisi hanya Tag tercentang (TC-FA-TAG-678)

13. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 44
14. Centang opsi RFID
15. Klik ikon close pada header dialog "Cancel Report TAG"
16. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
17. Verifikasi dialog "Cancel Report TAG" tetap terbuka di bawahnya
18. Klik [Leave]

### Dialog terisi hanya Reason (TC-FA-TAG-679)

19. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 44
20. Isi Textarea "Reason" dengan "Tag ternyata terbaca"
21. Klik ikon close pada header dialog "Cancel Report TAG"
22. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
23. Verifikasi dialog "Cancel Report TAG" tetap terbuka di bawahnya
24. Klik [Leave]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-676 s.d. 679). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Unsaved Changes dialog Cancel Report TAG ada juga di spec 161 (TC-FA-TAG-671 s.d. 675).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 12 (mengonfirmasi dialog beforeunload sehingga halaman dimuat ulang; kemampuan penanganan beforeunload tertulis di Prerequisites, S-08) dan tiap langkah `Klik [Leave]` pada TC-678 dan TC-679 (menutup form dirty).
- Temuan untuk QA:
  - Hook suite `beforeEach` membuka Fixed Asset > TAG untuk akun aktor pertama, sedangkan Staff Auditor tanpa Manage asset & TAG tidak berhak atas halaman itu; hook perlu dikecualikan untuk spec ini di tahap script.
  - TC-FA-TAG-676 meminta "Kosongkan kembali isian yang tadi diisi" pada Textarea "Reason"; spec mengosongkan isian (langkah 4) tanpa memicu Unsaved Changes mengikuti teks TC.
  - Post Condition TC-FA-TAG-676 s.d. 679 ("Kedua laporan tetap terbuka") tanpa langkah observasi di TC tidak diasersi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
