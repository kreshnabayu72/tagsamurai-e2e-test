---
id: TC-GS-NLU-E2E-005-empty-state-client-tanpa-non-login-user-dan-dropdown
title: "Empty state Client tanpa Non-Login User dan dropdown filter tanpa opsi"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-NLU-9
  - TC-GS-NLU-492
coverage:
  web: automated
---

# Empty state Client tanpa Non-Login User dan dropdown filter tanpa opsi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client PT Bintang Timur (Client tanpa Non-Login User dan tanpa Login User aktif selain aktor, Pre-setup No. 15). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE. Password `Spectra.env.GS_BINTANGTIMUR_TC_PASSWORD` (nama baru, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; perlu didaftarkan tim FE). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user` untuk akun Client PT Bintang Timur diset true oleh hook suite `before` (lihat `suite.md`); spec ini tidak mengubahnya.
- Data: Client PT Bintang Timur tanpa Non-Login User. Spec hanya membaca: tidak membuat data dan tidak mengubah state global. Bila Client ini menerima Non-Login User dari spec lain, spec ini kehilangan prasyaratnya; suite serial.
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.
- Suite berjalan serial (`parallel: false`).
- Env var yang dipakai terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-GS-NLU-9: Empty state genuinely kosong saat entitas belum punya Non-Login User

1. Verifikasi empty state `S-02` tampil: Illustration dengan Title `"No non-login user yet"` dan Description `"Get started by creating your first non-login user."`
2. Verifikasi Table Tools tetap tampil termasuk `[+ Non-Login User]`

### TC-GS-NLU-492: Dropdown filter menampilkan No options available saat tabel sumber kosong

3. Buka Filter Panel (klik icon Filter di Table Tools)
4. Buka dropdown Active
5. Verifikasi dropdown Active menampilkan teks `"No options available"` (bukan error)
6. Tutup dropdown Active
7. Buka dropdown Position
8. Verifikasi dropdown Position menampilkan teks `"No options available"` (bukan error)
9. Tutup dropdown Position
10. Buka dropdown Division
11. Verifikasi dropdown Division menampilkan teks `"No options available"` (bukan error)
12. Tutup dropdown Division
13. Buka dropdown Represented By
14. Verifikasi dropdown Represented By menampilkan teks `"No options available"` (bukan error)

## Notes

- Langkah penghubung (S-03): langkah 6, 9, 12 (menutup dropdown sebelum dropdown berikutnya dibuka).
- Temuan untuk QA:
  - Email akun Total Control Client PT Bintang Timur tidak tertulis di Tabel Pre-setup TC (No. 15 hanya menyebut Client). Akun dan nama env var diusulkan penulis dan disediakan tim FE (S-11, S-13).
  - TC-GS-NLU-492 langkah 1 "Buka Filter Panel" tidak menyebut kontrolnya; spec memakai icon Filter di Table Tools (TC-GS-NLU-1). Cara menutup dropdown tidak disebut TC.
- Lampiran A konvensi tidak memuat butir untuk modul Non-Login User; tidak ada pengecualian khusus modul yang dipakai.
