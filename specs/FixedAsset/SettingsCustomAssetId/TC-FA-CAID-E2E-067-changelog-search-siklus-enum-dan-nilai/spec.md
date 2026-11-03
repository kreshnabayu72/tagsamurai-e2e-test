---
id: TC-FA-CAID-E2E-067-changelog-search-siklus-enum-dan-nilai
title: "Modal Changelog: Search Siklus, Placeholder, Kelas Enum, dan Nilai Campuran"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-167
  - TC-FA-CAID-168
  - TC-FA-CAID-169
  - TC-FA-CAID-170
coverage:
  web: automated
---

# Modal Changelog: Search Siklus, Placeholder, Kelas Enum, dan Nilai Campuran

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
- Precondition TC-FA-CAID-167, TC-FA-CAID-168, TC-FA-CAID-169, TC-FA-CAID-170 (kecuali dinyatakan lain di butir berikut): login sebagai Total Control; Company Changelog dengan entri seed L1 sampai L7 (Pre-setup No 15); General Settings Date Format `dd/MM/yy` dan Time Format 24 jam; berada di Fixed Asset > Settings > Asset Master > Custom Asset ID.
- Kemampuan teknis: hover icon Search untuk membaca tooltip; membaca fokus kursor pada input Search; mengetik di kotak Search Modal Changelog.
- State global yang dipulihkan: tidak ada (spec hanya membaca).
- Suite serial (`parallel: false`) karena Company Changelog dan preferensi kolom browser dipakai bersama spec Modal Changelog lain dan sebagian spec mengubah state General Settings.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.

## Test Steps

### TC-FA-CAID-167: Siklus interaksi Search Changelog: reveal, clear, submit Enter, collapse

1. Klik tombol `[Changelog]` pada header kartu
2. Hover icon Search
3. Verifikasi tooltip `Search` tampil
4. Klik icon Search
5. Verifikasi input Search terbuka dengan kursor fokus
6. Ketik `edit` pada input Search tanpa menekan Enter
7. Verifikasi icon `(✕)` muncul di dalam input
8. Verifikasi tabel belum tersaring: baris L5, L6, L7 (Action `Create`) masih tampil
9. Tekan Enter
10. Verifikasi tabel hanya menampilkan baris ber-Action `Edit`, termasuk baris seed L1, L2, L3, L4
11. Verifikasi baris seed Action `Create` L5, L6, L7 tidak tampil
12. Klik icon `(✕)` di dalam input
13. Verifikasi input kosong dan tetap terbuka
14. Verifikasi tabel masih hanya menampilkan baris ber-Action `Edit`, termasuk baris seed L1, L2, L3, L4
15. Tekan Enter pada input kosong
16. Verifikasi tabel kembali menampilkan baris seed L1, L2, L3, L4, L5, L6, L7, termasuk baris Create L5, L6, L7
17. Ketik Search `edit`, tekan Enter
18. Klik icon `(←)` di kiri toolbar
19. Verifikasi kotak pencarian menutup
20. Verifikasi tabel langsung menampilkan kembali baris seed L1, L2, L3, L4, L5, L6, L7
21. Klik icon Search
22. Verifikasi keyword dikosongkan: input Search kosong

### TC-FA-CAID-168: Placeholder Search Modal Changelog

23. Verifikasi input Search menampilkan placeholder `Search action, field, modified by...`
24. Klik icon `(←)` pada kotak Search

### TC-FA-CAID-169: Search kelas teks enum: Action dan Field

25. Ketik Search `edit`, tekan Enter
26. Verifikasi Action: `edit` menemukan baris L1, L2, L3, L4
27. Ganti isi kotak search dengan `segments`, tekan Enter
28. Verifikasi Field: `segments` menemukan baris L5
29. Ganti isi kotak search dengan `separator`, tekan Enter
30. Verifikasi Field: `separator` menemukan baris L1, L4, L6
31. Verifikasi pencocokan tidak membedakan huruf besar-kecil: keyword huruf kecil `edit`, `segments`, dan `separator` mencocokkan nilai `Edit`, `Segments Formula`, dan `Separator`

### TC-FA-CAID-170: Search kelas nilai campuran: Old Value dan New Value

32. Ganti isi kotak search dengan `dot`, tekan Enter
33. Verifikasi New Value: `dot` menemukan baris L1 (New Value `Dot`)
34. Ganti isi kotak search dengan `slash`, tekan Enter
35. Verifikasi Old Value dan New Value: `slash` menemukan baris L4 (Old Value `Slash`) dan baris L6 (New Value `Slash`)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti TC sumber (167, 168, 169, 170). Modal Changelog dibuka sekali di langkah 1 untuk keempat TC.
- Langkah penghubung dan langkah bersama: langkah 21 (klik icon Search) adalah aksi TC-FA-CAID-168 sekaligus cara mengamati "keyword dikosongkan" pada TC-FA-CAID-167 butir f, sehingga `Verifikasi` keyword berada di blok TC-FA-CAID-167 dan `Verifikasi` placeholder di blok TC-FA-CAID-168; langkah 24 (menutup input Search sebelum TC-FA-CAID-169, S-09). Langkah "Ketik Search" pada TC-FA-CAID-169 membuka kembali input yang ditutup (bagian 8b butir 9).
- Asersi memakai pola baris seed L1 sampai L7 (relatif terhadap audit trail Company Changelog, S-12); tidak ada asersi total entri atau jumlah baris absolut. Langkah 8 (baris `Create` masih tampil) menjadi penanda "tabel belum tersaring" karena Expected TC tidak menyebut cara mengamatinya. Pada TC-FA-CAID-167 butir c, klausa "hanya baris ber-Action Edit, termasuk L1 sampai L4" (langkah 10) dan "baris seed Create L5, L6, L7 tidak tampil" (langkah 11) dipisah satu `Verifikasi` per klausa (S-01); baris Edit pada langkah 10 menjadi anchor positif bagi absence langkah 11 (bagian 8b butir 2).
- Dataset Company Changelog (seed L1 sampai L7) dan harness (FE+BE) sama dengan spec 066, 068 sampai 072, dan 079. Search Modal Changelog tidak digabung ke satu spec dengan spec 068 karena gabungan langkah spec 067 (35) dan 068 (24) melewati batas sekitar 35 langkah per spec (bagian 3 prinsip 13, smell).
- Pembagian TC lintas spec: Search Modified By, kolom Date, trim, empty state, dan visibilitas kolom (TC-FA-CAID-171 sampai 176) ada di spec 068.
- Temuan untuk QA: (1) TC-FA-CAID-167 butir b "tabel belum tersaring" tidak menyebut cara mengamati; spec memakai baris Action `Create` tetap tampil sebagai penanda. (2) TC-FA-CAID-169 butir b "pencocokan tidak membedakan huruf besar-kecil" tidak punya langkah dengan kapitalisasi berbeda; spec mengasersinya dari keyword huruf kecil yang mencocokkan nilai berhuruf kapital. (3) Kolom ACC dan akun Company Changelog: lihat Temuan spec 066.
