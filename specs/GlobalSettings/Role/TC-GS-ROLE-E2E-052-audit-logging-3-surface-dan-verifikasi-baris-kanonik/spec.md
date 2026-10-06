---
id: TC-GS-ROLE-E2E-052-audit-logging-3-surface-dan-verifikasi-baris-kanonik
title: "Pencatatan Audit Log pada 3 Surface (Changelog, System Log, Activity Log) dan Verifikasi Baris Kanonik"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-84
  - TC-GS-ROLE-86
  - TC-GS-ROLE-87
  - TC-GS-ROLE-88
  - TC-GS-ROLE-322
  - TC-GS-ROLE-323
  - TC-GS-ROLE-324
  - TC-GS-ROLE-325
coverage:
  web: automated
---

# Pencatatan Audit Log pada 3 Surface (Changelog, System Log, Activity Log) dan Verifikasi Baris Kanonik

## Prerequisites

- Login sebagai Role: Total Control
- Lakukan aksi penugasan dan pencabutan Total Control dan Read Only

## Test Steps

1. Buka Tab Total Control dan lakukan Assign Total Control pada user target baru
2. Buka Changelog modal Tab Total Control
3. Verifikasi baris kanonik tercatat dengan Field="Access Level", New Value="Total Control", Old Value="—"
4. Lakukan Remove Total Control pada user target tersebut
5. Buka kembali Changelog modal Tab Total Control
6. Verifikasi baris kanonik tercatat dengan Field="Access Level", Old Value="Total Control", New Value="—"
7. Buka menu User > buka Detail akun aktor > Tab System Log
8. Verifikasi System Log aktor mencatat aksi Assign dan Remove Total Control
9. Buka menu Global Settings > Activity Log
10. Verifikasi Activity Log global mencatat aksi penugasan dan pencabutan akses level tersebut
11. Verifikasi seluruh entri log bersifat read-only snapshot permanen (immutability)

## Notes

- Audit log tersinkronisasi di 3 permukaan: Changelog modal, System Log aktor, dan Activity Log global (role.md §8.5, §8.6).
