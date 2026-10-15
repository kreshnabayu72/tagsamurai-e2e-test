---
id: TC-AUTH-ACT-E2E-007-toggle-show-hide-ikon-dan-tooltip
title: "Toggle show/hide independen per field beserta ikon dan tooltip sesuai state"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-19
  - TC-AUTH-ACT-20
  - TC-AUTH-ACT-21
coverage:
  web: automated
---

# Toggle show/hide independen per field beserta ikon dan tooltip sesuai state

## Prerequisites

- Browser publik tanpa sesi login.
- User seeding milik automation berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run).
- Akses API read-only untuk memastikan token tetap Active (spec ini tidak pernah men-submit form).

## Test Steps

### Toggle pada field Password tidak memengaruhi Confirm Password (TC-AUTH-ACT-19)

1. Buka link aktivasi user seeding → halaman Set Password tampil.
2. Ketik `Aman#Sandi8` pada field Password dan `Aman#Sandi8` pada field Confirm Password.
3. Klik ikon toggle di field Password.
4. Verifikasi teks field Password terlihat sebagai `Aman#Sandi8` dan teks field Confirm Password tetap tersembunyi (masked).
5. Klik ikon toggle di field Password sekali lagi.
6. Verifikasi teks field Password kembali tersembunyi (masked) dan field Confirm Password tidak berubah.

### Toggle pada field Confirm Password independen dari field Password (TC-AUTH-ACT-20)

7. Klik ikon toggle di field Confirm Password.
8. Verifikasi teks field Confirm Password terlihat sebagai `Aman#Sandi8` dan teks field Password tetap tersembunyi (masked).
9. Klik ikon toggle di field Confirm Password sekali lagi.
10. Verifikasi teks field Confirm Password kembali tersembunyi (masked) dan field Password tidak berubah.

### Ikon dan tooltip mengikuti state field (TC-AUTH-ACT-21)

11. Pastikan teks field Password tersembunyi, lalu hover ikon toggle di field Password.
12. Verifikasi ikon `EyeLine` dengan tooltip "Show password" tampil saat teks tersembunyi.
13. Klik ikon toggle sehingga teks Password terlihat, lalu hover ikon yang sama.
14. Verifikasi ikon `EyeOffLine` dengan tooltip "Hide password" tampil saat teks terlihat.
15. Klik ikon toggle kembali sehingga teks Password tersembunyi.
16. Ulangi hover pada ikon toggle field Confirm Password pada kedua state (tersembunyi dan terlihat).
17. Verifikasi field Confirm Password menampilkan pasangan ikon dan tooltip yang sama dengan field Password pada tiap state.

## Notes

- Ketiga TC berbagi dataset dan topik aksi yang sama (menekan ikon toggle), sehingga digabung dalam satu sesi form.
- Verifikasi dilakukan tanpa submit sehingga token tetap Active dan tidak ada data yang berubah.
- Kebutuhan teknis dicatat di Prerequisites.
