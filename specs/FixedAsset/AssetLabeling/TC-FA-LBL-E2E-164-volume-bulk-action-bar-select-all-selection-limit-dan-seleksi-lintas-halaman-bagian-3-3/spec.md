---
id: TC-FA-LBL-E2E-164-volume-bulk-action-bar-select-all-selection-limit-dan-seleksi-lintas-halaman-bagian-3-3
title: "Volume: Bulk Action Bar, Select All, Selection Limit, dan Seleksi Lintas Halaman (bagian 3/3)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-183
  - TC-FA-LBL-184
coverage:
  web: automated
---

# Volume: Bulk Action Bar, Select All, Selection Limit, dan Seleksi Lintas Halaman (bagian 3/3)

## Prerequisites

- Mode: FE+BE. Backend nyata pada Company Volume; tidak ada respons yang di-mock atau di-intercept.
- Akun aktor: Total Control Volume (Pre-setup #10, Company Volume), `Fixture.assetLabeling.akun.totalControlVolume` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`, `{namaCompany}` = nama Company Volume). Password `Spectra.env.FA_TC_VOLUME_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. `fixtures/asset-labeling.json` belum ada dan disediakan tim FE.
- Hook suite `before`, `beforeEach`, dan `after` (lihat `suite.md`) berlaku. Hook `after` spec ini mengembalikan sesi ke akun default suite (Total Control Company Alpha) dan memulihkan Selection Limit ke nilai awal.
- Data Pre-setup (hanya dibaca, tidak diubah): Company Volume (#10) dengan 120 label `Project Tag 1` sampai `Project Tag 120` (log Create tersedia). Data Dinamis: tidak ada. Page size awal tabel 10 baris.
- Selection Limit diturunkan ke 100 di System Limits, diatur di hook `before` spec ini dan dipulihkan di hook `after`. Kemampuan mengubah dan memulihkan System Limits disediakan tim FE (TC, PRD, dan LLD tidak menyebut akun pelaku perubahannya). Pada page size 100 halaman 2 berisi 20 baris.
- Kelas harness e (volume data, 120 label): spec ini hanya memuat TC volume Company Volume dan tidak memuat TC kelas harness lain.
- State global: Selection Limit di System Limits (lihat butir sebelumnya); suite berjalan serial (`parallel: false`).
- Kemampuan teknis: mencentang 100 baris satu per satu dalam satu langkah (pengulangan centang di dalam skrip).
- Jeda nyata: TC-FA-LBL-184 menunggu 5 detik sungguhan tanpa memuat ulang halaman (langkah 14) untuk memastikan toast error bertahan; durasi adalah pilihan spec (TC hanya menyebut "bertahan sampai di-dismiss"), tanpa fake timer atau intercept.

## Test Steps

### TC-FA-LBL-183: Selection Limit: checkbox ke-(limit+1) disabled dengan tooltip

1. Atur page size 100
2. Centang 100 baris satu per satu
3. Pindah ke halaman 2
4. Hover checkbox baris pertama lalu coba centang
5. Verifikasi Checkbox baris ke-101 disabled dengan tooltip `You've reached the maximum selection of 100 rows.`
6. Verifikasi 100 baris tetap tercentang
7. Verifikasi Bulk Action Bar tetap aktif
8. Klik ikon `×`

### TC-FA-LBL-184: Selection Limit: Select All di atas limit di-cap ke limit baris pertama

9. Kembali ke halaman 1
10. Centang satu baris
11. Klik `Select All (120 records)`
12. Verifikasi seleksi di-cap ke 100 baris pertama (100 baris halaman 1 tercentang) dengan counter `100 Labels selected`
13. Verifikasi toast error `Error, only the first 100 of 120 rows were selected. Narrow your filter to include the rest.` tampil
14. Tunggu 5 detik tanpa memuat ulang halaman
15. Verifikasi toast error masih tampil (bertahan sampai di-dismiss)
16. Dismiss toast error
17. Verifikasi Bulk Action Bar tetap tampil dan tombol `Bulk Action` dapat dipakai
18. Klik ikon `×`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 2 mencentang 100 baris satu per satu sebagai satu langkah karena Langkah Uji TC menyebutnya satu aksi; langkah 14 memberi jendela 5 detik sebelum asersi toast bertahan; klik ikon `×` membersihkan seleksi (S-09); kembali ke halaman 1 sebelum Select All supaya "100 baris pertama" terletak di halaman aktif.
- Jendela 5 detik pada langkah 14 adalah pilihan spec (bukan nilai TC atau PRD): TC menyebut toast "bertahan sampai di-dismiss" tanpa durasi.
- Pembagian TC lintas spec: TC-FA-LBL-178 sampai TC-FA-LBL-182 ada di spec 057 dan spec 058.
- Temuan untuk QA:
  - TC-FA-LBL-184 Expected a ("di-cap ke 100 baris pertama") tidak menyebut urutan yang dipakai untuk "pertama"; spec mengasersi 100 baris halaman 1 (page size 100) tercentang bersama counter.
  - TC-FA-LBL-184 Expected b (toast bertahan sampai di-dismiss) tidak menyebut durasi pengamatan; lihat jendela 5 detik di Notes.
