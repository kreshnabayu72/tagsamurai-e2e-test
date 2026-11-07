---
id: TC-FA-SU-E2E-156-sub-tab-assigned-assets-setup-column-bagian-1
title: "Sub-tab Assigned Assets: Setup Column (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-459
  - TC-FA-SU-460
coverage:
  web: automated
---

# Sub-tab Assigned Assets: Setup Column (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` (#20) dan Responsibilities (#24): Detail Budi Santoso dengan Sub-tab Assigned Assets 5 baris (satu halaman). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE). Pre-setup #24 hanya menyebut "5 baris"; nilai kolom di bawah diturunkan dari Expected TC (Asset ID dan Transaction ID hanya tertulis sebagian):

| Name | Asset ID | Transaction ID | Brand | Model / Type | PIC |
|---|---|---|---|---|---|
| `AC Split Ruang Kerja` | tidak tertulis | tidak tertulis | `Daikin` | `1PK` | `Ahmad D` |
| `Lemari Arsip` | tidak tertulis | tidak tertulis | `Lion` | `2 Pintu` | `Citra L` |
| `Meja Kerja Kepala Divisi` | tidak tertulis | `ASG-20260505` | `Modera` | `Executive` | `Ahmad D` |
| `Printer Multifungsi` | tidak tertulis | tidak tertulis | `Canon` | `PIXMA G3010` | `Citra L` |
| `Server Rack Mini` | `AST-02113` | tidak tertulis | `HP` | `ProLiant DL20` | `Eka W` (Eka Wulandari) |
- Data Dinamis: tidak ada.
- State global: tidak ada yang diubah; spec hanya membaca Pre-setup. Suite berjalan serial (`parallel: false`).
- Tabel parameter "Kolom Disembunyikan" (dipakai langkah 5 sampai 6):

| Kolom |
|---|
| `Photo` |
| `Name` |
| `Asset ID` |
| `Transaction ID` |
| `Brand` |
| `PIC` |

Kolom `Model / Type` tetap visible sebagai satu-satunya kolom pada langkah penguji batas. Kolom `Model / Type` dan `Photo` dipakai pada putaran kedua (centang `Photo`, uncheck `Model / Type`) karena kolom yang tersisa sebagai satu-satunya kolom visible tidak dapat di-uncheck.
- Tabel parameter "Geser Kolom" (dipakai langkah 32 sampai 33):

| Kolom | Arah | Posisi (sebelum ke sesudah geser) | Posisi akhir tabel |
|---|---|---|---|
| `Photo` | bawah | 1 ke 2 | 7 |
| `Asset ID` | atas | 3 ke 2 | 1 |
| `Transaction ID` | atas | 4 ke 3 | 3 |
| `Brand` | atas | 5 ke 4 | 4 |
| `Model / Type` | atas | 6 ke 5 | 5 |
| `PIC` | atas | 7 ke 6 | 6 |
| `Name` | bawah | 1 ke 2 | 2 |

Urutan awal: `Photo`, `Name`, `Asset ID`, `Transaction ID`, `Brand`, `Model / Type`, `PIC`. Baris diproses dari atas ke bawah secara kumulatif; urutan akhir: `Asset ID`, `Name`, `Transaction ID`, `Brand`, `Model / Type`, `PIC`, `Photo`.
- Kemampuan menghapus preferensi kolom Setup Column di browser (disediakan tim FE): dipakai sebagai langkah pemulihan dan di hook `after` untuk tabel yang konfigurasinya disimpan spec ini (bagian 4 konvensi). Konfigurasi kolom tersimpan per perangkat dan per tabel.

## Test Steps

### TC-FA-SU-459: Ceklis dan unceklis Setup Column Sub-tab Assigned Assets kelas Hideable (default tampil)

1. Ketik Search `Budi Santoso`, tekan Enter, lalu klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Assigned Assets
3. Klik header kolom Actions (⋯)
4. Klik `Setup Column...`
5. Untuk setiap baris tabel parameter "Kolom Disembunyikan" (langkah 5 sampai 6): uncheck kolom itu pada popup Setup Column
6. Verifikasi kolom itu hilang dari Live Preview
7. Hover checkbox kolom `Model / Type` (satu-satunya kolom visible)
8. Verifikasi checkbox kolom `Model / Type` disabled dengan tooltip `At least one column must remain visible.`
9. Klik `[Save]`
10. Untuk setiap baris tabel parameter "Kolom Disembunyikan" (langkah 10): Verifikasi kolom itu tidak tampil di tabel
11. Tekan F5 pada halaman Detail
12. Klik tab Responsibilities, lalu klik Sub-tab Assigned Assets
13. Untuk setiap baris tabel parameter "Kolom Disembunyikan" (langkah 13): Verifikasi kolom itu tetap tidak tampil di tabel setelah F5
14. Klik header kolom Actions (⋯)
15. Klik `Setup Column...`
16. Check kolom `Photo` pada popup Setup Column
17. Verifikasi kolom `Photo` tampil di Live Preview
18. Uncheck kolom `Model / Type` pada popup Setup Column
19. Verifikasi kolom `Model / Type` hilang dari Live Preview
20. Klik `[Save]`
21. Verifikasi kolom `Photo` tampil di tabel
22. Verifikasi kolom `Model / Type` tidak tampil di tabel
23. Tekan F5 pada halaman Detail
24. Klik tab Responsibilities, lalu klik Sub-tab Assigned Assets
25. Verifikasi kolom `Photo` tetap tampil di tabel setelah F5
26. Verifikasi kolom `Model / Type` tetap tidak tampil di tabel setelah F5
27. Pulihkan konfigurasi kolom tabel Assigned Assets: hapus preferensi kolom di browser
28. Tekan F5 pada halaman Detail
29. Klik tab Responsibilities, lalu klik Sub-tab Assigned Assets

### TC-FA-SU-460: Geser (drag reorder) Setup Column Sub-tab Assigned Assets kelas Hideable (default tampil)

30. Klik header kolom Actions (⋯)
31. Klik `Setup Column...`
32. Untuk setiap baris tabel parameter "Geser Kolom" (langkah 32 sampai 33): geser kolom itu satu posisi sesuai kolom Arah pada tabel parameter
33. Verifikasi urutan Live Preview berubah: kolom itu berpindah satu posisi sesuai kolom Posisi pada tabel parameter
34. Klik `[Save]`
35. Untuk setiap baris tabel parameter "Geser Kolom" (langkah 35): Verifikasi kolom itu berada di posisi akhir sesuai tabel parameter pada tabel
36. Tekan F5 pada halaman Detail
37. Klik tab Responsibilities, lalu klik Sub-tab Assigned Assets
38. Untuk setiap baris tabel parameter "Geser Kolom" (langkah 38): Verifikasi kolom itu tetap berada di posisi akhir setelah F5
39. Pulihkan konfigurasi kolom tabel Assigned Assets: hapus preferensi kolom di browser
40. Tekan F5 pada halaman Detail
41. Klik tab Responsibilities, lalu klik Sub-tab Assigned Assets

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): Search nama `Budi Santoso` serta pembukaan Detail dan sub-tab (langkah 1 dan 2) serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Langkah 5 sampai 6, 10, 13, 32 sampai 33, 35, dan 38 diulang per baris tabel parameter (bagian 8b butir 7); `Verifikasi` tetap satu per klausa (Live Preview, tabel, setelah F5) tiap kolom. Konfigurasi kolom disimpan sekali per putaran `[Save]` karena kolom tersisa sebagai satu-satunya kolom visible tidak dapat di-uncheck.
- Langkah pemulihan konfigurasi kolom (27 dan 39) dan F5 sesudahnya memulihkan tabel ke default sebelum blok berikutnya (S-09); hook `after` mengulang pemulihan sebagai cadangan.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (85 langkah, 41 langkah nominal). Seluruhnya satu kelas (fungsional/screening sub-tab Assigned Assets (Setup Column), satu akun, data Pre-setup sama, tanpa mengubah data Pre-setup), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain. Satu pembukaan Detail dipakai bersama seluruh blok.
- Pembagian TC lintas spec: TC-FA-SU-461 dan 462 ada di spec 157; TC-FA-SU-457 dan 458 (screening) ada di spec 155.
- Temuan untuk QA (S-15):
  - TC-FA-SU-459 dan 460 mensyaratkan setiap kolom diubah lalu `[Save]`, sedangkan kolom terakhir yang visible tidak dapat di-uncheck (Expected h TC-FA-SU-459). Spec mengubah enam kolom lalu menguji batas kolom `Model / Type`, kemudian memakai putaran kedua untuk kolom `Photo` dan `Model / Type`.
  - TC-FA-SU-460 tidak menyebut arah geser dan posisi tujuan tiap kolom; spec memakai urutan geser kumulatif pada tabel parameter "Geser Kolom".
  - Langkah Uji TC-FA-SU-459 dan 460 menyebut F5 tanpa menyebut tab dan sub-tab aktif setelah muat ulang; spec membuka kembali tab Responsibilities dan sub-tab sebelum mengasersi.
