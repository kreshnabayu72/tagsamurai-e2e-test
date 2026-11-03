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

- Mode: FE+BE. Spec hanya membaca data Role, kecuali seeding Rudi Hartono di hook `before` (butir Seeding milik spec) dan seeding nilai Custom Field `Region` lewat API modul User (butir Seeding nilai Custom Field `Region`).
- Akun: Total Control, Ahmad Fauzi (Pre-setup #1), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dan navigasi ke Global Settings > Role & Permission > System > Detail "Manage TAG" dilakukan sekali di hook `before` (seedSession). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Data Pre-setup (tetap di environment, hanya dibaca): Detail "Manage TAG" berisi sedikitnya 4 user dengan Position dan Division berbeda (precondition TC), di antaranya Doni Pratama (Staff, IT), Siti Nurhaliza (Finance Staff, Finance), Rina Putri (HR Manager, HR), Hendra Wijaya (HR Manager, HR), dan Ahmad Fauzi (TAG `TG-00451`), serta Bayu Nugraha dan Intan Permata (Temporary User `Yes`, Temporary Until terisi dengan tanggal yang diketahui; Pre-setup #19). Nilai Custom Field `Region` bernilai `Bandung` pada akun Ahmad Fauzi di-seed spec lewat API modul User (butir Seeding nilai Custom Field `Region`; nilai Custom Field user tidak ada di `openapi.yaml` modul Role).
- Seeding milik spec (dibuat lewat API oleh akun Ahmad Fauzi di hook `before`; kemampuan POST/DELETE `/v2/iam/products/{product}/roles/access-level` dan DELETE `/v2/iam/products/{product}/roles/capabilities/users` dari `openapi.yaml`, pola spec 064): Rudi Hartono (Pre-setup #11, Pending Activation) di-assign Total Control agar Detail "Manage TAG" memuat baris Rudi Hartono (Activation Status `Pending Activation`). Hook `after` memulihkan Rudi Hartono ke kondisi kandidat Pre-setup #11 (tanpa access level, tanpa baris role) tanpa berasumsi seeding berhasil penuh. Efek yang tidak dipulihkan: Last Updated dan entri Changelog, Activity Log, serta System Log yang tercatat oleh seeding (log bersifat immutable).
- Seeding nilai Custom Field `Region` milik spec (hook `before`; endpoint milik modul User, bukan modul Role, dari `user-crud.yaml` modul User): userId dan `fieldId` dibaca dari akun aktor Ahmad Fauzi (userId dari `POST /v2/iam/users/list`; kunci `customFields` yang `fieldName`-nya `Region` pada `GET /v2/iam/users/{userId}` memberi `fieldId`, dan `valueText`-nya dicatat sebagai nilai awal). Lalu spec mengirim `PATCH /v2/iam/users/{userId}/custom-fields/{fieldId}` dengan body `{"value": "Bandung"}` pada akun Ahmad Fauzi sendiri (akun aktor sendiri tidak diblokir oleh aturan 403 untuk target Total Control, `USER-LOGIC-01f`). Prasyarat environment: Custom Field `Region` aktif bertipe Dropdown dengan opsi `Bandung` (label opsi yang tidak dikenal ditolak `422`); definisi field dan opsinya tetap data environment, hanya nilai pada user yang di-seed. Hook `after` (tetap jalan walau spec gagal di tengah, tidak berasumsi seeding berhasil penuh) memulihkan lewat `PATCH` yang sama berisi nilai awal yang dicatat (`null` bila awalnya kosong). Efek yang tidak dipulihkan: satu entri Changelog `Edit | Region` per `PATCH` dan Last Updated akun Ahmad Fauzi (log bersifat immutable).
- Data uji: keyword Search `PRATAMA`, `staf`, `it`, `Update`, `Pending`, `Yes`, `TG-00451`, `Bandung`, dan tanggal Temporary Until Bayu Nugraha atau Intan Permata (Pre-setup #19, tanggal diketahui; ditulis dalam format tanggal General Settings aktif dan dibaca di hook `before` lewat kemampuan membaca data yang disediakan tim FE). Custom Field aktif `Region` (definisi field dan opsi `Bandung`) tersedia di environment; nilainya di-seed spec.
- Preferensi kolom (visibilitas, urutan, pin) tersimpan per user di browser per tabel dan menjadi permanen setelah `[Save]` (prd-conventions.md §9.3).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State yang diubah dan dipulihkan di hook `after` (tetap jalan walau spec gagal di tengah): konfigurasi kolom tabel Detail "Manage TAG" dikembalikan ke default (kolom `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Region` tersembunyi) lewat penghapusan preferensi kolom tabel itu di browser (bagian 4 konvensi; kemampuan di butir Kemampuan teknis); langkah 29 sampai 32 memulihkannya lewat UI di dalam spec.
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
  - TC-GS-ROLE-188: Expected c ("menampilkan user temporary") tidak menyebut nama; spec mengasersi baris user dengan Temporary User `Yes`. Rudi Hartono (Pending Activation) hanya ada di Pre-setup #11 tanpa baris role, sehingga precondition TC tidak menjaminnya ada di Detail "Manage TAG"; spec men-seed Total Control lewat API. User Temporary User `Yes` memakai Pre-setup #19. User Region `Bandung` tidak ada di Tabel Pre-setup TC dan nilai Custom Field user tidak ada di `openapi.yaml` modul Role; spec men-seed nilai `Region` `Bandung` pada akun Ahmad Fauzi lewat `PATCH /v2/iam/users/{userId}/custom-fields/{fieldId}` (endpoint modul User, `user-crud.yaml`) dan memulihkannya di hook `after`. Keberadaan Custom Field `Region` dengan opsi `Bandung` tetap prasyarat environment.
  - TC-GS-ROLE-188 langkah 2: TC menyebut kolom "Region" sebagai Custom Field aktif tanpa menyebut tipenya; spec memakai nama `Region`.
