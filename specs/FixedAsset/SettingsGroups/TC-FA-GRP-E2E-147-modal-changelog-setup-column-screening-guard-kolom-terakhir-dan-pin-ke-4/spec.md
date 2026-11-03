---
id: TC-FA-GRP-E2E-147-modal-changelog-setup-column-screening-guard-kolom-terakhir-dan-pin-ke-4
title: "Modal Changelog Setup Column: Screening Overlay dan Popup, Guard Kolom Terakhir, dan Pin ke-4 Diblok"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-483
  - TC-FA-GRP-484
  - TC-FA-GRP-506
  - TC-FA-GRP-1088
coverage:
  web: automated
---

# Modal Changelog Setup Column: Screening Overlay dan Popup, Guard Kolom Terakhir, dan Pin ke-4 Diblok

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-147`, bagian 5), dibuat lewat API di hook `before` oleh akun aktor (`ModA` untuk aksi aktor Total Control Pre-setup No 1, `ModB` dan `ModC` untuk dua user lain; akun `ModB` dan `ModC` tidak tertulis di Pre-setup TC dan disediakan tim FE). Seeding terbagi tiga batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar kolom Date punya tiga nilai distinct. Group `Log1 {runId}-147` sampai `Log4 {runId}-147` adalah group level 1; Description awal group `Log2 {runId}-147` dan `Log3 {runId}-147` = `Edit me`; Function awal `Log1` dan `Log2` = `None`, `Log3` = `Assignable`. Entri hasil seeding dipakai sebagai "Example Data" Changelog (>= 12 entri variasi Action/Field); nilai tampilan `ModA`, `ModB`, `ModC` (format `[First Name] [Last Initial]`) dan nama lengkapnya dibaca sebelum uji:

| # | Action | Group Name | Field | Old Value | New Value | Modified By | Batch seeding |
|---:|---|---|---|---|---|---|:---:|
| 1 | Create | `Log1 {runId}-147` | Group Name | `—` | `Log1 {runId}-147` | ModA | 1 |
| 2 | Create | `Log2 {runId}-147` | Group Name | `—` | `Log2 {runId}-147` | ModA | 1 |
| 3 | Create | `Log3 {runId}-147` | Group Name | `—` | `Log3 {runId}-147` | ModB | 1 |
| 4 | Create | `Log4 {runId}-147` | Group Name | `—` | `Log4 {runId}-147` | ModB | 1 |
| 5 | Edit | `Log2 {runId}-147` | Function | `None` | `Assignable` | ModA | 2 |
| 6 | Edit | `Log2 {runId}-147` | Description | `Edit me` | `Updated notes` | ModA | 2 |
| 7 | Edit | `Log2 {runId}-147` | Code | `LA147` | `LB147` | ModA | 2 |
| 8 | Edit | `Log3 {runId}-147` | Function | `Assignable` | `None` | ModB | 2 |
| 9 | Edit | `Log3 {runId}-147` | Description | `Edit me` | `Updated notes` | ModB | 3 |
| 10 | Edit | `Log3 {runId}-147` | Code | `LC147` | `LD147` | ModB | 3 |
| 11 | Delete | `Log4 {runId}-147` | Group Name | `Log4 {runId}-147` | `—` | ModB | 3 |
| 12 | Edit | `Log1 {runId}-147` | Function | `None` | `Assignable` | ModC | 3 |
  - Changelog adalah audit trail permanen: jumlah total entri tidak diasersi; tabel dibatasi Search suffix spec sehingga hanya 12 entri di atas yang teramati (10 entri di halaman 1, 2 entri di halaman 2).
  - Entri permanen tidak dihapus; cleanup (hook `after`, tidak berasumsi seeding berhasil penuh) menghapus lewat API group `Log1 {runId}-147` sampai `Log4 {runId}-147` bila masih ada dan preferensi kolom Setup Column di browser (kemampuan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE): viewport browser disesuaikan sehingga tabel Modal Changelog dapat di-scroll horizontal, dan penghapusan preferensi kolom Setup Column di browser (hook `after`, bagian 4).

## Test Steps

1. Klik icon Changelog

### TC-FA-GRP-483: Screening Overlay Column Visibility

2. Hover icon `⋯` di header kolom terakhir tabel modal
3. Verifikasi tooltip `Column Visibility` tampil
4. Klik icon `⋯` di header kolom terakhir tabel modal
5. Verifikasi item `Setup Column...` tampil di bagian bawah panel overlay
6. Verifikasi daftar kolom berurutan Date, Action, Group Name, Field, Old Value, New Value, Modified By, masing-masing Hideable dengan checkbox tercentang dan aktif
7. Verifikasi tiap baris kolom punya drag handle

### TC-FA-GRP-484: Screening Popup Setup Column

8. Klik `Setup Column...`
9. Verifikasi Header popup: title `Setup Column`, teks panduan drag/check/pin, dan icon close (X)
10. Verifikasi Body: daftar kolom Date, Action, Group Name, Field, Old Value, New Value, Modified By, masing-masing tercentang dan aktif, dengan drag handle dan icon Pin
11. Verifikasi Live Preview menampilkan header kolom dan sel data sesuai tabel asli
12. Verifikasi Footer: [Reset to Default] (text, primary) dan [Save] (filled, success)
13. Verifikasi tidak ada tombol [Cancel] pada footer

### TC-FA-GRP-506: Guard kolom terakhir yang visible

14. Hilangkan centang kolom Date
15. Hilangkan centang kolom Action
16. Hilangkan centang kolom Group Name
17. Hilangkan centang kolom Field
18. Hilangkan centang kolom Old Value
19. Hilangkan centang kolom New Value
20. Hover checkbox kolom `Modified By` yang tersisa
21. Verifikasi checkbox kolom `Modified By` disabled (tetap tampil)
22. Verifikasi tooltip `At least one column must remain visible.` tampil
23. Klik [Reset to Default]

### TC-FA-GRP-1088: Pin ke-4 diblok setelah tiga kolom terpin

24. Klik icon Pin kolom Date
25. Klik icon Pin kolom Action
26. Klik icon Pin kolom Group Name
27. Verifikasi kolom Date, Action, dan Group Name berstatus terpin
28. Hover icon Pin kolom Field
29. Verifikasi icon Pin kolom Field disabled (tidak dapat diklik, kolom tidak beku)
30. Verifikasi tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.` tampil
31. Klik icon Pin kolom Group Name untuk unpin
32. Hover icon Pin kolom Field
33. Verifikasi icon Pin kolom Field kembali aktif
34. Klik icon close (X) pada header popup
35. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka dan menutup Modal Changelog, menghilangkan centang kolom sampai tersisa satu, [Reset to Default] untuk memulihkan susunan antar TC, dan menutup popup lewat icon close (X) tanpa [Save] (S-03, S-09). Kolom yang tersisa pada TC-FA-GRP-506 adalah `Modified By` (kolom terakhir), ditentukan spec.
- Keadaan awal "belum ada kolom yang terpin" pada TC-FA-GRP-1088 dipenuhi oleh [Reset to Default] pada akhir TC-FA-GRP-506 dan hook `after` yang menghapus preferensi kolom.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Rujukan "Example Data" dan "Tabel Data Uji" Changelog pada Precondition TC tidak punya data konkret; spec mendefinisikan 12 entri seeding sendiri di Prerequisites (Action Create/Edit/Delete; Field Group Name/Function/Description/Code). Entri Marked as Excess dan Restored from Excess hanya dipakai pada spec 132.
  - Changelog adalah audit trail permanen sehingga N total tidak dapat diturunkan dari seeding (bagian 8b butir 10); spec memakai Search suffix dan selisih terhadap data milik spec. Akun `ModB` dan `ModC` (dua user lain sebagai pelaku seeding) disediakan tim FE.
  - TC Setup Column tidak menyebut lebar viewport; asersi pin (sticky saat scroll horizontal) mensyaratkan tabel modal dapat di-scroll horizontal, sehingga viewport disesuaikan (Prerequisites).
