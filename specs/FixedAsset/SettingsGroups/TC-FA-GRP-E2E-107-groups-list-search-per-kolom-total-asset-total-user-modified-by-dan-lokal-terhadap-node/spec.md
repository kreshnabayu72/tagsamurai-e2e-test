---
id: TC-FA-GRP-E2E-107-groups-list-search-per-kolom-total-asset-total-user-modified-by-dan-lokal-terhadap-node
title: "Groups List Search per Kolom Total Asset, Total User, Modified By, dan Search Lokal Terhadap Node Terpilih"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-340
  - TC-FA-GRP-341
  - TC-FA-GRP-342
  - TC-FA-GRP-418
coverage:
  web: automated
---

# Groups List Search per Kolom Total Asset, Total User, Modified By, dan Search Lokal Terhadap Node Terpilih

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-107`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-107` | `V107L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-107` | `V107K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-107` | `V107J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-107` | `V107I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-107` | `V107H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-107` | `V107G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-107` | `V107F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-107` | `V107E` | None | 4 | 3 | ModB | 2 |
| `India {runId}-107` | `V107D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-107` | `V107C` | None | 7 | 7 | ModB | 2 |
| `Kilo {runId}-107` | `V107B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-107` | `V107A` | None | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-107`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).
- Data Pre-setup TC-FA-GRP-418: Head Office > Floor 2 (Pre-setup Tabel A, hanya dibaca). Data Dinamis tambahan spec ini: group `Floor 2 Annex {runId}-107` sebagai direct child Region West (Pre-setup Tabel A), dibuat lewat API di `before` dan dihapus di `after`.
- Parameter iterasi TC-FA-GRP-340, 341, 342 (kolom Total Asset, Total User, Modified By), urutan baris = urutan iterasi. Keyword numerik (`25`, `12`) tidak boleh muncul dalam `{runId}` (digit `{runId}` dapat mencocokkan baris yang harus tidak tampil): hook `before` memeriksa bahwa `{runId}` tidak memuat substring `25` maupun `12` dan membangkitkan `{runId}` baru bila memuatnya sebelum seeding (kemampuan membaca dan membangkitkan `{runId}` disediakan tim FE); sufiks `-107` dan Code `V107*` tidak memuat kedua keyword itu. Keyword Modified By dipilih dari nama `ModB` yang bukan bagian nama `ModA`:

| Kolom | Keyword huruf kecil | Keyword KAPITAL | Baris yang harus tampil | Baris yang tidak boleh tampil |
|---|---|---|---|---|
| Total Asset | `25` | `25` | `Echo {runId}-107` | `Alpha {runId}-107` |
| Total User | `12` | `12` | `Echo {runId}-107` | `Alpha {runId}-107` |
| Modified By | potongan nama `ModB` huruf kecil | potongan yang sama huruf KAPITAL | `India {runId}-107` | `Alpha {runId}-107` |

- Keyword tanpa kecocokan: `zzz-tidak-ada`.

## Test Steps

### TC-FA-GRP-340, 341, 342: Search per kolom Total Asset, Total User, dan Modified By (iterasi per kolom)

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

### TC-FA-GRP-418: Search lokal terhadap node terpilih di sidebar

13. Klik `Head Office` di sidebar Group Tree
14. Verifikasi group `Floor 2` tampil pada tabel sebagai direct child Head Office
15. Ketik Search `floor`, tekan Enter
16. Verifikasi group `Floor 2` tampil pada tabel yang tersaring
17. Verifikasi group `Floor 2 Annex {runId}-107` tidak tampil
18. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Pengulangan (bagian 8b butir 7): langkah 2 sampai 12 diulang untuk tiap baris tabel parameter iterasi (Total Asset, Total User, Modified By): 3 iterasi x 11 langkah.
- Langkah penghubung (tanpa awalan `Verifikasi`): `Klik (←)` pada kotak Search di akhir tiap iterasi dan tiap TC (S-09); membuka node `Head Office` di sidebar sebelum Search (TC-FA-GRP-418).
- Search adalah objek uji pada spec ini, sehingga tabel tidak dibatasi suffix. TC-FA-GRP-418 memakai Pre-setup `Floor 2` hanya dibaca; `Floor 2 Annex` dibuat spec dengan suffix (bagian 5).
- Spec 18 langkah (ekspansi iterasi ± 41 langkah), di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah per kolom/field memakai tabel di Prerequisites (bagian 8b butir 7).
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - TC-FA-GRP-340/341: langkah "keyword huruf KAPITAL" identik dengan huruf kecil untuk nilai numerik; spec tetap menulis langkahnya sesuai TC.
  - TC-FA-GRP-418 menyebut "Floor 2 Annex (child Region West)" yang tidak ada di Pre-setup Tabel A; spec membuatnya sebagai data Dinamis bersuffix.
  - Pembuatan `{runId}`: hook `before` memeriksa `{runId}` tidak memuat substring `25` dan `12`, lalu membuatnya ulang; mekanisme ini diasumsikan disediakan tim FE (menyangkut TC-FA-GRP-340/341 dan seluruh iterasi pencarian numerik). Dikonfirmasi tim FE.
