---
id: TC-GS-POS-E2E-005-persistensi-state-tabel-f5-dan-navigasi
title: "Persistensi state tabel saat F5, reset saat klik sidebar, dan retensi saat pindah sub-tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-13
  - TC-GS-POS-14
  - TC-GS-POS-15
coverage:
  web: automated
---

# Persistensi state tabel saat F5, reset saat klik sidebar, dan retensi saat pindah sub-tab

## Prerequisites

- Login sebagai Role: Total Control
- Tabel Position terisi data

## Test Steps

### Retensi Saat Refresh Browser (F5)

1. Buka Global Settings > User > Position
2. Masukkan kata kunci "Manager" pada input Search lalu tekan Enter
3. Klik header kolom Last Updated 1x untuk mengurutkan Oldest First
4. Ubah page size menjadi 25
5. Tekan tombol F5 (refresh browser)
6. Verifikasi setelah halaman termuat ulang: kata kunci "Manager" tetap terisi pada Search, sort Last Updated tetap aktif, dan page size tetap 25

### Retensi Saat Pindah Sub-Tab

7. Klik sub-tab "User List"
8. Klik kembali sub-tab "Position"
9. Verifikasi kata kunci Search "Manager", status sort, dan kondisi tabel tetap dipertahankan

### Reset State Saat Navigasi Sidebar

10. Klik menu sidebar Global Settings > User
11. Klik sub-tab "Position"
12. Verifikasi seluruh kondisi tabel telah direset ke default: search kosong, sort kembali Name A-Z, dan halaman kembali ke halaman 1

## Notes

- Menggabungkan TC-GS-POS-13, 14, dan 15.
