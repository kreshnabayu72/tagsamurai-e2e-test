---
id: TC-GS-ACTLOG-E2E-044-sanitasi-xss-search-box-dan-kolom-ip-address-tanpa-masking
title: "Sanitasi input XSS pada Search Box dan penegasan IP Address ditampilkan penuh tanpa masking"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-230
  - TC-GS-ACTLOG-231
coverage:
  web: automated
---

# Sanitasi input XSS pada Search Box dan penegasan IP Address ditampilkan penuh tanpa masking

## Prerequisites

- Login sebagai Role: Total Control pada Tab Session

## Test Steps

1. Buka Tab Session
2. Masukkan payload script `<script>alert(1)</script>` pada kotak Search Toolbar lalu tekan Enter
3. Verifikasi payload diperlakukan murni sebagai teks biasa, tidak dieksekusi, dan tidak ada dialog popup script yang jalan
4. Amati nilai pada kolom IP Address di tabel Tab Session
5. Verifikasi alamat IP ditampilkan penuh secara utuh (mis. `192.168.1.100`) dan tidak di-mask sebagian (karena akses terbatas pada Total Control dan Read Only untuk kebutuhan audit)

## Notes

- Masking IP tidak diterapkan karena mengurangi utilitas investigasi forensik dan akses menu sudah diproteksi ketat.
