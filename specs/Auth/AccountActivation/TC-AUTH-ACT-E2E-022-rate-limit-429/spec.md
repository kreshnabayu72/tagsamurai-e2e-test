---
id: TC-AUTH-ACT-E2E-022-rate-limit-429
title: "Penolakan IP Rate Limit 429 pada Validate Link dan Set Password"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-133
  - TC-AUTH-ACT-134
  - TC-AUTH-ACT-136
coverage:
  web: automated
---

# Penolakan IP Rate Limit 429 pada Validate Link dan Set Password

## Prerequisites

- Mode: FE+BE (flood nyata ke server; bukan mock, sesuai bagian 6 konvensi).
- Kemampuan teknis: klien HTTP yang mengirim request beruntun dari IP yang sama dengan browser uji ke dua endpoint dengan counter terpisah (`auth-foundation.md` §3.2): `GET /v2/iam/auth/activation/{token}` (Validate Link, TC-133) dan `POST /v2/iam/auth/activation/{token}/set-password` (Set Password, TC-134); akses untuk mereset counter IP rate limit environment.
- Ambang: 20 request per endpoint dari IP yang sama dalam 1 menit; request ke-21 ke endpoint yang sama ditolak 429. Counter dipisah per endpoint, jadi request ke endpoint Validate Link tidak ikut dihitung di counter Set Password (sesuai TC sumber dan `auth-foundation.md` §3.2).
- Request flood TC-134 dikirim ke `POST .../set-password` dengan body yang ditolak validasi kebijakan password (respons 422), supaya token tidak ter-consume dan tetap Active untuk verifikasi akhir.
- Hook `before`: reset counter IP rate limit environment terlebih dahulu supaya request dari spec sebelumnya tidak ikut terhitung, lalu (lewat API, email bersuffix per run) buat user Pending Activation dengan token Active dan ambil link aktivasinya:
  - TC-AUTH-ACT-133: `Andi Santoso` (`andisantoso+{runId}-022@qwertysystem.net`).
  - TC-AUTH-ACT-134: `Dewi Kurniawan` (`dewikurniawan+{runId}-022@qwertysystem.net`).
  - TC-AUTH-ACT-136: `Tiara Anggraini` (`tiaraanggraini+{runId}-022@qwertysystem.net`).
- Hook `after`: reset counter IP rate limit dan hapus ketiga user. Hook ini tetap jalan walau spec gagal di tengah.
- Password diambil dari environment variable `ACT_PASSWORD` (`Spectra.env.ACT_PASSWORD`).
- Tanpa login (halaman publik, tidak ada sesi aktif di browser).

## Test Steps

### TC-AUTH-ACT-133: Validate Link ditolak 429 oleh IP rate limit menampilkan error state, bukan halaman 404

1. Kirim 20 request `GET /v2/iam/auth/activation/{token}` (endpoint Validate Link) dengan token user `Andi Santoso` dari IP yang sama dalam 1 menit
2. Buka link aktivasi user `Andi Santoso` di browser (request ke-21 dalam 1 menit dari IP yang sama)
3. Verifikasi Halaman menampilkan error state `Unable to load this data.` dengan button `[Try Again]` (state S-02), bukan halaman 404
4. Verifikasi Token tetap Active dan tidak ada entri pencatatan baru

### TC-AUTH-ACT-134: Set Password ditolak 429 oleh IP rate limit menampilkan toast gagal dan form tetap terbuka

5. Reset counter IP rate limit, lalu buka link aktivasi user `Dewi Kurniawan` → halaman `Auth > Account Activation > Set Password` tampil
6. Kirim 20 request `POST /v2/iam/auth/activation/{token}/set-password` (endpoint Set Password) dengan token user `Dewi Kurniawan` dan body password yang ditolak validasi (422) dari IP yang sama dalam 1 menit; request Validate Link pada langkah 5 tidak dihitung karena counter dipisah per endpoint
7. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
8. Klik button `Set Password` (request ke-21 dalam 1 menit dari IP yang sama)
9. Verifikasi Toast error "Error, failed to set password." tampil (state S-12), form tetap terbuka dan nilai field dipertahankan
10. Verifikasi Token aktivasi user `Dewi Kurniawan` tetap Active dan status user tetap Pending Activation
11. Verifikasi Tidak ada entri pencatatan baru

### TC-AUTH-ACT-136: Request ke-20 ke Validate Link masih diproses dan counter Set Password terpisah

12. Reset counter IP rate limit, lalu kirim 19 request `GET /v2/iam/auth/activation/{token}` (endpoint Validate Link) dengan token user `Tiara Anggraini` dari IP yang sama dalam 1 menit (fixture BE; dikirim tepat sebelum langkah berikutnya supaya masih dalam jendela 1 menit)
13. Buka link aktivasi user `Tiara Anggraini` di browser (request ke-20 ke endpoint Validate Link dalam 1 menit dari IP yang sama)
14. Verifikasi `Auth > Account Activation > Set Password` tampil dengan Subtitle "Set a password to log in for tiaraanggraini+{runId}-022@qwertysystem.net." (bukan error state S-02)
15. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
16. Klik button `Set Password` (request pertama ke endpoint Set Password; counter dipisah per endpoint)
17. Verifikasi `Auth > Account Activation > Activation Success` tampil dan tidak ada toast error (penolakan baru dimulai pada request ke-21; request Validate Link tidak menambah counter Set Password)
18. Verifikasi User `Tiara Anggraini` Activated dan token Consumed

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Kelas harness c (flood rate limit). Suite berjalan `parallel: false`, jadi flood tidak mengganggu spec lain; counter tetap direset di `after`.
- Langkah 1, 5, dan 6 menuliskan secara eksplisit prasyarat "20 request sudah dikirim" dan "halaman Set Password sudah terbuka" dari TC sumber.
- TC-AUTH-ACT-136 adalah batas atas yang masih diterima (request ke-20), berpasangan dengan TC-AUTH-ACT-133 yang menguji penolakan di request ke-21; keduanya kelas c yang sama dan memakai harness flood yang sama, sehingga digabung di spec ini.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
