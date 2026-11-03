---
id: TC-GS-NLU-E2E-025-create-sukses-field-wajib-saja-dan-seluruh-field
title: "Create sukses: field wajib saja dan seluruh field"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-96
  - TC-GS-NLU-97
coverage:
  web: automated
---

# Create sukses: field wajib saja dan seluruh field

## Prerequisites

- Mode: FE+BE (backend nyata; record hasil Create dan Detail dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password lewat `Spectra.env.GS_TC_PASSWORD`.
- Env var: `GS_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9, 10, dan 13, hanya dibaca): Position `Driver`, Division `Operations` dan `Logistics`, Login User `Ahmad Fauzi` dan `Andi Wijaya` (pool Represented By), Custom Field aktif `Blood Type` (opsi `A`). Format tanggal Detail mengikuti General Settings (Pre-setup No. 16: `dd/MM/yy`).
- Berkas uji di perangkat uji: foto PNG 200 KB (TC-GS-NLU-97).
- Data Dinamis milik spec (Tabel Data Uji Dinamis No. 1): Non-Login User `Budi Santoso {runId}-025` (Last Name `Santoso {runId}-025`, Division `Operations`, Represented By `Ahmad Fauzi`), Email `budisantoso+{runId}-025@qwertysystem.net`; Non-Login User `Dewi Anggraini {runId}-025` (Last Name `Anggraini {runId}-025`, Position `Driver`, Division `Logistics`, Employee ID `NL-8001-{runId}-025`, Represented By `Andi Wijaya`, Temporary Until +30 hari, Blood Type `A`, foto PNG 200 KB), Email `dewianggraini.nl+{runId}-025@qwertysystem.net`. Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus Non-Login User ber-Email `+{runId}-025` lewat API (mekanisme disediakan tim FE/BE).
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` belum ada dan dibuat di tahap script.
- State global yang diubah: tidak ada. Suite berjalan serial.

## Test Steps

### TC-GS-NLU-96: Create dengan field wajib saja (Stay unchecked)

1. Klik `[+ Non-Login User]`
2. Isi First Name `Budi`, Last Name `Santoso {runId}-025`, dan Email `budisantoso+{runId}-025@qwertysystem.net`, lalu pilih Division `Operations`
3. Klik `[+ Select User]`, klik baris `Ahmad Fauzi` pada popup Select User, klik `[Select]`
4. Klik `[Submit]`
5. Verifikasi toast sukses `Success, non-login user has been created.`
6. Verifikasi popup menutup
7. Ketik Search `Budi Santoso {runId}-025`, tekan Enter
8. Verifikasi baris `Budi Santoso {runId}-025` muncul di tabel dengan switch Active ON
9. Verifikasi pada baris `Budi Santoso {runId}-025` kolom Position `—` dan kolom Employee ID `—`
10. Verifikasi pada baris `Budi Santoso {runId}-025` kolom Represented By `Ahmad F`
11. Buka Detail record `Budi Santoso {runId}-025`
12. Verifikasi Detail menampilkan Division `Operations` dan Email `budisantoso+{runId}-025@qwertysystem.net`
13. Arahkan kursor ke Represented By pada Detail
14. Verifikasi Represented By `Ahmad F` dengan tooltip `Ahmad Fauzi`
15. Verifikasi Detail tidak menampilkan baris `Temporary until`
16. Verifikasi Detail menampilkan badge `Non Login`
17. Kembali ke halaman tabel Non-Login User

### TC-GS-NLU-97: Create dengan seluruh field terisi

18. Klik `[+ Non-Login User]`
19. Unggah foto PNG 200 KB pada avatar
20. Isi First Name `Dewi`, Last Name `Anggraini {runId}-025`, Employee ID `NL-8001-{runId}-025`, dan Email `dewianggraini.nl+{runId}-025@qwertysystem.net`, lalu pilih Position `Driver` dan Division `Logistics`
21. Klik `[+ Select User]`, klik baris `Andi Wijaya` pada popup Select User, klik `[Select]`
22. Centang `Set as Temporary User` dan pilih Temporary Until +30 hari
23. Pilih Blood Type `A`
24. Klik `[Submit]`
25. Verifikasi toast sukses `Success, non-login user has been created.`
26. Ketik Search `Dewi Anggraini {runId}-025`, tekan Enter
27. Buka Detail record `Dewi Anggraini {runId}-025`
28. Verifikasi Detail menampilkan foto
29. Verifikasi Detail menampilkan Position `Driver`, Division `Logistics`, Employee ID `NL-8001-{runId}-025`, dan Email `dewianggraini.nl+{runId}-025@qwertysystem.net`
30. Arahkan kursor ke Represented By pada Detail
31. Verifikasi Represented By `Andi W` dengan tooltip `Andi Wijaya`
32. Verifikasi `Temporary until` menampilkan tanggal +30 hari
33. Verifikasi Blood Type `A`
34. Verifikasi switch Active ON

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 7 dan 26 (Search untuk menemukan baris target lewat Name bersuffix; R-16), langkah 11 dan 27 (membuka Detail), langkah 13 dan 30 (hover untuk tooltip; 8b.5), langkah 17 (kembali ke tabel).
- Post Condition TC-GS-NLU-96 poin c (Changelog, Activity Log, System Log aktor mencatat `Create`) ditunjuk TC ke Section 5 dan poin d (opsi di dropdown FAMS, tab milik Ahmad Fauzi) diuji di modul konsumen; keduanya bukan Expected TC ini dan tidak diasersi (S-05).
- Temuan untuk QA:
  - TC-GS-NLU-97 Data Uji menulis `Dewi Anggraini.NL` sedangkan langkah mengisi Last Name `Anggraini` dan Email berakhiran `.nl`; spec mengikuti langkah dan memakai Email unik `dewianggraini.nl+{runId}-025`. Nama `Dewi Anggraini` juga milik Login User Pre-setup (pool Represented By) sehingga Last Name diberi suffix `{runId}-025` dan baris dicari lewat Name bersuffix (kolom Name dapat dicari; kolom Email tidak termasuk kolom Search List).
  - TC-GS-NLU-97 Expected b menyebut `Temporary until` "sesuai tanggal" tanpa format; spec mengasersi tanggal +30 hari dalam format Detail yang berlaku (Pre-setup No. 16).
  - TC-GS-NLU-96 dan TC-GS-NLU-97 tidak menyebut pencarian baris; spec mencarinya lewat Name bersuffix.
  - TC-GS-NLU-97 Data Uji tidak menulis suffix pada Employee ID `NL-8001`; spec menambah `-{runId}-025` karena nilai tersimpan unik per run (S-12).
