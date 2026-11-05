---
id: TC-FA-TAG-E2E-153-decline-report-submit-berhasil-dan-konflik-pengguna-lain-bagian-1
title: "Decline Report: Submit Berhasil (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-641
  - TC-FA-TAG-642
  - TC-FA-TAG-643
coverage:
  web: automated
---

# Decline Report: Submit Berhasil (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor:

| Kode | Role (teks `Role:` TC) | Email | Env password |
|---|---|---|---|
| TC | Total Control | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Akun aktor pertama: Total Control [TC]. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, task Existence Audit, serta laporan Tag (laporan terbuka Damaged, Missing, atau Unreadable dan pembatalan laporan); tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset 'Excavator 20 Ton - 20' dengan laporan | AST-0020, Group Plant B; Tag tunggal RFID `RF-00130` punya laporan terbuka Damaged dari Staff Auditor | `aset20Laporan` |
| Aset 'Excavator 20 Ton - 44' dengan laporan | AST-0044, Group Plant B; Tag RFID `RF-00132` laporan terbuka Missing dan Tag QR `QR-00232` laporan terbuka Unreadable | `aset44Laporan` |

- State yang diubah dan pemulihannya: laporan yang ditutup (Declined) oleh spec ini dan laporan yang diatur ulang dipulihkan lewat fixture backend di hook `after`.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Decline Report` per Tag (langkah 5, 15, 24).

## Test Steps

1. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)

### Decline satu Tag (TC-FA-TAG-641)

2. Buka menu aksi baris Excavator 20 Ton - 20
3. Klik "Decline Report"
4. Isi Textarea "Reason" dengan "Tag masih terbaca"
5. Klik [Submit]
6. Verifikasi dialog "Decline Report" menutup
7. Verifikasi toast "Success, report has been declined." tampil
8. Verifikasi tabel Paired dimuat ulang dan baris Excavator 20 Ton - 20 tidak lagi memuat badge "Tag Reported" pada kolom Status

### Decline dua Tag sekaligus (TC-FA-TAG-642)

9. Atur ulang data lewat fixture backend: Tag RF-00132 laporan terbuka Missing dan Tag QR-00232 laporan terbuka Unreadable hingga tersimpan, lalu muat ulang halaman
10. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)
11. Buka menu aksi baris Excavator 20 Ton - 44
12. Klik "Decline Report"
13. Centang opsi RFID dan QR
14. Isi Textarea "Reason" dengan "Keduanya masih terbaca"
15. Klik [Submit]
16. Verifikasi toast "Success, reports have been declined." tampil
17. Verifikasi dialog "Decline Report" menutup

### Decline satu dari dua laporan (TC-FA-TAG-643)

18. Atur ulang data lewat fixture backend: Tag RF-00132 laporan terbuka Missing dan Tag QR-00232 laporan terbuka Unreadable hingga tersimpan, lalu muat ulang halaman
19. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)
20. Buka menu aksi baris Excavator 20 Ton - 44
21. Klik "Decline Report"
22. Centang hanya opsi RFID
23. Isi Textarea "Reason" dengan "RFID masih terbaca"
24. Klik [Submit]
25. Verifikasi toast "Success, report has been declined." tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-641 s.d. 643). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: konflik dengan pengguna lain pada Decline Report ada di spec 154 (TC-FA-TAG-1457, 1470) dan Tag Declined dilaporkan ulang di spec 169 (TC-FA-TAG-644).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9 dan 18 (mengatur ulang dua laporan terbuka pada AST-0044 lewat fixture backend; muat ulang halaman juga menghilangkan toast sebelumnya).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Decline Report` per Tag (langkah 5, 15, 24).
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-641 (laporan Declined, Tag tetap Paired, kartu Reported, row action "Decline Report" hilang, modul terdampak notification dan Audit), TC-FA-TAG-642, dan TC-FA-TAG-643 tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
