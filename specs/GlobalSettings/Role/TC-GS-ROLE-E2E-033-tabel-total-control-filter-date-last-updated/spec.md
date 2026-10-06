---
id: TC-GS-ROLE-E2E-033-tabel-total-control-filter-date-last-updated
title: "Penerapan Filter Date Picker Kolom Last Updated Tab Total Control (Varian 1 Hari vs Rentang Tanggal)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-338
  - TC-GS-ROLE-339
coverage:
  web: automated
---

# Penerapan Filter Date Picker Kolom Last Updated Tab Total Control (Varian 1 Hari vs Rentang Tanggal)

## Prerequisites

- Login sebagai Role: Total Control
- Data user memiliki tanggal Last Updated yang bervariasi

## Test Steps

1. Buka Global Settings > Role & Permission > Tab Total Control
2. Klik tombol Filter untuk membuka Filter Panel
3. Pilih field filter date 'Last Updated'
4. Pilih tanggal tunggal pada kalender date picker (start date dan end date sama pada 1 hari yang ada datanya)
5. Klik tombol [Apply]
6. Verifikasi tabel hanya menampilkan record yang diperbarui tepat pada tanggal tersebut
7. Buka kembali Filter Panel dan atur filter Last Updated ke rentang beberapa hari inklusif (mis. rentang 7 hari)
8. Klik tombol [Apply]
9. Verifikasi tabel menampilkan seluruh record yang diperbarui dalam rentang tanggal tersebut secara inklusif di kedua ujung batas

## Notes

- Pengujian filter date mencakup batas 1 hari persis dan rentang multi-hari (role.md §9.8).
