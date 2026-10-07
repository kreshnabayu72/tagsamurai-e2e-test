---
id: TC-AUTH-MFA-E2E-035-rate-limiting-resilience-dan-toast-sticky
title: "Ketahanan Sistem: IP Rate Limit (429), Fault Injection 5xx, Toast Sticky T-01, dan ARIA Live"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-12
  - TC-AUTH-MFA-83
  - TC-AUTH-MFA-84
  - TC-AUTH-MFA-192
  - TC-AUTH-MFA-193
  - TC-AUTH-MFA-197
  - TC-AUTH-MFA-198
  - TC-AUTH-MFA-199
  - TC-AUTH-MFA-201
  - TC-AUTH-MFA-202
  - TC-AUTH-MFA-203
  - TC-AUTH-MFA-204
  - TC-AUTH-MFA-205
coverage:
  web: automated
---
# Ketahanan Sistem: IP Rate Limit (429), Fault Injection 5xx, Toast Sticky T-01, dan ARIA Live

## Prerequisites

- Mode: mock (failure injection 5xx, network timeout, direct burst HTTP harness).
- User `Resilience User` (`resilience@qwertysystem.net`) profil NEWDEV.
- Mail-catcher lingkungan uji aktif.

## Test Steps

### Penolakan IP Rate Limit (Status 429) pada aksi Kirim OTP dan Verifikasi

1. Kirim request pengiriman OTP berulang dari alamat IP yang sama hingga melampaui ambang batas rate limit
2. Verifikasi sistem menolak request (HTTP 429) dan menampilkan caption error inline: "Too many requests. Please try again later."
3. Kirim request verifikasi OTP berulang dari IP yang sama hingga melebihi ambang batas
4. Verifikasi server mengembalikan status 429 dan UI menampilkan caption "Too many requests. Please try again later."
5. Kirim request verifikasi Authenticator berulang hingga terkena rate limit
6. Verifikasi caption "Too many requests. Please try again later." muncul dan nilai angka di dalam kotak digit tetap dipertahankan (tidak dikosongkan, sesuai TC-193)

### Fault Injection 5xx pada Evaluasi MFA dan Idempotensi Retry

7. Konfigurasikan mock error 500 saat evaluasi pemicu MFA dipanggil
8. Verifikasi toast error persisten tampil: "Error, failed to log in." (T-01)
9. Matikan simulasi error dan klik [Log in] kembali
10. Verifikasi retry evaluasi bersifat idempotent dan pengguna diarahkan ke Choose Verification Method secara normal

### Ketahanan terhadap kegagalan server 5xx dan persistensi Toast T-01

11. Buka form verifikasi faktor-2 dan masukkan kode valid
12. Simulasikan kegagalan server 5xx saat verifikasi dikirim
13. Verifikasi toast error persisten T-01 tampil di pojok kanan bawah: "Error, failed to log in."
14. Verifikasi isi kotak digit tetap dipertahankan (tidak dibersihkan saat 5xx)
15. Tunggu selama 10 detik dan verifikasi toast T-01 TIDAK hilang secara otomatis (bersifat sticky)
16. Klik tombol close [x] pada toast dan verifikasi toast tertutup secara manual
17. Hentikan mock 5xx, klik tombol submit verifikasi kembali dan verifikasi login berhasil tanpa sesi ganda

### Aksesibilitas ARIA Live pada caption error

18. Masukkan kode verifikasi yang salah pada form verifikasi
19. Verifikasi elemen caption error memiliki atribut ARIA live (`role="alert"` / `aria-live="polite"`) sehingga terbaca oleh pembaca layar (screen reader)

## Notes

- Sesuai PRD §7, toast error T-01 `"Error, failed to log in."` bersifat sticky dan wajib ditutup manual oleh pengguna.
- Nilai kotak digit tidak di-clear saat terjadi error 5xx atau rate limit 429.
