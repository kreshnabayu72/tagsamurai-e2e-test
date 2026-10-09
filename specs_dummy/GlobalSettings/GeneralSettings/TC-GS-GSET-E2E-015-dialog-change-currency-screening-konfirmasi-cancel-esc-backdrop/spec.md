---
id: TC-GS-GSET-E2E-015-dialog-change-currency-screening-konfirmasi-cancel-esc-backdrop
title: "Dialog Change Currency: screening tanpa request, konfirmasi melanjutkan Save, Cancel/Esc/backdrop menutup tanpa menyimpan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-37
  - TC-GS-GSET-38
  - TC-GS-GSET-39
  - TC-GS-GSET-40
  - TC-GS-GSET-115
coverage:
  web: automated
---

# Dialog Change Currency: screening tanpa request, konfirmasi melanjutkan Save, Cancel/Esc/backdrop menutup tanpa menyimpan

## Prerequisites

- Login sebagai Role: Total Control
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
- `[simbol opsi USD]` = simbol yang tampil pada label opsi untuk kode USD

## Test Steps

### Screening Dialog

1. Buka Global Settings > General Settings
2. Pilih Currency Code `USD` lalu klik `[Save]`
3. Verifikasi dialog muncul sebelum request simpan terkirim (tidak ada request PUT)
4. Verifikasi Title "Change Currency"
5. Verifikasi Body persis "Amounts already entered elsewhere in the app (e.g. Purchase Price) will not be converted — they'll simply be displayed under the new currency symbol. For example, an amount saved as 7,000 will still show as 7,000 — just with the new symbol. No conversion is applied. Are you sure you want to change the currency?"
6. Verifikasi Footer: `[Cancel]` (text, contrast) dan `[Change Currency]` (primary)

### Konfirmasi Melanjutkan Save

7. Klik `[Change Currency]`
8. Verifikasi dialog tertutup dan request simpan terkirim, lalu toast sukses "Success, general settings has been saved."
9. Verifikasi Button "Save" disabled dan Preview Currency "[simbol opsi USD] 5.000,00"
10. Refresh halaman (F5) dan verifikasi Currency Code `USD` tersimpan; Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes` tidak berubah

### Cancel Menutup Tanpa Menyimpan

11. Pilih Currency Code `USD`, klik `[Save]`, lalu klik `[Cancel]`
12. Verifikasi dialog tertutup tanpa request simpan dan tanpa toast
13. Verifikasi Currency Code tetap `USD` (tidak reset ke nilai lama), form tetap unsaved, dan Button "Save" enabled
14. Refresh halaman (F5) dan verifikasi Currency Code kembali `IDR` (tidak tersimpan)

### Esc Setara Cancel

15. Pilih Currency Code `USD`, klik `[Save]`, lalu tekan `Esc`
16. Verifikasi dialog tertutup (setara Cancel) tanpa request simpan dan tanpa toast, Currency Code tetap `USD`, dan fokus terjebak di dalam dialog selama terbuka

### Backdrop Tidak Menutup

17. Pilih Currency Code `USD`, klik `[Save]`, lalu klik area backdrop di luar dialog
18. Verifikasi Dialog Change Currency tetap terbuka dan tidak ada request simpan

## Notes

- Menggabungkan TC-GS-GSET-37 (screening), 38 (konfirmasi), 39 (Cancel), 40 (Esc), dan 115 (backdrop tidak menutup). Langkah 10 dan 14 mengasersi nilai tersimpan di server setelah refresh.
