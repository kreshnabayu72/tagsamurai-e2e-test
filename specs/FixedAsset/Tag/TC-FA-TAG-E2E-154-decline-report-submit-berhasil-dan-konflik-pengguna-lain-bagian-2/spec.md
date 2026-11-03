---
id: TC-FA-TAG-E2E-154-decline-report-submit-berhasil-dan-konflik-pengguna-lain-bagian-2
title: "Decline Report: Konflik dengan Pengguna Lain (Bagian 2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1457
  - TC-FA-TAG-1470
coverage:
  web: automated
---

# Decline Report: Konflik dengan Pengguna Lain (Bagian 2)

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
- Sesi API aktor: pelaku kedua memakai login API (password) yang tidak dihitung sebagai sesi web (lihat `suite.md`), tanpa asersi di sesinya; akun Total Control kedua disediakan tim FE (akun pelaku tidak tertulis di Pre-setup TC).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, task Existence Audit, serta laporan Tag (laporan terbuka Damaged, Missing, atau Unreadable dan pembatalan laporan); tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset 'Excavator 20 Ton - 20' dengan laporan | AST-0020, Group Plant B; Tag tunggal RFID `RF-00130` punya laporan terbuka Damaged dari Staff Auditor | `aset20Laporan` |
| Aset 'Excavator 20 Ton - 44' dengan laporan | AST-0044, Group Plant B; Tag RFID `RF-00132` laporan terbuka Missing dan Tag QR `QR-00232` laporan terbuka Unreadable | `aset44Laporan` |
| Pelaku kedua | Pengguna B: akun Total Control kedua, sesi API, disediakan tim FE | `pelakuKeduaTc` |

- State yang diubah dan pemulihannya: laporan yang ditutup pelaku kedua dan laporan yang diatur ulang dipulihkan lewat fixture backend di hook `after`.

## Test Steps

1. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)

### Laporan sudah ditolak pengguna lain (TC-FA-TAG-1457)

2. Buka menu aksi baris Excavator 20 Ton - 20
3. Klik "Decline Report"
4. Isi Textarea "Reason" dengan "Label masih terbaca"
5. Pelaku kedua lewat sesi API melakukan Decline Report pada Tag RF-00130 dengan Reason "Tag masih berfungsi" hingga penutupan laporan tersimpan
6. Klik [Submit]
7. Verifikasi toast "Error, failed to decline report." tampil untuk pengguna A
8. Verifikasi dialog "Decline Report" pengguna A tetap terbuka
9. Klik ikon close pada header dialog "Decline Report"
10. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
11. Klik [Leave]

### Dua Tag ketika laporan salah satu Tag sudah ditolak pengguna lain (TC-FA-TAG-1470)

12. Atur ulang data lewat fixture backend: Tag RF-00132 laporan terbuka Missing dan Tag QR-00232 laporan terbuka Unreadable hingga tersimpan, lalu muat ulang halaman
13. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)
14. Buka menu aksi baris Excavator 20 Ton - 44
15. Klik "Decline Report"
16. Centang kedua Tag pada bagian "TAG to decline"
17. Isi Textarea "Reason" dengan "Label masih terbaca"
18. Pelaku kedua lewat sesi API melakukan Decline Report pada Tag RF-00132 saja dengan Reason "Tag masih berfungsi" hingga penutupan laporan tersimpan
19. Klik [Submit]
20. Verifikasi toast "Error, failed to decline report." tampil untuk pengguna A
21. Verifikasi dialog "Decline Report" pengguna A tetap terbuka
22. Verifikasi (baca lewat fixture backend) laporan QR-00232 tidak ditutup oleh Submit pengguna A (semua-atau-tidak)
23. Klik ikon close pada header dialog "Decline Report"
24. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
25. Klik [Leave]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1457, 1470). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: Decline Report satu pengguna ada di spec 151 sampai 153. Laporan ulang Tag Declined (TC-FA-TAG-644) ada di spec 169.
- Pengguna B memakai sesi API (keputusan pelaku kedua yang hanya memicu perubahan state): bukan konteks kedua kelas c dan tidak memakai `P-2`; langkah pemicunya ditulis "... hingga ... tersimpan" (langkah 5 dan 18). Hasil di sesi pengguna B tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9 sampai 11 dan 23 sampai 25 (menutup form dirty) serta 12 (mengatur ulang dua laporan terbuka pada AST-0044 lewat fixture backend).
- Temuan untuk QA:
  - TC-FA-TAG-1457 dan TC-FA-TAG-1470 menulis dua sesi browser terpisah dengan pengguna B yang melakukan Decline Report "sampai sukses"; TC tidak menyebut akun pengguna B selain Role Total Control, sehingga spec menulisnya sebagai akun kedua yang disediakan tim FE lewat sesi API.
  - Post Condition TC-FA-TAG-1457 dan TC-FA-TAG-1470 (laporan hanya ditutup sekali dan Changelog memuat satu entri Decline Report) tanpa langkah observasi di TC tidak diasersi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
