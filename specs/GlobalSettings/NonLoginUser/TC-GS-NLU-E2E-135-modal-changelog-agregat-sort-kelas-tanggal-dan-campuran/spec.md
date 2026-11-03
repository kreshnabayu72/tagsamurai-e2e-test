---
id: TC-GS-NLU-E2E-135-modal-changelog-agregat-sort-kelas-tanggal-dan-campuran
title: "Modal Changelog Agregat: Sort Kelas Tanggal dan Campuran Tipe Data"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-321
  - TC-GS-NLU-322
coverage:
  web: automated
---

# Modal Changelog Agregat: Sort Kelas Tanggal dan Campuran Tipe Data

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup (hanya dibaca, tidak diubah atau dihapus): Tabel Data Uji Pre-setup No. 9 sampai 13 (Position, Division, pool Login User Represented By, Non-Login User dasar, Custom Field dasar).
- Custom Field uji `Skor Uji` (Numeric, 0 desimal, Active): dibuat dan diaktifkan hook `before`, dinonaktifkan atau dihapus hook `after` (suite.md, bagian Custom Field uji).
- Data milik spec (hook `before`, sesi API aktor, kemampuan disediakan tim FE/BE; dihapus di hook `after`): `Sortir Satu {runId}-135` dan `Sortir Dua {runId}-135`. Riwayat Create `Sortir Satu` dan Edit Division dibuat oleh `Siti N`, Create `Sortir Dua` oleh `Fajar N` (Fajar Nugroho, Full CRUD, `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_FULLCRUD_PASSWORD`), dan Skor Uji `Sortir Satu` diubah dari `80` ke `90` sehingga ada Old Value numerik (`80`), Old Value teks (mis. `Operations`), dan Old Value kosong (entri Create), serta New Value numerik, teks, dan kosong tidak ada pada Create; seluruh baris diamati dengan Search `Sortir {runId}-135` (tiga sampai lima baris, semuanya pada halaman 1; S-11, S-14).
- Date berketelitian menit: seeding dilakukan dalam dua tahap yang dipisah sampai menit berganti (hook menunggu maksimum 60 detik di antara dua tahap, bagian 6), sehingga sedikitnya dua nilai Date distinct (S-11).
- Tabel `Kolom sort kelas campuran TC-GS-NLU-322` (dipakai langkah 9 sampai 14):

  | Kolom |
  |---|
  | `Old Value` |
  | `New Value` |
- Format tanggal General Settings: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone `Asia/Jakarta` (Tabel Data Uji Pre-setup No. 16); spec tidak mengubahnya. Jam server dan jam browser sinkron.
- Sort Date berketelitian menit (konvensi bagian 6, KEPUTUSAN 2026-11-02): asersi urutan Date dibatasi pada pasangan entri yang berbeda menit; urutan entri se-menit tidak diasersi, dan penantian pergantian menit hanya satu kali (antara dua kelompok seed).
- Kemampuan teknis: membaca urutan baris tabel; membuat dan menonaktifkan Custom Field uji lewat API.
- Suite berjalan serial (`parallel: false`). Hook `after` menghapus data `{runId}` milik spec ini dan memulihkan state yang diubahnya.

## Test Steps

### TC-GS-NLU-321: Sort 3 tahap kelas tanggal pada Modal Changelog agregat

1. Klik icon Changelog di Table Tools sehingga Modal Changelog terbuka
2. Ketik Search `Sortir {runId}-135`, tekan Enter
3. Klik header kolom `Date` satu kali
4. Verifikasi klik #1: baris terurut `Oldest First` pada kolom `Date`
5. Klik header kolom `Date` untuk kedua kali
6. Verifikasi klik #2: baris terurut `Newest First` pada kolom `Date`
7. Klik header kolom `Date` untuk ketiga kali
8. Verifikasi klik #3: urutan kembali ke default sort tabel (Date terbaru di atas)

### TC-GS-NLU-322: Sort 3 tahap kelas campuran tipe data pada Modal Changelog agregat

9. Untuk setiap baris tabel `Kolom sort kelas campuran TC-GS-NLU-322` di `## Prerequisites` (langkah 9 sampai 14): klik header kolom pada baris tabel satu kali
10. Verifikasi klik #1: baris terurut ascending pada kolom tersebut (nilai numerik lebih dulu, teks setelahnya, nilai kosong di akhir)
11. Klik header kolom yang sama untuk kedua kali
12. Verifikasi klik #2: baris terurut descending pada kolom tersebut (nilai kosong di awal)
13. Klik header kolom yang sama untuk ketiga kali
14. Verifikasi klik #3: urutan kembali ke default sort tabel (Date terbaru di atas)

## Notes

- Sumber TC: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (321, 322) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka Modal Changelog) dan langkah 2 (Search `Sortir {runId}-135` membatasi tabel ke riwayat seeding sort; R-16, S-14).
- Langkah yang diulang: langkah 9 sampai 14 diulang untuk dua baris tabel `Kolom sort kelas campuran TC-GS-NLU-322` di Prerequisites.
- Pembagian TC lintas spec: TC-GS-NLU-320 (Sort kelas teks), 331 (Pagination), dan 332 (Download) ada di spec 092; Search ada di spec 090; Filter ada di spec 091; Setup Column ada di spec 093 dan 094.
- Temuan untuk QA:
  - TC-GS-NLU-322: Expected menyebut "numerik lebih dulu, teks setelahnya" tetapi tidak menyebut data numerik pada Old Value dan New Value; spec menyeding perubahan Custom Field Numeric `Skor Uji` dari `80` ke `90` untuk menghasilkan nilai numerik (mekanisme seeding disediakan tim FE/BE). Pada kolom New Value, nilai kosong tidak dihasilkan oleh riwayat seeding; asersi "kosong di akhir" untuk New Value hanya teramati bila ada entri dengan New Value kosong (mis. Delete).
  - TC-GS-NLU-321: TC menyebut label urutan `Oldest First` dan `Newest First`; label itu diasersi apa adanya sebagai urutan baris.
