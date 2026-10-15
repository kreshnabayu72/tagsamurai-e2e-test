---
id: TC-GS-USER-E2E-025-edit-user-validasi-duplikat-dan-guard-double-save
title: "Edit User: Validasi duplikat email dan employee ID serta guard double save"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-177
  - TC-GS-USER-178
  - TC-GS-USER-179
  - TC-GS-USER-180
  - TC-GS-USER-181
  - TC-GS-USER-182
  - TC-GS-USER-183
  - TC-GS-USER-184
coverage:
  web: automated
---

# Edit User: Validasi duplikat email dan employee ID serta guard double save

## Prerequisites

- Login sebagai Role: Total Control
- User target dan user pembanding tersedia

## Test Steps

### Validasi Duplikat pada Edit

1. Buka modal Edit user Dewi Lestari
2. Ubah Employee ID menjadi Employee ID milik user lain 'EMP-0001'
3. Verifikasi muncul error inline duplikat
4. Klik tombol '[Save]' berkali-kali secara cepat, verifikasi tombol masuk state loading disabled (guard double save)

## Notes

- Menggabungkan 8 test case granular (TC-GS-USER-177 s.d. TC-GS-USER-184).
