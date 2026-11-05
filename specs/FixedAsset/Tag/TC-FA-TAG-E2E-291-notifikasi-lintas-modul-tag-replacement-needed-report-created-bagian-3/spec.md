---
id: TC-FA-TAG-E2E-291-notifikasi-lintas-modul-tag-replacement-needed-report-created-bagian-3
title: "Notifikasi Lintas Modul: Notifikasi Laporan Ditandai Terbaca setelah Laporan Ditutup"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1254
coverage:
  web: automated
---

# Notifikasi Lintas Modul: Notifikasi Laporan Ditandai Terbaca setelah Laporan Ditutup

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Budi S. (pemegang Update di group Plant B) tidak tertulis di Tabel Pre-setup TC; disediakan tim FE.
- Akun aktor: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Dipakai sebagai pelaku kedua lewat sesi API (Decline Report).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE, lihat `suite.md`); langkah pemicunya tidak memuat asersi di sesi itu.
- Data (Pre-setup TC, tanpa suffix): aset AST-0020 ('Excavator 20 Ton - 20', Plant B) dengan Tag tunggal `RF-00130` dan laporan terbuka Damaged dari Staff Auditor; notifikasi "TAG reported" RF-00130 yang belum dibaca milik Budi S. (precondition TC, tidak diasersi).
- Kemampuan teknis (disediakan tim FE/BE): membaca status notifikasi tiap akun.
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog `Decline Report` per Tag (langkah 2).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan TAG Type Asset Name, aset, Tag, laporan, dan sesi ke akun default suite lewat fixture backend.
- State global yang diubah spec ini: status laporan Tag RF-00130 dan status baca notifikasi. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1254: notifikasi laporan ditandai terbaca otomatis setelah laporan ditutup

1. Siapkan lewat fixture backend: laporan terbuka Damaged dari Staff Auditor pada Tag RF-00130 (AST-0020, Plant B) dan notifikasi "TAG reported" RF-00130 yang belum dibaca untuk Budi S.
2. Pelaku kedua (Total Control) lewat sesi API melakukan Decline Report pada laporan itu dengan Reason "Tag masih terbaca" hingga tersimpan
3. Muat ulang halaman
4. Buka dropdown notifikasi
5. Verifikasi notifikasi "TAG reported" RF-00130 berstatus sudah dibaca

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 1 dan 3 (menyiapkan laporan dan notifikasi lewat fixture, memuat ulang halaman).
- Pemicu memakai pelaku kedua lewat sesi API karena hanya memicu penutupan laporan dan tidak diasersi di sesinya (R-20).
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Decline Report` per Tag (langkah 2).
- Temuan untuk QA:
  - TC-FA-TAG-1254 langkah TC ke-7 ('Login sbg Budi S.') adalah pengamat; spec memakai sesi UI Budi S. sejak hook `before` dan memicu Decline Report lewat sesi API.
