---
id: TC-GS-ROLE-E2E-062-detail-search-name-position-division-dan-kolom-lain
title: "Detail Manage TAG: Search Berdasarkan Name, Position, Division, dan Kolom Lain"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-186
  - TC-GS-ROLE-187
  - TC-GS-ROLE-188
coverage:
  web: automated
---

# Detail Manage TAG: Search Berdasarkan Name, Position, Division, dan Kolom Lain

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data Role; seluruh data hanya dibaca.
- Akun: Total Control, Ahmad Fauzi (Pre-setup #1), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Role & Permission > System > Detail "Manage TAG" dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (tetap di environment, hanya dibaca): Detail "Manage TAG" berisi sedikitnya 4 user dengan Position dan Division berbeda (precondition TC), di antaranya Doni Pratama (Staff, IT), Siti Nurhaliza (Finance Staff, Finance), Rina Putri (HR Manager, HR), Hendra Wijaya (HR Manager, HR), dan Ahmad Fauzi (TAG `TG-00451`); Rudi Hartono berstatus Pending Activation; sedikitnya satu user dengan Temporary User `Yes`; satu user ber-Custom Field `Region` bernilai `Bandung`. Keberadaan baris Rudi Hartono, user Temporary User `Yes`, dan user Region `Bandung` pada Detail "Manage TAG" mengikuti TC dan disediakan tim FE.
- Data uji: keyword Search `PRATAMA`, `staf`, `it`, `Update`, `Pending`, `Yes`, `TG-00451`, `Bandung`, dan tanggal Temporary Until salah satu user temporary pada Detail "Manage TAG" (ditulis dalam format tanggal General Settings aktif dan dibaca di hook `before` lewat kemampuan membaca data yang disediakan tim FE). Custom Field aktif `Region` disediakan tim FE.
- Preferensi kolom (visibilitas, urutan, pin) tersimpan per user di browser per tabel dan menjadi permanen setelah `[Save]` (prd-conventions.md §9.3).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom tabel Detail "Manage TAG" dikembalikan ke default (kolom `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Region` tersembunyi) lewat `[Reset to Default]` atau penghapusan preferensi kolom tabel itu di browser; langkah 29 sampai 32 memulihkannya di dalam spec.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission > System > Detail "Manage TAG" (Search dikosongkan).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: membaca data Temporary Until per user (disediakan tim FE); membaca dan menghapus preferensi kolom di penyimpanan browser.

## Test Steps

### TC-GS-ROLE-186: Search Detail berdasarkan Name, Position, Division

1. Klik icon Search
2. Verifikasi placeholder `Search name...`
3. Ketik Search `PRATAMA`, tekan Enter
4. Verifikasi baris Doni Pratama tampil
5. Ganti isi kotak search dengan `staf`, tekan Enter
6. Verifikasi baris dengan Position `Staff` (Doni Pratama) dan `Finance Staff` (Siti Nurhaliza) tampil
7. Ganti isi kotak search dengan `it`, tekan Enter
8. Verifikasi baris dengan Division `IT` (Doni Pratama) tampil

### TC-GS-ROLE-187: Search Detail tidak mencocokkan kolom CRUD dan Temporary Until

9. Ganti isi kotak search dengan `Update`, tekan Enter
10. Verifikasi `No results found` tampil
11. Ganti isi kotak search dengan tanggal Temporary Until salah satu user, tekan Enter
12. Verifikasi `No results found` tampil
13. Klik `(←)` pada kotak Search

### TC-GS-ROLE-188: Search Detail kolom Activation Status, Temporary User, TAG, dan Custom Field

14. Ketik Search `TG-00451`, tekan Enter
15. Verifikasi `No results found` tampil karena kolom `TAG` default tersembunyi
16. Klik header kolom Column Visibility (⋯)
17. Klik item `Setup Column...`
18. Centang `Activation Status`, `Temporary User`, `TAG`, dan `Region`
19. Klik `[Save]`
20. Ganti isi kotak search dengan `Pending`, tekan Enter
21. Verifikasi baris Rudi Hartono (Pending Activation) tampil
22. Ganti isi kotak search dengan `Yes`, tekan Enter
23. Verifikasi baris user dengan Temporary User `Yes` tampil
24. Ganti isi kotak search dengan `TG-00451`, tekan Enter
25. Verifikasi baris Ahmad Fauzi tampil
26. Ganti isi kotak search dengan `Bandung`, tekan Enter
27. Verifikasi baris user dengan Region `Bandung` tampil
28. Klik `(←)` pada kotak Search
29. Klik header kolom Column Visibility (⋯)
30. Klik item `Setup Column...`
31. Klik `[Reset to Default]`
32. Klik `[Save]`

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE (data Detail dimuat dari backend nyata; Search bekerja terhadap data server).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (186, 187, 188) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah "Klik `(←)` pada kotak Search" di akhir TC-GS-ROLE-187 (menutup Search dan mereset tabel sebelum TC-GS-ROLE-188), langkah "Klik `(←)` pada kotak Search" dan langkah 29 sampai 32 di akhir TC-GS-ROLE-188 (menutup Search dan memulihkan konfigurasi kolom; hook `after` sebagai cadangan).
- Asersi `No results found` (Search tanpa hasil) adalah anchor positif yang sah untuk absence hasil Search (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-GS-ROLE-189 dan 190 (Filter Detail) di spec 063; Download Detail (TC-GS-ROLE-194 dan 303) di spec 061; retensi Search Tab System (TC-GS-ROLE-195) di spec 060.
- Temuan untuk QA:
  - TC-GS-ROLE-186 Expected d: keyword `it` juga cocok dengan nama (mis. Siti Nurhaliza); spec hanya mengasersi baris Division `IT` tampil dan tidak mengasersi hasil lain.
  - TC-GS-ROLE-187: TC tidak menyebut user yang tanggal Temporary Until-nya dipakai dan format tanggalnya; spec memakai tanggal user temporary pada Detail "Manage TAG" dalam format General Settings aktif. Kolom `Temporary Until` default tersembunyi dan tidak ditampilkan pada TC ini.
  - TC-GS-ROLE-188: Expected c ("menampilkan user temporary") tidak menyebut nama; spec mengasersi baris user dengan Temporary User `Yes`. Keberadaan Rudi Hartono (Pending Activation), user Temporary User `Yes`, dan user Region `Bandung` pada Detail "Manage TAG" tidak ada di Tabel Pre-setup TC (Rudi Hartono hanya ada di Pre-setup #11); disediakan tim FE.
  - TC-GS-ROLE-188 langkah 2: TC menyebut kolom "Region" sebagai Custom Field aktif tanpa menyebut tipenya; spec memakai nama `Region`.
