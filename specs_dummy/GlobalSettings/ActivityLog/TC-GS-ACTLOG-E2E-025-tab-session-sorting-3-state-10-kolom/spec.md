---
id: TC-GS-ACTLOG-E2E-025-tab-session-sorting-3-state-10-kolom
title: "Tab Session: Siklus Sorting 3-State untuk 10 Kolom dan Penanganan Nilai Kosong"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-86
  - TC-GS-ACTLOG-87
  - TC-GS-ACTLOG-88
  - TC-GS-ACTLOG-89
  - TC-GS-ACTLOG-90
  - TC-GS-ACTLOG-91
  - TC-GS-ACTLOG-92
  - TC-GS-ACTLOG-116
coverage:
  web: automated
---

# Tab Session: Siklus Sorting 3-State untuk 10 Kolom dan Penanganan Nilai Kosong

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat variasi data log Session untuk seluruh 10 kolom

## Test Steps

### Siklus Sort 3-State Kolom Date
1. Klik header kolom Date sekali: indikator (↑) aktif, urutan Oldest First.
2. Klik header kolom Date kedua kali: indikator (↓) aktif, urutan Newest First.
3. Klik header kolom Date ketiga kali: indikator sort tidak aktif, urutan kembali ke default.
### Sort Kolom Teks Alfabetis & Case-Insensitive
4. Uji sort 3 klik pada kolom Activity, Division, dan Note: verifikasi urutan alfabetis A-Z dan Z-A.
5. Uji sort kolom Position dengan variasi huruf kapital dan kecil, verifikasi sort bersifat case-insensitive.
### Sort dengan Nilai Kosong (—)
6. Uji sort kolom Employee ID, Position, Device / Browser yang memiliki sel kosong ('—').
7. Verifikasi saat Ascending (↑), nilai terisi urut A-Z dan baris '—' ditaruh di paling bawah.
8. Verifikasi saat Descending (↓), baris '—' ditaruh di paling atas dan nilai terisi urut Z-A.
### Sort Kolom Khusus: User, Status, IP, Actions
9. Uji sort kolom User: verifikasi pengurutan mengikuti nama lengkap (bukan nama singkat yang tampil di tabel).
10. Uji sort kolom Status: verifikasi baris Logout dan Session diperlakukan bernilai '—' (di paling bawah saat Asc, di paling atas saat Desc).
11. Uji sort kolom IP Address: verifikasi pengurutan berbasis string karakter (bukan numerik per oktet).
12. Amati header kolom Column Visibility (⋯): verifikasi tidak memiliki ikon sort dan klik tidak memicu pengurutan.

## Notes

- Pengurutan mematuhi aturan platform 3-state sort dengan penanganan nilai kosong di akhir saat ascending.
