---
id: TC-FA-GRP-E2E-033-new-group-screening-popup-dan-create-level-1-happy-path-stay-on-form
title: "Popup New Group: Screening, Create Level 1 (Code Manual, Function Assignable), Field Opsional Kosong, dan Stay on This Form"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-79
  - TC-FA-GRP-80
  - TC-FA-GRP-81
  - TC-FA-GRP-83
coverage:
  web: automated
---

# Popup New Group: Screening, Create Level 1 (Code Manual, Function Assignable), Field Opsional Kosong, dan Stay on This Form

## Prerequisites

- Mode: FE+BE (backend nyata; Create Group menulis data dan hasilnya diasersi di tabel, sidebar, dan Detail).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8, jumlah group di bawah cap); pohon group Tabel A, termasuk Branch Office (Code `BO`). Sisa slot sedikitnya 2 (precondition TC-FA-GRP-83).
- Data Dinamis bersuffix `{runId}-033` (kecuali nama literal di bawah); nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas fixture belum ada, dibuat di tahap script):
  - TC-FA-GRP-80: Name `Jakarta Hub {runId}-033`, Code `JKT`, Description `Main hub`, Function Assignable.
  - TC-FA-GRP-81: Name literal `Bandung Office` (tanpa suffix karena Code auto-generate diturunkan dari Name; lihat Temuan untuk QA), tanpa Code; hasil Code `BO2` karena `BO` sudah dipakai Branch Office.
  - TC-FA-GRP-83: Name `Batch One {runId}-033` dan `Batch Two {runId}-033`.
- Kemampuan teknis: pembacaan jumlah user client yang dihitung Total User (Total Control, Default User, Read Only) lewat fixture BE (disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD); jam server dan jam browser sinkron untuk asersi Last Updated (toleransi satu menit).
- Pemulihan (hook `before` dan `after`): hapus lewat API semua group dengan suffix `{runId}-033`, group literal `Bandung Office`, dan group ber-Code literal `JKT` yang dibuat spec ini (hook `before` juga menghapus sisa literal dari run sebelumnya).
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-79: Screening Popup New Group

1. Klik [+] Group di sidebar
2. Verifikasi header popup: title `New Group` dan icon close (X)
3. Verifikasi field Group Name * dengan placeholder `Enter group name`
4. Verifikasi field Code dengan placeholder `Enter code, or leave blank to auto-generate` dan helper `Letters, numbers, hyphens, underscores, and dots only`
5. Verifikasi field Description (textarea) dengan placeholder `Enter description`
6. Verifikasi radio Function None / Assignable masing-masing dengan icon info, None terpilih default
7. Verifikasi checkbox `Stay on this form after submitting` unchecked
8. Verifikasi baris konteks Under tidak ada (level 1)
9. Verifikasi footer: [Clear Field] (text, primary) dan [Submit] (success)

### TC-FA-GRP-80: Create Group level 1 happy path, Code manual, Function Assignable

10. Isi Group Name `Jakarta Hub {runId}-033`, Code `JKT`, Description `Main hub`, lalu pilih Function Assignable
11. Klik [Submit]
12. Verifikasi popup tertutup
13. Verifikasi toast sukses `Success, group has been created.`
14. Ketik Search `Jakarta Hub {runId}-033`, tekan Enter
15. Verifikasi Jakarta Hub muncul sebagai baris level 1 di All Groups
16. Verifikasi Jakarta Hub muncul sebagai node level 1 di sidebar dengan dot primary
17. Verifikasi baris Jakarta Hub: Code `JKT`, Function badge Assignable, Total Asset 0
18. Verifikasi baris Jakarta Hub: Total User sama dengan jumlah user Total Control, Default User, dan Read Only client
19. Verifikasi baris Jakarta Hub: Modified By = aktor (format `[First Name] [Last Initial]`)
20. Verifikasi baris Jakarta Hub: Last Updated = waktu submit (toleransi satu menit)

### TC-FA-GRP-81: Create Group level 1 dengan field opsional kosong, Function default None

21. Klik [+] Group di sidebar
22. Isi hanya Group Name `Bandung Office`
23. Klik [Submit]
24. Verifikasi toast sukses `Success, group has been created.`
25. Ganti isi kotak search dengan `Bandung Office`, tekan Enter
26. Verifikasi Code pada baris Bandung Office ter-generate otomatis `BO2` (BO sudah dipakai Branch Office)
27. Klik nama Bandung Office untuk membuka Popup Detail Group
28. Verifikasi Function `—` di Detail
29. Verifikasi Description `—` di Detail
30. Tutup Popup Detail Group dan klik `(←)` pada kotak Search

### TC-FA-GRP-83: Create Group dengan Stay on this form tercentang (batch)

31. Klik [+] Group di sidebar
32. Centang `Stay on this form after submitting`
33. Isi Group Name `Batch One {runId}-033`, lalu klik [Submit]
34. Verifikasi toast sukses `Success, group has been created.` (submit pertama)
35. Verifikasi field form direset (submit pertama)
36. Verifikasi popup tetap terbuka (submit pertama)
37. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang (submit pertama)
38. Isi Group Name `Batch Two {runId}-033`, lalu klik [Submit]
39. Verifikasi toast sukses `Success, group has been created.` (submit kedua)
40. Verifikasi field form direset (submit kedua)
41. Verifikasi popup tetap terbuka (submit kedua)
42. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang (submit kedua)
43. Klik (X) pada popup (field sudah kosong, tanpa dialog `Unsaved changes`)
44. Ganti isi kotak search dengan `{runId}-033`, tekan Enter
45. Verifikasi Batch One dan Batch Two muncul di tabel
46. Verifikasi Batch One dan Batch Two muncul di sidebar

## Notes

- Mode: FE+BE (kelas fungsional, backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular untuk report per langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 27 (Klik nama Bandung Office untuk membuka Popup Detail Group; Search `Bandung Office` sudah dilakukan pada langkah 25); langkah 30 (Tutup Popup Detail Group dan klik `(←)` pada kotak Search); langkah 43 (Klik (X) pada popup (field sudah kosong, tanpa dialog `Unsaved changes`)); langkah 14, 25, dan 51 (Ketik Search atau ganti isi kotak search dengan `Jakarta Hub {runId}-033`, `Bandung Office`, dan `{runId}-033`) menemukan baris target karena client punya lebih dari 10 node level 1 dengan page size 10, sehingga baris tidak diandalkan berada di halaman 1 (R-16).
- Alasan spec melewati ~35 langkah (46 langkah): keempat TC satu kelas (fungsional Create Group level 1), satu dataset (Plan Professional dan pohon Pre-setup), dan tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); selisih terbesar berasal dari `Verifikasi` per klausa Expected (S-01), terutama TC-FA-GRP-79 dan TC-FA-GRP-83 (dua kali submit), bukan aksi tambahan.
- Popup yang dibuka di langkah 1 tidak dibuka dua kali; tiap blok membuka popup sekali dan menutupnya lewat submit (S-10).
- Temuan untuk QA:
  - TC-FA-GRP-80 Post Condition "Detail Group Jakarta Hub: Code, Description, badge Assignable", "Changelog berisi baris Create", dan "Tanpa auto-assign creator" tidak punya langkah observasi di TC; tidak diasersi di spec ini.
  - TC-FA-GRP-80 Expected c "Total User = jumlah TC/DU/RO client" tidak menyebut cara membaca jumlah; spec memakai pembacaan lewat fixture BE (disediakan tim FE/BE).
  - TC-FA-GRP-81 mengharuskan Name `Bandung Office` agar Code `BO2`; Code auto-generate diturunkan dari token Name sehingga suffix per run mengubah hasil Code. Nama literal dipakai dengan pembersihan di hook `before` dan `after`; butuh butir Lampiran A modul Groups (S-12).
  - TC-FA-GRP-81 Expected c "Function —, Description — di Detail" tidak menyebut langkah membuka Detail; spec menambahkannya sebagai langkah penghubung (langkah 27).

