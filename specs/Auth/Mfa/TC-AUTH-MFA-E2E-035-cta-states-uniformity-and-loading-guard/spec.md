---
id: TC-AUTH-MFA-E2E-035-cta-states-uniformity-and-loading-guard
title: State CTA disabled label seragam Login dan loading guard double submit
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-71
  - TC-AUTH-MFA-72
  - TC-AUTH-MFA-73
coverage:
  web: automated
---

# State CTA disabled label seragam Login dan loading guard double submit

## Prerequisites

- Mode: FE+BE
- Halaman alur MFA (Choose Method / Authenticator Verification)

## Test Steps

1. Buka halaman Choose Method dan amati tombol utama
2. Verifikasi tombol CTA dalam keadaan disabled sebelum ada opsi yang dipilih
3. Verifikasi label tombol bertuliskan "Login" secara seragam lintas halaman MFA
4. Pilih salah satu opsi dan lakukan klik tombol `[Login]`
5. Verifikasi saat request berlangsung tombol berubah menjadi disabled dan menampilkan indikator loading / spinner
6. Verifikasi tombol tidak dapat diklik ulang selama proses berlangsung untuk mencegah double submit

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-35`
- Merepresentasikan `TC-AUTH-MFA-71`, `72`, `73` (FE Ref: `TC-AUTH-MFA-FE-35`).
