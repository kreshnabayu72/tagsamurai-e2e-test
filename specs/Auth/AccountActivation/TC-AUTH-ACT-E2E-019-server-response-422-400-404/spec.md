---
id: TC-AUTH-ACT-E2E-019-server-response-422-400-404
title: "Tampilan Set Password untuk Respons Server 422 dan 400"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-117
  - TC-AUTH-ACT-118
coverage:
  web: automated
---

# Tampilan Set Password untuk Respons Server 422 dan 400

## Prerequisites

- Akun aktor seeding: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`.
- Mode: FE+BE dengan intercept parsial (backend nyata; asersi state token/user dicek ke backend). Respons dipaksa lewat `Spectra.intercept()` pada endpoint `POST /v2/iam/auth/activation/{token}/set-password`:
  - TC-AUTH-ACT-117: status 422, body `{"message": "Password does not meet the required policy", "data": {"field": "password", "failedRules": ["One special character"]}}` (skema contoh `policy_violation` di `auth/account-activation/API/openapi.yaml`; `failedRules` sengaja hanya memuat aturan yang dilanggar input TC-117, bukan ketiga aturan pada contoh).
  - Nilai `Spectra.env.ACT_PASSWORD` lolos validasi client, sehingga satu-satunya sumber error adalah respons yang di-intercept.
  - TC-AUTH-ACT-118: status 400, body `{"message": "Invalid request body", "error": [{"field": "body", "message": "Malformed JSON syntax at offset 20"}]}` (skema `ValidationErrorResponse`, contoh `malformedJson` di `openapi.yaml`); `field` bernilai `body`, bukan field form, sehingga tidak ada field form yang bisa ditandai.
- Endpoint `GET /v2/iam/auth/activation/{token}` tidak di-intercept (Validate Link memakai backend nyata).
- Hook `before`: buat lewat API dua user Pending Activation dengan token Active (email bersuffix per run) dan ambil link aktivasinya lewat API seeding. Hook `after`: hapus kedua user.
- Password diambil dari environment variable `ACT_PASSWORD` (`Spectra.env.ACT_PASSWORD`); tidak ditulis di spec atau fixture.
- Tanpa login (halaman publik, tidak ada sesi aktif di browser).
- TC-AUTH-ACT-117: User `Teguh Pratama` (`teguhpratama+{runId}-019@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active.
- TC-AUTH-ACT-118: User `Laras Nugroho` (`larasnugroho+{runId}-019@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active.

## Test Steps

### TC-AUTH-ACT-117: Tampilan halaman Set Password saat server menjawab 422 untuk request yang lolos validasi client

1. Buka link aktivasi user `Teguh Pratama` di browser → halaman `Auth > Account Activation > Set Password` tampil
2. Atur respons submit menjadi 422 sesuai body intercept TC-AUTH-ACT-117 di Prerequisites
3. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
4. Klik button "Set Password"
5. Verifikasi Inline error muncul di bawah field Password dengan teks "Password does not meet the required policy" (pesan dari respons server)
6. Verifikasi Halaman tetap `Auth > Account Activation > Set Password`; nilai field Password dan Confirm Password dipertahankan; tidak ada toast
7. Verifikasi Token aktivasi user `Teguh Pratama` tetap Active dan status user tetap Pending Activation

### TC-AUTH-ACT-118: Tampilan halaman Set Password saat server menjawab 400 tanpa field

8. Buka link aktivasi user `Laras Nugroho` di browser → halaman `Auth > Account Activation > Set Password` tampil
9. Atur respons submit menjadi 400 sesuai body intercept TC-AUTH-ACT-118 di Prerequisites
10. Ketik `Spectra.env.ACT_PASSWORD` di field Password dan Confirm Password
11. Klik button "Set Password"
12. Verifikasi Dialog tampil memuat teks "Invalid request. Please check your input."
13. Verifikasi Halaman tetap `Auth > Account Activation > Set Password` di belakang dialog dengan nilai field dipertahankan; tidak ada toast
14. Verifikasi Token aktivasi user `Laras Nugroho` tetap Active dan status user tetap Pending Activation

## Notes

- Mode: FE+BE (intercept parsial). Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Kelas harness b (pemetaan respons server). TC-AUTH-ACT-131 dan 132 (request langsung ke server) dipindah ke E2E-020 karena termasuk kelas a.
- Slug folder `server-response-422-400-404` dipertahankan supaya id spec tidak berubah.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
