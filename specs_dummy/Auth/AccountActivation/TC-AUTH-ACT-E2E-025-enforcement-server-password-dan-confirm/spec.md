---
id: TC-AUTH-ACT-E2E-025-enforcement-server-password-dan-confirm
title: "Enforcement server: request langsung dengan password/Confirm tidak valid ditolak 422"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-114
  - TC-AUTH-ACT-115
  - TC-AUTH-ACT-116
  - TC-AUTH-ACT-128
coverage:
  web: automated
---

# Enforcement server: request langsung dengan password/Confirm tidak valid ditolak 422

## Prerequisites

- Browser publik tanpa sesi login.
- Kemampuan mengambil token dari nilai parameter link aktivasi, lalu mengirim request Set Password langsung ke server (API client / fetch terprogram) melewati validasi client.
- 4 user seeding milik automation berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run): satu user untuk tiap blok TC-AUTH-ACT-114, 115, 116, dan 128; hook `after` membersihkan seluruh user.
- Akses API read-only untuk memverifikasi status respons (422) serta token tetap Active dan user tetap Pending Activation setelah tiap penolakan.

## Test Steps

### Password kurang dari 8 karakter ditolak server (TC-AUTH-ACT-114)

1. Ambil token dari link aktivasi user A.
2. Kirim request set password langsung ke server dengan token tersebut dan password `Abc1!` (kurang dari 8 karakter).
3. Verifikasi server menolak request dengan respons 422 dan error code kegagalan password policy.
4. Buka link aktivasi user A di browser.
5. Verifikasi halaman `Auth > Account Activation > Set Password` tampil kembali (token tetap valid) dan status user tetap Pending Activation.

### Password 73 karakter ditolak server (TC-AUTH-ACT-115)

6. Ambil token dari link aktivasi user B.
7. Kirim request set password langsung ke server dengan token tersebut dan password `Aa1!` diikuti 69 karakter `x` (total 73 karakter).
8. Verifikasi server menolak request dengan respons 422 dan error code kegagalan password policy.
9. Buka link aktivasi user B di browser.
10. Verifikasi halaman Set Password tampil kembali (token tetap valid) dan status user tetap Pending Activation.

### Password berisi spasi ditolak server tanpa di-trim (TC-AUTH-ACT-116)

11. Ambil token dari link aktivasi user C.
12. Kirim request set password langsung ke server dengan token tersebut dan password `Aman#Sandi8 ` (satu spasi di akhir).
13. Verifikasi server menolak request dengan respons 422 dan error code kegagalan password policy (password tidak di-trim lalu diterima).
14. Buka link aktivasi user C di browser.
15. Verifikasi halaman Set Password tampil kembali (token tetap valid) dan status user tetap Pending Activation.

### Confirm Password berbeda ditolak server (TC-AUTH-ACT-128)

16. Ambil token dari link aktivasi user D.
17. Kirim request set password langsung ke server dengan token tersebut, password `Aman#Sandi8`, dan confirmPassword `Aman#Sandi9`.
18. Verifikasi server menolak request dengan respons 422 dan pesan field Confirm Password "Passwords do not match".
19. Buka link aktivasi user D di browser.
20. Verifikasi halaman Set Password tampil kembali (token tetap valid) dan status user tetap Pending Activation.

## Notes

- Seluruh request dikirim melewati form sehingga hanya validasi server yang diuji; tidak ada token yang dikonsumsi sehingga urutan blok bebas.
- Screening dilakukan pada blok pertama; kebutuhan API client terprogram dicatat di Prerequisites.
