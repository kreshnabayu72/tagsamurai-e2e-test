---
id: TC-GS-ACTLOG-E2E-027-search-tab-user-action-kolom-teks-case-nama-trim-multi-kolom
title: "Search Tab User Action: Kolom Teks, Case, Nama, Trim, Multi-kolom"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-150
  - TC-GS-ACTLOG-151
  - TC-GS-ACTLOG-152
  - TC-GS-ACTLOG-153
  - TC-GS-ACTLOG-156
  - TC-GS-ACTLOG-157
coverage:
  web: automated
---

# Search Tab User Action: Kolom Teks, Case, Nama, Trim, Multi-kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > Activity Log > tab User Action. Hook `before` mengatur ukuran halaman tabel 25 supaya baris seeding berada di halaman 1 (urutan default tabel: Date terbaru di atas).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Akun seeding (hanya untuk aksi lewat API di hook `before`, bukan login UI), admin Client A dengan akses yang cukup untuk aksi seeding di bawah. Nama literal karena asersi memakai singkatan `Hendra P`, `Wulan S` dan kata kunci `hendra`, `pratama`, `WULAN`, `Sari`:
  - Hendra Pratama (`Hendra P`): `Fixture.activityLog.adminHendra` (email ditetapkan tim FE, fixture baru), `Spectra.env.GS_HENDRA_PASSWORD`.
  - Wulan (`Wulan`): `Fixture.activityLog.adminWulan` (email ditetapkan tim FE, fixture baru), `Spectra.env.GS_WULAN_PASSWORD`.
  - Wulan Sari (`Wulan S`): `Fixture.activityLog.adminWulanSari` (email ditetapkan tim FE, fixture baru), `Spectra.env.GS_WULANSARI_PASSWORD`.
- Environment variable: `GS_TC_PASSWORD`, `GS_HENDRA_PASSWORD`, `GS_WULAN_PASSWORD`, `GS_WULANSARI_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis (dibuat lewat API modul sumber di hook `before`, berurutan; baris log dihasilkan aksi nyata, bukan disisipkan):
  - Oleh Sari Dewi: Division `Marketing {runId}-027` dan `Finance {runId}-027`; Position `Finance Manager {runId}-027` (entri `Create` `Position` `Finance Manager {runId}-027`, dipakai TC-GS-ACTLOG-157).
  - Oleh Sari Dewi: Brand `Acme {runId}-027` dibuat lalu dihapus (entri `Delete` `Brand` `Acme {runId}-027`, Field `Brand Name`, New Value `—`).
  - Oleh Hendra Pratama: Brand `Hendra Brand {runId}-027` dibuat (entri Modified By `Hendra P`).
  - Oleh Wulan: Brand `Wulan Brand {runId}-027` dibuat (entri Modified By `Wulan`).
  - Oleh Wulan Sari: Brand `Wulan Sari Brand {runId}-027` dibuat (entri Modified By `Wulan S`).
  - Oleh Sari Dewi: User `Siti Nurbaya {runId}-027` dibuat lalu Division diubah dari `Marketing {runId}-027` ke `Finance {runId}-027` (entri `Edit` `User` `Siti Nurbaya {runId}-027` `Division` `Marketing {runId}-027` `Finance {runId}-027`).
  - Oleh Sari Dewi, aksi seeding terakhir: User `John Doe {runId}-027` dibuat (entri `Create` `User` `John Doe {runId}-027` `Name` `—` `John Doe {runId}-027`).
  - Nama `John Doe`, `Siti Nurbaya`, `Acme`, `Marketing`, `Finance` bersuffix; kata kunci pada tabel di bawah tetap memakai kata dari TC, sehingga baris milik spec lain yang memuat kata sama boleh ikut tampil. Asersi hanya pada baris milik spec ini.
- Tabel "Kata kunci TC-GS-ACTLOG-150" (satu kolom per baris; parameter pengulangan langkah 1 sampai 3):

| Kolom | Kata kunci | Baris yang tampil |
|---|---|---|
| Action | `Edit` | baris `Edit` milik `Siti Nurbaya {runId}-027` |
| Object | `Brand` | baris Object `Brand` (`Delete` `Acme {runId}-027`) |
| Name | `Siti` | baris dengan Name `Siti Nurbaya {runId}-027` |
| Field | `Division` | baris dengan Field `Division` (`Edit` `Siti Nurbaya {runId}-027`) |
| Old Value | `Marketing` | baris dengan Old Value `Marketing {runId}-027` |
| New Value | `Finance` | baris dengan New Value `Finance {runId}-027` |

- Tabel "Kata kunci TC-GS-ACTLOG-151" (kapitalisasi berbeda dari nilai tersimpan; parameter pengulangan langkah 4 sampai 6):

| Kolom | Kata kunci | Baris yang tampil |
|---|---|---|
| Action | `EDIT` | baris `Edit` milik `Siti Nurbaya {runId}-027` |
| Object | `brand` | baris Object `Brand` (`Delete` `Acme {runId}-027`) |
| Name | `SITI` | baris dengan Name `Siti Nurbaya {runId}-027` |
| Field | `division` | baris dengan Field `Division` (`Edit` `Siti Nurbaya {runId}-027`) |
| Old Value | `marketing` | baris dengan Old Value `Marketing {runId}-027` |
| New Value | `FINANCE` | baris dengan New Value `Finance {runId}-027` |

- Kemampuan teknis: mengatur ukuran halaman tabel 25 di hook `before` (klik pilihan jumlah baris per halaman); mengetik di kotak Search dengan spasi di awal dan akhir; membaca isi kotak Search apa adanya (tanpa trim).
- State global: tidak ada yang diubah selain Search. State Search dibersihkan lewat langkah penghubung; cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus User `John Doe {runId}-027` dan `Siti Nurbaya {runId}-027`, Brand `Hendra Brand`, `Wulan Brand`, `Wulan Sari Brand` bersuffix `-027`, Position `Finance Manager {runId}-027`, Division `Marketing {runId}-027` dan `Finance {runId}-027`. Entri Activity Log tidak bisa dihapus.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-GS-ACTLOG-150: Search substring pada kolom teks Tab User Action

1. Untuk setiap baris tabel "Kata kunci TC-GS-ACTLOG-150" (langkah 1 sampai 3): ketik Search kata kunci pada kolom "Kata kunci", tekan Enter
2. Verifikasi tabel menampilkan baris pada kolom "Baris yang tampil" tabel itu
3. Kosongkan isi kotak Search, tekan Enter

### TC-GS-ACTLOG-151: Search tidak membedakan huruf besar dan kecil pada kolom teks Tab User Action

4. Untuk setiap baris tabel "Kata kunci TC-GS-ACTLOG-151" (langkah 4 sampai 6): ketik Search kata kunci pada kolom "Kata kunci", tekan Enter
5. Verifikasi tabel menampilkan baris pada kolom "Baris yang tampil" tabel itu
6. Kosongkan isi kotak Search, tekan Enter

### TC-GS-ACTLOG-152: Search pada kolom Modified By memakai kata dari nama depan

7. Ketik Search `hendra`, tekan Enter
8. Verifikasi tabel menampilkan baris Modified By `Hendra P` (Brand `Hendra Brand {runId}-027`)
9. Verifikasi baris Modified By `Wulan` (Brand `Wulan Brand {runId}-027`) tidak tampil
10. Ganti isi kotak search dengan `WULAN`, tekan Enter
11. Verifikasi tabel menampilkan baris Modified By `Wulan` (Brand `Wulan Brand {runId}-027`)
12. Verifikasi baris Modified By `Hendra P` (Brand `Hendra Brand {runId}-027`) tidak tampil

### TC-GS-ACTLOG-153: Search kolom Modified By memakai kata dari nama belakang

13. Ganti isi kotak search dengan `pratama`, tekan Enter
14. Verifikasi tabel menampilkan baris Modified By `Hendra P` (Brand `Hendra Brand {runId}-027`)
15. Verifikasi baris Modified By `Wulan S` (Brand `Wulan Sari Brand {runId}-027`) tidak tampil
16. Ganti isi kotak search dengan `Sari`, tekan Enter
17. Verifikasi tabel menampilkan baris Modified By `Wulan S` (Brand `Wulan Sari Brand {runId}-027`)
18. Verifikasi baris Modified By `Hendra P` (Brand `Hendra Brand {runId}-027`) tidak tampil

### TC-GS-ACTLOG-156: Search memangkas spasi di awal dan akhir kata kunci

19. Ganti isi kotak search dengan `Brand`, tekan Enter, catat daftar baris yang tampil sebagai pembanding
20. Ganti isi kotak search dengan `  Brand  ` (dua spasi di awal dan di akhir), tekan Enter
21. Verifikasi tabel menampilkan daftar baris yang identik dengan pembanding dari kata kunci `Brand`
22. Verifikasi isi kotak Search tetap `  Brand  `
23. Ganti isi kotak search dengan tiga spasi saja, tekan Enter
24. Verifikasi tabel kembali menampilkan data tanpa saringan pencarian (baris `Create` `User` `John Doe {runId}-027` tampil)

### TC-GS-ACTLOG-157: Satu kata kunci cocok pada beberapa kolom sekaligus

25. Ganti isi kotak search dengan `finance`, tekan Enter
26. Verifikasi baris `Edit` `Siti Nurbaya {runId}-027` tampil (cocok di New Value)
27. Verifikasi baris `Create` `Position` `Finance Manager {runId}-027` tampil (cocok di Name dan New Value)
28. Verifikasi baris `Delete` `Brand` `Acme {runId}-027` tidak tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Alasan spec di atas smell 35 langkah: 28 langkah nominal, sekitar 58 langkah dieksekusi (langkah 1 sampai 3 dan 4 sampai 6 masing-masing diulang untuk enam kolom). Semua blok satu topik (Search Tab User Action), satu akun, satu dataset seed, tanpa kelas harness lain, dan tiap iterasi berdiri sendiri sehingga kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Pengulangan: langkah 1 sampai 3 diulang untuk enam baris tabel "Kata kunci TC-GS-ACTLOG-150" dan langkah 4 sampai 6 untuk enam baris tabel "Kata kunci TC-GS-ACTLOG-151"; tiap iterasi mengulang `Verifikasi` langkah 2 dan 5, sehingga tiap kolom (enam) punya `Verifikasi` sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 3 dan 6 (kotak Search dikosongkan di antara iterasi sesuai TC-GS-ACTLOG-150 langkah 1). Langkah 10, 13, 16, 19, 20, 23, 25 mengganti isi kotak Search yang sudah terbuka, sehingga tidak ada langkah pemulihan state tersendiri antar TC. Langkah 19 (kata kunci `Brand` sebagai pembanding) bukan dari TC: TC-GS-ACTLOG-156 menyatakan "hasil identik dengan kata kunci `Brand`" tanpa menyebut cara membandingkan.
- Seeding memakai nama bersuffix `{runId}-027` untuk subjek log; kata kunci memakai kata TC (`Siti`, `Brand`, `finance`) sehingga baris milik spec lain yang memuat kata sama boleh ikut tampil. Asersi "tidak tampil" hanya untuk baris milik spec ini dan didahului asersi baris yang tampil pada pencarian yang sama (anchor).
- Pembagian TC: TC-GS-ACTLOG-154, 155, 158 (Search Date, visibilitas kolom, siklus kotak Search) ada di spec 028.
- Temuan untuk QA:
  - TC-GS-ACTLOG-152 dan 153 memakai Modified By literal (`Hendra Pratama`, `Wulan`, `Wulan Sari`); kapabilitas ketiga admin tidak disebut TC, spec mengasumsikan cukup untuk membuat Brand. Nama env `GS_HENDRA_PASSWORD`, `GS_WULAN_PASSWORD`, `GS_WULANSARI_PASSWORD` belum ada di `.env.example`.
  - TC-GS-ACTLOG-153: kata kunci `Sari` juga cocok dengan nama lengkap aktor Total Control `Sari Dewi` (`Sari D`) bila ada baris miliknya; asersi dibatasi pada baris `Wulan S` dan `Hendra P` milik spec ini.
  - TC-GS-ACTLOG-156 langkah 1 tidak menyebut pembanding hasil `Brand`; spec menambah langkah 19 (lihat di atas).
