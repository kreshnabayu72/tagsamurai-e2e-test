---
id: TC-AUTH-ACT-E2E-006-password-policy-checklist-real-time
title: "Password Policy dan checklist real-time pada field Password"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-ACT-22
  - TC-AUTH-ACT-23
  - TC-AUTH-ACT-24
  - TC-AUTH-ACT-25
  - TC-AUTH-ACT-26
  - TC-AUTH-ACT-27
  - TC-AUTH-ACT-28
  - TC-AUTH-ACT-29
coverage:
  web: automated
---

# Password Policy dan checklist real-time pada field Password

## Prerequisites

- Browser publik tanpa sesi login.
- User seeding milik automation berstatus Pending Activation dengan token Active, dibuat lewat API di hook `before` (email unik per run).
- Akses API read-only untuk memastikan token tetap Active (spec ini tidak pernah men-submit form).
- Password Policy pada halaman Set Password terdiri dari 6 baris: "Minimum 8 characters", "One uppercase (A-Z)", "One lowercase (a-z)", "One number (0-9)", "One special character", "Password cannot contain spaces".

## Test Steps

### Checklist baris "Minimum 8 characters" (TC-AUTH-ACT-22)

1. Buka link aktivasi user seeding → halaman Set Password tampil.
2. Ketik `Abcde1!` pada field Password.
3. Verifikasi baris "Minimum 8 characters" abu-abu (disabled) dengan ikon ○, sedangkan baris lain hitam (primary) dengan ikon ✓.
4. Sisipkan karakter `f` setelah `e` sehingga menjadi `Abcdefg1!` (8 karakter).
5. Verifikasi baris "Minimum 8 characters" berubah hitam (primary) dengan ikon ✓ tanpa menekan button "Set Password".
6. Hapus karakter `f` sehingga kembali `Abcde1!`.
7. Verifikasi baris "Minimum 8 characters" kembali abu-abu (disabled) dengan ikon ○ dan kelima baris lain tetap hitam.

### Checklist baris "One uppercase (A-Z)" (TC-AUTH-ACT-23)

8. Kosongkan field Password, lalu ketik `abcdefg1!`.
9. Verifikasi baris "One uppercase (A-Z)" abu-abu (disabled) + ○ dan lima baris lain hitam + ✓.
10. Ganti karakter pertama menjadi `A` sehingga `Abcdefg1!`.
11. Verifikasi seluruh baris hitam + ✓ secara real-time.
12. Ganti karakter pertama kembali menjadi `a`.
13. Verifikasi baris "One uppercase (A-Z)" kembali abu-abu + ○.

### Checklist baris "One lowercase (a-z)" (TC-AUTH-ACT-24)

14. Kosongkan field Password, lalu ketik `ABCDEFG1!`.
15. Verifikasi baris "One lowercase (a-z)" abu-abu + ○ dan lima baris lain hitam + ✓.
16. Tambahkan karakter `a` di akhir sehingga `ABCDEFG1!a`.
17. Verifikasi seluruh baris hitam + ✓.
18. Hapus karakter `a`.
19. Verifikasi baris "One lowercase (a-z)" kembali abu-abu + ○.

### Checklist baris "One number (0-9)" (TC-AUTH-ACT-25)

20. Kosongkan field Password, lalu ketik `Abcdefgh!`.
21. Verifikasi baris "One number (0-9)" abu-abu + ○ dan lima baris lain hitam + ✓.
22. Tambahkan karakter `1` di akhir sehingga `Abcdefgh!1`.
23. Verifikasi seluruh baris hitam + ✓.
24. Hapus karakter `1`.
25. Verifikasi baris "One number (0-9)" kembali abu-abu + ○.

### Checklist baris "One special character" (TC-AUTH-ACT-26)

26. Kosongkan field Password, lalu ketik `Abcdefg1`.
27. Verifikasi baris "One special character" abu-abu + ○ dan lima baris lain hitam + ✓.
28. Tambahkan karakter `!` di akhir sehingga `Abcdefg1!`.
29. Verifikasi seluruh baris hitam + ✓.
30. Hapus karakter `!`.
31. Verifikasi baris "One special character" kembali abu-abu + ○.

### Checklist baris "Password cannot contain spaces" (TC-AUTH-ACT-27)

32. Kosongkan field Password, lalu ketik `Abcdefg1!`.
33. Verifikasi seluruh baris hitam + ✓.
34. Sisipkan spasi di tengah sehingga `Abcd efg1!`.
35. Verifikasi baris "Password cannot contain spaces" abu-abu + ○ dan kelima baris lain tetap hitam + ✓.
36. Hapus spasi sehingga kembali `Abcdefg1!`.
37. Verifikasi baris "Password cannot contain spaces" kembali hitam + ✓.

### Semua baris hitam saat seluruh aturan terpenuhi (TC-AUTH-ACT-28)

38. Kosongkan field Password, lalu ketik `Aman#Sandi8`.
39. Verifikasi keenam baris checklist hitam (primary) dengan ikon ✓ dan tidak ada baris abu-abu.

### State checklist saat field dikosongkan kembali (TC-AUTH-ACT-29)

40. Kosongkan field Password, lalu ketik `a`.
41. Verifikasi baris "Password cannot contain spaces" dan "One lowercase (a-z)" hitam + ✓, sedangkan "Minimum 8 characters", "One uppercase (A-Z)", "One number (0-9)", dan "One special character" tetap abu-abu + ○.
42. Hapus karakter `a` sehingga field Password kosong.
43. Verifikasi keenam baris checklist kembali abu-abu (disabled) + ○ seperti state awal, termasuk baris "Password cannot contain spaces".

## Notes

- Seluruh blok hanya mengetik pada field tanpa submit, sehingga satu user seeding cukup dan token dijamin tetap Active.
- Urutan baris checklist disesuaikan dengan urutan di halaman sehingga satu sesi dapat berjalan lurus tanpa membuka ulang.
- Id TC disebut pada subjudul blok agar report per langkah dapat dipetakan ke TC granular.
