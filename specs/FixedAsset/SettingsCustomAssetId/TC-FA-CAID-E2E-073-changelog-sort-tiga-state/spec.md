---
id: TC-FA-CAID-E2E-073-changelog-sort-tiga-state
title: "Modal Changelog: Urutan Default dan Sort 3-State per Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-192
  - TC-FA-CAID-193
  - TC-FA-CAID-194
  - TC-FA-CAID-195
  - TC-FA-CAID-196
  - TC-FA-CAID-197
coverage:
  web: automated
---

# Modal Changelog: Urutan Default dan Sort 3-State per Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Changelog (Pre-setup No 1, pola `totalControl_automated_{namaCompany}@qwertysystem.net`; Company Changelog, Pre-setup No 15). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Login di hook `before` spec ini (kredensial `Spectra.env.FA_CHANGELOG_TC_PASSWORD`); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > Custom Asset ID); hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_TC_PASSWORD`).
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

- Seeding (hook `before`, lewat sesi API aktor): ketujuh entri L1 sampai L7 dengan Date, Action, Field, Old Value, New Value, dan Modified By persis tabel di atas (entri L1 tersimpan 15/09/26 07:25 UTC). Cara membuat entri Changelog bertanggal tetap dengan Modified By pengguna lain tidak disebut TC, PRD, atau LLD: disediakan tim FE/BE. Company Changelog dikembalikan tim FE/BE ke keadaan awal (tujuh entri) sebelum tiap run (lihat `suite.md`); spec ini tidak menambah entri Changelog. Entri Changelog tidak bisa dihapus.
- Precondition TC-FA-CAID-192, TC-FA-CAID-193, TC-FA-CAID-194, TC-FA-CAID-195, TC-FA-CAID-196, TC-FA-CAID-197 (kecuali dinyatakan lain di butir berikut): login sebagai Total Control; Company Changelog dengan tujuh entri log; General Settings Date Format `dd/MM/yy` dan Time Format 24 jam; berada di Fixed Asset > Settings > Asset Master > Custom Asset ID.
- Kemampuan teknis: klik header kolom untuk sort dan membaca indikator sort; mengetik di kotak Search Modal Changelog.
- Date ketujuh entri seed berbeda menitnya (tabel entri di atas), sehingga asersi sort Date dan urutan default tidak membutuhkan penantian pergantian menit; asersi sort non-Date memakai kolom yang punya sedikitnya dua nilai distinct pada tujuh entri seed (S-11, S-14).
- State global yang dipulihkan: tidak ada (spec hanya membaca; sort kembali ke default saat modal ditutup).
- Suite serial (`parallel: false`) karena Company Changelog dan preferensi kolom browser dipakai bersama spec Modal Changelog lain dan sebagian spec mengubah state General Settings.
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.

## Test Steps

### TC-FA-CAID-192: Urutan default Changelog adalah Date terbaru di atas

1. Klik tombol `[Changelog]` pada header kartu
2. Verifikasi baris berurutan L1, L2, L3, L4, L5, L6, L7 (Date Newest First)
3. Verifikasi indikator sort aktif pada header `Date`

### TC-FA-CAID-193: Sort 3-state kolom Date

4. Klik header `Date` satu kali
5. Verifikasi klik 1 (Oldest First): baris berurutan L7, L6, L5, L4, L3, L2, L1
6. Klik header `Date` kedua kali
7. Verifikasi klik 2 (Newest First): baris berurutan L1, L2, L3, L4, L5, L6, L7
8. Klik header `Date` ketiga kali
9. Verifikasi klik 3: indikator sort hilang
10. Verifikasi klik 3: urutan kembali default Newest First (L1, L2, L3, L4, L5, L6, L7)

### TC-FA-CAID-194: Sort 3-state kolom Action dan Field

11. Klik header `Action` satu kali
12. Verifikasi `Action` Ascending: L5, L6, L7 (Create) lalu L1, L2, L3, L4 (Edit)
13. Klik header `Action` kedua kali
14. Verifikasi `Action` Descending: L1, L2, L3, L4 (Edit) lalu L5, L6, L7 (Create)
15. Klik header `Field` satu kali
16. Verifikasi `Field` Ascending: L5 (Segments Formula), L1, L4, L6 (Separator), L2, L3, L7 (Status); baris bernilai sama mengikuti default sort Date terbaru di atas
17. Klik header `Field` kedua kali
18. Verifikasi `Field` Descending: L2, L3, L7, L1, L4, L6, L5; baris bernilai sama mengikuti default sort Date terbaru di atas

### TC-FA-CAID-195: Sort kolom Old Value dan New Value: nilai kosong di akhir saat ascending

19. Klik header `Old Value` satu kali
20. Verifikasi `Old Value` Ascending: L3 (Active), L1 (Dash), L2 (Inactive), L4 (Slash), lalu L5, L6, L7 yang bernilai `—` di akhir
21. Klik header `Old Value` kedua kali
22. Verifikasi `Old Value` Descending: L5, L6, L7 di awal lalu L4, L2, L1, L3
23. Klik header `New Value` satu kali
24. Verifikasi `New Value` Ascending: L2, L7 (Active), L4 (Dash), L1 (Dot), L3 (Inactive), L5 (Initial Company ...), L6 (Slash)

### TC-FA-CAID-196: Sort kolom Modified By memakai nama lengkap

25. Klik header `Modified By` satu kali
26. Verifikasi Ascending berdasarkan nama lengkap: L3 (`Budi S`), L1 (`Rina P`), lalu L2, L4, L5, L6, L7 (`Sarah J`)
27. Klik header `Modified By` kedua kali
28. Verifikasi Descending: L2, L4, L5, L6, L7 (`Sarah J`), L1 (`Rina P`), lalu L3 (`Budi S`)

### TC-FA-CAID-197: Mengganti kolom sort tidak mereset Search aktif

29. Ketik Search `separator`, tekan Enter
30. Klik header `Action`
31. Klik header `Field`
32. Verifikasi keyword `separator` tetap aktif di Search
33. Verifikasi sort berpindah ke kolom `Field`
34. Verifikasi sort `Action` kembali netral
35. Verifikasi tabel menampilkan L1, L4, L6

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti TC sumber (192 sampai 197). Modal Changelog dibuka sekali di langkah 1. Pada tiap TC, mengklik header kolom lain mereset indikator sort kolom sebelumnya (perilaku yang diasersi TC-FA-CAID-197), sehingga tidak ada langkah penghubung pemulihan sort antar TC.
- Asersi urutan memakai baris L1 sampai L7 seed milik Company Changelog (tim FE/BE mengembalikan Company ke keadaan awal sebelum tiap run); urutan itu bukan total audit trail (S-12, S-14).
- Pembagian TC lintas spec: Search Modal Changelog ada di spec 067 dan 068; Filter di spec 069 sampai 072; Sort pada Modal View Code List ada di spec 053.
- Alasan satu dataset berada di beberapa spec: Sort (spec ini) dan Setup Column (spec 074 sampai 077) memakai dataset Pre-setup No 15 (L1 sampai L7) yang sama. Spec 073 sampai 077 berjumlah 137 langkah (35, 36, 19, 19, dan 28), jauh di atas batas sekitar 35 langkah per spec (bagian 3 prinsip 13); tiap spec berdiri sendiri dan Setup Column dibagi menurut Anggota kelas kolom di TC sumber (Date, teks pendek, nilai campuran) serta batas pin, Reset to Default, close, guard, dan cache.
- Temuan untuk QA: (1) Hanya TC-FA-CAID-194 menyebut bahwa baris bernilai sama mengikuti default sort Date terbaru di atas; TC-FA-CAID-195 dan 196 tidak menyebut urutan sekunder, sehingga spec mengasersi urutan persis seperti daftar baris yang tertulis di Expected. (2) Tiga baris `—` pada Old Value (L5, L6, L7) diasersi dengan urutan Expected apa adanya (L5, L6, L7). (3) Kolom ACC dan akun Company Changelog: lihat Temuan spec 066. (4) Judul TC-FA-CAID-196 menulis "memakai nama lengkap", sedangkan Expected menulis nilai kolom `Budi S`, `Rina P`, `Sarah J`; spec mengasersi nilai sesuai format kolom (R-14) dan mengikuti urutan Expected.
