---
id: TC-GS-POS-E2E-049-loading-failure-slow-response-mock
title: Loading State, Kegagalan Server, dan Respons Lambat di Seluruh Endpoint (Mock)
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-POS-20
  - TC-GS-POS-53
  - TC-GS-POS-74
  - TC-GS-POS-93
  - TC-GS-POS-94
  - TC-GS-POS-95
  - TC-GS-POS-109
  - TC-GS-POS-226
coverage:
  web: automated
mock: true
---

# Loading State, Kegagalan Server, dan Respons Lambat di Seluruh Endpoint (Mock)

## Prerequisites

- Mode: mock
- Skenario ini menggunakan **mock** (hanya 049 dan 050 boleh memakai mock).
- Mock endpoint API Position (list, create, edit, delete, changelog, download) untuk mensimulasikan slow response, 4xx/5xx, timeout, network error.
- Environment test mendukung API interception/mock sesuai framework.

## Test Steps

### A. Loading state

1. Mock list Position dengan delay lambat → buka halaman tab Position.
2. Verifikasi indikator loading/skeleton tampil selama data belum termuat.
3. Verifikasi tabel tidak kosong/error sebelum data selesai, lalu terisi saat response berhasil.
4. Uji loading pada operasi Create/Edit/Delete (submit) → tombol disabled/loading state selama request berjalan.
5. Uji loading pada Popup Changelog (load list changelog) dan Download (jika ada indikator).

### B. Kegagalan server (5xx)

6. Mock list Position return 500 → buka halaman Position.
7. Verifikasi pesan error/empty state error sesuai konvensi aplikasi muncul, tidak crash.
8. Mock Create return 500 → submit form → verifikasi toast error dan form tetap terbuka (dirty state terjaga sesuai kebutuhan).
9. Mock Edit return 500 → submit edit → toast error, perubahan tidak tersimpan.
10. Mock Delete return 500 → konfirmasi delete → toast error, record tetap ada.
11. Mock Changelog list return 500 → buka Popup Changelog → tampil error state.
12. Mock Download return 500 → klik download → tampil toast error `"Error, failed to download Changelog-Position."` atau sesuai konteks (sesuai TC-GS-POS-226).

### C. Kegagalan klien/4xx & validasi server

13. Mock Create return 400 (duplikat/validasi) → verifikasi pesan validasi terdisplay dengan benar.
14. Mock Edit return 404 (record not found) → verifikasi penanganan not found (toast/error sesuai konvensi).
15. Mock Delete return 404/409 (already deleted/in use) → verifikasi handling race/error sesuai kasus.

### D. Respons lambat & timeout

16. Mock dengan delay sangat lama (near-timeout) → verifikasi timeout handling dan pesan sesuai.
17. Batalkan/ulang permintaan jika memungkinkan, pastikan tidak ada double submit saat loading.

### E. Recovery

18. Kembalikan mock ke success → ulang operasi → berhasil normal.
19. Verifikasi state UI kembali bersih (tidak ada residual error/loading).

## Notes

- Hanya spec ini dan 050 yang boleh memakai mock. Fokus pada resiliensi UI (loading, error, timeout), bukan logika bisnis.
