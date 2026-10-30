---
id: TC-GS-USER-E2E-053-bulk-selection-limit-checkbox-dan-select-all
title: "Selection Limit Bulk Action: Checkbox Melewati Batas Disabled, Select All Dibatasi dengan Toast Error Persist, dan Nilai Dibaca Live"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-282
  - TC-GS-USER-283
  - TC-GS-USER-284
coverage:
  web: automated
---

# Selection Limit Bulk Action: Checkbox Melewati Batas Disabled, Select All Dibatasi dengan Toast Error Persist, dan Nilai Dibaca Live

## Prerequisites

- Mode: FE+BE. Kelas harness: volume atau limit (Selection Limit 3, lalu 4). Spec hanya memilih baris dan tidak menekan aksi yang mengubah atau menghapus data.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User); hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- State global yang diubah: Selection Limit entitas di Admin Console > Lifecycle Settings > System Limits. Hook `before` membaca nilai awal lalu mengubahnya menjadi 3; langkah 22 mengubahnya menjadi 4; hook `after` mengembalikannya ke nilai awal yang dibaca (tetap jalan walau spec gagal). Kemampuan membaca, mengubah, dan memulihkan System Limits (termasuk akun pelaku dan tab Admin Console) disediakan tim FE (TC tidak memberi akun atau caranya). Suite berjalan serial (`parallel: false`) karena state global ini.
- Data Pre-setup (Tabel Data Uji Pre-setup No. 10-22) tidak dipakai dan tidak diubah.
- Data Dinamis, 9 user milik spec, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD): `Batas Seleksi 01 {runId}-053` sampai `Batas Seleksi 09 {runId}-053`, Activated, Active, Division `Finance`, Access `Fixed Asset`, email `batasseleksi<NN>+{runId}-053@qwertysystem.net`. Dengan Search `{runId}-053`, tabel menampilkan 9 baris pada satu halaman (halaman 10 baris) dengan urutan default Name A-Z; tombol Select All menampilkan `Select All (9 records)`.
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): pulihkan Selection Limit, hapus 9 user seed lewat API, bersihkan seleksi, tutup toast, dan kosongkan Search.
- State global lain: tidak ada.

## Test Steps

### Persiapan

1. Klik icon Search, ketik `{runId}-053`, tekan Enter

### TC-GS-USER-282: Selection Limit, centang baris ke-(limit+1) disabled dengan tooltip

2. Centang baris ke-1
3. Centang baris ke-2
4. Centang baris ke-3
5. Verifikasi baris ke-1 sampai ke-3 tercentang
6. Verifikasi Bulk Action Bar tetap aktif
7. Verifikasi checkbox baris ke-4 sampai ke-9 tampil namun disabled
8. Hover checkbox baris ke-4
9. Verifikasi tooltip `You've reached the maximum selection of 3 rows.`
10. Klik icon `×` pada Bulk Action Bar

### TC-GS-USER-283: Selection Limit, Select All di-cap otomatis dengan toast error persist

11. Centang baris ke-1
12. Klik `Select All (9 records)`
13. Verifikasi baris ke-1 sampai ke-3 tercentang
14. Verifikasi baris ke-4 sampai ke-9 tidak tercentang
15. Verifikasi toast error "Error, only the first 3 of 9 rows were selected. Narrow your filter to include the rest."
16. Verifikasi toast error tetap tampil dan tidak hilang otomatis (persist)
17. Klik `Bulk Action`
18. Verifikasi dropdown `Bulk Action` memuat aksi `Delete` (Bulk Action Bar dapat dipakai untuk 3 baris)
19. Tutup dropdown `Bulk Action` dengan Esc
20. Klik icon `×` pada Bulk Action Bar
21. Tutup toast error persist

### TC-GS-USER-284: Selection Limit dibaca live dari System Limits tanpa hardcode

22. Di tab Admin Console (Lifecycle Settings > System Limits) ubah Selection Limit menjadi 4
23. Kembali ke tab User List
24. Muat ulang halaman User List
25. Klik icon Search, ketik `{runId}-053`, tekan Enter
26. Centang baris ke-1
27. Centang baris ke-2
28. Centang baris ke-3
29. Centang baris ke-4
30. Verifikasi baris ke-4 tercentang
31. Verifikasi checkbox baris ke-5 disabled
32. Hover checkbox baris ke-5
33. Verifikasi tooltip `You've reached the maximum selection of 4 rows.`
34. Klik icon `×` pada Bulk Action Bar

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Kelas harness e (bagian 3 prinsip 13e): TC-GS-USER-282, 283, dan 284 bergantung pada nilai Selection Limit.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): 1 dan 25 (Search), 10, 20, dan 34 (membersihkan seleksi), 11 (mencentang satu baris supaya Bulk Action Bar dengan tombol `Select All (9 records)` tampil), 17 dan 19 (membuka dan menutup dropdown `Bulk Action`), 21 (menutup toast persist), 22 sampai 24 (mengubah Selection Limit di tab Admin Console, kembali, dan memuat ulang).
- Asersi tambahan: langkah 14 (baris ke-4 sampai ke-9 tidak tercentang) menegaskan "hanya 3 baris pertama terselect" (TC-GS-USER-283 butir a); langkah 18 adalah bentuk konkret "bar tetap bisa dipakai" (butir c), ditulis sebagai aksi `Delete` tersedia di dropdown tanpa menekannya.
- Teks tooltip diasersi tanpa tanda petik; TC menuliskannya dalam tanda petik.
- Tidak ada aksi yang mengubah atau menghapus data user di spec ini.
- Temuan untuk QA:
  - TC-GS-USER-282, 283, dan 284 mensyaratkan Selection Limit 3 (dan 4) lewat Admin Console > Lifecycle Settings > System Limits tanpa menyebut akun pelaku, nilai awal, atau cara memulihkan; spec membaca nilai awal di hook `before` dan memulihkannya di `after`.
  - TC-GS-USER-283 langkah 1 menekan `Select All (9 records)` tanpa langkah yang memunculkan bar; spec mencentang satu baris lebih dulu.
  - TC-GS-USER-283 butir c ("Bar tetap bisa dipakai") tidak menyebut cara mengamati; spec membuka dropdown `Bulk Action`.
  - TC-GS-USER-283 butir b ("toast error persist") tidak menyebut lamanya pengamatan; spec mengasersi toast masih tampil sebelum langkah berikutnya.
  - TC-GS-USER-282 dan 284 tidak menyebut baris mana yang dicentang; spec memakai urutan tampil pada halaman 1 (Name A-Z).
  - TC-GS-USER-282, 283, dan 284 tanpa Post Condition.
