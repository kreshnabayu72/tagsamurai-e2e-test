---
id: TC-FA-FAAL-E2E-003-empty-state-kedua-tab
title: "Empty State Kedua Tab pada Client Baru"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-7
  - TC-FA-FAAL-8
coverage:
  web: automated
---

# Empty State Kedua Tab pada Client Baru

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Reports & Logs > Activity Log.
- Akun aktor: Total Control pada client baru tanpa riwayat sesi dan tanpa log aksi FAMS (Pre-setup #13). Email dan password akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini (client berbeda dari akun default suite); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: client baru Pre-setup #13 tanpa satu pun baris Tab Session maupun Tab User Action; disediakan tim FE/BE lewat seeding (butir "Seed dan pemulihan lewat API" di `suite.md`). Client tidak boleh dipakai spec lain yang menulis log.
- Flag Guided Tooltip: mengikuti butir "Flag Guided Tooltip" di `suite.md`; kemampuan men-set flag untuk akun client baru disediakan tim FE/BE.
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).

## Test Steps

### TC-FA-FAAL-7: Empty state Tab Session saat belum ada log

1. Klik tab Session
2. Verifikasi empty state tampil dengan Illustration, Title `No activity yet`, dan Description `Fixed Asset session activity — when your staff open and close access — will appear here.`
3. Verifikasi tidak ada baris tabel dan tidak ada CTA

### TC-FA-FAAL-8: Empty state Tab User Action saat belum ada log

4. Klik tab User Action
5. Verifikasi empty state tampil dengan Illustration, Title `No activity yet`, dan Description `Fixed Asset user actions and changes will appear here.`
6. Verifikasi tidak ada baris tabel dan tidak ada CTA

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 (memastikan tab Session aktif).
- Verifikasi empty state pada langkah 2 dan 5 menjadi anchor positif untuk asersi absence baris dan CTA pada langkah 3 dan 6 (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAL-7 dan 8 menyebut "Client baru" (Pre-setup #13) tanpa menyebut akun Total Control di client itu; Tabel Pre-setup hanya memuat entitas client (tidak ada baris User Actor untuk client ini).
