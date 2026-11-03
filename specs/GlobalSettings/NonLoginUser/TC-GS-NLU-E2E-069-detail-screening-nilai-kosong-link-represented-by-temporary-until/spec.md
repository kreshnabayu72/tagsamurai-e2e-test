---
id: TC-GS-NLU-E2E-069-detail-screening-nilai-kosong-link-represented-by-temporary-until
title: "Detail: Screening, Nilai Kosong, Link Represented By, Temporary Until, Custom Fields, dan Tanpa Access Level"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-247
  - TC-GS-NLU-248
  - TC-GS-NLU-249
  - TC-GS-NLU-250
  - TC-GS-NLU-251
  - TC-GS-NLU-252
  - TC-GS-NLU-451
  - TC-GS-NLU-459
coverage:
  web: automated
---

# Detail: Screening, Nilai Kosong, Link Represented By, Temporary Until, Custom Fields, dan Tanpa Access Level

## Prerequisites

- Mode: FE+BE (backend nyata). Spec hanya membaca data dan tidak mengubahnya.
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup No. 11 yang dibaca (tidak diubah dan tidak dihapus): `Budi Kurniawan` (Position Field Technician, Division Operations, Employee ID `FT-0231`, Email `budi.kurniawan@qwertysystem.net`, Represented By Ahmad Fauzi, foto, Active, Custom Field terisi), `Siti Rahayu` (tanpa Position dan Employee ID, Division Warehouse, Active, Represented By terisi), `Rina Marlina` (Temporary +30 hari, Position Driver, Division Logistics). Pre-setup No. 10: Login User `Ahmad Fauzi`. Pre-setup No. 16: Date Format `dd/MM/yy`.
- Spec tidak menulis atau menghapus data (S-06); kesamaan nama record Pre-setup dengan record bersuffix milik spec lain diatasi dengan mengklik teks Name yang persis sama.
- State global yang diubah: tidak ada.

## Test Steps


### TC-GS-NLU-248: Row action Detail dan klik Name membuka Detail yang sama

1. Ketik Search `Budi Kurniawan`, tekan Enter
2. Klik `⋯` pada baris `Budi Kurniawan` > `Detail`
3. Verifikasi Detail `Budi Kurniawan` terbuka pada tab browser yang sama dengan tab Responsibilities dan sub-tab Borrowed Assets aktif
4. Kembali ke list Non-Login User
5. Klik teks Name `Budi Kurniawan`
6. Verifikasi Detail `Budi Kurniawan` terbuka pada tab browser yang sama dengan tab Responsibilities dan sub-tab Borrowed Assets aktif

### TC-GS-NLU-247: Screening halaman Detail Non-Login User

7. Verifikasi Breadcrumb `User > Detail`
8. Verifikasi `[Avatar]` `Budi Kurniawan` dengan switch Active ON
9. Verifikasi menu `⋯` tampil di header
10. Verifikasi subtitle Employee ID `FT-0231` (teks muted)
11. Verifikasi General Information `Position` `Field Technician`
12. Verifikasi General Information `Division` `Operations`
13. Verifikasi General Information `Email` `budi.kurniawan@qwertysystem.net`
14. Verifikasi General Information `Represented By` `Ahmad F` dengan ikon user, tooltip `Ahmad Fauzi`, dan tampil sebagai link
15. Verifikasi General Information `User Type` badge `Non Login` (gelap)
16. Verifikasi section Custom Fields collapsible dan collapsed by default
17. Verifikasi tab `Responsibilities` (aktif) dan `Changelog`
18. Verifikasi tidak ada tab System Log dan User Log
19. Verifikasi tidak ada footer halaman

### TC-GS-NLU-252: Custom Fields collapsed secara default dan dapat diperluas

20. Klik section Custom Fields untuk memperluas
21. Verifikasi section Custom Fields menampilkan nilai Custom Field `Budi Kurniawan`

### TC-GS-NLU-250: Represented By di Detail adalah link ke Detail Login User

22. Hover `Ahmad F` pada Represented By
23. Verifikasi tooltip `Ahmad Fauzi`
24. Klik `Ahmad F` pada Represented By
25. Verifikasi navigasi ke Detail Login User Ahmad Fauzi

### TC-GS-NLU-249: Nilai kosong General Information tampil strip

26. Kembali ke list Non-Login User
27. Ganti isi kotak search dengan `Siti Rahayu`, tekan Enter
28. Klik teks Name `Siti Rahayu`
29. Verifikasi General Information `Position` menampilkan `—`
30. Verifikasi General Information `Division` `Warehouse`
31. Verifikasi General Information `Email` terisi
32. Verifikasi General Information `Represented By` terisi

### TC-GS-NLU-451: Subtitle Employee ID kosong tampil strip

33. Verifikasi subtitle di bawah nama menampilkan `—` karena Employee ID kosong

### TC-GS-NLU-251: Temporary User menampilkan Temporary until

34. Kembali ke list Non-Login User
35. Ganti isi kotak search dengan `Rina Marlina`, tekan Enter
36. Klik teks Name `Rina Marlina`
37. Verifikasi di bawah Represented By tampil `Temporary until` diikuti tanggal Temporary Until record dalam Date Format General Settings (`dd/MM/yy`)

### TC-GS-NLU-459: Form dan Detail tidak memiliki field Access Level

38. Kembali ke list Non-Login User
39. Klik `[+ Non-Login User]` sehingga Popup Create Non-Login User terbuka
40. Verifikasi Popup Create hanya memuat Photo, First Name, Last Name, Position, Division, Employee ID, Email, Represented By, Temporary User, dan Custom Field aktif
41. Verifikasi Popup Create tidak memuat field Access Level
42. Tutup Popup Create dengan `✕`
43. Ganti isi kotak search dengan `Budi Kurniawan`, tekan Enter
44. Klik teks Name `Budi Kurniawan` untuk membuka Detail
45. Verifikasi header dan General Information Detail tidak menampilkan Access Level maupun badge akses lain milik Login User
46. Verifikasi tidak ada tab Role

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 4, 26, 34, 38, 42.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 1, 27, 35, 43.
- Urutan: TC-248 lebih dulu karena Langkah Uji-nya (`⋯` > Detail, lalu klik Name) membawa spec ke Detail `Budi Kurniawan` yang sama dengan TC-247, TC-252, dan TC-250; screening TC-247 memakai halaman yang dibuka langkah 6. TC-250 diletakkan terakhir di antara TC Budi karena klik link meninggalkan Detail. TC-451 dan TC-249 memakai Detail `Siti Rahayu` yang sama.
- Tooltip `Ahmad Fauzi` pada TC-247 b.i dan TC-250 a diasersi di TC-250 (hover) dan TC-247 hanya mengasersi keberadaan tooltip sebagai bagian elemen Represented By.
- Temuan untuk QA:
  - TC-252 Expected b menyebut "nilai Custom Field Budi Kurniawan" tanpa menyebut field dan nilainya; spec memverifikasi bahwa nilai Custom Field tampil.
  - TC-251 menyebut `[tanggal Temporary Until sesuai format General Settings]` tanpa nilai tanggal; spec membandingkan dengan Temporary Until record (dibaca lewat fixture).
  - TC-247 Expected b.i memuat tooltip `Ahmad Fauzi` pada Represented By; tooltip diasersi sekali di TC-250.
- Alasan di atas 35 langkah: semua blok satu kelas fungsional baca-saja pada halaman Detail Non-Login User, tidak mengubah data, dan berdiri sendiri: kegagalan satu blok tidak membuat blok lain kehilangan makna.
