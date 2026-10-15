---
id: TC-GS-GSET-E2E-016-resilience-save-5xx-timeout-dan-currency-gagal
title: "Resilience Save: error 5xx (form unsaved, tab lain tak berubah), timeout, dan kegagalan pasca Change Currency"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-46
  - TC-GS-GSET-47
  - TC-GS-GSET-48
coverage:
  web: automated
---

# Resilience Save: error 5xx (form unsaved, tab lain tak berubah), timeout, dan kegagalan pasca Change Currency

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control pada tab pertama dan tab kedua (entitas sama)
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
- Spectra.intercept() dikonfigurasi untuk memaksa error HTTP 500 dan timeout (tanpa respons) pada endpoint PUT general settings

## Test Steps

### Error 5xx Mempertahankan Form Unsaved

1. Paksa PUT general settings gagal (5xx)
2. Di tab pertama pilih Session Idle Timeout `1 hour` lalu klik `[Save]`
3. Verifikasi toast error "Error, failed to save general settings."
4. Verifikasi form tetap terbuka, Session Idle Timeout tetap `1 hour` (input dipertahankan), dan Button "Save" kembali enabled
5. Di tab kedua refresh halaman dan verifikasi Session Idle Timeout tetap `30 minutes` (nilai tersimpan tidak berubah)
6. Kembali ke tab pertama, lepas intercept, lalu klik `[Save]` lagi
7. Verifikasi toast sukses "Success, general settings has been saved."

### Timeout

8. Buat PUT general settings tidak mendapat respons (timeout)
9. Pilih Time Format `hh:mm a` lalu klik `[Save]` dan tunggu hingga timeout
10. Verifikasi toast error "Error, failed to save general settings."
11. Verifikasi form tetap terbuka, Time Format tetap `hh:mm a`, dan Button "Save" enabled kembali

### Gagal 5xx Pasca Change Currency

12. Paksa PUT general settings gagal (5xx)
13. Pilih Currency Code `USD`, klik `[Save]`, lalu klik `[Change Currency]`
14. Verifikasi dialog tertutup dan toast error "Error, failed to save general settings."
15. Verifikasi Currency Code tetap `USD` (form unsaved) dan Button "Save" enabled
16. Refresh halaman (F5) dan verifikasi Currency Code `IDR` (tidak tersimpan)

## Notes

- Mode: mock untuk memaksa 500 dan timeout secara terkontrol (TC-GS-GSET-46, 47, 48). Langkah 5 dan 16 mengasersi nilai tersimpan di server.
