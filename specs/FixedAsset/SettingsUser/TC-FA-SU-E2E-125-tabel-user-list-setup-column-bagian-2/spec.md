---
id: TC-FA-SU-E2E-125-tabel-user-list-setup-column-bagian-2
title: "Tabel User List: Setup Column (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-354
  - TC-FA-SU-355
coverage:
  web: automated
---

# Tabel User List: Setup Column (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Kemampuan teknis: viewport browser dipersempit agar tabel dapat di-scroll horizontal (disediakan tim FE).
- Pin dilakukan berpasangan per putaran karena maksimum tiga kolom dapat di-pin sekaligus (TC-FA-SU-354 tidak menyebut pengelompokan). Pin dilepas pada akhir tiap putaran.
- Tabel `Pasangan Kolom Pin`:

| Kolom A | Kolom B |
|---|---|
| Active | Name |
| Email | Role |
| Home Group | Position |
| Division | Employee ID |
| Modified By | Last Updated |

- Tabel `Kolom Curated`:

| Kolom |
|---|
| Activation Status |
| Temporary User |
| Temporary Until |
| TAG |
| Shift |

- Preferensi kolom User List (Setup Column) dihapus di browser pada hook `before` dan `after` spec ini (kemampuan disediakan tim FE, bagian 4 konvensi), bukan lewat `[Reset to Default]`.

## Test Steps

### TC-FA-SU-354: Pin dan unpin kelas Hideable

1. Untuk setiap baris tabel `Pasangan Kolom Pin` di Prerequisites (langkah 2 sampai 14):
2. Klik header kolom Actions (⋯), klik `Setup Column...`
3. Klik icon Pin pada kolom `<Kolom A>` dan `<Kolom B>`
4. Klik `[Save]`
5. Scroll tabel secara horizontal
6. Verifikasi kolom `<Kolom A>` membeku di kiri saat tabel di-scroll horizontal
7. Verifikasi kolom `<Kolom B>` membeku di kiri saat tabel di-scroll horizontal
8. Tekan F5, scroll tabel secara horizontal
9. Verifikasi kolom `<Kolom A>` tetap membeku setelah F5
10. Verifikasi kolom `<Kolom B>` tetap membeku setelah F5
11. Klik header kolom Actions (⋯), klik `Setup Column...`
12. Unpin kolom `<Kolom A>` dan `<Kolom B>`, klik `[Save]`
13. Verifikasi kolom `<Kolom A>` terlepas dan ikut ter-scroll
14. Verifikasi kolom `<Kolom B>` terlepas dan ikut ter-scroll
15. Klik header kolom Actions (⋯), klik `Setup Column...`
16. Klik icon Pin pada kolom `Active`, `Name`, dan `Email`
17. Hover icon Pin kolom `Role`
18. Verifikasi icon Pin kolom `Role` disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
19. Klik `[✕]` pada Setup Column

### TC-FA-SU-355: Ceklis dan unceklis kelas Curated

20. Klik header kolom Actions (⋯), klik `Setup Column...`
21. Untuk setiap baris tabel `Kolom Curated` di Prerequisites (langkah 22 sampai 23):
22. Centang `<Kolom>`
23. Verifikasi perubahan kolom `<Kolom>` tampil di Live Preview
24. Klik `[Save]`
25. Untuk setiap baris tabel `Kolom Curated` di Prerequisites (langkah 26):
26. Verifikasi perubahan kolom `<Kolom>` tampil di tabel
27. Tekan F5
28. Untuk setiap baris tabel `Kolom Curated` di Prerequisites (langkah 29):
29. Verifikasi perubahan kolom `<Kolom>` bertahan setelah refresh
30. Klik header kolom Actions (⋯), klik `Setup Column...`
31. Hapus centang seluruh kolom selain `Shift` hingga `Shift` menjadi satu-satunya kolom visible
32. Hover checkbox `Shift`
33. Verifikasi checkbox `Shift` disabled dengan tooltip `At least one column must remain visible.`
34. Klik `[✕]` pada Setup Column

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 15, 20, 30 (membuka Setup Column) dan 19, 34 (menutup Setup Column tanpa menyimpan).
- Langkah yang diulang: langkah 2 sampai 14 (lima pasangan kolom), langkah 22 sampai 23, langkah 26, langkah 29 (lima kolom Curated), dengan parameter pada tabel Prerequisites.
- Temuan untuk QA (S-15): (1) TC-FA-SU-354 meminta pin pada kesepuluh kolom, padahal Expected k membatasi tiga kolom; spec mem-pin berpasangan dan melepasnya. Cara pembuktian "membeku di kiri" (posisi kolom saat scroll horizontal) tidak dirinci TC.
- Alasan di atas sekitar 35 langkah (ekspansi perulangan dihitung): seluruh blok berkelas fungsional yang sama pada halaman, akun, dan dataset Pre-setup #20 yang sama tanpa mengubah data; langkah berulang per kolom atau field berpola identik (langkah 2 sampai 14, langkah 22 sampai 23) dan kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna; bagian 3 konvensi menetapkan Setup Column, Bulk Action Bar, dan Search, Filter, Sort tetap satu spec selama dataset dan harness sama, sedangkan pemecahan hanya menambah login, hook, dan pembukaan halaman. Dua TC pada satu surface dengan pola identik; kegagalan satu putaran pin tidak membuat putaran lain kehilangan makna.
