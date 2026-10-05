---
id: TC-GS-ACTLOG-E2E-011-tab-session-search-per-kolom-dan-guard-date
title: "Tab Session: Pencarian per kolom untuk 9 kolom teks dan guard Date tidak searchable"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-31
  - TC-GS-ACTLOG-32
  - TC-GS-ACTLOG-33
  - TC-GS-ACTLOG-34
  - TC-GS-ACTLOG-35
  - TC-GS-ACTLOG-36
  - TC-GS-ACTLOG-37
  - TC-GS-ACTLOG-38
  - TC-GS-ACTLOG-39
  - TC-GS-ACTLOG-40
coverage:
  web: automated
---

# Tab Session: Pencarian per kolom untuk 9 kolom teks dan guard Date tidak searchable

## Prerequisites

- Login sebagai Role: Total Control
- Tab Session memuat entri dengan variasi data User, Employee ID, Position, Division, Activity, Status, Note, IP Address, dan Device/Browser

## Test Steps

1. Buka Tab Session
2. Masukkan substring nama User pada search box lalu tekan Enter, dan verifikasi entri yang cocok ditampilkan secara case-insensitive
3. Masukkan substring Employee ID lalu tekan Enter, dan verifikasi entri yang cocok ditampilkan
4. Masukkan substring Position lalu tekan Enter, dan verifikasi entri yang cocok ditampilkan
5. Masukkan substring Division lalu tekan Enter, dan verifikasi entri yang cocok ditampilkan
6. Masukkan keyword Activity "Login" lalu tekan Enter, dan verifikasi hanya entri aktivitas Login yang tampil
7. Masukkan keyword Status "Failed" lalu tekan Enter, dan verifikasi hanya entri berstatus Failed yang tampil
8. Masukkan substring Note "Incorrect" lalu tekan Enter, dan verifikasi entri dengan Note tersebut tampil
9. Masukkan segmen IP Address "192.168" lalu tekan Enter, dan verifikasi entri yang cocok ditampilkan
10. Masukkan keyword Device/Browser "Chrome" lalu tekan Enter, dan verifikasi entri yang cocok ditampilkan
11. Masukkan teks tanggal kalender pada search box lalu tekan Enter
12. Verifikasi tidak ada pencarian yang dicocokkan berdasarkan kolom Date (guard Date wajib via Filter Panel)

## Notes

- Tanggal sengaja dikecualikan dari search box universal karena format tanggal berisiko memicu match parsial ambigu.
