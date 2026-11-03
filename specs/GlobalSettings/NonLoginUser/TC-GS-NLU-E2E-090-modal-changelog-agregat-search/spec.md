---
id: TC-GS-NLU-E2E-090-modal-changelog-agregat-search
title: "Modal Changelog Agregat: Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-313
  - TC-GS-NLU-314
  - TC-GS-NLU-315
coverage:
  web: automated
---

# Modal Changelog Agregat: Search

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup (hanya dibaca, tidak diubah atau dihapus): Tabel Data Uji Pre-setup No. 9 sampai 13 (Position, Division, pool Login User Represented By, Non-Login User dasar, Custom Field dasar).
- Data milik spec (hook `before`, sesi API aktor Total Control, kemampuan disediakan tim FE/BE; dihapus di hook `after`; Login User hasil Convert ikut dibersihkan):
  - Non-Login User `Budi Kurniawan {runId}-090` (Represented By awal `Ahmad Fauzi`), dibuat oleh `Siti N` (entri Create, Field `Name`), lalu Represented By diubah ke `Dewi Anggraini` oleh `Siti N` (entri Edit, Field `Represented By`, Old Value `Ahmad Fauzi`).
  - Non-Login User `Rani Lestari {runId}-090` (email `ranilestari+{runId}-090@qwertysystem.net`), dibuat oleh `Siti N` (entri Create dengan New Value memuat `Rani Lestari`), lalu di-Convert to Login User oleh `Siti N` (entri dengan Action memuat `Convert`).
  - Kata kunci Search TC-GS-NLU-313 (Old Value `fauz`, New Value `lestari`, Field `represent`, Action `convert`, Modified By `siti`, User Name `kurniawan`) semuanya dipenuhi oleh entri di atas; mekanisme Convert lewat API disediakan tim FE/BE.
- Tabel `Data uji Search TC-GS-NLU-313` (dipakai langkah 4 sampai 5):

  | Kolom | Kata kunci |
  |---|---|
  | `Action` | `convert` |
  | `User Name` | `kurniawan` |
  | `Field` | `represent` |
  | `Old Value` | `fauz` |
  | `New Value` | `lestari` |
  | `Modified By` | `siti` |
- Kolom Date bukan kolom yang dapat dicari: TC-GS-NLU-314 memakai teks sel Date yang dibaca dari tabel pada langkah 8.
- Format tanggal General Settings: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone `Asia/Jakarta` (Tabel Data Uji Pre-setup No. 16); spec tidak mengubahnya. Jam server dan jam browser sinkron.
- Suite berjalan serial (`parallel: false`). Hook `after` menghapus data `{runId}` milik spec ini dan memulihkan state yang diubahnya.

## Test Steps

### TC-GS-NLU-313: Search substring dan case-insensitive pada kolom Action, User Name, Field, Old Value, New Value, Modified By di Modal Changelog agregat

1. Klik icon Changelog di Table Tools sehingga Modal Changelog terbuka
2. Verifikasi sedikitnya satu baris tampil di tabel Modal Changelog sebelum Search (pembanding generik)
3. Klik icon Search
4. Untuk setiap baris tabel `Data uji Search TC-GS-NLU-313` di `## Prerequisites` (langkah 4 sampai 5): ketik Search kata kunci pada baris tabel, tekan Enter
5. Verifikasi sedikitnya satu baris tampil dan baris yang memuat kata kunci pada kolom pada baris tabel ditemukan (substring, tidak membedakan huruf besar kecil)

### TC-GS-NLU-314: Kolom Date tidak dapat dicari lewat Search Modal Changelog

6. Klik `(←)` pada kotak Search
7. Verifikasi sedikitnya satu baris tampil di tabel (pembanding generik)
8. Baca teks pada kolom Date salah satu baris
9. Klik icon Search, ketik teks Date yang dibaca, tekan Enter
10. Verifikasi ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`

### TC-GS-NLU-315: Empty state saat Search tidak ditemukan di Modal Changelog agregat

11. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
12. Verifikasi ilustrasi dengan judul `No results found` dan deskripsi `Try adjusting your search or filter.`
13. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (313, 314, 315) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka Modal Changelog), langkah 3 (membuka input Search; TC-GS-NLU-313 memakai siklus ketik-Enter berulang pada input yang sama), langkah 6 (mengosongkan Search sebelum TC-GS-NLU-314), langkah 8 (membaca teks Date baris yang tampil karena TC hanya menyebut "tanggal salah satu entri"), langkah 13 (mengosongkan Search di akhir spec).
- Langkah yang diulang: langkah 4 sampai 5 diulang untuk enam baris tabel `Data uji Search TC-GS-NLU-313` di Prerequisites; langkah 4 memakai idiom "Ketik Search ... tekan Enter" (bagian 8b butir 9), sehingga pada pengulangan kedua dan seterusnya kotak berisi kata kunci sebelumnya dan diganti.
- Asersi tambahan (konkretisasi Expected): "baris yang memuat kata kunci ditemukan" ditulis dengan pembanding generik pada langkah 2 ("sedikitnya satu baris tampil") dan tiap Verifikasi memuat klausa "sedikitnya satu baris tampil" agar hasil kosong tidak meloloskan asersi; data seeding spec ini menjamin tiap kata kunci memiliki baris (S-11).
- Pembagian TC lintas spec: Filter ada di spec 091; Sort, Pagination, Download ada di spec 092 dan 135; Setup Column ada di spec 093 dan 094.
- Temuan untuk QA:
  - TC-GS-NLU-313: TC tidak menyebut data yang memuat kata kunci `fauz` (Old Value) dan `lestari` (New Value) dan `convert` (Action); spec menyeding riwayat yang memenuhinya dan menuliskan seeding itu di Prerequisites. Kata kunci diasersi sebagai pencarian lintas kolom: TC tidak menyebut apakah Search mencocokkan hanya kolom yang disebut atau semua kolom yang dapat dicari.
  - TC-GS-NLU-314: TC tidak menyebut format teks tanggal yang diketik; spec memakai teks sel Date apa adanya sesuai General Settings.
