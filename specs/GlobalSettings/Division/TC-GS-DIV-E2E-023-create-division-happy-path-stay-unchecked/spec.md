---
id: TC-GS-DIV-E2E-023-create-division-happy-path-stay-unchecked
title: "Pembuatan Divisi Berhasil dengan Checkbox Stay Unchecked: Penutupan Modal, Toast Sukses, Refleksi Tabel, dan Submit Enter"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-65
  - TC-GS-DIV-78
coverage:
  web: automated
---

# Pembuatan Divisi Berhasil dengan Checkbox Stay Unchecked: Penutupan Modal, Toast Sukses, Refleksi Tabel, dan Submit Enter

## Prerequisites

- Login sebagai Role: Total Control
- Data: Public Relations (PR)
- User berada di Global Settings > User > Division

## Test Steps

### Submit Create dengan Stay unchecked menutup modal (TC-GS-DIV-65)

1. Klik `[+ Division]`
2. Biarkan checkbox `Stay on this form after submitting` unchecked
3. Isi Division Name `Public Relations` dan Code `PR`
4. Klik `[Submit]`
5. Verifikasi Muncul toast sukses: `Success, division has been created.`
6. Verifikasi Modal Create Division tertutup
7. Verifikasi Baris `Public Relations` tampil di tabel

### Klik ganda Submit hanya membuat satu Division (TC-GS-DIV-78)

8. Klik `[+ Division]`
9. Isi Division Name `Treasury Operations` dan Code `TRO`
10. Klik `[Submit]` dua kali cepat
11. Verifikasi Tombol `[Submit]` disabled setelah klik pertama
12. Verifikasi Hanya 1 Division `Treasury Operations` dibuat; tidak ada duplikat dan tidak ada error duplicate

## Notes

- Memvalidasi alur happy path pembuatan divisi dengan submit tombol maupun Enter: modal tertutup, toast sukses muncul, baris baru tampil di tabel (PRD §3, §4.4 FI-13).
- Sumber pemetaan test case granular: TC-GS-DIV-65, TC-GS-DIV-78.
