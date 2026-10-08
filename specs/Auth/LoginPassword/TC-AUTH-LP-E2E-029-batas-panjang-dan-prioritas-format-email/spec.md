---
id: TC-AUTH-LP-E2E-029-batas-panjang-dan-prioritas-format-email
title: Batas panjang karakter dan prioritas format pada field Email
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-LP-17
  - TC-AUTH-LP-161
coverage:
  web: automated
---

# Batas panjang karakter dan prioritas format pada field Email

## Prerequisites

- User belum login (guest); browser web diarahkan ke URL `/login`.
- Environment uji terisolasi khusus pengujian otomatis.
- Password valid `Spectra.env.AUTH_PASSWORD` tersedia di environment variables.
- Data fixture `Fixture.authLoginPassword` tersedia untuk nilai email batas karakter.
- Endpoint reCAPTCHA dapat diselesaikan otomatis atau dilewati melalui token bypass uji automation.

## Test Steps

### Validasi batas panjang karakter Email

1. Buka halaman Login with Password di browser web
2. Masukkan email dengan total 120 karakter (103 karakter `a` diikuti `@qwertysystem.net`) yang belum terdaftar
3. Selesaikan reCAPTCHA lalu klik tombol [Log in]
4. Verifikasi caption "Max. 120 characters" tidak tampil
5. Verifikasi caption inline "Email is not registered yet" tampil di bawah field Email, membuktikan 120 karakter lolos validasi panjang
6. Ketik 1 karakter tambahan pada field Email sehingga panjangnya menjadi 121 karakter
7. Verifikasi caption inline "Max. 120 characters" langsung muncul saat mengetik sebelum tombol [Log in] diklik
8. Selesaikan reCAPTCHA lalu klik tombol [Log in] (input tidak diblok pada karakter ke-121)
9. Verifikasi caption "Max. 120 characters" tetap bertahan di bawah field Email, sedangkan caption "Email is not registered yet" dan Alert pesan server tidak tampil, serta tidak ada sesi yang dibuat (request ditolak server dengan caption yang sama)

### Format email menang atas batas panjang

10. Ganti isi field Email dengan 121 karakter `a` tanpa tanda `@`
11. Pindahkan fokus ke field lain (blur)
12. Verifikasi caption inline "Email format is incorrect" tampil dan caption "Max. 120 characters" tidak tampil
13. Masukkan password `Spectra.env.AUTH_PASSWORD`, selesaikan reCAPTCHA, lalu klik tombol [Log in]
14. Verifikasi caption "Email format is incorrect" tetap tampil, sedangkan caption "Max. 120 characters" dan "Email is not registered yet" tidak tampil, serta tidak ada sesi yang dibuat
15. Verifikasi tidak ada entri log baru untuk percobaan ini

## Notes

- Batas maksimal 120 karakter memicu pesan "Max. 120 characters" secara langsung saat pengetikan melebihi kuota (`NC-08`); input tidak diblok pada karakter ke-121 dan ditolak server dengan caption yang sama (`V-AUTHLP-03`, `TC-AUTH-LP-17`).
- Format email salah menang atas batas panjang saat blur/submit, sehingga caption "Email format is incorrect" yang tampil untuk input 121 karakter tanpa `@` (`V-AUTHLP-03`, `TC-AUTH-LP-161`).
- Spec ini dipecah dari E2E-001 agar uji boundary panjang karakter terisolasi dari screening dan validasi format biasa (lihat `gap-spec/gap-spec.md` GAP-LP-E2E-009).