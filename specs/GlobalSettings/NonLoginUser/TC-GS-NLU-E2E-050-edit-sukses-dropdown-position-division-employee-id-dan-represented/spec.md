---
id: TC-GS-NLU-E2E-050-edit-sukses-dropdown-position-division-employee-id-dan-represented
title: "Edit sukses: dropdown, Position Division Employee ID, dan Represented By"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-162
  - TC-GS-NLU-173
  - TC-GS-NLU-174
coverage:
  web: automated
---

# Edit sukses: dropdown, Position Division Employee ID, dan Represented By

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/non-login-user.json`, nilai dirujuk sebagai `Fixture.nonLoginUser.<key>` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): Position `Driver`, Division `Operations` dan `Logistics`, serta Login User Ahmad Fauzi dan Dewi Anggraini (halaman Detail Login User dan Tab Non-Login User milik keduanya hanya dibaca).
- Data milik spec (di-seed hook `before` lewat API, dihapus hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE; Tabel Data Uji Pre-setup No. 12 sebagai acuan): Non-Login User Edit Target 41 (TC-GS-NLU-162 dan TC-GS-NLU-173; First Name `Edit Target 41`, Last Name `{runId}-050`, Email `edittarget41+{runId}-050@qwertysystem.net`, tanpa Position dan Employee ID, Division `Operations`, Represented By `Ahmad Fauzi`, Active) dan Edit Target 42 (TC-GS-NLU-174; sama dengan Edit Target 41 tetapi nomor 42, Email `edittarget42+{runId}-050@qwertysystem.net`, Represented By `Ahmad Fauzi`).
- Data uji: Position `Driver`, Division `Logistics`, Employee ID `NL-9041-{runId}-050` (TC-GS-NLU-173 menulis `NL-9041`; suffix per run, S-12); Represented By baru `Dewi Anggraini` (TC-GS-NLU-174).
- State global: tidak ada yang diubah.

## Test Steps

1. Ketik Search `Edit Target 41 {runId}-050`, tekan Enter
2. Klik `⋯` pada baris Edit Target 41 > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi

### TC-GS-NLU-162: Dropdown Position dan Division searchable pada Popup Edit

3. Klik dropdown Position
4. Verifikasi dropdown Position menampilkan placeholder `Select position`
5. Verifikasi kotak pencarian dropdown Position berplaceholder `Search position...`
6. Ketik `driv` pada kotak pencarian Position
7. Verifikasi daftar Position menyempit ke `Driver`
8. Klik dropdown Division
9. Verifikasi dropdown Division menampilkan placeholder `Select division`
10. Verifikasi kotak pencarian dropdown Division berplaceholder `Search division...`
11. Ketik `logi` pada kotak pencarian Division
12. Verifikasi daftar Division menyempit ke `Logistics`

### TC-GS-NLU-173: Edit Position, Division, dan Employee ID tersimpan dan terlihat di tabel serta Detail

13. Pilih Position `Driver`
14. Pilih Division `Logistics`
15. Ubah Employee ID menjadi `NL-9041-{runId}-050`
16. Klik `[Save]`
17. Verifikasi Popup Edit menutup
18. Verifikasi toast sukses `Success, non-login user has been updated.`
19. Verifikasi baris tabel Edit Target 41 menampilkan Position `Driver`, Division `Logistics`, dan Employee ID `NL-9041-{runId}-050`
20. Buka Detail Edit Target 41
21. Verifikasi Detail menampilkan Position `Driver`, Division `Logistics`, dan Employee ID `NL-9041-{runId}-050`
22. Verifikasi field lain di Detail tidak berubah
23. Kembali ke daftar Non-Login User lewat breadcrumb

### TC-GS-NLU-174: Edit Represented By lewat popup Select User menyimpan Login User baru

24. Ketik Search `Edit Target 42 {runId}-050`, tekan Enter
25. Klik `⋯` pada baris Edit Target 42 > `Edit` sehingga Popup Edit Non-Login User terbuka dengan seluruh field terisi
26. Klik ikon `✎` pada badge Represented By
27. Klik baris Dewi Anggraini lalu klik `[Select]`
28. Klik `[Save]`
29. Verifikasi toast sukses `Success, non-login user has been updated.`
30. Verifikasi sel Represented By baris Edit Target 42 menampilkan `Dewi A`
31. Buka Detail Edit Target 42
32. Verifikasi Detail menampilkan Represented By `Dewi A`
33. Verifikasi tooltip Represented By di Detail `Dewi Anggraini`
34. Verifikasi Represented By di Detail berupa text link ke Detail Login User
35. Klik text link `Dewi A` sehingga Detail Login User Dewi Anggraini terbuka
36. Buka Tab "Non-Login User" milik Dewi Anggraini lalu ketik Search `Edit Target 42 {runId}-050`, tekan Enter
37. Verifikasi Tab "Non-Login User" milik Dewi Anggraini memuat baris Edit Target 42
38. Buka Detail Login User Ahmad Fauzi dan Tab "Non-Login User" miliknya
39. Ketik Search `Edit Target 42 {runId}-050`, tekan Enter
40. Verifikasi Tab "Non-Login User" milik Ahmad Fauzi menampilkan `No results found` untuk Edit Target 42

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber dipertahankan.
- Spec ini melewati sekitar 35 langkah (nominal 40). Alasan: ketiga blok adalah Popup Edit sukses yang berdiri sendiri; TC-GS-NLU-162 dan TC-GS-NLU-173 memakai Edit Target 41 sedangkan TC-GS-NLU-174 memakai Edit Target 42 dengan hasil Detail dan tab Login User sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung tanpa `Verifikasi`: langkah 1 dan 24 (Search Name bersuffix untuk menemukan baris target, R-16; Email bukan kolom Search List); langkah 23 (kembali ke daftar setelah Detail); langkah 35 dan 38 (berpindah ke Detail Login User untuk mengamati tab); langkah 36 dan 39 (Search Name bersuffix pada Tab "Non-Login User" untuk menemukan baris target; R-16).
- Absence pada Tab "Non-Login User" Ahmad Fauzi memakai empty state `No results found` hasil Search sebagai anchor positif.
- Temuan untuk QA:
  - TC-GS-NLU-162 menyebut placeholder `Select division` pada Edit Target 21, tetapi Division wajib dan terisi saat Popup Edit terbuka sehingga placeholder tidak teramati kecuali field dikosongkan; spec mengikuti TC. Edit Target 41 sengaja tanpa Position agar placeholder `Select position` teramati.
  - TC-GS-NLU-173 Post Condition butir b (Changelog, Activity Log, System Log mencatat tiap field) tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini.
  - TC-GS-NLU-174 Expected butir c tidak menyebut cara mencari baris di Tab "Non-Login User"; spec memakai Search dengan Name bersuffix.
  - Kolom yang dapat dicari pada Tab "Non-Login User" di Detail Login User (langkah 36 dan 39) belum terbukti di TC, PRD, atau LLD; spec memakai Name baris (`Edit Target 42 {runId}-050`) dan hasil pencarian perlu dikonfirmasi tim FE pada tahap script.
