---
id: TC-GS-DIV-E2E-036-selection-limit-checkbox-dan-select-all
title: "Selection Limit: Checkbox Disabled dan Select All Dibatasi"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-DIV-129
  - TC-GS-DIV-130
coverage:
  web: automated
---

# Selection Limit: Checkbox Disabled dan Select All Dibatasi

## Prerequisites

- Mode: FE+BE. Kelas fungsional dengan state limit sebagai pemicu (Selection Limit diatur 5 di hook `before`). Spec hanya memilih baris dan tidak menekan aksi yang menghapus; tidak ada data Division diubah atau dihapus.
- Akun aktor: Total Control (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login akun aktor dan navigasi ke Global Settings > User > Division dilakukan di hook `before` spec ini (seedSession, kredensial dari env var). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Environment variable: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- State global yang diubah: Selection Limit entitas diset 5 lewat Admin Console > Plans & Licensing > Lifecycle Settings > System Limits. Hook `before` membaca nilai awal lalu mengubahnya menjadi 5; hook `after` mengembalikannya ke nilai awal yang dibaca (tetap jalan walau spec gagal). Kemampuan mengubah dan memulihkan System Limits disediakan tim FE (TC tidak memberi akun atau caranya). Suite berjalan serial (`parallel: false`) karena state global ini.
- Data Pre-setup (tetap di environment, tidak diubah): 6 Division.
- Data dinamis: Population D-02 (26 Division literal `Accounting` sampai `Warehouse`, setara TC-GS-DIV-30; nama literal tanpa suffix karena asersi bergantung pada total 32 baris pada `Select All (32 records)`; pengecualian S-12). Seeding lewat API di hook `before`, idempotent: nama yang sudah ada dilewati, dan cleanup di hook `after` hanya menghapus Division yang dibuat hook `before` spec ini. Fixture belum ada; tim FE menyiapkan kunci `populationD02`. Total tabel harus 32 baris tanpa filter (6 Pre-setup + 26 Population) saat spec berjalan.
- Page size tabel default 10.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Cleanup di hook `after`: pulihkan Selection Limit, hapus Division Population yang dibuat hook `before`, bersihkan seleksi tabel. Hook `beforeEach`: tutup dialog, dropdown, atau toast yang terbuka lalu kembali ke Global Settings > User > Division.

## Test Steps

### TC-GS-DIV-129: Selection Limit, checkbox melewati batas disabled saat dicentang satu per satu

1. Centang checkbox baris ke-1
2. Centang checkbox baris ke-2
3. Centang checkbox baris ke-3
4. Centang checkbox baris ke-4
5. Centang checkbox baris ke-5
6. Verifikasi baris ke-1 sampai ke-5 tercentang
7. Verifikasi Bulk Action Bar tetap aktif
8. Coba centang checkbox baris ke-6
9. Verifikasi checkbox baris ke-6 disabled
10. Hover checkbox baris ke-6
11. Verifikasi tooltip `You've reached the maximum selection of 5 rows.`
12. Klik icon `(✕)` pada Bulk Action Bar

### TC-GS-DIV-130: Selection Limit, Select All di-cap ke batas dengan toast error persist

13. Centang checkbox baris ke-1
14. Klik `Select All (32 records)`
15. Verifikasi seleksi di-cap ke 5 baris pertama: baris ke-1 sampai ke-5 tercentang
16. Verifikasi tidak ada dialog yang tampil
17. Verifikasi toast error `Error, only the first 5 of 32 rows were selected. Narrow your filter to include the rest.`
18. Verifikasi toast error tetap tampil dan tidak hilang otomatis (persist)
19. Verifikasi Bulk Action Bar tetap tampil
20. Verifikasi counter `5 Divisions selected`
21. Klik tombol `Bulk Action`
22. Verifikasi dropdown `Bulk Action` memuat aksi `Delete` (Bulk Action Bar dapat dipakai untuk 5 baris)
23. Tutup dropdown `Bulk Action` tanpa memilih aksi
24. Klik icon `(✕)` pada Bulk Action Bar
25. Tutup toast error persist

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`. Kelas fungsional dengan state limit sebagai pemicu (Selection Limit diatur 5 di hook `before`).
- Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): 12 dan 24 (membersihkan seleksi), 13 (mencentang satu baris supaya Bulk Action Bar dengan tombol `Select All (32 records)` tampil; TC-130 sumber langsung menekan `Select All (32 records)` tanpa langkah yang memunculkan bar), 21 dan 23 (membuka dan menutup dropdown `Bulk Action` untuk mengamati bar dapat dipakai), 25 (menutup toast persist).
- Asersi tambahan: langkah 22 adalah bentuk konkret "dapat dipakai untuk 5 baris" butir c TC-130, ditulis sebagai aksi `Delete` tersedia di dropdown (tanpa menekannya).
- Tidak ada aksi yang menghapus data di spec ini.
- Temuan untuk QA:
  - TC-129 dan TC-130 mensyaratkan Selection Limit 5 lewat Admin Console > Plans & Licensing > Lifecycle Settings > System Limits, tanpa menyebut akun, entitas, atau cara mengubah dan memulihkannya; nilai awal Selection Limit tidak disebut. Spec membaca nilai awal di hook `before` dan memulihkannya di `after`.
  - TC-130 langkah 1 menekan `Select All (32 records)` tanpa langkah yang memunculkan Bulk Action Bar; spec menambah satu langkah mencentang satu baris.
  - TC-129 dan TC-130 tidak menyebut baris mana yang dicentang; spec memakai urutan tampil pada halaman 1.
  - TC-129 dan TC-130 tanpa Post Condition.
