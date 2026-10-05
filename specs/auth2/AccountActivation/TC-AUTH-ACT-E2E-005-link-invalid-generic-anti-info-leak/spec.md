---
id: TC-AUTH-ACT-E2E-005-link-invalid-generic-anti-info-leak
title: Link invalid/malformed/user-deleted → 404 generik & anti-kebocoran penyebab teknis
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-14
  - TC-AUTH-ACT-15
coverage:
  web: automated
---

# Link invalid/malformed/user-deleted → 404 generik & anti-kebocoran penyebab teknis

## Prerequisites

- Token malformed/tidak dikenal, kosong, injection-like tersedia.
- Token `active` untuk user yang telah di-deactivate/delete tersedia.
- Akses network response untuk verifikasi tidak ada bocoran alasan spesifik.

## Test Steps

### A. Token malformed / tidak dikenal / injection-like

1. Buka `/activate?token=` (token kosong).
2. Buka `/activate?token=invalid-malformed-token`.
3. Buka `/activate?token=' OR 1=1 --`.
4. Verifikasi untuk semua kasus di atas, halaman 404 generik dirender dan tidak membocorkan penyebab spesifik.
5. Verifikasi input injection-like tidak memengaruhi query/eksekusi SQL (dikonfirmasi melalui network response dan perilaku UI).

### B. User terkait dihapus / nonaktif

6. Buka `/activate?token={tokenForDeletedUser}` untuk user yang sudah di-deactivate atau di-delete.
7. Verifikasi halaman 404 dirender (token dianggap invalid), tanpa menyebutkan alasan "user deleted" secara eksplisit.

## Notes

- Anti-kebocoran informasi penting untuk security. Response API tidak boleh membocorkan detail mengapa token invalid.
