---
id: TC-GS-NLU-E2E-030-storage-penuh-create-dengan-foto-pada-client-storage-penuh-mb
title: "Storage penuh: Create dengan foto pada Client Storage Penuh MB"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-NLU-508
  - TC-GS-NLU-509
coverage:
  web: automated
---

# Storage penuh: Create dengan foto pada Client Storage Penuh MB

## Prerequisites

- Mode: FE+BE (backend nyata; pengecekan Storage dilakukan server berdasarkan usage ledger, bukan kartu Storage Usage File Manager).
- Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor: Total Control pada Client PT Storage Penuh MB `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Client PT Storage Penuh MB (Tabel Data Uji Pre-setup No. 1 dan 19), password lewat `Spectra.env.GS_STORAGEMB_TC_PASSWORD`. Nama env baru yang diusulkan (belum terdaftar di `spectra.config.ts` dan `.env.example`; akun disediakan tim FE).
- Env var: `GS_STORAGEMB_TC_PASSWORD`.
- Hook suite: flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` = seen untuk akun aktor (lihat `suite.md`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 9 sampai 12 dan 19, hanya dibaca): Division `Operations`, Login User `Ahmad Fauzi` (pool Represented By), Client PT Storage Penuh MB dengan kuota Storage 536870912 byte (512.0 MB) dan usage ledger 629145600 byte (600.0 MB); kartu Storage Usage File Manager masih menampilkan laporan terakhir sebelum penuh (snapshot), dasar pengecekan adalah usage ledger server.
- Berkas uji di perangkat uji: gambar JPG 500 KB.
- Data Dinamis milik spec (Tabel Data Uji Dinamis No. 7): Non-Login User `Foto Penuh Dua {runId}-030` (First Name `Foto`, Last Name `Penuh Dua {runId}-030`, Division `Operations`, Represented By `Ahmad Fauzi`) Email `fotopenuhdua+{runId}-030@qwertysystem.net` (milik Client PT Storage Penuh MB). Non-Login User `Foto Penuh Satu {runId}-030` Email `fotopenuhsatu+{runId}-030@qwertysystem.net` tidak boleh tersimpan. Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus Non-Login User ber-Email `+{runId}-030` lewat API (mekanisme disediakan tim FE/BE).
- Jeda: langkah 6 menunggu 10 detik tanpa menutup toast agar kepersistenan toast teramati; jeda melampaui durasi tampil toast biasa dan jauh di bawah ±30 detik (R-10).
- Kemampuan teknis: membaca jumlah total entri Modal Changelog sebelum aksi sebagai baseline N0 (disediakan tim FE/BE; audit trail permanen, 8b.10).
- Fixture: nilai uji ditulis di langkah sesuai TC; `fixtures/non-login-user.json` (dirujuk sebagai `Fixture.nonLoginUser.<key>`) belum ada dan dibuat di tahap script.
- State global yang diubah: tidak ada; usage ledger Client PT Storage Penuh MB tetap karena tidak ada foto yang berhasil disimpan. Suite berjalan serial.

## Test Steps

1. Buka Modal Changelog, catat jumlah total entri sebagai baseline N0, lalu tutup Modal Changelog

### TC-GS-NLU-508: Create dengan foto baru saat Storage penuh ditolak

2. Klik `[+ Non-Login User]`
3. Isi First Name `Foto`, Last Name `Penuh Satu {runId}-030`, Email `fotopenuhsatu+{runId}-030@qwertysystem.net`, pilih Division `Operations` dan Represented By `Ahmad Fauzi`, lalu unggah berkas JPG 500 KB pada avatar
4. Klik `[Submit]`
5. Verifikasi toast error: `Error, failed to upload photo. Storage is full (600.0 MB of 512.0 MB used).`
6. Tunggu 10 detik tanpa menutup toast
7. Verifikasi toast error masih tampil (persisten, tidak hilang otomatis)
8. Verifikasi Popup Create tetap terbuka
9. Verifikasi seluruh isian dan avatar pilihan tetap terisi
10. Tutup toast error secara manual
11. Klik `✕`
12. Verifikasi dialog Unsaved Changes tampil
13. Klik `[Leave]`
14. Ketik Search `Foto Penuh Satu {runId}-030`, tekan Enter
15. Verifikasi tabel menampilkan `No results found`
16. Klik `(←)` pada kotak Search
17. Buka Modal Changelog
18. Verifikasi jumlah total entri sama dengan baseline N0 (tidak ada entri Create baru untuk `Foto Penuh Satu {runId}-030`)
19. Tutup Modal Changelog

### TC-GS-NLU-509: Hapus foto terpilih lalu Submit ulang menyimpan record tanpa foto

20. Klik `[+ Non-Login User]`
21. Isi First Name `Foto`, Last Name `Penuh Dua {runId}-030`, Email `fotopenuhdua+{runId}-030@qwertysystem.net`, pilih Division `Operations` dan Represented By `Ahmad Fauzi`, lalu unggah berkas JPG 500 KB pada avatar
22. Klik `[Submit]`
23. Verifikasi toast error: `Error, failed to upload photo. Storage is full (600.0 MB of 512.0 MB used).`
24. Verifikasi Popup Create tetap terbuka
25. Tutup toast error secara manual
26. Arahkan kursor ke avatar, klik `[Delete]`
27. Klik `[Submit]`
28. Verifikasi popup menutup
29. Verifikasi toast sukses `Success, non-login user has been created.`
30. Verifikasi tidak ada toast Storage penuh
31. Ketik Search `Foto Penuh Dua {runId}-030`, tekan Enter
32. Verifikasi baris `Foto Penuh Dua {runId}-030` muncul di tabel dengan placeholder avatar generik

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Kelas blokir kondisi data (prinsip 12): Client PT Storage Penuh MB dengan usage ledger melebihi kuota.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 (baseline N0), langkah 6 (jeda 10 detik, melampaui durasi tampil toast biasa, agar kepersistenan toast teramati; jeda pendek pilihan spec, bukan nilai TC), langkah 10 dan 25 (menutup toast error persisten sebelum langkah berikut; R-12), langkah 11 sampai 13 (menutup form dirty secara deterministik; S-08), langkah 16 (mengosongkan Search sebelum Modal Changelog), langkah 17 dan 19 (membuka dan menutup Modal Changelog), langkah 14 dan 31 (Search Name bersuffix untuk menemukan baris target karena Email bukan kolom Search; R-16).
- Klausa Expected c TC-GS-NLU-508 "tidak memuat entri Create" diasersi sebagai jumlah entri sama dengan baseline N0 (S-12); asersi absence murni tidak ditulis di spec fungsional ini (S-05). Hasil `No results found` pada langkah 15 adalah anchor positif untuk Search.
- Temuan untuk QA:
  - TC-GS-NLU-508 Expected a menyebut toast "persisten (tidak hilang otomatis hingga ditutup manual)" tanpa durasi pengamatan; spec memilih jeda 10 detik pada langkah 6.
  - TC-GS-NLU-508 langkah 5 membuka Modal Changelog tanpa menyebut baseline; spec menambah baseline N0 agar "tidak memuat entri" dapat diasersi sebagai selisih.
  - Akun Total Control untuk Client PT Storage Penuh MB belum tentu terdaftar dengan nama env di atas.
