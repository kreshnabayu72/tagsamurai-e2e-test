---
id: TC-AUTH-ACT-E2E-007-password-policy-dan-checklist-real-time
title: Password Policy, real-time checklist, boundary min/max, dan karakter khusus
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-20
  - TC-AUTH-ACT-21
  - TC-AUTH-ACT-22
  - TC-AUTH-ACT-23
  - TC-AUTH-ACT-24
  - TC-AUTH-ACT-25
  - TC-AUTH-ACT-26
  - TC-AUTH-ACT-27
  - TC-AUTH-ACT-28
  - TC-AUTH-ACT-29
  - TC-AUTH-ACT-30
  - TC-AUTH-ACT-31
coverage:
  web: automated
---

# Password Policy, real-time checklist, boundary min/max, dan karakter khusus

## Prerequisites

- Token valid `active` dan belum expired tersedia (disiapkan oleh hook `before`).
- Halaman Set Password `/activate?token={validToken}` terbuka.
- Hook `beforeEach` memastikan form dalam state bersih untuk tiap skenario jika diperlukan.
- Untuk submit sukses (boundary min 8 char, boundary max 72 char, special char valid), hook menyiapkan user dengan token valid dan membersihkan state pasca-submit.
- Validasi policy berdasarkan Password Policy Auth Foundation (min 8, max 72, uppercase, lowercase, number, special char, no spaces).

## Test Steps

### A. Boundary length

1. Isi Password dan Confirm Password dengan `Abcd1!23` (tepat 8 karakter). Selesaikan pengisian lalu klik `[Set Password]`.
2. Verifikasi seluruh checklist 6 baris berwarna hitam (semua rule terpenuhi).
3. Verifikasi submit diterima dan halaman berpindah ke Activation Success.
4. Siapkan ulang halaman Set Password dengan token valid baru.
5. Isi Password dengan `Abc1!2a` (7 karakter) dan amati checklist.
6. Verifikasi baris `"Minimum 8 characters"` tetap berwarna abu-abu (belum terpenuhi).
7. Klik `[Set Password]`.
8. Verifikasi submit ditolak dan tetap berada di halaman Set Password. Token tetap `active`, tidak ter-consume.
9. Siapkan ulang halaman Set Password dengan token valid baru.
10. Isi Password 72 karakter valid (kombinasi upper/lower/number/special) dan Confirm Password sama, lalu klik `[Set Password]`.
11. Verifikasi seluruh checklist berwarna hitam dan submit diterima → Activation Success.
12. Siapkan ulang halaman Set Password dengan token valid baru.
13. Isi Password 73 karakter dan amati.
14. Verifikasi muncul error real-time terpisah `"Maximum 72 characters"` (bukan bagian dari checklist 6-baris).
15. Klik `[Set Password]`.
16. Verifikasi HTTP `422` terjadi (berdasarkan response), `data.failedRules` berisi `"Maximum 72 characters"`, dan submit tetap ditolak. Token tetap `active`.

### B. Masing-masing rule gagal

17. Isi Password `abcd123!` (tanpa huruf besar). Amati checklist real-time.
18. Verifikasi baris `"One uppercase (A-Z)"` berwarna abu-abu; baris lain yang terpenuhi berwarna hitam sesuai state.
19. Ganti Password menjadi `ABCD123!` (tanpa huruf kecil).
20. Verifikasi baris `"One lowercase (a-z)"` berwarna abu-abu.
21. Ganti Password menjadi `Abcdefg!` (tanpa angka).
22. Verifikasi baris `"One number (0-9)"` berwarna abu-abu.
23. Ganti Password menjadi `Abcd1234` (tanpa special character).
24. Verifikasi baris `"One special character"` berwarna abu-abu.

### C. Spasi tidak diperbolehkan

25. Isi Password dengan `Abcd 123!` (mengandung spasi) dan amati checklist.
26. Verifikasi baris `"Password cannot contain spaces"` berwarna abu-abu (muncul sebagai rule failure).
27. Klik `[Set Password]` dengan Confirm Password sama.
28. Verifikasi submit ditolak. Spasi **tidak** di-trim otomatis. Token tetap `active`, tidak ter-consume.

### D. Karakter khusus valid & real-time update

29. Isi Password dengan `Abcd12!@` (mengandung `!@` sebagai special char valid) dan Confirm Password sama.
30. Verifikasi checklist menunjukkan rule special character terpenuhi (hitam) sesuai konfigurasi policy.
31. Klik `[Set Password]`.
32. Verifikasi submit diterima → Activation Success.
33. Buka kembali halaman Set Password dengan token valid baru.
34. Ketik password valid secara bertahap (karakter demi karakter), amati checklist per keystroke.
35. Verifikasi setiap baris berubah dari abu-abu menjadi hitam saat rule yang bersangkutan terpenuhi (update real-time, tanpa perlu submit/blur).
36. Verifikasi checklist tetap update instan selama pengetikan.

## Notes

- Beberapa skenario submit sukses (langkah 1-3, 10-11, 29-32) memerlukan token valid baru untuk skenario berikutnya; hook `beforeEach` atau setup ulang token perlu diperhatikan untuk menjaga isolasi.
- Untuk TC-AUTH-ACT-23 (73 char), verifikasi mencakup HTTP `422`, `data.failedRules` berisi `"Maximum 72 characters"`, dan error real-time terpisah - ini perlu dicek via network response.
- Rule "Password cannot contain spaces" bersifat eksplisit dan diuji terpisah (TC-AUTH-ACT-28).
- Real-time checklist update per keystroke (TC-AUTH-ACT-30, TC-AUTH-ACT-31) adalah UI-only behavior; tetap digabung dalam spec ini karena topik yang sama.
