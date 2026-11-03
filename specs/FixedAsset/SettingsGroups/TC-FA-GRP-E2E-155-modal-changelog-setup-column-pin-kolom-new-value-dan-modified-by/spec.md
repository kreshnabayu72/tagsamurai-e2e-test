---
id: TC-FA-GRP-E2E-155-modal-changelog-setup-column-pin-kolom-new-value-dan-modified-by
title: "Modal Changelog Setup Column: Pin Kolom New Value dan Modified By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-504
  - TC-FA-GRP-505
coverage:
  web: automated
---

# Modal Changelog Setup Column: Pin Kolom New Value dan Modified By

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-155`, bagian 5), dibuat lewat API di hook `before` oleh akun aktor (`ModA` untuk aksi aktor Total Control Pre-setup No 1, `ModB` dan `ModC` untuk dua user lain; akun `ModB` dan `ModC` tidak tertulis di Pre-setup TC dan disediakan tim FE). Seeding terbagi tiga batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar kolom Date punya tiga nilai distinct. Group `Log1 {runId}-155` sampai `Log4 {runId}-155` adalah group level 1; Description awal group `Log2 {runId}-155` dan `Log3 {runId}-155` = `Edit me`; Function awal `Log1` dan `Log2` = `None`, `Log3` = `Assignable`. Entri hasil seeding dipakai sebagai "Example Data" Changelog (>= 12 entri variasi Action/Field); nilai tampilan `ModA`, `ModB`, `ModC` (format `[First Name] [Last Initial]`) dan nama lengkapnya dibaca sebelum uji:

| # | Action | Group Name | Field | Old Value | New Value | Modified By | Batch seeding |
|---:|---|---|---|---|---|---|:---:|
| 1 | Create | `Log1 {runId}-155` | Group Name | `—` | `Log1 {runId}-155` | ModA | 1 |
| 2 | Create | `Log2 {runId}-155` | Group Name | `—` | `Log2 {runId}-155` | ModA | 1 |
| 3 | Create | `Log3 {runId}-155` | Group Name | `—` | `Log3 {runId}-155` | ModB | 1 |
| 4 | Create | `Log4 {runId}-155` | Group Name | `—` | `Log4 {runId}-155` | ModB | 1 |
| 5 | Edit | `Log2 {runId}-155` | Function | `None` | `Assignable` | ModA | 2 |
| 6 | Edit | `Log2 {runId}-155` | Description | `Edit me` | `Updated notes` | ModA | 2 |
| 7 | Edit | `Log2 {runId}-155` | Code | `LA155` | `LB155` | ModA | 2 |
| 8 | Edit | `Log3 {runId}-155` | Function | `Assignable` | `None` | ModB | 2 |
| 9 | Edit | `Log3 {runId}-155` | Description | `Edit me` | `Updated notes` | ModB | 3 |
| 10 | Edit | `Log3 {runId}-155` | Code | `LC155` | `LD155` | ModB | 3 |
| 11 | Delete | `Log4 {runId}-155` | Group Name | `Log4 {runId}-155` | `—` | ModB | 3 |
| 12 | Edit | `Log1 {runId}-155` | Function | `None` | `Assignable` | ModC | 3 |
  - Changelog adalah audit trail permanen: jumlah total entri tidak diasersi; tabel dibatasi Search suffix spec sehingga hanya 12 entri di atas yang teramati (10 entri di halaman 1, 2 entri di halaman 2).
  - Entri permanen tidak dihapus; cleanup (hook `after`, tidak berasumsi seeding berhasil penuh) menghapus lewat API group `Log1 {runId}-155` sampai `Log4 {runId}-155` bila masih ada dan preferensi kolom Setup Column di browser (kemampuan disediakan tim FE).
- Lebar viewport 900px sehingga tabel Modal Changelog dapat di-scroll horizontal; viewport disetel pada langkah 2 dan dipulihkan pada langkah 19.
- Kemampuan teknis (disediakan tim FE): penghapusan preferensi kolom Setup Column di browser (hook `after`, bagian 4).
- Parameter iterasi TC-FA-GRP-504, 505, urutan baris = urutan iterasi:

| Kolom |
|---|
| New Value |
| Modified By |

## Test Steps

1. Klik icon Changelog
2. Setel lebar viewport 900px

### TC-FA-GRP-504 dan 505: Pin kolom New Value dan Modified By (iterasi per kolom)

3. Untuk setiap baris tabel parameter iterasi (langkah 4 sampai 17): jalankan langkah berikut dengan kolom pada baris itu
4. Buka Popup Setup Column pada Modal Changelog: klik icon `⋯` di header kolom terakhir tabel modal, lalu klik `Setup Column...`
5. Klik icon Pin kolom pada baris tabel
6. Klik [Save]
7. Scroll tabel modal secara horizontal
8. Verifikasi kolom pada baris tabel membeku (sticky) saat tabel modal di-scroll horizontal
9. Muat ulang halaman (F5)
10. Klik icon Changelog
11. Scroll tabel modal secara horizontal
12. Verifikasi kolom pada baris tabel masih membeku (pin bertahan setelah F5)
13. Buka Popup Setup Column pada Modal Changelog: klik icon `⋯` di header kolom terakhir tabel modal, lalu klik `Setup Column...`
14. Klik icon Pin kolom pada baris tabel untuk unpin
15. Klik [Save]
16. Scroll tabel modal secara horizontal
17. Verifikasi kolom pada baris tabel kembali ikut ter-scroll
18. Klik icon close (X) pada header Modal Changelog
19. Pulihkan lebar viewport

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Pengulangan (bagian 8b butir 7): langkah 4 sampai 17 diulang untuk tiap baris tabel parameter iterasi (New Value/Modified By): 14 langkah per iterasi.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka Modal Changelog dan Popup Setup Column (icon `⋯` > `Setup Column...`), [Reset to Default] + [Save] untuk memulihkan susunan default antar iterasi, dan membuka kembali Modal Changelog setelah F5 karena F5 menutup modal (S-03, S-09). Pemulihan akhir preferensi kolom: hook `after` menghapus preferensi kolom di browser (bagian 4).
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Rujukan "Example Data" dan "Tabel Data Uji" Changelog pada Precondition TC tidak punya data konkret; spec mendefinisikan 12 entri seeding sendiri di Prerequisites (Action Create/Edit/Delete; Field Group Name/Function/Description/Code). Entri Marked as Excess dan Restored from Excess hanya dipakai pada spec 132.
  - Changelog adalah audit trail permanen sehingga N total tidak dapat diturunkan dari seeding (bagian 8b butir 10); spec memakai Search suffix dan selisih terhadap data milik spec. Akun `ModB` dan `ModC` (dua user lain sebagai pelaku seeding) disediakan tim FE.
  - TC Setup Column tidak menyebut lebar viewport; asersi pin (sticky saat scroll horizontal) mensyaratkan tabel modal dapat di-scroll horizontal, sehingga spec menyetel lebar viewport 900px (langkah 2) dan memulihkannya (langkah 19), pola spec 186.
