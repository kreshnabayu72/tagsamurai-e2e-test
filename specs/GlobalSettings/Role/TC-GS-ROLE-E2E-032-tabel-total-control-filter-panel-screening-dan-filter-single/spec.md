---
id: TC-GS-ROLE-E2E-032-tabel-total-control-filter-panel-screening-dan-filter-single
title: "Screening Filter Panel Tab Total Control dan Penerapan Filter Single 8 Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-69
  - TC-GS-ROLE-131
  - TC-GS-ROLE-132
  - TC-GS-ROLE-133
  - TC-GS-ROLE-134
  - TC-GS-ROLE-135
  - TC-GS-ROLE-136
  - TC-GS-ROLE-230
coverage:
  web: automated
---

# Screening Filter Panel Tab Total Control dan Penerapan Filter Single 8 Field

## Prerequisites

- Login sebagai Role: Total Control
- Data user di Tab Total Control memiliki kombinasi atribut lengkap

## Test Steps

1. Buka Global Settings > Role & Permission > Tab Total Control
2. Klik tombol Filter pada toolbar
3. Verifikasi Filter Panel terbuka menampilkan tepat 8 field filter multi-select/date: Position, Division, Status, Modified By, Activation Status, Temporary User, Temporary Until, TAG
4. Pilih satu opsi pada filter Position (mis. 'IT Manager') lalu klik [Apply]
5. Verifikasi tabel hanya menampilkan user dengan posisi IT Manager
6. Buka kembali Filter Panel, klik [Clear] pada Position, lalu pilih opsi pada filter Division (mis. 'Information Technology') dan klik [Apply]
7. Verifikasi tabel hanya menampilkan user dari divisi Information Technology
8. Uji penerapan filter secara bergiliran untuk Status, Modified By, Activation Status, Temporary User, Temporary Until, dan TAG
9. Verifikasi masing-masing filter menyaring data tabel secara independen dan akurat

## Notes

- Filter Panel Tab Total Control mencakup 8 field penyaringan standar (role.md §4.2, §4.2a).
