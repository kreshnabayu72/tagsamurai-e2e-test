---
id: TC-GS-ACTLOG-E2E-031-filter-tab-user-action-chip-hapus-chip-hapus-centang-dan-overflow
title: "Filter Tab User Action: Chip, Hapus Chip, Hapus Centang, dan Overflow"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-171
  - TC-GS-ACTLOG-172
  - TC-GS-ACTLOG-173
  - TC-GS-ACTLOG-174
coverage:
  web: automated
---

# Filter Tab User Action: Chip, Hapus Chip, Hapus Centang, dan Overflow

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > Activity Log > tab User Action. Hook `before` mengatur ukuran halaman tabel 25 dan viewport desktop lebar 1280 px (dipulihkan di hook `after`).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Akun seeding (hanya untuk aksi lewat API di hook `before`, bukan login UI):
  - Total Control Client A kedua `totalControlSecond_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC2_PASSWORD`.
  - Create+Read `createOnly_automated_qaTeam1@qwertysystem.net` (`Rina M`), `Spectra.env.GS_CREATE_PASSWORD`.
  - Update+Read `updateOnly_automated_qaTeam1@qwertysystem.net` (`Agus W`), `Spectra.env.GS_UPDATE_PASSWORD`.
  - Delete+Read `deleteOnly_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_DELETE_PASSWORD`.
  - Hendra Pratama (`Hendra P`): `Fixture.activityLog.adminHendra` (email ditetapkan tim FE, fixture baru), `Spectra.env.GS_HENDRA_PASSWORD`. Nama literal karena opsi Modified By `Hendra Pratama` adalah data uji TC.
  - Wulan (`Wulan`): `Fixture.activityLog.adminWulan` (email ditetapkan tim FE, fixture baru), `Spectra.env.GS_WULAN_PASSWORD`. Nama literal karena opsi Modified By `Wulan` adalah data uji TC.
- Environment variable: `GS_TC_PASSWORD`, `GS_TC2_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`, `GS_HENDRA_PASSWORD`, `GS_WULAN_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis (dibuat lewat API modul sumber di hook `before`; baris log dihasilkan aksi nyata):
  - Oleh Sari Dewi: Division `Marketing {runId}-031` dan `Finance {runId}-031` (entri Object `Division`, Field `Division Name`); User `Siti Nurbaya {runId}-031` dibuat, Division diubah dari `Marketing {runId}-031` ke `Finance {runId}-031` (entri `Edit` `User`, Field `Division`), lalu dinonaktifkan dan diaktifkan kembali (entri `Deactivate` dan `Activate`); User `Pending User {runId}-031` dibuat dan belum teraktivasi, lalu Resend Activation Email (entri `Resend Activation Email`); Brand `Delete Brand {runId}-031` dibuat.
  - Oleh Sari Dewi, aksi seeding terakhir untuk User: User `John Doe {runId}-031` dibuat (entri `Create` `User`, Field `Name`).
  - Oleh Delete+Read: Brand `Delete Brand {runId}-031` dihapus (entri `Delete` `Brand`, Field `Brand Name`).
  - Oleh Create+Read: Brand `Rina Brand {runId}-031` dibuat. Oleh Update+Read: Brand `Rina Brand {runId}-031` diubah namanya (entri `Edit` `Brand`).
  - Oleh Hendra Pratama: Brand `Hendra Brand {runId}-031` dibuat. Oleh Wulan: Brand `Wulan Brand {runId}-031` dibuat.
  - Oleh Total Control kedua: Position `Position TC2 {runId}-031` dibuat (Object `Position`, Field `Position Name`); oleh Sari Dewi: Measurement `Unit {runId}-031` (Object `Measurement`, Field `Unit Name`) dan Role `Role {runId}-031` (Object `Role & Permission`) dibuat.
- Kemampuan teknis (disediakan tim FE/BE, tanpa mengarang endpoint): seeding di atas menghasilkan minimal enam nilai pada tiap field untuk TC-GS-ACTLOG-174; spec memilih enam pertama yang tertulis berikut (Action: `Create`, `Edit`, `Delete`, `Resend Activation Email`, `Activate`, `Deactivate`; Object: `User`, `Brand`, `Position`, `Measurement`, `Role & Permission`, `Division`; Field: `Name`, `Division`, `Brand Name`, `Position Name`, `Division Name`, `Unit Name`; Modified By: enam pelaku pertama pada tabel "Enam opsi TC-GS-ACTLOG-174"), lihat tabel "Enam opsi TC-GS-ACTLOG-174". Tersedia juga: mengatur ukuran halaman tabel 25 dan viewport 1280 px di hook `before`; mengklik `(X)` pada chip filter; membaca jumlah chip yang tampil dan angka `+N more`.
- Tabel "Opsi TC-GS-ACTLOG-171 sampai 173" (parameter pengulangan langkah 2 sampai 6, 8 sampai 14, dan 16 sampai 22):

| Field | Opsi pertama | Opsi kedua | Baris yang tampil setelah opsi pertama dihapus (TC-GS-ACTLOG-173) | Baris yang tidak tampil |
|---|---|---|---|---|
| Action | `Create` | `Edit` | baris `Edit` `User` `Siti Nurbaya {runId}-031` | baris `Create` `User` `John Doe {runId}-031` |
| Object | `User` | `Brand` | baris Object `Brand` (`Delete` `Delete Brand {runId}-031`) | baris Object `User` (`Create` `John Doe {runId}-031`) |
| Field | `Division` | `Brand Name` | baris Field `Brand Name` (`Delete` `Delete Brand {runId}-031`) | baris Field `Division` (`Edit` `Siti Nurbaya {runId}-031`) |
| Modified By | `Hendra Pratama` | `Wulan` | baris oleh `Wulan` (Brand `Wulan Brand {runId}-031`) | baris oleh `Hendra P` (Brand `Hendra Brand {runId}-031`) |

- Tabel "Enam opsi TC-GS-ACTLOG-174" (parameter pengulangan langkah 25 sampai 29):

| Field | Enam opsi yang dipilih |
|---|---|
| Action | `Create`, `Edit`, `Delete`, `Resend Activation Email`, `Activate`, `Deactivate` |
| Object | `User`, `Brand`, `Position`, `Measurement`, `Role & Permission`, `Division` |
| Field | `Name`, `Division`, `Brand Name`, `Position Name`, `Division Name`, `Unit Name` |
| Modified By | Sari Dewi, Total Control kedua, `Rina M`, `Agus W`, `Hendra Pratama`, `Wulan` (nama lengkap sesuai akun) |

- State global: tidak ada yang diubah selain Filter. State Filter dibersihkan lewat `[Clear Field]` dan `[Apply]` di akhir; cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus User `John Doe {runId}-031`, `Siti Nurbaya {runId}-031`, dan `Pending User {runId}-031`, Brand `Rina Brand`, `Hendra Brand`, `Wulan Brand` bersuffix `-031`, Position, Measurement, Role, dan Division bersuffix `-031`. Entri Activity Log tidak bisa dihapus.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-GS-ACTLOG-171: Chip opsi terpilih muncul di dalam field multi-select

1. Klik icon Filter pada toolbar tab User Action
2. Untuk setiap baris tabel "Opsi TC-GS-ACTLOG-171 sampai 173" (langkah 2 sampai 6): pilih opsi pertama field pada kolom "Field", biarkan field tertutup
3. Verifikasi satu chip berlabel opsi pertama muncul di dalam field
4. Pilih opsi kedua field itu
5. Verifikasi chip kedua muncul di samping chip pertama
6. Verifikasi chip pertama tetap ada (tidak digantikan)

### Pemulihan state antar TC

7. Klik `[Clear Field]` pada Filter Panel

### TC-GS-ACTLOG-172: Hapus chip lewat (X) menghapus centang opsi

8. Untuk setiap baris tabel "Opsi TC-GS-ACTLOG-171 sampai 173" (langkah 8 sampai 14): pilih opsi pertama dan opsi kedua field pada kolom "Field"
9. Klik icon `(X)` pada chip pertama tanpa membuka daftar opsi
10. Verifikasi chip pertama hilang
11. Buka daftar opsi field
12. Verifikasi centang opsi pertama di daftar opsi hilang
13. Verifikasi chip kedua tetap ada
14. Tutup daftar opsi

### Pemulihan state antar TC

15. Klik `[Clear Field]` pada Filter Panel, lalu klik `[Apply]`

### TC-GS-ACTLOG-173: Hapus centang di dalam daftar opsi menghapus chip

16. Untuk setiap baris tabel "Opsi TC-GS-ACTLOG-171 sampai 173" (langkah 16 sampai 22): klik icon Filter, klik `[Clear Field]`, pilih opsi pertama dan opsi kedua field pada kolom "Field"
17. Buka daftar opsi field, hilangkan centang opsi pertama
18. Verifikasi chip opsi pertama langsung hilang dari field (sebelum daftar ditutup)
19. Verifikasi chip kedua tetap ada
20. Tutup daftar opsi, klik `[Apply]`
21. Verifikasi tabel menampilkan baris pada kolom "Baris yang tampil setelah opsi pertama dihapus" tabel itu
22. Verifikasi baris pada kolom "Baris yang tidak tampil" tabel itu tidak tampil

### Pemulihan state antar TC

23. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-GS-ACTLOG-174: Overflow chip banyak opsi terpilih

24. Klik icon Filter
25. Untuk setiap baris tabel "Enam opsi TC-GS-ACTLOG-174" (langkah 25 sampai 29): pilih enam opsi pada kolom "Enam opsi yang dipilih" di field pada kolom "Field", lalu tutup daftar opsi
26. Verifikasi sebagian chip tampil dan sisanya diringkas dalam `+N more`
27. Verifikasi jumlah chip yang tampil ditambah N sama dengan 6
28. Verifikasi field tidak melebar keluar panel
29. Klik `[Clear Field]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan (TC-GS-ACTLOG-172 dan 173 bergantung pada 171 menurut kolom Dependensi).
- Alasan spec di atas smell 35 langkah: 29 langkah nominal, sekitar 101 langkah dieksekusi (langkah 2 sampai 6, 8 sampai 14, 16 sampai 22, dan 25 sampai 29 masing-masing diulang untuk empat field). Semua blok satu topik (field multi-select Filter Panel Tab User Action), satu akun, satu dataset seed, tanpa kelas harness lain; tiap TC berdiri sendiri (Filter dibersihkan di antara TC) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pengulangan: langkah 2 sampai 6, 8 sampai 14, dan 16 sampai 22 diulang untuk empat baris tabel "Opsi TC-GS-ACTLOG-171 sampai 173"; langkah 25 sampai 29 diulang untuk empat baris tabel "Enam opsi TC-GS-ACTLOG-174". Tiap iterasi mengulang `Verifikasi` di dalam blok, sehingga tiap field (empat) punya `Verifikasi` sendiri sesuai butir a sampai d Expected tiap TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7, 15, 23, 29 (membersihkan pilihan Filter antar TC dan antar field), langkah 14 (menutup daftar opsi), langkah 25 (menutup daftar opsi sesudah memilih enam opsi, supaya ringkasan `+N more` diamati pada field dalam keadaan tertutup), dan awal langkah 16 (membuka Filter dan `[Clear Field]` pada tiap iterasi supaya hasil `[Apply]` tiap field terpisah; bukan dari TC).
- Asersi tambahan di luar Expected TC, dengan alasan: langkah 22 (baris pada opsi pertama tidak tampil) merinci Expected "hasil tabel hanya mengikuti opsi kedua" dan didahului langkah 21 (baris opsi kedua tampil) sebagai anchor positif.
- Pembagian TC: TC-GS-ACTLOG-159 sampai 164 ada di spec 029; TC-GS-ACTLOG-165 sampai 167 dan 170 ada di spec 030.
- Temuan untuk QA:
  - PRD belum menetapkan apakah Filter Panel menutup sesudah [Apply]; langkah klik icon Filter pada langkah 16 dan 23 mengikuti TC-GS-ACTLOG-173 (diawali klik icon Filter; pada langkah 16 sebagai penghubung per iterasi).
  - TC-GS-ACTLOG-174 menuntut "minimal 6 opsi" pada tiap field tanpa menyebut nilainya; spec men-seed dan memilih enam nilai per field yang ditulis pada tabel "Enam opsi TC-GS-ACTLOG-174". Nilai Field `Position Name`, `Division Name`, dan `Unit Name` mengikuti Changelog modul Position, Division, dan Measurement.
  - TC-GS-ACTLOG-171 sampai 173 memakai Modified By literal `Hendra Pratama` dan `Wulan`; nama env `GS_HENDRA_PASSWORD` dan `GS_WULAN_PASSWORD` belum ada di `.env.example`.
  - TC-GS-ACTLOG-172 Expected a menyatakan "centang opsi pertama di daftar opsi hilang" untuk empat field tanpa merinci cara mengamatinya (checkbox pada daftar); spec membuka daftar opsi setelah klik `(X)`.
