---
id: TC-GS-NLU-E2E-026-create-sukses-custom-fields-dan-stay-on-this-form
title: "Create sukses: Custom Fields dan Stay on this form"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-94
  - TC-GS-NLU-98
coverage:
  web: automated
---

# Create sukses: Custom Fields dan Stay on this form

## Prerequisites

- Mode: FE+BE (backend nyata; record hasil Create dan Detail dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password lewat `Spectra.env.GS_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9, 10, dan 13, hanya dibaca): Division `Logistics`, Login User `Ahmad Fauzi` (pool Represented By), Custom Field aktif dan tidak Required: `Blood Type` (Dropdown A/B/O/AB), `Emergency Phone` (Phone), `Badge Note` (Text).
- Data Dinamis milik spec (Tabel Data Uji Dinamis No. 4 dan 2): Non-Login User `Gilang Pratama {runId}-026` (Division `Logistics`, Represented By `Ahmad Fauzi`, Blood Type `O`, Emergency Phone `+62 81234567890`), Email `gilangpratama+{runId}-026@qwertysystem.net`; Non-Login User `Populasi Satu {runId}-026` (Division `Logistics`, Represented By `Ahmad Fauzi`), Email `populasi01+{runId}-026@qwertysystem.net`. Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus Non-Login User ber-Email `+{runId}-026` lewat API (mekanisme disediakan tim FE/BE).
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` belum ada dan dibuat di tahap script.
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

### TC-GS-NLU-94: Bagian Custom Fields tampil dan nilai tersimpan

1. Klik `[+ Non-Login User]`
2. Verifikasi ketiga Custom Field (Blood Type, Emergency Phone, Badge Note) tampil di Popup Create sebelum diisi
3. Isi First Name `Gilang`, Last Name `Pratama {runId}-026`, dan Email `gilangpratama+{runId}-026@qwertysystem.net`, lalu pilih Division `Logistics`
4. Klik `[+ Select User]`, klik baris `Ahmad Fauzi` pada popup Select User, klik `[Select]`
5. Pilih Blood Type `O`
6. Isi Emergency Phone kode negara `+62` nomor `81234567890`
7. Klik `[Submit]`
8. Verifikasi toast sukses `Success, non-login user has been created.`
9. Ketik Search `Gilang Pratama {runId}-026`, tekan Enter
10. Buka Detail record `Gilang Pratama {runId}-026` dan perluas bagian Custom Fields
11. Verifikasi Detail menampilkan Blood Type `O`
12. Verifikasi Detail menampilkan Emergency Phone sesuai input (`+62 81234567890`)
13. Kembali ke halaman tabel Non-Login User

### TC-GS-NLU-98: Stay on this form tercentang mempertahankan popup terbuka dan mengosongkan field

14. Klik `[+ Non-Login User]`
15. Centang `Stay on this form after submitting`
16. Isi First Name `Populasi`, Last Name `Satu {runId}-026`, dan Email `populasi01+{runId}-026@qwertysystem.net`, lalu pilih Division `Logistics`
17. Klik `[+ Select User]`, klik baris `Ahmad Fauzi` pada popup Select User, klik `[Select]`
18. Klik `[Submit]`
19. Verifikasi toast sukses `Success, non-login user has been created.`
20. Verifikasi popup tetap terbuka
21. Verifikasi seluruh field kosong
22. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
23. Klik `✕`
24. Ketik Search `Populasi Satu {runId}-026`, tekan Enter
25. Verifikasi baris `Populasi Satu {runId}-026` muncul di tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC-GS-NLU-99 (Create beruntun 12 data) ada di spec 128 dan memakai `Populasi Satu` hasil seeding di sana (record spec ini bernama `Populasi Satu {runId}-026`).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 9 dan 24 (Search untuk menemukan baris target; R-16), langkah 10 (membuka Detail), langkah 13 (kembali ke tabel), langkah 23 (menutup popup yang sudah kosong sehingga tabel dapat diamati; popup kosong tidak memunculkan dialog Unsaved Changes).
- Temuan untuk QA:
  - TC-GS-NLU-94 Expected a menyebut Badge Note "dibiarkan kosong" tetapi tidak menyebut apa yang diasersi pada Badge Note sesudah Submit; spec tidak mengasersinya di Detail.
  - TC-GS-NLU-94 Expected c menyebut Emergency Phone "sesuai input" tanpa format tampilan; spec mengasersi `+62 81234567890` dari kolom Data Uji.
  - TC-GS-NLU-98 Expected c ("Baris Populasi Satu muncul di tabel") tidak menyebut cara menemukan baris saat popup masih terbuka; spec menutup popup (langkah 23) lalu mencari lewat Name bersuffix (kolom Name dapat dicari; kolom Email tidak termasuk kolom Search List).
