---
id: TC-GS-DIV-E2E-081-security-penegakan-izin-server-side-dan-guard-in-use-api
title: "Penegakan Izin Server-Side Tanpa Capability (Create, Edit, Delete Ditolak 403) dan Guard In-Use Server-Side pada Permintaan API Langsung"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-259
  - TC-GS-DIV-260
  - TC-GS-DIV-261
  - TC-GS-DIV-262
coverage:
  web: automated
---

# Penegakan Izin Server-Side Tanpa Capability (Create, Edit, Delete Ditolak 403) dan Guard In-Use Server-Side pada Permintaan API Langsung

## Prerequisites

- Login sebagai Role: Read Only, Create-Only, Update-Only, Total Control
- Token sesi dari akun dengan hak terbatas (Read Only, Create-Only, Update-Only)
- Akses langsung request API POST/PATCH/DELETE /divisions

## Test Steps

### Request Create langsung tanpa capability Create ditolak server (TC-GS-DIV-259)

1. Login sbg Read Only lalu tangkap token sesi
2. Kirim request Create Division langsung ke server dengan token tersebut tanpa lewat UI
3. Verifikasi Server menolak dengan `403 Forbidden`
4. Verifikasi Division tidak dibuat

### Request Edit langsung tanpa capability Update ditolak server (TC-GS-DIV-260)

5. Login sbg Create-Only lalu tangkap token sesi
6. Kirim request Edit Division `Finance` langsung ke server
7. Verifikasi Server menolak dengan `403 Forbidden`
8. Verifikasi Name `Finance` tidak berubah

### Request Delete langsung tanpa capability Delete ditolak server (TC-GS-DIV-261)

9. Login sbg Update-Only lalu tangkap token sesi
10. Kirim request Delete Division `Finance` langsung ke server
11. Verifikasi Server menolak dengan `403 Forbidden`
12. Verifikasi Division `Finance` tetap ada

### Request Delete Division in-use langsung ke server tetap ditolak guard (TC-GS-DIV-262)

13. Login sbg Total Control lalu tangkap token sesi
14. Kirim request Delete Division `Human Resources` (in-use) langsung ke server tanpa lewat UI
15. Verifikasi Server menolak penghapusan karena Division masih dipakai user
16. Verifikasi Division `Human Resources` tetap ada

## Notes

- Memvalidasi defense-in-depth (§9.3, prd-conventions.md §18.6): server secara mandiri menolak permintaan tulis tanpa capability dengan status 403 Forbidden, dan guard in-use tetap ditegakkan di server pada pemanggilan DELETE langsung.
- Sumber pemetaan test case granular: TC-GS-DIV-259, TC-GS-DIV-260, TC-GS-DIV-261, TC-GS-DIV-262.
