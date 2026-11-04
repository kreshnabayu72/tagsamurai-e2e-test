---
id: TC-AC-SU-E2E-012-screening-detail-user-user-type-temporary-until-dan-tag
title: "Detail User: Badge User Type per Kondisi Role, Field Temporary Until, dan Field TAG"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-42
  - TC-AC-SU-43
  - TC-AC-SU-44
  - TC-AC-SU-45
coverage:
  web: automated
---

# Detail User: Badge User Type per Kondisi Role, Field Temporary Until, dan Field TAG

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- General Settings Date Format `DD/MM/YY` (state environment yang diasumsikan TC-AC-SU-44; tidak diubah oleh spec ini).
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-42 | `Dewi Lestari` | `Dewi Lestari {runId}-012` | `dewilestari+{runId}-012@qwertysystem.net` | Total Control |
| TC-AC-SU-42 | `Andi Wijaya` | `Andi Wijaya {runId}-012` | `andiwijaya+{runId}-012@qwertysystem.net` | Read Only |
| TC-AC-SU-42 | `Dedi Kurnia` | `Dedi Kurnia {runId}-012` | `dedikurnia+{runId}-012@qwertysystem.net` | Group Manager `Region A` saja (bukan pemegang Global Role) |
| TC-AC-SU-42, 45 | `Jane Smith` | `Jane Smith {runId}-012` | `janesmith+{runId}-012@qwertysystem.net` | ≥1 role aktif bukan tier; TAG `E2003412` |
| TC-AC-SU-42 | `Sarah Lee` | `Sarah Lee {runId}-012` | `sarahlee+{runId}-012@qwertysystem.net` | 0 role aktif |
| TC-AC-SU-43 | `Dedi Kurnia` | `Dedi Kurnia T43 {runId}-012` | `dedikurnia+{runId}-012-T43@qwertysystem.net` | Group Manager `Region A` sekaligus Global Role aktif `Manage group` |
| TC-AC-SU-43 | `Sarah Lee` | `Sarah Lee T43 {runId}-012` | `sarahlee+{runId}-012-T43@qwertysystem.net` | hanya Global Role dengan switch OFF dan Group Role tanpa group |
| TC-AC-SU-44 | `Andi Wijaya` | `Andi Wijaya T44 {runId}-012` | `andiwijaya+{runId}-012-T44@qwertysystem.net` | Temporary User sampai 30 Jun 2026 |
| TC-AC-SU-44, 45 | `John Doe` | `John Doe {runId}-012` | `johndoe+{runId}-012@qwertysystem.net` | bukan Temporary User; tanpa TAG |

- Group `Region A` yang dirujuk Group Manager adalah group milik spec bersuffix `{runId}-012`.
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-42: Badge User Type per kondisi role

1. Ketik Search `Dewi Lestari {runId}-012`, tekan Enter
2. Klik Name `Dewi Lestari {runId}-012`
3. Verifikasi field User Type `Dewi Lestari {runId}-012`: `Total Control`
4. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
5. Ganti isi kotak search dengan `Andi Wijaya {runId}-012`, tekan Enter
6. Klik Name `Andi Wijaya {runId}-012`
7. Verifikasi field User Type `Andi Wijaya {runId}-012`: `Read Only`
8. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
9. Ganti isi kotak search dengan `Dedi Kurnia {runId}-012`, tekan Enter
10. Klik Name `Dedi Kurnia {runId}-012`
11. Verifikasi field User Type `Dedi Kurnia {runId}-012`: `Group Manager`
12. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
13. Ganti isi kotak search dengan `Jane Smith {runId}-012`, tekan Enter
14. Klik Name `Jane Smith {runId}-012`
15. Verifikasi field User Type `Jane Smith {runId}-012`: `Admin`

### TC-AC-SU-45: Field TAG tampil strip bila belum paired (butir Jane Smith)

16. Verifikasi field TAG `Jane Smith {runId}-012`: `E2003412`
17. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User

### TC-AC-SU-42: Badge User Type (lanjutan)

18. Ganti isi kotak search dengan `Sarah Lee {runId}-012`, tekan Enter
19. Klik Name `Sarah Lee {runId}-012`
20. Verifikasi field User Type `Sarah Lee {runId}-012`: `Basic`
21. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User

### TC-AC-SU-43: User Type prioritas overlap dan role nonaktif tidak dihitung

22. Ganti isi kotak search dengan `Dedi Kurnia T43 {runId}-012`, tekan Enter
23. Klik Name `Dedi Kurnia T43 {runId}-012`
24. Verifikasi field User Type `Dedi Kurnia T43 {runId}-012`: `Group Manager`
25. Verifikasi field User Type `Dedi Kurnia T43 {runId}-012` bukan `Admin`
26. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
27. Ganti isi kotak search dengan `Sarah Lee T43 {runId}-012`, tekan Enter
28. Klik Name `Sarah Lee T43 {runId}-012`
29. Verifikasi field User Type `Sarah Lee T43 {runId}-012`: `Basic`
30. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User

### TC-AC-SU-44: Field Temporary Until untuk Temporary User

31. Ganti isi kotak search dengan `Andi Wijaya T44 {runId}-012`, tekan Enter
32. Klik Name `Andi Wijaya T44 {runId}-012`
33. Verifikasi field Temporary Until `Andi Wijaya T44 {runId}-012`: `Temporary until 30/06/26` (format mengikuti General Settings)
34. Verifikasi field Temporary Until `Andi Wijaya T44 {runId}-012` read-only
35. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
36. Ganti isi kotak search dengan `John Doe {runId}-012`, tekan Enter
37. Klik Name `John Doe {runId}-012`
38. Verifikasi field Temporary Until `John Doe {runId}-012` hidden

### TC-AC-SU-45: Field TAG tampil strip bila belum paired (butir John Doe)

39. Verifikasi field TAG `John Doe {runId}-012`: `—`
40. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User
41. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16; berlaku juga untuk semua Search sesudahnya), langkah 4, 40, dan langkah kembali ke daftar lain, langkah 41 (reset Search). Layar awal dibuka hook `beforeEach` suite.
- Perubahan urutan TC (S-05): TC-AC-SU-45 diletakkan pada kunjungan Detail `Jane Smith` dan `John Doe` yang sama dengan TC-AC-SU-42 dan TC-AC-SU-44 agar tidak membuka Detail yang sama dua kali; sebab itu urutannya 42, 45, 42, 43, 44, 45. Subjudul pada tiap blok memetakan langkah ke id TC.
- Ukuran spec (41 langkah, di atas smell sekitar 35 langkah): sembilan kunjungan Detail dengan pola identik (cari, buka, `Verifikasi`, kembali) pada satu halaman dan satu dataset; tiap kunjungan berdiri sendiri dan data TC-AC-SU-43 dan TC-AC-SU-44 memakai seed terpisah (penanda `T43`, `T44` pada nama, ditaruh sebelum `{runId}-012` agar nama seed tidak saling mengandung), sehingga kegagalan satu kunjungan tidak membuat kunjungan lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-SU-44: tanggal Temporary Until `30 Jun 2026` sudah lewat terhadap tanggal run; TC tidak menyebut perilaku BE untuk tanggal lampau. Seed memakai tanggal TC; bila BE menolaknya, QA menentukan tanggal lain beserta teks hasil format `Temporary until`.
  - TC-AC-SU-44 precondition b menyebut General Settings Date Format `DD/MM/YY` sebagai kondisi lingkungan; spec tidak menyetelnya.
  - TC-AC-SU-45: nilai TAG `E2003412` dipakai literal sesuai TC; bila bentrok dengan TAG Pre-setup, QA/FE menentukan TAG seed lain.
  - TC-AC-SU-42 dan TC-AC-SU-43 memakai nama user yang sama (`Dedi Kurnia`, `Sarah Lee`) untuk kondisi berbeda; spec membuat dua record terpisah (penanda `T43` pada nama).
  - Nama user TC (`Dewi Lestari`, `Andi Wijaya`, `Dedi Kurnia`, `Jane Smith`, `Sarah Lee`, `John Doe`) dipakai sebagai nama bersuffix `{runId}-012` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
