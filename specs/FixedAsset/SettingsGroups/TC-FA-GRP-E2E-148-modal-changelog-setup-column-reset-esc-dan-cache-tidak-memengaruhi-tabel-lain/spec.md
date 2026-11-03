---
id: TC-FA-GRP-E2E-148-modal-changelog-setup-column-reset-esc-dan-cache-tidak-memengaruhi-tabel-lain
title: "Modal Changelog Setup Column: [Reset to Default], (X) dan Esc, dan Cache Tidak Memengaruhi Tabel Lain"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-507
  - TC-FA-GRP-508
  - TC-FA-GRP-509
coverage:
  web: automated
---

# Modal Changelog Setup Column: [Reset to Default], (X) dan Esc, dan Cache Tidak Memengaruhi Tabel Lain

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-148`, bagian 5), dibuat lewat API di hook `before` oleh akun aktor (`ModA` untuk aksi aktor Total Control Pre-setup No 1, `ModB` dan `ModC` untuk dua user lain; akun `ModB` dan `ModC` tidak tertulis di Pre-setup TC dan disediakan tim FE). Seeding terbagi tiga batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar kolom Date punya tiga nilai distinct. Group `Log1 {runId}-148` sampai `Log4 {runId}-148` adalah group level 1; Description awal group `Log2 {runId}-148` dan `Log3 {runId}-148` = `Edit me`; Function awal `Log1` dan `Log2` = `None`, `Log3` = `Assignable`. Entri hasil seeding dipakai sebagai "Example Data" Changelog (>= 12 entri variasi Action/Field); nilai tampilan `ModA`, `ModB`, `ModC` (format `[First Name] [Last Initial]`) dan nama lengkapnya dibaca sebelum uji:

| # | Action | Group Name | Field | Old Value | New Value | Modified By | Batch seeding |
|---:|---|---|---|---|---|---|:---:|
| 1 | Create | `Log1 {runId}-148` | Group Name | `—` | `Log1 {runId}-148` | ModA | 1 |
| 2 | Create | `Log2 {runId}-148` | Group Name | `—` | `Log2 {runId}-148` | ModA | 1 |
| 3 | Create | `Log3 {runId}-148` | Group Name | `—` | `Log3 {runId}-148` | ModB | 1 |
| 4 | Create | `Log4 {runId}-148` | Group Name | `—` | `Log4 {runId}-148` | ModB | 1 |
| 5 | Edit | `Log2 {runId}-148` | Function | `None` | `Assignable` | ModA | 2 |
| 6 | Edit | `Log2 {runId}-148` | Description | `Edit me` | `Updated notes` | ModA | 2 |
| 7 | Edit | `Log2 {runId}-148` | Code | `LA148` | `LB148` | ModA | 2 |
| 8 | Edit | `Log3 {runId}-148` | Function | `Assignable` | `None` | ModB | 2 |
| 9 | Edit | `Log3 {runId}-148` | Description | `Edit me` | `Updated notes` | ModB | 3 |
| 10 | Edit | `Log3 {runId}-148` | Code | `LC148` | `LD148` | ModB | 3 |
| 11 | Delete | `Log4 {runId}-148` | Group Name | `Log4 {runId}-148` | `—` | ModB | 3 |
| 12 | Edit | `Log1 {runId}-148` | Function | `None` | `Assignable` | ModC | 3 |
  - Changelog adalah audit trail permanen: jumlah total entri tidak diasersi; tabel dibatasi Search suffix spec sehingga hanya 12 entri di atas yang teramati (10 entri di halaman 1, 2 entri di halaman 2).
  - Entri permanen tidak dihapus; cleanup (hook `after`, tidak berasumsi seeding berhasil penuh) menghapus lewat API group `Log1 {runId}-148` sampai `Log4 {runId}-148` bila masih ada dan preferensi kolom Setup Column di browser (kemampuan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): viewport browser disesuaikan sehingga tabel Modal Changelog dapat di-scroll horizontal, dan penghapusan preferensi kolom Setup Column di browser (hook `after`, bagian 4).

## Test Steps

1. Klik icon Changelog

### TC-FA-GRP-507: [Reset to Default]

2. Buka Popup Setup Column pada Modal Changelog: klik icon `⋯` di header kolom terakhir tabel modal, lalu klik `Setup Column...`
3. Drag kolom Modified By ke posisi paling awal
4. Hilangkan centang kolom Old Value
5. Klik icon Pin kolom Date
6. Klik [Save]
7. Verifikasi tabel modal menampilkan urutan header Modified By, Date, Action, Group Name, Field, New Value tanpa kolom Old Value
8. Buka Popup Setup Column pada Modal Changelog: klik icon `⋯` di header kolom terakhir tabel modal, lalu klik `Setup Column...`
9. Klik [Reset to Default]
10. Verifikasi Live Preview kembali ke susunan default: urutan Date, Action, Group Name, Field, Old Value, New Value, Modified By, semua tampil dan tanpa pin
11. Klik [Save]
12. Muat ulang halaman (F5)
13. Klik icon Changelog
14. Verifikasi tabel modal kembali ke susunan default dan bertahan setelah F5: urutan header Date, Action, Group Name, Field, Old Value, New Value, Modified By

### TC-FA-GRP-508: (X) dan Esc membatalkan perubahan

15. Buka Popup Setup Column pada Modal Changelog: klik icon `⋯` di header kolom terakhir tabel modal, lalu klik `Setup Column...`
16. Hilangkan centang kolom Old Value
17. Klik icon close (X) pada header popup
18. Verifikasi popup tertutup
19. Verifikasi kolom Old Value masih tampil pada header tabel modal (perubahan tidak diterapkan)
20. Buka Popup Setup Column pada Modal Changelog: klik icon `⋯` di header kolom terakhir tabel modal, lalu klik `Setup Column...`
21. Drag kolom Modified By ke posisi paling awal
22. Tekan Esc
23. Verifikasi popup tertutup
24. Verifikasi urutan header tabel modal tetap Date, Action, Group Name, Field, Old Value, New Value, Modified By (konfigurasi tersimpan terakhir)

### TC-FA-GRP-509: Cache tidak memengaruhi tabel lain

25. Buka Popup Setup Column pada Modal Changelog: klik icon `⋯` di header kolom terakhir tabel modal, lalu klik `Setup Column...`
26. Hilangkan centang kolom New Value
27. Klik [Save]
28. Verifikasi kolom New Value hilang dari tabel modal
29. Klik icon close (X) pada header Modal Changelog
30. Verifikasi tabel Groups List tetap memuat kolom Group, Code, Function, Total Asset, Total User, Modified By, dan Last Updated (konfigurasi kolomnya sendiri)
31. Klik icon Changelog
32. Verifikasi kolom New Value masih hilang dari tabel modal (konfigurasi tersimpan)
33. Buka Popup Setup Column pada Modal Changelog: klik icon `⋯` di header kolom terakhir tabel modal, lalu klik `Setup Column...`
34. Klik [Reset to Default]
35. Klik [Save]
36. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka dan menutup Modal Changelog (termasuk membuka ulang setelah F5), membuka Popup Setup Column, serta [Clear Field] + [Apply] (S-03, S-09, R-16). Posisi drag (paling awal), kolom yang di-hide (`Old Value`, `New Value`), dan kolom yang dipin (`Date`) ditentukan spec karena TC menyebut "beberapa kolom" tanpa nama.
- Footer popup tanpa tombol [Cancel]: penutupan lewat icon close (X) dan Esc (TC-FA-GRP-508, Expected a).
- Pada TC-FA-GRP-509 "tabel lain" = Groups List; kolom Groups List diamati lewat header tabel setelah Modal Changelog ditutup.
- TC-FA-GRP-1119 berada di spec 283.
- Spec 36 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Rujukan "Example Data" dan "Tabel Data Uji" Changelog pada Precondition TC tidak punya data konkret; spec mendefinisikan 12 entri seeding sendiri di Prerequisites (Action Create/Edit/Delete; Field Group Name/Function/Description/Code). Entri Marked as Excess dan Restored from Excess hanya dipakai pada spec 132.
  - Changelog adalah audit trail permanen sehingga N total tidak dapat diturunkan dari seeding (bagian 8b butir 10); spec memakai Search suffix dan selisih terhadap data milik spec. Akun `ModB` dan `ModC` (dua user lain sebagai pelaku seeding) disediakan tim FE.
  - TC Setup Column tidak menyebut lebar viewport; asersi pin (sticky saat scroll horizontal) mensyaratkan tabel modal dapat di-scroll horizontal, sehingga viewport disesuaikan (Prerequisites).
