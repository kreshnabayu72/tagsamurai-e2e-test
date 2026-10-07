---
id: TC-GS-DIV-E2E-077-sinkronisasi-dua-arah-dropdown-user-dan-non-login-user
title: "Sinkronisasi Real-Time Katalog Division ke Dropdown Form User dan Non-Login User (Create Muncul, Edit Reflected, Delete Terhapus)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-250
  - TC-GS-DIV-251
  - TC-GS-DIV-252
  - TC-GS-DIV-258
coverage:
  web: automated
---

# Sinkronisasi Real-Time Katalog Division ke Dropdown Form User dan Non-Login User (Create Muncul, Edit Reflected, Delete Terhapus)

## Prerequisites

- Login sebagai Role: Total Control
- Buka form Create/Edit User (user/PRD/user.md) dan Non-Login User
- User berada di Global Settings > User > Division
- Division `Metro Branch 3` (Code `MTB`) ada (TC-GS-DIV-245)
- Division `Warehouse and Distribution` ada (TC-GS-DIV-109)
- Division `Import Division A` dibuat lewat tombol `[Create Missing Divisions]` dari Import User Login (TC-GS-DIV-256)

## Test Steps

### Division baru muncul pada dropdown Division form Create User (TC-GS-DIV-250)

1. Buka Global Settings > User > Tab User List lalu klik tombol Create User
2. Buka field dropdown Division
3. Verifikasi Opsi `Metro Branch 3` tampil pada field dropdown Division form Create User
4. Verifikasi Opsi dapat dipilih

### Division baru muncul pada dropdown Division form Create Non-Login User (TC-GS-DIV-251)

5. Buka Global Settings > User > Non Login User lalu klik tombol Create Non-Login User
6. Buka field dropdown Division
7. Verifikasi Opsi `Metro Branch 3` tampil pada field dropdown Division form Create Non-Login User

### Rename Division tercermin pada dropdown Division form User (TC-GS-DIV-252)

8. Buka form Create User dan buka dropdown Division
9. Lihat opsi Division yang di-rename
10. Verifikasi Opsi tampil dengan nama `Warehouse and Distribution` dan opsi `Warehouse` tidak ada
11. Verifikasi Pada User yang memakai Division ini nama baru tampil tanpa perubahan data user

### Division hasil Create Missing Divisions tercatat sebagai Create biasa (TC-GS-DIV-258)

12. Buka Modal Changelog dan lihat entri `Import Division A`
13. Verifikasi 1 entri Action `Create` (tanpa qualifier khusus), Field `Division Name`, Old Value `—`, New Value `Import Division A`
14. Verifikasi Modified By = aktor yang mengklik tombol `[Create Missing Divisions]`

## Notes

- Memvalidasi DIV-LOGIC-03a: Division adalah referensi tunggal dropdown wajib pada User dan Non-Login User; perubahan Name/Code di Division langsung tercermin seketika (reflected via FK) pada dropdown konsumen (PRD §9.7, §11).
- Sumber pemetaan test case granular: TC-GS-DIV-250, TC-GS-DIV-251, TC-GS-DIV-252, TC-GS-DIV-258.
