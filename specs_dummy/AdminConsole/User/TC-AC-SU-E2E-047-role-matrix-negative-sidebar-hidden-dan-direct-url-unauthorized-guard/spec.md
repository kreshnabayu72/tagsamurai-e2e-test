---
id: TC-AC-SU-E2E-047-role-matrix-negative-sidebar-hidden-dan-direct-url-unauthorized-guard
title: "Role Matrix Negatif: Penolakan Sidebar Menu dan Direct URL Unauthorized Guard"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-21
  - TC-AC-SU-153
  - TC-AC-SU-154
  - TC-AC-SU-239
coverage:
  web: automated
---

# Role Matrix Negatif: Penolakan Sidebar Menu dan Direct URL Unauthorized Guard

## Prerequisites

- Pengguna terdaftar dengan peran terbatas: Akun Basic User, Akun Client, Akun Group Manager, dan Akun Read Only

## Test Steps

### Verifikasi Penolakan Sidebar Menu
1. Login sebagai akun Basic User / Client / Group Manager
2. Periksa menu sidebar navigasi
3. Verifikasi menu `Settings > User` TIDAK DITAMPILKAN sama sekali (hidden)

### Verifikasi Pencegatan Direct URL dari Address Bar
4. Ketikkan URL langsung ke halaman daftar pengguna pada address bar: `/admin-console/settings/user`
5. Verifikasi sistem mencegat navigasi dan me-redirect browser ke halaman error `403 Forbidden` atau `Unauthorized`
6. Ketikkan URL langsung ke halaman detail pengguna: `/admin-console/settings/user/detail/123`
7. Verifikasi akses ditolak dan dialihkan ke halaman unauthorized

### Verifikasi Kontrol Write Terkunci pada Mode Read Only
8. Login sebagai akun berstatus `Read Only`
9. Buka menu Settings > User
10. Verifikasi seluruh kontrol write dikunci: checkbox baris hidden, Bulk Action Bar hidden, switch Active disabled, dan tombol aksi mutasi tidak tersedia

## Notes

Menjamin pencegahan eskalasi hak akses ilegal baik melalui interaksi visual maupun navigasi langsung.
