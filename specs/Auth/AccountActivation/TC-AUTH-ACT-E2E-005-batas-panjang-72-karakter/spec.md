---
id: TC-AUTH-ACT-E2E-005-batas-panjang-72-karakter
title: "Batas Panjang 72 Karakter pada Password dan Confirm Password"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-ACT-32
  - TC-AUTH-ACT-33
  - TC-AUTH-ACT-34
  - TC-AUTH-ACT-35
  - TC-AUTH-ACT-36
  - TC-AUTH-ACT-37
  - TC-AUTH-ACT-135
coverage:
  web: automated
---

# Batas Panjang 72 Karakter pada Password dan Confirm Password

## Prerequisites

- Konteks browser: spec berjalan di konteks browser baru tanpa sesi login (jendela privat), sesuai precondition "Tanpa login" semua TC di spec ini.
- Seeding: setiap user Pending Activation dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`). Link aktivasi (token Active) diambil dari respons seeding API. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}` (contoh `budiaditya+{runId}-005@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: pemantauan request jaringan; paste dari clipboard.
- TC-AUTH-ACT-32: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-32: User `Ayu Kartika` (`ayukartika+{runId}-005@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-32 data: Password: `Aa1!` diikuti 68 karakter `x` (total 72 karakter), lalu `Aa1!` diikuti 69 karakter `x` (total 73 karakter)
- TC-AUTH-ACT-33 data: Password: `Aa1!` diikuti 68 karakter `x` (total 72 karakter)
- TC-AUTH-ACT-34 data: Password: `Aa1!` diikuti 76 karakter `x` (total 80 karakter)
- TC-AUTH-ACT-35 data: Password: `Aa1!` diikuti 69 karakter `x` (total 73 karakter) lalu dikurangi 1 karakter
- TC-AUTH-ACT-36 data: Password: `Aa1!` diikuti 68 karakter `x` (total 72 karakter); Confirm Password: `Aa1!` diikuti 68 karakter `x` (total 72 karakter), lalu `Aa1!` diikuti 69 karakter `x` (total 73 karakter)
- TC-AUTH-ACT-37: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-37: User `Darma Setiawan` (`darmasetiawan+{runId}-005@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-37 data: Password dan Confirm Password: `Aa1!` diikuti 69 karakter `x` (total 73 karakter)
- TC-AUTH-ACT-135: Tanpa login (halaman publik, tidak ada sesi aktif di browser)
- TC-AUTH-ACT-135: User `Rendra Pradana` (`rendrapradana+{runId}-005@qwertysystem.net`) berstatus Pending Activation dengan token aktivasi Active (di-seed lewat API di hook `before`, setara Global Settings > User > Create User; link aktivasi dari respons seeding)
- TC-AUTH-ACT-135 data: Password: `Aa1!` diikuti 68 karakter `x` (total 72 karakter); Confirm Password: `Bb2@` diikuti 69 karakter `x` (total 73 karakter, berbeda dari Password)
- Halaman dipakai berulang: TC-AUTH-ACT-33, 34, 35, 36 memakai halaman Set Password yang sama dengan TC-AUTH-ACT-32 (satu user, satu pembukaan link); field dikosongkan di antara kasus karena kasus-kasus ini hanya mengetik dan mengamati tanpa submit.

## Test Steps

### TC-AUTH-ACT-32: Mengetik 73 karakter di Password menampilkan error "Max. 72 characters" secara real-time

1. Buka link aktivasi user `Ayu Kartika` di browser → halaman `Auth > Account Activation > Set Password` tampil
2. Ketik `Aa1!` diikuti 68 karakter `x` (total 72 karakter) di field Password
3. Verifikasi Tidak ada pesan "Max. 72 characters"
4. Ketik satu karakter `x` tambahan sehingga total 73 karakter
5. Verifikasi Pesan inline "Max. 72 characters" muncul di bawah field Password seketika tanpa klik button "Set Password" (field Password berstatus Invalid)
6. Verifikasi Password Policy checklist tetap aktif dan tetap memperbarui status barisnya

### TC-AUTH-ACT-33: Tepat 72 karakter di Password tidak menampilkan error "Max. 72 characters"

7. Kosongkan field Password dan Confirm Password sehingga kembali ke state awal
8. Ketik `Aa1!` diikuti 68 karakter `x` (total 72 karakter) di field Password
9. Verifikasi Pesan "Max. 72 characters" tidak muncul
10. Verifikasi "Minimum 8 characters" hitam (primary) + ✓; "One uppercase (A-Z)" hitam (primary) + ✓; "One lowercase (a-z)" hitam (primary) + ✓; "One number (0-9)" hitam (primary) + ✓; "One special character" hitam (primary) + ✓; "Password cannot contain spaces" hitam (primary) + ✓

### TC-AUTH-ACT-34: Paste 80 karakter ke Password tersimpan penuh di field dan menampilkan error "Max. 72 characters"

11. Kosongkan field Password dan Confirm Password sehingga kembali ke state awal
12. Paste teks 80 karakter (`Aa1!` diikuti 76 karakter `x`) ke field Password
13. Verifikasi Pesan "Max. 72 characters" muncul real-time
14. Klik ikon toggle di field Password untuk melihat isi field
15. Verifikasi Field Password berisi seluruh 80 karakter yang di-paste (tidak dipotong menjadi 72)

### TC-AUTH-ACT-35: Error "Max. 72 characters" hilang real-time saat panjang kembali 72 karakter atau kurang

16. Kosongkan field Password dan Confirm Password sehingga kembali ke state awal
17. Ketik `Aa1!` diikuti 69 karakter `x` (total 73 karakter) di field Password
18. Verifikasi Pesan "Max. 72 characters" tampil
19. Hapus satu karakter sehingga total 72 karakter
20. Verifikasi Pesan "Max. 72 characters" hilang seketika tanpa klik button "Set Password"
21. Ketik satu karakter `x` lagi sehingga total 73 karakter
22. Verifikasi Pesan "Max. 72 characters" muncul kembali seketika

### TC-AUTH-ACT-36: Mengetik lebih dari 72 karakter di Confirm Password menampilkan error "Max. 72 characters" secara real-time

23. Kosongkan field Password dan Confirm Password sehingga kembali ke state awal
24. Ketik `Aa1!` diikuti 68 karakter `x` (total 72 karakter) di field Password
25. Ketik `Aa1!` diikuti 68 karakter `x` (total 72 karakter) di field Confirm Password
26. Verifikasi Tidak ada pesan "Max. 72 characters" pada field Confirm Password (tepat 72 karakter)
27. Ketik satu karakter `x` tambahan di field Confirm Password sehingga total 73 karakter
28. Verifikasi Pesan inline "Max. 72 characters" muncul di bawah field Confirm Password seketika tanpa klik button "Set Password"
29. Verifikasi Tidak ada pesan "Max. 72 characters" pada field Password

### TC-AUTH-ACT-37: Klik Set Password dengan 73 karakter tidak mengirim request dan tetap di halaman

30. Buka link aktivasi user `Darma Setiawan` di browser → halaman `Auth > Account Activation > Set Password` tampil
31. Ketik `Aa1!` diikuti 69 karakter `x` (total 73 karakter) di field Password dan field Confirm Password
32. Pantau request jaringan, lalu klik button "Set Password"
33. Verifikasi Tidak ada request set password yang dikirim ke server
34. Verifikasi Halaman tetap `Auth > Account Activation > Set Password`; pesan "Max. 72 characters" tetap tampil; tidak ada toast
35. Verifikasi Password Policy checklist tetap menampilkan status barisnya (tidak ada perubahan akibat klik)

### TC-AUTH-ACT-135: Klik Set Password dengan Confirm Password lebih dari 72 karakter dan berbeda dari Password hanya menampilkan error Max. 72 characters

36. Buka link aktivasi user `Rendra Pradana` di browser → halaman `Auth > Account Activation > Set Password` tampil
37. Ketik `Aa1!` diikuti 68 karakter `x` (total 72 karakter) di field Password
38. Ketik `Bb2@` diikuti 69 karakter `x` (total 73 karakter, berbeda dari Password) di field Confirm Password
39. Pantau request jaringan, lalu klik button "Set Password"
40. Verifikasi Inline error di bawah Confirm Password hanya "Max. 72 characters" (prioritas over-limit di atas mismatch)
41. Verifikasi Tidak ada pesan "Passwords do not match" pada field mana pun
42. Verifikasi Tidak ada request set password yang dikirim ke server; halaman tetap `Auth > Account Activation > Set Password` tanpa toast
43. Verifikasi Token aktivasi user `Rendra Pradana` tetap Active dan status user tetap Pending Activation

## Notes

- Mode: FE+BE. Sumber: `auth/account-activation/TestCases/tc-account-activation.md`.
- Spec ini 43 langkah, di atas smell sekitar 35 langkah (prinsip 13). Dipertahankan karena seluruh blok satu topik dan satu kelas (batas 72 karakter di Password dan Confirm Password, tanpa mail-catcher atau harness lain), tiap blok berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-AUTH-ACT-135 digabung ke sini (bukan spec baru) karena menguji batas 72 karakter yang sama, hanya pada field Confirm Password dengan nilai berbeda dari Password.
- TC-AUTH-ACT-37 dan TC-AUTH-ACT-135 tetap membuka link sendiri karena klik button "Set Password" meninggalkan state error submit yang dapat memengaruhi kasus sesudahnya.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
