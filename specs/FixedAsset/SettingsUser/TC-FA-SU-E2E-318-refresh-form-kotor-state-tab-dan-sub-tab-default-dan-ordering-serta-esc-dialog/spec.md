---
id: TC-FA-SU-E2E-318-refresh-form-kotor-state-tab-dan-sub-tab-default-dan-ordering-serta-esc-dialog
title: "Refresh Form Kotor dan Esc Dialog Downgrade"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1021
  - TC-FA-SU-1032
coverage:
  web: automated
---

# Refresh Form Kotor dan Esc Dialog Downgrade

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21), penugasan peran (#23), Transaction Role (#39). Target: Wawan Setiawan (Group Role Manage files) dan Mira Anggraini (Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting).
- Nama pengguna dan grup Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Penanganan dialog `beforeunload` browser (konfirmasi bawaan browser dibatalkan lalu form ditutup lewat `✕` dan `[Leave]`, S-08): disediakan tim FE.
- State global dan pemulihan: tidak ada state global yang diubah dan tidak ada data yang diubah karena semua perubahan form dibuang lewat `[Leave]`, sehingga tidak ada pemulihan. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1021: Refresh atau tutup tab saat form kotor

1. Ketik Search `Wawan`, tekan Enter, klik nama Wawan Setiawan, lalu buka Tab Role > Sub-tab Group Role
2. Buka popup Assign Group Role Manage files dan ubah satu centang (Delete pada Branch Surabaya)
3. Tekan F5
4. Verifikasi konfirmasi bawaan browser (`beforeunload`) tampil
5. Batalkan konfirmasi bawaan browser (tetap di halaman)
6. Klik `✕` pada popup Assign Group Role
7. Verifikasi dialog `Unsaved Changes` tampil
8. Klik `[Leave]`
9. Buka Sub-tab Transaction Role, klik `[+ Assign]`, dan pilih satu Group pada modal Assign Transaction Role
10. Tekan F5
11. Verifikasi konfirmasi bawaan browser (`beforeunload`) tampil
12. Batalkan konfirmasi bawaan browser (tetap di halaman)
13. Klik `✕` pada modal Assign Transaction Role
14. Verifikasi dialog `Unsaved Changes` tampil
15. Klik `[Leave]`
16. Tekan F5 tanpa perubahan pada form
17. Verifikasi Breadcrumb halaman Detail tampil sesudah halaman dimuat ulang
18. Verifikasi tidak ada konfirmasi bawaan browser yang muncul saat refresh tanpa perubahan

### TC-FA-SU-1032: Dialog Downgrade di atas modal Assign Transaction Role: Esc menutup lapisan teratas saja

19. Kembali ke User List, ketik Search `Mira`, tekan Enter, klik nama Mira Anggraini, lalu buka Tab Role > Sub-tab Transaction Role
20. Klik `[+ Assign]` dan isi Disposal × Monitoring & Report untuk Finance & Accounting
21. Klik `[Submit]`
22. Verifikasi dialog `Change Transaction Role` tampil
23. Tekan Esc
24. Verifikasi dialog `Change Transaction Role` tertutup
25. Verifikasi modal Assign Transaction Role tetap terbuka dengan isian utuh (Disposal × Monitoring & Report untuk Finance & Accounting)
26. Klik `✕` pada modal Assign Transaction Role
27. Verifikasi dialog `Unsaved Changes` tampil
28. Klik `[Leave]`
29. Verifikasi tidak ada perubahan tersimpan: Sub-tab Transaction Role Mira Anggraini tetap memuat Disposal × Staff pada Finance & Accounting dan tidak memuat Disposal × Monitoring & Report

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Form dirty ditutup deterministik (S-08): `✕`, `Verifikasi` dialog `Unsaved Changes`, `[Leave]`. Refresh (F5) saat form dirty hanya dibatalkan pada konfirmasi bawaan browser, lalu form ditutup lewat `✕`; kemampuan dicatat di Prerequisites.
- Spec 351 memuat TC-FA-SU-1025 dan 1026 (state tab dan sub-tab Detail, default dan ordering).
- Langkah penghubung (tanpa awalan `Verifikasi` dan bukan asersi, S-03): langkah 1, 19.
- Temuan untuk QA:
  - TC-FA-SU-1021 tidak menyebut pengguna target, Group Role, ataupun Group yang dipilih; spec memakai Wawan Setiawan (Manage files, Delete pada Branch Surabaya) dan satu Group pada modal Assign Transaction Role.
  - TC-FA-SU-1032 tidak menyebut pengguna target; spec memakai Mira Anggraini (Disposal × Staff pada Finance & Accounting) agar Disposal × Monitoring & Report memicu dialog `Change Transaction Role`; bila urutan tangga berbeda, tim FE menetapkan target lain.
  - Expected b TC-FA-SU-1032 ("Tidak ada perubahan tersimpan") tidak punya langkah observasi; spec membaca Sub-tab Transaction Role sesudah form ditutup.
