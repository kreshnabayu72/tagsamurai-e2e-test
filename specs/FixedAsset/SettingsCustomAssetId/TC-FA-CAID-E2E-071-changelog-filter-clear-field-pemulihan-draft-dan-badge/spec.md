---
id: TC-FA-CAID-E2E-071-changelog-filter-clear-field-pemulihan-draft-dan-badge
title: "Modal Changelog: Clear Field, Pemulihan Empty State, Draft Filter, dan Badge"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-185
  - TC-FA-CAID-186
  - TC-FA-CAID-187
  - TC-FA-CAID-188
  - TC-FA-CAID-189
coverage:
  web: automated
---

# Modal Changelog: Clear Field, Pemulihan Empty State, Draft Filter, dan Badge

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
- Precondition TC-FA-CAID-185, TC-FA-CAID-186, TC-FA-CAID-187, TC-FA-CAID-188, TC-FA-CAID-189 (kecuali dinyatakan lain di butir berikut): login sebagai Total Control; Company Changelog dengan entri seed L1 sampai L7 (Pre-setup No 15); General Settings Date Format `dd/MM/yy` dan Time Format 24 jam; berada di Fixed Asset > Settings > Asset Master > Custom Asset ID.
- Kemampuan teknis: mengetik di kotak Search Modal Changelog; klik header kolom untuk sort; membaca chip pada field Filter; membaca badge titik pada icon Filter.
- State global yang dipulihkan: tidak ada (Search, Filter, dan Sort dibersihkan lewat langkah penghubung; spec hanya membaca).
- Suite serial (`parallel: false`) karena Company Changelog dan preferensi kolom browser dipakai bersama spec Modal Changelog lain dan sebagian spec mengubah state General Settings.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.

## Test Steps

### TC-FA-CAID-185: Clear Field pada Filter Panel tidak mereset Search dan Sort

1. Klik tombol `[Changelog]` pada header kartu
2. Ketik Search `separator`, tekan Enter
3. Klik header `Field` sekali
4. Klik icon Filter, pilih `Edit` pada `Action`, klik `[Apply]`
5. Klik icon Filter, lalu klik `[Clear Field]` dan `[Apply]`
6. Verifikasi keyword `separator` tetap aktif di Search
7. Verifikasi sort `Field` Ascending tetap aktif
8. Verifikasi tabel menampilkan L1, L4, L6

### TC-FA-CAID-186: Mengosongkan Search tidak mereset Filter dan Sort

9. Klik icon `(←)` pada kotak Search
10. Klik header `Field` dua kali
11. Ketik Search `separator`, tekan Enter
12. Klik icon Filter, pilih `Edit` pada `Action`, klik `[Apply]`
13. Klik `✕` pada Search, tekan Enter
14. Verifikasi tabel menampilkan L1, L2, L3, L4
15. Klik icon Filter
16. Verifikasi Filter `Action = Edit` tetap aktif: field `Action` berisi chip `Edit`

### TC-FA-CAID-187: Pemulihan dari empty state saat kombinasi Search dan Filter kosong

17. Klik `[Clear Field]`, lalu klik `[Apply]`
18. Ketik Search `segments`, tekan Enter
19. Klik icon Filter, pilih `Edit` pada `Action`, klik `[Apply]`
20. Verifikasi tampil Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
21. Kosongkan isi kotak search, tekan Enter
22. Verifikasi tabel pulih menampilkan L1, L2, L3, L4 sesuai Filter yang tersisa

### TC-FA-CAID-188: Menutup panel Filter tanpa Apply membuang draft

23. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
24. Catat baris yang tampil pada tabel sebagai baseline (sebelum pilihan `Edit` pada langkah 25)
25. Klik icon Filter, lalu pilih `Edit` pada `Action` tanpa menekan `[Apply]`
26. Klik icon Filter lagi untuk menutup panel, lalu klik icon Filter untuk membuka kembali
27. Verifikasi panel menampilkan field `Action` kosong dengan placeholder `All actions`
28. Verifikasi tabel tetap menampilkan baris yang sama seperti baseline langkah 24, termasuk baris seed L1, L2, L3, L4, L5, L6, L7 (Action `Create` dan `Edit`)

### TC-FA-CAID-189: Badge titik pada icon Filter tampil saat ada filter ter-Apply dan hilang saat di-clear

29. Pilih `Edit` pada `Action`, klik `[Apply]`
30. Verifikasi badge titik tampil pada icon Filter dengan panel tertutup
31. Klik icon Filter
32. Verifikasi badge titik tampil pada icon Filter dengan panel terbuka
33. Klik `[Clear Field]`, lalu klik `[Apply]`
34. Verifikasi badge titik hilang

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti TC sumber (185 sampai 189). Modal Changelog dibuka sekali di langkah 1 untuk kelima TC.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): langkah 9 (menutup Search dan mereset tabel), langkah 10 (dua klik header `Field` menuntaskan siklus sort tiga keadaan sehingga indikator sort hilang dan urutan kembali default Date terbaru di atas), langkah 17 dan 23 (membersihkan Filter dari TC sebelumnya; langkah 17 dijalankan pada panel yang masih terbuka dari langkah 15), dan langkah 24 (mencatat baris yang tampil sebagai baseline untuk asersi "baris yang sama seperti sebelum langkah 2" pada TC-FA-CAID-188; S-12). Langkah 15 dan `Verifikasi` sesudahnya membuka panel hanya untuk mengamati chip `Edit`, karena Expected TC-FA-CAID-186 tidak menyebut cara mengamati "Filter tetap aktif" (S-03).
- Asersi memakai pola baris seed L1 sampai L7 milik Company Changelog (relatif terhadap audit trail, S-12); tidak ada asersi total entri absolut.
- Dataset Company Changelog (seed L1 sampai L7) dan harness (FE+BE) sama dengan spec 066 sampai 070, 072, dan 079. Filter Modal Changelog tidak digabung ke satu spec dengan spec 069, 070, dan 072 karena gabungan langkah spec 069 (40), 070 (25), 071 (34), dan 072 (14) melewati batas sekitar 35 langkah per spec (bagian 3 prinsip 13, smell).
- Pembagian TC lintas spec: screening Filter Panel (TC-FA-CAID-177 sampai 180) ada di spec 069; chip dan kombinasi Search dengan Filter (TC-FA-CAID-181 sampai 184) ada di spec 070; Sort ada di spec 073.
- Temuan untuk QA: (1) TC-FA-CAID-189 langkah 3 "Tutup panel Filter" menyiratkan panel tetap terbuka sesudah `[Apply]`, sedangkan TC lain ("Buka lagi panel") menyiratkan panel menutup; spec mengikuti panel menutup setelah `[Apply]`, sehingga badge diamati dengan panel tertutup lalu terbuka. (2) TC-FA-CAID-185 tidak menyebut cara mengamati "sort Field Ascending tetap aktif"; spec memakai indikator sort pada header `Field`. (3) Kolom ACC dan akun Company Changelog: lihat Temuan spec 066.
