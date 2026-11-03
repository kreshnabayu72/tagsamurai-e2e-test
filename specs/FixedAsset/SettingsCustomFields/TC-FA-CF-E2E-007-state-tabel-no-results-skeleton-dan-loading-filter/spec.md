---
id: TC-FA-CF-E2E-007-state-tabel-no-results-skeleton-dan-loading-filter
title: "State Tabel: No Results, Skeleton Loading, dan Loading Dropdown Filter"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-21
  - TC-FA-CF-23
  - TC-FA-CF-641
coverage:
  web: automated
---

# State Tabel: No Results, Skeleton Loading, dan Loading Dropdown Filter

## Prerequisites

- Mode: FE+BE (backend nyata; intercept parsial hanya menahan respons untuk mengamati state loading, bukan memaksa kegagalan).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan `{namaCompany}` = Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Alpha (Pre-setup #11) dengan baseline tab General (Pre-setup #12), dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE); spec hanya membaca dan tidak mengubah data. Kata kunci Search `zzzxxx` tidak cocok dengan field mana pun.
- Kemampuan teknis (Pre-setup #26): penyunting request/respons pada sesi otomasi untuk menahan respons daftar custom field dan respons opsi filter selama 3 detik; intercept dilepas segera setelah state diamati (langkah 8 dan 14).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah; intercept dilepas oleh hook `after` bila spec gagal di tengah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-21: Search tanpa hasil menampilkan empty state filtered

1. Ketik Search `zzzxxx`, tekan Enter
2. Verifikasi empty state: ilustrasi dengan Title `No results found` dan Description `Try adjusting your search or filter.`
3. Klik `(←)` pada kotak Search

### TC-FA-CF-23: Tabel menampilkan skeleton loading lima baris saat data dimuat

4. Tahan respons daftar custom field selama 3 detik
5. Buka Fixed Asset > Settings > Custom Fields lewat menu sidebar
6. Verifikasi tabel menampilkan skeleton loading 5 baris selama respons tertunda
7. Verifikasi toolbar menampilkan indikator loading selama respons tertunda
8. Lepas tahanan respons daftar custom field
9. Verifikasi data tabel tampil setelah respons

### TC-FA-CF-641: Dropdown filter menampilkan indikator loading saat opsi dimuat

10. Tahan respons opsi filter selama 3 detik
11. Klik icon Filter
12. Buka dropdown Data Type
13. Verifikasi dropdown Data Type menampilkan skeleton atau spinner mini selama respons tertunda
14. Lepas tahanan respons opsi filter
15. Verifikasi opsi Data Type tampil setelah respons
16. Tutup dropdown Data Type dan panel Filter dengan menekan `Esc`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Menahan respons hanya untuk mengamati state loading (bukan fault injection kelas b, bagian 3 prinsip 13b); respons dilepas segera sesudah state diamati (S-09). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3 (mengosongkan Search dengan `(←)`, mereset tabel) dan langkah 16 (menutup dropdown dan panel Filter).
- Langkah 5 membuka halaman lewat menu sidebar karena Langkah Uji TC-FA-CF-23 meminta pemuatan ulang halaman saat respons ditahan; klik sidebar mereset Search, Sort, dan Filter.
- Langkah 1 menggabungkan "Klik icon Search" dan "Ketik zzzxxx lalu Enter" dalam satu langkah atomik (8b butir 9).
- Asersi loading (langkah 6, 7, 13) ditulis sebelum respons dilepas (8b butir 5).
- Temuan untuk QA:
  - TC-FA-CF-641 Expected a menyebut "skeleton atau spinner mini" tanpa memilih salah satu; spec mengasersi salah satunya tampil.
