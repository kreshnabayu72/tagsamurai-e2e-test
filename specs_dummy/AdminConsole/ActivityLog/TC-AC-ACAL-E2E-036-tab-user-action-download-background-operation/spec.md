---
id: TC-AC-ACAL-E2E-036-tab-user-action-download-background-operation
title: "Tab User Action — Pengalihan ke Background Download untuk dataset besar (>5.000 baris)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-207
coverage:
  web: automated
---

# Tab User Action — Pengalihan ke Background Download untuk dataset besar (>5.000 baris)

## Prerequisites

- Login sebagai Role: Principal Total Control
- Data riwayat log Tab User Action berjumlah lebih dari 5.000 baris (minimal 5.001 baris)

## Test Steps

1. Buka menu `Admin Console > Activity Log` > klik tab `"User Action"`
2. Pastikan tidak ada filter aktif sehingga total dataset melebihi 5.000 entri
3. Klik tombol `[Download]` pada toolbar dan pilih `"Download as CSV"`
4. Verifikasi sistem tidak mengunduh file secara langsung di browser, melainkan memicu job Background Download
5. Verifikasi toast / notifikasi in-app muncul menginformasikan proses download sedang berlangsung di background
6. Verifikasi setelah job selesai, notifikasi siap unduh diterima dengan masa berlaku file selama 24 jam

## Notes

- Kriteria volume >5.000 baris memicu Long-Running Operation protocol sesuai konvensi platform TAG Samurai.
