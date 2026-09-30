---
id: TC-GS-USER-E2E-053-audit-handheld
title: Assign, Check Out, Check In, dan Unassign Handheld tercatat di log user
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-390
coverage:
  web: automated
---

# Assign, Check Out, Check In, dan Unassign Handheld tercatat di log user

## Prerequisites

- Akses ke modul hardware-handheld-reader sebagai admin atau PIC yang berwenang meng-assign Handheld
- Perangkat Handheld "Handheld-01" tersedia dan belum ter-assign ke user mana pun
- User "Yoga Handheld" ada dan Active
- Login ke Global Settings sebagai admin atau PIC yang sama untuk memeriksa log
- Spec ini menjalankan satu siklus penuh sampai Unassign, jadi "Handheld-01" kembali bebas

## Test Steps

### Assign

1. Di modul hardware-handheld-reader, Assign "Handheld-01" ke "Yoga Handheld"
2. Di Global Settings, buka Changelog "Yoga Handheld"
3. Verifikasi ada baris Action "Assign Handheld", Field "Handheld", Old Value "—", New Value "Handheld-01", dan Modified By admin atau PIC pelaku
4. Buka System Log admin atau PIC pelaku dan Global Settings > Activity Log
5. Verifikasi kedua surface mencatat baris yang sama

### Check Out dan Check In

6. Di modul hardware-handheld-reader, lakukan Check Out "Handheld-01" atas nama "Yoga Handheld"
7. Verifikasi Changelog "Yoga Handheld" memuat baris Action "Check Out Handheld", Field "Handheld", Old Value "—", New Value "Handheld-01"
8. Lakukan Check In "Handheld-01"
9. Verifikasi Changelog memuat baris Action "Check In Handheld", Field "Handheld", Old Value "Handheld-01", New Value "—"

### Unassign

10. Di modul hardware-handheld-reader, Unassign "Handheld-01" dari "Yoga Handheld"
11. Verifikasi Changelog memuat baris Action "Unassign Handheld", Field "Handheld", Old Value "Handheld-01", New Value "—"
12. Verifikasi System Log admin atau PIC pelaku dan Activity Log juga memuat baris Check Out, Check In, dan Unassign dengan pola yang sama

## Notes

- Aksi Handheld dipicu dari modul lain (hardware-handheld-reader), sedangkan pencatatannya ada di modul User (`user.md` bagian 8.3). Pola tiga surface sama dengan Pair TAG (`TC-GS-USER-148`, di spec 031).
- Spec ini butuh akses ke dua modul dan perangkat Handheld. Kebutuhan itu ditulis di Prerequisites untuk tim FE.
