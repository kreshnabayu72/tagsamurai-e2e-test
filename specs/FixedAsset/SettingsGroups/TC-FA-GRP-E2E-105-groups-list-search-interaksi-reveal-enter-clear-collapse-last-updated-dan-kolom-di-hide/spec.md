---
id: TC-FA-GRP-E2E-105-groups-list-search-interaksi-reveal-enter-clear-collapse-last-updated-dan-kolom-di-hide
title: "Groups List Search: Interaksi (Reveal, Enter, Clear, Collapse), Last Updated Tidak Match, dan Kolom Code yang Di-Hide"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-336
  - TC-FA-GRP-343
  - TC-FA-GRP-344
coverage:
  web: automated
---

# Groups List Search: Interaksi (Reveal, Enter, Clear, Collapse), Last Updated Tidak Match, dan Kolom Code yang Di-Hide

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-105`, bagian 5 konvensi), dibuat lewat API di hook `before` oleh akun aktor, dua batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar Last Updated punya dua nilai distinct; seluruhnya node level 1 (Parent: All Groups). Dipakai sebagai "Tabel Data Uji" TC (>= 12 baris data variasi):

| Group | Code | Function | Total Asset | Total User | Modified By | Batch seeding |
|---|---|---|---:|---:|---|:---:|
| `Alpha {runId}-105` | `V105L` | Assignable | 2 | 4 | ModA | 1 |
| `bravo {runId}-105` | `V105K` | None | 0 | 3 | ModA | 1 |
| `Charlie {runId}-105` | `V105J` | Assignable | 10 | 5 | ModA | 1 |
| `delta {runId}-105` | `V105I` | None | 0 | 3 | ModA | 1 |
| `Echo {runId}-105` | `V105H` | Assignable | 25 | 12 | ModA | 1 |
| `foxtrot {runId}-105` | `V105G` | None | 0 | 4 | ModA | 1 |
| `Golf {runId}-105` | `V105F` | Assignable | 1 | 6 | ModA | 1 |
| `hotel {runId}-105` | `V105E` | None | 4 | 3 | ModB | 2 |
| `India {runId}-105` | `V105D` | Assignable | 13 | 4 | ModB | 2 |
| `juliet {runId}-105` | `V105C` | None | 7 | 7 | ModB | 2 |
| `Kilo {runId}-105` | `V105B` | Assignable | 3 | 5 | ModB | 2 |
| `lima {runId}-105` | `V105A` | None | 5 | 3 | ModB | 2 |

  - `ModA` = nama Modified By aktor Total Control Pre-setup No 1 dalam format `[First Name] [Last Initial]`; `ModB` = nama Modified By user kedua yang membuat batch 2 (akun tidak tertulis di Pre-setup TC; disediakan tim FE). Nilai tampilan keduanya dibaca sebelum uji.
  - Total Asset dibentuk dengan menambahkan aset ke group; Total User = user yang otomatis punya akses ke semua group (Total Control, Default User, Read Only client) ditambah user yang ditugaskan lewat Group Role; kemampuan seeding aset dan penugasan user ini disediakan tim FE/BE.
  - Group Pre-setup Tabel A (Default Group, Head Office, dan seterusnya) tetap tampil di Groups List dan hanya dibaca; asersi memakai baris data di atas.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group `... {runId}-105`, aset, dan penugasan user yang di-seed spec ini; hapus preferensi kolom Setup Column yang disimpan spec (kemampuan disediakan tim FE).

## Test Steps

### TC-FA-GRP-336: Interaksi Search (reveal, Enter, clear, collapse)

1. Catat nama baris halaman 1 tabel Groups List sebelum Search
2. Hover icon Search pada toolbar
3. Verifikasi tooltip `Search` tampil
4. Klik icon Search
5. Verifikasi input Search melebar
6. Verifikasi input Search terfokus otomatis
7. Verifikasi placeholder input `Search group, code, function...`
8. Ketik `x` (1 karakter) di input Search tanpa menekan Enter
9. Verifikasi icon `✕` tampil di dalam input
10. Verifikasi tabel belum tersaring: nama baris halaman 1 sama dengan yang dicatat pada langkah 1
11. Tekan Enter
12. Verifikasi sedikitnya satu baris tampil pada tabel
13. Verifikasi baris `foxtrot {runId}-105` tampil pada tabel yang tersaring
14. Verifikasi baris `Alpha {runId}-105` tidak tampil
15. Klik `✕` di dalam input
16. Verifikasi input Search kosong
17. Verifikasi input Search tetap terbuka dan terfokus
18. Verifikasi tabel tetap menampilkan hasil search terakhir: baris `foxtrot {runId}-105` tampil dan baris `Alpha {runId}-105` tidak tampil
19. Tekan Enter pada input kosong
20. Verifikasi tabel kembali ke semua data: nama baris halaman 1 sama dengan yang dicatat pada langkah 1
21. Ganti isi kotak search dengan `foxtrot {runId}-105`, tekan Enter
22. Verifikasi tabel hanya menampilkan baris `foxtrot {runId}-105`
23. Ganti isi kotak search dengan `  foxtrot {runId}-105  ` (dua spasi sebelum dan sesudah keyword), tekan Enter
24. Verifikasi tabel menampilkan baris yang sama dengan hasil pada langkah 22 (baris `foxtrot {runId}-105` saja)
25. Verifikasi isi input Search tetap `  foxtrot {runId}-105  ` seperti yang diketik
26. Ganti isi kotak search dengan `golf {runId}-105`, tekan Enter
27. Klik `(←)` pada kotak Search
28. Verifikasi input Search tertutup
29. Verifikasi keyword Search kosong dan tabel langsung reset: nama baris halaman 1 sama dengan yang dicatat pada langkah 1

### TC-FA-GRP-343: Nilai Last Updated tidak menghasilkan match

30. Salin nilai Last Updated yang tampil pada baris pertama tabel
31. Ketik Search dengan nilai Last Updated yang disalin, tekan Enter
32. Verifikasi empty state tampil dengan title `No results found`
33. Klik `(←)` pada kotak Search
34. Klik icon Filter
35. Verifikasi Filter Panel memuat field Last Updated (date range picker, placeholder `Select date`)
36. Klik icon Filter untuk menutup Filter Panel

### TC-FA-GRP-344: Search pada kolom Code yang di-hide

37. Hide kolom Code lewat Column Visibility (icon `⋯` di header kolom terakhir, hilangkan centang Code)
38. Verifikasi kolom Code tidak tampil pada header tabel
39. Ketik Search `V105L`, tekan Enter
40. Verifikasi empty state tampil dengan title `No results found` (kolom yang di-hide dikecualikan dari cakupan search)
41. Klik `(←)` pada kotak Search
42. Tampilkan kembali kolom Code lewat Column Visibility
43. Verifikasi kolom Code tampil pada header tabel
44. Ketik Search `V105L`, tekan Enter
45. Verifikasi baris `Alpha {runId}-105` tampil
46. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): mencatat nama baris halaman 1 (langkah 1), mengganti isi kotak search antar bagian TC-FA-GRP-336, menutup Search dengan `(←)` antar TC, menyalin nilai Last Updated, membuka dan menutup Filter Panel, serta men-hide dan meng-unhide kolom Code lewat Column Visibility (S-03, R-16).
- Keyword 1 karakter `x` dipilih spec (TC menyebut "keyword 1 karakter" tanpa nilai); hanya group `foxtrot` pada dataset yang memuat `x` pada kolom yang di-search.
- Search adalah objek uji pada spec ini, sehingga tabel tidak dibatasi suffix; Pre-setup Tabel A hanya dibaca dan baris Pre-setup yang memuat `x` boleh ikut tampil.
- Expected b TC-FA-GRP-343 ("penyaringan Last Updated hanya tersedia lewat Filter Panel") ditulis sebagai `Verifikasi` Filter Panel memuat field Last Updated; TC tidak merinci cara mengamati kata "hanya".
- Spec 46 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - TC-FA-GRP-344 memakai nilai unik kolom Code tanpa menyebut nilainya; spec memakai Code dataset `V105L`.
