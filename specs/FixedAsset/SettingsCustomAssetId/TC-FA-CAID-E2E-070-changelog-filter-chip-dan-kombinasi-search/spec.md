---
id: TC-FA-CAID-E2E-070-changelog-filter-chip-dan-kombinasi-search
title: "Modal Changelog: Chip Filter dan Kombinasi Search dengan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-181
  - TC-FA-CAID-182
  - TC-FA-CAID-183
  - TC-FA-CAID-184
coverage:
  web: automated
---

# Modal Changelog: Chip Filter dan Kombinasi Search dengan Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Changelog (Pre-setup No 1, pola `totalControl_automated_{namaCompany}@qwertysystem.net`; Company Changelog, Pre-setup No 15). Email akun disediakan tim FE/BE (Pre-setup No 15 hanya menyebut env var). Login di hook `before` spec ini (kredensial `Spectra.env.FA_CHANGELOG_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > Custom Asset ID); hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`).
- Environment variable: `FA_CHANGELOG_TC_PASSWORD` (Total Control Company Changelog) dan `FA_TC_PASSWORD` (akun default suite). Password tidak ditulis di spec atau fixture; kedua nama didaftarkan di tahap script.
- Data Pre-setup (hanya dibaca): No 15 Company Changelog; No 27 General Settings Company Changelog (Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`). Data Dinamis: tidak ada. Nilai L1 sampai L7 adalah data Pre-setup tetap (bukan data Dinamis) sehingga tidak bersuffix `{runId}`; fixture modul Custom Asset ID untuk nilai ini dan teks UI belum ada; prasyarat tahap script yang disediakan tim FE/BE.
- Entri Changelog seed (Pre-setup No 15, urut Date terbaru di atas, pengguna Rina Putri `Rina P`, Sarah Johnson `Sarah J`, Budi Santoso `Budi S`):

| Id | Date | Action | Field | Old Value | New Value | Modified By |
|---|---|---|---|---|---|---|
| L1 | `15/09/26, 14:25` | Edit | Separator | `Dash` | `Dot` | `Rina P` |
| L2 | `14/09/26, 11:30` | Edit | Status | `Inactive` | `Active` | `Sarah J` |
| L3 | `13/09/26, 09:15` | Edit | Status | `Active` | `Inactive` | `Budi S` |
| L4 | `12/09/26, 16:40` | Edit | Separator | `Slash` | `Dash` | `Sarah J` |
| L5 | `10/09/26, 10:02` | Create | Segments Formula | `—` | `Initial Company (Inactive), Group Code (Active), Category Code (Active), Asset Name Code (Active), Division Code (Inactive), Account Code (Inactive), Purchase Date (Active), Asset Increment (Active)` | `Sarah J` |
| L6 | `10/09/26, 10:01` | Create | Separator | `—` | `Slash` | `Sarah J` |
| L7 | `10/09/26, 10:00` | Create | Status | `—` | `Active` | `Sarah J` |

- Seeding (hook `before`, lewat sesi API aktor): ketujuh entri L1 sampai L7 dengan Date, Action, Field, Old Value, New Value, dan Modified By persis tabel di atas (entri L1 tersimpan 15/09/26 07:25 UTC). Cara membuat entri Changelog bertanggal tetap dengan Modified By pengguna lain tidak disebut TC, PRD, atau LLD: disediakan tim FE/BE. Entri log audit lain pada Company Changelog tidak dihapus dan tidak diasersi (audit trail permanen, S-12); spec ini tidak menambah entri Changelog. Entri Changelog tidak bisa dihapus.
- Precondition TC-FA-CAID-181, TC-FA-CAID-182, TC-FA-CAID-183, TC-FA-CAID-184 (kecuali dinyatakan lain di butir berikut): login sebagai Total Control; Company Changelog dengan entri seed L1 sampai L7 (Pre-setup No 15); General Settings Date Format `dd/MM/yy` dan Time Format 24 jam; berada di Fixed Asset > Settings > Asset Master > Custom Asset ID.
- Kemampuan teknis: membaca chip pada field Filter; membuka dropdown multi-select dan mengubah centang opsi; mengetik di kotak Search Modal Changelog.
- State global yang dipulihkan: tidak ada (Search dan Filter dibersihkan lewat langkah penghubung; spec hanya membaca).
- Suite serial (`parallel: false`) karena Company Changelog dan preferensi kolom browser dipakai bersama spec Modal Changelog lain dan sebagian spec mengubah state General Settings.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.

## Test Steps

### TC-FA-CAID-181: Chip pada field filter dihapus dengan ikon silang dan checkbox opsi ikut ter-uncheck

1. Klik tombol `[Changelog]` pada header kartu
2. Klik icon Filter, lalu pilih `Create` dan `Edit` pada `Action`
3. Klik ikon `(✕)` pada chip `Create` tanpa membuka dropdown
4. Verifikasi chip `Create` hilang
5. Verifikasi chip `Edit` tetap tampil
6. Buka dropdown `Action`
7. Verifikasi di dalam dropdown checkbox `Create` tidak tercentang
8. Verifikasi di dalam dropdown checkbox `Edit` tetap tercentang
9. Klik `[Apply]`
10. Verifikasi tabel menampilkan L1, L2, L3, L4 (Action `Edit`)

### TC-FA-CAID-182: Meng-uncheck opsi di dalam dropdown menghapus chip yang bersangkutan

11. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
12. Klik icon Filter, lalu pilih `Create` dan `Edit` pada `Action`
13. Buka dropdown `Action`, lalu hilangkan centang `Create`
14. Verifikasi chip `Create` hilang dari field
15. Verifikasi chip `Edit` tetap tampil

### TC-FA-CAID-183: Search dahulu lalu Filter menghasilkan irisan

16. Klik `[Clear Field]`, lalu klik `[Apply]`
17. Ketik Search `separator`, tekan Enter
18. Klik icon Filter, pilih `Edit` pada `Action`, klik `[Apply]`
19. Verifikasi tabel menampilkan L1 dan L4
20. Verifikasi keyword `separator` tetap terisi di Search

### TC-FA-CAID-184: Filter dahulu lalu Search menghasilkan irisan yang sama

21. Klik icon `(←)` pada kotak Search
22. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
23. Klik icon Filter, pilih `Edit` pada `Action`, klik `[Apply]`
24. Ketik Search `separator`, tekan Enter
25. Verifikasi tabel menampilkan L1 dan L4, identik dengan urutan Search lalu Filter

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti TC sumber (181, 182, 183, 184). Modal Changelog dibuka sekali di langkah 1 untuk keempat TC.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 11 dan 16 (membersihkan Filter dari TC sebelumnya; langkah 16 dijalankan pada panel yang masih terbuka), langkah 21 (menutup Search dan mereset tabel), dan langkah 22 (membersihkan Filter sebelum urutan Filter lalu Search). Langkah "Klik icon Filter" sebelum memilih opsi membuka kembali panel yang ditutup `[Apply]`.
- Asersi memakai pola baris seed L1 sampai L4 milik Company Changelog (relatif terhadap audit trail, S-12); tidak ada asersi total entri absolut.
- Dataset Company Changelog (seed L1 sampai L7) dan harness (FE+BE) sama dengan spec 066 sampai 069, 071, 072, dan 079. Filter Modal Changelog tidak digabung ke satu spec dengan spec 069, 071, dan 072 karena gabungan langkah spec 069 (40), 070 (25), 071 (34), dan 072 (14) melewati batas sekitar 35 langkah per spec (bagian 3 prinsip 13, smell).
- Pembagian TC lintas spec: screening Filter Panel, Date, dropdown, dan AND (TC-FA-CAID-177 sampai 180) ada di spec 069; Clear Field, pemulihan empty state, draft, dan badge (TC-FA-CAID-185 sampai 189) ada di spec 071.
- Temuan untuk QA: (1) TC-FA-CAID-181 dan 182 tidak menyebut dengan jelas apakah panel tetap terbuka sesudah `[Apply]`; spec mengikuti panel menutup setelah `[Apply]` dan membuka kembali lewat icon Filter. (2) Kolom ACC dan akun Company Changelog: lihat Temuan spec 066.
