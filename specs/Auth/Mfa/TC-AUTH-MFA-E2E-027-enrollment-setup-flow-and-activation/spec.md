---
id: TC-AUTH-MFA-E2E-027-enrollment-setup-flow-and-activation
title: Alur setup pendaftaran Authenticator Step 1 dan Step 2 hingga aktivasi inline
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-48
  - TC-AUTH-MFA-49
  - TC-AUTH-MFA-50
  - TC-AUTH-MFA-51
  - TC-AUTH-MFA-52
coverage:
  web: automated
---

# Alur setup pendaftaran Authenticator Step 1 dan Step 2 hingga aktivasi inline

## Prerequisites

- Mode: FE+BE
- User baru atau user yang belum pernah mendaftarkan Authenticator app
- Halaman setup Authenticator terbuka

## Test Steps

### Step 1: Screening Elemen Setup & Copy Key
1. Verifikasi heading halaman bertuliskan "Set up authenticator app"
2. Verifikasi QR code ter-render sebagai gambar
3. Verifikasi secret key ditampilkan dalam format terbaca ("XXXX XXXX XXXX XXXX")
4. Klik tombol `[Copy key]`
5. Verifikasi secret key tersalin ke clipboard dan tooltip menampilkan "Copy secret key"

### Step 2: Validasi Kode Salah (Manual Verify)
6. Buka bagian verifikasi kode setup Step 2
7. Masukkan 6 digit kode yang salah
8. Verifikasi tidak ada auto-submit saat digit ke-6 terisi
9. Klik tombol `[Verify]`
10. Verifikasi muncul caption error "Invalid code", halaman tetap pada Step 2, dan kejadian ini TIDAK dicatat di audit log

### Step 2: Verifikasi Kode Benar & Aktivasi Inline
11. Masukkan 6 digit kode yang dihasilkan dari secret key tersebut
12. Klik tombol `[Verify]`
13. Verifikasi status enrollment berubah menjadi aktif (`authenticator_enrollment.is_active = true`)
14. Verifikasi sistem langsung melanjutkan login final ke Portal tanpa memerlukan layar konfirmasi tambahan

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-27`
- Merepresentasikan `TC-AUTH-MFA-48`, `49`, `50`, `51`, `52` (FE Ref: `TC-AUTH-MFA-FE-27`).
