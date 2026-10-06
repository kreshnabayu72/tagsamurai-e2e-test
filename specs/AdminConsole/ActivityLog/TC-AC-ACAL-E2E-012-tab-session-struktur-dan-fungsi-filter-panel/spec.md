---
id: TC-AC-ACAL-E2E-012-tab-session-struktur-dan-fungsi-filter-panel
title: "Tab Session — Screening struktur Filter Panel 4 field dan fungsi filter individual"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-46
  - TC-AC-ACAL-47
  - TC-AC-ACAL-48
  - TC-AC-ACAL-49
  - TC-AC-ACAL-50
  - TC-AC-ACAL-268
coverage:
  web: automated
---

# Tab Session — Screening struktur Filter Panel 4 field dan fungsi filter individual

## Prerequisites

- Login sebagai Role: Principal Total Control
- Tab Session terisi data dengan minimal 2 variasi User, Position, Division, dan tanggal yang berbeda

## Test Steps

### Screening Struktur Filter Panel

1. Buka menu `Admin Console > Activity Log` (Tab Session)
2. Klik tombol `[Filter]` pada toolbar
3. Verifikasi Filter Panel terbuka menampilkan tepat 4 field:
   - `Date` (Date picker dengan placeholder `"Select date"`)
   - `User` (Multi-select searchable dengan placeholder `"All users"`)
   - `Position` (Multi-select searchable dengan placeholder `"All positions"`)
   - `Division` (Multi-select searchable dengan placeholder `"All divisions"`)
4. Verifikasi tidak ada field Activity maupun Status pada Filter Panel

### Uji Filter Date & Format Input

5. Pilih satu tanggal spesifik melalui date picker
6. Verifikasi nilai tanggal di dalam input field terformat presisi mengikuti General Settings (misal `DD/MM/YY`)
7. Klik tombol `[Apply]`
8. Verifikasi tabel tersaring hanya menampilkan baris dengan Date yang dipilih

### Uji Filter User, Position, Division Individual

9. Buka kembali Filter Panel dan klik `[Clear Field]` pada field Date
10. Pilih 1 nama User pada dropdown `User`, lalu klik `[Apply]`
11. Verifikasi tabel hanya memuat entri milik User tersebut
12. Buka kembali Filter Panel, ganti filter dengan memilih 1 `Position`, lalu klik `[Apply]`
13. Verifikasi tabel hanya memuat entri dengan Position tersebut
14. Buka kembali Filter Panel, ganti filter dengan memilih 1 `Division`, lalu klik `[Apply]`
15. Verifikasi tabel hanya memuat entri dengan Division tersebut

## Notes

- Memverifikasi fungsionalitas penyaringan individual masing-masing field di Filter Panel Tab Session.
