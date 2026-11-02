---
id: TC-FA-GRP-E2E-132-modal-changelog-group-screening-baris-excess-aktor-scoped-dan-read-only
title: "Modal Changelog Group: Screening, Baris Marked/Restored Excess, Aktor Scoped Hanya Riwayat dalam Scope, dan Total Control/Read Only/Default User Melihat Seluruh Riwayat"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-427
  - TC-FA-GRP-429
  - TC-FA-GRP-430
  - TC-FA-GRP-991
coverage:
  web: automated
---

# Modal Changelog Group: Screening, Baris Marked/Restored Excess, Aktor Scoped Hanya Riwayat dalam Scope, dan Total Control/Read Only/Default User Melihat Seluruh Riwayat

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-132`, bagian 5), dibuat lewat API di hook `before` oleh akun aktor (`ModA` untuk aksi aktor Total Control Pre-setup No 1, `ModB` dan `ModC` untuk dua user lain; akun `ModB` dan `ModC` tidak tertulis di Pre-setup TC dan disediakan tim FE). Seeding terbagi tiga batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar kolom Date punya tiga nilai distinct. Group `Log1 {runId}-132` sampai `Log4 {runId}-132` adalah group level 1; Description awal group `Log2 {runId}-132` dan `Log3 {runId}-132` = `Edit me`; Function awal `Log1` dan `Log2` = `None`, `Log3` = `Assignable`. Entri hasil seeding dipakai sebagai "Example Data" Changelog (>= 12 entri variasi Action/Field); nilai tampilan `ModA`, `ModB`, `ModC` (format `[First Name] [Last Initial]`) dan nama lengkapnya dibaca sebelum uji:

| # | Action | Group Name | Field | Old Value | New Value | Modified By | Batch seeding |
|---:|---|---|---|---|---|---|:---:|
| 1 | Create | `Log1 {runId}-132` | Group Name | `—` | `Log1 {runId}-132` | ModA | 1 |
| 2 | Create | `Log2 {runId}-132` | Group Name | `—` | `Log2 {runId}-132` | ModA | 1 |
| 3 | Create | `Log3 {runId}-132` | Group Name | `—` | `Log3 {runId}-132` | ModB | 1 |
| 4 | Create | `Log4 {runId}-132` | Group Name | `—` | `Log4 {runId}-132` | ModB | 1 |
| 5 | Edit | `Log2 {runId}-132` | Function | `None` | `Assignable` | ModA | 2 |
| 6 | Edit | `Log2 {runId}-132` | Description | `Edit me` | `Updated notes` | ModA | 2 |
| 7 | Edit | `Log2 {runId}-132` | Code | `LA132` | `LB132` | ModA | 2 |
| 8 | Edit | `Log3 {runId}-132` | Function | `Assignable` | `None` | ModB | 2 |
| 9 | Edit | `Log3 {runId}-132` | Description | `Edit me` | `Updated notes` | ModB | 3 |
| 10 | Edit | `Log3 {runId}-132` | Code | `LC132` | `LD132` | ModB | 3 |
| 11 | Delete | `Log4 {runId}-132` | Group Name | `Log4 {runId}-132` | `—` | ModB | 3 |
| 12 | Edit | `Log1 {runId}-132` | Function | `None` | `Assignable` | ModC | 3 |
  - Data tambahan spec ini (dibuat lewat API di `before`, dibersihkan di `after`): (a) group `Excess Node {runId}-132` (level 1, Assignable) yang ditandai Excess lalu dipulihkan, menghasilkan entri Marked as Excess dan Restored from Excess (Field `Excess`, Old Value `Usable` lalu `Excess`; mekanisme penandaan Excess dan pemulihan disediakan tim FE/BE; seeding batch 3); (b) group `West Child {runId}-132` di bawah `Region West`, `East Child {runId}-132` di bawah `Region East` (keduanya anak Pre-setup Tabel A), dan group level 1 `Old Storage {runId}-132` yang dibuat lalu dihapus (entri Create dan Delete, seeding batch 1).
  - Akun peran (ganti akun eksplisit): Group Manager scope Region West (`groupManagerGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 4, `Spectra.env.FA_GM_PASSWORD`); parameter iterasi TC-FA-GRP-430:

| Role | Email | Env var password |
|---|---|---|
| Read Only | `readOnlyGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 3) | `Spectra.env.FA_RO_PASSWORD` |
| Total Control | `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1) | `Spectra.env.FA_TC_PASSWORD` |
| Default User | `defaultUserGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 2) | `Spectra.env.FA_DU_PASSWORD` |
  - Changelog adalah audit trail permanen: jumlah total entri tidak diasersi; tabel dibatasi Search suffix spec sehingga hanya 12 entri di atas yang teramati (10 entri di halaman 1, 2 entri di halaman 2).
  - Entri permanen tidak dihapus; cleanup (hook `after`, tidak berasumsi seeding berhasil penuh) menghapus lewat API group `Log1 {runId}-132` sampai `Log4 {runId}-132` bila masih ada dan preferensi kolom Setup Column di browser (kemampuan disediakan tim FE).

## Test Steps

### TC-FA-GRP-427: Screening Modal Changelog: Group (Total Control)

1. Klik icon Changelog
2. Verifikasi title Modal Changelog `Changelog: Group`
3. Verifikasi toolbar memuat Search, Filter, dan Download
4. Verifikasi icon close (X) tampil pada header modal
5. Verifikasi kolom tabel berurutan Date, Action, Group Name, Field, Old Value, New Value, dan Modified By, lalu Column Visibility (`⋯`)
6. Verifikasi baris pertama tabel adalah entri seeding batch 3 (urutan default Date terbaru di atas)
7. Verifikasi footer pagination tampil
8. Ketik Search `Excess Node {runId}-132`, tekan Enter
9. Verifikasi baris Action `Marked as Excess` Group Name `Excess Node {runId}-132`: Field `Excess`, Old Value `Usable`, New Value `Excess`
10. Verifikasi baris Action `Restored from Excess` Group Name `Excess Node {runId}-132`: Field `Excess`, Old Value `Excess`, New Value `Usable`
11. Verifikasi Group Name pada baris pertama berupa teks biasa (bukan link)
12. Verifikasi nilai Modified By pada baris pertama berformat `[First Name] [Last Initial]`
13. Hover nilai Modified By pada baris pertama
14. Verifikasi hover menampilkan nama lengkap
15. Ganti isi kotak search dengan `Log1 {runId}-132`, tekan Enter
16. Verifikasi baris Action Create Group Name `Log1 {runId}-132` memiliki Old Value `—`
17. Ganti isi kotak search dengan `Log4 {runId}-132`, tekan Enter
18. Verifikasi baris Action Delete Group Name `Log4 {runId}-132` memiliki New Value `—`
19. Klik `(←)` pada kotak Search

### TC-FA-GRP-991: Baris Marked/Restored Excess

20. Ketik Search `Excess Node {runId}-132`, tekan Enter
21. Verifikasi baris Marked as Excess `Excess Node {runId}-132`: Field `Excess`, Old Value `Usable`, New Value `Excess`
22. Verifikasi baris Restored from Excess `Excess Node {runId}-132`: Field `Excess`, Old Value `Excess`, New Value `Usable`
23. Verifikasi Old Value dan New Value pada kedua baris tidak sama-sama `—`
24. Verifikasi kolom Field pada kedua baris tidak kosong
25. Klik `(←)` pada kotak Search
26. Klik icon Filter
27. Buka dropdown Field
28. Verifikasi opsi `Excess` tampil pada dropdown Field
29. Klik icon Filter untuk menutup panel
30. Klik icon close (X) pada header Modal Changelog

### TC-FA-GRP-429: Aktor scoped hanya melihat riwayat dalam scope

31. Ganti akun: logout, lalu login sebagai Group Manager scope Region West dengan `Spectra.env.FA_GM_PASSWORD`
32. Klik icon Changelog
33. Ketik Search `West Child {runId}-132`, tekan Enter
34. Verifikasi baris Group Name `Global HQ > Region West > West Child {runId}-132` tampil
35. Ganti isi kotak search dengan `East Child {runId}-132`, tekan Enter
36. Verifikasi empty state tampil dengan title `No results found` (riwayat Region East di luar scope)
37. Ganti isi kotak search dengan `Old Storage {runId}-132`, tekan Enter
38. Verifikasi empty state tampil dengan title `No results found` (node terhapus di luar scope)
39. Klik icon close (X) pada header Modal Changelog

### TC-FA-GRP-430: Total Control, Read Only, dan Default User melihat seluruh riwayat

40. Untuk setiap baris tabel Role (langkah 41 sampai 47): jalankan langkah berikut dengan akun pada baris itu
41. Ganti akun: logout, lalu login sebagai role pada baris tabel dengan env var password pada baris itu
42. Klik icon Changelog
43. Ketik Search `Old Storage {runId}-132`, tekan Enter
44. Verifikasi baris Action Delete Group Name `Old Storage {runId}-132` tampil
45. Ganti isi kotak search dengan `East Child {runId}-132`, tekan Enter
46. Verifikasi baris Group Name `Global HQ > Region East > East Child {runId}-132` tampil
47. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Spec memuat tiga akun di luar akun default suite; ganti akun punya langkah eksplisit (S-07) dan hook `after` mengembalikan sesi ke akun default suite. Spec ditulis per blok TC (bukan satu perulangan role) karena TC-FA-GRP-429 menguji aktor scoped dengan asersi berbeda dari TC-FA-GRP-430.
- Pengulangan (bagian 8b butir 7): langkah 41 sampai 47 diulang untuk tiap baris tabel Role (Read Only, Total Control, Default User).
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka dan menutup Modal Changelog, mengganti isi kotak search antar pemeriksaan, `(←)` pada kotak Search, dan menutup Filter Panel (S-03). Search per nama (`Excess Node`, `Log1`, `Log4`, `West Child`, `East Child`, `Old Storage`) dipakai agar baris yang dicek tampil di halaman 1.
- TC-FA-GRP-427 memakai node Excess, scope, dan terhapus milik spec (`Excess Node`, `West Child`, `East Child`, `Old Storage`) sebagai pengganti Warehouse B, Region West/East, dan Old Storage Pre-setup (S-06). Log Region West dan Branch West 1 pada TC-FA-GRP-429 diwakili entri `West Child`.
- Asersi "tidak tampil" (TC-FA-GRP-429 Expected b) memakai empty state `No results found` hasil Search sebagai anchor positif (bagian 8b butir 2).
- Spec 47 langkah (ekspansi iterasi ± 60 langkah), di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah per kolom/field memakai tabel di Prerequisites (bagian 8b butir 7).
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Rujukan "Example Data" dan "Tabel Data Uji" Changelog pada Precondition TC tidak punya data konkret; spec mendefinisikan 12 entri seeding sendiri di Prerequisites (Action Create/Edit/Delete; Field Group Name/Function/Description/Code). Entri Marked as Excess dan Restored from Excess hanya dipakai pada spec 132.
  - Changelog adalah audit trail permanen sehingga N total tidak dapat diturunkan dari seeding (bagian 8b butir 10); spec memakai Search suffix dan selisih terhadap data milik spec. Akun `ModB` dan `ModC` (dua user lain sebagai pelaku seeding) disediakan tim FE.
  - TC-FA-GRP-429/430 memakai Region West, Region East, dan Old Storage Pre-setup yang tidak punya entri log pada Tabel A; spec membuat entri pada anak node baru.
  - Akun peran Default User dan Read Only memakai env baru `FA_DU_PASSWORD` dan `FA_RO_PASSWORD`, serta Group Manager `FA_GM_PASSWORD`; perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
