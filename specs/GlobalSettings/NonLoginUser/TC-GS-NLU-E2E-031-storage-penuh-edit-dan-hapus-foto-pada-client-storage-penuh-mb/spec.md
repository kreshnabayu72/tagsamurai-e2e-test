---
id: TC-GS-NLU-E2E-031-storage-penuh-edit-dan-hapus-foto-pada-client-storage-penuh-mb
title: "Storage penuh: Edit dan hapus foto pada Client Storage Penuh MB"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-512
  - TC-GS-NLU-513
  - TC-GS-NLU-514
coverage:
  web: automated
---

# Storage penuh: Edit dan hapus foto pada Client Storage Penuh MB

## Prerequisites

- Mode: FE+BE (backend nyata; pengecekan Storage dilakukan server berdasarkan usage ledger, dan Tab Changelog dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control pada Client PT Storage Penuh MB `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Client PT Storage Penuh MB (Tabel Data Uji Pre-setup No. 1 dan 19), password lewat `Spectra.env.GS_STORAGEMB_TC_PASSWORD`. Nama env baru yang diusulkan (belum terdaftar di `spectra.config.ts` dan `.env.example`; akun disediakan tim FE).
- Env var: `GS_STORAGEMB_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9 sampai 12 dan 19, hanya dibaca): Position `Driver` dan `Manager`, Division `Operations`, Login User `Ahmad Fauzi` (pool Represented By), Client PT Storage Penuh MB dengan kuota Storage 536870912 byte (512.0 MB) dan usage ledger 629145600 byte (600.0 MB).
- Berkas uji di perangkat uji: gambar JPG 500 KB.
- Data Dinamis milik spec, di-seed lewat API di hook `before` pada Client PT Storage Penuh MB dengan padanan Pre-setup No. 19 (record Pre-setup tidak diubah; S-06). Foto dipasang saat seeding sebelum usage ledger diatur ke 600.0 MB (mekanisme seeding dan pengaturan ledger disediakan tim FE/BE):
  - `Storage Penuh Satu {runId}-031` (First Name `Storage`, Last Name `Penuh Satu {runId}-031`, berfoto, Position `Driver`, Division `Operations`, Represented By `Ahmad Fauzi`, Active), Email `storagepenuhsatu+{runId}-031@qwertysystem.net`.
  - `Storage Penuh Dua {runId}-031` (Last Name `Penuh Dua {runId}-031`, tanpa foto, Position `Driver`), Email `storagepenuhdua+{runId}-031@qwertysystem.net`.
  - `Storage Penuh Tiga {runId}-031` (Last Name `Penuh Tiga {runId}-031`, berfoto), Email `storagepenuhtiga+{runId}-031@qwertysystem.net`.
  - Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus Non-Login User ber-Email `+{runId}-031` lewat API.
- Kemampuan teknis: membaca jumlah entri Tab Changelog Detail dengan Action `Edit` untuk `Storage Penuh Satu {runId}-031` sebagai baseline E0 sebelum aksi (disediakan tim FE/BE; audit trail permanen, 8b.10).
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` (dirujuk sebagai `Fixture.nonLoginUser.<key>`) belum ada dan dibuat di tahap script.
- State global yang diubah: tidak ada; usage ledger tetap 600.0 MB karena Edit foto ditolak, Edit tanpa foto dan hapus foto tidak menambah ledger. Suite berjalan serial.

## Test Steps

1. Baca jumlah entri Tab Changelog Detail `Storage Penuh Satu {runId}-031` dengan Action `Edit` sebagai baseline E0 lewat kemampuan baca

### TC-GS-NLU-512: Edit mengganti foto saat Storage penuh ditolak

2. Ketik Search `Storage Penuh Satu {runId}-031`, tekan Enter
3. Klik `⋯` pada baris `Storage Penuh Satu {runId}-031` > `Edit`
4. Ubah Position menjadi `Manager`, lalu unggah berkas JPG 500 KB pada avatar
5. Klik `[Save]`
6. Verifikasi toast error persisten: `Error, failed to upload photo. Storage is full (600.0 MB of 512.0 MB used).`
7. Verifikasi Popup Edit tetap terbuka
8. Verifikasi Position `Manager` dan pilihan file tetap terisi
9. Tutup toast error secara manual
10. Klik `✕`
11. Verifikasi dialog Unsaved Changes tampil
12. Klik `[Leave]`
13. Verifikasi Position baris `Storage Penuh Satu {runId}-031` tetap `Driver`
14. Verifikasi avatar baris `Storage Penuh Satu {runId}-031` tetap foto lama
15. Buka Detail `Storage Penuh Satu {runId}-031`, lalu buka Tab Changelog
16. Verifikasi jumlah entri Action `Edit` sama dengan baseline E0 (tidak ada entri Edit baru)
17. Kembali ke halaman tabel Non-Login User

### TC-GS-NLU-513: Edit tanpa file foto baru berhasil tanpa pengecekan Storage

18. Ketik Search `Storage Penuh Dua {runId}-031`, tekan Enter
19. Klik `⋯` pada baris `Storage Penuh Dua {runId}-031` > `Edit`
20. Ubah Position menjadi `Manager` tanpa mengubah avatar
21. Klik `[Save]`
22. Verifikasi popup menutup
23. Verifikasi toast sukses `Success, non-login user has been updated.`
24. Verifikasi tidak ada toast Storage penuh
25. Verifikasi Position baris `Storage Penuh Dua {runId}-031` menjadi `Manager`

### TC-GS-NLU-514: Hapus foto berhasil tanpa pengecekan Storage

26. Ketik Search `Storage Penuh Tiga {runId}-031`, tekan Enter
27. Klik `⋯` pada baris `Storage Penuh Tiga {runId}-031` > `Edit`
28. Arahkan kursor ke avatar, klik `[Delete]`
29. Klik `[Save]`
30. Verifikasi popup menutup
31. Verifikasi toast sukses `Success, non-login user has been updated.`
32. Verifikasi tidak ada toast Storage penuh
33. Verifikasi avatar baris `Storage Penuh Tiga {runId}-031` kembali ke placeholder generik
34. Buka Detail `Storage Penuh Tiga {runId}-031`, lalu buka Tab Changelog
35. Verifikasi entri Action `Edit`, Field `Photo`, Old Value `-`, New Value `-`, dan Modified By `Siti N`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Kelas blokir kondisi data (prinsip 12): Client PT Storage Penuh MB dengan usage ledger melebihi kuota. TC-GS-NLU-515 (client tanpa kuota) ada di spec 032.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (baseline E0), langkah 2, 18, dan 26 (Search Name bersuffix untuk menemukan baris target karena Email bukan kolom Search; R-16), langkah 9 (menutup toast error persisten; R-12), langkah 10 sampai 12 (menutup form dirty secara deterministik; S-08), langkah 15, 17, dan 34 (membuka Detail, Tab Changelog, dan kembali ke tabel).
- Klausa Expected d TC-GS-NLU-512 "Tab Changelog Detail tidak memuat entri Edit baru" diasersi sebagai jumlah entri Action `Edit` sama dengan E0 (S-12); asersi absence murni tidak ditulis di spec fungsional ini (S-05).
- Langkah 35 memakai Modified By berformat `[First Name] [Last Initial]` (R-14), nama aktor Siti Nurhaliza.
- Temuan untuk QA:
  - TC-GS-NLU-514 Expected c menulis Old Value `-` dan New Value `-` untuk Field `Photo` padahal foto lama ada sebelum dihapus; spec mengikuti TC. Konfirmasi apakah Old Value seharusnya menyebut foto lama.
  - TC-GS-NLU-512, 513, dan 514 menyebut record Pre-setup `Storage Penuh Satu/Dua/Tiga`; spec memakai padanan milik spec (seeding dengan Email unik) supaya Pre-setup tidak berubah.
  - TC-GS-NLU-512 tidak menyebut baseline Changelog; spec menambahkan E0.
