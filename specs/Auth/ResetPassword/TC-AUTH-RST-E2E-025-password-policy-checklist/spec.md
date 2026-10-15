---
id: TC-AUTH-RST-E2E-025-password-policy-checklist
title: "Checklist Password Policy Reaktif, Batas Karakter 8–72, dan Karakter Spesial"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-RST-67
  - TC-AUTH-RST-68
  - TC-AUTH-RST-69
  - TC-AUTH-RST-80
coverage:
  web: automated
---

# Checklist Password Policy Reaktif, Batas Karakter 8–72, dan Karakter Spesial

## Prerequisites

- Mode: FE+BE.
- Seeding: user subjek `Budi Santoso` (`budisantoso+{runId}-025@qwertysystem.net`) dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password `Spectra.env.RST_PASSWORD`; satu token reset aktif diterbitkan di hook `before` lewat API Request, tautan diambil dari mail-catcher. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`.
- Kemampuan teknis: mail-catcher; jendela privat tanpa sesi login; mengetik karakter non-ASCII dan emoji.
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat suite.md); mekanisme reset disediakan tim FE/BE.
- TC-AUTH-RST-67, TC-AUTH-RST-68, TC-AUTH-RST-69, TC-AUTH-RST-80: User belum login (guest); browser web; Setup New Password terbuka dari tautan reset (tanpa submit, token tidak dikonsumsi).
- TC-AUTH-RST-67 data: Password diketik bertahap `a`, `aB`, `aB1`, `aB1!`, `aB1!aaaa`.
- TC-AUTH-RST-68 data: Password `aB1! aaa`.
- TC-AUTH-RST-69 data: 7 karakter `Aa1!aaa`; 8 karakter `Aa1!aaaa`; 72 karakter `Aa1!` + 68 karakter "a"; 73 karakter `Aa1!` + 69 karakter "a".
- TC-AUTH-RST-80 data: karakter spesial valid `_` `-` `.` `#` `!` `@` `?` `&` `~`; bukan karakter spesial `é`, `😀`, spasi.

## Test Steps

### TC-AUTH-RST-67: Checklist dievaluasi reaktif pada setiap karakter yang diketik

1. Buka jendela privat baru lalu buka tautan reset milik `budisantoso+{runId}-025@qwertysystem.net` dari mail-catcher sehingga Setup New Password tampil
2. Ketik "a" pada field Password
3. Verifikasi "One lowercase (a-z)" dan "Password cannot contain spaces" terpenuhi
4. Verifikasi ikon kedua item tersebut berupa centang hitam
5. Verifikasi teks kedua item tersebut berwarna hitam
6. Verifikasi empat item lain abu-abu
7. Tambahkan "B" sehingga isi menjadi "aB"
8. Verifikasi "One uppercase (A-Z)" ikut terpenuhi
9. Tambahkan "1" sehingga isi menjadi "aB1"
10. Verifikasi "One number (0-9)" ikut terpenuhi
11. Tambahkan "!" sehingga isi menjadi "aB1!"
12. Verifikasi "One special character" ikut terpenuhi
13. Verifikasi "Minimum 8 characters" masih abu-abu
14. Tambahkan "aaaa" sehingga isi menjadi "aB1!aaaa"
15. Verifikasi "Minimum 8 characters" terpenuhi sehingga keenam item terpenuhi
16. Hapus semua karakter satu per satu sampai kosong
17. Verifikasi item kembali abu-abu satu per satu mengikuti karakter yang dihapus
18. Verifikasi semua item abu-abu saat field kosong

### TC-AUTH-RST-68: Spasi membuat item Password cannot contain spaces tidak terpenuhi

19. Ketik "aB1! aaa" pada field Password
20. Verifikasi item "Password cannot contain spaces" berstatus belum terpenuhi
21. Verifikasi ikon item "Password cannot contain spaces" berupa lingkaran kosong abu-abu
22. Verifikasi item "Minimum 8 characters", "One uppercase (A-Z)", "One lowercase (a-z)", "One number (0-9)", dan "One special character" berstatus terpenuhi

### TC-AUTH-RST-69: Batas panjang password 7, 8, dan 73 karakter

23. Kosongkan field Password lalu ketik "Aa1!aaa" (7 karakter)
24. Verifikasi "Minimum 8 characters" belum terpenuhi (abu-abu)
25. Tambahkan "a" sehingga menjadi "Aa1!aaaa" (8 karakter)
26. Verifikasi "Minimum 8 characters" terpenuhi
27. Ganti isi dengan password 72 karakter (`Aa1!` + 68 karakter "a")
28. Verifikasi caption "Max. 72 characters" tidak tampil
29. Tambahkan satu karakter sehingga menjadi 73 karakter
30. Verifikasi caption terpisah "Max. 72 characters" tampil real-time pada field Password
31. Verifikasi field Password berstatus Invalid
32. Verifikasi checklist tetap 6 baris
33. Verifikasi checklist tidak memuat baris "Max. 72 characters"

### TC-AUTH-RST-80: Karakter yang dihitung sebagai karakter spesial

34. Kosongkan field Password lalu ketik "Aa1_aaaa"
35. Verifikasi item "One special character" terpenuhi
36. Verifikasi ikon item "One special character" berupa centang hitam
37. Ulangi dengan "Aa1-aaaa", "Aa1.aaaa", "Aa1#aaaa", "Aa1!aaaa", "Aa1@aaaa", "Aa1?aaaa", "Aa1&aaaa", dan "Aa1~aaaa"
38. Verifikasi item "One special character" terpenuhi untuk setiap karakter ASCII non-alfanumerik tersebut
39. Ulangi dengan "Aa1éaaaa" dan "Aa1😀aaaa"
40. Verifikasi item "One special character" tetap belum terpenuhi untuk karakter non-ASCII `é` dan `😀`
41. Ulangi dengan "Aa1 aaaa" (spasi)
42. Verifikasi item "One special character" belum terpenuhi
43. Verifikasi item "Password cannot contain spaces" belum terpenuhi
44. Ulangi dengan "Aaaaaaaa1" (tanpa karakter non-alfanumerik)
45. Verifikasi item "One special character" belum terpenuhi

## Notes

- Sumber: `auth/reset-password/TestCases/tc-reset-password.md`. Satu token dipakai bersama karena tidak ada submit; spec ini hanya mengamati checklist sehingga token tidak dikonsumsi.
- Mengosongkan field Password antar-TC adalah langkah penghubung (S-09, S-03).
- Himpunan karakter spesial mengikuti keputusan NC-17 di TC sumber (semua ASCII non-alfanumerik yang dapat dicetak selain spasi).
- Jumlah langkah 45 melampaui ±35: alasan Verifikasi dipecah per klausa sesuai S-01 (28 dari 45 langkah adalah Verifikasi; 17 sisanya aksi mengetik atau mengosongkan field, termasuk langkah penghubung S-09 dan langkah 1 membuka tautan reset). Satu topik (checklist Password Policy), satu kelas harness (fungsional, tanpa submit, satu form), tanpa prefix login berulang (tidak ada login).
