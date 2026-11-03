---
id: TC-AC-SU-E2E-113-tab-system-log-screening-dan-state
title: "Tab System Log: Screening, Search Kosong, Loading, Hover Snapshot Group, dan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-404
  - TC-AC-SU-405
  - TC-AC-SU-406
  - TC-AC-SU-408
  - TC-AC-SU-654
coverage:
  web: automated
---

# Tab System Log: Screening, Search Kosong, Loading, Hover Snapshot Group, dan Empty State

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE, dibaca dari Fixture `settingsUser`):
  - User A `Jane Smith {runId}-113` (email `janesmith+{runId}-113@qwertysystem.net`) sebagai aktor: sedikitnya 4 entri System Log (`Deactivate` Object `User`, `Resend Activation Email` Object `User`, `Assign` Object `Total Control`, `Edit` Object `Global Role`) dengan Name berisi user lain (mis. `John Doe {runId}-113`, `Sarah Lee {runId}-113`, `Rina Putri {runId}-113`).
  - User B `Budi Santoso {runId}-113` (email `budisantoso+{runId}-113@qwertysystem.net`) sebagai aktor: entri `Delete` Object `Group` dengan Name leaf `Hapus Warn B1 {runId}-113` dan snapshot full path `Hapus Warn B {runId}-113 > Hapus Warn B1 {runId}-113` (hasil Delete Group dari Settings > Group, di-seed BE), serta entri Object `User` Name `John Doe {runId}-113`.
  - User C `Rina Putri {runId}-113` (email `rinaputri+{runId}-113@qwertysystem.net`): tanpa entri System Log (0 baris).
- Kemampuan teknis: Spectra.intercept untuk menahan respons request data tabel tab System Log selama 3000 ms (TC-406; menahan respons hanya untuk mengamati Loading); kemampuan baca dan seed entri System Log disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-404: Screening Tab System Log

1. Cari `Jane Smith {runId}-113` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
2. Klik tab `System Log`
3. Verifikasi toolbar menampilkan `Search`, `Filter`, dan `Download`
4. Verifikasi header kolom berurutan `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`, diikuti kolom Actions (`⋯`)
5. Verifikasi kolom `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, dan `New Value` sortable
6. Verifikasi kolom Actions (`⋯`) hanya memicu Column Visibility dan tanpa row action
7. Verifikasi tidak ada kolom Modified By
8. Verifikasi sedikitnya satu baris tampil pada tabel
9. Verifikasi setiap baris pada kolom `Name` berisi user target (bukan `Jane Smith {runId}-113`, pemilik halaman)
10. Verifikasi default sort Date Newest First
11. Verifikasi footer menampilkan pagination standar

### TC-AC-SU-408: Empty state hasil Search Tab System Log tanpa kecocokan

12. Ketik Search `zzqx-tidak-ada`, tekan Enter
13. Verifikasi tabel menampilkan illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
14. Klik icon `(←)` pada kotak Search

### TC-AC-SU-406: Loading state Tab System Log

15. Pasang tahanan respons 3000 ms pada request data tabel tab System Log
16. Muat ulang halaman Detail dengan F5
17. Klik tab `System Log`
18. Verifikasi tabel menampilkan 5 skeleton rows sesuai layout kolom
19. Lepas tahanan respons setelah 3000 ms
20. Verifikasi baris data menggantikan skeleton rows
21. Lepas intercept request data tabel tab System Log

### TC-AC-SU-654: Hover kolom Name entri Object Group menampilkan snapshot full path

22. Buka Settings > User lewat sidebar
23. Cari `Budi Santoso {runId}-113` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
24. Klik tab `System Log`
25. Verifikasi sel Name entri Object `Group` menampilkan nama leaf `Hapus Warn B1 {runId}-113`
26. Hover sel Name entri Object `Group`
27. Verifikasi tooltip snapshot full path `Hapus Warn B {runId}-113 > Hapus Warn B1 {runId}-113` tampil
28. Hover sel Name entri Object `User`
29. Verifikasi tooltip tidak tampil pada sel Name entri Object `User`
30. Klik icon Filter, lalu buka dropdown `Name`
31. Verifikasi field `Name` berplaceholder `All names`
32. Verifikasi dropdown `Name` memuat opsi `Hapus Warn B1 {runId}-113` (label opsi group berupa nama leaf) dan `John Doe {runId}-113`
33. Tutup dropdown, lalu klik icon Filter untuk menutup Filter Panel

### TC-AC-SU-405: Empty state Tab System Log saat belum ada data

34. Buka Settings > User lewat sidebar
35. Cari `Rina Putri {runId}-113` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
36. Klik tab `System Log`
37. Verifikasi tabel menampilkan illustration dengan Title `No system logs recorded` dan Description `Security and audit trail records will appear here.`
38. Verifikasi pagination tidak menampilkan baris data

## Notes

- Langkah pembuka yang mencari user target lewat Search pada User List lalu membuka Detail adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Langkah penghubung tanpa Verifikasi: tutup Search `(←)` (setelah TC-408), lepas tahanan respons, muat ulang F5 sebelum klik tab pada TC-406 (agar request data tabel dikirim ulang dan dapat ditahan), menutup dropdown dan Filter Panel, serta kembali ke Settings > User lewat sidebar sebelum tiap user berikutnya. Hover sel Object `User` langsung setelah tooltip Object `Group` tampil adalah anchor positif bagi Verifikasi tooltip tidak tampil.
- Temuan untuk QA:
  - TC-405 meminta Jane Smith dengan 0 baris System Log, sedangkan TC-404, 406, dan 408 meminta Jane Smith dengan entri; satu user tidak dapat memenuhi keduanya. Spec memakai user C untuk TC-405 dan user B (`Budi Santoso`, aktor Pre-setup baris 12) untuk TC-654 karena preconditionnya khusus.
  - TC-406 tidak menyatakan cara memicu pemuatan ulang data tab; spec memakai F5 lalu klik tab (langkah penghubung).
  - Nama leaf dan snapshot full path group pada TC-654 dipakai dengan suffix `{runId}-113` dan di-seed sebagai data milik spec, bukan memakai data Pre-setup baris 12 (`Hapus Warn B1`).
  - Cara men-seed entri System Log (Date, Action, Object, Name, Field, Old Value, New Value, aktor, termasuk snapshot full path untuk Object `Group`) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
- Spec ini melewati sekitar 35 langkah (38 langkah nominal, sekitar 38 dengan ekspansi blok berulang). Alasan pertahanan: seluruh blok berada pada satu permukaan, satu kelas harness (fungsional biasa), memakai dataset seeding yang sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
