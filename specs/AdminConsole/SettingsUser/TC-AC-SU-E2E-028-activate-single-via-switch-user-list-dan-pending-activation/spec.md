---
id: TC-AC-SU-E2E-028-activate-single-via-switch-user-list-dan-pending-activation
title: "Activate Single via Switch User List: Dialog, Cancel, Confirm, Aktivasi Ulang, dan Switch Pending Activation"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-87
  - TC-AC-SU-88
  - TC-AC-SU-89
  - TC-AC-SU-96
  - TC-AC-SU-97
coverage:
  web: automated
---

# Activate Single via Switch User List: Dialog, Cancel, Confirm, Aktivasi Ulang, dan Switch Pending Activation

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-96 | `Region A` | `Region A {runId}-028` | - | Group |
| TC-AC-SU-96 | `Branch 1` | `Branch 1 {runId}-028` | - | Group |
| TC-AC-SU-87, 88, 89 | `Jane Smith` | `Jane Smith {runId}-028` | `janesmith+{runId}-028@qwertysystem.net` | Inactive, sudah aktivasi, 2 role aktif tersimpan |
| TC-AC-SU-96 | `Jane Smith` | `Jane Smith {runId}-028-T96` | `janesmith+{runId}-028-T96@qwertysystem.net` | Inactive, sudah aktivasi, 2 Group Role tersimpan: `Manage allocation` di `Region A {runId}-028`, `Manage partner` di `Branch 1 {runId}-028` |
| TC-AC-SU-97 | `Mike Tan` | `Mike Tan {runId}-028` | `miketan+{runId}-028@qwertysystem.net` | Pending Activation, Active |
| TC-AC-SU-97 | `Sarah Lee` | `Sarah Lee {runId}-028` | `sarahlee+{runId}-028@qwertysystem.net` | Pending Activation, Inactive |

- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-87: Screening dialog Activate User dari switch Active di User List

1. Ketik Search `{runId}-028`, tekan Enter
2. Klik switch Active baris `Jane Smith {runId}-028`
3. Verifikasi dialog muncul: Title `Activate User` dengan icon `[×]`; Body bullet `Jane Smith {runId}-028`, `This user will regain access to the portal.`, `Are you sure you want to activate it?`; tombol `[Cancel]` (Text, Contrast) dan `[Activate]` (filled, primary)
4. Verifikasi dialog `severity="info"`
5. Klik `[Cancel]` pada dialog

### TC-AC-SU-89: Activate user via switch, Cancel

6. Klik switch Active baris `Jane Smith {runId}-028`
7. Klik `[Cancel]` pada dialog Activate User
8. Verifikasi dialog tertutup
9. Verifikasi switch kembali OFF
10. Verifikasi tidak ada toast

### TC-AC-SU-97: Switch Active tetap Enabled untuk user Pending Activation (blok Cancel)

11. Klik switch Active baris `Mike Tan {runId}-028`
12. Verifikasi switch `Mike Tan {runId}-028` enabled
13. Verifikasi switch `Mike Tan {runId}-028` membuka dialog Deactivate User
14. Klik `[Cancel]` pada dialog Deactivate User

### TC-AC-SU-88: Activate user via switch User List, Confirm

15. Klik switch Active baris `Jane Smith {runId}-028`
16. Klik `[Activate]` pada dialog Activate User
17. Verifikasi dialog tertutup
18. Verifikasi toast sukses: "Success, user has been activated."
19. Verifikasi switch baris `Jane Smith {runId}-028` ON
20. Verifikasi kolom Role baris `Jane Smith {runId}-028` tetap `2 roles`
21. Muat ulang halaman dengan F5
22. Ketik Search `Jane Smith {runId}-028`, tekan Enter
23. Verifikasi status `Jane Smith {runId}-028` Active (switch ON) tetap setelah refresh

### TC-AC-SU-96: Activate ulang user yang pernah di-deactivate, role dan group assignment berlaku lagi

24. Ganti isi kotak search dengan `Jane Smith {runId}-028-T96`, tekan Enter
25. Klik switch Active baris `Jane Smith {runId}-028-T96`
26. Klik `[Activate]` pada dialog Activate User
27. Verifikasi toast sukses: "Success, user has been activated."
28. Klik Name `Jane Smith {runId}-028-T96`
29. Klik Tab Role
30. Klik sub-tab Group Role
31. Verifikasi 2 Group Role tampil aktif dengan group yang sama seperti sebelum deactivate: `Manage allocation` di `Region A {runId}-028` dan `Manage partner` di `Branch 1 {runId}-028`
32. Klik segmen `User` pada Breadcrumb untuk kembali ke Settings > User

### TC-AC-SU-97: Switch Active tetap Enabled untuk user Pending Activation (blok Confirm)

33. Ganti isi kotak search dengan `Sarah Lee {runId}-028`, tekan Enter
34. Verifikasi switch `Sarah Lee {runId}-028` enabled
35. Klik switch Active baris `Sarah Lee {runId}-028`
36. Klik `[Activate]` pada dialog Activate User
37. Verifikasi toast sukses: "Success, user has been activated."
38. Verifikasi badge `Pending Activation` tetap tampil di samping nama `Sarah Lee {runId}-028`
39. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target, R-16; berlaku juga untuk Search sesudahnya), langkah 5 (tutup dialog sebelum TC berikutnya, S-09), langkah 21 (muat ulang untuk Post Condition TC-AC-SU-88), langkah 32 (kembali ke daftar), langkah 39 (reset Search).
- Urutan TC (S-05 dan S-10): TC-AC-SU-97 dipecah menjadi blok Cancel (sebelum aksi sukses) dan blok Confirm (sesudah), dan seluruh aksi yang mengubah status (88, 96, 97 Confirm) diletakkan sesudah screening dan Cancel (87, 89, 97 Cancel). Subjudul memetakan langkah ke id TC.
- Ukuran spec (39 langkah, di atas smell sekitar 35 langkah): satu dialog (Activate User) pada satu halaman dengan empat user seed terpisah; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-AC-SU-88 Post Condition b ("Role dan group assignment sama seperti sebelum dinonaktifkan") dan c (log) tidak punya langkah observasi di TC dan tidak diasersi (S-01); butir a (persist setelah refresh) diasersi.
  - TC-AC-SU-96 memakai user `Jane Smith` yang sama dengan TC-AC-SU-88 yang sudah menjadi Active setelah TC-AC-SU-88; spec memakai seed terpisah (suffix `-T96`).
  - TC-AC-SU-97 butir b: "Sarah Lee enabled; muncul toast sukses" diasersi sebagai dua `Verifikasi`; Post Condition "Sarah Lee Active + Pending Activation" diasersi lewat badge yang tetap tampil.
  - Nama user TC (`Jane Smith`, `Mike Tan`, `Sarah Lee`, `Region A`, `Branch 1`) dipakai sebagai nama bersuffix `{runId}-028` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
