---
id: TC-FA-TAG-E2E-168-report-tag-konflik-dua-tag-ketika-satu-tag-sudah-dilaporkan-pengguna-lain
title: "Report TAG: Konflik Dua Tag Ketika Satu Tag Sudah Dilaporkan Pengguna Lain"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1472
coverage:
  web: automated
---

# Report TAG: Konflik Dua Tag Ketika Satu Tag Sudah Dilaporkan Pengguna Lain

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
- Sesi API aktor: pelaku kedua memakai login API (password) yang tidak dihitung sebagai sesi web (lihat `suite.md`), tanpa asersi di sesinya; akun Staff Auditor kedua disediakan tim FE (akun pelaku tidak tertulis di Pre-setup TC).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, task Existence Audit, serta laporan Tag (laporan terbuka Damaged, Missing, atau Unreadable dan pembatalan laporan); tidak ada endpoint yang dikarang di spec ini.
- Kemampuan teknis (disediakan tim FE/BE): pembacaan status laporan Tag (terbuka atau ditutup) dari backend lewat fixture backend; dipakai hanya untuk Verifikasi "baca lewat fixture backend" pada butir Expected semua-atau-tidak, tanpa endpoint yang dikarang.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Task Existence Audit | Task milik spec berstatus In Audit dengan item AST-0020 dan AST-0044 | `taskExistenceAudit` |
| Aset 'Excavator 20 Ton - 44' | AST-0044, Group Plant B; Tag RFID `RF-00132` dan Tag QR `QR-00232` keduanya Paired | `aset44` |
| Pelaku kedua | Pengguna B: akun Staff Auditor kedua, sesi API, disediakan tim FE | `pelakuKeduaSa` |

- State yang diubah dan pemulihannya: laporan Missing yang dibuat pelaku kedua pada `RF-00132` dibatalkan dan data dipulihkan lewat fixture backend di hook `after`.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 6). Aksi tulis pada langkah 7 ditolak dan tidak menambah entri.

## Test Steps

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
2. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 44
3. Centang opsi "RFID" dan "QR"
4. Pilih Report Type "Damaged"
5. Isi Textarea "Note" dengan "Dua label rusak"
6. Pelaku kedua lewat sesi API melaporkan Tag RFID RF-00132 saja dengan Report Type "Missing" dan Note "Label hilang" hingga laporan tersimpan
7. Klik tombol [Submit]
8. Verifikasi toast "Error, failed to report TAG." tampil untuk pengguna A
9. Verifikasi dialog "Report TAG" pengguna A tetap terbuka
10. Verifikasi (baca lewat fixture backend) tidak ada laporan baru dibuat untuk QR-00232 oleh Submit pengguna A (semua-atau-tidak)
11. Klik ikon close pada header dialog "Report TAG"
12. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
13. Klik [Leave]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1472). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: konflik laporan pada satu Tag (TC-FA-TAG-618) ada di spec 147.
- Pengguna B memakai sesi API (keputusan pelaku kedua yang hanya memicu perubahan state): bukan konteks kedua kelas c dan tidak memakai `P-2`; langkah pemicunya ditulis "... hingga ... tersimpan" (langkah 6). Hasil di sesi pengguna B tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 11 sampai 13 (menutup form dirty: ikon close, `Verifikasi` dialog "Unsaved Changes", [Leave]).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 6). Aksi tulis pada langkah 7 ditolak dan tidak menambah entri.
- Temuan untuk QA:
  - Hook suite `beforeEach` membuka Fixed Asset > TAG untuk akun aktor pertama, sedangkan Staff Auditor tanpa Manage asset & TAG tidak berhak atas halaman itu; spec ini dikecualikan di `suite.md` bagian Hook sehingga halaman yang diuji dibuka di langkahnya sendiri.
  - TC-FA-TAG-1472 menulis pengguna B login pada sesi browser terpisah tanpa menyebut akun pengguna B; spec menulisnya sebagai akun Staff Auditor kedua yang disediakan tim FE lewat sesi API.
  - Post Condition TC-FA-TAG-1472 ("Hanya satu laporan terbuka untuk RF-00132 (Missing dari pengguna B)") tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
