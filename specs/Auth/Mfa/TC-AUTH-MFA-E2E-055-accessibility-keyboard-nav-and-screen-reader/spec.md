---
id: TC-AUTH-MFA-E2E-055-accessibility-keyboard-nav-and-screen-reader
title: Aksesibilitas keyboard fokus otomatis aria describedby teks alternatif QR dan role radio
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-110
  - TC-AUTH-MFA-111
  - TC-AUTH-MFA-112
  - TC-AUTH-MFA-113
coverage:
  web: automated
---

# Aksesibilitas keyboard fokus otomatis aria describedby teks alternatif QR dan role radio

## Prerequisites

- Mode: mock
- Halaman komponen MFA ter-render di browser

## Test Steps

### Fokus Otomatis & Aksesibilitas Keyboard
1. Buka form verifikasi OTP / Authenticator
2. Verifikasi fokus kursor secara otomatis berada di kotak input digit pertama
3. Uji navigasi keyboard (Tab dan Backspace) antar field

### Asosiasi Error dengan aria-describedby
4. Picu pesan error validasi
5. Verifikasi atribut `aria-describedby` pada field input mengarah ke elemen caption error dan `aria-invalid="true"` aktif

### Teks Alternatif QR Code
6. Buka halaman Setup Authenticator Step 1
7. Verifikasi elemen gambar QR code memiliki atribut `alt` yang bermakna bagi pengguna pembaca layar

### Semantik Radio Group pada Choose Method
8. Buka halaman Choose Method
9. Verifikasi kontainer kartu opsi memiliki atribut `role="radiogroup"` dan setiap Option Card memiliki `role="radio"`

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-55`
- Merepresentasikan `TC-AUTH-MFA-110`, `111`, `112`, `113` (FE Ref: `TC-AUTH-MFA-FE-55`).
