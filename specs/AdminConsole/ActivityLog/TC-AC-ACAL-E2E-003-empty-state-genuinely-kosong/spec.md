---
id: TC-AC-ACAL-E2E-003-empty-state-genuinely-kosong
title: "Empty state genuinely kosong pada Tab Session dan Tab User Action untuk entitas baru"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-08
  - TC-AC-ACAL-09
coverage:
  web: automated
---

# Empty state genuinely kosong pada Tab Session dan Tab User Action untuk entitas baru

## Prerequisites

- Login sebagai Role: Distributor Total Control pada entitas baru yang belum pernah memiliki aktivitas login staff AC maupun aksi write

## Test Steps

### Empty State Tab Session

1. Buka menu `Admin Console > Activity Log`
2. Verifikasi Tab "Session" aktif secara default
3. Verifikasi area tabel menampilkan ilustrasi empty state, judul `"No activity yet"`, dan deskripsi `"Admin Console session activity — when your staff open and close access — will appear here."`

### Empty State Tab User Action

4. Klik tab `"User Action"`
5. Verifikasi area tabel menampilkan ilustrasi empty state, judul `"No activity yet"`, dan deskripsi `"Admin console user actions and changes will appear here."`

## Notes

- Skenario ini memverifikasi pesan empty state bawaan (genuinely empty) sebelum ada aktivitas apapun tercatat pada entitas tersebut.
