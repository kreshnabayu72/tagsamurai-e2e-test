---
id: TC-GS-GSET-E2E-013-save-per-field-saving-state-dan-guard-klik-ganda
title: "Save per field (Time Zone, Date Format, Time Format, Session Idle Timeout), tanpa dialog non-Currency, state Saving beku, dan guard klik ganda"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-33
  - TC-GS-GSET-34
  - TC-GS-GSET-35
  - TC-GS-GSET-36
  - TC-GS-GSET-41
  - TC-GS-GSET-44
  - TC-GS-GSET-45
coverage:
  web: automated
---

# Save per field (Time Zone, Date Format, Time Format, Session Idle Timeout), tanpa dialog non-Currency, state Saving beku, dan guard klik ganda

## Prerequisites

- Login sebagai Role: Total Control
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
- Spectra.intercept() dikonfigurasi untuk menahan (delay 5 detik) respons PUT general settings pada bagian State Saving

## Test Steps

### Save Time Zone

1. Pilih Time Zone Lain lalu klik `[Save]`
2. Verifikasi tidak ada dialog tambahan sebelum request simpan
3. Verifikasi toast sukses "Success, general settings has been saved." dan Button "Save" kembali disabled
4. Refresh halaman (F5) dan verifikasi Time Zone Lain tersimpan, sedangkan Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Session Idle Timeout `30 minutes` tidak berubah

### Save Date Format

5. Pilih Date Format `M/d/yy` lalu klik `[Save]`
6. Verifikasi tidak ada dialog tambahan, toast sukses tampil, Button "Save" disabled, dan Preview Date & Time "3/17/23 14:30"
7. Refresh halaman (F5) dan verifikasi Date Format `M/d/yy` tersimpan, field lain tetap baseline

### Save Time Format

8. Pilih Time Format `hh:mm a` lalu klik `[Save]`
9. Verifikasi tidak ada dialog tambahan, toast sukses tampil, Button "Save" disabled, dan Preview Date & Time "17/03/23 02:30 PM"
10. Refresh halaman (F5) dan verifikasi Time Format `hh:mm a` tersimpan, field lain tetap baseline

### Save Session Idle Timeout

11. Pilih Session Idle Timeout `1 hour` lalu klik `[Save]`
12. Verifikasi tidak ada dialog tambahan, toast sukses tampil, Button "Save" disabled
13. Refresh halaman (F5) dan verifikasi Session Idle Timeout `1 hour` tersimpan, field lain tetap baseline

### Save Tanpa Perubahan Currency Code

14. Pilih Date Format `M/d/yy` dan Session Idle Timeout `1 hour` lalu klik `[Save]`
15. Verifikasi request simpan langsung terkirim tanpa dialog, toast sukses tampil, dan Button "Save" disabled

### State Saving Form Beku

16. Aktifkan penundaan (delay 5 detik) respons PUT general settings
17. Pilih Session Idle Timeout `1 hour` lalu klik `[Save]`
18. Verifikasi Button "Save" menampilkan loading state
19. Coba ubah Select "Date Format" selama menunggu; verifikasi kelima Select dibekukan dan tidak dapat diubah
20. Setelah respons diterima, verifikasi toast sukses "Success, general settings has been saved."

### Guard Klik Ganda

21. Lepas penundaan, pilih Session Idle Timeout `1 hour`, lalu klik ganda cepat `[Save]`
22. Verifikasi hanya 1 request simpan terkirim (Button "Save" disabled + loading setelah klik pertama) dan hanya satu toast sukses "Success, general settings has been saved."
23. Buka Modal Changelog dan verifikasi tepat 1 baris baru untuk Field `Session Idle Timeout`

## Notes

- Menggabungkan TC-GS-GSET-33, 34, 35, 36 (save per field), TC-GS-GSET-41 (save tanpa dialog non-Currency), TC-GS-GSET-44 (state Saving form beku), dan TC-GS-GSET-45 (guard klik ganda). Intercept delay hanya untuk bagian State Saving.
