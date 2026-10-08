---
id: TC-AC-ACAL-E2E-034-tab-user-action-setup-column-pin-sticky-reset-dan-cancel
title: "Tab User Action — Pin freeze kolom sticky, Reset to Default, Cancel Discard, dan isolasi cache"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-192
  - TC-AC-ACAL-193
  - TC-AC-ACAL-194
  - TC-AC-ACAL-195
  - TC-AC-ACAL-196
  - TC-AC-ACAL-197
  - TC-AC-ACAL-198
  - TC-AC-ACAL-199
  - TC-AC-ACAL-200
  - TC-AC-ACAL-201
  - TC-AC-ACAL-202
coverage:
  web: automated
---

# Tab User Action — Pin freeze kolom sticky, Reset to Default, Cancel Discard, dan isolasi cache

## Prerequisites

- Login sebagai Role: Principal Total Control
- Pengguna berada di `Admin Console > Activity Log` (Tab User Action)

## Test Steps

### Pin / Freeze Kolom Sticky

1. Klik header kolom `⋯` > klik `"Setup Column"`
2. Klik icon Pin pada kolom `Date` dan `Action`
3. Klik tombol `[Save]`
4. Geser (scroll) tabel Tab User Action secara horizontal ke kanan
5. Verifikasi kolom Date dan Action tetap membeku (freeze/sticky) di sisi kiri saat kolom lain bergeser
6. Refresh browser (F5) dan verifikasi status freeze tetap aktif

### Cancel / Discard Perubahan

7. Buka kembali Setup Column modal
8. Uncheck kolom `Modified By` dan ubah urutan kolom
9. Klik tombol `[Cancel]`
10. Verifikasi modal tertutup dan perubahan konfigurasi dibatalkan

### Reset to Default & Isolasi Cache Antar Tab

11. Buka kembali Setup Column modal
12. Klik tombol `[Reset to Default]`
13. Verifikasi konfigurasi di Live Preview kembali ke urutan, visibilitas, dan status unpin default
14. Klik `[Save]`
15. Verifikasi tabel Tab User Action kembali normal ke format default
16. Klik tab `"Session"`
17. Verifikasi konfigurasi kolom pada Tab Session tidak terpengaruh oleh aksi pada Tab User Action (isolasi cache storage)

## Notes

- Memverifikasi isolasi key storage konfigurasi tabel Tab User Action vs Tab Session.
