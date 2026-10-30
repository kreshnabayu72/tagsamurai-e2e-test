---
id: TC-GS-GSET-E2E-054-changelog-setup-column-kolom-visible-terakhir-dan-reset-to-default-belum-disimpan
title: "Changelog General Settings: Setup Column Kolom Visible Terakhir dan Hasil Reset to Default yang Belum Disimpan Dibuang"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-GSET-92
  - TC-GS-GSET-95
coverage:
  web: automated
---

# Changelog General Settings: Setup Column Kolom Visible Terakhir dan Hasil Reset to Default yang Belum Disimpan Dibuang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Budi Santoso (`Budi S`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup TC baris 1; `Fixture.generalSettings.totalControl`, fixture belum ada), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); halaman General Settings dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Hook suite (`suite.md`, bagian Hook suite): flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` disetel true untuk akun aktor dan record Client A dipulihkan ke baseline sebelum spec; spec ini tidak mengatur flag sendiri.
- Data Pre-setup: record General Settings Client A baseline (Pre-setup 10: `IDR`, `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`, `30 minutes`).
- Seeding di hook `before` (precondition TC "Changelog berisi baris riwayat", dipakai sebagai precondition TC, tidak diasersi): satu PUT `/v2/enterprise-management/general-settings` (full-replace, `global-settings/general-settings/API/openapi.yaml`) oleh sesi API Budi Santoso yang mengubah `sessionIdleTimeout` dari 30 ke 60 menit sehingga Changelog memuat sedikitnya satu baris Field `Session Idle Timeout` (`30 minutes` ke `1 hour`), lalu satu PUT yang mengembalikan nilai ke 30 menit. Total entri Changelog tidak pernah diasersi sebagai angka (audit trail permanen).
- Data uji: kolom Changelog `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By` (semua Hideable, default visible); kolom yang di-uncheck: `Date`, `Action`, `Field`, `Old Value`, `New Value` (TC-92, tersisa `Modified By`) dan `Field` (TC-95).
- Konfigurasi kolom Modal Changelog (visibilitas, urutan, pin) tersimpan per pengguna di cache browser dan baru permanen setelah `[Save]` (PRD general-settings.md §4.2c). Pemulihan: langkah 19 mengembalikan konfigurasi ke default lewat `[Reset to Default]` lalu `[Save]`; hook `after` (tetap jalan walau spec gagal di tengah) memulihkan konfigurasi kolom Changelog dengan menghapus preferensi kolom Changelog di browser (mekanisme disediakan tim FE; TC, PRD, dan LLD tidak mendefinisikannya).
- Sesi API aktor memakai token yang tidak dihitung sebagai sesi web (pernyataan di `suite.md`).
- Kemampuan teknis: mengarahkan kursor ke checkbox disabled untuk membaca tooltip; membaca dan menghapus preferensi kolom di penyimpanan browser.
- Suite berjalan serial (`parallel: false`): konfigurasi kolom Changelog bersifat state bersama dengan spec Setup Column dan Download lain.

## Test Steps

### TC-GS-GSET-92: Setup Column: minimal satu kolom tetap visible

1. Klik icon Changelog di pojok kanan atas halaman
2. Buka Setup Column via header kolom Actions (⋯) > `Setup Column...`
3. Hilangkan centang kolom `Date`, `Action`, `Field`, `Old Value`, dan `New Value` satu per satu hingga hanya `Modified By` yang tercentang
4. Arahkan kursor ke checkbox kolom `Modified By`
5. Verifikasi checkbox kolom `Modified By` disabled
6. Verifikasi checkbox kolom `Modified By` tetap tampil
7. Verifikasi tooltip `At least one column must remain visible.`
8. Coba hilangkan centang kolom `Modified By`
9. Verifikasi kolom `Modified By` tetap tercentang (tidak dapat di-uncheck)
10. Klik `[✕]` untuk menutup Modal Setup Column tanpa menyimpan

### TC-GS-GSET-95: Setup Column: hasil Reset to Default yang belum di-Save dibuang saat ditutup

11. Buka Setup Column via header kolom Actions (⋯) > `Setup Column...`
12. Hilangkan centang kolom `Field`
13. Klik `[Save]`
14. Buka Setup Column via header kolom Actions (⋯) > `Setup Column...` lagi
15. Klik `[Reset to Default]`
16. Klik `[✕]`
17. Verifikasi kolom Date, Action, Old Value, New Value, dan Modified By tampil di tabel
18. Verifikasi kolom `Field` tidak tampil di tabel (tabel tetap memakai konfigurasi tersimpan)
19. Buka Setup Column via header kolom Actions (⋯) > `Setup Column...`, klik `[Reset to Default]`, klik `[Save]`

## Notes

- Sumber TC: `global-settings/general-settings/TestCases/tc-general-settings.md` (Section 4b). Mode: FE+BE (Changelog dimuat dari backend nyata; konfigurasi kolom tersimpan di browser).
- TC-GS-GSET-92 dan TC-GS-GSET-95 ada di spec ini; TC-GS-GSET-84, 87, 89, dan 94 ada di spec 034 (TC-GS-GSET-94 melanjutkan modal dari blok TC-GS-GSET-87). Blok TC-GS-GSET-92 dan TC-GS-GSET-95 membuka Modal Setup Column sendiri lewat header Actions (⋯) dan tidak meneruskan modal dari blok lain. Prerequisites, akun, dan hook ditulis utuh di spec ini (S-04, S-06); spec ini tidak bergantung pada spec lain. `caseType: Negative` mengikuti TC-92 (prioritas lebih tinggi).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC dalam spec: 92 lalu 95 di akhir karena TC-95 menyimpan konfigurasi dengan kolom `Field` tersembunyi dan dipulihkan di langkah 19. Urutan di `tc-general-settings.md`: 92, 95.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka Modal Changelog), langkah 10 (menutup Modal Setup Column tanpa menyimpan agar centang pada langkah 3 tidak tersimpan), dan langkah 19 (memulihkan konfigurasi kolom ke default). Langkah 2, 11, dan 14 membuka Modal Setup Column lewat header Actions (⋯) > `Setup Column...` karena modal tertutup sesudah `[✕]` atau `[Save]`.
- Save Setup Column (langkah 13 dan 19) adalah aksi sisi klien tanpa request tulis ke server, jadi tidak diikuti langkah "Tunggu aksi selesai".
- Asersi tambahan (konkretisasi, S-03): langkah 17 (kolom lain tampil) adalah pembanding positif sebelum asersi absence kolom `Field` pada langkah 18 (bagian 8b butir 2 konvensi).
- Pembagian TC lintas spec: TC-GS-GSET-84, 87, 89, dan 94 ada di spec 034; TC-GS-GSET-88, 90, 91, dan 93 (Pin/Unpin, hide/unhide dengan Save, reorder, Reset to Default dengan Save) di spec 035; TC-GS-GSET-70 di spec 028; TC-GS-GSET-100 dan 159 di spec 036; TC-GS-GSET-85, 86, 96 di spec 027.
- Temuan untuk QA:
  - TC-GS-GSET-92: langkah 2 tidak menyebut kolom mana yang tersisa; spec menyisakan `Modified By` (kolom terakhir pada urutan default) dan menulis urutan uncheck eksplisit.
  - TC-GS-GSET-95: TC tidak menyebut cara mengembalikan konfigurasi kolom; TC-95 menyimpan konfigurasi dengan `Field` tersembunyi. Pemulihan di langkah 19 dan hook `after` adalah tambahan spec; mekanisme menghapus preferensi kolom di browser tidak didefinisikan di TC, PRD, atau LLD (disediakan tim FE).
