---
id: TC-AC-SU-E2E-115-tab-system-log-search-siklus-dan-kolom-non-searchable
title: "Tab System Log: Siklus Search Box dan Kolom Non-searchable"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-411
  - TC-AC-SU-413
coverage:
  web: automated
---

# Tab System Log: Siklus Search Box dan Kolom Non-searchable

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-115` (email `janesmith+{runId}-115@qwertysystem.net`) sebagai aktor dengan 3 entri System Log: (1) Action `Deactivate`, Object `User`, Name `John Doe {runId}-115`, Field `Status`, Old Value `Active`, New Value `Inactive`; (2) Date `15 Jun 2026`, Action `Assign`, Object `Total Control`, Name `Rina Putri {runId}-115`, Field `Access Level`, Old Value `Inactive`, New Value `Active`; (3) Action `Edit`, Object `Global Role`, Name `Sarah Lee {runId}-115`, Field `Manage group — Update`, Old Value `Read`, New Value `Update`. Keyword `Deactivate` hanya memuat entri (1); nilai `15 Jun 2026` tidak muncul di kolom searchable mana pun.
- Kemampuan teknis: kemampuan seed entri System Log dengan Date tertentu disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-411: Siklus interaksi Search box Tab System Log

1. Cari `Jane Smith {runId}-115` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
2. Klik tab `System Log`
3. Hover icon Search
4. Verifikasi tooltip `Search` tampil
5. Klik icon Search
6. Verifikasi input Search melebar
7. Verifikasi kursor auto-focus di input Search
8. Verifikasi placeholder input Search `Search action, field, or value...`
9. Ketik `Deactivate` di input Search tanpa menekan Enter
10. Verifikasi icon `(✕)` muncul
11. Verifikasi tabel belum tersaring (jumlah baris sama dengan sebelum mengetik)
12. Tekan Enter
13. Verifikasi sedikitnya satu baris tampil
14. Verifikasi setiap baris yang tampil memuat `Deactivate`
15. Klik icon `(✕)`
16. Verifikasi input Search kosong
17. Verifikasi search bar tetap terbuka
18. Verifikasi tabel tetap menampilkan hasil search terakhir
19. Tekan Enter pada input kosong
20. Verifikasi tabel kembali menampilkan semua data (jumlah baris sama dengan sebelum Search)
21. Ketik Search `Deactivate`, tekan Enter
22. Klik icon `(←)`
23. Verifikasi search bar collapse ke icon
24. Verifikasi keyword Search kosong
25. Verifikasi tabel langsung kembali menampilkan semua data

### TC-AC-SU-413: Kolom non-searchable tidak ikut dicari

26. Verifikasi sedikitnya satu baris data tampil pada tabel
27. Ketik Search `15 Jun 2026`, tekan Enter
28. Verifikasi tabel menampilkan empty state `No results found`
29. Klik icon Filter
30. Verifikasi Filter Panel memuat field `Date`
31. Klik icon Filter untuk menutup Filter Panel
32. Klik icon `(←)` pada kotak Search

## Notes

- Langkah pembuka yang mencari user target lewat Search pada User List lalu membuka Detail adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Pada TC-413, klik icon Filter, Verifikasi field `Date`, dan menutup panel mengasersi Expected b (penyaringan kolom Date hanya lewat Filter Panel) dan diturunkan dari TC-414 yang menyatakan `Date` ada di Filter Panel Tab System Log. Pembagian TC lintas spec: TC-412 ada di spec 196.
- Temuan untuk QA:
  - Expected b TC-413 ('hanya tersedia lewat Filter Panel (bila Filterable)') bersifat penjelasan bersyarat tanpa hasil teramati sendiri; spec mengasersinya lewat keberadaan field `Date`.
  - Keyword `15 Jun 2026` ditulis tahun empat digit, sedangkan format tampil Date mengikuti Date Format General Settings (tidak tertulis di TC).
  - Cara men-seed entri System Log (Date, Action, Object, Name, Field, Old Value, New Value, aktor, termasuk snapshot full path untuk Object `Group`) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
