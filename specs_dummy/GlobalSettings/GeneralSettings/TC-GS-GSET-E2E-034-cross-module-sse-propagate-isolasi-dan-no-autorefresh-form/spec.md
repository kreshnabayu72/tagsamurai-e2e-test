---
id: TC-GS-GSET-E2E-034-cross-module-sse-propagate-isolasi-dan-no-autorefresh-form
title: "Cross-Module Sync: propagate format tanpa reload, Session Idle Timeout tanpa memutus sesi, form tidak auto-refresh, dan isolasi entitas"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-118
  - TC-GS-GSET-119
  - TC-GS-GSET-120
  - TC-GS-GSET-121
coverage:
  web: automated
---

# Cross-Module Sync: propagate format tanpa reload, Session Idle Timeout tanpa memutus sesi, form tidak auto-refresh, dan isolasi entitas

## Prerequisites

- Login sebagai Role: Total Control (Budi Santoso) dengan tab 1 di General Settings dan tab 2 di Admin Console (entitas sama)
- Admin B (Total Control) pada sesi terpisah untuk blok form tidak auto-refresh
- Entitas `Client A` dan `Client Lain` untuk blok isolasi tenant
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`

## Test Steps

### Propagate Format ke Surface Konsumen Tanpa Reload

1. Di tab 1 pilih Date Format `M/d/yy` dan klik `[Save]`
2. Pindah ke tab 2 (Admin Console) tanpa reload dan amati kolom tanggal pada tabel yang terbuka
3. Verifikasi tab 2 menyegarkan tampilan tanggal diam-diam ke `M/d/yy` tanpa dialog interupsi dan tanpa reload halaman

### Session Idle Timeout Tanpa Memutus Sesi

4. Di tab 1 pilih Session Idle Timeout `1 hour` dan klik `[Save]`
5. Amati tab 2 tanpa reload
6. Lakukan aksi apa pun di tab 2
7. Verifikasi tab 2 tidak menampilkan dialog dan tidak berubah tampilan, serta sesi tab 1 dan tab 2 tetap aktif (tidak diputus dan tidak di-reset)

### Form General Settings Tidak Auto-Refresh

8. Admin B memilih Time Format `hh:mm a` dan klik `[Save]`
9. Amati tab 1 (General Settings) tanpa reload
10. Verifikasi form di tab 1 tidak berubah (Time Format tetap `HH:mm`) dan tidak ada dialog

### Isolasi Tenant

11. Di tab 1 (`Client A`) pilih Date Format `M/d/yy` dan klik `[Save]`
12. Amati tab 2 (`Client Lain`) tanpa reload
13. Verifikasi tab 2 tidak berubah (format `Client Lain` tetap) dan tidak menerima event

## Notes

- Menggabungkan TC-GS-GSET-118, 119, 120, dan 121 (Cross-Module Sync via SSE dan isolasi tenant). Butuh dua/lebih sesi browser simultan.
