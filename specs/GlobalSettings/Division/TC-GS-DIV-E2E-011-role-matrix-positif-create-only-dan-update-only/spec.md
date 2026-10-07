---
id: TC-GS-DIV-E2E-011-role-matrix-positif-create-only-dan-update-only
title: "Eksekusi Operasi oleh Aktor System Role Berhak Terbatas: Create-Only dan Update-Only"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-26
  - TC-GS-DIV-27
coverage:
  web: automated
---

# Eksekusi Operasi oleh Aktor System Role Berhak Terbatas: Create-Only dan Update-Only

## Prerequisites

- Login sebagai Role: System Role Create-Only dan Update-Only
- Akun A: System Role capability Create dan Read
- Akun B: System Role capability Update dan Read
- User berada di Global Settings > User > Division
- Division `Corporate Secretary` sudah dibuat (TC-GS-DIV-26)

## Test Steps

### Aktor Create-saja berhasil membuat Division (TC-GS-DIV-26)

1. Klik `[+ Division]`
2. Isi Division Name `Corporate Secretary`
3. Biarkan Code kosong
4. Klik `[Submit]`
5. Verifikasi Modal Create Division tertutup
6. Verifikasi Muncul toast sukses: `Success, division has been created.`
7. Verifikasi Baris `Corporate Secretary` tampil di tabel

### Aktor Update-saja berhasil mengubah Name Division (TC-GS-DIV-27)

8. Buka row action baris `Corporate Secretary` lalu klik `Edit`
9. Ubah Division Name menjadi `Corporate Secretariat`
10. Klik `[Save]`
11. Verifikasi Modal Edit Division tertutup
12. Verifikasi Muncul toast sukses: `Success, division has been updated.`
13. Verifikasi Baris tabel menampilkan `Corporate Secretariat`

## Notes

- Memvalidasi bahwa aktor Create-only berhasil membuat divisi baru dan aktor Update-only berhasil mengubah nama divisi (PRD §2, §4.8).
- Sumber pemetaan test case granular: TC-GS-DIV-26, TC-GS-DIV-27.
