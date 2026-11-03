---
id: TC-FA-GRP-E2E-214-tab-assets-filter-panel-screening-dan-filter-status-opsi-or-search-dropdown
title: "Tab Assets Filter: Screening Panel dan Filter Status (Isi Opsi, Satu/Dua Opsi OR)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-683
  - TC-FA-GRP-684
  - TC-FA-GRP-685
  - TC-FA-GRP-686
coverage:
  web: automated
---

# Tab Assets Filter: Screening Panel dan Filter Status (Isi Opsi, Satu/Dua Opsi OR)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`) berlaku: login default, flag Guided Tooltip `seen`, sesi API aktor, klien HTTP, dan fixture BE disediakan tim FE/BE.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9: 24 aset aktif variasi status + 2 Disposed). Nilai variasi (Name, Asset ID, Status, Brand, Model/Type, Category, Last Updated; sedikitnya dua nilai distinct per kolom yang dipakai Search, Filter, dan Sort, S-11) dan nilai fixture acuan `Fixture.settingsGroups.<kunci>` disediakan tim FE/BE; Tabel Data Uji TC tidak memuat nilai konkret (lihat Temuan untuk QA).
- Opsi Status: Fixture.settingsGroups.statusA dan Fixture.settingsGroups.statusB adalah dua nilai Status distinct yang genuinely dimiliki baris Warehouse A; Fixture.settingsGroups.statusTidakDipakai adalah nilai Status yang tidak dipakai baris mana pun.
- Field Custom Field pada Filter Panel diverifikasi memakai fixture tipe Custom Field (Tabel Dinamis No 18: Condition Grade, Features, Inspection Time, Usage Hours, Budget, Utilization, Contact Email, Computed Total; Scope General, Active); fixture di-seed per spec ini di hook `before` dengan nama bersuffix `{runId}-214` (mis. `Condition Grade {runId}-214`), hanya dibaca oleh langkah, dan dihapus di hook `after`; spec tidak memakai Custom Field milik spec lain. Suite berjalan serial.

## Test Steps

### TC-FA-GRP-683: Screening Filter Panel Tab Assets

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total Asset Warehouse A untuk membuka Popup Detail Group, Tab Assets
3. Telusuri semua halaman tabel dari halaman 1 sampai halaman terakhir, lalu catat himpunan nilai Status distinct pada baris tabel
4. Klik icon Filter pada toolbar
5. Verifikasi Filter Panel terbuka
6. Verifikasi urutan field Filter Panel mengikuti Setup Column Tab Assets
7. Verifikasi field Asset Name adalah dropdown multi-select searchable dengan placeholder `All asset names`
8. Verifikasi field TAG adalah dropdown multi-select searchable dengan placeholder `All tags`
9. Verifikasi field Brand adalah dropdown multi-select searchable dengan placeholder `All brands`
10. Verifikasi field Model/Type adalah dropdown multi-select searchable dengan placeholder `All models`
11. Verifikasi field Measurement adalah dropdown multi-select searchable dengan placeholder `All units`
12. Verifikasi field Category adalah tombol tree picker multi-select dengan placeholder `All categories`
13. Verifikasi field Label adalah dropdown multi-select searchable dengan placeholder `All labels`
14. Verifikasi field Status adalah dropdown multi-select searchable dengan placeholder `All statuses`
15. Verifikasi field Transactional Policy adalah dropdown multi-select searchable dengan placeholder `All transactions`
16. Verifikasi field Last Scanned adalah date range picker dengan placeholder `Select date`
17. Verifikasi field Asset Value (Commercial) dan Asset Value (Fiscal) masing-masing satu field range Min–Max dengan placeholder `Min` dan `Max`
18. Verifikasi field Warranty Expiry adalah date range picker dengan placeholder `Select date`
19. Verifikasi field Last Updated adalah date range picker dengan placeholder `Select date`
20. Verifikasi tombol footer [Clear Field] dan [Apply] tampil
21. Verifikasi tidak ada field filter lain di luar daftar Setup Column
22. Verifikasi tidak ada field Group
23. Verifikasi field Custom Field bertipe Dropdown dan Multi-Dropdown adalah multi-select searchable
24. Verifikasi field Custom Field bertipe DateTime adalah date range picker
25. Verifikasi field Custom Field bertipe Numeric, Currency, dan Percentage adalah range Min–Max
26. Verifikasi Custom Field bertipe Email dan Formula tidak memiliki field filter

### TC-FA-GRP-684: Screening isi opsi dropdown Filter Status

27. Buka dropdown Status
28. Verifikasi opsi = himpunan nilai Status distinct yang dicatat pada langkah 3
29. Verifikasi opsi `Fixture.settingsGroups.statusTidakDipakai` tidak tampil
30. Verifikasi opsi dapat dicentang lebih dari satu (multi-select)
31. Verifikasi kotak search internal tampil di dalam dropdown

### TC-FA-GRP-685: Filter Status satu opsi

32. Tutup dropdown Status dan klik [Clear Field] (langkah penghubung)
33. Pilih opsi `Fixture.settingsGroups.statusA` pada Status, klik [Apply]
34. Verifikasi sedikitnya satu baris tampil
35. Verifikasi setiap baris yang tampil berstatus `Fixture.settingsGroups.statusA`
36. Verifikasi indikator filter aktif tampil pada icon Filter

### TC-FA-GRP-686: Filter Status dua opsi (OR)

37. Klik icon Filter, klik [Clear Field], klik [Apply] (langkah penghubung)
38. Klik icon Filter, centang opsi `Fixture.settingsGroups.statusA` dan `Fixture.settingsGroups.statusB` pada Status, klik [Apply]
39. Verifikasi baris berstatus `Fixture.settingsGroups.statusA` tampil
40. Verifikasi baris berstatus `Fixture.settingsGroups.statusB` tampil
41. Verifikasi setiap baris yang tampil berstatus `Fixture.settingsGroups.statusA` atau `Fixture.settingsGroups.statusB`

## Notes

- Langkah penghubung (S-03): langkah 2 membuka Popup Detail Group Tab Assets; langkah penutup dropdown dan [Clear Field] serta [Apply] mengosongkan Filter antar-TC (S-09).
- Spec berisi 4 TC Filter Status dan screening Filter Panel dalam satu kelas harness dan satu dataset Warehouse A; tiap blok berdiri sendiri. Melewati sekitar 35 langkah karena TC-683 memuat 11+ field dengan tipe dan placeholder masing-masing sebagai klausa terpisah (S-01).
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Himpunan nilai Status distinct dicatat dengan menelusuri seluruh halaman tabel sebelum Filter Panel dibuka (langkah 3), karena Warehouse A memuat 24 aset aktif dengan page size 10 sehingga halaman 1 saja tidak mewakili himpunan (S-11, S-14).
- Temuan untuk QA:
  - TC-683 c: daftar tipe field Custom Field (Dropdown, Date/DateTime, Numeric/Currency/Percentage, Text/Text Area/Phone/Email/URL/Document/Formula) tidak punya fixture Custom Field per tipe di Tabel Data Uji TC-683; spec memakai fixture Tabel Dinamis No 18 (hanya sebagian tipe) dan tidak mengasersi tipe Date, Text Area, Phone, URL, Document.
  - TC-683 a: urutan field "mengikuti Setup Column" tidak disebut urutan konkretnya selain daftar; spec mengasersi urutan sesuai daftar Expected.
  - TC-683 c: field Custom Field Scope General pada Warehouse A berpotensi tidak muncul bila kolom curated tersembunyi default; kebergantungan ini tidak dinyatakan.
