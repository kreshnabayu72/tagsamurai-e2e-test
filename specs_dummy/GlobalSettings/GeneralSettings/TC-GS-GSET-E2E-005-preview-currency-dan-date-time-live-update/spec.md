---
id: TC-GS-GSET-E2E-005-preview-currency-dan-date-time-live-update
title: "Preview Currency dan Preview Date & Time: update langsung mengikuti pilihan field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-30
  - TC-GS-GSET-31
  - TC-GS-GSET-32
coverage:
  web: automated
---

# Preview Currency dan Preview Date & Time: update langsung mengikuti pilihan field

## Prerequisites

- Login sebagai Role: Total Control
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
- Tanggal referensi Preview: Jumat 17 Maret 2023, pukul 14:30; nominal `5.000,00`
- `[simbol opsi X]` = simbol yang tampil pada label opsi untuk kode X

## Test Steps

### Preview Currency

1. Buka Global Settings > General Settings
2. Pilih Currency Code `USD` dan amati Preview text Currency
3. Verifikasi Preview "[simbol opsi USD] 5.000,00"
4. Pilih Currency Code `EUR` dan amati Preview text Currency
5. Verifikasi Preview "[simbol opsi EUR] 5.000,00"
6. Pilih Currency Code `IDR` dan amati Preview text Currency
7. Verifikasi Preview "Rp 5.000,00"
8. Verifikasi pemisah ribuan titik dan desimal koma tetap untuk `USD`, `EUR`, dan `IDR`, dan selalu 2 digit desimal

### Preview Date & Time

9. Amati Preview Date & Time awal
10. Verifikasi Preview "17/03/23 14:30"
11. Pilih Date Format `M/d/yy` dan amati Preview
12. Verifikasi Preview "3/17/23 14:30"
13. Pilih Date Format `dd MMM yy` dan amati Preview
14. Verifikasi Preview "17 Mar 23 14:30"
15. Pilih Date Format `DDD, MMM dd, yy` dan amati Preview
16. Verifikasi Preview "Fri, Mar 17, 23 14:30"
17. Pilih Date Format `DDD, MMM dd, yyyy` dan Time Format `hh:mm a` lalu amati Preview
18. Verifikasi Preview "Fri, Mar 17, 2023 02:30 PM"

### Time Zone Tidak Mengubah Preview

19. Pilih Time Zone Lain (opsi mana pun selain `Asia/Jakarta`) dan amati Preview Date & Time
20. Verifikasi Preview Date & Time tetap "17/03/23 14:30" (mengikuti hanya Date Format + Time Format)
21. Verifikasi tombol "Save" enabled

## Notes

- Menggabungkan TC-GS-GSET-30, TC-GS-GSET-31, dan TC-GS-GSET-32 (Preview live update kelima field).
