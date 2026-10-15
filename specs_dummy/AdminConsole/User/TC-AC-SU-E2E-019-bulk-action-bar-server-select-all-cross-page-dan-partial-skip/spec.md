---
id: TC-AC-SU-E2E-019-bulk-action-bar-server-select-all-cross-page-dan-partial-skip
title: "Bulk Action Bar Server Select All Lintas Halaman dan Partial Skip User Non-Eligible"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-214
  - TC-AC-SU-249
coverage:
  web: automated
---

# Bulk Action Bar Server Select All Lintas Halaman dan Partial Skip User Non-Eligible

## Prerequisites

- Login sebagai Total Control
- Dataset pengguna lebih dari 1 halaman (minimal 25 user terdistribusi dalam 3 halaman)
- Terdapat 2 akun non-eligible (Default User dan isActiveGlobal=false)

## Test Steps

### Aktivasi Server Select All Lintas Halaman
1. Buka `Admin Console > Settings > User`
2. Centang checkbox pada header tabel (Master Checkbox)
3. Verifikasi seluruh baris pada halaman 1 tercentang dan muncul banner: `"All 10 users on this page are selected. Select all 25 users in system"`
4. Klik tautan teks `"Select all 25 users in system"`
5. Verifikasi teks banner berubah menjadi: `"All 25 users in system are selected. Clear selection"`

### Eksekusi Batch dan Partial Skip
6. Klik tombol `[Deactivate User]` pada Bulk Action Bar
7. Verifikasi dialog konfirmasi menampilkan ringkasan jumlah target dan peringatan partial skip untuk akun terlindungi
8. Klik tombol konfirmasi `[Deactivate]`
9. Verifikasi toast menampilkan: `"23 users deactivated successfully. 2 protected users were skipped."`
10. Pindah ke halaman 2 dan 3; verifikasi status user yang eligible telah berubah menjadi Inactive sedangkan akun terproteksi tetap Active

## Notes

Memverifikasi eksekusi skala besar lintas halaman serta mekanisme perlindungan integritas akun.
