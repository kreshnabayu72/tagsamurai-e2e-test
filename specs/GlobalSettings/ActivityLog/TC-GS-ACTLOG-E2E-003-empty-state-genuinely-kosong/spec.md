---
id: TC-GS-ACTLOG-E2E-003-empty-state-genuinely-kosong
title: "Tampilan Empty State Genuinely Kosong pada Tab Session dan User Action"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-05
coverage:
  web: automated
---

# Tampilan Empty State Genuinely Kosong pada Tab Session dan User Action

## Prerequisites

Mode: mock
- Login sebagai Role: Total Control Global Settings
- Intercept respons endpoint daftar log mengembalikan 0 baris data (karena aktor yang login live otomatis mencatat baris sesi)

## Test Steps

### Empty State Tab Session
1. Intercept endpoint daftar log Tab Session untuk mengembalikan 0 baris data.
2. Buka Global Settings > Activity Log > Session.
3. Verifikasi area tabel menampilkan ilustrasi empty state dengan Title 'No activity yet'.
4. Verifikasi Description menampilkan teks 'Activities will appear here as actions are performed.'.
5. Verifikasi tidak ada tombol aksi atau CTA di dalam empty state.
### Empty State Tab User Action
6. Intercept endpoint daftar log Tab User Action untuk mengembalikan 0 baris data.
7. Klik tab 'User Action'.
8. Verifikasi area tabel menampilkan ilustrasi empty state dengan Title 'No activity yet'.
9. Verifikasi Description menampilkan teks 'Activities will appear here as actions are performed.'.
10. Verifikasi tidak ada tombol aksi yang ditampilkan.

## Notes

- Kondisi genuinely empty diisolasi menggunakan mock karena di backend nyata setiap login otomatis menulis baris Session.
