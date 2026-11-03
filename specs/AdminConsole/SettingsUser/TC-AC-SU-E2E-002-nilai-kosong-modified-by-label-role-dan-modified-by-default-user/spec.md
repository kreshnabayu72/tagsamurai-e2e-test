---
id: TC-AC-SU-E2E-002-nilai-kosong-modified-by-label-role-dan-modified-by-default-user
title: "User List: Nilai Kosong Kolom, Format Modified By, Label Kolom Role, dan Modified By Default User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-5
  - TC-AC-SU-6
  - TC-AC-SU-8
  - TC-AC-SU-664
coverage:
  web: automated
---

# User List: Nilai Kosong Kolom, Format Modified By, Label Kolom Role, dan Modified By Default User

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-5, 8 | `Sarah Lee` | `Sarah Lee {runId}-002` | `sarahlee+{runId}-002@qwertysystem.net` | tanpa Position; 0 role aktif |
| TC-AC-SU-5 | `Rudi Hartono` | `Rudi Hartono {runId}-002` | `rudihartono+{runId}-002@qwertysystem.net` | tanpa Employee ID |
| TC-AC-SU-6 | `John Doe` | `John Doe {runId}-002` | `johndoe+{runId}-002@qwertysystem.net` | Modified By terakhir = `Dewi Lestari {runId}-002` |
| TC-AC-SU-6, 8 | `Dewi Lestari` | `Dewi Lestari {runId}-002` | `dewilestari+{runId}-002@qwertysystem.net` | Total Control |
| TC-AC-SU-8 | `Mike Tan` | `Mike Tan {runId}-002` | `miketan+{runId}-002@qwertysystem.net` | 1 role aktif |
| TC-AC-SU-8 | `Jane Smith` | `Jane Smith {runId}-002` | `janesmith+{runId}-002@qwertysystem.net` | 2 role aktif |
| TC-AC-SU-8 | `Andi Wijaya` | `Andi Wijaya {runId}-002` | `andiwijaya+{runId}-002@qwertysystem.net` | Read Only |

- Seluruh user seed memiliki Email dan Division terisi (TC-AC-SU-5). Baris Default User entitas (Pre-setup #1) dicari lewat Search atas emailnya dan tidak diubah.
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-5: Nilai kosong kolom Position dan Employee ID tampil strip; Email dan Division selalu terisi

1. Ketik Search `{runId}-002`, tekan Enter
2. Amati baris `Sarah Lee {runId}-002` dan `Rudi Hartono {runId}-002`
3. Verifikasi `Sarah Lee {runId}-002`: Position `—`
4. Verifikasi `Rudi Hartono {runId}-002`: Employee ID `—`
5. Verifikasi kolom Email terisi di setiap baris hasil Search (tidak ada `—`)
6. Verifikasi kolom Division terisi di setiap baris hasil Search (tidak ada `—`)

### TC-AC-SU-6: Format kolom Modified By dan hover nama lengkap

7. Amati kolom Modified By baris `John Doe {runId}-002`
8. Verifikasi Modified By tampil `Dewi L`
9. Hover nilai Modified By tersebut
10. Verifikasi tooltip `Dewi Lestari {runId}-002`

### TC-AC-SU-8: Label kolom Role per kondisi jumlah role dan tier

11. Amati kolom Role pada baris `Sarah Lee {runId}-002`, `Mike Tan {runId}-002`, `Jane Smith {runId}-002`, `Dewi Lestari {runId}-002`, dan `Andi Wijaya {runId}-002`
12. Verifikasi `Sarah Lee {runId}-002`: teks `0 roles`
13. Verifikasi `Sarah Lee {runId}-002`: `0 roles` berupa teks biasa (bukan link)
14. Klik `0 roles` pada `Sarah Lee {runId}-002`
15. Verifikasi klik `0 roles` tidak membuka popup
16. Verifikasi `Mike Tan {runId}-002`: label `1 role`
17. Verifikasi `Mike Tan {runId}-002`: `1 role` clickable
18. Verifikasi `Jane Smith {runId}-002`: label `2 roles`
19. Verifikasi `Jane Smith {runId}-002`: `2 roles` clickable
20. Verifikasi `Dewi Lestari {runId}-002`: badge `Total Control` menggantikan label jumlah
21. Verifikasi `Andi Wijaya {runId}-002`: badge `Read Only` menggantikan label jumlah
22. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SU-664: Modified By Default User seed tampil `System`

23. Ketik Search `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, tekan Enter
24. Amati kolom Modified By baris Default User
25. Verifikasi Modified By baris Default User = `System`
26. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search atas suffix spec, R-16), langkah 22 dan 26 (reset Search), langkah 23 (Search untuk menemukan baris Default User lewat email Pre-setup #1, R-16).
- Temuan untuk QA:
  - TC-AC-SU-6: cara membuat `John Doe` "terakhir dimodifikasi oleh Dewi Lestari" tidak dijelaskan TC; spec memakai Fixture BE (disediakan tim FE/BE) dan user seed bersuffix. Format Modified By diasersi `[First Name] [Last Initial]` (R-14), sehingga suffix dianggap bagian nama belakang.
  - TC-AC-SU-664: TC menyatakan Default User seed dibuat otomatis tanpa aktor; spec mengasumsikan baris Default User yang dicari lewat email Pre-setup #1 adalah baris seed itu (TC tidak menyebut emailnya).
  - TC-AC-SU-5: Position dan Division adalah nilai master data; TC tidak menyebut nilai yang dipakai seed. Nilai disediakan tim FE/BE.
  - Nama user TC (`Sarah Lee`, `Rudi Hartono`, `John Doe`, `Dewi Lestari`, `Mike Tan`, `Jane Smith`, `Andi Wijaya`) dipakai sebagai nama bersuffix `{runId}-002` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
