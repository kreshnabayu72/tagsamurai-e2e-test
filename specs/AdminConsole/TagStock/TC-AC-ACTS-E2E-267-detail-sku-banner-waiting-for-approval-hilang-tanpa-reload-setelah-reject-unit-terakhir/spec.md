---
id: TC-AC-ACTS-E2E-267-detail-sku-banner-waiting-for-approval-hilang-tanpa-reload-setelah-reject-unit-terakhir
title: "Detail SKU Realtime: Banner Waiting for Approval Hilang Tanpa Reload Setelah Unit Terakhir Di-Reject"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-995
coverage:
  web: automated
---

# Detail SKU Realtime: Banner Waiting for Approval Hilang Tanpa Reload Setelah Unit Terakhir Di-Reject

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (TAG > Stock lewat sidebar). Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data Pre-setup: SKU `Fixture.tagStock.skuRfid` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Dataset milik spec di-seed fixture BE di hook `before` (idempoten) dan dipulihkan di hook `after`: satu Subject Register Duplicate pending pada SKU itu (satu unit Waiting for Approval).
- Kemampuan teknis: sesi API aktor (login API password, token tidak dihitung sebagai sesi web) untuk pelaku kedua (Admin 2) yang hanya memicu perubahan state (Reject Subject), disediakan tim FE/BE (lihat `suite.md`); aktor dan mekanisme tidak disebut di TC, PRD, atau LLD (S-13). Hasil diasersi di sesi Admin 1 (Total Control) pada halaman yang sudah terbuka tanpa memuat ulang halaman.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec), pembacaan state BE yang tidak terlihat di UI, dan sesi API aktor, disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Reset dataset: satu Subject Register Duplicate pending pada SKU `Fixture.tagStock.skuRfid` lewat fixture BE
2. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
3. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`; pastikan Tab `Available` aktif

### TC-AC-ACTS-995: Banner Waiting for Approval hilang tanpa reload setelah unit terakhir di-reject

4. Verifikasi banner `1 TAG is waiting for approval.` tampil
5. Catat Total Registered pada Summary bar dan jumlah total baris Tab Available (teks footer `Showing [From]–[To] of [Total] entries`)
6. Sesi API (Admin 2) me-Reject Subject itu dengan Approval Note terisi hingga status Rejected tersimpan
7. Amati Tab Available tanpa memuat ulang halaman
8. Verifikasi banner hilang tanpa reload
9. Verifikasi tidak ada baris baru di Tab Available (jumlah total baris sama dengan yang dicatat sebelum Reject)
10. Verifikasi Total Registered tidak berubah dari nilai yang dicatat sebelum Reject

## Notes

- Pasangan TC-AC-ACTS-991 (banner hilang setelah unit terakhir di-approve) ada di spec 160; spec ini memuat sisi Reject.
- Pelaku kedua (Admin 2) memakai sesi API aktor yang hanya memicu perubahan state dan bukan konteks UI kedua; hasil diasersi di sesi Admin 1.
- Langkah penghubung (S-03): langkah 1 (Reset dataset), langkah 2 dan 3 (Search SKU untuk menemukan baris target, R-16, dan membuka Detail SKU), dan langkah 7 (mengamati halaman tanpa reload). Langkah 4 adalah anchor positif sebelum asersi banner hilang (8b butir 2); langkah 5 adalah baseline untuk asersi tidak ada baris baru dan Total Registered tidak berubah (S-12).
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun perlu dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
  - TC-AC-ACTS-995 menyebut Admin 2 di Approvals > TAG Stock > Tab Active me-reject Subject; sesuai keputusan suite pelaku kedua yang hanya memicu perubahan state memakai sesi API aktor (disediakan tim FE/BE), bukan sesi UI kedua. TC tidak menyebut isi Approval Note; spec memakai Approval Note terisi.
