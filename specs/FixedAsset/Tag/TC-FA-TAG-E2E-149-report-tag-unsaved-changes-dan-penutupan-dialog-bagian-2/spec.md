---
id: TC-FA-TAG-E2E-149-report-tag-unsaved-changes-dan-penutupan-dialog-bagian-2
title: "Report TAG: Unsaved Changes dan Penutupan Dialog (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-627
  - TC-FA-TAG-628
  - TC-FA-TAG-629
  - TC-FA-TAG-630
  - TC-FA-TAG-631
  - TC-FA-TAG-632
coverage:
  web: automated
---

# Report TAG: Unsaved Changes dan Penutupan Dialog (Bagian 2)

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
| Aset 'Excavator 20 Ton - 44' | AST-0044, Group Plant B; Tag RFID `RF-00132` dan Tag QR `QR-00232` keduanya Paired | `aset44` |

- State yang diubah dan pemulihannya: tidak ada laporan yang dibuat spec ini; data dipulihkan lewat fixture backend di hook `after`.

## Test Steps

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit

### Ikon close pada dialog yang belum terisi (TC-FA-TAG-627)

2. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 44
3. Klik ikon close pada header dialog "Report TAG"
4. Verifikasi dialog "Report TAG" menutup langsung
5. Verifikasi dialog "Unsaved Changes" tidak tampil

### Isian dikosongkan kembali (TC-FA-TAG-628)

6. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 44
7. Pilih Report Type "Damaged"
8. Kosongkan kembali isian yang tadi diisi
9. Klik ikon close pada header dialog "Report TAG"
10. Verifikasi dialog "Report TAG" menutup langsung
11. Verifikasi dialog "Unsaved Changes" tidak tampil

### Refresh halaman pada dialog terisi (TC-FA-TAG-629)

12. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 44
13. Pilih Report Type "Damaged"
14. Tekan F5 untuk memuat ulang halaman
15. Verifikasi konfirmasi bawaan browser (beforeunload) muncul sebelum halaman dimuat ulang
16. Konfirmasi dialog beforeunload sehingga halaman dimuat ulang

### Dialog terisi hanya Tag tercentang (TC-FA-TAG-630)

17. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 44
18. Centang opsi "RFID"
19. Klik ikon close pada header dialog "Report TAG"
20. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
21. Verifikasi dialog "Report TAG" tetap terbuka di bawahnya
22. Klik [Leave]

### Dialog terisi hanya Report Type (TC-FA-TAG-631)

23. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 44
24. Pilih Report Type "Damaged"
25. Klik ikon close pada header dialog "Report TAG"
26. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
27. Verifikasi dialog "Report TAG" tetap terbuka di bawahnya
28. Klik [Leave]

### Dialog terisi hanya Note (TC-FA-TAG-632)

29. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 44
30. Isi Textarea "Note" dengan "Label retak"
31. Klik ikon close pada header dialog "Report TAG"
32. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
33. Verifikasi dialog "Report TAG" tetap terbuka di bawahnya
34. Klik [Leave]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-627 s.d. 632). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Unsaved Changes dialog Report TAG ada juga di spec 148 (TC-FA-TAG-622 s.d. 626) dan spec 150 (TC-FA-TAG-633, 634).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 16 (mengonfirmasi dialog beforeunload sehingga halaman dimuat ulang; kemampuan penanganan beforeunload tertulis di Prerequisites, S-08) dan tiap langkah `Klik [Leave]` pada TC-630 sampai TC-632 (menutup form dirty).
- Temuan untuk QA:
  - Hook suite `beforeEach` membuka Fixed Asset > TAG untuk akun aktor pertama, sedangkan Staff Auditor tanpa Manage asset & TAG tidak berhak atas halaman itu; hook perlu dikecualikan untuk spec ini di tahap script.
  - TC-FA-TAG-628 meminta "Kosongkan kembali isian yang tadi diisi" setelah memilih Report Type; Radio tidak lazim dapat dikosongkan, sehingga spec mengikuti teks TC pada langkah 8 dan cara mengosongkan Radio perlu dipastikan QA.
  - Post Condition TC-FA-TAG-627 s.d. 632 ("Tidak ada laporan baru untuk RF-00132 maupun QR-00232") tanpa langkah observasi di TC tidak diasersi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
