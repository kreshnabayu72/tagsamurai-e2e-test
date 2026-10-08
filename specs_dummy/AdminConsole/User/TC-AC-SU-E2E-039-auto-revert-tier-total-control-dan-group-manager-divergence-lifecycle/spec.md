---
id: TC-AC-SU-E2E-039-auto-revert-tier-total-control-dan-group-manager-divergence-lifecycle
title: "Siklus Auto-Revert Tier Total Control dan Group Manager Saat Konfigurasi Role Menyimpang"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-70
  - TC-AC-SU-107
  - TC-AC-SU-108
  - TC-AC-SU-110
  - TC-AC-SU-112
  - TC-AC-SU-262
  - TC-AC-SU-290
coverage:
  web: automated
---

# Siklus Auto-Revert Tier Total Control dan Group Manager Saat Konfigurasi Role Menyimpang

## Prerequisites

- Login sebagai Total Control
- Target user terdaftar dengan tier Total Control atau Group Manager

## Test Steps

### Pemicuan Divergensi Izin dan Dialog Konfirmasi Auto-Revert
1. Buka Detail User target berstatus tier `Total Control` > tab `Role`
2. Coba lakukan mutasi individual pada salah satu sub-fitur atau cabang izin
3. Verifikasi dialog peringatan divergensi tier muncul: `"Modifying specific permissions will cause this user to lose Total Control tier status and revert to Custom Role. Do you wish to continue?"`
4. Klik tombol `[Cancel]`; verifikasi tidak ada izin yang berubah dan banner tier tetap utuh

### Konfirmasi Mutasi dan Pelepasan Tier
5. Lakukan mutasi kembali dan klik tombol konfirmasi `[Confirm]` pada dialog
6. Verifikasi izin khusus berhasil disimpan
7. Verifikasi banner tier Total Control terlepas seketika dari tampilan
8. Verifikasi status akun pengguna beralih menjadi `Custom Role`
9. Verifikasi event auto-revert tier ini tercatat secara presisi pada tab `Changelog`

## Notes

Menjaga kepatuhan aturan bisnis auto-revert saat hak akses tier disesuaikan secara granular.
