---
id: TC-AUTH-ACT-E2E-006-validasi-kosong-dan-konfirmasi-tidak-sama
title: "Validasi Field Kosong dan Confirm Password Tidak Sama"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-38
  - TC-AUTH-ACT-39
  - TC-AUTH-ACT-40
  - TC-AUTH-ACT-41
  - TC-AUTH-ACT-42
  - TC-AUTH-ACT-43
  - TC-AUTH-ACT-44
  - TC-AUTH-ACT-53
  - TC-AUTH-ACT-54
  - TC-AUTH-ACT-55
  - TC-AUTH-ACT-56
coverage:
  web: automated
---

# Validasi Field Kosong dan Confirm Password Tidak Sama

## Prerequisites

- Konteks browser: spec berjalan di konteks browser baru tanpa sesi login (jendela privat), sesuai precondition "Tanpa login" semua TC di spec ini.
- Seeding: setiap user Pending Activation dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`). Link aktivasi (token Active) diambil dari respons seeding API. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}` (contoh `budiaditya+{runId}-006@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: pemantauan request jaringan.
- TC-AUTH-ACT-38: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-38: User `Kirana Utami` (`kiranautami+{runId}-006@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-38 data: Password: kosong; Confirm Password: kosong
- TC-AUTH-ACT-39: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-39: User `Surya Pratama` (`suryapratama+{runId}-006@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-39 data: Password: kosong; Confirm Password: `Aman#Sandi8`
- TC-AUTH-ACT-40: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-40: User `Anisa Nugroho` (`anisanugroho+{runId}-006@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-40 data: Password: `Aman#Sandi8`; Confirm Password: kosong
- TC-AUTH-ACT-41: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-41: User `Bagas Wibowo` (`bagaswibowo+{runId}-006@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-41 data: Password: `Aman#Sandi8`; Confirm Password: `Aman#Sandi9`
- TC-AUTH-ACT-42: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-42: User `Fitri Yulianti` (`fitriyulianti+{runId}-006@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-42 data: Password: `Aman#Sandi8`; Confirm Password: `aman#sandi8`
- TC-AUTH-ACT-43: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-43: User `Budi Fitriani` (`budifitriani+{runId}-006@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-43 data: Password: `Aman#Sandi8`; Confirm Password: `Aman#Sandi8 ` (spasi di akhir)
- TC-AUTH-ACT-44: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-44: User `Siti Gunawan` (`sitigunawan+{runId}-006@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-44 data: Password: `abc`; Confirm Password: `xyz`
- TC-AUTH-ACT-53: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-53: User `Fajar Wardana` (`fajarwardana+{runId}-006@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-54: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-54: User `Putri Setiawan` (`putrisetiawan+{runId}-006@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-54 data: Password: `Aman#Sandi8`; Confirm Password: `Aman#Sandi9`
- TC-AUTH-ACT-55: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-55: User `Dimas Utami` (`dimasutami+{runId}-006@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-55 data: Password: `a`
- TC-AUTH-ACT-56: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-56: User `Lestari Pratama` (`lestaripratama+{runId}-006@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-56 data: Password: `Aman#Sandi8`; Confirm Password: `x`

## Test Steps

### TC-AUTH-ACT-38: Klik Set Password dengan kedua field kosong menampilkan dua error inline

1. Buka link aktivasi user `Kirana Utami` di browser → halaman `Auth > Account Activation > Set Password` tampil
2. Biarkan field Password dan Confirm Password kosong, klik button "Set Password"
3. Verifikasi Inline error di bawah Password: "Password must not be empty"
4. Verifikasi Inline error di bawah Confirm Password: "Confirm password must not be empty"
5. Verifikasi Halaman tetap `Auth > Account Activation > Set Password` dan tidak ada request dikirim

### TC-AUTH-ACT-39: Klik Set Password dengan Password kosong dan Confirm Password terisi hanya menampilkan error Password kosong

6. Buka link aktivasi user `Surya Pratama` di browser → halaman `Auth > Account Activation > Set Password` tampil
7. Biarkan field Password kosong, ketik `Aman#Sandi8` di field Confirm Password
8. Klik button "Set Password"
9. Verifikasi Inline error di bawah Password: "Password must not be empty"
10. Verifikasi Tidak ada error "Passwords do not match" pada Confirm Password (mismatch tidak dievaluasi selama Password kosong)
11. Verifikasi Tidak ada request set password yang dikirim ke server

### TC-AUTH-ACT-40: Klik Set Password dengan Password valid dan Confirm Password kosong hanya menampilkan error Confirm kosong

12. Buka link aktivasi user `Anisa Nugroho` di browser → halaman `Auth > Account Activation > Set Password` tampil
13. Ketik `Aman#Sandi8` di field Password, biarkan Confirm Password kosong
14. Klik button "Set Password"
15. Verifikasi Inline error di bawah Confirm Password: "Confirm password must not be empty"
16. Verifikasi Tidak ada error "Passwords do not match" dan tidak ada error di field Password
17. Verifikasi Tidak ada request set password yang dikirim ke server

### TC-AUTH-ACT-41: Klik Set Password dengan Confirm Password berbeda menampilkan error "Passwords do not match"

18. Buka link aktivasi user `Bagas Wibowo` di browser → halaman `Auth > Account Activation > Set Password` tampil
19. Ketik `Aman#Sandi8` di field Password dan `Aman#Sandi9` di field Confirm Password
20. Klik button "Set Password"
21. Verifikasi Inline error di bawah Confirm Password: "Passwords do not match"
22. Verifikasi Halaman tetap `Auth > Account Activation > Set Password`; tidak ada request yang dikirim dan tidak ada toast

### TC-AUTH-ACT-42: Confirm Password yang hanya berbeda huruf besar-kecil dianggap tidak sama

23. Buka link aktivasi user `Fitri Yulianti` di browser → halaman `Auth > Account Activation > Set Password` tampil
24. Ketik `Aman#Sandi8` di field Password dan `aman#sandi8` di field Confirm Password
25. Klik button "Set Password"
26. Verifikasi Inline error di bawah Confirm Password: "Passwords do not match"
27. Verifikasi Halaman tetap `Auth > Account Activation > Set Password`; tidak ada request yang dikirim

### TC-AUTH-ACT-43: Confirm Password dengan spasi tambahan di akhir dianggap tidak sama

28. Buka link aktivasi user `Budi Fitriani` di browser → halaman `Auth > Account Activation > Set Password` tampil
29. Ketik `Aman#Sandi8` di field Password dan `Aman#Sandi8 ` (dengan satu spasi di akhir) di field Confirm Password
30. Klik button "Set Password"
31. Verifikasi Inline error di bawah Confirm Password: "Passwords do not match"
32. Verifikasi Halaman tetap `Auth > Account Activation > Set Password`; tidak ada request yang dikirim

### TC-AUTH-ACT-44: Password belum memenuhi policy dan Confirm Password berbeda tetap menampilkan error mismatch tanpa request

33. Buka link aktivasi user `Siti Gunawan` di browser → halaman `Auth > Account Activation > Set Password` tampil
34. Ketik `abc` di field Password dan `xyz` di field Confirm Password
35. Pantau request jaringan, lalu klik button "Set Password"
36. Verifikasi Inline error di bawah Confirm Password: "Passwords do not match" (Password terisi sehingga mismatch dievaluasi)
37. Verifikasi Tidak ada request dikirim; baris checklist yang belum terpenuhi tetap abu-abu (disabled) + ○; tidak ada toast

### TC-AUTH-ACT-53: Error kosong tidak muncul sebelum tombol Set Password ditekan

38. Buka link aktivasi user `Fajar Wardana` di browser → halaman `Auth > Account Activation > Set Password` tampil
39. Klik field Password lalu pindah fokus ke field Confirm Password tanpa mengetik apa pun
40. Klik di luar kedua field
41. Verifikasi Tidak ada inline error "Password must not be empty" maupun "Confirm password must not be empty" (dievaluasi hanya saat tombol "Set Password" ditekan)

### TC-AUTH-ACT-54: Error "Passwords do not match" hanya muncul saat submit, bukan saat mengetik

42. Buka link aktivasi user `Putri Setiawan` di browser → halaman `Auth > Account Activation > Set Password` tampil
43. Ketik `Aman#Sandi8` di field Password
44. Ketik `Aman#Sandi9` di field Confirm Password
45. Amati halaman sebelum klik button "Set Password"
46. Verifikasi Tidak ada pesan "Passwords do not match" selama mengetik dan sebelum button "Set Password" ditekan

### TC-AUTH-ACT-55: Error Password kosong hilang saat field Password diedit

47. Buka link aktivasi user `Dimas Utami` di browser → halaman `Auth > Account Activation > Set Password` tampil
48. Klik button "Set Password" dengan kedua field kosong
49. Verifikasi "Password must not be empty" dan "Confirm password must not be empty" tampil
50. Ketik `a` di field Password
51. Verifikasi "Password must not be empty" hilang seketika setelah field Password diedit; "Confirm password must not be empty" tetap tampil

### TC-AUTH-ACT-56: Error Confirm Password hilang saat field diedit dan dievaluasi ulang pada submit berikutnya

52. Buka link aktivasi user `Lestari Pratama` di browser → halaman `Auth > Account Activation > Set Password` tampil
53. Ketik `Aman#Sandi8` di field Password, biarkan Confirm Password kosong, klik button "Set Password"
54. Verifikasi "Confirm password must not be empty" tampil
55. Ketik `x` di field Confirm Password
56. Verifikasi "Confirm password must not be empty" hilang seketika setelah field Confirm Password diedit
57. Klik button "Set Password"
58. Verifikasi "Passwords do not match" tampil di bawah Confirm Password (dievaluasi ulang saat submit)

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
