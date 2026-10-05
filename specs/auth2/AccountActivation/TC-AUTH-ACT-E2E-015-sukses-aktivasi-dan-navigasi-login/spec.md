---
id: TC-AUTH-ACT-E2E-015-sukses-aktivasi-dan-navigasi-login
title: Halaman Activation Success, reload setelah sukses, browser back, dan navigasi ke Login
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-50
  - TC-AUTH-ACT-51
  - TC-AUTH-ACT-52
  - TC-AUTH-ACT-53
  - TC-AUTH-ACT-54
  - TC-AUTH-ACT-55
  - TC-AUTH-ACT-56
coverage:
  web: automated
---

# Halaman Activation Success, reload setelah sukses, browser back, dan navigasi ke Login

## Prerequisites

- Token valid `active` tersedia untuk melakukan aktivasi sukses.
- Hook `beforeEach` menyiapkan state bersih dan token valid baru.
- Setelah aktivasi sukses, token menjadi `consumed`. State ini dipertahankan untuk verifikasi reload dan navigasi.
- Akses untuk menguji browser back behavior (history navigation).

## Test Steps

### A. Tampilan halaman sukses

1. Lakukan aktivasi sukses dengan token valid (isi password valid dan klik `[Set Password]`).
2. Verifikasi redirect ke halaman Activation Success.
3. Verifikasi terdapat ilustrasi sukses.
4. Verifikasi title halaman adalah `"Account Activated"`.
5. Verifikasi body text adalah `"Your account is now active. You can log in with your new password."`.
6. Verifikasi tombol CTA `"Go to Login"` tampil.
7. Verifikasi hanya ada 1 CTA (`Go to Login`) dan tidak ada link/tombol lain di halaman ini.

### B. Reload setelah sukses → 404 "Used"

8. Tetap berada di halaman Activation Success atau simpan URL `/activate?token={consumedToken}` (token yang baru saja dikonsumsi).
9. Reload halaman `/activate?token={sameToken}`.
10. Verifikasi halaman 404 dirender dengan title `"Link Already Used"`.
11. Verifikasi body varian "Used" sesuai copy dan menampilkan CTA `"Go to Login"`.

### C. Browser back button setelah sukses

12. Lakukan aktivasi sukses baru dengan token valid berbeda (melalui setup ulang).
13. Setelah berada di halaman Activation Success, klik tombol Back pada browser.
14. Verifikasi tidak terjadi resubmit form lama.
15. Verifikasi saat kembali ke `/activate?token={consumedToken}`, halaman menampilkan 404 (token sudah consumed), bukan form Set Password stale.

### D. Navigasi ke Login dari halaman Success

16. Lakukan aktivasi sukses dengan token valid baru (atau kembali ke state halaman Success).
17. Klik tombol `"Go to Login"` pada halaman Activation Success.
18. Verifikasi redirect langsung ke halaman **Login with Password**, tanpa cek sesi lain.

### E. Navigasi ke Login dari halaman 404 "Used"

19. Akses halaman 404 varian "Link Already Used" (misalnya dengan token yang sudah consumed).
20. Klik tombol `"Go to Login"` pada halaman 404 varian "Link Already Used".
21. Verifikasi redirect ke halaman **Login with Password**, perilaku identik dengan navigasi dari halaman Success (TC-AUTH-ACT-55).

### F. Zero-logging klik CTA Go to Login

22. Catat jumlah entri pada keempat surface log (Activity Log, User Log, System Log, Changelog) sebagai baseline.
23. Klik `"Go to Login"` dari halaman Success atau halaman 404 "Used".
24. Verifikasi tidak ada entri log baru terkait klik CTA ini (jumlah entri tetap sama dengan baseline).

## Notes

- Verifikasi browser back behavior (langkah 12-15) penting untuk mencegah resubmit form stale setelah aktivasi berhasil.
- Setelah sukses, token menjadi consumed - reload harus mengarahkan ke 404 varian "Used" (TC-AUTH-ACT-51).
- Navigasi ke Login dari Success dan dari 404 "Used" harus identik (TC-AUTH-ACT-54, TC-AUTH-ACT-55).
- Klik CTA Go to Login tidak boleh dicatat di log manapun (TC-AUTH-ACT-56).
