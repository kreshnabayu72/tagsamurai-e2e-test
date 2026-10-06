---
id: TC-AC-ACAL-E2E-022-tab-session-download-background-operation
title: "Tab Session — Pengalihan ke Background Download untuk dataset besar (>5.000 baris)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-122
coverage:
  web: automated
---

# Tab Session — Pengalihan ke Background Download untuk dataset besar (>5.000 baris)

## Prerequisites

- Login sebagai Role: Principal Total Control
- Data riwayat log Tab Session berjumlah lebih dari 5.000 baris (minimal 5.001 baris)

## Test Steps

1. Buka menu `Admin Console > Activity Log` (Tab Session)
2. Pastikan tidak ada filter aktif sehingga total dataset melebihi 5.000 entri
3. Klik tombol `[Download]` pada toolbar dan pilih `"Download as CSV"`
4. Verifikasi sistem tidak mengunduh file secara langsung di browser, melainkan memicu job Background Download
5. Verifikasi toast / notifikasi in-app muncul menginformasikan proses download sedang berlangsung di background
6. Verifikasi setelah job selesai, notifikasi siap unduh diterima dengan masa berlaku file selama 24 jam

## Notes

- Kriteria volume >5.000 baris memicu Long-Running Operation protocol sesuai konvensi platform TAG Samurai.
