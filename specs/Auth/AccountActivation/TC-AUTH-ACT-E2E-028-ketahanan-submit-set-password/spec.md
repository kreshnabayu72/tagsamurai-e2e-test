---
id: TC-AUTH-ACT-E2E-028-ketahanan-submit-set-password
title: "Ketahanan Submit Set Password terhadap Error Server dan Timeout"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-64
  - TC-AUTH-ACT-66
  - TC-AUTH-ACT-67
  - TC-AUTH-ACT-68
  - TC-AUTH-ACT-69
coverage:
  web: automated
---

# Ketahanan Submit Set Password terhadap Error Server dan Timeout

## Prerequisites

- Mode: FE+BE dengan intercept parsial (backend nyata; asersi state token/user dicek ke backend). Respons dipaksa lewat `Spectra.intercept()` per TC:
  - TC-AUTH-ACT-66: `POST /v2/iam/auth/activation/{token}/set-password` dipaksa HTTP 500
  - TC-AUTH-ACT-67: `POST /v2/iam/auth/activation/{token}/set-password` dipaksa HTTP 500
  - TC-AUTH-ACT-68: `POST /v2/iam/auth/activation/{token}/set-password` dipaksa HTTP 500, lalu intercept dilepas (respons normal)
  - TC-AUTH-ACT-69: `POST /v2/iam/auth/activation/{token}/set-password` tidak pernah dijawab sampai timeout klien
  - TC-AUTH-ACT-64: `POST /v2/iam/auth/activation/{token}/set-password` ditahan 5 detik, lalu diteruskan normal
- Akun aktor (hanya TC-AUTH-ACT-67): Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`.
- Password user uji dari `Spectra.env.ACT_PASSWORD`. Tidak ada password atau token di spec atau fixture.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-028` beserta link aktivasinya, semuanya Pending Activation dengan token Active: `Mega Wijaya` (TC-66), `Arif Handayani` (TC-67), `Nina Santoso` (TC-68), `Galih Kurniawan` (TC-69), `Tika Hartono` (TC-64), masing-masing dengan email nama huruf kecil tanpa spasi + `+{runId}-028@qwertysystem.net` (contoh `megawijaya+{runId}-028@qwertysystem.net`). Hook `after` melepas semua intercept dan menghapus user tersebut (tetap jalan walau spec gagal di tengah).
- Kemampuan teknis: intercept network di browser (delay, HTTP 500, tanpa respons sampai timeout), membuka tab baru, dua konteks browser (jendela privat publik dan browser admin untuk TC-67).

## Test Steps

### TC-AUTH-ACT-66: Server error 5xx saat Set Password menampilkan toast gagal dan mempertahankan input

1. Buka link aktivasi user `Mega Wijaya` di browser → halaman `Auth > Account Activation > Set Password` tampil
2. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
3. Atur respons submit menjadi server error 500
4. Klik button "Set Password"
5. Verifikasi Toast error: "Error, failed to set password."
6. Verifikasi Halaman tetap `Auth > Account Activation > Set Password`; field Password dan Confirm Password tetap berisi nilai `Spectra.env.ACT_PASSWORD`
7. Verifikasi Button "Set Password" kembali enabled (tidak Loading) dan `Auth > Account Activation > Activation Success` tidak tampil
8. Verifikasi Token aktivasi user `Mega Wijaya` tetap Active dan status user tetap Pending Activation

### TC-AUTH-ACT-67: Token tetap valid dan user tetap Pending Activation setelah submit gagal 5xx

9. Buka link aktivasi user `Arif Handayani` di browser → halaman `Auth > Account Activation > Set Password` tampil
10. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
11. Atur respons submit menjadi server error 500
12. Klik button "Set Password"
13. Buka kembali link aktivasi yang sama di tab baru
14. Verifikasi `Auth > Account Activation > Set Password` tampil kembali (token masih valid)
15. Ganti konteks ke browser admin: login sebagai akun aktor Total Control (Global Settings)
16. Buka `Global Settings > User > Login User` dan cari user `Arif Handayani`
17. Verifikasi User `Arif Handayani` tetap berbadge Pending Activation pada tabel
18. Verifikasi Token aktivasi user `Arif Handayani` tetap Active dan status user tetap Pending Activation (transaksi di-rollback)

### TC-AUTH-ACT-68: Retry Set Password setelah server pulih dari error 5xx berhasil

19. Buka link aktivasi user `Nina Santoso` di browser → halaman `Auth > Account Activation > Set Password` tampil
20. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
21. Atur respons submit menjadi server error 500, lalu klik button "Set Password"
22. Verifikasi Toast error: "Error, failed to set password." dan input tetap terisi
23. Pulihkan respons submit menjadi normal
24. Klik button "Set Password"
25. Verifikasi `Auth > Account Activation > Activation Success` tampil tanpa perlu mengisi ulang field
26. Verifikasi Token aktivasi user `Nina Santoso` Consumed dan status user Activated

### TC-AUTH-ACT-69: Timeout saat Set Password menampilkan toast gagal dan mempertahankan input

27. Buka link aktivasi user `Galih Kurniawan` di browser → halaman `Auth > Account Activation > Set Password` tampil
28. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
29. Putuskan koneksi atau blokir respons submit sampai timeout
30. Klik button "Set Password"
31. Tunggu sampai timeout terjadi
32. Verifikasi Toast error: "Error, failed to set password."
33. Verifikasi Halaman tetap `Auth > Account Activation > Set Password` dengan field Password dan Confirm Password tetap berisi nilai `Spectra.env.ACT_PASSWORD` dan button "Set Password" enabled kembali
34. Verifikasi Token aktivasi user `Galih Kurniawan` tetap Active

### TC-AUTH-ACT-64: Button Set Password berstatus Loading dan disabled selama request berjalan

35. Buka link aktivasi user `Tika Hartono` → halaman `Auth > Account Activation > Set Password` tampil
36. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
37. Tahan respons submit selama 5 detik (delay network)
38. Klik button "Set Password"
39. Amati button selama 5 detik
40. Verifikasi button "Set Password" berstatus Loading dan disabled (tidak dapat diklik kembali)
41. Lepaskan respons submit
42. Verifikasi `Auth > Account Activation > Activation Success` tampil
43. Verifikasi Token aktivasi user `Tika Hartono` Consumed dan status user Activated

## Notes

- Mode: FE+BE (intercept parsial). Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Kelas harness b (fault injection), endpoint submit Set Password (`POST`). Dipisah dari E2E-018 (Validate Link). TC-AUTH-ACT-64 berasal dari E2E-009 karena butuh intercept.
- Browser admin di TC-AUTH-ACT-67 hanya dipakai untuk mengecek data (badge user), bukan untuk menguji race, sehingga TC tetap di kelas harness b.
- Spec ini 43 langkah, di atas smell sekitar 35 langkah (prinsip 13). Dipertahankan karena kelima blok memakai harness yang sama (intercept pada `POST .../set-password`), dan tiap blok memakai user sendiri sehingga blok berikutnya tidak bergantung pada hasil blok sebelumnya. Blok TC-AUTH-ACT-67 memakai browser admin hanya untuk membaca data; bila di lapangan terbukti menggagalkan blok lain, blok itu yang dipindah ke spec sendiri.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
