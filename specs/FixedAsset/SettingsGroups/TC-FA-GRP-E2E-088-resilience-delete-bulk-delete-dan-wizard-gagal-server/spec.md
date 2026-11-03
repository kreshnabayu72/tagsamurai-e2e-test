---
id: TC-FA-GRP-E2E-088-resilience-delete-bulk-delete-dan-wizard-gagal-server
title: "Resilience: Delete Single, Bulk Delete, dan Simpan Wizard Gagal Server Mempertahankan State"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-GRP-243
  - TC-FA-GRP-267
  - TC-FA-GRP-307
coverage:
  web: automated
---

# Resilience: Delete Single, Bulk Delete, dan Simpan Wizard Gagal Server Mempertahankan State

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control (Pre-setup No 1: `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Intercept parsial (`Spectra.intercept()`) di atas backend nyata: respons 5xx untuk request hapus group (TC-243), request hapus massal (TC-267), dan request simpan seleksi Wizard (TC-307). Nama endpoint tidak disebut TC, PRD, atau LLD (APISpec kosong); ditentukan tim FE. Intercept dilepas segera setelah pemicu selesai (S-09).
- Data Dinamis (di-seed lewat API di `before`, kosong tanpa aset): `Del Empty` (TC-243), `Bulk E11` dan `Bulk E12` (TC-267).
- Akun TC-307 (kelas h): Total Control client Wizard (Pre-setup No 8; email dan `Spectra.env.FA_WIZ_TC_PASSWORD` disediakan tim FE, tidak tertulis di Pre-setup TC). Dipakai lewat langkah Ganti akun sebelum TC-307; akun aktor hook `before` (Total Control No 1) tidak dipakai untuk TC-307.
- State (precondition TC-307, bukan objek uji): plan dijadwalkan downgrade Professional ke Growth (cap 3), T-30 berjalan, client Wizard punya 6 group (disediakan tim FE/BE; Pre-setup No 8); Wizard Reconciliation > Step Group Consolidation. Hook `after` memulihkan plan terjadwal, seleksi tersimpan, dan status Excess lewat fixture BE (disediakan tim FE/BE), lalu mengembalikan sesi ke akun default suite.
- Cleanup di `after`: hapus sisa data milik spec lewat API.

## Test Steps

### TC-FA-GRP-243: Delete single gagal server

1. Pasang intercept: respons 5xx pada request hapus group
2. Ketik Search `{runId}-088`, tekan Enter
3. Buka elipsis `⋯` baris `Del Empty`, pilih `Delete`
4. Klik [Delete]
5. Verifikasi toast error "Error, failed to delete group."
6. Verifikasi `Del Empty` tetap ada di tabel (node tidak terhapus)
7. Lepas intercept
8. Buka elipsis `⋯` baris `Del Empty`, pilih `Delete` lagi
9. Verifikasi dialog dengan title "Delete Group" tampil kembali (dialog dapat diulang)
10. Klik [Cancel]

### TC-FA-GRP-267: Bulk Delete gagal server

11. Pasang intercept: respons 5xx pada request hapus massal
12. Centang `Bulk E11` dan `Bulk E12`
13. Buka Bulk Action, pilih `Delete`
14. Tunggu toast lama hilang otomatis
15. Klik [Delete]
16. Verifikasi toast error "Error, failed to delete group."
17. Verifikasi bar bulk action dan seleksi dipertahankan (counter `2 groups selected`)
18. Verifikasi list di-refresh dan `Bulk E11` serta `Bulk E12` tampil sesuai keadaan nyata server (tetap ada)
19. Lepas intercept, lalu klik (X)

### TC-FA-GRP-307: Simpan Wizard gagal server mempertahankan seleksi

20. Ganti akun: Logout, login sebagai Total Control client Wizard (`Spectra.env.FA_WIZ_TC_PASSWORD`), lalu buka Fixed Asset > Settings > Groups
21. Pasang intercept: respons 5xx pada request simpan seleksi Wizard
22. Buka Wizard Reconciliation > Step Group Consolidation
23. Centang 3 group
24. Klik [Save Selection]
25. Verifikasi toast error "Error, failed to update group consolidation."
26. Verifikasi centang 3 group dipertahankan
27. Lepas intercept, lalu klik [Cancel]
28. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tampil
29. Klik [Leave]

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 7, 10 dan 11, 19 sampai 22, 27, 29: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state. Langkah 14 (Tunggu toast lama hilang otomatis) memastikan toast error langkah 5 sudah hilang sebelum toast error langkah 16 diasersi (R-12).
- Pencarian baris target (S-03, R-16): langkah 2 (Ketik Search `{runId}-088`, tekan Enter) menampilkan seluruh group seed spec ini (`Del Empty`, `Bulk E11`, `Bulk E12`; satu halaman); client memiliki lebih dari 10 node level 1 dan page size 10, jadi baris target tidak dijamin berada di halaman 1 All Groups.
- Spec FE+BE dengan intercept parsial, bukan `Mode: mock`: asersi memakai state nyata server (APISpec kosong sehingga daftar endpoint mock tidak dapat dituliskan tanpa mengarang; S-13, R-15). Dua dari TC bersumber dari resilience Delete; TC-307 memakai plan terjadwal hanya sebagai precondition (kelas h bukan objek uji); pengecualian kelas h: state tenant plan downgrade terjadwal dibentuk dan dipulihkan fixture BE (disediakan tim FE/BE) pada client Wizard, bukan oleh akun aktor hook `before`, sehingga langkah 20 mengganti akun.
- Temuan untuk QA:
  - TC-243 Expected c "Dialog dapat diulang" ambigu (dialog tetap terbuka atau dapat dibuka lagi); spec mengasersi dialog Delete tampil kembali saat dibuka ulang.
  - TC-267 Expected b ("item yang sudah ter-commit tetap commit; sisanya tetap") tidak bermakna bila seluruh request dibalas 5xx; spec mengasersi keadaan nyata server lewat refresh list.
  - TC-307 tidak menyebut cara menutup step sesudah gagal; spec memakai [Cancel], dialog Unsaved Changes, dan [Leave].
