---
id: TC-AC-ACAL-E2E-020-tab-session-setup-column-pin-sticky-reset-dan-cancel
title: "Tab Session — Pin freeze kolom sticky, Reset to Default, Cancel Discard, dan isolasi cache antar tab"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-105
  - TC-AC-ACAL-106
  - TC-AC-ACAL-107
  - TC-AC-ACAL-108
  - TC-AC-ACAL-109
  - TC-AC-ACAL-110
  - TC-AC-ACAL-111
  - TC-AC-ACAL-112
  - TC-AC-ACAL-113
  - TC-AC-ACAL-114
  - TC-AC-ACAL-115
  - TC-AC-ACAL-116
  - TC-AC-ACAL-117
coverage:
  web: automated
---

# Tab Session — Pin freeze kolom sticky, Reset to Default, Cancel Discard, dan isolasi cache antar tab

## Prerequisites

- Login sebagai Role: Principal Total Control
- Pengguna berada di `Admin Console > Activity Log` (Tab Session)

## Test Steps

### Pin / Freeze Kolom Sticky

1. Klik header kolom `⋯` > klik `"Setup Column"`
2. Klik icon Pin pada kolom `Date` dan `User`
3. Klik tombol `[Save]`
4. Geser (scroll) tabel Tab Session secara horizontal ke kanan
5. Verifikasi kolom Date dan User tetap membeku (freeze/sticky) di sisi kiri saat kolom lain bergeser
6. Refresh browser (F5) dan verifikasi status freeze tetap aktif

### Cancel / Discard Perubahan

7. Buka kembali Setup Column modal
8. Uncheck kolom `IP Address` dan ganti urutan kolom
9. Klik tombol `[Cancel]`
10. Verifikasi modal tertutup dan perubahan konfigurasi dibatalkan (kolom IP Address tetap tampil dan urutan tidak berubah)

### Reset to Default & Isolasi Cache Antar Tab

11. Buka kembali Setup Column modal
12. Klik tombol `[Reset to Default]`
13. Verifikasi konfigurasi di Live Preview kembali ke urutan, visibilitas, dan status unpin default
14. Klik `[Save]`
15. Verifikasi tabel Tab Session kembali normal ke format default
16. Klik tab `"User Action"`
17. Verifikasi konfigurasi kolom pada Tab User Action tidak terpengaruh oleh perubahan pada Tab Session (cache konfigurasi terisolasi per tabel)

## Notes

- Konfigurasi Setup Column disimpan terpisah per tabel (isolasi key storage).
