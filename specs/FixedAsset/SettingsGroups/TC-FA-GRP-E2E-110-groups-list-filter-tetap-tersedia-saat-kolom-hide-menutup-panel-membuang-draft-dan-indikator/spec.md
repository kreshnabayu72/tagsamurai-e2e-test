---
id: TC-FA-GRP-E2E-110-groups-list-filter-tetap-tersedia-saat-kolom-hide-menutup-panel-membuang-draft-dan-indikator
title: "Groups List Filter: Tetap Berlaku Saat Kolom Function Di-Hide, Menutup Panel Tanpa [Apply] Membuang Draft, dan Indikator Filter Aktif"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1118
  - TC-FA-GRP-1130
  - TC-FA-GRP-1131
coverage:
  web: automated
---

# Groups List Filter: Tetap Berlaku Saat Kolom Function Di-Hide, Menutup Panel Tanpa [Apply] Membuang Draft, dan Indikator Filter Aktif

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-110`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-110` | `V110L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-110` | `V110K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-110` | `V110J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-110` | `V110I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-110` | `V110H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-110` | `V110G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-110` | `V110F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-110` | `V110E` | Disposal Group | 4 | 3 | ModB | 2 |
| `India {runId}-110` | `V110D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-110` | `V110C` | Disposal Group | 7 | 7 | ModB | 2 |
| `Kilo {runId}-110` | `V110B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-110` | `V110A` | Disposal Group | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-110`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).

## Test Steps

1. Ketik Search `{runId}-110`, tekan Enter, lalu catat nama baris halaman 1 tabel (baseline sebelum filter)

### TC-FA-GRP-1131: Indikator filter aktif muncul saat Apply dan hilang saat Clear

2. Klik icon Filter
3. Pilih `Assignable` pada dropdown Function
4. Klik [Apply]
5. Verifikasi badge titik tampil pada icon Filter saat panel tertutup
6. Klik icon Filter
7. Verifikasi badge titik tampil pada icon Filter saat panel terbuka
8. Klik [Clear Field]
9. Klik [Apply]
10. Verifikasi badge titik hilang dari icon Filter
11. Verifikasi nama baris halaman 1 tabel sama dengan yang dicatat pada langkah 1 (tabel kembali menampilkan seluruh baris)

### TC-FA-GRP-1118: Filter tetap tersedia dan berlaku saat kolom Function di-hide

12. Klik icon Filter
13. Pilih `Assignable` pada dropdown Function
14. Klik [Apply]
15. Verifikasi sedikitnya satu baris tampil dan seluruh baris yang tampil ber-Function `Assignable` (baris `Alpha {runId}-110` tampil, baris `bravo {runId}-110` tidak tampil)
16. Catat nama baris yang tampil pada tabel
17. Hide kolom Function lewat Column Visibility (icon `⋯` di header kolom terakhir)
18. Verifikasi kolom Function tidak tampil pada header tabel
19. Verifikasi filter yang sudah di-Apply tetap berlaku: nama baris yang tampil sama dengan yang dicatat pada langkah 16
20. Klik icon Filter
21. Verifikasi Filter Panel tetap memuat field Function walau kolomnya tersembunyi
22. Klik icon Filter untuk menutup panel
23. Tampilkan kembali kolom Function lewat Column Visibility
24. Verifikasi kolom Function tampil pada header tabel
25. Verifikasi nama baris yang tampil tidak berubah dari yang dicatat pada langkah 16
26. Klik icon Filter
27. Verifikasi nilai filter Function tetap `Assignable`
28. Klik [Clear Field]
29. Klik [Apply]

### TC-FA-GRP-1130: Menutup panel tanpa [Apply] membuang draft

30. Klik icon Filter
31. Pilih `None` pada dropdown Function
32. Klik [Apply]
33. Klik icon Filter
34. Ubah Function menjadi `Assignable` (hilangkan centang `None`, centang `Assignable`) tanpa [Apply]
35. Klik di luar Filter Panel
36. Verifikasi tabel tetap menampilkan hasil Function = `None`: baris `bravo {runId}-110` tampil dan baris `Alpha {runId}-110` tidak tampil
37. Klik icon Filter
38. Verifikasi Filter Panel menampilkan Function = `None` (nilai ter-Apply, bukan draft)
39. Ubah Function menjadi `Disposal Group` (hilangkan centang `None`, centang `Disposal Group`) tanpa [Apply]
40. Klik icon Filter untuk menutup panel
41. Verifikasi tabel tetap menampilkan hasil Function = `None`: baris `bravo {runId}-110` tampil dan baris `hotel {runId}-110` tidak tampil
42. Klik icon Filter
43. Verifikasi Filter Panel menampilkan Function = `None` (nilai ter-Apply, bukan draft)
44. Verifikasi indikator filter aktif tetap tampil pada icon Filter
45. Klik [Clear Field]
46. Klik [Apply]
47. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): membatasi tabel dengan Search suffix spec di awal sekaligus mencatat nama baris halaman 1 sebagai baseline langkah 11 (S-12; posisi baris tertentu di halaman 1 tidak diandalkan, 12 baris seeding dengan page size 10), membuka Filter Panel dan dropdown, menutup dropdown, serta [Clear Field] + [Apply] dan `(←)` pada kotak Search sebagai pemulihan state antar TC (S-03, S-09, R-16). Panel Filter menutup sendiri sesudah [Apply] (A-9), sehingga tiap pembukaan panel berikutnya memakai satu `Klik icon Filter`.
- Urutan TC di spec berbeda dari urutan sumber (TC-FA-GRP-1131 lebih dulu, lalu TC-FA-GRP-1118, TC-FA-GRP-1130) karena TC-FA-GRP-1131 mensyaratkan tidak ada filter ter-Apply sebelum aksi, sedangkan TC-FA-GRP-1130 mensyaratkan Function = None sudah ter-Apply.
- Catatan TC-FA-GRP-1131 Expected c (bagian nilai kosong diuji pada Tab Users) tidak diasersi di spec ini.
- Spec 47 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
