---
id: TC-AC-SU-E2E-048-multi-tenant-data-isolation-antara-entitas-distributor
title: "Multi-Tenant Data Isolation Antara Entitas Distributor Terpisah"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-151
coverage:
  web: automated
---

# Multi-Tenant Data Isolation Antara Entitas Distributor Terpisah

## Prerequisites

- Lingkungan multi-tenant aktif
- Akun Distributor A Total Control (Tenant ID: ENT-DIST-A)
- Akun Distributor B Total Control (Tenant ID: ENT-DIST-B)
- Masing-masing entitas memiliki pengguna terdaftar tersendiri

## Test Steps

### Verifikasi Daftar Pengguna di Entitas Distributor A
1. Login sebagai Distributor A Total Control
2. Buka menu `Admin Console > Settings > User`
3. Catat daftar nama dan email seluruh pengguna yang tampil pada tabel (User List Distributor A)

### Verifikasi Isolasi Total di Entitas Distributor B
4. Buka sesi browser baru dan login sebagai Distributor B Total Control
5. Buka menu `Admin Console > Settings > User`
6. Verifikasi secara tegas bahwa TIDAK ADA SATUPUN pengguna atau data email milik Distributor A yang muncul pada tabel Distributor B
7. Coba lakukan pencarian nama pengguna milik Distributor A pada toolbar search Distributor B
8. Verifikasi hasil pencarian mengembalikan status `"No matching users found"`

### Pencegahan Akses Lintas Entitas via Direct API
9. Lakukan request API langsung untuk mengambil detail pengguna Distributor A menggunakan token otorisasi Distributor B
10. Verifikasi backend mengembalikan status error `404 Not Found` atau `403 Forbidden` (Zero data leakage)

## Notes

Memastikan isolasi batas data antar tenant distributor terpenuhi tanpa celah kebocoran informasi.
