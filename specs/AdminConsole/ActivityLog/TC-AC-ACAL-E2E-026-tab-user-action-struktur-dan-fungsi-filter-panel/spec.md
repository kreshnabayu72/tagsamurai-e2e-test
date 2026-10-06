---
id: TC-AC-ACAL-E2E-026-tab-user-action-struktur-dan-fungsi-filter-panel
title: "Tab User Action — Screening struktur Filter Panel 4 field dan fungsi filter individual"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-138
  - TC-AC-ACAL-139
  - TC-AC-ACAL-140
  - TC-AC-ACAL-141
  - TC-AC-ACAL-142
  - TC-AC-ACAL-272
coverage:
  web: automated
---

# Tab User Action — Screening struktur Filter Panel 4 field dan fungsi filter individual

## Prerequisites

- Login sebagai Role: Principal Total Control
- Tab User Action terisi data dengan variasi Action, Object, Modified By, dan tanggal yang berbeda

## Test Steps

### Screening Struktur Filter Panel

1. Buka menu `Admin Console > Activity Log` > klik tab `"User Action"`
2. Klik tombol `[Filter]` pada toolbar
3. Verifikasi Filter Panel terbuka menampilkan tepat 4 field:
   - `Date` (Date picker dengan placeholder `"Select date"`)
   - `Action` (Multi-select searchable dengan placeholder `"All actions"`)
   - `Object` (Multi-select searchable dengan placeholder `"All objects"`)
   - `Modified By` (Multi-select searchable dengan placeholder `"All modified by"`)

### Uji Filter Date & Format Input

4. Pilih satu tanggal spesifik melalui date picker
5. Verifikasi nilai tanggal di dalam input field terformat presisi mengikuti General Settings (misal `DD/MM/YY`)
6. Klik tombol `[Apply]`
7. Verifikasi tabel tersaring hanya menampilkan baris dengan Date yang dipilih

### Uji Filter Action, Object, Modified By Individual

8. Buka kembali Filter Panel dan klik `[Clear Field]` pada field Date
9. Pilih 1 tipe `Action` (contoh: `"Create"`), lalu klik `[Apply]`
10. Verifikasi tabel hanya memuat entri dengan Action Create
11. Buka kembali Filter Panel, ganti filter dengan memilih 1 `Object` (contoh: `"Client"`), lalu klik `[Apply]`
12. Verifikasi tabel hanya memuat entri dengan Object Client
13. Buka kembali Filter Panel, ganti filter dengan memilih 1 `Modified By`, lalu klik `[Apply]`
14. Verifikasi tabel hanya memuat entri yang dimodifikasi oleh user tersebut

## Notes

- Memverifikasi fungsionalitas penyaringan individual masing-masing field di Filter Panel Tab User Action.
