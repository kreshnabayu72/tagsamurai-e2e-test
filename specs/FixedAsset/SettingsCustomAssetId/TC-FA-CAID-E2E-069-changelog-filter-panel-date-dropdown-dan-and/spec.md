---
id: TC-FA-CAID-E2E-069-changelog-filter-panel-date-dropdown-dan-and
title: "Modal Changelog: Filter Panel, Rentang Date, Dropdown OR, dan Logika AND"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-177
  - TC-FA-CAID-178
  - TC-FA-CAID-179
  - TC-FA-CAID-180
coverage:
  web: automated
---

# Modal Changelog: Filter Panel, Rentang Date, Dropdown OR, dan Logika AND

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Changelog (Pre-setup No 1, pola `totalControl_automated_{namaCompany}@qwertysystem.net`; Company Changelog, Pre-setup No 15). Email akun disediakan tim FE/BE (Pre-setup No 15 hanya menyebut env var). Login di hook `before` spec ini (kredensial `Spectra.env.FA_CHANGELOG_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > Custom Asset ID); hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`).
- Environment variable: `FA_CHANGELOG_TC_PASSWORD` (Total Control Company Changelog) dan `FA_TC_PASSWORD` (akun default suite). Password tidak ditulis di spec atau fixture; kedua nama didaftarkan di tahap script.
- Data Pre-setup (hanya dibaca): No 15 Company Changelog; No 27 General Settings Company Changelog (Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`). Data Dinamis: tidak ada. Nilai L1 sampai L7 adalah data Pre-setup tetap (bukan data Dinamis) sehingga tidak bersuffix `{runId}`; fixture modul Custom Asset ID untuk nilai ini dan teks UI belum ada; prasyarat tahap script yang disediakan tim FE/BE.
- Entri Changelog seed (Pre-setup No 15, urut Date terbaru di atas, pengguna Rina Putri `Rina P`, Sarah Johnson `Sarah J`, Budi Santoso `Budi S`):

| Id | Date | Action | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| L1 | `15/09/26, 14:25` | Edit | Separator | `Dash` | `Dot` | `Rina P` |
| L2 | `14/09/26, 11:30` | Edit | Status | `Inactive` | `Active` | `Sarah J` |
| L3 | `13/09/26, 09:15` | Edit | Status | `Active` | `Inactive` | `Budi S` |
| L4 | `12/09/26, 16:40` | Edit | Separator | `Slash` | `Dash` | `Sarah J` |
| L5 | `10/09/26, 10:02` | Create | Segments Formula | `—` | `Initial Company (Inactive), Group Code (Active), Category Code (Active), Asset Name Code (Active), Division Code (Inactive), Account Code (Inactive), Purchase Date (Active), Asset Increment (Active)` | `Sarah J` |
| L6 | `10/09/26, 10:01` | Create | Separator | `—` | `Slash` | `Sarah J` |
| L7 | `10/09/26, 10:00` | Create | Status | `—` | `Active` | `Sarah J` |

- Seeding (hook `before`, lewat sesi API aktor): ketujuh entri L1 sampai L7 dengan Date, Action, Field, Old Value, New Value, dan Modified By persis tabel di atas (entri L1 tersimpan 15/09/26 07:25 UTC). Cara membuat entri Changelog bertanggal tetap dengan Modified By pengguna lain tidak disebut TC, PRD, atau LLD: disediakan tim FE/BE. Entri log audit lain pada Company Changelog tidak dihapus dan tidak diasersi (audit trail permanen, S-12); spec ini tidak menambah entri Changelog. Entri Changelog tidak bisa dihapus.
- Precondition TC-FA-CAID-177, TC-FA-CAID-178, TC-FA-CAID-179, TC-FA-CAID-180 (kecuali dinyatakan lain di butir berikut): login sebagai Total Control; Company Changelog dengan entri seed L1 sampai L7 (Pre-setup No 15); General Settings Date Format `dd/MM/yy` dan Time Format 24 jam; berada di Fixed Asset > Settings > Asset Master > Custom Asset ID.
- Kemampuan teknis: hover icon Filter untuk membaca tooltip; memilih rentang tanggal pada date range picker; membuka dropdown multi-select searchable, memilih opsi, dan mengetik pada kotak search di dalam dropdown.
- State global yang dipulihkan: tidak ada (Filter dibersihkan lewat langkah penghubung; spec hanya membaca).
- Suite serial (`parallel: false`) karena Company Changelog dan preferensi kolom browser dipakai bersama spec Modal Changelog lain dan sebagian spec mengubah state General Settings.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.

## Test Steps

### TC-FA-CAID-177: Screening Filter Panel Modal Changelog

1. Klik tombol `[Changelog]` pada header kartu
2. Hover icon Filter
3. Verifikasi tooltip `Filter` tampil
4. Klik icon Filter
5. Verifikasi panel muncul di bawah toolbar modal
6. Verifikasi icon Filter berubah gelap
7. Verifikasi field pertama `Date`: date range picker dengan placeholder `Select date`
8. Verifikasi field kedua `Action`: multi-select searchable dengan placeholder `All actions`
9. Verifikasi field ketiga `Field`: multi-select searchable dengan placeholder `All fields`
10. Verifikasi field keempat `Modified By`: multi-select searchable dengan placeholder `All users`
11. Verifikasi tombol `[Clear Field]` di kiri dan `[Apply]` di kanan
12. Verifikasi tidak ada field untuk `Old Value` dan `New Value`

### TC-FA-CAID-178: Filter Date rentang tanggal inklusif

13. Pilih rentang `12/09/26` sampai `13/09/26` pada field `Date`
14. Klik `[Apply]`
15. Verifikasi rentang 12 sampai 13 September: tabel menampilkan L3 dan L4 (batas awal dan akhir inklusif)
16. Verifikasi baris L1, L2, L5, L6, L7 tidak tampil
17. Klik icon Filter, pilih rentang satu hari `14/09/26` sampai `14/09/26` pada field `Date`, klik `[Apply]`
18. Verifikasi rentang satu hari 14 September: tabel menampilkan L2
19. Verifikasi baris L1, L3, L4, L5, L6, L7 tidak tampil

### TC-FA-CAID-179: Filter dropdown Action, Field, dan Modified By: opsi DISTINCT dari data tabel dan logika OR dalam satu field

20. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
21. Klik icon Filter
22. Buka dropdown `Action`
23. Verifikasi opsi `Action`: `Create`, `Edit`
24. Verifikasi dropdown `Action` memiliki kotak search di dalamnya
25. Buka dropdown `Field`
26. Verifikasi opsi `Field`: `Segments Formula`, `Separator`, `Status`
27. Verifikasi dropdown `Field` memiliki kotak search di dalamnya
28. Buka dropdown `Modified By`
29. Verifikasi opsi `Modified By`: `Budi S`, `Rina P`, `Sarah J`
30. Verifikasi dropdown `Modified By` memiliki kotak search di dalamnya
31. Verifikasi tidak ada opsi `Modified By` untuk pengguna yang belum pernah tercatat: daftar opsi hanya memuat `Budi S`, `Rina P`, dan `Sarah J`
32. Pilih `Separator` dan `Status` pada `Field`, klik `[Apply]`
33. Verifikasi setelah Apply `Separator` dan `Status`: tabel menampilkan L1, L2, L3, L4, L6, L7 (OR dalam satu field)
34. Verifikasi baris L5 tidak tampil
35. Klik icon Filter, buka dropdown `Field`, lalu ketik `sep` pada kotak search di dalamnya
36. Verifikasi daftar opsi `Field` menyempit menjadi `Separator`

### TC-FA-CAID-180: Filter beberapa field berlogika AND

37. Klik `[Clear Field]`, lalu klik `[Apply]`
38. Klik icon Filter, pilih `Edit` pada `Action` dan `Status` pada `Field`, klik `[Apply]`
39. Verifikasi tabel menampilkan L2 dan L3 (irisan Action `Edit` dan Field `Status`)
40. Verifikasi baris L1, L4, L5, L6, L7 tidak tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti TC sumber (177, 178, 179, 180). Modal Changelog dibuka sekali di langkah 1 untuk keempat TC.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 20 dan 37 (membersihkan Filter dari TC sebelumnya; langkah 37 dijalankan pada panel yang masih terbuka dari langkah sebelumnya). Langkah "Klik icon Filter" sebelum memilih opsi membuka kembali panel yang ditutup `[Apply]`.
- Asersi ketiadaan baris (L5, L1 dan lainnya) didahului `Verifikasi` baris yang tampil pada surface yang sama sebagai anchor positif (bagian 8b butir 2); Expected TC-FA-CAID-178, 179, dan 180 menyebut "saja", "tidak menampilkan", atau OR/AND sehingga ketiadaan itu diasersi.
- Pembagian TC lintas spec: chip dan kombinasi Search dengan Filter (TC-FA-CAID-181 sampai 184) ada di spec 070; Clear Field, draft, dan badge (TC-FA-CAID-185 sampai 189) ada di spec 071; Filter independen Column Visibility, kolom tanpa filter, dan filter tanpa hasil (TC-FA-CAID-190, 191, 229) ada di spec 072.
- Spec melewati sekitar 35 langkah (40 langkah) karena TC-FA-CAID-177 memuat tiga zona dengan satu `Verifikasi` per field dan elemen (S-01) dan TC-FA-CAID-179 membuka tiga dropdown dengan opsi dan kotak search masing-masing; semua blok satu kelas harness (Filter Panel Modal Changelog fungsional read-only), satu akun, satu dataset, dan tiap blok berdiri sendiri karena Filter dibersihkan di langkah penghubung.
- Dataset Company Changelog (seed L1 sampai L7) dan harness (FE+BE) sama dengan spec 066 sampai 068, 070 sampai 072, dan 079. Filter Modal Changelog tidak digabung ke satu spec dengan spec 070, 071, dan 072 karena gabungan langkah spec 069 (40), 070 (25), 071 (34), dan 072 (14) melewati batas sekitar 35 langkah per spec (bagian 3 prinsip 13, smell).
- Temuan untuk QA: (1) TC-FA-CAID-179 Expected a "tidak ada opsi untuk pengguna yang belum pernah tercatat" tidak menyebut pengguna konkret; spec mengasersi bahwa daftar opsi `Modified By` hanya memuat tiga pengguna seed. (2) TC-FA-CAID-178 langkah 5 "Buka lagi panel" dan TC-FA-CAID-189 langkah 3 "Tutup panel Filter" menyiratkan perilaku panel sesudah `[Apply]` yang berbeda (menutup atau tetap terbuka); spec mengikuti panel menutup setelah `[Apply]`. (3) Kolom ACC dan akun Company Changelog: lihat Temuan spec 066.
