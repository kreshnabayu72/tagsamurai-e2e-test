---
id: TC-GS-GSET-E2E-031-pencatatan-changelog-activity-log-mutasi-dan-snapshot
title: "Audit Log: pencatatan Save per field di Changelog & Activity Log, tiga field sekaligus tanpa duplikat, dan snapshot entri lama"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-104
  - TC-GS-GSET-105
  - TC-GS-GSET-106
  - TC-GS-GSET-107
  - TC-GS-GSET-108
  - TC-GS-GSET-109
  - TC-GS-GSET-111
coverage:
  web: automated
---

# Audit Log: pencatatan Save per field di Changelog & Activity Log, tiga field sekaligus tanpa duplikat, dan snapshot entri lama

## Prerequisites

- Login sebagai Role: Total Control (aktor Budi Santoso)
- Changelog dan Activity Log General Settings dapat diakses
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`

## Test Steps

### Save Currency Code

1. Pilih Currency Code `USD`, klik `[Save]` lalu `[Change Currency]`
2. Buka Modal Changelog dan amati baris teratas
3. Verifikasi tepat 1 baris baru: Action `Edit`, Field `Currency Code`, Old Value `Rp - Indonesian Rupiah`, New Value `teks label opsi USD`, Modified By `Budi S`; tidak ada baris untuk field yang tidak berubah
4. Buka Global Settings > Activity Log dan amati baris teratas
5. Verifikasi tepat 1 baris baru: Action `Edit`, Object `General Settings`, Name `—`, Field `Currency Code`, Old Value `Rp - Indonesian Rupiah`, New Value `teks label opsi USD`, Modified By `[nama aktor singkat]`

### Save Time Zone

6. Pilih Time Zone Lain, klik `[Save]`
7. Verifikasi Modal Changelog mencatat tepat 1 baris: Action `Edit`, Field `Time Zone`, Old Value `teks label opsi Asia/Jakarta`, New Value `teks label opsi Time Zone Lain`, Modified By `Budi S`
8. Verifikasi Activity Log mencatat tepat 1 baris dengan Field/Old/New yang sama dan Name `—`

### Save Date Format

9. Pilih Date Format `M/d/yy`, klik `[Save]`
10. Verifikasi Modal Changelog mencatat tepat 1 baris: Field `Date Format`, Old `dd/MM/yy`, New `M/d/yy`
11. Verifikasi Activity Log mencatat tepat 1 baris dengan Field/Old/New yang sama dan Name `—`

### Save Time Format

12. Pilih Time Format `hh:mm a`, klik `[Save]`
13. Verifikasi Modal Changelog mencatat tepat 1 baris: Field `Time Format`, Old `HH:mm`, New `hh:mm a`
14. Verifikasi Activity Log mencatat tepat 1 baris dengan Field/Old/New yang sama dan Name `—`

### Save Session Idle Timeout

15. Pilih Session Idle Timeout `1 hour`, klik `[Save]`
16. Verifikasi Modal Changelog mencatat tepat 1 baris: Field `Session Idle Timeout`, Old `30 minutes`, New `1 hour`
17. Verifikasi Activity Log mencatat tepat 1 baris dengan Field/Old/New yang sama dan Name `—`

### Save Tiga Field Sekaligus Tanpa Duplikat

18. Pilih Date Format `dd MMM yy`, Time Format `hh:mm a`, Session Idle Timeout `2 hours`, lalu klik `[Save]`
19. Verifikasi Modal Changelog mencatat tepat 3 baris baru (Field `Date Format`, `Time Format`, `Session Idle Timeout`), tanpa baris untuk Currency Code dan Time Zone
20. Verifikasi Activity Log mencatat tepat 3 baris baru dengan Field/Old/New yang sama dan Name `—`

### Snapshot Entri Lama

21. Pilih Session Idle Timeout `1 hour` lalu Save, kemudian pilih `4 hours` lalu Save
22. Buka Modal Changelog dan bandingkan 2 baris Session Idle Timeout
23. Verifikasi baris Save pertama tetap berisi perubahan `30 minutes` ke `1 hour` (tidak ter-overwrite) dan baris Save kedua berisi `1 hour` ke `4 hours`

## Notes

- Menggabungkan TC-GS-GSET-104 s.d. 109 dan 111 (pencatatan Audit Log mutasi General Settings dan snapshot).
