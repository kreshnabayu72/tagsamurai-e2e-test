---
id: TC-GS-ACTLOG-E2E-032-tab-user-action-sorting-3-state-8-kolom
title: "Tab User Action: Sorting 3-state untuk 8 kolom tabel dan penempatan baris Import/Create kosong di akhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-161
  - TC-GS-ACTLOG-162
  - TC-GS-ACTLOG-163
  - TC-GS-ACTLOG-164
  - TC-GS-ACTLOG-165
  - TC-GS-ACTLOG-166
  - TC-GS-ACTLOG-167
  - TC-GS-ACTLOG-168
coverage:
  web: automated
---

# Tab User Action: Sorting 3-state untuk 8 kolom tabel dan penempatan baris Import/Create kosong di akhir

## Prerequisites

- Login sebagai Role: Total Control pada Tab User Action dengan dataset memuat entri Import bulk (Name strip), entri Create/Delete (Field kosong), dan nilai campuran teks/angka pada Old/New Value

## Test Steps

1. Klik header kolom Date: klik 1 (Oldest First), klik 2 (Newest First), klik 3 (kembali ke default)
2. Klik header kolom Action dan verifikasi urutan diurutkan secara alfabetis A-Z
3. Klik header kolom Object dan verifikasi urutan diurutkan secara alfabetis A-Z
4. Klik header kolom Name ascending dan verifikasi baris Import bulk (Name strip) ditaruh di akhir urutan
5. Klik header kolom Field ascending dan verifikasi baris Create/Delete (Field strip) ditaruh di akhir urutan
6. Klik header kolom Old Value ascending dan verifikasi nilai numerik terurut lebih dulu, diikuti teks alfabetis, dan baris kosong di akhir
7. Klik header kolom New Value ascending dan verifikasi pola pengurutan campuran numerik/teks yang sama berlaku
8. Klik header kolom Modified By dan verifikasi urutan diurutkan berdasarkan nama lengkap asli admin

## Notes

- Kolom Old Value dan New Value dapat berisi angka, teks, atau kosong sehingga diurutkan dengan aturan natural sorting campuran.
