---
id: TC-GS-POS-E2E-049-security-isolasi-entitas-multi-tenant
title: "State Tenant: Isolasi entitas — Position milik Client Lain tidak terlihat di tabel entitas aktif"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-267
coverage:
  web: automated
---

# State Tenant: Isolasi entitas — Position milik Client Lain tidak terlihat di tabel entitas aktif

## Prerequisites

- Dua entitas: Client A (entitas aktif) dan Client B (Client Lain)
- Client B memiliki record Position unik "Regional Sales Lead" (Pre-setup No. 19)

## Test Steps

### Uji Isolasi Data Multi-Tenant

1. Login ke akun Client A
2. Buka Global Settings > User > Position
3. Cari kata kunci "Regional Sales Lead" pada input Search tabel
4. Verifikasi hasil pencarian "No results found" (data Client B tidak bocor ke Client A)
5. Buka Popup Changelog pada Client A, cari "Regional Sales Lead"
6. Verifikasi riwayat Client B tidak muncul di Changelog Client A
7. Buka form Create User pada Client A, periksa dropdown Position
8. Verifikasi "Regional Sales Lead" tidak terdapat di dropdown opsi

## Notes

- Menguji isolasi data multi-tenant (TC-GS-POS-267) dalam kelas State Tenant.
