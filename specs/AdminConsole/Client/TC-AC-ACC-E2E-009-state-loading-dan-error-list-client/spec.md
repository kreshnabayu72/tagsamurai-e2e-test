---
id: TC-AC-ACC-E2E-009-state-loading-dan-error-list-client
title: "State Loading dan Error pada List Client"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-25
  - TC-AC-ACC-26
coverage:
  web: automated
---

# State Loading dan Error pada List Client

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| A-01 | Total Control (Principal) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, A-01); halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, A-01, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah login dan logout eksplisit.
- Password akun tidak ditulis di spec atau fixture. Env var selain `AC_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; tim FE mendaftarkannya saat tahap script. Akun Tabel A1/A3 disediakan lewat fixture seed (nama akun mengikuti kolom namaRoleCapability dan namaCompany).
- Data: Pre-setup C-01…C-14 (Tabel A2), aktor Tabel A1, dan fixture Tabel A3 yang disebut TC tersedia lewat skrip seed (Fixture BE); fixture A3 yang dipakai spec ini hanya dibaca kecuali disebut lain di bawah.
- Kemampuan teknis: `Spectra.intercept()` pada respons endpoint list Client (rujukan endpoint dilengkapi tim FE dari LLD modul saat tahap script; TC hanya menyebut "response list") untuk menahan respons (TC-AC-ACC-25) dan memaksa respons 5xx lalu memulihkannya (TC-AC-ACC-26). Intercept dilepas pada langkah spec dan dipulihkan hook `after` bila spec gagal di tengah.
- Backend nyata dipakai untuk respons yang tidak diintercept (Mode FE+BE dengan intercept parsial, bagian 6 konvensi).
- Suite berjalan serial (`parallel: false`): jam server, Selection Limit, flag Guided Tooltip, dan data bersama Tabel A tidak diubah oleh spec lain secara bersamaan.
- Flag Guided Tooltip `guided_tooltip_seen_ac-client` dan `guided_tooltip_seen_ac-client-detail` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).

## Test Steps

### TC-AC-ACC-25: Loading state saat data List diambil

1. Tahan respons list Client lewat `Spectra.intercept()` (simulasi throttle jaringan)
2. Klik item `Client` pada sidebar
3. Verifikasi Loading component tampil selama data diambil
4. Lepas tahanan respons list Client
5. Verifikasi tabel menampilkan baris setelah data diterima

### TC-AC-ACC-26: Error state gagal memuat List dan pulih dengan Try Again

6. Paksa respons list Client menjadi 5xx lewat `Spectra.intercept()`
7. Klik item `Client` pada sidebar
8. Verifikasi teks `Unable to load this data.` tampil
9. Verifikasi tombol `[Try Again]` tampil
10. Pulihkan respons list Client (lepas intercept)
11. Klik `[Try Again]`
12. Verifikasi data List tampil normal dengan sedikitnya satu baris
13. Verifikasi state error `Unable to load this data.` hilang

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 10. Tanpa awalan `Verifikasi`; menyiapkan, menutup, atau membersihkan state untuk blok berikutnya, atau mencari baris target lewat Search (R-16).
- Pengecualian S-12 (diizinkan pemilik, Q5): nama Client Pre-setup dan fixture A3 residen ditulis literal tanpa suffix karena dirujuk TC sebagai Population yang dibaca (urutan, jumlah, badge, isi sel); spec ini tidak membuat atau mengubah Client bernama literal kecuali disebut di bawah.
- P-5 (butir b): TC-AC-ACC-26 adalah satu-satunya objek uji ringan kelas b (fault injection) di spec ini; TC-AC-ACC-25 menahan respons hanya untuk mengamati state Loading (bukan kelas b).
- Temuan untuk QA:
  - TC-AC-ACC-25 dan 26: kolom Data Uji menyebut "Network throttling" dan "Mock response 500 lalu 200" tanpa menyebut endpoint; spec tidak mengarang endpoint dan menyerahkannya ke tim FE (S-13).
