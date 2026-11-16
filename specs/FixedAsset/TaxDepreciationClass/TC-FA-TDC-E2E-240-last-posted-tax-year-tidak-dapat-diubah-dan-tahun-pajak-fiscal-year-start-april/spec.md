---
id: TC-FA-TDC-E2E-240-last-posted-tax-year-tidak-dapat-diubah-dan-tahun-pajak-fiscal-year-start-april
title: "Last Posted Tax Year Tidak Dapat Diubah dari UI dan Dicatat sebagai Tahun Kalender Awal Tahun Pajak (Fiscal Year Start April)"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-358
  - TC-FA-TDC-359
sourceRules: ["§4.1.2#r11", "§9.9#r10", "ST-07", "FATDC-LOGIC-03a.3", "§4.2c#b1", "FATDC-LOGIC-04v", "F-FATDC-11.k1a"]
smoke: []
dependsOn: []
trace:
  "§4.1.2#r11": 3
  "§9.9#r10": [3, 5]
  "ST-07": 6
  "FATDC-LOGIC-03a.3": 6
  "§4.2c#b1": 8
  "FATDC-LOGIC-04v": 14
  "F-FATDC-11.k1a": 14
coverage:
  web: automated
---

# Last Posted Tax Year Tidak Dapat Diubah dari UI dan Dicatat sebagai Tahun Kalender Awal Tahun Pajak (Fiscal Year Start April)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`. Hook, sesi API aktor, seed dan pemulihan lewat API, dan flag Guided Tooltip mengikuti `suite.md`.
- Kemampuan teknis: memicu posting penyusutan fiskal untuk tahun pajak tertentu pada class lewat fixture BE (job J-03; Depreciation Run belum tersedia; disediakan tim FE/BE, mekanismenya tidak disebut TC, S-13); mengatur Fiscal Year Start lewat seeding API (langkah 10) dan memulihkannya ke Januari di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; Active, Non-building, Used By 0): `KHS-LP6-{runId}-240` (Last Posted Tax Year `2026`, TC-358) dan `KHS-LP7-{runId}-240` (Last Posted Tax Year kosong, TC-359). Baris `KHS-*` berada di halaman pertama sehingga dibuka tanpa Search.
- State global: Fiscal Year Start April untuk TC-359 (langkah 10), dipulihkan ke Januari di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-358: Last Posted Tax Year tidak dapat dikosongkan atau diubah dari UI

1. Klik link Class Code `KHS-LP6-{runId}-240` pada tabel
2. Coba ketik pada Last Posted Tax Year
3. Verifikasi field Last Posted Tax Year tidak menerima input; nilai tetap "2026"
4. Klik `[Clear Field]`
5. Verifikasi Last Posted Tax Year tetap "2026"
6. Verifikasi Asset Type tetap Disabled
7. Klik `[×]` pada header Drawer
8. Verifikasi dialog `Unsaved Changes` tampil
9. Klik `[Leave]`

### TC-FA-TDC-359: Tahun pajak dicatat sebagai tahun kalender awal tahun pajak (Fiscal Year Start April)

10. Atur Fiscal Year Start menjadi April lewat seeding API, lalu muat ulang halaman
11. Picu posting penyusutan fiskal untuk tahun pajak yang dimulai 1 Apr 2026 (berakhir 31 Mar 2027) pada `KHS-LP7-{runId}-240` lewat fixture BE (J-03)
12. Muat ulang halaman
13. Klik link Class Code `KHS-LP7-{runId}-240` pada tabel
14. Verifikasi Last Posted Tax Year bernilai "2026"
15. Klik `[×]` pada header Drawer

## Notes

- Langkah penghubung (S-03): langkah 7 sampai 9 (menutup Drawer yang dirty karena `[Clear Field]`, S-08; `Verifikasi` dialog `Unsaved Changes` wajib menurut S-08 dan tidak dicatat lagi), langkah 10 (pembentuk precondition c TC-359, tidak diasersi), langkah 12 (muat ulang agar nilai dari fixture BE terbaca), dan langkah 15 (menutup Drawer tanpa perubahan, tanpa dialog `Unsaved Changes`).
- Posting penyusutan fiskal (job J-03) lewat fixture BE hanya memicu kondisi yang diuji dan bukan objek asersi; yang diasersi adalah nilai Last Posted Tax Year yang tampil di Drawer (langkah 14).
- Langkah 10 mengatur Fiscal Year Start lewat seeding API karena tidak ada versi ber-Effective From pada company (TC-359 tidak menyebut caranya); pengaturan lewat Settings > Accounting > Preferences ada di spec 094.
- Post Condition TC-359 (entri L-10: Old Value "—", New Value "2026") tidak punya langkah observasi di TC; tidak diasersi di spec ini (S-01). Pencatatan L-10 ada di spec 096.
- Temuan untuk QA:
  - TC-358 Expected b ("Asset Type tetap Disabled") bergantung `[Clear Field]` mengosongkan field lain pada Drawer; TC tidak menyebut state field lain setelah `[Clear Field]`, dan Drawer menjadi dirty sehingga ditutup dengan `[Leave]` (S-08).
  - Post Condition TC-359 tanpa langkah observasi di TC.
  - TC-359 tidak menyebut cara mengatur Fiscal Year Start April; spec memakai seeding API.
  - `KHS-LP6` dan `KHS-LP7` tanpa suffix di TC; spec memakai `-{runId}-240` (S-12).
  - Email akun Total Control tidak tertulis di TC.
