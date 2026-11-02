---
id: TC-FA-GRP-E2E-106-groups-list-search-per-kolom-group-code-function-nilai-penuh-none-dan-disposal-group
title: "Groups List Search per Kolom Group, Code, Function (Nilai Penuh None dan Disposal Group)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-337
  - TC-FA-GRP-338
  - TC-FA-GRP-339
  - TC-FA-GRP-419
  - TC-FA-GRP-420
coverage:
  web: automated
---

# Groups List Search per Kolom Group, Code, Function (Nilai Penuh None dan Disposal Group)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-106`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-106` | `V106L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-106` | `V106K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-106` | `V106J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-106` | `V106I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-106` | `V106H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-106` | `V106G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-106` | `V106F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-106` | `V106E` | Disposal Group | 4 | 3 | ModB | 2 |
| `India {runId}-106` | `V106D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-106` | `V106C` | Disposal Group | 7 | 7 | ModB | 2 |
| `Kilo {runId}-106` | `V106B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-106` | `V106A` | Disposal Group | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-106`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).
- Parameter iterasi TC-FA-GRP-337, 338, 339 (kolom Group, Code, Function), urutan baris = urutan iterasi:

| Kolom | Keyword huruf kecil | Keyword KAPITAL | Baris yang harus tampil | Baris yang tidak boleh tampil |
|---|---|---|---|---|
| Group | `charlie {runId}-106` | `CHARLIE {runId}-106` | `Charlie {runId}-106` | `Alpha {runId}-106` |
| Code | `v106j` | `V106J` | `Charlie {runId}-106` | `Alpha {runId}-106` |
| Function | `assignable` | `ASSIGNABLE` | `Alpha {runId}-106` | `bravo {runId}-106` |

- Keyword tanpa kecocokan untuk iterasi: `zzz-tidak-ada`.

## Test Steps

### TC-FA-GRP-337, 338, 339: Search per kolom Group, Code, dan Function (iterasi per kolom)

1. Untuk setiap baris tabel parameter iterasi (langkah 2 sampai 12): jalankan langkah berikut dengan kolom dan keyword pada baris itu
2. Verifikasi header kolom pada baris tabel tampil di tabel
3. Ketik Search keyword huruf kecil baris tabel, tekan Enter
4. Verifikasi sedikitnya satu baris tampil pada tabel
5. Verifikasi baris yang harus tampil pada baris tabel tampil
6. Verifikasi baris yang tidak boleh tampil pada baris tabel tidak tampil
7. Ganti isi kotak search dengan keyword KAPITAL baris tabel, tekan Enter
8. Verifikasi baris yang harus tampil pada baris tabel tampil (hasil identik dengan keyword huruf kecil)
9. Verifikasi baris yang tidak boleh tampil pada baris tabel tidak tampil
10. Ganti isi kotak search dengan `zzz-tidak-ada`, tekan Enter
11. Verifikasi empty state tampil dengan Illustration, title `No results found`, dan body `Try adjusting your search or filter.`
12. Klik `(←)` pada kotak Search

### TC-FA-GRP-419: Search kolom Function dengan nilai penuh Disposal Group

13. Ketik Search `disposal group`, tekan Enter
14. Verifikasi sedikitnya satu baris tampil pada tabel
15. Verifikasi baris `hotel {runId}-106` tampil (Function Disposal Group dicocokkan ke nilai penuh, case-insensitive)
16. Verifikasi baris `Alpha {runId}-106` tidak tampil
17. Klik `(←)` pada kotak Search

### TC-FA-GRP-420: Search kolom Function dengan nilai penuh None

18. Ketik Search `none`, tekan Enter
19. Verifikasi sedikitnya satu baris tampil pada tabel
20. Verifikasi baris `bravo {runId}-106` ber-Function None (tampil `—`) ikut tampil
21. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Pengulangan (bagian 8b butir 7): langkah 2 sampai 12 diulang untuk tiap baris tabel parameter iterasi (Group, Code, Function): 3 iterasi x 11 langkah. Tiap `Verifikasi` tetap satu per klausa.
- Langkah penghubung (tanpa awalan `Verifikasi`): `Klik (←)` pada kotak Search di akhir tiap iterasi dan tiap TC (menutup input dan mereset tabel, S-09).
- Search adalah objek uji pada spec ini, sehingga tabel tidak dibatasi suffix; asersi memakai baris dataset milik spec. Baris Pre-setup (mis. group ber-Function Assignable) ikut tampil dan hanya dibaca.
- Spec 21 langkah (ekspansi iterasi ± 46 langkah), di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah per kolom/field memakai tabel di Prerequisites (bagian 8b butir 7).
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - Keyword Code uji `v106j`/`V106J` ditentukan spec dari Code dataset; TC menyebut "potongan nilai kolom" tanpa nilainya.
