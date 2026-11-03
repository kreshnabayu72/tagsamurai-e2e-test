---
id: TC-GS-NLU-E2E-136-tab-changelog-detail-sort-tiga-kelas
title: "Tab Changelog Detail: Sort Kelas Teks, Tanggal, dan Campuran Tipe Data"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-340
  - TC-GS-NLU-341
  - TC-GS-NLU-342
coverage:
  web: automated
---

# Tab Changelog Detail: Sort Kelas Teks, Tanggal, dan Campuran Tipe Data

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup (hanya dibaca, tidak diubah atau dihapus): Tabel Data Uji Pre-setup No. 9 sampai 13 (Position, Division, pool Login User Represented By, Non-Login User dasar, Custom Field dasar).
- Data milik spec (hook `before`, sesi API aktor, kemampuan disediakan tim FE/BE; dihapus di hook `after`): `Sortir {runId}-136` dengan riwayat empat entri: Create (Field `Name`, oleh `Siti N`), Edit Division `Operations` ke `Logistics` (oleh `Fajar N`: Fajar Nugroho, Manage user and role Full CRUD, `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_FULLCRUD_PASSWORD`), Edit Division `Logistics` ke `Operations` (oleh `Siti N`), lalu Deactivate (Field `Status`, `Active` ke `Inactive`, oleh `Siti N`). Seeding dibagi dua tahap yang dipisah sampai menit berganti (hook menunggu maksimum 60 detik, bagian 6) sehingga Date punya sedikitnya dua nilai distinct. Tiap kolom yang diurutkan punya sedikitnya dua nilai distinct pada satu halaman (Action `Create`, `Edit`, `Deactivate`; Field `Name`, `Division`, `Status`; Modified By `Siti N` dan `Fajar N`; Old Value kosong dan teks; New Value teks) (S-11, S-14).
- Tabel `Kolom sort kelas teks TC-GS-NLU-340` (dipakai langkah 4 sampai 9):

  | Kolom |
  |---|
  | `Action` |
  | `Field` |
  | `Modified By` |
- Tabel `Kolom sort kelas campuran TC-GS-NLU-342` (dipakai langkah 16 sampai 21):

  | Kolom |
  |---|
  | `Old Value` |
  | `New Value` |
- Format tanggal General Settings: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone `Asia/Jakarta` (Tabel Data Uji Pre-setup No. 16); spec tidak mengubahnya. Jam server dan jam browser sinkron.
- Sort Date berketelitian menit (konvensi bagian 6, KEPUTUSAN 2026-11-02): asersi urutan Date dibatasi pada pasangan entri yang berbeda menit; urutan entri se-menit tidak diasersi, dan penantian pergantian menit hanya satu kali (antara dua kelompok seed).
- Kemampuan teknis: membaca urutan baris tabel.
- Suite berjalan serial (`parallel: false`). Hook `after` menghapus data `{runId}` milik spec ini dan memulihkan state yang diubahnya.

## Test Steps

### TC-GS-NLU-340: Sort 3 tahap kelas teks alfabetis pada Tab Changelog Detail

1. Ketik Search `Sortir {runId}-136`, tekan Enter
2. Buka Detail Non-Login User dengan Name tepat `Sortir {runId}-136`
3. Klik tab `Changelog`
4. Untuk setiap baris tabel `Kolom sort kelas teks TC-GS-NLU-340` di `## Prerequisites` (langkah 4 sampai 9): klik header kolom pada baris tabel satu kali
5. Verifikasi klik #1: baris terurut ascending A-Z pada kolom tersebut
6. Klik header kolom yang sama untuk kedua kali
7. Verifikasi klik #2: baris terurut descending Z-A pada kolom tersebut
8. Klik header kolom yang sama untuk ketiga kali
9. Verifikasi klik #3: urutan kembali ke default sort tabel (Date terbaru di atas)

### TC-GS-NLU-341: Sort 3 tahap kelas tanggal pada Tab Changelog Detail

10. Klik header kolom `Date` satu kali
11. Verifikasi klik #1: baris terurut `Oldest First` pada kolom `Date`
12. Klik header kolom `Date` untuk kedua kali
13. Verifikasi klik #2: baris terurut `Newest First` pada kolom `Date`
14. Klik header kolom `Date` untuk ketiga kali
15. Verifikasi klik #3: urutan kembali ke default sort tabel (Date terbaru di atas)

### TC-GS-NLU-342: Sort 3 tahap kelas campuran tipe data pada Tab Changelog Detail

16. Untuk setiap baris tabel `Kolom sort kelas campuran TC-GS-NLU-342` di `## Prerequisites` (langkah 16 sampai 21): klik header kolom pada baris tabel satu kali
17. Verifikasi klik #1: baris terurut ascending pada kolom tersebut (nilai kosong di akhir)
18. Klik header kolom yang sama untuk kedua kali
19. Verifikasi klik #2: baris terurut descending pada kolom tersebut (nilai kosong di awal)
20. Klik header kolom yang sama untuk ketiga kali
21. Verifikasi klik #3: urutan kembali ke default sort tabel (Date terbaru di atas)

## Notes

- Sumber TC: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (340, 341, 342) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 2, 3 (Search `Sortir {runId}-136`, membuka Detail, dan tab `Changelog`; R-16).
- Langkah yang diulang: langkah 4 sampai 9 diulang untuk tiga baris tabel `Kolom sort kelas teks TC-GS-NLU-340`; langkah 16 sampai 21 diulang untuk dua baris tabel `Kolom sort kelas campuran TC-GS-NLU-342`.
- Pembagian TC lintas spec: Filter, Pagination, Download Tab Changelog ada di spec 096; Screening, Search ada di spec 095; Setup Column ada di spec 097 dan 098.
- Spec melewati sekitar 35 langkah (21 langkah nominal, 39 dengan ekspansi sort lima kolom). Alasan: seluruh blok adalah sort satu kelas harness (fungsional) pada satu layar dan satu dataset, dan tiap blok berdiri sendiri (kegagalan satu kolom tidak membuat kolom lain kehilangan makna); memisahkannya mengulang login, pembukaan Detail, dan seeding riwayat yang sama.
- Temuan untuk QA:
  - TC-GS-NLU-342: Expected "klik #1 ascending (kosong di akhir)" tidak menyebut nilai New Value kosong; riwayat seeding tidak menghasilkan New Value kosong, sehingga klausa kosong teramati hanya pada Old Value.
  - Pada TC-GS-NLU-341, label `Oldest First` dan `Newest First` diasersi apa adanya sebagai urutan baris. Cara membuka Detail Non-Login User dari daftar tidak dijelaskan TC (hanya "User > Detail"); spec menulis "Buka Detail Non-Login User" tanpa mekanisme klik tertentu.
