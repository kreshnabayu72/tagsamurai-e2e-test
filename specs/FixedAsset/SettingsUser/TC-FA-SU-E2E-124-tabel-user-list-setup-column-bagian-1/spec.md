---
id: TC-FA-SU-E2E-124-tabel-user-list-setup-column-bagian-1
title: "Tabel User List: Setup Column (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-352
  - TC-FA-SU-353
coverage:
  web: automated
---

# Tabel User List: Setup Column (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Kolom kelas Hideable dibagi dua kelompok agar paling sedikit satu kolom tetap visible saat kolom lain disembunyikan (TC tidak menyebut kelompok). Arah dan urutan geser TC-FA-SU-353 tidak disebut TC; spec menggeser kolom satu per satu secara kumulatif (tanpa reset di antara seretan) dari urutan awal `Active, Name, Email, Role, Home Group, Position, Division, Employee ID, Modified By, Last Updated`, sehingga tiap seretan punya baseline (urutan sebelumnya) dan tabel `Kolom Hideable Geser` memuat urutan Live Preview sesudah tiap seretan serta posisi akhir tiap kolom (1 sampai 10).
- Tabel `Kolom Hideable Kelompok 1`:

| Kolom |
|---|
| Active |
| Name |
| Email |
| Role |
| Home Group |

- Tabel `Kolom Hideable Kelompok 2`:

| Kolom |
|---|
| Position |
| Division |
| Employee ID |
| Modified By |
| Last Updated |

- Tabel `Kolom Hideable Geser`:

| Kolom | Arah | Urutan Live Preview | Posisi akhir |
|---|---|---|---|
| Name | kiri | Name, Active, Email, Role, Home Group, Position, Division, Employee ID, Modified By, Last Updated | 1 |
| Email | kiri | Name, Email, Active, Role, Home Group, Position, Division, Employee ID, Modified By, Last Updated | 2 |
| Role | kiri | Name, Email, Role, Active, Home Group, Position, Division, Employee ID, Modified By, Last Updated | 3 |
| Home Group | kiri | Name, Email, Role, Home Group, Active, Position, Division, Employee ID, Modified By, Last Updated | 4 |
| Position | kiri | Name, Email, Role, Home Group, Position, Active, Division, Employee ID, Modified By, Last Updated | 5 |
| Division | kiri | Name, Email, Role, Home Group, Position, Division, Active, Employee ID, Modified By, Last Updated | 6 |
| Employee ID | kiri | Name, Email, Role, Home Group, Position, Division, Employee ID, Active, Modified By, Last Updated | 7 |
| Modified By | kiri | Name, Email, Role, Home Group, Position, Division, Employee ID, Modified By, Active, Last Updated | 9 |
| Active | kanan | Name, Email, Role, Home Group, Position, Division, Employee ID, Modified By, Last Updated, Active | 10 |
| Last Updated | kiri | Name, Email, Role, Home Group, Position, Division, Employee ID, Last Updated, Modified By, Active | 8 |

- Preferensi kolom User List (Setup Column) dihapus di browser pada hook `before` dan `after` spec ini (kemampuan disediakan tim FE, bagian 4 konvensi), bukan lewat `[Reset to Default]`.

## Test Steps

### TC-FA-SU-352: Ceklis dan unceklis kelas Hideable

1. Klik header kolom Actions (⋯), klik `Setup Column...`
2. Untuk setiap baris tabel `Kolom Hideable Kelompok 1` di Prerequisites (langkah 3 sampai 4):
3. Hapus centang `<Kolom>`
4. Verifikasi perubahan kolom `<Kolom>` tampil di Live Preview
5. Klik `[Save]`
6. Untuk setiap baris tabel `Kolom Hideable Kelompok 1` di Prerequisites (langkah 7):
7. Verifikasi perubahan kolom `<Kolom>` tampil di tabel
8. Tekan F5
9. Untuk setiap baris tabel `Kolom Hideable Kelompok 1` di Prerequisites (langkah 10):
10. Verifikasi perubahan kolom `<Kolom>` bertahan setelah refresh
11. Klik header kolom Actions (⋯), klik `Setup Column...`
12. Centang kembali `Active`, `Name`, `Email`, `Role`, dan `Home Group`
13. Untuk setiap baris tabel `Kolom Hideable Kelompok 2` di Prerequisites (langkah 14 sampai 15):
14. Hapus centang `<Kolom>`
15. Verifikasi perubahan kolom `<Kolom>` tampil di Live Preview
16. Klik `[Save]`
17. Untuk setiap baris tabel `Kolom Hideable Kelompok 2` di Prerequisites (langkah 18):
18. Verifikasi perubahan kolom `<Kolom>` tampil di tabel
19. Tekan F5
20. Untuk setiap baris tabel `Kolom Hideable Kelompok 2` di Prerequisites (langkah 21):
21. Verifikasi perubahan kolom `<Kolom>` bertahan setelah refresh
22. Klik header kolom Actions (⋯), klik `Setup Column...`
23. Hapus centang `Name`, `Email`, `Role`, dan `Home Group` hingga `Active` menjadi satu-satunya kolom visible
24. Hover checkbox `Active`
25. Verifikasi checkbox `Active` disabled dengan tooltip `At least one column must remain visible.`
26. Klik `[✕]` pada Setup Column

### TC-FA-SU-353: Geser (drag reorder) kelas Hideable

27. Klik header kolom Actions (⋯), klik `Setup Column...`
28. Centang kembali `Position`, `Division`, `Employee ID`, `Modified By`, dan `Last Updated`, klik `[Save]`
29. Klik header kolom Actions (⋯), klik `Setup Column...`
30. Untuk setiap baris tabel `Kolom Hideable Geser` di Prerequisites (langkah 31 sampai 32):
31. Seret kolom `<Kolom>` satu posisi ke <Arah>
32. Verifikasi urutan kolom pada Live Preview menjadi `<Urutan Live Preview>`
33. Klik `[Save]`
34. Untuk setiap baris tabel `Kolom Hideable Geser` di Prerequisites (langkah 35):
35. Verifikasi kolom `<Kolom>` pada tabel berada di posisi `<Posisi akhir>`
36. Tekan F5
37. Untuk setiap baris tabel `Kolom Hideable Geser` di Prerequisites (langkah 38):
38. Verifikasi kolom `<Kolom>` bertahan di posisi `<Posisi akhir>` setelah F5

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 1, 11, 22, 27, 29 (membuka Setup Column), 12 dan 28 (mengembalikan kolom yang disembunyikan), dan 26 (menutup Setup Column tanpa menyimpan).
- Langkah yang diulang: langkah 3 sampai 4, langkah 7, langkah 10, langkah 14 sampai 15, langkah 18, langkah 21 (kelompok Hideable), serta langkah 31 sampai 32, langkah 35, langkah 38 (geser sepuluh kolom), dengan parameter pada tabel Prerequisites.
- Temuan untuk QA (S-15): (1) TC-FA-SU-352 meminta "ubah centang" pada kesepuluh kolom Hideable sekaligus, padahal kolom yang tersisa sebagai satu-satunya yang visible tidak dapat di-uncheck (Expected k); spec membagi kolom ke dua kelompok yang disembunyikan bergantian. (2) TC-FA-SU-353 tidak menyebut arah geser; arah dan urutan kumulatif (urutan Live Preview sesudah tiap seretan serta posisi akhir) ditetapkan spec pada tabel Prerequisites agar tiap seretan punya baseline dan seretan tidak saling membatalkan.
- Alasan di atas sekitar 35 langkah (ekspansi perulangan dihitung): seluruh blok berkelas fungsional yang sama pada halaman, akun, dan dataset Pre-setup #20 yang sama tanpa mengubah data; langkah berulang per kolom atau field berpola identik (langkah 3 sampai 4, langkah 14 sampai 15, langkah 31 sampai 32) dan kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna; bagian 3 konvensi menetapkan Setup Column, Bulk Action Bar, dan Search, Filter, Sort tetap satu spec selama dataset dan harness sama, sedangkan pemecahan hanya menambah login, hook, dan pembukaan halaman. Dua TC pada satu surface dengan pola identik, sehingga tidak ada nomor lain untuk memecah tanpa menggandakan dua pembukaan dan satu pemulihan preferensi.
