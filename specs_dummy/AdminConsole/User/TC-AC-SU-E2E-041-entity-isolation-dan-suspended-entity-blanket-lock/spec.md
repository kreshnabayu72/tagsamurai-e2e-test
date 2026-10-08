---
id: TC-AC-SU-E2E-041-entity-isolation-dan-suspended-entity-blanket-lock
title: "Isolasi data antar entitas Distributor dan mode blanket lock read-only pada entitas suspended"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-40
  - TC-AC-SU-151
  - TC-AC-SU-159
coverage:
  web: automated
---

# Isolasi data antar entitas Distributor dan mode blanket lock read-only pada entitas suspended

## Prerequisites

- Akun login Distributor A Total Control, Distributor B Total Control, dan Akun Entitas Suspended

## Test Steps

### Isolasi Visibilitas Data Antar Entitas

1. Login sebagai admin Distributor A, buka User List
2. Verifikasi hanya daftar pengguna milik entitas Distributor A yang tampil (tidak ada pengguna Principal atau Distributor B yang terlihat)
3. Login sebagai admin Distributor B, buka User List
4. Verifikasi hanya pengguna milik Distributor B yang tampil, memastikan isolasi multi-tenant antar entitas

### Blanket Lock pada Entitas Suspended

1. Login sebagai admin pada entitas yang sedang di-suspend
2. Buka menu `Settings > User`, verifikasi seluruh switch Active berstatus Disabled dan Bulk Action Bar tidak memuat aksi apa pun
3. Buka menu `Settings > Role & Permission` dan `Settings > Group`
4. Verifikasi seluruh kontrol write di seluruh modul administratif terkunci (blanket read-only lock) tanpa pengecualian

## Notes

- Isolasi data multi-tenant dan penguncian total pada status suspend menjamin kepatuhan keamanan data.
