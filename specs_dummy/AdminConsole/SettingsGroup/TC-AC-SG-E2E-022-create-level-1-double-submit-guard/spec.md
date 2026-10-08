---
id: TC-AC-SG-E2E-022-create-level-1-double-submit-guard
title: "Perlindungan double-click submit pada Form Create Level 1"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SG-110
coverage:
  web: automated
---

# Perlindungan double-click submit pada Form Create Level 1

## Prerequisites

- Login sebagai Role: Total Control

## Test Steps

### Rapid Double-Click Submit
1. Buka modal `[+ New Group]`
2. Isi Group Name dengan nama unik `"Region Rapid"`
3. Lakukan klik dua kali secara sangat cepat pada tombol `[Submit]`
4. Verifikasi pada klik pertama, tombol `[Submit]` seketika berubah state menjadi disabled dan menampilkan loading spinner
5. Verifikasi hanya tepat 1 request Create yang dikirim ke server
6. Verifikasi hanya 1 record `"Region Rapid"` yang terbentuk di tabel (tidak ada duplikasi data)

## Notes

- Menguji debounce client-side button submission (error-handling-convention.md §5).
