---
id: TC-AUTH-ACT-E2E-022-rate-limit-429
title: "Penolakan IP Rate Limit 429 pada Validate Link dan Set Password"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-133
  - TC-AUTH-ACT-134
coverage:
  web: automated
---

# Penolakan IP Rate Limit 429 pada Validate Link dan Set Password

## Prerequisites

- Mode: FE+BE (flood nyata ke server; bukan mock, sesuai bagian 6 konvensi).
- Kemampuan teknis: klien HTTP yang mengirim request beruntun dari IP yang sama dengan browser uji ke `GET /v2/iam/auth/activation/{token}`; akses untuk mereset counter IP rate limit environment.
- Ambang: 20 request ke endpoint aktivasi dari IP yang sama dalam 1 menit; request ke-21 ditolak 429 (sesuai TC sumber dan `auth-foundation.md` §3.2).
- Hook `before`: reset counter IP rate limit environment terlebih dahulu supaya request dari spec sebelumnya tidak ikut terhitung, lalu (lewat API, email bersuffix per run) buat user Pending Activation dengan token Active dan ambil link aktivasinya:
  - TC-AUTH-ACT-133: `Andi Santoso` (`andisantoso+{runId}-022@qwertysystem.net`).
  - TC-AUTH-ACT-134: `Dewi Kurniawan` (`dewikurniawan+{runId}-022@qwertysystem.net`).
- Hook `after`: reset counter IP rate limit dan hapus kedua user. Hook ini tetap jalan walau spec gagal di tengah.
- Password diambil dari environment variable `ACT_PASSWORD` (`Spectra.env.ACT_PASSWORD`).
- Tanpa login (halaman publik, tidak ada sesi aktif di browser).

## Test Steps

### TC-AUTH-ACT-133: Validate Link ditolak 429 oleh IP rate limit menampilkan error state, bukan halaman 404

1. Kirim 20 request `GET /v2/iam/auth/activation/{token}` dengan token user `Andi Santoso` dari IP yang sama dalam 1 menit
2. Buka link aktivasi user `Andi Santoso` di browser (request ke-21 dalam 1 menit dari IP yang sama)
3. Verifikasi Halaman menampilkan error state `Unable to load this data.` dengan button `[Try Again]` (state S-02), bukan halaman 404
4. Verifikasi Token tetap Active dan tidak ada entri pencatatan baru

### TC-AUTH-ACT-134: Set Password ditolak 429 oleh IP rate limit menampilkan toast gagal dan form tetap terbuka

5. Reset counter IP rate limit, lalu buka link aktivasi user `Dewi Kurniawan` → halaman `Auth > Account Activation > Set Password` tampil
6. Kirim request ke endpoint aktivasi dari IP yang sama sampai total 20 request dalam 1 menit (termasuk request Validate Link pada langkah 5)
7. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
8. Klik button `Set Password` (request ke-21 dalam 1 menit dari IP yang sama)
9. Verifikasi Toast gagal tampil (state S-12), form tetap terbuka dan nilai field dipertahankan
10. Verifikasi Token aktivasi user `Dewi Kurniawan` tetap Active dan status user tetap Pending Activation
11. Verifikasi Tidak ada entri pencatatan baru

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Kelas harness c (flood rate limit). Suite berjalan `parallel: false`, jadi flood tidak mengganggu spec lain; counter tetap direset di `after`.
- Langkah 1, 5, dan 6 menuliskan secara eksplisit prasyarat "20 request sudah dikirim" dan "halaman Set Password sudah terbuka" dari TC sumber.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
