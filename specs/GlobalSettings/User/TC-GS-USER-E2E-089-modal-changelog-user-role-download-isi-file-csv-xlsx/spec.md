---
id: TC-GS-USER-E2E-089-modal-changelog-user-role-download-isi-file-csv-xlsx
title: "Modal Changelog Role: Download CSV/XLSX (isi berkas, cakupan Search/Filter, kolom hidden, nilai kosong)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-544
  - TC-GS-USER-545
  - TC-GS-USER-546
  - TC-GS-USER-547
  - TC-GS-USER-548
coverage:
  web: automated
---

# Modal Changelog Role: Download CSV/XLSX (isi berkas, cakupan Search/Filter, kolom hidden, nilai kosong)

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control Siti Nurhaliza (`Siti N`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 2), akun default suite. Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User).
- Pelaku seeding lewat sesi API (tidak login UI): Manage user and role (Full CRUD) Fajar Nugroho (`Fajar N`), `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 4), `Spectra.env.GS_FULLCRUD_PASSWORD`. Fajar menjadi nilai Modified By kedua selain `Siti N`.
- Environment variable: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: tidak dipakai. TC menyebut `Ahmad Fauzi` (Tabel Data Uji Pre-setup baris 13); aksi tulis Role memakai user seed milik spec (S-06), jadi Pre-setup tidak diubah.
- Data Dinamis: user seed `Ahmad Fauzi {runId}-089`, email `ahmadfauzi+{runId}-089@qwertysystem.net`, Access `Global Settings`, bukan tier, field wajib lain diisi seadanya oleh seeding. Nama berkas unduhan mengikuti pola PRD `Changelog-User-[User-Name]-Role` dengan spasi nama menjadi tanda hubung: `Changelog-User-Ahmad-Fauzi-{runId}-089-Role.csv` dan `.xlsx`.
- Seeding minimal (S-11; lewat API di hook `before`, urutan sebagai berikut; setara TC-GS-USER-902, 903, 904, 1052). Seeding membuat 12 entri agar berkas memuat lebih banyak baris daripada satu halaman (10 baris) untuk TC-GS-USER-544:
  - 1. Siti N: Assign `Manage TAG` -> `Assign | Manage TAG | Access | — | Assigned | Siti N`.
  - 2. Siti N: centang Update `Manage TAG` -> `Edit | Manage TAG | Update | Inactive | Active | Siti N`.
  - 3. Fajar N: Assign `Manage files` -> `Assign | Manage files | Access | — | Assigned | Fajar N`.
  - 4. Siti N: Remove `Manage files` -> `Remove | Manage files | Access | Assigned | — | Siti N`.
  - 5. Siti N: centang Read `Manage hardware` -> `Assign | Manage hardware | Access | — | Assigned | Siti N`.
  - 6. Fajar N: centang Update `Manage hardware` -> `Edit | Manage hardware | Update | Inactive | Active | Fajar N`.
  - 7 sampai 12. Siti N: 6 kali mengubah centang bergantian Create, Update, dan Delete pada `Manage TAG` (tiap perubahan satu baris `Edit`).
  - Nilai distinct (S-11): Action 3 (`Assign`, `Edit`, `Remove`), Role 3, Field 4 (`Access`, `Create`, `Delete`, `Update`), Modified By 2 (`Siti N`, `Fajar N`); Old Value dan New Value kosong (`—`) pada baris `Assign` dan `Remove`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus user seed lewat API; hapus berkas unduhan; pulihkan visibilitas kolom Modal Changelog Role ke default (7 kolom tampil) lewat penghapusan key `localStorage` tabel itu (nama key disediakan tim FE). Entri Changelog tidak bisa dihapus.
- Kemampuan teknis (kelas binary buffer, prinsip 13f): menangkap berkas unduhan browser ke direktori bersih per unduhan; membaca isi berkas CSV dan XLSX (nama berkas, kolom header, jumlah baris data, nilai sel); membaca ada atau tidaknya toast.
- Precondition TC-GS-USER-544 sampai 548: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); data pre-setup User tersedia; riwayat Changelog Role user seed terisi.
- Suite serial (`parallel: false`), lihat `suite.md`.
- State global yang dipulihkan: visibilitas kolom Modal Changelog Role (default).

## Test Steps

### TC-GS-USER-544: Download CSV seluruh data tanpa toast sukses

1. Klik Name `Ahmad Fauzi {runId}-089` di User List
2. Klik Tab `Role`
3. Klik icon Changelog di toolbar Tab Role
4. Klik icon Download
5. Verifikasi overlay opsi `Download as CSV` dan `Download as XLSX`
6. Klik `Download as CSV`
7. Verifikasi file `Changelog-User-Ahmad-Fauzi-{runId}-089-Role.csv` terunduh
8. Verifikasi file memuat semua baris (12 baris data, melebihi satu halaman 10 baris, tidak dibatasi halaman)
9. Verifikasi tidak ada toast sukses

### TC-GS-USER-545: Download XLSX

10. Klik icon Download, lalu klik `Download as XLSX`
11. Verifikasi file `Changelog-User-Ahmad-Fauzi-{runId}-089-Role.xlsx` terunduh

### TC-GS-USER-548: Nilai kosong ditulis `-` di file export

12. Klik icon Download, lalu klik `Download as CSV`
13. Buka file CSV yang terunduh (baca isi berkas)
14. Verifikasi sel kosong ditulis `-` (Old Value pada baris Action `Assign` dan New Value pada baris Action `Remove`)

### TC-GS-USER-546: Download mengikuti Search aktif

15. Klik icon Search, ketik `hardw`, tekan Enter
16. Verifikasi baris Role `Manage hardware` tampil di tabel
17. Klik icon Download, lalu klik `Download as CSV`
18. Verifikasi file hanya berisi baris hasil search (2 baris data, keduanya Role `Manage hardware`)
19. Klik icon `(×)`, lalu tekan Enter pada input kosong

### TC-GS-USER-547: Download mengecualikan kolom hidden lalu menyertakannya setelah unhide

20. Klik header kolom Column Visibility (⋯), hilangkan centang `Modified By` pada overlay, lalu tutup overlay
21. Klik icon Download, lalu klik `Download as CSV`
22. Verifikasi file pertama memuat kolom `Date`, `Action`, `Role`, `Field`, `Old Value`, dan `New Value` (pembanding)
23. Verifikasi file pertama tanpa kolom `Modified By`
24. Verifikasi tidak ada toast peringatan
25. Klik header kolom Column Visibility (⋯), centang kembali `Modified By` pada overlay, lalu tutup overlay
26. Klik icon Download, lalu klik `Download as CSV`
27. Verifikasi file kedua memuat kolom `Modified By`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Modal Changelog Role dibuka sekali di langkah 1 sampai 3 untuk semua TC. Tiap unduhan ditangkap ke direktori bersih sehingga berkas dengan nama sama dari unduhan sebelumnya tidak tertukar.
- Spec kelas f (binary buffer): isi berkas CSV dan XLSX dipisah dari kegagalan ekspor. Tidak ada TC kegagalan ekspor di spec ini.
- Urutan TC dalam spec: TC-GS-USER-544, 545, 548, 546, 547. Alasan: TC-GS-USER-548 membaca CSV tanpa Search dan tanpa kolom hidden, sehingga dikerjakan sebelum TC-GS-USER-546 (Search) dan TC-GS-USER-547 (kolom hidden, mengubah preferensi di `localStorage` dan dipulihkan di langkah 25); TC-GS-USER-547 di akhir.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 13 (membaca isi berkas yang terunduh; "Buka file" pada TC-GS-USER-548), langkah 19 (mengosongkan Search dan mereset tabel), serta langkah 20 dan 25 (membuka dan menutup overlay Column Visibility; hide dan unhide adalah aksi TC).
- Langkah 16 dan 22 adalah asersi pembanding tambahan (S-03): langkah 16 memastikan Search sudah menyaring sebelum Download, langkah 22 memastikan berkas pertama berisi kolom lain sebelum asersi ketiadaan `Modified By` di langkah 23 (bagian 8b butir 2).
- Pada TC-GS-USER-546 Expected hanya menuntut isi berkas; jumlah baris hasil search (2) berasal dari seeding (entri 5 dan 6 dengan Role `Manage hardware`).
- TC terbagi lintas spec: perilaku kolom hidden pada Search diverifikasi di spec 084 dan pada Filter di spec 086.
- Temuan untuk QA: (1) TC-GS-USER-544 dan 545 menyebut nama berkas `Changelog-User-Ahmad-Fauzi-Role.csv` dan `.xlsx`; spec memakai user seed bersuffix sehingga nama berkas memuat suffix. Cara PRD §8.2a menuliskan spasi nama dalam nama berkas (tanda hubung) disimpulkan dari TC. (2) TC-GS-USER-544 Expected b "semua baris" tidak menyebut cara mengetahui total entri; spec memakai jumlah entri hasil seeding (12). (3) TC-GS-USER-545 tidak punya Expected tentang isi berkas XLSX; spec hanya mengasersi nama berkas. (4) TC-GS-USER-548 "buka file" tidak menyebut aplikasi atau pembaca; spec membaca isi berkas lewat kemampuan tim FE. (5) TC-GS-USER-547 Expected a "tanpa toast peringatan" tidak menyebut teks toast; spec mengasersi ketiadaan toast. (6) TC-GS-USER-546 dan 547 "keyword" dan "1 kolom" tidak menyebut nilai; spec memakai `hardw` dan `Modified By`.
