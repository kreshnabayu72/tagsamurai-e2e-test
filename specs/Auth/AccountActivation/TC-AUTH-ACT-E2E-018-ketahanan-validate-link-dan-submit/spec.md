---
id: TC-AUTH-ACT-E2E-018-ketahanan-validate-link-dan-submit
title: "Ketahanan Validate Link terhadap Error Server dan Timeout"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-02
  - TC-AUTH-ACT-03
  - TC-AUTH-ACT-04
  - TC-AUTH-ACT-05
  - TC-AUTH-ACT-06
coverage:
  web: automated
---

# Ketahanan Validate Link terhadap Error Server dan Timeout

## Prerequisites

- Mode: FE+BE dengan intercept parsial (backend nyata; asersi state token/user dicek ke backend). Respons dipaksa lewat `Spectra.intercept()` per TC:
  - TC-AUTH-ACT-02: `GET /v2/iam/auth/activation/{token}` ditahan 5 detik, lalu diteruskan normal
  - TC-AUTH-ACT-03: `GET /v2/iam/auth/activation/{token}` dipaksa HTTP 500 dengan body `{"message": "Internal server error"}` (contoh 500 di `openapi.yaml`); body yang sama dipakai untuk semua respons 500 di spec ini
  - TC-AUTH-ACT-04: `GET /v2/iam/auth/activation/{token}` tidak pernah dijawab sampai timeout klien
  - TC-AUTH-ACT-05: `GET /v2/iam/auth/activation/{token}` dipaksa HTTP 500, lalu intercept dilepas (respons normal)
  - TC-AUTH-ACT-06: `GET /v2/iam/auth/activation/{token}` dipaksa HTTP 500 untuk semua percobaan
- Hook `before` (seeding API oleh akun aktor Total Control (Global Settings) pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.GS_TC_PASSWORD`) membuat user berikut dengan suffix per run `+{runId}-018` beserta link aktivasinya, semuanya Pending Activation dengan token Active: `Siti Lestari` (TC-02), `Andi Saputra` (TC-03), `Dewi Maharani` (TC-04), `Rizky Hartono` (TC-05), `Nur Octaviani` (TC-06), masing-masing dengan email nama huruf kecil tanpa spasi + `+{runId}-018@qwertysystem.net` (contoh `sitilestari+{runId}-018@qwertysystem.net`). Hook `after` melepas semua intercept dan menghapus user tersebut (tetap jalan walau spec gagal di tengah).
- Tidak ada password atau token di spec atau fixture.
- Kemampuan teknis: intercept network di browser (delay, HTTP 500, tanpa respons sampai timeout).

## Test Steps

### TC-AUTH-ACT-02: Full-page loading saat token sedang divalidasi dan form belum dirender

1. Tahan respons validasi link aktivasi selama 5 detik (delay network)
2. Buka link aktivasi user `Siti Lestari`
3. Amati halaman selama 5 detik
4. Verifikasi Full-page loading tampil; field Password, field Confirm Password, dan button "Set Password" belum dirender (tidak ada form kosong tanpa indikator)
5. Lepaskan respons validasi
6. Verifikasi Loading hilang dan halaman `Auth > Account Activation > Set Password` tampil dengan Subtitle "Set a password to log in for sitilestari+{runId}-018@qwertysystem.net."
7. Verifikasi Token aktivasi user `Siti Lestari` tetap Active

### TC-AUTH-ACT-03: Validate Link gagal karena server error 5xx menampilkan error state, bukan halaman 404

8. Atur respons validasi link aktivasi menjadi server error 500
9. Buka link aktivasi user `Andi Saputra`
10. Amati halaman
11. Verifikasi Error state tampil: "Unable to load this data." dengan button [Try Again]
12. Verifikasi Halaman Invalid Link tidak tampil dan form Set Password tidak dirender
13. Verifikasi Token aktivasi user `Andi Saputra` tetap Active

### TC-AUTH-ACT-04: Validate Link timeout atau tanpa respons jaringan menampilkan error state, bukan halaman 404

14. Putuskan koneksi atau blokir respons validasi link aktivasi sampai timeout
15. Buka link aktivasi user `Dewi Maharani`
16. Tunggu sampai timeout terjadi dan amati halaman
17. Verifikasi Error state tampil: "Unable to load this data." dengan button [Try Again]
18. Verifikasi Halaman Invalid Link tidak tampil dan form Set Password tidak dirender
19. Verifikasi Token aktivasi user `Dewi Maharani` tetap Active

### TC-AUTH-ACT-05: Klik [Try Again] setelah server pulih memuat ulang validasi dan menampilkan form Set Password

20. Atur respons validasi menjadi 500, lalu buka link aktivasi user `Rizky Hartono` → error state "Unable to load this data." dengan [Try Again] tampil
21. Pulihkan respons validasi menjadi normal
22. Klik [Try Again]
23. Verifikasi Loading tampil sesaat, lalu halaman `Auth > Account Activation > Set Password` tampil dengan Subtitle "Set a password to log in for rizkyhartono+{runId}-018@qwertysystem.net."
24. Verifikasi Error state "Unable to load this data." tidak tampil lagi
25. Verifikasi Token aktivasi user `Rizky Hartono` tetap Active

### TC-AUTH-ACT-06: Klik [Try Again] saat server masih error tetap menampilkan error state

26. Atur respons validasi menjadi 500, lalu buka link aktivasi user `Nur Octaviani` → error state tampil
27. Biarkan respons tetap 500, klik [Try Again]
28. Verifikasi Error state "Unable to load this data." dengan button [Try Again] tetap tampil
29. Verifikasi Tidak ada redirect ke halaman Invalid Link dan form tidak dirender
30. Verifikasi Token aktivasi user `Nur Octaviani` tetap Active

## Notes

- Mode: FE+BE (intercept parsial). Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Kelas harness b (fault injection), endpoint Validate Link (`GET`). Resilience submit Set Password (`POST`) ada di spec E2E-028; keduanya dipisah supaya kegagalan keras pada satu endpoint tidak menutupi hasil endpoint lain.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
