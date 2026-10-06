---
id: TC-GS-ROLE-E2E-036-tabel-total-control-sorting-3-state-10-kolom
title: "Sorting 3-State (Ascending, Descending, Default) untuk Seluruh 10 Kolom Sortable Tab Total Control"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-164
  - TC-GS-ROLE-165
  - TC-GS-ROLE-166
  - TC-GS-ROLE-167
  - TC-GS-ROLE-168
  - TC-GS-ROLE-169
  - TC-GS-ROLE-170
  - TC-GS-ROLE-171
  - TC-GS-ROLE-172
coverage:
  web: automated
---

# Sorting 3-State (Ascending, Descending, Default) untuk Seluruh 10 Kolom Sortable Tab Total Control

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia minimal 3 data user dengan variasi nilai pada seluruh kolom

## Test Steps

1. Buka Global Settings > Role & Permission > Tab Total Control
2. Klik header kolom Name (klik 1) -> verifikasi data terurut A-Z (Ascending) dengan indikator panah atas
3. Klik header kolom Name (klik 2) -> verifikasi data terurut Z-A (Descending) dengan indikator panah bawah
4. Klik header kolom Name (klik 3) -> verifikasi sorting kembali ke default state
5. Ulangi siklus 3-state (Ascending, Descending, Default) berturut-turut untuk kolom: Position, Division, Status, Modified By, Last Updated, Activation Status, Temporary User, Temporary Until, dan TAG
6. Verifikasi setiap kolom merespons siklus pengurutan secara tepat tanpa saling mengganggu

## Notes

- Tab Total Control mendukung sorting 3-state pada 10 kolom data (role.md §9.10).
