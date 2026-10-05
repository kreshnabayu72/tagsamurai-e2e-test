---
id: TC-AUTH-ACT-E2E-011-concurrency-race-tab-resend-midfill
title: Race condition - token dikonsumsi di tab lain & resend mid-fill
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-43
  - TC-AUTH-ACT-44
coverage:
  web: automated
---

# Race condition - token dikonsumsi di tab lain & resend mid-fill

## Prerequisites

- Token valid `active` tersedia.
- Kemampuan membuka multiple tab/context atau simulasi state concurrency.
- Akses admin untuk melakukan Resend Activation Email (via UI/API).

## Test Steps

### A. Token dikonsumsi di tab lain (race antar tab)

1. Buka link aktivasi yang sama di 2 tab (Tab 1 dan Tab 2). Keduanya menampilkan form Set Password dengan token yang sama (`active`).
2. Di Tab 1, isi password valid dan submit → aktivasi berhasil, token menjadi `consumed`.
3. Di Tab 2 (form masih terbuka), isi password valid dan submit.
4. Verifikasi re-validate gagal (409/404) dan terjadi redirect ke halaman **404**.
5. Verifikasi password **tidak** ter-set ulang sebagai efek dari submit Tab 2.
6. Verifikasi token tetap `consumed` dari Tab 1, kredensial user tidak berubah lagi.

### B. Resend terjadi saat user sedang mengisi form (token disupersede mid-fill)

7. Siapkan user dengan token `active` (token lama). Buka halaman Set Password dengan token lama, form terbuka (belum submit).
8. Lakukan Resend Activation Email sehingga token lama menjadi `superseded` dan token baru dibuat `active`.
9. Dengan form masih terbuka (menggunakan token lama), user submit password valid.
10. Verifikasi submit gagal saat re-validate dan redirect ke halaman **404**.
11. Verifikasi token baru (dari resend) tetap `active` dan terpisah dari token lama yang `superseded`.

## Notes

- Race condition diuji untuk memastikan transaksionalitas dan tidak ada double-consume.
