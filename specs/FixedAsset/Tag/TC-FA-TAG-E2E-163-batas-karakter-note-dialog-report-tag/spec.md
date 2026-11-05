---
id: TC-FA-TAG-E2E-163-batas-karakter-note-dialog-report-tag
title: "Batas Karakter Note Dialog Report TAG"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-1384
  - TC-FA-TAG-1385
  - TC-FA-TAG-1386
  - TC-FA-TAG-1387
coverage:
  web: automated
---

# Batas Karakter Note Dialog Report TAG

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
| Aset 'Excavator 20 Ton - 20' | AST-0020, Group Plant B, status Assigned; Tag tunggal RFID `RF-00130` Paired | `aset20` |

- State yang diubah dan pemulihannya: laporan terbuka yang dibuat spec ini pada `RF-00130` dibatalkan dan data dipulihkan lewat fixture backend di hook `after`.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 21, 29). Aksi tulis pada langkah 6, 10 ditolak dan tidak menambah entri.

## Test Steps

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit

### Note 361 karakter ditolak (TC-FA-TAG-1385)

2. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
3. Pilih Report Type "Damaged"
4. Isi Textarea "Note" dengan teks 361 karakter (huruf `a` diulang 361 kali)
5. Verifikasi pesan error "Max. 360 characters" tampil pada Textarea "Note" langsung setelah teks diisi
6. Klik tombol [Submit]
7. Verifikasi [Submit] diblok selama error masih tampil (tidak ada toast sukses dan error "Max. 360 characters" masih tampil)
8. Verifikasi dialog "Report TAG" tetap terbuka

### Note hanya berisi spasi ditolak (TC-FA-TAG-1387)

9. Ganti isi Textarea "Note" dengan lima spasi saja (tanpa karakter lain)
10. Klik tombol [Submit]
11. Verifikasi pesan error "Note must not be empty" tampil pada Textarea "Note" karena isian dihitung kosong setelah trim
12. Verifikasi dialog "Report TAG" tetap terbuka
13. Verifikasi tidak ada toast sukses
14. Klik ikon close pada header dialog "Report TAG"
15. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
16. Klik [Leave]

### Note tepat 360 karakter diterima (TC-FA-TAG-1384)

17. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
18. Pilih Report Type "Damaged"
19. Isi Textarea "Note" dengan teks 360 karakter (huruf `a` diulang 360 kali)
20. Verifikasi tidak ada pesan error "Max. 360 characters" pada Textarea "Note"
21. Klik tombol [Submit]
22. Verifikasi dialog "Report TAG" menutup
23. Verifikasi toast "Success, TAG has been reported." tampil

### Note 360 karakter dengan kelebihan spasi di ujung (TC-FA-TAG-1386)

24. Atur ulang data lewat fixture backend: Tag RF-00130 tanpa laporan terbuka hingga tersimpan, lalu muat ulang halaman Task Detail
25. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
26. Pilih Report Type "Damaged"
27. Isi Textarea "Note" dengan teks 360 karakter (huruf `a` diulang 360 kali) diikuti 10 spasi di akhir
28. Verifikasi tidak ada pesan error "Max. 360 characters" karena panjang dihitung setelah trim
29. Klik tombol [Submit]
30. Verifikasi dialog "Report TAG" menutup
31. Verifikasi toast "Success, TAG has been reported." tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1384 s.d. 1387). Tidak ada TC hanya-BE.
- Urutan TC di dalam spec: TC-1385, TC-1387, TC-1384, TC-1386. Validasi yang diblokir (TC-1385 dan TC-1387) dijalankan sebelum Submit yang berhasil; TC-1387 melanjutkan dialog TC-1385 (aset dan Report Type identik). Sesudah dua laporan berhasil, `RF-00130` diatur ulang (langkah 24).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 14 sampai 16 (menutup form dirty: ikon close, `Verifikasi` dialog "Unsaved Changes", [Leave]) dan 24 (mengatur ulang state laporan lewat fixture backend; muat ulang halaman juga menghilangkan toast sebelumnya).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 21, 29). Aksi tulis pada langkah 6, 10 ditolak dan tidak menambah entri.
- Temuan untuk QA:
  - Hook suite `beforeEach` membuka Fixed Asset > TAG untuk akun aktor pertama, sedangkan Staff Auditor tanpa Manage asset & TAG tidak berhak atas halaman itu; spec ini dikecualikan di `suite.md` bagian Hook sehingga halaman yang diuji dibuka di langkahnya sendiri.
  - Panjang teks dihitung setelah trim sesuai Expected TC; nilai 360 dan 361 karakter ditulis tepat sebagai huruf `a` yang diulang tanpa suffix karena asersi bergantung pada panjang persis.
  - Post Condition TC-FA-TAG-1384 s.d. 1387 (laporan terbuka tercatat dengan Note sepanjang 360 karakter atau tidak ada laporan baru untuk RF-00130) tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
