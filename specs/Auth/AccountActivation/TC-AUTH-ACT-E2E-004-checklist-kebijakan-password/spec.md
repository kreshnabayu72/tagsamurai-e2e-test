---
id: TC-AUTH-ACT-E2E-004-checklist-kebijakan-password
title: "Checklist Password Policy Real-time"
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
  - TC-AUTH-ACT-30
  - TC-AUTH-ACT-31
coverage:
  web: automated
---

# Checklist Password Policy Real-time

## Prerequisites

- Konteks browser: spec berjalan di konteks browser baru tanpa sesi login (jendela privat), sesuai precondition "Tanpa login" semua TC di spec ini.
- Seeding: setiap user Pending Activation dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`). Link aktivasi (token Active) diambil dari respons seeding API. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}` (contoh `budiaditya+{runId}-004@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- TC-AUTH-ACT-22: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-22: User `Ratna Anggraini` (`ratnaanggraini+{runId}-004@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-22 data: Password: `Abcde1!` lalu `Abcdef1!`
- TC-AUTH-ACT-23: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-23: User `Wahyu Susanto` (`wahyususanto+{runId}-004@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-23 data: Password: `abcdefg1!` lalu `Abcdefg1!`
- TC-AUTH-ACT-24: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-24: User `Tika Sulistyo` (`tikasulistyo+{runId}-004@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-24 data: Password: `ABCDEFG1!` lalu `ABCDEFG1!a`
- TC-AUTH-ACT-25: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-25: User `Joko Basuki` (`jokobasuki+{runId}-004@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-25 data: Password: `Abcdefgh!` lalu `Abcdefgh!1`
- TC-AUTH-ACT-26: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-26: User `Mega Fitriani` (`megafitriani+{runId}-004@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-26 data: Password: `Abcdefg1` lalu `Abcdefg1!`
- TC-AUTH-ACT-27: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-27: User `Arif Gunawan` (`arifgunawan+{runId}-004@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-27 data: Password: `Abcdefg1!` lalu `Abcd efg1!`
- TC-AUTH-ACT-28: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-28: User `Nina Safitri` (`ninasafitri+{runId}-004@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-28 data: Password: `Aman#Sandi8`
- TC-AUTH-ACT-29: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-29: User `Galih Firmansyah` (`galihfirmansyah+{runId}-004@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-29 data: Password: `a` lalu dikosongkan
- TC-AUTH-ACT-30: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-30: User `Citra Pangestu` (`citrapangestu+{runId}-004@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-30 data: Password: `Abcdefg1_`, `Abcdefg1#`, `Abcdefg1-`, `Abcdefg1~`
- TC-AUTH-ACT-31: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-31: User `Reza Suryani` (`rezasuryani+{runId}-004@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-31 data: Password: `Abcdefg1é`, `Abcdefg1😀`

## Test Steps

### TC-AUTH-ACT-22: Checklist real-time baris "Minimum 8 characters" berubah ke hitam saat terpenuhi dan kembali abu-abu saat tidak terpenuhi

1. Buka link aktivasi user `Ratna Anggraini` di browser → halaman `Auth > Account Activation > Set Password` tampil
2. Ketik `Abcde1!` di field Password
3. Verifikasi "Minimum 8 characters" abu-abu (disabled) + ○; "One uppercase (A-Z)" hitam (primary) + ✓; "One lowercase (a-z)" hitam (primary) + ✓; "One number (0-9)" hitam (primary) + ✓; "One special character" hitam (primary) + ✓; "Password cannot contain spaces" hitam (primary) + ✓
4. Sisipkan karakter `f` setelah `e` → `Abcdef1!` (8 karakter)
5. Verifikasi "Minimum 8 characters" hitam (primary) + ✓; "One uppercase (A-Z)" hitam (primary) + ✓; "One lowercase (a-z)" hitam (primary) + ✓; "One number (0-9)" hitam (primary) + ✓; "One special character" hitam (primary) + ✓; "Password cannot contain spaces" hitam (primary) + ✓ (berubah real-time tanpa klik button "Set Password")
6. Hapus karakter `f` → `Abcde1!` (7 karakter)
7. Verifikasi "Minimum 8 characters" abu-abu (disabled) + ○; "One uppercase (A-Z)" hitam (primary) + ✓; "One lowercase (a-z)" hitam (primary) + ✓; "One number (0-9)" hitam (primary) + ✓; "One special character" hitam (primary) + ✓; "Password cannot contain spaces" hitam (primary) + ✓

### TC-AUTH-ACT-23: Checklist real-time baris "One uppercase (A-Z)" berubah ke hitam saat terpenuhi dan kembali abu-abu saat tidak terpenuhi

8. Buka link aktivasi user `Wahyu Susanto` di browser → halaman `Auth > Account Activation > Set Password` tampil
9. Ketik `abcdefg1!` di field Password
10. Verifikasi "Minimum 8 characters" hitam (primary) + ✓; "One uppercase (A-Z)" abu-abu (disabled) + ○; "One lowercase (a-z)" hitam (primary) + ✓; "One number (0-9)" hitam (primary) + ✓; "One special character" hitam (primary) + ✓; "Password cannot contain spaces" hitam (primary) + ✓
11. Ganti karakter pertama menjadi `A` → `Abcdefg1!`
12. Verifikasi "Minimum 8 characters" hitam (primary) + ✓; "One uppercase (A-Z)" hitam (primary) + ✓; "One lowercase (a-z)" hitam (primary) + ✓; "One number (0-9)" hitam (primary) + ✓; "One special character" hitam (primary) + ✓; "Password cannot contain spaces" hitam (primary) + ✓ (berubah real-time tanpa klik button "Set Password")
13. Ganti karakter pertama kembali menjadi `a` → `abcdefg1!`
14. Verifikasi "Minimum 8 characters" hitam (primary) + ✓; "One uppercase (A-Z)" abu-abu (disabled) + ○; "One lowercase (a-z)" hitam (primary) + ✓; "One number (0-9)" hitam (primary) + ✓; "One special character" hitam (primary) + ✓; "Password cannot contain spaces" hitam (primary) + ✓

### TC-AUTH-ACT-24: Checklist real-time baris "One lowercase (a-z)" berubah ke hitam saat terpenuhi dan kembali abu-abu saat tidak terpenuhi

15. Buka link aktivasi user `Tika Sulistyo` di browser → halaman `Auth > Account Activation > Set Password` tampil
16. Ketik `ABCDEFG1!` di field Password
17. Verifikasi "Minimum 8 characters" hitam (primary) + ✓; "One uppercase (A-Z)" hitam (primary) + ✓; "One lowercase (a-z)" abu-abu (disabled) + ○; "One number (0-9)" hitam (primary) + ✓; "One special character" hitam (primary) + ✓; "Password cannot contain spaces" hitam (primary) + ✓
18. Tambah karakter `a` di akhir → `ABCDEFG1!a`
19. Verifikasi "Minimum 8 characters" hitam (primary) + ✓; "One uppercase (A-Z)" hitam (primary) + ✓; "One lowercase (a-z)" hitam (primary) + ✓; "One number (0-9)" hitam (primary) + ✓; "One special character" hitam (primary) + ✓; "Password cannot contain spaces" hitam (primary) + ✓ (berubah real-time tanpa klik button "Set Password")
20. Hapus karakter `a` → `ABCDEFG1!`
21. Verifikasi "Minimum 8 characters" hitam (primary) + ✓; "One uppercase (A-Z)" hitam (primary) + ✓; "One lowercase (a-z)" abu-abu (disabled) + ○; "One number (0-9)" hitam (primary) + ✓; "One special character" hitam (primary) + ✓; "Password cannot contain spaces" hitam (primary) + ✓

### TC-AUTH-ACT-25: Checklist real-time baris "One number (0-9)" berubah ke hitam saat terpenuhi dan kembali abu-abu saat tidak terpenuhi

22. Buka link aktivasi user `Joko Basuki` di browser → halaman `Auth > Account Activation > Set Password` tampil
23. Ketik `Abcdefgh!` di field Password
24. Verifikasi "Minimum 8 characters" hitam (primary) + ✓; "One uppercase (A-Z)" hitam (primary) + ✓; "One lowercase (a-z)" hitam (primary) + ✓; "One number (0-9)" abu-abu (disabled) + ○; "One special character" hitam (primary) + ✓; "Password cannot contain spaces" hitam (primary) + ✓
25. Tambah karakter `1` di akhir → `Abcdefgh!1`
26. Verifikasi "Minimum 8 characters" hitam (primary) + ✓; "One uppercase (A-Z)" hitam (primary) + ✓; "One lowercase (a-z)" hitam (primary) + ✓; "One number (0-9)" hitam (primary) + ✓; "One special character" hitam (primary) + ✓; "Password cannot contain spaces" hitam (primary) + ✓ (berubah real-time tanpa klik button "Set Password")
27. Hapus karakter `1` → `Abcdefgh!`
28. Verifikasi "Minimum 8 characters" hitam (primary) + ✓; "One uppercase (A-Z)" hitam (primary) + ✓; "One lowercase (a-z)" hitam (primary) + ✓; "One number (0-9)" abu-abu (disabled) + ○; "One special character" hitam (primary) + ✓; "Password cannot contain spaces" hitam (primary) + ✓

### TC-AUTH-ACT-26: Checklist real-time baris "One special character" berubah ke hitam saat terpenuhi dan kembali abu-abu saat tidak terpenuhi

29. Buka link aktivasi user `Mega Fitriani` di browser → halaman `Auth > Account Activation > Set Password` tampil
30. Ketik `Abcdefg1` di field Password
31. Verifikasi "Minimum 8 characters" hitam (primary) + ✓; "One uppercase (A-Z)" hitam (primary) + ✓; "One lowercase (a-z)" hitam (primary) + ✓; "One number (0-9)" hitam (primary) + ✓; "One special character" abu-abu (disabled) + ○; "Password cannot contain spaces" hitam (primary) + ✓
32. Tambah karakter `!` di akhir → `Abcdefg1!`
33. Verifikasi "Minimum 8 characters" hitam (primary) + ✓; "One uppercase (A-Z)" hitam (primary) + ✓; "One lowercase (a-z)" hitam (primary) + ✓; "One number (0-9)" hitam (primary) + ✓; "One special character" hitam (primary) + ✓; "Password cannot contain spaces" hitam (primary) + ✓ (berubah real-time tanpa klik button "Set Password")
34. Hapus karakter `!` → `Abcdefg1`
35. Verifikasi "Minimum 8 characters" hitam (primary) + ✓; "One uppercase (A-Z)" hitam (primary) + ✓; "One lowercase (a-z)" hitam (primary) + ✓; "One number (0-9)" hitam (primary) + ✓; "One special character" abu-abu (disabled) + ○; "Password cannot contain spaces" hitam (primary) + ✓

### TC-AUTH-ACT-27: Checklist real-time baris "Password cannot contain spaces" berubah ke hitam saat tanpa spasi dan kembali abu-abu saat ada spasi

36. Buka link aktivasi user `Arif Gunawan` di browser → halaman `Auth > Account Activation > Set Password` tampil
37. Ketik `Abcdefg1!` di field Password
38. Verifikasi "Minimum 8 characters" hitam (primary) + ✓; "One uppercase (A-Z)" hitam (primary) + ✓; "One lowercase (a-z)" hitam (primary) + ✓; "One number (0-9)" hitam (primary) + ✓; "One special character" hitam (primary) + ✓; "Password cannot contain spaces" hitam (primary) + ✓
39. Sisipkan spasi di tengah → `Abcd efg1!`
40. Verifikasi "Password cannot contain spaces" abu-abu (disabled) + ○; kelima baris lain tetap hitam (primary) + ✓
41. Hapus spasi → `Abcdefg1!`
42. Verifikasi "Password cannot contain spaces" hitam (primary) + ✓ kembali

### TC-AUTH-ACT-28: Semua baris checklist hitam saat password memenuhi seluruh aturan

43. Buka link aktivasi user `Nina Safitri` di browser → halaman `Auth > Account Activation > Set Password` tampil
44. Ketik `Aman#Sandi8` di field Password
45. Verifikasi "Minimum 8 characters" hitam (primary) + ✓; "One uppercase (A-Z)" hitam (primary) + ✓; "One lowercase (a-z)" hitam (primary) + ✓; "One number (0-9)" hitam (primary) + ✓; "One special character" hitam (primary) + ✓; "Password cannot contain spaces" hitam (primary) + ✓ — keenam baris hitam (primary) dengan ikon ✓, tidak ada baris abu-abu

### TC-AUTH-ACT-29: Status checklist saat field Password dikosongkan kembali setelah sempat terisi

46. Buka link aktivasi user `Galih Firmansyah` di browser → halaman `Auth > Account Activation > Set Password` tampil
47. Ketik `a` di field Password
48. Verifikasi "Password cannot contain spaces" berubah hitam (primary) + ✓ karena field berisi teks tanpa spasi; "One lowercase (a-z)" hitam + ✓; "Minimum 8 characters", "One uppercase (A-Z)", "One number (0-9)", "One special character" tetap abu-abu + ○
49. Hapus karakter `a` sehingga field Password kosong
50. Verifikasi Keenam baris checklist kembali abu-abu (disabled) + ○ seperti state awal, termasuk "Password cannot contain spaces"

### TC-AUTH-ACT-30: Simbol ASCII non-alfanumerik di luar `!@?&` dihitung sebagai karakter spesial

51. Buka link aktivasi user `Citra Pangestu` di browser → halaman `Auth > Account Activation > Set Password` tampil
52. Ketik `Abcdefg1_` di field Password
53. Verifikasi "One special character" hitam (primary) + ✓ untuk `_`
54. Kosongkan field, lalu ketik `Abcdefg1#`
55. Verifikasi "One special character" hitam + ✓ untuk `#`
56. Kosongkan field, lalu ketik `Abcdefg1-`
57. Verifikasi "One special character" hitam + ✓ untuk `-`
58. Kosongkan field, lalu ketik `Abcdefg1~`
59. Verifikasi "One special character" hitam + ✓ untuk `~`

### TC-AUTH-ACT-31: Huruf berdiakritik dan emoji diterima di field tetapi tidak dihitung sebagai karakter spesial

60. Buka link aktivasi user `Reza Suryani` di browser → halaman `Auth > Account Activation > Set Password` tampil
61. Ketik `Abcdefg1é` di field Password
62. Verifikasi Karakter `é` masuk ke field (tidak diblokir); "One special character" tetap abu-abu (disabled) + ○
63. Kosongkan field, lalu ketik `Abcdefg1😀`
64. Verifikasi Karakter `😀` masuk ke field (tidak diblokir); "One special character" tetap abu-abu (disabled) + ○

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
