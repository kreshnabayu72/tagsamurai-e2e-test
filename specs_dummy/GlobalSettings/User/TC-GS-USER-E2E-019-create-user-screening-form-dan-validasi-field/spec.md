---
id: TC-GS-USER-E2E-019-create-user-screening-form-dan-validasi-field
title: "Create User: Screening modal Create, kontrol form, validasi format, dan batas input"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-88
  - TC-GS-USER-89
  - TC-GS-USER-90
  - TC-GS-USER-91
  - TC-GS-USER-92
  - TC-GS-USER-93
  - TC-GS-USER-94
  - TC-GS-USER-95
  - TC-GS-USER-96
  - TC-GS-USER-97
  - TC-GS-USER-98
  - TC-GS-USER-99
  - TC-GS-USER-100
  - TC-GS-USER-101
  - TC-GS-USER-102
  - TC-GS-USER-103
  - TC-GS-USER-104
  - TC-GS-USER-105
  - TC-GS-USER-106
  - TC-GS-USER-107
  - TC-GS-USER-108
  - TC-GS-USER-109
  - TC-GS-USER-110
  - TC-GS-USER-111
  - TC-GS-USER-112
  - TC-GS-USER-113
  - TC-GS-USER-114
  - TC-GS-USER-115
  - TC-GS-USER-116
coverage:
  web: automated
---

# Create User: Screening modal Create, kontrol form, validasi format, dan batas input

## Prerequisites

- Login sebagai Role: Total Control
- Berada di Global Settings > User > User List

## Test Steps

### Screening Modal Create

1. Klik tombol '[+ User]'
2. Verifikasi modal terbuka dengan title 'Create User' dan tombol [✕] di header
3. Verifikasi field First Name, Last Name, Email, Position, Division, Access, Employee ID, Phone, dan checkbox 'Stay on this form after submitting'
4. Verifikasi footer modal memuat tombol '[Clear Field]' dan '[Submit]' (tanpa tombol Cancel)

### Validasi Field Wajib dan Format

5. Klik tombol '[Submit]' tanpa mengisi form, verifikasi pesan error inline muncul pada field wajib First Name, Last Name, Email, Division, dan Access
6. Masukkan email tidak valid 'budi@invalid', verifikasi pesan error format email
7. Masukkan First Name melebihi batas karakter (120 karakter), verifikasi pemotongan atau pesan batas karakter
8. Klik tombol '[Clear Field]', verifikasi seluruh input kembali bersih

## Notes

- Menggabungkan 29 test case granular (TC-GS-USER-88 s.d. TC-GS-USER-116).
