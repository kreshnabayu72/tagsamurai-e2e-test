---
id: TC-FA-CF-E2E-048-global-value-document-submit-disabled-dan-per-asset-name
title: "Global Value Document: Submit Disabled Saat File Dikirim dan Satu Kontrol Unggah per Asset Name"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-148
  - TC-FA-CF-149
coverage:
  web: automated
---

# Global Value Document: Submit Disabled Saat File Dikirim dan Satu Kontrol Unggah per Asset Name

## Prerequisites

- Mode: FE+BE (backend nyata) dengan intercept parsial: respons Create ditunda 3 detik hanya untuk mengamati state tombol (bukan kegagalan yang dipaksakan); intercept dilepas segera sesudah pengamatan.
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, dengan `{namaCompany}` berisi nama Company Alpha. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan hook `after` (lihat `suite.md`).
- Data Pre-setup (hanya dibaca): Company Alpha baseline (Pre-setup #11 dan #12) dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE); Asset Name `Generator` dan `Pump` sudah ada di baseline.
- Berkas uji (Pre-setup #36; fixture berkas `Fixture.berkasUji` baru, belum ada): `valid.pdf` (200 KB).
- Data Dinamis (dibuat lewat UI; `{runId}` terdiri atas digit; nama bersuffix `-048`): `Global Doc Submit {runId}-048` (Document, Global, Scope General, tersimpan) dan `Doc Per AN {runId}-048` (Document, Global, Scope `Generator` dan `Pump`, tidak tersimpan).
- Cleanup (hook `after`; tidak berasumsi setup berhasil penuh): hapus lewat API semua field Company Alpha yang namanya memuat `{runId}-048` beserta berkas yang terunggah; lepaskan intercept respons Create bila masih aktif.
- Kemampuan teknis: Penyunting request dan respons yang menunda respons Create 3 detik (Pre-setup #26); pengamatan request jaringan Create untuk memastikan berkas dikirim bersama Submit tanpa request unggah terpisah dan tanpa progress unggah (disediakan tim FE).
- State global: tidak ada yang diubah (intercept dilepas di langkah 10 dan hook `after`); suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik [+ Custom Field]

### TC-FA-CF-148: Tombol Submit disabled selama file dikirim bersama Submit

2. Isi Field Name `Global Doc Submit {runId}-048`, pilih Data Type `Document`, Scope `General`, Value Type `Global`
3. Tunda respons Create 3 detik
4. Pilih berkas `valid.pdf`
5. Klik [Submit]
6. Verifikasi file dikirim bersama Submit tanpa unggah terpisah
7. Verifikasi tidak ada progress unggah
8. Verifikasi tombol `[Submit]` disabled selama menunggu
9. Verifikasi tombol `[Submit]` menampilkan indikator loading selama menunggu
10. Lepas tundaan respons Create
11. Tunggu aksi selesai (modal tertutup)

### TC-FA-CF-149: Scope Specific Asset Name dengan Global Document menampilkan satu kontrol unggah per Asset Name

12. Klik [+ Custom Field]
13. Isi Field Name `Doc Per AN {runId}-048`, Data Type `Document`, Scope `Specific Asset Name` dengan `Generator` dan `Pump`, Value Type `Global`
14. Verifikasi dua kontrol unggah berlabel `Generator` dan `Pump` tampil
15. Pilih berkas `valid.pdf` pada kontrol `Generator`
16. Klik [Submit] tanpa mengisi kontrol `Pump`
17. Verifikasi pesan inline "Value must not be empty" tampil pada kontrol `Pump`
18. Verifikasi field tidak tersimpan: modal tetap terbuka
19. Klik `[✕]`
20. Verifikasi dialog `Unsaved Changes` dengan body "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]` tampil
21. Klik `[Leave]`

### Penutup: field yang ditolak tidak tersimpan

22. Ketik Search `{runId}-048`, tekan Enter
23. Verifikasi tabel menampilkan tepat 1 baris `Global Doc Submit {runId}-048` (field `Doc Per AN {runId}-048` tidak tersimpan)
24. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE dengan intercept. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sama dengan sumber (148, 149). Penundaan respons pada TC-FA-CF-148 hanya untuk mengamati state tombol Submit, bukan kegagalan yang dipaksakan, sehingga spec ini tetap fungsional (bagian 3 prinsip 13b). Intercept dilepas segera setelah pengamatan (langkah 10, S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 3, 4, 10, 11 (menunggu modal tertutup sebelum membuka modal berikutnya, bagian 8b butir 8), 12, 15, 16, 19, 21, 22, 24, serta pengisian form sebagai bagian langkah TC. Langkah 22 sampai 24 membuktikan lewat satu baris tersimpan sebagai anchor positif bahwa field TC-FA-CF-149 tidak muncul.
- Langkah 6 dan 7 memecah Expected a TC-FA-CF-148 per klausa (S-01); langkah 8 dan 9 memecah Expected b (state tombol dan indikator loading).
- Temuan untuk QA:
  - TC-FA-CF-148: Expected a ("tanpa unggah terpisah dan tanpa progress") membutuhkan pengamatan request jaringan; mekanismenya tidak didefinisikan di TC, PRD, atau LLD dan ditulis "disediakan tim FE" (S-13).
  - Nama field memakai suffix `{runId}-048` (S-12) sehingga tidak sama dengan `Global Doc` dan `Doc Per AN` pada Data Uji TC.
