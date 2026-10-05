---
id: TC-GS-ACTLOG-E2E-028-tab-user-action-struktur-filter-panel-dan-filter-individual
title: "Tab User Action: Struktur 4 field Filter Panel dan penerapan filter individual"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-133
  - TC-GS-ACTLOG-134
  - TC-GS-ACTLOG-135
  - TC-GS-ACTLOG-136
  - TC-GS-ACTLOG-137
coverage:
  web: automated
---

# Tab User Action: Struktur 4 field Filter Panel dan penerapan filter individual

## Prerequisites

- Login sebagai Role: Total Control pada Tab User Action dengan data changelog bervariasi Action dan Object

## Test Steps

1. Buka Tab User Action lalu klik icon Filter
2. Verifikasi struktur 4 field Filter Panel berurutan: Date, Action, Object, dan Modified By
3. Pilih satu tanggal spesifik pada field Date lalu klik `[Apply]`
4. Verifikasi hanya entri changelog pada tanggal tersebut yang tampil
5. Buka Filter, pilih Action "Create" dan "Delete" lalu klik `[Apply]`
6. Verifikasi hanya entri dengan aksi Create atau Delete yang tampil
7. Buka Filter, pilih Object "User" dan "Role & Permission" lalu klik `[Apply]`
8. Verifikasi hanya entri dari kedua object tersebut yang tampil
9. Buka Filter, pilih 2 admin pada field Modified By lalu klik `[Apply]`
10. Verifikasi hanya entri yang diubah oleh kedua admin tersebut yang tampil

## Notes

- Tab User Action hanya memiliki 4 field filter utama sesuai arsitektur data mutasi.
