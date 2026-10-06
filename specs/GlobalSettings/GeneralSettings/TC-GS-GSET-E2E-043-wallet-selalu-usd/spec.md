---
id: TC-GS-GSET-E2E-043-wallet-selalu-usd
title: Wallet selalu USD, tanpa konsumsi currency_code
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-140
coverage:
  web: automated
---

# Wallet selalu USD dan tidak mengonsumsi currency_code

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Field `Currency` tersimpan `IDR`.
- Modul Wallet (selubung pembayaran) tersedia di environment untuk diverifikasi.

## Test Steps

1. Verifikasi field `Currency` pada General Settings saat ini `IDR`
2. Buka modul Wallet/selubung pembayaran yang relevan
3. Verifikasi nilai yang ditampilkan wallet menggunakan mata uang `USD` dan bukan mengikuti
   `currency_code` (`IDR`)
4. Verifikasi saat `currency_code` diubah (misal ke `USD`) di General Settings, tampilan wallet tetap
   `USD`
5. Verifikasi wallet tidak pernah menampilkan format `Rp` meskipun currency general setting `IDR`
6. Kembalikan `Currency` ke `IDR` bila diubah pada langkah 4

## Notes

- PMC `WALLET-USD-CONTRACT` terpenuhi: wallet tidak membaca/mengonsumsi `currency_code` dari General
  Settings; nilainya selalu `USD` (hard-coded/sumber terpisah).