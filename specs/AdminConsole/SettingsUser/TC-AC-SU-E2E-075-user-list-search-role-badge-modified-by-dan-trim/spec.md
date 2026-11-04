---
id: TC-AC-SU-E2E-075-user-list-search-role-badge-modified-by-dan-trim
title: "User List Search: Kolom Role, Badge, Modified By, Custom Field, dan Trim Query"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-265
  - TC-AC-SU-266
  - TC-AC-SU-267
  - TC-AC-SU-268
  - TC-AC-SU-271
coverage:
  web: automated
---

# User List Search: Kolom Role, Badge, Modified By, Custom Field, dan Trim Query

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-075`): `John Doe {runId}-075` (Global Role `Manage group` aktif, Activated, Active, Custom Field `Office Location` = `Jakarta HQ`), `Jane Smith {runId}-075` (Global Role `Manage group` dengan switch OFF, Activated), `Dewi Lestari {runId}-075` dan `Rina Putri {runId}-075` (Total Control; `Rina Putri {runId}-075` Pending Email Confirmation), `Budi Santoso {runId}-075` (Pending Email Confirmation), `Andi Wijaya {runId}-075` (Read Only, Temporary User `Yes`), `Mike Tan {runId}-075` (Modified By `Budi Hartono {runId}-075`, tampil `Budi H`), `Rudi Hartono {runId}-075` (kolom Name memuat `hartono`). Baris Default User Principal (Pre-setup #1, `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`) dipakai apa adanya dan tidak diubah.
- Custom Field Pre-setup `Office Location` (Text) berstatus Active (Pre-setup #10); spec hanya mengisi nilai pada user milik spec dan tidak mengubah field.
- Fixture `Fixture.settingsUser` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `defaultUserName` (nama tampil baris Default User Principal, Pre-setup #1).
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### TC-AC-SU-265: Search kolom Role mencocokkan nama role aktif dan label tier, bukan teks label jumlah

1. Klik icon Search
2. Ketik Search `manage group`, tekan Enter
3. Verifikasi baris `John Doe {runId}-075` tampil
4. Verifikasi baris `Jane Smith {runId}-075` tidak tampil
5. Verifikasi baris `Dewi Lestari {runId}-075` (Total Control) tidak tampil karena peran termaterialisasi tidak dicocokkan
6. Klik `✕` pada Search
7. Ketik Search `total control`, tekan Enter
8. Verifikasi baris `Fixture.settingsUser.defaultUserName`, `Dewi Lestari {runId}-075`, dan `Rina Putri {runId}-075` tampil
9. Klik `✕` pada Search
10. Ketik Search `3 roles`, tekan Enter
11. Verifikasi empty state dengan ilustrasi, judul `No results found`, dan deskripsi `Try adjusting your search or filter.`
12. Klik `(←)` pada kotak Search

### TC-AC-SU-266: Search kelas badge (Activation Status, Temporary User)

13. Klik `⋯` pada header Actions
14. Klik `[Setup Column]`
15. Centang kolom `Activation Status` dan `Temporary User` pada Setup Column
16. Klik `[Save]`
17. Klik icon Search
18. Ketik Search `pending email`, tekan Enter
19. Verifikasi baris `Rina Putri {runId}-075` dan `Budi Santoso {runId}-075` tampil
20. Verifikasi baris `John Doe {runId}-075` tidak tampil
21. Klik `✕` pada Search
22. Ketik Search `yes`, tekan Enter
23. Verifikasi baris `Andi Wijaya {runId}-075` tampil
24. Verifikasi baris `John Doe {runId}-075` tidak tampil
25. Klik `(←)` pada kotak Search

### TC-AC-SU-267: Search kolom Modified By mencocokkan nama lengkap

26. Klik icon Search
27. Ketik Search `hartono`, tekan Enter
28. Verifikasi baris `Mike Tan {runId}-075` tampil (cocok ke nama lengkap modifier meski sel Modified By tampil `Budi H`)
29. Verifikasi baris `Rudi Hartono {runId}-075` tampil (cocok di kolom Name)
30. Verifikasi baris `John Doe {runId}-075` tidak tampil
31. Klik `(←)` pada kotak Search

### TC-AC-SU-268: Search kolom Custom Field aktif (`Office Location`)

32. Klik `⋯` pada header Actions
33. Klik `[Setup Column]`
34. Centang kolom `Office Location` pada Setup Column
35. Klik `[Save]`
36. Klik icon Search
37. Ketik Search `jakarta`, tekan Enter
38. Verifikasi baris `John Doe {runId}-075` tampil
39. Verifikasi baris `Jane Smith {runId}-075` tidak tampil
40. Klik `(←)` pada kotak Search

### TC-AC-SU-271: Search query di-trim saat Enter

41. Klik icon Search
42. Ketik Search `  jane  ` (spasi di awal dan akhir), tekan Enter
43. Verifikasi baris `Jane Smith {runId}-075` tampil
44. Verifikasi baris `John Doe {runId}-075` tidak tampil
45. Verifikasi isi search box tetap `  jane  `
46. Klik `✕` pada Search
47. Ketik Search tiga spasi, tekan Enter
48. Verifikasi tabel kembali ke seluruh baris (baris `John Doe {runId}-075` dan `Jane Smith {runId}-075` tampil)

## Notes

- Langkah penghubung (S-03): klik `(←)` pada kotak Search di akhir tiap TC menutup input dan mereset tabel supaya TC berikutnya tidak mewarisi keyword (S-09); `Verifikasi` baris pembanding milik spec berfungsi sebagai anchor untuk asersi absence (8b butir 2).
- Alasan di atas ±35 langkah: kelima TC adalah Search User List kelas fungsional dengan dataset yang sama dan berdiri sendiri; kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-075` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-265 menyebut Default User ikut hasil `total control` tetapi baris Default User tidak diberi nama; spec memakai baris Default User Principal (Pre-setup #1) tanpa mengubahnya.
  - TC-267 menyebut Modified By `Budi Hartono`; spec men-seed Modified By bersuffix dan sel tetap tampil `Budi H` (format [First Name] [Last Initial]).
