---
id: TC-AC-SG-E2E-016-guided-tooltip-skip-step-3-aktor-tanpa-mutasi
title: "Guided Tooltip otomatis melewati Step 3 untuk aktor tanpa tombol aksi mutasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-222
coverage:
  web: automated
---

# Guided Tooltip otomatis melewati Step 3 untuk aktor tanpa tombol aksi mutasi

## Prerequisites

- Mode: mock
- Login sebagai Role: Read Only (atau Manage group R-only)
- Flag `guided_tooltip_seen_ac-settings-group` belum aktif (false / kunjungan pertama)

## Test Steps

### Walkthrough Aktor Read-Only
1. Buka halaman `Settings > Group`
2. Verifikasi walkthrough Guided Tooltip otomatis muncul dari Step 1 (Sidebar Tree)
3. Verifikasi indikator langkah di header tooltip bertuliskan `"Step 1 of 3"` (bukan 4)
4. Klik `[Next]`
5. Verifikasi walkthrough langsung menuju Step 2 (Table Details) dengan indikator `"Step 2 of 3"`
6. Klik `[Next]`
7. Verifikasi Step 3 (target tombol `⋯`) dilewati otomatis dan langsung berpindah ke Step 4 (Toolbar Search & Export)
8. Verifikasi indikator langkah bertuliskan `"Step 3 of 3"` dan tombol `[Next]` berubah menjadi `[Done]`
9. Klik `[Done]` dan verifikasi walkthrough selesai

## Notes

- Mencegah tooltip macet mencari target elemen DOM yang sengaja disembunyikan untuk aktor view-only.
