---
id: TC-AC-SU-E2E-120-tab-user-log-screening-dan-state
title: "Tab User Log: Screening, Isolasi Sesi, Search Kosong, Loading, dan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-425
  - TC-AC-SU-426
  - TC-AC-SU-427
  - TC-AC-SU-428
  - TC-AC-SU-429
  - TC-AC-SU-431
coverage:
  web: automated
---

# Tab User Log: Screening, Isolasi Sesi, Search Kosong, Loading, dan Empty State

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE, dibaca dari Fixture `settingsUser`):
  - User A `Jane Smith {runId}-120` (email `janesmith+{runId}-120@qwertysystem.net`): sesi Admin Console `Session started` dan `Session ended` dengan IP `203.0.113.10` dan user agent Chrome on Windows; satu sesi Admin Console dengan IP `198.51.100.7` dan user agent tidak dikenali; satu sesi Global Settings dengan IP `203.0.113.20`.
  - User lain `Mike Tan {runId}-120` (email `miketan+{runId}-120@qwertysystem.net`): satu sesi Admin Console dengan IP `203.0.113.30`.
  - User B `Rina Putri {runId}-120` (email `rinaputri+{runId}-120@qwertysystem.net`): tanpa sesi (0 baris).
- Kemampuan teknis: Spectra.intercept untuk menahan respons request data tabel tab User Log selama 3000 ms (TC-429; menahan respons hanya untuk mengamati Loading); kemampuan baca dan seed sesi User Log disediakan tim FE/BE.
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-425: Screening Tab User Log

1. Cari `Jane Smith {runId}-120` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
2. Klik tab `User Log`
3. Verifikasi toolbar menampilkan `Search`, `Filter`, dan `Download`
4. Verifikasi header kolom berurutan `Date`, `Activity`, `Status`, `Note`, `IP Address`, `Device / Browser`, diikuti kolom Actions (`⋯`)
5. Verifikasi kolom `Date`, `Activity`, `Status`, `Note`, `IP Address`, dan `Device / Browser` sortable
6. Verifikasi kolom Actions (`⋯`) hanya memicu Column Visibility dan tanpa row action
7. Verifikasi sedikitnya satu baris tampil pada tabel
8. Verifikasi kolom `Activity` setiap baris berisi literal `Session`
9. Verifikasi kolom `Status` setiap baris berisi `—`
10. Verifikasi kolom `Device / Browser` pada baris IP `203.0.113.10` berformat `Chrome on Windows`
11. Verifikasi default sort Date Newest First

### TC-AC-SU-426: Device/Browser tidak terparse tampil strip

12. Verifikasi sel `Device / Browser` pada baris IP `198.51.100.7` (user agent tidak dikenali) berisi `—`

### TC-AC-SU-427: User Log hanya menampilkan sesi Admin Console milik user ini

13. Verifikasi baris sesi Admin Console milik user ini (IP `203.0.113.10`) tampil
14. Verifikasi sesi Global Settings milik user ini (IP `203.0.113.20`) tidak tampil
15. Verifikasi sesi user lain di Admin Console (IP `203.0.113.30`) tidak tampil

### TC-AC-SU-431: Empty state hasil Search Tab User Log tanpa kecocokan

16. Ketik Search `zzqx-tidak-ada`, tekan Enter
17. Verifikasi tabel menampilkan illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
18. Klik icon `(←)` pada kotak Search

### TC-AC-SU-429: Loading state Tab User Log

19. Pasang tahanan respons 3000 ms pada request data tabel tab User Log
20. Muat ulang halaman Detail dengan F5
21. Klik tab `User Log`
22. Verifikasi tabel menampilkan 5 skeleton rows sesuai layout kolom
23. Lepas tahanan respons setelah 3000 ms
24. Verifikasi baris data menggantikan skeleton rows
25. Lepas intercept request data tabel tab User Log

### TC-AC-SU-428: Empty state Tab User Log saat belum ada data

26. Buka Settings > User lewat sidebar
27. Cari `Rina Putri {runId}-120` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
28. Klik tab `User Log`
29. Verifikasi tabel menampilkan illustration dengan Title `No sessions recorded` dan Description `Session activity will appear here.`
30. Verifikasi pagination tidak menampilkan baris data

## Notes

- Langkah pembuka yang mencari user target lewat Search pada User List lalu membuka Detail adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Langkah penghubung tanpa Verifikasi: tutup Search `(←)` (setelah TC-431), lepas tahanan respons, muat ulang F5 sebelum klik tab pada TC-429 (agar request data tabel dikirim ulang dan dapat ditahan), dan kembali ke Settings > User lewat sidebar sebelum TC-428.
- Sesi dibedakan lewat IP Address karena TC-427 tidak menyatakan pembeda antar-sesi Admin Console, Global Settings, dan user lain; Verifikasi baris sesi milik user ini tampil menjadi anchor positif bagi Verifikasi dua sesi lain tidak tampil.
- Temuan untuk QA:
  - TC-428 meminta Jane Smith dengan 0 baris User Log, sedangkan TC-425 sampai 427, 429, dan 431 meminta Jane Smith dengan sesi; satu user tidak dapat memenuhi keduanya. Spec memakai user B untuk TC-428.
  - TC-425 menyebut Status tiap baris `—` dan Activity tiap baris `Session`; nilai itu diasersi untuk semua baris yang tampil, termasuk sesi tambahan dari TC-426.
  - TC-426 dan TC-427 tidak menyebut IP, Note, atau pembeda baris target; IP `198.51.100.7`, `203.0.113.20`, dan `203.0.113.30` adalah pilihan spec.
  - TC-429 tidak menyatakan cara memicu pemuatan ulang data tab; spec memakai F5 lalu klik tab (langkah penghubung).
  - Cara men-seed sesi User Log (Date, Note, IP Address, user agent, asal Admin Console atau Global Settings, user pemilik sesi) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
