---
id: TC-GS-ACTLOG-E2E-029-filter-tab-user-action-struktur-or-and-search-dan-filter-berurutan
title: "Filter Tab User Action: Struktur, OR, AND, Search dan Filter Berurutan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-159
  - TC-GS-ACTLOG-160
  - TC-GS-ACTLOG-161
  - TC-GS-ACTLOG-162
  - TC-GS-ACTLOG-163
  - TC-GS-ACTLOG-164
coverage:
  web: automated
---

# Filter Tab User Action: Struktur, OR, AND, Search dan Filter Berurutan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; ini akun default suite sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > Activity Log > tab User Action. Hook `before` mengatur ukuran halaman tabel 25 supaya baris seeding berada di halaman 1 (urutan default tabel: Date terbaru di atas).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Akun seeding (hanya untuk aksi lewat API di hook `before`, bukan login UI), admin Client A dengan akses yang cukup untuk aksi seeding. Nama literal karena opsi Filter Modified By `Hendra Pratama` dan `Wulan` adalah bagian asersi TC-GS-ACTLOG-160:
  - Hendra Pratama (`Hendra P`): `Fixture.activityLog.adminHendra` (email ditetapkan tim FE, fixture baru), `Spectra.env.GS_HENDRA_PASSWORD`.
  - Wulan (`Wulan`): `Fixture.activityLog.adminWulan` (email ditetapkan tim FE, fixture baru), `Spectra.env.GS_WULAN_PASSWORD`.
- Environment variable: `GS_TC_PASSWORD`, `GS_HENDRA_PASSWORD`, `GS_WULAN_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Dinamis (dibuat lewat API modul sumber di hook `before`, berurutan; baris log dihasilkan aksi nyata):
  - Oleh Sari Dewi: Division `Marketing {runId}-029` dan `Finance {runId}-029`.
  - Oleh Hendra Pratama: Brand `Acme {runId}-029` dibuat (entri `Create` `Brand` `Acme {runId}-029`), lalu diubah namanya menjadi `Acme {runId}-029 Renamed` (entri `Edit` `Brand`, Field `Brand Name`).
  - Oleh Wulan: Brand `Acme {runId}-029 Renamed` dihapus (entri `Delete` `Brand`, Field `Brand Name`).
  - Oleh Hendra Pratama: User `Siti Nurbaya {runId}-029` dibuat lalu Division diubah dari `Marketing {runId}-029` ke `Finance {runId}-029` (entri `Edit` `User`, Field `Division`).
  - Oleh Hendra Pratama, aksi seeding terakhir: User `John Doe {runId}-029` dibuat (entri `Create` `User`, Field `Name`).
  - Pada langkah di bawah, "baris Acme" berarti baris yang Name, Old Value, atau New Value-nya memuat `Acme {runId}-029`. Kata kunci Search TC-GS-ACTLOG-163 dan 164 memakai nama itu (`Acme {runId}-029`) sebagai ganti `Acme` literal TC, supaya baris Brand `Acme` milik spec lain pada Client A tidak ikut tampil. Alasan nama literal tidak dipakai: asersi "hanya baris `Edit` `Brand` `Acme`" tidak benar pada Client A yang dipakai bersama seluruh suite.
- Tabel "Pilihan TC-GS-ACTLOG-160 dengan baris tidak tampil" (parameter pengulangan langkah 13 sampai 17):

| Field | Opsi pertama | Opsi kedua | Baris opsi pertama | Baris opsi kedua | Baris yang tidak tampil |
|---|---|---|---|---|---|
| Action | `Create` | `Delete` | baris `Create` (`Create` `Brand` Acme, `Create` `User` `John Doe {runId}-029`) | baris `Delete` (`Delete` `Brand` Acme) | baris `Edit` `User` `Siti Nurbaya {runId}-029` |
| Field | `Division` | `Brand Name` | baris Field `Division` (`Edit` `Siti Nurbaya {runId}-029`) | baris Field `Brand Name` (`Delete` Acme) | baris Field `Name` (`Create` `John Doe {runId}-029`) |

- Tabel "Pilihan TC-GS-ACTLOG-160 tanpa baris tidak tampil" (TC tidak menyebut baris yang tidak tampil; parameter pengulangan langkah 18 sampai 21):

| Field | Opsi pertama | Opsi kedua | Baris opsi pertama | Baris opsi kedua |
|---|---|---|---|---|
| Object | `User` | `Brand` | baris Object `User` (`Create` `John Doe {runId}-029`) | baris Object `Brand` (`Delete` Acme) |
| Modified By | `Hendra Pratama` | `Wulan` | baris oleh `Hendra P` (`Create` `John Doe {runId}-029`) | baris oleh `Wulan` (`Delete` Acme) |

- Kemampuan teknis: mengatur ukuran halaman tabel 25 di hook `before` (klik pilihan jumlah baris per halaman); memilih opsi pada field multi-select Filter Panel; membaca keadaan icon Filter (gelap saat panel terbuka).
- State global: tidak ada yang diubah selain Filter dan Search. State Filter dan Search dibersihkan lewat langkah pemulihan; cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus User `John Doe {runId}-029` dan `Siti Nurbaya {runId}-029`, Division `Marketing {runId}-029` dan `Finance {runId}-029`. Entri Activity Log tidak bisa dihapus.
- Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-GS-ACTLOG-159: Struktur Filter Panel Tab User Action

1. Klik icon Filter pada toolbar tab User Action
2. Verifikasi field berurutan dari atas ke bawah: `Date`, `Action`, `Object`, `Field`, `Modified By`
3. Verifikasi field `Date` berupa date range picker dengan placeholder `"Select date"`
4. Verifikasi field `Action` berupa multi-select searchable dengan placeholder `"All actions"`
5. Verifikasi field `Object` berupa multi-select searchable dengan placeholder `"All objects"`
6. Verifikasi field `Field` berupa multi-select searchable dengan placeholder `"All fields"`
7. Verifikasi field `Modified By` berupa multi-select searchable dengan placeholder `"All users"`
8. Verifikasi tombol `[Clear Field]` berada di kiri footer panel
9. Verifikasi tombol `[Apply]` berada di kanan footer panel
10. Verifikasi icon Filter di toolbar berubah gelap saat panel terbuka
11. Verifikasi kolom `Name`, `Old Value`, dan `New Value` tidak punya field di Filter Panel
12. Klik icon Filter untuk menutup Filter Panel

### TC-GS-ACTLOG-160: Filter multi-select, dua opsi dalam satu field memakai logika OR

13. Untuk setiap baris tabel "Pilihan TC-GS-ACTLOG-160 dengan baris tidak tampil" (langkah 13 sampai 17): klik icon Filter, pilih opsi pertama dan opsi kedua pada field kolom "Field", klik `[Apply]`
14. Verifikasi tabel menampilkan baris pada kolom "Baris opsi pertama" tabel itu
15. Verifikasi tabel menampilkan baris pada kolom "Baris opsi kedua" tabel itu
16. Verifikasi baris pada kolom "Baris yang tidak tampil" tabel itu tidak tampil
17. Klik `[Clear Field]`, klik `[Apply]`
18. Untuk setiap baris tabel "Pilihan TC-GS-ACTLOG-160 tanpa baris tidak tampil" (langkah 18 sampai 21): klik icon Filter, pilih opsi pertama dan opsi kedua pada field kolom "Field", klik `[Apply]`
19. Verifikasi tabel menampilkan baris pada kolom "Baris opsi pertama" tabel itu
20. Verifikasi tabel menampilkan baris pada kolom "Baris opsi kedua" tabel itu
21. Klik `[Clear Field]`, klik `[Apply]`

### TC-GS-ACTLOG-161: Filter dua field berbeda memakai logika AND

22. Klik icon Filter, pilih Action `Edit` dan Object `User`, klik `[Apply]`
23. Verifikasi baris `Edit` `User` `Siti Nurbaya {runId}-029` tampil
24. Verifikasi baris `Edit` `Brand` (Acme) tidak tampil
25. Verifikasi baris `Create` `User` `John Doe {runId}-029` tidak tampil

### Pemulihan state antar TC

26. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-GS-ACTLOG-162: OR dalam satu field dan AND antar field dalam satu penerapan

27. Klik icon Filter, pilih Action `Create` dan `Delete`, pilih Object `Brand`, klik `[Apply]`
28. Verifikasi baris `Create` `Brand` (Acme) tampil
29. Verifikasi baris `Delete` `Brand` (Acme) tampil
30. Verifikasi baris `Edit` `Brand` (Acme) tidak tampil
31. Verifikasi baris `Create` `User` `John Doe {runId}-029` tidak tampil

### Pemulihan state antar TC

32. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-GS-ACTLOG-163: Alur Search lalu Filter

33. Ketik Search `Acme {runId}-029`, tekan Enter
34. Klik icon Filter, pilih Action `Edit`, klik `[Apply]`
35. Verifikasi tabel hanya memuat baris `Edit` `Brand` (Acme)
36. Verifikasi baris `Delete` `Brand` (Acme) tidak tampil
37. Verifikasi baris `Edit` `User` `Siti Nurbaya {runId}-029` tidak tampil
38. Verifikasi kata kunci `Acme {runId}-029` tetap ada di kotak Search

### Pemulihan state antar TC

39. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`; klik `(←)` pada kotak Search (menutup kotak dan mereset tabel)

### TC-GS-ACTLOG-164: Alur Filter lalu Search

40. Klik icon Filter, pilih Action `Edit`, klik `[Apply]`
41. Ketik Search `Acme {runId}-029`, tekan Enter
42. Verifikasi tabel hanya memuat baris `Edit` `Brand` (Acme) (irisan Filter dan Search)
43. Verifikasi baris `Delete` `Brand` (Acme) tidak tampil
44. Verifikasi baris `Edit` `User` `Siti Nurbaya {runId}-029` tidak tampil
45. Klik icon Filter
46. Verifikasi Filter Action `Edit` tetap aktif (chip `Edit` pada field Action)

## Notes

- Mode: FE+BE. Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Alasan spec di atas smell 35 langkah: 46 langkah nominal, sekitar 55 langkah dieksekusi (langkah 13 sampai 17 diulang untuk dua field dan langkah 18 sampai 21 untuk dua field). Semua blok satu topik (Filter dan Search Tab User Action), satu akun, satu dataset seed, tanpa kelas harness lain; tiap TC berdiri sendiri (Filter dan Search dibersihkan di antara TC) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Sebagian besar langkah adalah `Verifikasi` hasil pecahan klausa Expected (S-01).
- Pengulangan: langkah 13 sampai 17 diulang untuk dua baris tabel "Pilihan TC-GS-ACTLOG-160 dengan baris tidak tampil" (Action, Field) dan langkah 18 sampai 21 untuk dua baris tabel "Pilihan TC-GS-ACTLOG-160 tanpa baris tidak tampil" (Object, Modified By); tabel dipisah supaya tidak ada langkah bersyarat. Urutan field dalam pengulangan (Action, Field, Object, Modified By) berbeda dari urutan Expected TC (Action, Object, Field, Modified By). Tiap iterasi mengulang `Verifikasi` langkah 14, 15, 16 dan 19, 20, sehingga tiap field (empat) dan tiap opsi punya `Verifikasi` sendiri.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 12 (menutup Filter Panel sebelum TC-GS-ACTLOG-160), langkah 17 dan 21 (Clear Field di akhir tiap iterasi; mengikuti TC-GS-ACTLOG-160 "klik [Clear Field] dan [Apply]" tanpa membuka ulang panel), langkah 26, 32, 39 (pemulihan Filter dan Search antar TC).
- Asersi tambahan di luar Expected TC, dengan alasan: asersi "tidak tampil" TC-GS-ACTLOG-163 dan 164 untuk baris `Delete` `Brand` dan `Edit` `User` merinci Expected "hanya baris `Edit` `Brand` `Acme`" pada Client A; tiap asersi "tidak tampil" didahului asersi baris yang tampil pada penyaringan yang sama (anchor).
- Kata kunci Search TC-GS-ACTLOG-163 dan 164 memakai `Acme {runId}-029` (nama bersuffix) sebagai ganti `Acme` literal; lihat Prerequisites.
- Pembagian TC: TC-GS-ACTLOG-165 sampai 167 dan 170 (opsi filter dari data dan pencarian opsi) ada di spec 030; TC-GS-ACTLOG-171 sampai 174 (chip dan overflow) ada di spec 031.
- Temuan untuk QA:
  - PRD belum menetapkan apakah Filter Panel menutup sesudah [Apply]; langkah klik icon Filter pada langkah 13, 18, 22, 27, 34, dan 40 mengikuti TC-GS-ACTLOG-160 sampai 164, sedangkan langkah 26, 32, dan 39 (pemulihan antar TC) mengasumsikan panel tertutup sesudah [Apply] seperti TC-GS-ACTLOG-161 sampai 163 yang diawali klik icon Filter; langkah 17 dan 21 mengikuti TC-GS-ACTLOG-160 (tanpa klik icon Filter).
  - TC-GS-ACTLOG-160 memakai Modified By literal `Hendra Pratama` dan `Wulan`; nama env `GS_HENDRA_PASSWORD` dan `GS_WULAN_PASSWORD` belum ada di `.env.example`.
  - TC-GS-ACTLOG-163 dan 164 menyebut entri `Edit` `Brand` `Acme` dan `Delete` `Brand` `Acme` tanpa menyebut bahwa Brand hanya punya satu field (`Brand Name`); `Edit` terjadi lewat penggantian nama sehingga Name pada baris `Edit` bisa nama lama atau nama baru. Spec mengidentifikasi baris lewat `Acme {runId}-029` pada Name, Old Value, atau New Value.
  - TC-GS-ACTLOG-159 Expected c menyebut icon Filter "berubah gelap" tanpa kriteria visual yang terukur (warna atau atribut); spec meminta tim FE menyediakan penanda state (mis. atribut aria).
