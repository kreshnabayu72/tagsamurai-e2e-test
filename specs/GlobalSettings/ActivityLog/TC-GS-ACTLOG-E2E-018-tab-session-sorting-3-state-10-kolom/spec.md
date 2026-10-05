---
id: TC-GS-ACTLOG-E2E-018-tab-session-sorting-3-state-10-kolom
title: "Tab Session: Sorting 3-state untuk 10 kolom tabel dan penempatan nilai kosong di akhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-76
  - TC-GS-ACTLOG-77
  - TC-GS-ACTLOG-78
  - TC-GS-ACTLOG-79
  - TC-GS-ACTLOG-80
  - TC-GS-ACTLOG-81
  - TC-GS-ACTLOG-82
  - TC-GS-ACTLOG-83
  - TC-GS-ACTLOG-84
  - TC-GS-ACTLOG-85
coverage:
  web: automated
---

# Tab Session: Sorting 3-state untuk 10 kolom tabel dan penempatan nilai kosong di akhir

## Prerequisites

- Login sebagai Role: Total Control pada Tab Session dengan dataset memuat nilai kosong pada Employee ID, Position, Division, Note, status strip pada Logout, dan variasi IP string

## Test Steps

1. Klik header kolom Date: klik 1 (Oldest First), klik 2 (Newest First), klik 3 (kembali ke default sort)
2. Klik header kolom User dan verifikasi urutan diurutkan berdasarkan nama lengkap asli (bukan teks terpotong)
3. Klik header kolom Employee ID ascending dan verifikasi baris dengan nilai kosong (`—`) ditaruh di akhir urutan
4. Klik header kolom Position ascending dan verifikasi baris kosong ditaruh di akhir urutan
5. Klik header kolom Division ascending dan verifikasi baris kosong ditaruh di akhir urutan
6. Klik header kolom Activity dan verifikasi urutan diurutkan secara alfabetis A-Z
7. Klik header kolom Status ascending dan verifikasi baris dengan status strip (`—`) tampil di akhir urutan
8. Klik header kolom Note ascending dan verifikasi baris tanpa note ditaruh di akhir urutan
9. Klik header kolom IP Address ascending dan verifikasi urutan diurutkan berdasarkan string comparison (mis. "10.0.0.9" sebelum "9.255.255.1")
10. Klik header kolom Device/Browser ascending dan verifikasi nilai tidak terparse ditaruh di akhir urutan

## Notes

- Siklus sorting 3-state: Ascending -> Descending -> Reset ke default. Nilai null/strip selalu ditempatkan paling akhir saat ascending.
