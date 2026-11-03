---
id: TC-GS-NLU-E2E-121-multi-konteks-dua-admin-edit-create-email-sama-employee
title: "Multi-konteks: dua admin Edit, Create email sama, Employee ID sama, slot terakhir limit"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-184
  - TC-GS-NLU-440
  - TC-GS-NLU-441
  - TC-GS-NLU-478
coverage:
  web: automated
---

# Multi-konteks: dua admin Edit, Create email sama, Employee ID sama, slot terakhir limit

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata dengan dua sesi UI (sesi A dan sesi B); tidak ada respons yang di-mock atau di-intercept.
- Role yang diuji:

| Sesi | Akun | Env var password |
|---|---|---|
| A | Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1) | `Spectra.env.GS_TC_PASSWORD` |
| B | Total Control kedua (admin kedua); tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.GS_TC2_PASSWORD` |

- Environment variable: `GS_TC_PASSWORD`, `GS_TC2_PASSWORD`.
- Login sesi A di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Sesi B dibuka sebagai jendela browser kedua pada langkah 1 dan ditutup hook `after`. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup No. 9 sampai 13 (Position `Driver` dan `Manager`; Division `Operations`, `Warehouse`, `Logistics`, `Finance`; Login User `Ahmad Fauzi` dan `Dewi Anggraini`; Custom Field dasar) hanya dibaca, tidak diubah atau dihapus.
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE):
  - TC-GS-NLU-184: `Dua Admin {runId}-121` (First Name `Dua`, Last Name `Admin {runId}-121`, Division `Operations`, Email `duaadmin+{runId}-121@qwertysystem.net`, Represented By `Ahmad Fauzi`, Active).
  - TC-GS-NLU-440 (dibuat lewat UI): First Name `Kembar`, Last Name `Email {runId}-121`, Division `Logistics`, Email `kembar+{runId}-121@qwertysystem.net` pada kedua sesi, Represented By `Ahmad Fauzi`.
  - TC-GS-NLU-478 (dibuat lewat UI): First Name `Kembar`, Last Name `EmpA {runId}-121` (sesi A) dan `EmpB {runId}-121` (sesi B), Email `kembarempa+{runId}-121@qwertysystem.net` dan `kembarempb+{runId}-121@qwertysystem.net`, Employee ID `EMP-KEMBAR-{runId}-121` pada kedua sesi (belum dipakai), Division `Logistics`, Represented By `Ahmad Fauzi`.
  - TC-GS-NLU-441 (dibuat lewat UI): First Name `Slot`, Last Name `A {runId}-121` (sesi A) dan `B {runId}-121` (sesi B), Email `slota+{runId}-121@qwertysystem.net` dan `slotb+{runId}-121@qwertysystem.net`, Division `Logistics`, Represented By `Ahmad Fauzi`.
- State global: Master Data Count Limit gabungan `1000`. Hook `before` mengatur limit dengan sisa slot yang cukup untuk TC-GS-NLU-440 dan TC-GS-NLU-478 (masing-masing menghabiskan satu slot); langkah penghubung 34 mengatur ulang sehingga tersisa tepat satu slot (jumlah master data gabungan 999) untuk TC-GS-NLU-441. Hook `after` memulihkan limit. Kemampuan dan akun pelaku perubahan limit di Admin Console tidak disebut TC, PRD, atau LLD sehingga disediakan tim FE. Suite berjalan serial (`parallel: false`).
- Pemulihan: hook `after` menghapus lewat API semua data `{runId}-121` yang tersisa dan memulihkan Master Data Count Limit.
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

1. Buka sesi B: jendela browser kedua, login sebagai Total Control kedua (`Spectra.env.GS_TC2_PASSWORD`), lalu buka Global Settings > User > User List > sub-tab Non-Login User

### TC-GS-NLU-184: Dua admin mengedit record yang sama, Save kedua sukses dan nilai akhir mengikuti Save terakhir

2. Sesi A: ketik Search `Dua Admin {runId}-121`, tekan Enter, klik `⋯` baris `Dua Admin {runId}-121` > `Edit`
3. Sesi B: ketik Search `Dua Admin {runId}-121`, tekan Enter, klik `⋯` baris `Dua Admin {runId}-121` > `Edit`
4. Sesi A: ubah First Name menjadi `AdminA`, lalu klik `[Save]`
5. Verifikasi sesi A menampilkan Toast sukses `Success, non-login user has been updated.`
6. Verifikasi sesi A tidak menampilkan dialog konflik
7. Sesi B (tanpa muat ulang): ubah First Name menjadi `AdminB`, lalu klik `[Save]`
8. Verifikasi sesi B menampilkan Toast sukses `Success, non-login user has been updated.`
9. Verifikasi sesi B tidak menampilkan dialog konflik
10. Sesi A: muat ulang list dengan F5, lalu ketik Search `Admin {runId}-121`, tekan Enter
11. Verifikasi First Name akhir baris record tersebut `AdminB` (last-write-wins)

### TC-GS-NLU-440: Dua admin membuat Non-Login User dengan email sama, submit kedua ditolak inline

12. Sesi A: klik `[+ Non-Login User]`, isi First Name `Kembar`, Last Name `Email {runId}-121`, Division `Logistics`, Email `kembar+{runId}-121@qwertysystem.net`, pilih Represented By `Ahmad Fauzi`
13. Sesi B: klik `[+ Non-Login User]`, isi First Name `Kembar`, Last Name `Email {runId}-121`, Division `Logistics`, Email `kembar+{runId}-121@qwertysystem.net`, pilih Represented By `Ahmad Fauzi`
14. Sesi A: klik `[Submit]`
15. Verifikasi sesi A menampilkan Toast sukses `Success, non-login user has been created.`
16. Sesi B: klik `[Submit]`
17. Verifikasi sesi B menampilkan pesan inline `Email already exists` pada field Email
18. Verifikasi form Create sesi B tetap terbuka
19. Verifikasi sesi B tidak menampilkan dialog
20. Sesi B: tutup popup Create dengan `✕`
21. Verifikasi dialog `Unsaved Changes` tampil di sesi B
22. Sesi B: klik `[Leave]`

### TC-GS-NLU-478: Dua admin membuat Non-Login User dengan Employee ID sama, submit kedua ditolak inline

23. Sesi A: klik `[+ Non-Login User]`, isi First Name `Kembar`, Last Name `EmpA {runId}-121`, Division `Logistics`, Email `kembarempa+{runId}-121@qwertysystem.net`, Employee ID `EMP-KEMBAR-{runId}-121`, pilih Represented By `Ahmad Fauzi`
24. Sesi B: klik `[+ Non-Login User]`, isi First Name `Kembar`, Last Name `EmpB {runId}-121`, Division `Logistics`, Email `kembarempb+{runId}-121@qwertysystem.net`, Employee ID `EMP-KEMBAR-{runId}-121`, pilih Represented By `Ahmad Fauzi`
25. Sesi A: klik `[Submit]`
26. Verifikasi sesi A menampilkan Toast sukses `Success, non-login user has been created.`
27. Sesi B: klik `[Submit]`
28. Verifikasi sesi B menampilkan pesan inline `Employee ID already exists` pada field Employee ID
29. Verifikasi form Create sesi B tetap terbuka
30. Verifikasi sesi B tidak menampilkan dialog
31. Sesi B: tutup popup Create dengan `✕`
32. Verifikasi dialog `Unsaved Changes` tampil di sesi B
33. Sesi B: klik `[Leave]`

### TC-GS-NLU-441: Dua admin membuat pada slot terakhir Master Data Count Limit, hanya satu berhasil

34. Atur Master Data Count Limit gabungan `1000` sehingga tersisa tepat satu slot (jumlah master data gabungan 999)
35. Sesi A: klik `[+ Non-Login User]`, isi First Name `Slot`, Last Name `A {runId}-121`, Division `Logistics`, Email `slota+{runId}-121@qwertysystem.net`, pilih Represented By `Ahmad Fauzi`
36. Sesi B: klik `[+ Non-Login User]`, isi First Name `Slot`, Last Name `B {runId}-121`, Division `Logistics`, Email `slotb+{runId}-121@qwertysystem.net`, pilih Represented By `Ahmad Fauzi`
37. Klik `[Submit]` di sesi A dan sesi B hampir bersamaan
38. Verifikasi tepat satu dari sesi A dan sesi B menampilkan Toast sukses `Success, non-login user has been created.`
39. Verifikasi sesi yang lain menampilkan dialog dengan Title `Limit Reached` dan isi `You've reached the platform limit of 1000 users. Contact support if you need a higher limit.`
40. Verifikasi sesi yang lain tidak menampilkan pesan duplikat (`Email already exists`)
41. Sesi yang ditolak (sesi yang menampilkan dialog `Limit Reached` pada langkah 39): tutup dialog `Limit Reached`
42. Sesi yang ditolak: tutup popup Create dengan `✕`
43. Verifikasi dialog `Unsaved Changes` tampil di sesi yang ditolak
44. Sesi yang ditolak: klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Kelas c (multi-konteks): dua sesi UI karena hasil di kedua sesi diasersi. Kuota Master Data Count Limit pada TC-GS-NLU-441 adalah pemicu state race dua sesi dan spec ini tidak dipindah ke kelas e (P-2).
- Langkah penghubung (S-03, R-16): langkah 1 (membuka sesi B), langkah 2, 3, 10 (Search record yang dicari dan membuka popup), langkah 12, 13, 23, 24, 35, 36 (membuka popup Create di kedua sesi), langkah 34 (mengatur Master Data Count Limit hingga tersisa satu slot), langkah 20, 22, 31, 33 (menutup form dirty sesi B dengan `✕` dan `[Leave]`, `Verifikasi` dialog `Unsaved Changes` pada langkah 21 dan 32, S-08), dan langkah 41, 42, dan 44 (menutup dialog `Limit Reached` dan popup Create sesi yang ditolak dengan `✕` dan `[Leave]`, `Verifikasi` dialog `Unsaved Changes` pada langkah 43, S-08).
- Di atas 35 langkah, alasan: Alasan jumlah langkah: nominal 44 langkah. Semua blok kelas c dengan harness yang sama (dua sesi UI), dan tiap blok memakai record serta field uji sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-NLU-184, 440, 441, dan 478 menyebut "dua sesi admin" tanpa akun admin kedua; Pre-setup No. 1 sampai 8 tidak memuat Total Control kedua. Env `GS_TC2_PASSWORD` sudah terdaftar untuk "admin kedua Total Control Client A" di suite lain dan dipakai ulang; kecocokan akun dengan Client suite ini perlu dikonfirmasi tim FE.
  - TC-GS-NLU-441 menyebut "limit `1000`" dan "sisa slot tepat 1" sedangkan Pre-setup No. 17 menyatakan limit diturunkan penguji; dialog TC memuat angka 1000 sehingga spec mengatur limit 1000 dengan 999 master data pada langkah 34 (hook `before` hanya menyisakan slot cukup untuk TC-GS-NLU-440 dan TC-GS-NLU-478). Cara mencapai jumlah itu tidak disebut TC, PRD, atau LLD dan disediakan tim FE.
  - TC-GS-NLU-441 tidak menyebut cara menutup dialog `Limit Reached`; spec menulis "tutup dialog" tanpa menyebut tombol.
  - TC-GS-NLU-441 tidak menyebut sesi mana yang berhasil; spec mengasersi tepat satu sesi sukses dan sesi lain menampilkan dialog `Limit Reached`.
  - TC-GS-NLU-478 menyebut "seluruh field wajib lain terisi valid" tanpa nilai; Email dibedakan per sesi supaya hanya duplikat Employee ID yang diuji.
  - TC-GS-NLU-184 Expected b menyebut nama akhir `AdminB`; nama record memakai Last Name bersuffix sehingga baris dicari lewat Search `Admin {runId}-121`.
