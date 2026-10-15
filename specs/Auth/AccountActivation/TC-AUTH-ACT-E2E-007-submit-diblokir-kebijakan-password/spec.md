---
id: TC-AUTH-ACT-E2E-007-submit-diblokir-kebijakan-password
title: "Submit Diblokir saat Password Tidak Memenuhi Policy"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-45
  - TC-AUTH-ACT-46
  - TC-AUTH-ACT-47
  - TC-AUTH-ACT-48
  - TC-AUTH-ACT-49
  - TC-AUTH-ACT-50
  - TC-AUTH-ACT-51
  - TC-AUTH-ACT-52
coverage:
  web: automated
---

# Submit Diblokir saat Password Tidak Memenuhi Policy

## Prerequisites

- Konteks browser: spec berjalan di konteks browser baru tanpa sesi login (jendela privat), sesuai precondition "Tanpa login" semua TC di spec ini.
- Seeding: setiap user Pending Activation dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`). Link aktivasi (token Active) diambil dari respons seeding API. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}` (contoh `budiaditya+{runId}-007@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: pemantauan request jaringan.
- TC-AUTH-ACT-45: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-45: User `Andi Safitri` (`andisafitri+{runId}-007@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-45 data: Password dan Confirm Password: `Abcde1!`
- TC-AUTH-ACT-46: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-46: User `Dewi Firmansyah` (`dewifirmansyah+{runId}-007@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-46 data: Password dan Confirm Password: `abcdefg1!`
- TC-AUTH-ACT-47: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-47: User `Rizky Pangestu` (`rizkypangestu+{runId}-007@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-47 data: Password dan Confirm Password: `ABCDEFG1!`
- TC-AUTH-ACT-48: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-48: User `Nur Suryani` (`nursuryani+{runId}-007@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-48 data: Password dan Confirm Password: `Abcdefgh!`
- TC-AUTH-ACT-49: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-49: User `Agus Kartika` (`aguskartika+{runId}-007@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-49 data: Password dan Confirm Password: `Abcdefg1`
- TC-AUTH-ACT-50: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-50: User `Rina Prasetyo` (`rinaprasetyo+{runId}-007@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-50 data: Password dan Confirm Password: `Abcd efg1!`
- TC-AUTH-ACT-51: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-51: User `Hendra Permana` (`hendrapermana+{runId}-007@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-51 data: Password dan Confirm Password: ` Abcdefg1!` (satu spasi di awal)
- TC-AUTH-ACT-52: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-52: User `Maya Purnama` (`mayapurnama+{runId}-007@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-52 data: Password dan Confirm Password: `Abcdefg1! ` (satu spasi di akhir)

## Test Steps

### TC-AUTH-ACT-45: Klik Set Password dengan password kurang dari 8 karakter tidak mengirim request

1. Buka link aktivasi user `Andi Safitri` di browser → halaman `Auth > Account Activation > Set Password` tampil
2. Ketik `Abcde1!` di field Password dan Confirm Password
3. Pantau request jaringan, lalu klik button "Set Password"
4. Verifikasi Tidak ada request set password yang dikirim ke server
5. Verifikasi Baris checklist "Minimum 8 characters" tetap abu-abu (disabled) + ○
6. Verifikasi Halaman tetap `Auth > Account Activation > Set Password`, tanpa toast, dan tidak ada inline error pada Confirm Password

### TC-AUTH-ACT-46: Klik Set Password dengan password tanpa huruf besar tidak mengirim request

7. Buka link aktivasi user `Dewi Firmansyah` di browser → halaman `Auth > Account Activation > Set Password` tampil
8. Ketik `abcdefg1!` di field Password dan Confirm Password
9. Pantau request jaringan, lalu klik button "Set Password"
10. Verifikasi Tidak ada request set password yang dikirim ke server
11. Verifikasi Baris checklist "One uppercase (A-Z)" tetap abu-abu (disabled) + ○
12. Verifikasi Halaman tetap `Auth > Account Activation > Set Password`, tanpa toast, dan tidak ada inline error pada Confirm Password

### TC-AUTH-ACT-47: Klik Set Password dengan password tanpa huruf kecil tidak mengirim request

13. Buka link aktivasi user `Rizky Pangestu` di browser → halaman `Auth > Account Activation > Set Password` tampil
14. Ketik `ABCDEFG1!` di field Password dan Confirm Password
15. Pantau request jaringan, lalu klik button "Set Password"
16. Verifikasi Tidak ada request set password yang dikirim ke server
17. Verifikasi Baris checklist "One lowercase (a-z)" tetap abu-abu (disabled) + ○
18. Verifikasi Halaman tetap `Auth > Account Activation > Set Password`, tanpa toast, dan tidak ada inline error pada Confirm Password

### TC-AUTH-ACT-48: Klik Set Password dengan password tanpa angka tidak mengirim request

19. Buka link aktivasi user `Nur Suryani` di browser → halaman `Auth > Account Activation > Set Password` tampil
20. Ketik `Abcdefgh!` di field Password dan Confirm Password
21. Pantau request jaringan, lalu klik button "Set Password"
22. Verifikasi Tidak ada request set password yang dikirim ke server
23. Verifikasi Baris checklist "One number (0-9)" tetap abu-abu (disabled) + ○
24. Verifikasi Halaman tetap `Auth > Account Activation > Set Password`, tanpa toast, dan tidak ada inline error pada Confirm Password

### TC-AUTH-ACT-49: Klik Set Password dengan password tanpa karakter spesial tidak mengirim request

25. Buka link aktivasi user `Agus Kartika` di browser → halaman `Auth > Account Activation > Set Password` tampil
26. Ketik `Abcdefg1` di field Password dan Confirm Password
27. Pantau request jaringan, lalu klik button "Set Password"
28. Verifikasi Tidak ada request set password yang dikirim ke server
29. Verifikasi Baris checklist "One special character" tetap abu-abu (disabled) + ○
30. Verifikasi Halaman tetap `Auth > Account Activation > Set Password`, tanpa toast, dan tidak ada inline error pada Confirm Password

### TC-AUTH-ACT-50: Klik Set Password dengan password berisi spasi di tengah tidak mengirim request

31. Buka link aktivasi user `Rina Prasetyo` di browser → halaman `Auth > Account Activation > Set Password` tampil
32. Ketik `Abcd efg1!` di field Password dan Confirm Password
33. Pantau request jaringan, lalu klik button "Set Password"
34. Verifikasi Tidak ada request set password yang dikirim ke server
35. Verifikasi Baris checklist "Password cannot contain spaces" tetap abu-abu (disabled) + ○
36. Verifikasi Halaman tetap `Auth > Account Activation > Set Password`, tanpa toast, dan tidak ada inline error pada Confirm Password

### TC-AUTH-ACT-51: Klik Set Password dengan password berisi spasi di awal tidak mengirim request

37. Buka link aktivasi user `Hendra Permana` di browser → halaman `Auth > Account Activation > Set Password` tampil
38. Ketik ` Abcdefg1!` di field Password dan Confirm Password
39. Pantau request jaringan, lalu klik button "Set Password"
40. Verifikasi Tidak ada request set password yang dikirim ke server
41. Verifikasi Baris checklist "Password cannot contain spaces" tetap abu-abu (disabled) + ○
42. Verifikasi Halaman tetap `Auth > Account Activation > Set Password`, tanpa toast, dan tidak ada inline error pada Confirm Password

### TC-AUTH-ACT-52: Klik Set Password dengan password berisi spasi di akhir tidak mengirim request

43. Buka link aktivasi user `Maya Purnama` di browser → halaman `Auth > Account Activation > Set Password` tampil
44. Ketik `Abcdefg1! ` di field Password dan Confirm Password
45. Pantau request jaringan, lalu klik button "Set Password"
46. Verifikasi Tidak ada request set password yang dikirim ke server
47. Verifikasi Baris checklist "Password cannot contain spaces" tetap abu-abu (disabled) + ○
48. Verifikasi Halaman tetap `Auth > Account Activation > Set Password`, tanpa toast, dan tidak ada inline error pada Confirm Password

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Spec ini 48 langkah, di atas smell sekitar 35 langkah (prinsip 13). Dipertahankan karena delapan blok adalah variasi satu aksi (klik Set Password dengan password yang melanggar satu aturan policy) di satu kelas, dan tiap blok membuka link user sendiri sehingga blok berikutnya tidak bergantung pada hasil blok sebelumnya. Pada tahap script, pola ini cocok ditulis berbasis tabel data.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
