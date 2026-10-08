---
id: TC-AUTH-LP-E2E-011-agreement-gate-konfirmasi-dan-siklus-persetujuan
title: Konfirmasi Agreement, validasi checkbox, pemulihan, dan handoff ke MFA
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-82
  - TC-AUTH-LP-83
  - TC-AUTH-LP-84
  - TC-AUTH-LP-85
  - TC-AUTH-LP-86
coverage:
  web: automated
---

# Konfirmasi Agreement, validasi checkbox, pemulihan, dan handoff ke MFA

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- User `tonokurniawan@qwertysystem.net`, `sitirahmawati@qwertysystem.net`.

## Test Steps

### Validasi penolakan submit tanpa centang checkbox

1. Buka halaman Login with Password di browser web
2. Login menggunakan email `tonokurniawan@qwertysystem.net` dan password `QaLogin#2026` sampai layar Confirm to Continue tampil
3. Biarkan checkbox unchecked lalu klik tombol [Continue ➔]
4. Verifikasi checkbox berada dalam status invalid (severity danger)
5. Verifikasi caption inline "You need to agree to the Privacy Policy to continue" tampil tepat di bawah checkbox
6. Verifikasi tombol [Continue ➔] tetap enabled dan browser tidak berpindah halaman

### Pemulihan: Centang checkbox dan submit berhasil

7. Centang checkbox persetujuan
8. Verifikasi caption inline "You need to agree to the Privacy Policy to continue" langsung hilang
9. Klik tombol [Continue ➔]
10. Verifikasi browser berpindah menuju Portal — Product Hub
11. Lakukan logout lalu login kembali dengan `tonokurniawan@qwertysystem.net`
12. Verifikasi layar Confirm to Continue tidak tampil lagi pada login berikutnya untuk versi policy yang sama

### Alur kombinasi Agreement dengan MFA handoff

13. Login menggunakan `sitirahmawati@qwertysystem.net` (login pertama) sampai layar Confirm to Continue tampil
14. Centang checkbox persetujuan lalu klik tombol [Continue ➔]
15. Verifikasi browser dialihkan ke halaman MFA (bukan langsung ke Portal) karena akun belum menyelesaikan MFA

## Notes

- Submit tanpa centang checkbox ditolak dengan caption inline dan tombol tetap enabled tanpa perpindahan halaman (`FI-AUTHLP-11`, `TC-AUTH-LP-82`).
- Persetujuan untuk versi policy aktif bersifat satu kali: layar Confirm tidak tampil lagi pada login berikutnya (`TC-AUTH-LP-83`, `TC-AUTH-LP-84`, `TC-AUTH-LP-85`, PRD F-AUTHLP-09).
- Handoff gabungan Agreement → MFA mengarahkan user ke halaman MFA sebelum Portal (`TC-AUTH-LP-86`).
- Lifecycle, perkalian versi dokumen, dan idempotensi token pre-auth dipecah ke spec tersendiri E2E-027; kondisi "meninggalkan layar tanpa Continue" dipindah ke E2E-028 (lihat `gap-spec/gap-spec.md` GAP-LP-E2E-009).
