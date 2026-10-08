---
id: TC-AC-SG-E2E-029-delete-single-guard-last-group
title: "Guard Delete Single Kondisi #1: Pemblokiran penghapusan satu-satunya group milik entitas"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-57
  - TC-AC-SG-58
coverage:
  web: automated
---

# Guard Delete Single Kondisi #1: Pemblokiran penghapusan satu-satunya group milik entitas

## Prerequisites

- Login sebagai Role: Total Control
- Entitas hanya memiliki tepat 1 group di seluruh organisasi (kondisi last group)

## Test Steps

### Tombol Tetap Enabled & Evaluasi Klik
1. Buka halaman `Settings > Group` pada entitas dengan 1 group tersisa
2. Amati tombol row action `[Delete]` pada group tersebut
3. Verifikasi tombol `Delete` berstatus Show dan enabled (tidak disabled di muka)
4. Klik tombol `[Delete]`
5. Verifikasi muncul dialog blokir informasi `"Cannot Delete Group"`
6. Verifikasi body dialog menampilkan bullet nama group beserta teks `"Deleting this group would leave you with no groups. Create another group before deleting this one."` dengan tombol tunggal `[OK]`
7. Verifikasi TIDAK ADA tombol konfirmasi lanjut pada dialog
8. Klik `[OK]` dan verifikasi group tidak terhapus

## Notes

- Guard last group (Kondisi #1 ACSG-LOGIC-02) dicek paling awal sebelum pemeriksaan member.
