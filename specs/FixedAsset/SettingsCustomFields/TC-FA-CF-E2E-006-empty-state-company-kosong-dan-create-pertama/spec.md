---
id: TC-FA-CF-E2E-006-empty-state-company-kosong-dan-create-pertama
title: "Empty State Company Kosong dan Create Field Pertama"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-20
  - TC-FA-CF-203
  - TC-FA-CF-454
  - TC-FA-CF-640
coverage:
  web: automated
---

# Empty State Company Kosong dan Create Field Pertama

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Kosong. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_KOSONG_PASSWORD`; halaman Fixed Asset > Settings > Custom Fields (tab General) dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup: Company Kosong (Pre-setup #14): lisensi FA-7 aktif, tanpa custom field, tanpa Asset Name, dan tanpa riwayat Changelog. Dipulihkan hook `before` lewat seed reset Company (disediakan tim FE/BE).
- Data Dinamis: field `No AN General {runId}-006` (Text, Scope `General`) dibuat spec pada langkah 11 sampai 16 dan dihapus hook `after` (seed reset Company).
- Kemampuan teknis: pembacaan state empty (ilustrasi, Title, Description).
- Guided Tooltip: hook `before` suite menyetel flag `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor dan hook `after` memulihkannya (lihat `suite.md`).
- State global: tidak ada yang diubah selain data field Company Kosong (dipulihkan hook `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-20: Tab tanpa custom field menampilkan genuinely empty state

1. Verifikasi empty state tab General: ilustrasi dengan Title `No custom field yet` dan Description `Get started by creating your first custom field.`
2. Verifikasi tidak ada CTA selain tombol toolbar pada empty state

### TC-FA-CF-454: Modal Changelog tanpa riwayat menampilkan genuinely empty state

3. Klik icon Changelog di toolbar
4. Verifikasi Modal Changelog menampilkan ilustrasi dengan Title `No changelog yet` dan Description `Activities and changes will appear here.`
5. Tutup Modal Changelog dengan icon close

### TC-FA-CF-640: Dropdown filter pada tab tanpa field menampilkan No options available

6. Klik icon Filter
7. Buka dropdown Data Type
8. Verifikasi dropdown Data Type menampilkan teks `No options available`
9. Verifikasi dropdown Data Type tidak menampilkan error
10. Tutup dropdown Data Type dan panel Filter dengan menekan `Esc`

### TC-FA-CF-203: Create Scope General pada client tanpa Asset Name tersimpan

11. Klik `[+ Custom Field]`
12. Isi Field Name `No AN General {runId}-006`
13. Pilih Data Type `Text` dan Scope `General`
14. Klik `[Submit]`
15. Verifikasi toast sukses `Success, custom field has been created.` tampil
16. Verifikasi baris `No AN General {runId}-006` tampil di tabel dengan Scope `General`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 20, 454, 640, lalu 203. Create pertama (TC-FA-CF-203) berada di akhir karena sesudahnya Company Kosong tidak lagi kosong (S-10, aksi yang mengubah data di akhir).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 (menutup Modal Changelog) dan langkah 10 (menutup dropdown dan panel Filter dengan Esc).
- Langkah 2 (tidak ada CTA selain tombol toolbar) beranchor langkah 1 yang membuktikan empty state tampil. Langkah 9 (tanpa error) beranchor langkah 8.
- Langkah 13 mengisi Data Type `Text` dan Scope `General` dalam satu langkah penghubung form karena Langkah Uji TC-FA-CF-203 menyebut keduanya sebagai satu butir isian; field wajib lain tidak disebut TC.
- Nama field Dinamis bersuffix `{runId}-006` (S-12); Expected TC menyebut `No AN General` sebagai nama tanpa suffix.
- Temuan untuk QA:
  - Pre-setup TC tidak memuat email akun Total Control Company Kosong; akun disediakan tim FE.
  - TC-FA-CF-203 tidak menyebut apakah form Create punya field wajib lain atau nilai default Scope; spec hanya mengisi yang disebut TC.
  - TC-FA-CF-640 Langkah Uji tidak menyebut cara menutup dropdown Filter; spec memakai Esc sebagai langkah penghubung.
