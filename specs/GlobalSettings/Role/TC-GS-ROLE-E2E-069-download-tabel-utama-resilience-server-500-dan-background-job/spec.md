---
id: TC-GS-ROLE-E2E-069-download-tabel-utama-resilience-server-500-dan-background-job
title: "Ketahanan Download Tab Utama: Toast Error Server 500 dan Eksekusi Background Job untuk Ekspor >5.000 Baris"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-179
  - TC-GS-ROLE-180
coverage:
  web: automated
---

# Ketahanan Download Tab Utama: Toast Error Server 500 dan Eksekusi Background Job untuk Ekspor >5.000 Baris

## Prerequisites

- Login sebagai Total Control; intercept export 500 & >5000 rows
- Data Uji: Volume data >5.000 user
- Spectra.intercept aktif untuk penanganan simulasi network/mock response
- Setup Hook: beforeEach: navigateTo(Tab Total Control)
- Login sbg Role: Total Control (Ahmad Fauzi)
- Response Download dibuat gagal 5xx
- User berada di Global Settings > Role & Permission > Total Control
- Tab Total Control berisi >5.000 user (data volume)

## Test Steps

### Download gagal pada Tab Total Control (TC-GS-ROLE-179)

1. Download > "Download as CSV"
2. Verifikasi Muncul toast error: "Error, failed to download Role-Permission-Total-Control."
3. Verifikasi Tidak ada file terunduh

### Download lebih dari 5.000 baris berjalan sebagai background job (TC-GS-ROLE-180)

4. Download CSV
5. Verifikasi Toast informational saat trigger dan halaman tidak terkunci
6. Verifikasi Notifikasi Notification Center berisi [Download] saat selesai

## Notes

- Memvalidasi alur skenario "Ketahanan Download Tab Utama: Toast Error Server 500 dan Eksekusi Background Job untuk Ekspor >5.000 Baris".
- Aturan PRD terkait: global-settings/role/PRD/role.md §6 V-14; foundation/process/prd-process/prd-conventions.md §7; global-settings/role/PRD/role.md §5 Download; foundation/process/prd-process/error-handling-convention.md §10.1.
- Sumber pemetaan test case granular: TC-GS-ROLE-179, TC-GS-ROLE-180.
