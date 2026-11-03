---
id: TC-AC-SU-E2E-076-user-list-search-kolom-hidden-non-searchable-dan-status
title: "User List Search: Kolom Hidden, Kolom Non-Searchable, Status Active/Inactive, dan Custom Field Date"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-269
  - TC-AC-SU-270
  - TC-AC-SU-648
  - TC-AC-SU-659
coverage:
  web: automated
---

# User List Search: Kolom Hidden, Kolom Non-Searchable, Status Active/Inactive, dan Custom Field Date

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` dan kemampuan Fixture BE mengikuti `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed hook `before` lewat Fixture BE; nama bersuffix `{runId}-076`): `Jane Smith {runId}-076` (Active, Position `Finance Manager`, Custom Field `Join Date` = 15 Jan 2026), `John Doe {runId}-076` (Active, Last Updated terisi), `Andi Wijaya {runId}-076` (Temporary User `Yes`, Temporary Until terisi), `Budi Santoso {runId}-076` (Inactive), `Mike Tan {runId}-076` (Active). Tidak ada user lain yang memuat teks `15/01/26` di kolom mana pun.
- Custom Field Pre-setup `Join Date` (Date) berstatus Active (Pre-setup #10); spec hanya mengisi nilai pada user milik spec.
- General Settings: Date Format `DD/MM/YY` diatur hook `before` lewat Fixture BE dan dipulihkan ke nilai awal di hook `after` (state global; suite serial).
- Tabel keyword TC-270 (parameter langkah 17 sampai 20):
| No | Kolom | Baris sumber nilai |
|---|---|---|
| 1 | Last Updated | `John Doe {runId}-076` |
| 2 | Temporary Until | `Andi Wijaya {runId}-076` |
- Hook `after` menghapus data yang di-seed hook `before` spec ini lewat Fixture BE; pembersihan tidak berasumsi seeding berhasil penuh.
- Pemulihan Setup Column: preferensi kolom yang disimpan spec ini dihapus di hook `after` dengan menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.

## Test Steps

### TC-AC-SU-269: Search kolom yang di-hide tidak mencocokkan, lalu cocok lagi setelah di-unhide

1. Klik `⋯` pada header Actions
2. Hapus centang `Position` pada overlay Column Visibility
3. Klik icon Search
4. Ketik Search `finance man`, tekan Enter
5. Verifikasi empty state dengan judul `No results found`
6. Klik `⋯` pada header Actions
7. Centang `Position` pada overlay Column Visibility
8. Klik `✕` pada Search
9. Ketik Search `finance man`, tekan Enter
10. Verifikasi baris `Jane Smith {runId}-076` (Position `Finance Manager`) tampil kembali
11. Klik `(←)` pada kotak Search

### TC-AC-SU-270: Guard kolom non-searchable (Last Updated, Temporary Until)

12. Klik `⋯` pada header Actions
13. Klik `[Setup Column]`
14. Centang kolom `Temporary Until` pada Setup Column
15. Klik `[Save]`
16. Klik icon Search
17. Baca teks sel pada kolom "Kolom" di baris "Baris sumber nilai" tabel keyword TC-270, persis seperti tampil di sel
18. Ketik Search teks sel tersebut, tekan Enter
19. Verifikasi empty state dengan judul `No results found`
20. Klik `✕` pada Search, tekan Enter
21. Klik `(←)` pada kotak Search

### TC-AC-SU-648: Search kolom Active mencocokkan status Active/Inactive

22. Klik icon Search
23. Ketik Search `inactive`, tekan Enter
24. Verifikasi baris `Budi Santoso {runId}-076` (Inactive) tampil
25. Verifikasi baris `Mike Tan {runId}-076` (Active) tidak tampil
26. Klik `✕` pada Search
27. Ketik Search `active`, tekan Enter
28. Verifikasi baris `Mike Tan {runId}-076` (Active) tampil
29. Verifikasi baris `Budi Santoso {runId}-076` (Inactive) tidak tampil (exact match, bukan substring `inactive`)
30. Klik `(←)` pada kotak Search

### TC-AC-SU-659: Search tidak mencocokkan kolom Custom Field bertipe Date

31. Klik `⋯` pada header Actions
32. Klik `[Setup Column]`
33. Centang kolom `Join Date` pada Setup Column
34. Klik `[Save]`
35. Verifikasi sel `Join Date` baris `Jane Smith {runId}-076` menampilkan `15/01/26`
36. Klik icon Search
37. Ketik Search `15/01/26`, tekan Enter
38. Verifikasi empty state dengan ilustrasi, judul `No results found`, dan deskripsi `Try adjusting your search or filter.`
39. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): klik `(←)` pada kotak Search di akhir tiap TC mereset tabel; langkah Setup Column pada TC-659 memenuhi precondition TC ("ditampilkan lewat Setup Column"); `Verifikasi` sel `Join Date` baris `Jane Smith {runId}-076` di TC-659 adalah anchor positif untuk empty state (8b butir 2) dan dicatat sebagai asersi tambahan di luar Expected TC.
- Langkah 17 sampai 20 diulang untuk tiap baris tabel keyword TC-270 (8b butir 7); parameter ada di Prerequisites.
- Alasan di atas ±35 langkah: keempat TC adalah Search User List kelas fungsional, dataset sama, berdiri sendiri; kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Temuan untuk QA:
  - TC menulis nama data DS-UL secara literal (nama user, email, position, division). Spec memakai nama bersuffix ` {runId}-076` (S-12) dan mengasersi baris milik spec; klaim "hanya X yang tampil" pada TC tidak dapat diasersi atas seluruh tabel karena baris Pre-setup bernama sama ikut ada di entitas Principal.
  - TC-270 membaca tanggal Last Updated dan Temporary Until dari baris DS-UL; TC tidak menyatakan bagaimana baris sumber ditemukan bila berada di halaman lain; spec mengandalkan baris milik spec tampil di halaman 1.
  - TC-659 precondition d menyebut Jane Smith punya Join Date 15 Jan 2026 dan Date Format `DD/MM/YY`; TC tidak menyatakan Date Format diatur oleh siapa; spec mengatur lewat Fixture BE di hook dan memulihkannya.
