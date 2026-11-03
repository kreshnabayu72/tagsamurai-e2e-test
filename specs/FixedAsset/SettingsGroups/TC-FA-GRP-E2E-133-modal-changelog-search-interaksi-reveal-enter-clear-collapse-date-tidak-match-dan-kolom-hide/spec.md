---
id: TC-FA-GRP-E2E-133-modal-changelog-search-interaksi-reveal-enter-clear-collapse-date-tidak-match-dan-kolom-hide
title: "Modal Changelog Search: Interaksi, Kolom Date Tidak Match, dan Kolom Group Name yang Di-Hide"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-432
  - TC-FA-GRP-439
  - TC-FA-GRP-440
coverage:
  web: automated
---

# Modal Changelog Search: Interaksi, Kolom Date Tidak Match, dan Kolom Group Name yang Di-Hide

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-133`, bagian 5), dibuat lewat API di hook `before` oleh akun aktor (`ModA` untuk aksi aktor Total Control Pre-setup No 1, `ModB` dan `ModC` untuk dua user lain; akun `ModB` dan `ModC` tidak tertulis di Pre-setup TC dan disediakan tim FE). Seeding terbagi tiga batch dengan jeda sampai menit berganti (maksimum 60 detik) di antara batch agar kolom Date punya tiga nilai distinct. Group `Log1 {runId}-133` sampai `Log4 {runId}-133` adalah group level 1; Description awal group `Log2 {runId}-133` dan `Log3 {runId}-133` = `Edit me`; Function awal `Log1` dan `Log2` = `None`, `Log3` = `Assignable`. Entri hasil seeding dipakai sebagai "Example Data" Changelog (>= 12 entri variasi Action/Field); nilai tampilan `ModA`, `ModB`, `ModC` (format `[First Name] [Last Initial]`) dan nama lengkapnya dibaca sebelum uji:

| # | Action | Group Name | Field | Old Value | New Value | Modified By | Batch seeding |
|---:|---|---|---|---|---|---|:---:|
| 1 | Create | `Log1 {runId}-133` | Group Name | `—` | `Log1 {runId}-133` | ModA | 1 |
| 2 | Create | `Log2 {runId}-133` | Group Name | `—` | `Log2 {runId}-133` | ModA | 1 |
| 3 | Create | `Log3 {runId}-133` | Group Name | `—` | `Log3 {runId}-133` | ModB | 1 |
| 4 | Create | `Log4 {runId}-133` | Group Name | `—` | `Log4 {runId}-133` | ModB | 1 |
| 5 | Edit | `Log2 {runId}-133` | Function | `None` | `Assignable` | ModA | 2 |
| 6 | Edit | `Log2 {runId}-133` | Description | `Edit me` | `Updated notes` | ModA | 2 |
| 7 | Edit | `Log2 {runId}-133` | Code | `LA133` | `LB133` | ModA | 2 |
| 8 | Edit | `Log3 {runId}-133` | Function | `Assignable` | `None` | ModB | 2 |
| 9 | Edit | `Log3 {runId}-133` | Description | `Edit me` | `Updated notes` | ModB | 3 |
| 10 | Edit | `Log3 {runId}-133` | Code | `LC133` | `LD133` | ModB | 3 |
| 11 | Delete | `Log4 {runId}-133` | Group Name | `Log4 {runId}-133` | `—` | ModB | 3 |
| 12 | Edit | `Log1 {runId}-133` | Function | `None` | `Assignable` | ModC | 3 |
  - Changelog adalah audit trail permanen: jumlah total entri tidak diasersi; tabel dibatasi Search suffix spec sehingga hanya 12 entri di atas yang teramati (10 entri di halaman 1, 2 entri di halaman 2).
  - Entri permanen tidak dihapus; cleanup (hook `after`, tidak berasumsi seeding berhasil penuh) menghapus lewat API group `Log1 {runId}-133` sampai `Log4 {runId}-133` bila masih ada dan preferensi kolom Setup Column di browser (kemampuan disediakan tim FE).

## Test Steps

### TC-FA-GRP-432: Interaksi Search (reveal, Enter, clear, collapse)

1. Klik icon Changelog
2. Catat nama baris halaman 1 tabel Modal Changelog sebelum Search
3. Hover icon Search pada toolbar
4. Verifikasi tooltip `Search` tampil
5. Klik icon Search
6. Verifikasi input Search melebar
7. Verifikasi input Search terfokus otomatis
8. Verifikasi placeholder input sesuai konvensi platform
9. Ketik `L` (1 karakter) di input Search tanpa menekan Enter
10. Verifikasi icon `✕` tampil di dalam input
11. Verifikasi tabel belum tersaring: nama baris halaman 1 sama dengan yang dicatat pada langkah 2
12. Tekan Enter
13. Verifikasi sedikitnya satu baris tampil pada tabel
14. Verifikasi tabel tersaring sesuai keyword `L`: sedikitnya satu baris tampil dan seluruh baris yang tampil memuat karakter `l` pada kolom yang dicari
15. Klik `✕` di dalam input
16. Verifikasi input Search kosong
17. Verifikasi input Search tetap terbuka dan terfokus
18. Verifikasi tabel tetap menampilkan hasil search terakhir (keyword `L`)
19. Tekan Enter pada input kosong
20. Verifikasi tabel kembali ke semua data: nama baris halaman 1 sama dengan yang dicatat pada langkah 2
21. Ganti isi kotak search dengan `Log3 {runId}-133`, tekan Enter
22. Verifikasi sedikitnya satu baris tampil pada tabel
23. Verifikasi tabel hanya memuat baris dengan Group Name `Log3 {runId}-133`
24. Ganti isi kotak search dengan `  Log3 {runId}-133  ` (dua spasi sebelum dan sesudah keyword), tekan Enter
25. Verifikasi tabel menampilkan baris yang sama dengan hasil pada langkah 23
26. Verifikasi isi input Search tetap `  Log3 {runId}-133  ` seperti yang diketik
27. Ganti isi kotak search dengan `Log1 {runId}-133`, tekan Enter
28. Klik `(←)` pada kotak Search
29. Verifikasi input Search tertutup
30. Verifikasi keyword Search kosong dan tabel langsung reset: nama baris halaman 1 sama dengan yang dicatat pada langkah 2

### TC-FA-GRP-439: Nilai kolom Date tidak menghasilkan match

31. Salin nilai Date yang tampil pada baris pertama tabel
32. Ketik Search dengan nilai Date yang disalin, tekan Enter
33. Verifikasi empty state tampil dengan title `No results found`
34. Klik `(←)` pada kotak Search
35. Klik icon Filter
36. Verifikasi Filter Panel memuat field Date (date range picker, placeholder `Select date`)
37. Klik icon Filter untuk menutup panel

### TC-FA-GRP-440: Search pada kolom Group Name yang di-hide

38. Hide kolom Group Name lewat Column Visibility (icon `⋯` di header kolom terakhir)
39. Verifikasi kolom Group Name tidak tampil pada header tabel
40. Ketik Search `Log3 {runId}-133`, tekan Enter
41. Verifikasi baris Action Create dengan New Value `Log3 {runId}-133` tampil (cocok lewat kolom New Value yang masih tampil)
42. Verifikasi tidak ada baris Action Edit pada tabel (baris Edit `Log3 {runId}-133` hanya memuat nama di kolom Group Name yang di-hide)
43. Klik `(←)` pada kotak Search
44. Tampilkan kembali kolom Group Name lewat Column Visibility
45. Verifikasi kolom Group Name tampil pada header tabel
46. Ketik Search `Log3 {runId}-133`, tekan Enter
47. Verifikasi baris Group Name `Log3 {runId}-133` tampil
48. Verifikasi baris Action Edit Group Name `Log3 {runId}-133` tampil
49. Klik `(←)` pada kotak Search
50. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Langkah penghubung (tanpa awalan `Verifikasi`): mencatat nama baris halaman 1 (langkah 2), mengganti isi kotak search antar bagian TC-FA-GRP-432, menutup Search dengan `(←)`, menyalin nilai Date, membuka dan menutup Filter Panel, serta men-hide dan meng-unhide kolom Group Name lewat Column Visibility (S-03, R-16).
- Anchor positif (8b butir 2, S-03): `Verifikasi sedikitnya satu baris tampil pada tabel` mendahului asersi universal "hanya memuat" hasil Search `Log3 {runId}-133` (langkah 22), seperti pada langkah 13; bukan klausa Expected TC.
- Search adalah objek uji pada spec ini sehingga tabel tidak dibatasi suffix kecuali pada keyword yang memuat suffix spec.
- Keyword 1 karakter `L` ditentukan spec (TC: "keyword 1 karakter" tanpa nilai); karena 12 entri seeding semuanya memuat `L` pada Group Name, asersi hasil Enter adalah tersaring dan memuat karakter itu.
- Expected b TC-FA-GRP-439 ("penyaringan Date hanya tersedia lewat Filter Panel") ditulis sebagai `Verifikasi` Filter Panel memuat field Date.
- Spec 50 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Nama group seeding juga muncul di kolom New Value (baris Create) dan Old Value (baris Delete) sehingga Search tidak menghasilkan empty state; asersi kolom Group Name yang di-hide memakai baris Action Edit yang namanya hanya ada di kolom itu (TC-FA-GRP-440, R-13).
- Temuan untuk QA:
  - Rujukan "Tabel Data Uji" pada Precondition TC tidak punya tabel konkret (Catatan TC hanya menyebut data variasi baris Groups List); spec mendefinisikan dataset sendiri di Prerequisites dan menjamin sedikitnya dua nilai distinct per kolom.
  - Akun Modified By kedua (`ModB`) dan nilai tampilan `ModA`/`ModB` tidak tertulis di Pre-setup TC; ditulis "disediakan tim FE". Nilai Total User dasar (user yang otomatis punya akses semua group) tidak tertulis di TC; dataset memakai target nilai yang dibentuk lewat penugasan Group Role.
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - TC-FA-GRP-440 Expected a (empty state "No results found") tidak dapat dipenuhi pada dataset ini: seluruh nama group seeding level 1 juga ada di kolom New Value atau Old Value yang tetap tampil. Spec mengasersi baris Action Edit tidak tampil; empty state penuh butuh nilai unik Group Name (mis. path group non-level-1), perlu seeding tambahan atau keputusan QA.
  - Rujukan "Example Data" dan "Tabel Data Uji" Changelog pada Precondition TC tidak punya data konkret; spec mendefinisikan 12 entri seeding sendiri di Prerequisites (Action Create/Edit/Delete; Field Group Name/Function/Description/Code). Entri Marked as Excess dan Restored from Excess hanya dipakai pada spec 132.
  - Changelog adalah audit trail permanen sehingga N total tidak dapat diturunkan dari seeding (bagian 8b butir 10); spec memakai Search suffix dan selisih terhadap data milik spec. Akun `ModB` dan `ModC` (dua user lain sebagai pelaku seeding) disediakan tim FE.
