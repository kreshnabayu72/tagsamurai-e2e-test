---
id: TC-AC-SU-E2E-009-guided-tooltip-user-list-step-next-back-dan-skip
title: "Guided Tooltip User List: Step 1, Step 2 sampai 4 dan Done, Back, serta Skip via Tombol"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-29
  - TC-AC-SU-30
  - TC-AC-SU-31
  - TC-AC-SU-32
coverage:
  web: automated
---

# Guided Tooltip User List: Step 1, Step 2 sampai 4 dan Done, Back, serta Skip via Tombol

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Pengecualian atas hook suite: spec ini menguji Guided Tooltip sehingga mengatur flag `guided_tooltip_seen_ac-settings-user` sendiri sesudah hook (flag disetel belum `seen` sebelum tiap blok TC dan dipulihkan oleh hook `after` suite).
- Kemampuan teknis: Fixture BE untuk membaca dan menyetel flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` pada akun aktor; disediakan tim FE/BE (lihat `suite.md`).
- Tidak ada data dinamis yang dibuat spec.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-29: Guided Tooltip muncul otomatis di kunjungan pertama, Step 1

1. Setel flag Guided Tooltip belum `seen` untuk akun aktor lewat Fixture BE
2. Muat ulang halaman Settings > User dengan F5
3. Verifikasi walkthrough otomatis tampil di Step 1 dengan target Group Sidebar (right)
4. Verifikasi Title `Group Sidebar`
5. Verifikasi Description `Use the sidebar to filter users by group. Click a group node to see only users within that group and its children.`
6. Verifikasi tombol `[Back]` hidden
7. Verifikasi tombol `[Next]` dan `[Skip]` tampil
8. Klik `[Skip]` untuk menutup walkthrough

### TC-AC-SU-30: Guided Tooltip Step 2-4 dan Done

9. Setel flag Guided Tooltip belum `seen` untuk akun aktor lewat Fixture BE
10. Muat ulang halaman Settings > User dengan F5
11. Klik `[Next]`
12. Verifikasi Step 2 (Toolbar, Search & Filter Bar): Title `Search & Filters`
13. Verifikasi Step 2: Description `Use the search bar and filters to quickly narrow down the user list.`
14. Klik `[Next]`
15. Verifikasi Step 3 (kolom Active): Title `Portal Access Switch`
16. Verifikasi Step 3: Description `Toggle a user's access to the portal. Some rows may be locked and cannot be toggled — hover for details.`
17. Klik `[Next]`
18. Verifikasi Step 4 (kolom Role): Title `Role Summary`
19. Verifikasi Step 4: Description `Shows how many active roles each user has. Click the role count to view the breakdown.`
20. Verifikasi tombol `[Next]` berubah menjadi `[Done]` pada Step 4
21. Klik `[Done]`
22. Verifikasi walkthrough tertutup
23. Muat ulang halaman dengan F5
24. Verifikasi halaman Settings > User tampil dengan tabel User List
25. Verifikasi walkthrough tidak muncul otomatis setelah muat ulang

### TC-AC-SU-31: Guided Tooltip tombol Back

26. Setel flag Guided Tooltip belum `seen` untuk akun aktor lewat Fixture BE
27. Muat ulang halaman Settings > User dengan F5
28. Verifikasi tombol `[Back]` hidden di Step 1
29. Klik `[Next]` dua kali sampai Step 3
30. Klik `[Back]`
31. Verifikasi kembali ke Step 2 dengan Title `Search & Filters`
32. Klik `[Skip]` untuk menutup walkthrough

### TC-AC-SU-32: Guided Tooltip Skip via tombol

33. Setel flag Guided Tooltip belum `seen` untuk akun aktor lewat Fixture BE
34. Muat ulang halaman Settings > User dengan F5
35. Klik `[Skip]`
36. Verifikasi walkthrough tertutup
37. Muat ulang halaman dengan F5
38. Verifikasi halaman Settings > User tampil dengan tabel User List
39. Verifikasi walkthrough tidak muncul otomatis setelah muat ulang

## Notes

- Langkah penghubung (S-03): langkah 1 (precondition flag belum `seen` yang diulang di awal tiap blok TC), langkah 8 dan 32 (tutup walkthrough sebelum TC berikutnya, S-09).
- Urutan langkah TC-AC-SU-31 mengikuti state (bagian 8b butir 5): `[Back]` hidden di Step 1 diasersi sebelum `[Next]` pertama, walau Expected b TC ditulis sesudah Expected a.
- Ukuran spec (39 langkah, di atas smell sekitar 35 langkah): satu halaman, satu komponen (Guided Tooltip), dan tiap blok TC dimulai dengan flag yang disetel ulang sehingga berdiri sendiri; tiap Title dan Description menjadi `Verifikasi` sendiri (S-01).
- Temuan untuk QA:
  - TC-AC-SU-30 dan TC-AC-SU-32 mencatat Post Condition "Flag seen = true" tanpa langkah observasi; tidak diasersi (S-01). Perilaku tidak muncul otomatis setelah muat ulang diasersi dari Expected.
  - Mekanisme membaca dan menyetel flag Guided Tooltip tidak dijelaskan TC; disediakan tim FE/BE.
