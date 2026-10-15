---
id: TC-GS-USER-E2E-023-create-user-variasi-custom-field-dan-plan-gating
title: "Create User: Variasi input custom field, tanggal temporary, dan pembatasan fitur plan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-139
  - TC-GS-USER-140
  - TC-GS-USER-141
  - TC-GS-USER-142
  - TC-GS-USER-143
  - TC-GS-USER-144
  - TC-GS-USER-145
  - TC-GS-USER-146
  - TC-GS-USER-147
  - TC-GS-USER-148
  - TC-GS-USER-149
  - TC-GS-USER-150
  - TC-GS-USER-151
  - TC-GS-USER-152
  - TC-GS-USER-153
  - TC-GS-USER-154
  - TC-GS-USER-155
  - TC-GS-USER-156
  - TC-GS-USER-157
  - TC-GS-USER-158
  - TC-GS-USER-159
  - TC-GS-USER-1040
coverage:
  web: automated
---

# Create User: Variasi input custom field, tanggal temporary, dan pembatasan fitur plan

## Prerequisites

- Client dengan plan Growth (mendukung TAG dan fitur lanjutan)
- Custom Field aktif tersedia di form

## Test Steps

### Pengisian Custom Fields dan Temporary User

1. Buka modal '[+ User]'
2. Isi data identitas wajib
3. Isi field Custom Field: Blood Type (Dropdown), Skills (Multi-select), Phone
4. Centang 'Set as Temporary User', pilih tanggal Temporary Until (besok atau lebih)
5. Klik '[Submit]'
6. Verifikasi user berhasil dibuat dengan atribut custom field dan status temporary tercatat

## Notes

- Menggabungkan 22 test case granular (TC-GS-USER-139 s.d. TC-GS-USER-1040).
