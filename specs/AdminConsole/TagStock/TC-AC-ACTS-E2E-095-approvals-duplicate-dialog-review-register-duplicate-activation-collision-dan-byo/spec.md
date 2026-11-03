---
id: TC-AC-ACTS-E2E-095-approvals-duplicate-dialog-review-register-duplicate-activation-collision-dan-byo
title: "Approvals Duplicate: Dialog Review Register Duplicate, Activation Collision, Client BYO Tanpa SKU, dan Label Registered by/at dari Import GPS"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-273
  - TC-AC-ACTS-274
  - TC-AC-ACTS-275
  - TC-AC-ACTS-728
coverage:
  web: automated
---

# Approvals Duplicate: Dialog Review Register Duplicate, Activation Collision, Client BYO Tanpa SKU, dan Label Registered by/at dari Import GPS

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal spec: Approvals > TAG Stock > Tab Active (dibuka langkah 1).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Data Subject pending disiapkan seeding fixture BE (disediakan tim FE/BE): Subject Register Duplicate RFID (requester Distributor), Subject Activation Collision dengan SKU `RFID-ASSET-CORE-R5` dari Client, Subject Activation Collision dari Client BYO tanpa SKU (Device Name, Brand, dan Model manual), dan Subject Register Duplicate GPS hasil Import atau Manual Entry dari requester Distributor. Spec ini tidak memutuskan Subject mana pun.
- Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-273: Dialog Review Register Duplicate, blok Existing Record dan New Request

1. Buka Approvals > TAG Stock > Tab Active
2. Klik `Review` pada Subject Type Register Duplicate RFID
3. Verifikasi dialog `Duplicate Identifier Review` dibuka (bukan halaman penuh)
4. Verifikasi header memuat icon TAG Type, badge Type, dan `Matched Identifier: [value]`
5. Verifikasi blok `Existing Record` di atas memuat TAG Code, Status, Registered by, dan Registered at
6. Verifikasi blok `New Request — Register Duplicate` di bawah memuat Entity, Scanned by, dan Scanned at
7. Verifikasi radio Approve dan Reject belum dipilih
8. Verifikasi field Approval Note tampil
9. Verifikasi footer `[Cancel]` dan `[Submit]` dengan `[Submit]` disabled
10. Klik `[Cancel]`

### TC-AC-ACTS-274: Dialog Review Activation Collision, blok New Request Client

11. Klik `Review` pada Subject Type Activation Collision
12. Verifikasi blok `Existing Record` memuat Status In Use dan Client pemegang
13. Verifikasi blok `New Request — Activation Collision` memuat Client, Device Name, SKU, dan Requested at
14. Verifikasi hanya satu blok New Request tampil
15. Klik `[Cancel]`

### TC-AC-ACTS-275: Dialog Review Client BYO tanpa SKU menampilkan SKU `—`, Brand, dan Model manual

16. Hover sel Device Name (SKU) pada Subject Activation Collision Client BYO tanpa SKU
17. Verifikasi sel menampilkan `[Device Name] (—)`
18. Verifikasi tooltip `Brand: [Brand] · Model: [Model]`
19. Klik `Review` pada Subject itu
20. Verifikasi blok New Request memuat `SKU: —`, `Brand: [Brand]`, dan `Model: [Model]`
21. Klik `[Cancel]`

### TC-AC-ACTS-728: Dialog Review Register Duplicate dari Import GPS memakai label Registered by dan Registered at

22. Klik `Review` pada Subject Register Duplicate GPS
23. Verifikasi blok `New Request — Register Duplicate` memuat baris pelaku dan waktu berlabel `Registered by` dan `Registered at`
24. Verifikasi label `Scanned by` dan `Scanned at` tidak tampil pada blok itu
25. Klik `[Cancel]`

## Notes

- Mode: FE+BE.
- Langkah penghubung tanpa Verifikasi (S-03): `[Cancel]` menutup dialog Review sebelum TC berikutnya (S-09).
- `[Value]`, `[Device Name]`, `[Brand]`, dan `[Model]` pada Expected TC adalah nilai dari Subject seeding.
- Absence label `Scanned by` dan `Scanned at` didahului anchor positif (label `Registered by` dan `Registered at` tampil pada blok yang sama; 8b butir 2).
- Temuan untuk QA:
  - TC-AC-ACTS-273 sampai TC-AC-ACTS-728 menyebut "Approvals > TAG Stock > Tab Active memuat Subject ..." tanpa nilai data Subject; spec menuliskannya sebagai kebutuhan seeding.
