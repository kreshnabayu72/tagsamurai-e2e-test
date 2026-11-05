---
id: TC-FA-TAG-E2E-159-cancel-report-tag-submit-berhasil-keep-report-dan-modul-borrow-bagian-1
title: "Cancel Report TAG: Submit Berhasil, Keep Report, dan Laporan Ulang (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-662
  - TC-FA-TAG-663
  - TC-FA-TAG-664
  - TC-FA-TAG-665
  - TC-FA-TAG-666
coverage:
  web: automated
---

# Cancel Report TAG: Submit Berhasil, Keep Report, dan Laporan Ulang (Bagian 1)

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

- State yang diubah dan pemulihannya: laporan yang dibatalkan, laporan baru Missing pada `RF-00130`, dan laporan yang diatur ulang dipulihkan lewat fixture backend di hook `after`.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 14); entri Changelog `Cancel Report` per Tag (langkah 7, 20, 27).

## Test Steps

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit

### Keep Report pada dialog yang masih kosong (TC-FA-TAG-666)

2. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 20
3. Klik tombol [Keep Report]
4. Verifikasi dialog "Cancel Report" menutup langsung tanpa dialog konfirmasi

### Cancel Report satu Tag lalu laporan ulang (TC-FA-TAG-662 dan TC-FA-TAG-665)

5. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 20
6. Isi Textarea "Reason" dengan "Tag ternyata terbaca"
7. Klik tombol [Cancel Report]
8. Verifikasi dialog "Cancel Report" menutup
9. Verifikasi toast "Success, report has been canceled." tampil
10. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
11. Verifikasi dialog "Report TAG" menerima RF-00130 (opsi tidak Disabled)
12. Pilih Report Type "Missing"
13. Isi Textarea "Note" dengan "Hilang lagi"
14. Klik tombol [Submit]
15. Verifikasi toast "Success, TAG has been reported." tampil

### Cancel Report dua Tag sekaligus (TC-FA-TAG-663)

16. Atur ulang data lewat fixture backend: Tag RF-00132 laporan terbuka Missing dan Tag QR-00232 laporan terbuka Unreadable hingga tersimpan, lalu muat ulang halaman Task Detail
17. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 44
18. Centang opsi RFID dan QR
19. Isi Textarea "Reason" dengan "Keduanya terbaca"
20. Klik tombol [Cancel Report]
21. Verifikasi toast "Success, reports have been canceled." tampil
22. Verifikasi dialog "Cancel Report" menutup

### Cancel Report satu dari dua laporan (TC-FA-TAG-664)

23. Atur ulang data lewat fixture backend: Tag RF-00132 laporan terbuka Missing dan Tag QR-00232 laporan terbuka Unreadable hingga tersimpan, lalu muat ulang halaman Task Detail
24. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 44
25. Centang hanya opsi QR
26. Isi Textarea "Reason" dengan "QR terbaca"
27. Klik tombol [Cancel Report]
28. Verifikasi toast "Success, report has been canceled." tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-662 s.d. 666). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: Cancel Report TAG lewat dialog milik Borrow dan Keep Report pada dialog terisi ada di spec 160.
- Urutan TC di dalam spec: TC-666 (Keep Report pada dialog kosong) lebih dulu, lalu TC-662 dan TC-665, TC-663, TC-664. TC-662 dan TC-665 memakai langkah Cancel Report yang identik (AST-0020, Reason "Tag ternyata terbaca"; langkah 5 sampai 7), sehingga satu pembatalan menjadi dasar kedua TC dan laporan ulang TC-665 langsung menyusul.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 16 dan 23 (mengatur ulang dua laporan terbuka pada AST-0044 lewat fixture backend; muat ulang halaman juga menghilangkan toast sebelumnya).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 14); entri Changelog `Cancel Report` per Tag (langkah 7, 20, 27).
- Temuan untuk QA:
  - Hook suite `beforeEach` membuka Fixed Asset > TAG untuk akun aktor pertama, sedangkan Staff Auditor tanpa Manage asset & TAG tidak berhak atas halaman itu; spec ini dikecualikan di `suite.md` bagian Hook sehingga halaman yang diuji dibuka di langkahnya sendiri.
  - Post Condition TC-FA-TAG-662 s.d. 665 (laporan Canceled, Tag tetap Paired, status "Tag Reported", kartu Reported, modul terdampak notification dan Audit) dan TC-FA-TAG-666 ("tidak ada notifikasi atau entri Changelog baru") tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
