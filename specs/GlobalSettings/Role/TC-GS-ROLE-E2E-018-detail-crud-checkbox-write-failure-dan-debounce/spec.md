---
id: TC-GS-ROLE-E2E-018-detail-crud-checkbox-write-failure-dan-debounce
title: "Ketahanan Auto-Save Checkbox CRUD Terhadap Kegagalan Server 5xx dan Rapid Toggle Debounce"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-35
  - TC-GS-ROLE-110
coverage:
  web: automated
---

# Ketahanan Auto-Save Checkbox CRUD Terhadap Kegagalan Server 5xx dan Rapid Toggle Debounce

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Tersedia kemampuan intersept API PATCH /roles/roles/users/{user_id}

## Test Steps

1. Buka Global Settings > Role & Permission > Tab System > Detail role 'Manage user and role'
2. Simulasikan endpoint PATCH mengembalikan HTTP 500
3. Klik checkbox Update pada salah satu baris user reguler
4. Verifikasi toast error muncul: "Error, failed to update permissions."
5. Verifikasi checkbox Update otomatis revert kembali ke kondisi semula sebelum diklik
6. Pulihkan respons endpoint ke normal 200 OK
7. Lakukan rapid clicking toggle checkbox Update secara cepat berkali-kali dalam hitungan detik
8. Verifikasi sistem menerapkan mekanisme debounce dan hanya mengirimkan payload untuk status centang terakhir

## Notes

- Debounce melindungi backend dari flooding request saat pengguna mengklik checkbox berulang-ulang (role.md §9.6).
