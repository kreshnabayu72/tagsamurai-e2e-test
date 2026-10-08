---
id: TC-AC-SU-E2E-038-tab-role-banner-tier-total-control-read-only-group-manager
title: "Banner Indikator Tier pada Tab Role (Total Control, Read Only, Group Manager)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-102
  - TC-AC-SU-103
  - TC-AC-SU-104
  - TC-AC-SU-105
coverage:
  web: automated
---

# Banner Indikator Tier pada Tab Role (Total Control, Read Only, Group Manager)

## Prerequisites

- Login sebagai Total Control
- Terdapat 3 akun dengan tingkatan tier berbeda: Akun Total Control, Akun Read Only, dan Akun Group Manager

## Test Steps

### Screening Banner Tier Total Control
1. Buka Detail User untuk user dengan tier `Total Control` > buka tab `Role`
2. Verifikasi banner warna khusus muncul di bagian atas tab: `"This user has Total Control access across all features."`
3. Verifikasi seluruh kontrol toggle role individual dalam kondisi tersembunyi atau locked

### Screening Banner Tier Read Only dan Group Manager
4. Buka Detail User untuk user dengan tier `Read Only` > buka tab `Role`
5. Verifikasi banner tier menampilkan: `"This user has Read Only access across all features."`
6. Buka Detail User untuk user dengan tier `Group Manager` > buka tab `Role`
7. Verifikasi banner tier menampilkan: `"This user has Group Manager tier access."`

### Verifikasi Ketiadaan Kontrol Mutasi Tier di Settings User
8. Periksa seluruh komponen pada halaman `Admin Console > Settings > User`
9. Verifikasi TIDAK ADA tombol atau dropdown untuk mengubah tier akun (Tier dikelola terpusat di Global Settings)

## Notes

Memastikan segregasi pengelolaan tier dan visualisasi status kepemilikan hak akses.
