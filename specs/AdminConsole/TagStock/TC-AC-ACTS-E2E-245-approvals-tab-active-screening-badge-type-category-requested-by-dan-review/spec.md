---
id: TC-AC-ACTS-E2E-245-approvals-tab-active-screening-badge-type-category-requested-by-dan-review
title: "Approvals Tab Active: Screening, Satu Tabel Dua Type, Sel Device Name dan Category BYO Tanpa SKU, Requested By, Row Action Review, dan Subject Canceled Tidak Tampil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-566
  - TC-AC-ACTS-567
  - TC-AC-ACTS-568
  - TC-AC-ACTS-569
  - TC-AC-ACTS-570
  - TC-AC-ACTS-571
  - TC-AC-ACTS-572
coverage:
  web: automated
---

# Approvals Tab Active: Screening, Satu Tabel Dua Type, Sel Device Name dan Category BYO Tanpa SKU, Requested By, Row Action Review, dan Subject Canceled Tidak Tampil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Halaman kerja spec ini adalah Approvals > TAG Stock, dibuka oleh langkah 1 dan 2.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `canceledSubjectId` = Matched Identifier Subject Activation Collision yang berstatus Canceled (seed fixture BE); `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Approvals > TAG Stock > Tab Active: sedikitnya 5 Subject Register Duplicate dan Activation Collision dengan sedikitnya dua nilai distinct pada tiap kolom (SKU `Fixture.tagStock.skuRfid`, Existing Record `TAG-4F7K2XQ9`, Requested By `PT Principal Utama (Principal)`, `PT Maju Bersama (Distributor)`, dan `PT ABC Logistics (Client)`, serta satu Subject Client BYO tanpa SKU). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Data seed tambahan: Subject Activation Collision yang Canceled oleh event Delete TAG (`Fixture.tagStock.canceledSubjectId`) berada di Tab History, bukan Tab Active.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Approvals > TAG Stock lewat sidebar
2. Klik Tab `Active`

### TC-AC-ACTS-566: Screening halaman Approvals > TAG Stock dengan Tab Active default

3. Verifikasi breadcrumb `Approvals > TAG Stock` tampil sebagai dua segmen statis yang tidak bisa diklik
4. Verifikasi Tab `Active` dan `History` tampil dengan `Active` terpilih
5. Verifikasi toolbar memuat Search, Filter, Download
6. Klik (⋯) pada satu baris Tab Active, klik `Review`
7. Verifikasi Detail Approval dibuka sebagai Dialog (bukan halaman penuh)
8. Tutup Dialog Detail Approval dengan Esc

### TC-AC-ACTS-567: Satu tabel menampung dua Type dengan badge berbeda

9. Verifikasi badge Type Register Duplicate tampil dengan severity primary
10. Verifikasi badge Type Activation Collision tampil dengan severity warning

### TC-AC-ACTS-568: Sel Device Name (SKU) Client BYO tanpa SKU menampilkan `(—)` dan tooltip Brand/Model

11. Hover sel Device Name (SKU) pada baris Subject BYO tanpa SKU
12. Verifikasi sel menampilkan `[Device Name] (—)`
13. Verifikasi tooltip menampilkan `Brand: [Brand] · Model: [Model]`

### TC-AC-ACTS-569: Sel Category Subject BYO tanpa SKU menampilkan `[TAG Type] - —`

14. Verifikasi sel Category baris Subject BYO tanpa SKU menampilkan `RFID - —` (TAG Type terisi, bagian Type `—`)
15. Klik icon Filter, buka dropdown `Category`
16. Verifikasi opsi filter Category memuat `RFID - —`
17. Tutup dropdown `Category` dengan Esc, lalu tutup panel Filter

### TC-AC-ACTS-570: Requested By ditulis `[nama entitas] ([tipe])`, Principal tidak pernah bare

18. Verifikasi kolom Requested By memuat `PT Principal Utama (Principal)`
19. Verifikasi kolom Requested By memuat `PT Maju Bersama (Distributor)`
20. Verifikasi kolom Requested By memuat `PT ABC Logistics (Client)`

### TC-AC-ACTS-571: Row action Review tampil untuk viewer yang bisa membuka menu

21. Klik (⋯) pada satu baris Tab Active
22. Verifikasi row action `Review` tampil
23. Klik `Review`
24. Verifikasi Dialog Detail Approval terbuka (sesuai Deviasi PRD)
25. Tutup Dialog Detail Approval dengan Esc

### TC-AC-ACTS-572: Subject yang Canceled tidak lagi tampil di Tab Active

26. Muat ulang halaman (F5)
27. Klik Tab `Active`
28. Verifikasi sedikitnya satu baris Subject lain tampil pada Tab Active
29. Ketik Search `Fixture.tagStock.canceledSubjectId`, tekan Enter
30. Verifikasi Subject Activation Collision yang Canceled tidak ada di Tab Active (empty state `No results found`)
31. Klik `(←)` pada kotak Search
32. Klik Tab `History`
33. Ketik Search `Fixture.tagStock.canceledSubjectId`, tekan Enter
34. Verifikasi Subject yang Canceled pindah ke Tab History
35. Klik `(←)` pada kotak Search
36. Klik Tab `Active`

## Notes

- Langkah penghubung (S-03): langkah 1 dan 2 membuka Approvals > TAG Stock dan Tab `Active`; tidak ada `Verifikasi` karena hanya menyiapkan halaman kerja.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay; menutup kotak Search lewat `(←)`.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Alasan di atas sekitar 35 langkah: spec ini 36 langkah dihitung dengan ekspansi; semua blok membaca satu halaman Approvals Tab Active dengan satu dataset seed dan berdiri sendiri; jumlah langkah berasal dari `Verifikasi` per klausa Expected (S-01).
- Temuan untuk QA (S-15):
