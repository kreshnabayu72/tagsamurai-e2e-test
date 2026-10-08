---
id: TC-GS-DIV-E2E-045-bulk-delete-collapse-dialog-single-n-sama-dengan-1
title: "Penyederhanaan Dialog Bulk Delete Menjadi Dialog Single Saat Tepat 1 Baris Terpilih (N=1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-131
coverage:
  web: automated
---

# Penyederhanaan Dialog Bulk Delete Menjadi Dialog Single Saat Tepat 1 Baris Terpilih (N=1)

## Prerequisites

- Login sebagai Role: Total Control
- Centang tepat 1 divisi bebas relasi
- User berada di Global Settings > User > Division
- Division `Marketing` dan `Logistics` bebas relasi (TC-GS-DIV-30)

## Test Steps

1. Centang baris `Marketing` dan `Logistics`
2. Klik aksi `[Delete]` pada Bulk Action Bar
3. Verifikasi Title `Delete Divisions` (severity danger)
4. Verifikasi Body: bullet `Logistics` dan `Marketing`, lalu `Are you sure you want to delete them? This action cannot be undone.`
5. Verifikasi Tombol `[Cancel]` dan `[Delete]` (filled, danger)

## Notes

- Memvalidasi aturan penyederhanaan: saat N=1 baris dicentang lalu tombol bulk [Delete] diklik, sistem menampilkan Dialog 1 konfirmasi single (bukan Dialog 4 homogen) (PRD §4.2d tabel evaluasi bulk).
- Sumber pemetaan test case granular: TC-GS-DIV-131.
