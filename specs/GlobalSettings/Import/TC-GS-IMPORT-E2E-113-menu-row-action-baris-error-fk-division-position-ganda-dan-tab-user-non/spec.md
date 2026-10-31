---
id: TC-GS-IMPORT-E2E-113-menu-row-action-baris-error-fk-division-position-ganda-dan-tab-user-non
title: "Menu row action baris error FK Division, Position, ganda, dan Tab User Non Login memuat Create Missing yang sesuai"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-278
  - TC-GS-IMPORT-693
  - TC-GS-IMPORT-694
coverage:
  web: automated
---

# Menu row action baris error FK Division, Position, ganda, dan Tab User Non Login memuat Create Missing yang sesuai

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > User Login untuk Client C.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Layanan AI: mock tetap mode normal (D-40, tabel D-41 dan D-42); disediakan tim FE/BE.
- Data Dinamis (nama literal karena asersi bergantung pada isi dan nomor baris; pengecualian S-12), dibuat lewat skrip fixture sebelum spec (Kontrak Fixture R2): D-30 (Draft User Login Client C 7 baris dari `user-login-fk.csv`: #1 Ahmad Fauzi `pending`; #2 Division `Gudng` tidak ditemukan; #3 Position `Seniur Developer` tidak ditemukan; #4 Email `dewi.anggraini.c@example.com` sudah terdaftar (`duplicate`); #5 Division `Gudng` dan Position `Seniur Developer`; #6 First Name 121 karakter (error non-FK); #7 First Name 121 karakter dan Division `Gudng`) dan D-31 (Draft User Non Login Client C 3 baris dari `user-non-login-fk.csv`: #1 Siti Rahayu `pending`; #2 Division `Gudng` (error FK); #3 Represented By `tidak.ada@example.com` (error non-FK)).
- Tabel "Menu dengan Create Missing" (TC-693 dan TC-278):

  | Sub-Tab | Baris | Kondisi | Item menu berurutan dari atas |
  |---|---|---|---|
  | User Login | #2 | Division `Gudng` tidak ditemukan (TC-278) | Duplicate, Edit, `[Create Missing Divisions]`, Remove |
  | User Login | #3 | Position `Seniur Developer` tidak ditemukan | Duplicate, Edit, `[Create Missing Positions]`, Remove |
  | User Login | #5 | Division `Gudng` dan Position `Seniur Developer` tidak ditemukan | Duplicate, Edit, `[Create Missing Divisions]`, `[Create Missing Positions]`, Remove |
  | User Non Login | #2 | Division `Gudng` tidak ditemukan | Duplicate, Edit, `[Create Missing Divisions]`, Remove |

- Tabel "Menu tanpa Create Missing" (TC-694):

  | Sub-Tab | Baris | Kondisi |
  |---|---|---|
  | User Login | #1 | pending |
  | User Login | #4 | duplicate (Email sudah terdaftar) |
  | User Login | #6 | error (First Name 121 karakter) |
  | User Non Login | #1 | pending |
  | User Non Login | #3 | error (Represented By `tidak.ada@example.com`) |
- Kemampuan teknis: pengamatan menu row action (tanpa mutasi), skrip seed D-30 dan D-31, mock AI (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain draft Client C dan flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): buang draft User Login dan User Non Login Client C.

## Test Steps

### TC-GS-IMPORT-278 dan TC-GS-IMPORT-693: Menu dengan Create Missing (Tab User Login)

1. Seed draft D-30 di Client C lewat skrip fixture, lalu muat ulang halaman Import > User Login
2. Klik `⋯` pada baris #2
3. Verifikasi menu berisi empat item berurutan dari atas: Duplicate, Edit, `[Create Missing Divisions]`, Remove
4. Verifikasi Remove tampil paling bawah
5. Verifikasi icon tiap item: Duplicate `FileCopyLine`, Edit `Edit2Line`, `[Create Missing Divisions]` `AddLine`, Remove `DeleteBin6Line`
6. Verifikasi Remove berseverity `danger`
7. Verifikasi Duplicate, Edit, dan `[Create Missing Divisions]` berseverity `dark`
8. Tekan Esc untuk menutup menu
9. Klik `⋯` pada baris #3
10. Verifikasi menu memuat Duplicate, Edit, `[Create Missing Positions]`, Remove dengan Duplicate dan Edit di atas dan Remove paling bawah
11. Tekan Esc untuk menutup menu
12. Klik `⋯` pada baris #5
13. Verifikasi menu memuat Duplicate, Edit, `[Create Missing Divisions]`, `[Create Missing Positions]`, Remove dengan Duplicate dan Edit di atas dan Remove paling bawah
14. Verifikasi kedua item Create Missing tampil di antara Edit dan Remove
15. Tekan Esc untuk menutup menu

### TC-GS-IMPORT-694: Menu tanpa Create Missing (Tab User Login)

Untuk setiap baris User Login pada tabel "Menu tanpa Create Missing" (langkah 16 sampai 19 diulang tiga kali: baris #1, #4, #6):

16. Klik `⋯` pada baris sesuai tabel
17. Verifikasi menu berisi tepat tiga item dari atas: Duplicate, Edit, dan Remove
18. Verifikasi item `[Create Missing Divisions]` dan `[Create Missing Positions]` tidak ada di menu
19. Tekan Esc untuk menutup menu

### Tab User Non Login: TC-GS-IMPORT-693 varian 3 dan TC-GS-IMPORT-694 varian 4 dan 5

20. Seed draft D-31 di Client C lewat skrip fixture, pilih Sub-Tab User Non Login, lalu muat ulang halaman
21. Klik `⋯` pada baris #2
22. Verifikasi menu memuat Duplicate, Edit, `[Create Missing Divisions]`, Remove dengan Duplicate dan Edit di atas dan Remove paling bawah
23. Tekan Esc untuk menutup menu
Untuk setiap baris User Non Login pada tabel "Menu tanpa Create Missing" (langkah 24 sampai 27 diulang dua kali: baris #1, #3):
24. Klik `⋯` pada baris sesuai tabel
25. Verifikasi menu berisi tepat tiga item dari atas: Duplicate, Edit, dan Remove
26. Verifikasi item `[Create Missing Divisions]` dan `[Create Missing Positions]` tidak ada di menu
27. Tekan Esc untuk menutup menu

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional; hanya screening menu tanpa mutasi.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: varian TC-693 dan TC-694 dikelompokkan per Sub-Tab (User Login dahulu, lalu User Non Login) supaya Sub-Tab tidak berpindah berulang.
- Asersi absence (langkah 18 dan 26) didahului menu tampil dengan tiga item terverifikasi (langkah 17 dan 25) sebagai anchor positif pada surface yang sama.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 dan 20 menyiapkan D-30 dan D-31; langkah 8, 11, 15, 19, 23, 27 menutup menu.
- Spec berisi sekitar 40 langkah dengan ekspansi. Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional, screening menu tanpa mutasi), parameter tiap iterasi ada di tabel Prerequisites, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-GS-IMPORT-665 (tombol Create Missing Disabled selama Edit Mode) ada di spec 103; dialog Create Missing ada di spec lain.
- Temuan untuk QA:
  - TC-GS-IMPORT-278 Expected c mengasersi nama icon (`FileCopyLine`, `Edit2Line`, `AddLine`, `DeleteBin6Line`), sedangkan NC-04 (keputusan 2026-10-13) menetapkan icon row action tidak diasersi sampai terdaftar di `prd-conventions.md` §23.2. Spec mengikuti Expected TC (langkah 5); perlu keputusan QA apakah langkah itu dihapus.
  - TC-GS-IMPORT-694 Expected a ("tepat tiga item") dan b (item Create Missing tidak ada) dipecah per klausa (langkah 17 dan 18).
  - Post Condition semua TC kosong; tidak ada yang diasersi.
