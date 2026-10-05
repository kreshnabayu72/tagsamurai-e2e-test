---
id: TC-AUTH-ACT-E2E-009-toggle-show-hide-a11y-no-captcha-button-state
title: Toggle show/hide independen, aksesibilitas keyboard, ketiadaan CAPTCHA, dan state tombol
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-35
  - TC-AUTH-ACT-36
  - TC-AUTH-ACT-37
  - TC-AUTH-ACT-38
  - TC-AUTH-ACT-39
coverage:
  web: automated
---

# Toggle show/hide independen, aksesibilitas keyboard, ketiadaan CAPTCHA, dan state tombol

## Prerequisites

- Token valid `active` tersedia, halaman Set Password `/activate?token={validToken}` terbuka.
- Hook `beforeEach` mengembalikan form ke state kosong/default.

## Test Steps

### A. Toggle show/hide password

1. Isi field Password dengan satu nilai.
2. Klik ikon mata (eye icon) pada field Password.
3. Verifikasi teks password terlihat dan tooltip berubah sesuai state aplikasi.
4. Klik kembali ikon mata pada field Password.
5. Verifikasi teks password kembali tersembunyi dan tooltip kembali sesuai state aplikasi.
6. Verifikasi nilai pada field Password tidak hilang saat ikon mata diklik.

### B. Toggle independen per field

7. Isi field Password dan field Confirm Password dengan nilai.
8. Toggle show/hide hanya pada field Password.
9. Verifikasi field Confirm Password tetap dalam state tersembunyi (tidak ikut ter-toggle).
10. Verifikasi state masing-masing field independen.

### C. Aksesibilitas keyboard (eye icon)

11. Pindahkan fokus keyboard (Tab) ke ikon mata pada field Password.
12. Verifikasi ikon mata mendapatkan fokus yang terlihat (focus ring).
13. Tekan `Enter` atau `Space` pada ikon mata yang sedang difokus.
14. Verifikasi toggle show/hide berfungsi melalui keyboard.

### D. Ketiadaan CAPTCHA & state tombol

15. Buka halaman Set Password dalam state form kosong (default).
16. Verifikasi tidak ada elemen CAPTCHA/reCAPTCHA di DOM halaman ini.
17. Verifikasi tombol `"Set Password"` selalu enabled sejak awal, meski checklist 6 baris masih berwarna abu-abu.
18. Verifikasi validasi terjadi saat submit (bukan dengan mendisable tombol).

## Notes

- Label tombol sesuai konvensi: `[Set Password]`.
