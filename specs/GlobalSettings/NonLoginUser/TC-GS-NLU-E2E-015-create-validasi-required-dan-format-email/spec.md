---
id: TC-GS-NLU-E2E-015-create-validasi-required-dan-format-email
title: "Create: validasi required dan format Email"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-63
  - TC-GS-NLU-64
  - TC-GS-NLU-65
  - TC-GS-NLU-69
  - TC-GS-NLU-75
coverage:
  web: automated
---

# Create: validasi required dan format Email

## Prerequisites

- Mode: FE+BE (backend nyata; validasi server dan state tabel dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password lewat `Spectra.env.GS_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9 sampai 13, hanya dibaca): Division `Logistics`, Login User `Ahmad Fauzi` (pool Represented By).
- Data Dinamis: tidak ada record yang berhasil tersimpan di spec ini (semua Submit ditolak validasi). Email TC-GS-NLU-64 dan TC-GS-NLU-65 (`fikriramadhan@qwertysystem.net`) serta nilai field wajib lain TC-GS-NLU-69 (First Name `Fikri`, Last Name `Ramadhan`, Email `fikri.at.qwertysystem.net`, Division `Logistics`, Represented By `Ahmad Fauzi`) dipakai persis TC karena tidak pernah tersimpan. Cleanup di hook `after`: hapus Non-Login User ber-Email `fikriramadhan@qwertysystem.net` bila ada (tidak berasumsi).
- Kemampuan teknis: mengetik dan menempel emoji pada input; membaca jumlah total baris tabel (baseline B0) untuk asersi "tidak ada record dibuat/diubah".
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` belum ada dan dibuat di tahap script.
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

### Baseline

1. Catat jumlah total baris tabel Non-Login User sebagai baseline B0

### TC-GS-NLU-63: Validasi required First Name, Last Name, dan Email kosong

2. Klik `[+ Non-Login User]`
3. Pilih Division `Logistics` dan Represented By `Ahmad Fauzi`, biarkan First Name, Last Name, dan Email kosong
4. Klik `[Submit]`
5. Verifikasi First Name: pesan inline `First name must not be empty`
6. Verifikasi Last Name: pesan inline `Last name must not be empty`
7. Verifikasi Email: pesan inline `Email must not be empty`
8. Verifikasi Popup Create tetap terbuka
9. Verifikasi tidak ada toast tampil
10. Klik `[Clear Field]`

### TC-GS-NLU-64: Validasi required Division kosong

11. Isi First Name `Fikri`, Last Name `Ramadhan`, Email `fikriramadhan@qwertysystem.net`, dan pilih Represented By `Ahmad Fauzi` (Division dibiarkan belum dipilih)
12. Klik `[Submit]`
13. Verifikasi pesan inline di bawah Division: `Division must not be empty`
14. Verifikasi Popup Create tetap terbuka
15. Klik `[Clear Field]`

### TC-GS-NLU-65: Validasi required Represented By belum dipilih

16. Isi First Name `Fikri`, Last Name `Ramadhan`, Email `fikriramadhan@qwertysystem.net`, dan pilih Division `Logistics` (Represented By dibiarkan `[+ Select User]`)
17. Klik `[Submit]`
18. Verifikasi pesan inline di bawah Represented By: `Represented by must not be empty`
19. Verifikasi Popup Create tetap terbuka
20. Klik `[Clear Field]`

### TC-GS-NLU-69: Validasi format Email tidak valid

21. Isi Email `fikri.at.qwertysystem.net`
22. Lengkapi field wajib lain: First Name `Fikri`, Last Name `Ramadhan`, Division `Logistics`, Represented By `Ahmad Fauzi`
23. Klik `[Submit]`
24. Verifikasi pesan inline di bawah Email: `Invalid email format`
25. Verifikasi Popup Create tetap terbuka
26. Klik `[Clear Field]`

### TC-GS-NLU-75: Karakter emoji diblok saat mengetik dan menempel

27. Ketik `Budi😊` di First Name
28. Tempel `Santoso🔥` di Last Name
29. Verifikasi First Name hanya berisi `Budi` tanpa pesan error
30. Verifikasi Last Name hanya berisi `Santoso`

### Penutup

31. Klik `✕`
32. Verifikasi dialog `Unsaved Changes` tampil
33. Klik `[Leave]`
34. Verifikasi jumlah total baris tabel sama dengan baseline B0

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan mengikuti nomor TC; TC-GS-NLU-75 terakhir karena memakai field yang bukan bagian validasi submit.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (baseline B0), langkah 10, 15, 20, dan 26 (`[Clear Field]` agar pesan inline dan isian TC sebelumnya tidak terbawa; R-12), langkah 31 sampai 33 (menutup form dirty secara deterministik; S-08).
- Klausa "tidak ada record dibuat/diubah" pada TC-GS-NLU-63, 64, 65, dan 69 diasersi sekali di langkah 34 terhadap B0 karena Popup menutupi tabel; anchor positifnya adalah nilai B0 yang dibaca di langkah 1 dari tabel yang sama. Klausa ini tidak diasersi per TC.
- Langkah 8 dan 9 memetakan dua klausa Expected d TC-GS-NLU-63 ("Popup tetap terbuka" dan "tidak ada toast").
- Temuan untuk QA:
  - TC-GS-NLU-75 tidak menyatakan Expected untuk Post Condition dan tidak menyebut cara menempel emoji (clipboard); mekanisme ditentukan di tahap script.
  - TC-GS-NLU-65 langkah 2 dan langkah 3 saling tumpang tindih (Represented By dibiarkan kosong); spec mengikuti urutan TC.
  - Email `fikriramadhan@qwertysystem.net` tidak diberi suffix `{runId}` karena tidak pernah tersimpan; bila validasi server suatu saat menerima, cleanup hook `after` menghapusnya.
