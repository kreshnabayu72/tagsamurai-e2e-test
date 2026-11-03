---
id: TC-GS-NLU-E2E-092-modal-changelog-agregat-sort-pagination-download
title: "Modal Changelog Agregat: Sort, Pagination, dan Download"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-320
  - TC-GS-NLU-331
  - TC-GS-NLU-332
coverage:
  web: automated
---

# Modal Changelog Agregat: Sort, Pagination, dan Download

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup (hanya dibaca, tidak diubah atau dihapus): Tabel Data Uji Pre-setup No. 9 sampai 13 (Position, Division, pool Login User Represented By, Non-Login User dasar, Custom Field dasar).
- Data milik spec (hook `before`, sesi API aktor, kemampuan disediakan tim FE/BE; dihapus di hook `after`):
  - Data sort TC-GS-NLU-320: `Sortir Satu {runId}-092` dibuat oleh `Siti N` (entri Create) lalu Division diubah oleh `Siti N` (entri Edit, Field `Division`); `Sortir Dua {runId}-092` dibuat oleh `Fajar N` (Fajar Nugroho, Manage user and role Full CRUD, `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_FULLCRUD_PASSWORD`; entri Create). Search `Sortir {runId}-092` membatasi tabel ke tiga baris ini sehingga tiap kolom yang diurutkan punya sedikitnya dua nilai distinct pada halaman teramati (Action `Create` dan `Edit`; User Name dua nama; Field `Name` dan `Division`; Modified By `Siti N` dan `Fajar N`) (S-11, S-14).
  - Data pagination TC-GS-NLU-331: `Riwayat Banyak {runId}-092` dengan 12 perubahan Division bergantian (12 entri Edit) sehingga riwayat Changelog lebih dari 10 entri.
- Tabel `Kolom sort kelas teks TC-GS-NLU-320` (dipakai langkah 3 sampai 8):

  | Kolom |
  |---|
  | `Action` |
  | `User Name` |
  | `Field` |
  | `Modified By` |
- Format tanggal General Settings: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone `Asia/Jakarta` (Tabel Data Uji Pre-setup No. 16); spec tidak mengubahnya. Jam server dan jam browser sinkron.
- Kemampuan teknis: membaca urutan baris tabel, memilih opsi pada Filter Panel, menerima unduhan berkas CSV dan membaca nama berkasnya.
- Suite berjalan serial (`parallel: false`). Hook `after` menghapus data `{runId}` milik spec ini dan memulihkan state yang diubahnya.

## Test Steps

### TC-GS-NLU-320: Sort 3 tahap kelas teks alfabetis pada Modal Changelog agregat

1. Klik icon Changelog di Table Tools sehingga Modal Changelog terbuka
2. Ketik Search `Sortir {runId}-092`, tekan Enter
3. Untuk setiap baris tabel `Kolom sort kelas teks TC-GS-NLU-320` di `## Prerequisites` (langkah 3 sampai 8): klik header kolom pada baris tabel satu kali
4. Verifikasi klik #1: baris terurut ascending A-Z pada kolom tersebut
5. Klik header kolom yang sama untuk kedua kali
6. Verifikasi klik #2: baris terurut descending Z-A pada kolom tersebut
7. Klik header kolom yang sama untuk ketiga kali
8. Verifikasi klik #3: urutan kembali ke default sort tabel (Date terbaru di atas)

### TC-GS-NLU-331: Pagination Modal Changelog agregat

9. Klik `(←)` pada kotak Search
10. Verifikasi footer modal: default 10 baris per halaman
11. Verifikasi footer modal: opsi jumlah baris per halaman `10`, `25`, `50`, dan `100`
12. Klik halaman 2
13. Verifikasi halaman 2 menampilkan entri berikutnya (sedikitnya satu baris yang berbeda dari baris halaman 1)

### TC-GS-NLU-332: Download Modal Changelog agregat mengikuti Search dan Filter

14. Klik icon Filter, pilih Action `Create`, klik `[Apply]`
15. Klik Download > `Download as CSV`
16. Verifikasi tidak ada toast sukses
17. Verifikasi berkas `Changelog-Non-Login-User.csv` terunduh
18. Klik `[Clear Field]` pada Filter Panel, klik `[Apply]`

## Notes

- Sumber TC: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (320, 331, 332) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (membuka Modal Changelog); langkah 2 (Search `Sortir {runId}-092` membatasi tabel ke riwayat seeding sort); langkah 9 (mengosongkan Search sebelum TC-GS-NLU-331); langkah 14 dan 18 (memasang dan mengosongkan Filter Action).
- Langkah yang diulang: langkah 3 sampai 8 diulang untuk empat baris tabel `Kolom sort kelas teks TC-GS-NLU-320` di Prerequisites; tiap iterasi mempertahankan satu `Verifikasi` per klik (S-01).
- Asersi tambahan (konkretisasi Expected): "Opsi 10/25/50/100" (TC-GS-NLU-331) ditulis sebagai satu Verifikasi daftar opsi; "kembali ke default sort tabel" ditulis sebagai urutan Date terbaru di atas.
- Pembagian TC lintas spec: TC-GS-NLU-321 dan TC-GS-NLU-322 (Sort kelas tanggal dan campuran) ada di spec 135; Search ada di spec 090; Filter ada di spec 091; Setup Column ada di spec 093 dan 094.
- Temuan untuk QA:
  - TC-GS-NLU-332: Expected "hanya berisi entri Create" adalah isi sel berkas (kelas f, bagian 3 prinsip 13); spec hanya mengasersi nama berkas dan tidak adanya toast sukses, dan isi sel tidak diasersi. Belum ada spec kelas f yang memuat isi berkas Changelog agregat.
  - TC-GS-NLU-331: TC tidak menyebut cara riwayat lebih dari 10 entri disediakan; spec menyeding 12 entri Edit milik spec.
- Spec melewati sekitar 35 langkah (18 langkah nominal, 36 dengan ekspansi sort empat kolom). Alasan: sort empat kolom adalah blok identik satu kelas harness (fungsional) pada satu layar dan satu dataset, dan tiap blok berdiri sendiri (kegagalan satu kolom tidak membuat kolom lain kehilangan makna); Pagination dan Download memakai Modal Changelog yang sama sehingga memisahkannya mengulang login dan pembukaan modal.
