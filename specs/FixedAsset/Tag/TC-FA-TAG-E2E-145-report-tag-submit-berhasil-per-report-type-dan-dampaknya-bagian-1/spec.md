---
id: TC-FA-TAG-E2E-145-report-tag-submit-berhasil-per-report-type-dan-dampaknya-bagian-1
title: "Report TAG: Submit Berhasil per Report Type dan Dua Tag (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-609
  - TC-FA-TAG-610
  - TC-FA-TAG-611
  - TC-FA-TAG-612
coverage:
  web: automated
---

# Report TAG: Submit Berhasil per Report Type dan Dua Tag (Bagian 1)

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
| Aset 'Excavator 20 Ton - 20' | AST-0020, Group Plant B, status Assigned; Tag tunggal RFID `RF-00130` Paired | `aset20` |
| Aset 'Excavator 20 Ton - 44' | AST-0044, Group Plant B; Tag RFID `RF-00132` dan Tag QR `QR-00232` keduanya Paired | `aset44` |

- State yang diubah dan pemulihannya: laporan terbuka yang dibuat spec ini pada `RF-00130`, `RF-00132`, dan `QR-00232` dibatalkan dan data dipulihkan lewat fixture backend di hook `after`.

## Test Steps

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit

### Report Type Damaged (TC-FA-TAG-609)

2. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
3. Pilih Report Type "Damaged"
4. Isi Textarea "Note" dengan "Label retak"
5. Klik [Submit]
6. Verifikasi dialog "Report TAG" menutup
7. Verifikasi toast "Success, TAG has been reported." tampil

### Report Type Missing (TC-FA-TAG-610)

8. Atur ulang data lewat fixture backend: Tag RF-00130 tanpa laporan terbuka hingga tersimpan, lalu muat ulang halaman Task Detail
9. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
10. Pilih Report Type "Missing"
11. Isi Textarea "Note" dengan "Label retak"
12. Klik [Submit]
13. Verifikasi dialog "Report TAG" menutup
14. Verifikasi toast "Success, TAG has been reported." tampil

### Report Type Unreadable (TC-FA-TAG-611)

15. Atur ulang data lewat fixture backend: Tag RF-00130 tanpa laporan terbuka hingga tersimpan, lalu muat ulang halaman Task Detail
16. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
17. Pilih Report Type "Unreadable"
18. Isi Textarea "Note" dengan "Label retak"
19. Klik [Submit]
20. Verifikasi dialog "Report TAG" menutup
21. Verifikasi toast "Success, TAG has been reported." tampil

### Dua Tag sekaligus (TC-FA-TAG-612)

22. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 44
23. Centang opsi "RFID" dan "QR"
24. Pilih Report Type "Damaged"
25. Isi Textarea "Note" dengan "Dua label rusak"
26. Klik [Submit]
27. Verifikasi dialog "Report TAG" menutup
28. Verifikasi toast "Success, TAGs have been reported." tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-609 s.d. 612). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: dampak laporan pada status aset, registri Global, dan kartu Reported ada di spec 146 (TC-FA-TAG-613 s.d. 616).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 8 dan 15 (mengatur ulang `RF-00130` tanpa laporan terbuka agar TC berikutnya dapat melaporkannya lagi; muat ulang halaman juga menghilangkan toast TC sebelumnya sehingga asersi toast berikutnya tidak membaca toast lama).
- Temuan untuk QA:
  - Hook suite `beforeEach` membuka Fixed Asset > TAG untuk akun aktor pertama, sedangkan Staff Auditor tanpa Manage asset & TAG tidak berhak atas halaman itu; hook perlu dikecualikan untuk spec ini di tahap script.
  - Post Condition TC-FA-TAG-609 s.d. 612 (laporan terbuka tercatat, Tag tetap Paired di registri Global, status "Tag Reported", kartu Reported, modul terdampak Audit dan notification) tanpa langkah observasi di TC tidak diasersi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
