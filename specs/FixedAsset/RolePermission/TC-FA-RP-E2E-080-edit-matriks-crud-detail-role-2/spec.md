---
id: TC-FA-RP-E2E-080-edit-matriks-crud-detail-role-2
title: "Edit matriks CRUD Detail Role (2/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-269
  - TC-FA-RP-270
  - TC-FA-RP-271
  - TC-FA-RP-272
  - TC-FA-RP-273
coverage:
  web: automated
---

# Edit matriks CRUD Detail Role (2/3)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: pool #15 (Ahmad Fauzi) dan #18. Ahmad Fauzi memegang, dengan hanya Read aktif (disiapkan lewat seed API di hook `before`): Global Role `Manage asset transactional policy` dan `Manage Open API`; Group Role `Manage files`, `Manage user & role`, dan `View asset value` di `Data Center`.
- Kemampuan teknis: pencatat request jaringan untuk membuktikan klik sel `—` tidak mengirim permintaan (disediakan tim FE).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan Global Role dan Group Role Ahmad Fauzi pada keadaan awal pool #15), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-269: Sel `—` pada role berkolom RU (Manage asset transactional policy)

1. Klik Tab `System`, klik Role Name `Manage asset transactional policy` pada section Global Role
2. Klik sel Create dan sel Delete pada baris Ahmad Fauzi
3. Verifikasi sel Create dan Delete berupa teks `—` tanpa elemen interaktif
4. Verifikasi klik tidak mengirim permintaan
5. Verifikasi klik tidak menampilkan toast
6. Centang kolom Update pada baris Ahmad Fauzi
7. Verifikasi kolom Read dan Update berupa checkbox
8. Verifikasi Read tercentang Disabled
9. Verifikasi muncul toast sukses: `Success, permissions have been updated.`

### TC-FA-RP-270: Sel `—` pada role berkolom RD (Manage files)

10. Klik Tab `System`, klik Role Name `Manage files` pada section Group Role
11. Klik node `Data Center` di Sidebar Group Tree
12. Klik sel Create dan sel Update pada baris Ahmad Fauzi
13. Verifikasi sel Create dan Update berupa teks `—` tanpa elemen interaktif
14. Verifikasi klik tidak mengirim permintaan
15. Verifikasi klik tidak menampilkan toast
16. Centang kolom Delete pada baris Ahmad Fauzi
17. Verifikasi kolom Read dan Delete berupa checkbox
18. Verifikasi Read tercentang Disabled
19. Verifikasi muncul toast sukses: `Success, permissions have been updated.`

### TC-FA-RP-271: Sel `—` pada role berkolom RU (Manage user & role Group)

20. Klik Tab `System`, klik Role Name `Manage user & role` pada section Group Role
21. Klik node `Data Center` di Sidebar Group Tree
22. Klik sel Create dan sel Delete pada baris Ahmad Fauzi
23. Verifikasi sel Create dan Delete berupa teks `—` tanpa elemen interaktif
24. Verifikasi klik tidak mengirim permintaan
25. Verifikasi klik tidak menampilkan toast
26. Centang kolom Update pada baris Ahmad Fauzi
27. Verifikasi kolom Read dan Update berupa checkbox
28. Verifikasi Read tercentang Disabled
29. Verifikasi muncul toast sukses: `Success, permissions have been updated.`

### TC-FA-RP-272: Sel `—` pada role berkolom R (View asset value)

30. Klik Tab `System`, klik Role Name `View asset value` pada section Group Role
31. Klik node `Data Center` di Sidebar Group Tree
32. Klik sel Create, sel Update, dan sel Delete pada baris Ahmad Fauzi
33. Verifikasi sel Create, Update, dan Delete berupa teks `—` tanpa elemen interaktif
34. Verifikasi klik tidak mengirim permintaan
35. Verifikasi klik tidak menampilkan toast
36. Verifikasi kolom Read berupa checkbox
37. Verifikasi Read tercentang Disabled

### TC-FA-RP-273: Checkbox Read terkunci

38. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
39. Hover checkbox Read baris Ahmad Fauzi
40. Verifikasi tooltip `Read access is required and can only be removed by removing the role.`
41. Klik checkbox Read baris Ahmad Fauzi
42. Amati checkbox Read dan ada tidaknya toast
43. Verifikasi Read tetap tercentang
44. Verifikasi tidak ada toast
45. Verifikasi tidak ada perubahan data pada baris Ahmad Fauzi (Create, Update, Delete tetap tidak tercentang)

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-269, TC-FA-RP-270, TC-FA-RP-271, TC-FA-RP-272, TC-FA-RP-273).
- Langkah penghubung (S-03): membuka Tab System, Detail Role, dan node `Data Center` pada tiap blok; langkah 42 (mengamati checkbox Read dan ada tidaknya toast pada TC-FA-RP-273) langsung diikuti `Verifikasi`.
- Pola langkah blok TC-FA-RP-269 sampai TC-FA-RP-271 identik dengan parameter role, node, sel `—`, dan kolom yang diubah; ditulis eksplisit karena Detail Role dan sectionnya berbeda.
- Temuan untuk QA:
  - TC-FA-RP-269 dan TC-FA-RP-273 tidak menyebut Ahmad Fauzi memegang role (hanya "Pre-setup #15 tersedia"); spec mengasumsikan penugasan dengan hanya Read aktif. TC-FA-RP-271 memberi precondition seed API sendiri.
  - TC-FA-RP-273 Expected b menyebut "tidak ada perubahan data" tanpa kolom pembanding; spec mengasersi kolom Create, Update, Delete tetap tidak tercentang berdasarkan state awal hanya-Read.
  - TC-FA-RP-273 bertipe UI Only di TC; spec memakai FE+BE karena baris Ahmad Fauzi dan state datanya berasal dari backend nyata.
- Spec ini 45 langkah, di atas smell 35 langkah. Alasan: lima blok satu kelas (fungsional) pada matriks CRUD Detail Role yang sama; tiap blok berdiri sendiri dengan data seed sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
