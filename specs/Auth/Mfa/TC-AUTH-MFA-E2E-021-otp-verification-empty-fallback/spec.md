---
id: TC-AUTH-MFA-E2E-021-otp-verification-empty-fallback
title: Validasi kode OTP kosong via tombol fallback Verify setelah error jaringan
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-37
coverage:
  web: automated
---

# Validasi kode OTP kosong via tombol fallback Verify setelah error jaringan

## Prerequisites

- Mode: mock
- Mode: mock (simulasikan network error pada auto-submit sehingga tombol fallback `[Verify]` muncul)
- Kotak input OTP dalam keadaan belum terisi lengkap (<6 digit)

## Test Steps

1. Simulasikan kemunculan tombol fallback `[Verify]` setelah percobaan auto-submit sebelumnya gagal akibat gangguan jaringan
2. Hapus sebagian digit sehingga kotak input kode belum lengkap
3. Klik tombol `[Verify]`
4. Verifikasi sistem memvalidasi kelengkapan digit dan menampilkan caption error
5. Verifikasi tercatat di Activity Log Session dengan Status "Failed" dan Note "Empty OTP"

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-21`
- Merepresentasikan `TC-AUTH-MFA-37` (FE Ref: `TC-AUTH-MFA-FE-21`).
