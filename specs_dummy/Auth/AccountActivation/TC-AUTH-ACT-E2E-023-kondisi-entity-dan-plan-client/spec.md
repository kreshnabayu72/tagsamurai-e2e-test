---
id: TC-AUTH-ACT-E2E-023-kondisi-entity-dan-plan-client
title: "Kondisi Client dan plan tidak memengaruhi alur Set Password dan Activation Success"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-ACT-110
  - TC-AUTH-ACT-111
  - TC-AUTH-ACT-112
coverage:
  web: automated
---

# Kondisi Client dan plan tidak memengaruhi alur Set Password dan Activation Success

## Prerequisites

- Browser publik tanpa sesi login.
- 4 user seeding milik automation berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run), masing-masing dengan kondisi prasyarat berbeda:
  - User A: Default User dari Client berstatus Suspended.
  - User B: Default User dari Client berstatus Expired.
  - User C: Default User dari Client plan Starter.
  - User D: Default User dari Client plan Enterprise.
- Akses API read-only untuk memverifikasi status user (Activated) dan status Client masing-masing sebelum serta sesudah tiap aktivasi.
- Hook `after` membersihkan seluruh user beserta Client seed.

## Test Steps

### Client Suspended: aktivasi tetap berjalan (TC-AUTH-ACT-110)

1. Buka link aktivasi user A → halaman `Auth > Account Activation > Set Password` tampil normal (tidak ada halaman Invalid Link).
2. Ketik `Aman#Sandi8` pada field Password dan `Aman#Sandi8` pada field Confirm Password.
3. Klik button "Set Password".
4. Verifikasi halaman Activation Success tampil dengan Title "Account Activated".
5. Verifikasi via API bahwa status user A Activated dan status Client tetap Suspended (pembatasan berlaku saat login, bukan saat aktivasi).

### Client Expired: aktivasi tetap berjalan (TC-AUTH-ACT-111)

6. Buka link aktivasi user B → halaman Set Password tampil normal.
7. Ketik `Aman#Sandi8` pada kedua field, lalu klik button "Set Password".
8. Verifikasi halaman Activation Success tampil dengan Title "Account Activated".
9. Verifikasi via API bahwa status user B Activated dan status Client tetap Expired (pembatasan berlaku saat login, bukan saat aktivasi).

### Plan Starter dan Enterprise menghasilkan alur identik (TC-AUTH-ACT-112)

10. Buka link aktivasi user C (Client plan Starter) → halaman Set Password tampil.
11. Ketik `Aman#Sandi8` pada kedua field, lalu klik button "Set Password".
12. Verifikasi halaman Activation Success tampil dengan Title "Account Activated" tanpa batasan atau pesan upsell.
13. Buka link aktivasi user D (Client plan Enterprise) → halaman Set Password tampil.
14. Ketik `Aman#Sandi8` pada kedua field, lalu klik button "Set Password".
15. Verifikasi halaman Activation Success tampil dengan Title "Account Activated" yang sama persis dengan hasil pada plan Starter, tanpa batasan atau pesan upsell yang berbeda.
16. Verifikasi via API bahwa status kedua user Activated.

## Notes

- Screening dilakukan pada blok pertama; seluruh blok mengonsumsi token user masing-masing sehingga urutan bebas dari dependensi.
- Semua kebutuhan kondisi Client/plan (Suspended, Expired, Starter, Enterprise) dicatat di Prerequisites agar tim FE menyiapkan seed-nya.
