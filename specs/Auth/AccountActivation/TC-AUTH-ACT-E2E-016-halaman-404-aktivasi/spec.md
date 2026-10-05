---
id: TC-AUTH-ACT-E2E-016-halaman-404-aktivasi
title: Halaman 404 aktivasi, copy verbatim Expired/Used, dan anti-kebocoran penyebab teknis
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-57
  - TC-AUTH-ACT-58
  - TC-AUTH-ACT-59
  - TC-AUTH-ACT-60
coverage:
  web: automated
---

# Halaman 404 aktivasi, copy verbatim Expired/Used, dan anti-kebocoran penyebab teknis

## Prerequisites

- Berbagai state token tersedia melalui hook `before`: token expired (>24 jam), token consumed, token superseded (di-resend), token malformed/tidak dikenal, dan token untuk user yang dihapus/deactivated.
- Akses network response (DevTools) untuk memverifikasi response API tidak mengembalikan alasan spesifik ke client.
- Halaman 404 aktivasi dapat diakses dengan membuka `/activate?token={token}` sesuai state.

## Test Steps

### A. Copy verbatim varian Expired

1. Buka `/activate?token={expiredToken}` (token expired atau superseded).
2. Verifikasi title halaman adalah `"Activation Link Expired"`.
3. Verifikasi body text persis sesuai copy: `"This activation link has expired. Activation links are valid for 24 hours. Please contact your administrator to receive a new activation email."`.
4. Verifikasi tidak ada CTA pada halaman ini (hanya varian Used yang menampilkan CTA).

### B. Copy verbatim varian Used

5. Buka `/activate?token={consumedToken}` (token sudah consumed).
6. Verifikasi title halaman adalah `"Link Already Used"`.
7. Verifikasi body text persis sesuai copy: `"This activation link has already been used. Your account has been activated."`.
8. Verifikasi CTA `"Go to Login"` tampil pada halaman ini.

### C. Tidak ada kebocoran penyebab teknis

9. Uji berbagai kondisi invalid dengan membuka `/activate?token={token}` untuk: token expired, token consumed, token superseded, token malformed, token tidak dikenal, token untuk user yang dihapus/deactivated.
10. Verifikasi UI hanya menampilkan salah satu dari 2 copy di atas (Expired atau Used). Tidak ada varian ke-3 yang membocorkan "superseded", "malformed", "user deleted", "invalid format", atau alasan teknis lainnya secara eksplisit.
11. Verifikasi response API untuk permintaan validasi token pada kondisi-kondisi tersebut tidak mengembalikan field alasan spesifik yang bisa diekspos ke UI (cek network response). UI tetap hanya menampilkan copy generik sesuai mapping (Expired/Used).
12. Verifikasi mapping state token ke UI copy sesuai spesifikasi: superseded → 404 varian "Expired" (bukan "Used"); consumed → "Used"; expired → "Expired"; malformed/tidak dikenal/user deleted → 404 generik sesuai mapping aplikasi.

### D. Tidak ada aksi destruktif di halaman 404

13. Buka halaman 404 aktivasi untuk varian Expired.
14. Verifikasi tidak ada tombol delete, reset, retry-destruktif, atau aksi lain yang dapat mengubah state. Hanya (jika ada) CTA Go to Login yang bersifat navigasi.
15. Buka halaman 404 aktivasi untuk varian Used.
16. Verifikasi tidak ada aksi destruktif; hanya CTA `"Go to Login"`.
17. Verifikasi elemen interaktif hanya terbatas pada CTA navigasi yang aman.

## Notes

- Anti-kebocoran informasi penting untuk security (TC-AUTH-ACT-59). Response API tidak boleh membocorkan detail mengapa token invalid.
- Superseded token (< 24 jam) harus menampilkan varian "Expired", bukan "Used" (TC-AUTH-ACT-13).
- Hanya varian "Used" yang memiliki CTA Go to Login; varian "Expired" tidak memiliki CTA.
- Tidak ada varian ketiga - kedua copy ini cukup untuk semua kondisi invalid.
