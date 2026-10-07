---
id: TC-GS-ACTLOG-E2E-057-edge-case-retensi-data-tanpa-batas-dan-paritas-paket-langganan
title: "Edge Case Bisnis: Retensi Data Historis Lintas Tahun Tanpa Batas dan Paritas Fungsional Penuh Seluruh Tier Plan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-224
  - TC-GS-ACTLOG-225
coverage:
  web: automated
---

# Edge Case Bisnis: Retensi Data Historis Lintas Tahun Tanpa Batas dan Paritas Fungsional Penuh Seluruh Tier Plan

## Prerequisites

- Akun uji pada 4 tier langganan: Starter, Growth, Professional, dan Enterprise
- Entitas uji (Client, Principal, Distributor, Partner) dengan riwayat data log 3 tahun lalu

## Test Steps

### Retensi Data Historis 3 Tahun
1. Login pada entitas yang memiliki data riwayat log dari 3 tahun yang lalu.
2. Buka Tab Session dan User Action, atur filter Date ke rentang 3 tahun yang lalu.
3. Verifikasi data log historis tetap tampil utuh tanpa batasan waktu retensi atau notifikasi kedaluwarsa.
### Paritas Fungsional Lintas Tier Langganan
4. Login berturut-turut pada akun dengan paket Starter, Growth, Professional, dan Enterprise.
5. Buka modul Activity Log pada masing-masing akun.
6. Lakukan operasi Search, Filter multi-dimensi, Setup Column, dan Download CSV.
7. Verifikasi seluruh fungsionalitas tersedia setara 100% tanpa fitur terkunci, tanpa watermark, dan tanpa pembatasan kuota baris.

## Notes

- Sesuai ACTLOG-LOGIC-04 log disimpan tanpa batas waktu dan berlaku setara tanpa plan gating.
