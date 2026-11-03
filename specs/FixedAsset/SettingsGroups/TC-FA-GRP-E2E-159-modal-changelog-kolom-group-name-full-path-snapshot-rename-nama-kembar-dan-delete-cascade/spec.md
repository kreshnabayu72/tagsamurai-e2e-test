---
id: TC-FA-GRP-E2E-159-modal-changelog-kolom-group-name-full-path-snapshot-rename-nama-kembar-dan-delete-cascade
title: "Modal Changelog Kolom Group Name: Full Path Subgroup, Path Setelah Rename, Snapshot Tidak Berubah, Dua Group Bernama Sama, dan Path Saat Delete Cascade"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1018
  - TC-FA-GRP-1019
  - TC-FA-GRP-1020
  - TC-FA-GRP-1021
  - TC-FA-GRP-1022
coverage:
  web: automated
---

# Modal Changelog Kolom Group Name: Full Path Subgroup, Path Setelah Rename, Snapshot Tidak Berubah, Dua Group Bernama Sama, dan Path Saat Delete Cascade

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Akun aktor: Total Control (`totalControlGroups_automated_{namaCompany}@qwertysystem.net`, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`). Hook `after` mengembalikan sesi ke akun default suite. Guided Tooltip, sesi API aktor, klien HTTP, dan fixture BE: lihat `suite.md`.
- Data Dinamis (suffix `{runId}-159`, bagian 5), dibuat lewat API di `before` oleh akun aktor (seeding menghasilkan entri Create di Changelog): `Path Anchor {runId}-159` (level 1, Assignable); `Ren Parent {runId}-159` > `Ren Child {runId}-159` (tanpa aset); `Snap Anc {runId}-159` > `Snap Desc {runId}-159` (sudah punya entri Create); `Floor 2` kedua di bawah `Branch Office` (Tabel A, Pre-setup No 9; nama literal tanpa suffix karena harus kembar dengan `Floor 2` di bawah `Head Office`; TC-FA-GRP-1021); `Del Parent {runId}-159` > `Del Child {runId}-159` (kosong, level 1). Dipakai sebagai pengganti Warehouse A, Ren Parent/Child, Snap Anc/Desc, serta Del Parent/Child fixture Pre-setup tambahan (S-06). `Head Office > Floor 2` adalah group Pre-setup (hanya dibaca) dan keduanya punya entri Changelog.
- Data baru yang dibuat langkah (dibersihkan di `after`): `Rack Path {runId}-159` (subgroup di bawah `Path Anchor {runId}-159`), `Path Root {runId}-159` (level 1), `Snap New {runId}-159` (subgroup di bawah `Snap Anc Renamed {runId}-159`); hasil rename: `Ren Child Renamed {runId}-159`, `Snap Anc Renamed {runId}-159`.
- Field wajib form Create/Edit selain Group Name diisi nilai bawaan form (tidak diasersi).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API seluruh group di atas bila masih ada. Entri Changelog permanen tidak dihapus.

## Test Steps

### TC-FA-GRP-1018: Aksi Create subgroup dan Create level 1

1. Ketik Search `Path Anchor {runId}-159`, tekan Enter
2. Klik row action `Add Subgroup` pada `Path Anchor {runId}-159`
3. Isi Group Name `Rack Path {runId}-159`, klik [Submit]
4. Tunggu aksi selesai (dialog Create tertutup)
5. Klik `(←)` pada kotak Search
6. Klik `[+] Group` pada sidebar Group Tree
7. Isi Group Name `Path Root {runId}-159`, klik [Submit]
8. Tunggu aksi selesai (dialog Create tertutup)

### TC-FA-GRP-1019: Aksi rename group

9. Klik `Ren Parent {runId}-159` di sidebar Group Tree
10. Klik row action `Edit` pada `Ren Child {runId}-159`
11. Ubah Group Name menjadi `Ren Child Renamed {runId}-159`, klik [Save]
12. Tunggu aksi selesai (dialog Edit tertutup)

### TC-FA-GRP-1020: Aksi rename ancestor dan Add Subgroup

13. Klik `All Groups` di sidebar Group Tree (kembali ke root Group Tree)
14. Ketik Search `Snap Anc {runId}-159`, tekan Enter
15. Klik row action `Edit` pada `Snap Anc {runId}-159`
16. Ubah Group Name menjadi `Snap Anc Renamed {runId}-159`, klik [Save]
17. Tunggu aksi selesai (dialog Edit tertutup)
18. Ganti isi kotak search dengan `Snap Anc Renamed {runId}-159`, tekan Enter
19. Klik row action `Add Subgroup` pada `Snap Anc Renamed {runId}-159`
20. Isi Group Name `Snap New {runId}-159`, klik [Submit]
21. Tunggu aksi selesai (dialog Create tertutup)
22. Klik `(←)` pada kotak Search

### TC-FA-GRP-1022: Aksi Delete subgroup dengan cascade (aksi menghapus data di akhir)

23. Ketik Search `Del Parent {runId}-159`, tekan Enter
24. Klik row action `Delete` pada `Del Parent {runId}-159`
25. Klik [Delete] pada dialog konfirmasi
26. Tunggu aksi selesai (dialog Delete tertutup)
27. Klik `(←)` pada kotak Search

### TC-FA-GRP-1018 dan 1019: Kolom Group Name pada Modal Changelog

28. Klik icon Changelog
29. Ketik Search `Rack Path {runId}-159`, tekan Enter
30. Verifikasi baris Action Create Group Name `Path Anchor {runId}-159 > Rack Path {runId}-159` tampil (full path breadcrumb `Parent > Child`)
31. Verifikasi baris tersebut memiliki Field `Group Name`, Old Value `—`, dan New Value `Rack Path {runId}-159` (nama exact, bukan path)
32. Ganti isi kotak search dengan `Path Root {runId}-159`, tekan Enter
33. Verifikasi baris Action Create Group Name `Path Root {runId}-159` tampil (level 1 tanpa pemisah)
34. Verifikasi baris tersebut memiliki New Value `Path Root {runId}-159`
35. Ganti isi kotak search dengan `Ren Child Renamed {runId}-159`, tekan Enter
36. Verifikasi baris Action Edit Group Name `Ren Parent {runId}-159 > Ren Child Renamed {runId}-159` tampil
37. Verifikasi baris tersebut memiliki Field `Group Name`, Old Value `Ren Child {runId}-159`, dan New Value `Ren Child Renamed {runId}-159`
38. Verifikasi Old Value dan New Value pada baris tersebut berisi nama saja, tanpa path

### TC-FA-GRP-1020: Path di Changelog adalah snapshot

39. Ganti isi kotak search dengan `Snap Desc {runId}-159`, tekan Enter
40. Verifikasi entri Create `Snap Desc` yang lama tetap ber-Group Name `Snap Anc {runId}-159 > Snap Desc {runId}-159`
41. Ganti isi kotak search dengan `Snap Anc Renamed {runId}-159`, tekan Enter
42. Verifikasi baris Action Edit rename `Snap Anc`: Group Name `Snap Anc Renamed {runId}-159`, Old Value `Snap Anc {runId}-159`, New Value `Snap Anc Renamed {runId}-159`
43. Verifikasi entri Create `Snap New {runId}-159` memakai path `Snap Anc Renamed {runId}-159 > Snap New {runId}-159`

### TC-FA-GRP-1022: Delete subgroup dan cascade

44. Ganti isi kotak search dengan `Del Parent {runId}-159`, tekan Enter
45. Verifikasi baris Action Delete untuk `Del Parent {runId}-159`: Group Name `Del Parent {runId}-159`, Old Value `Del Parent {runId}-159`, New Value `—`
46. Verifikasi baris Action Delete untuk descendant: Group Name `Del Parent {runId}-159 > Del Child {runId}-159`, Old Value `Del Child {runId}-159`, New Value `—`
47. Verifikasi terdapat tepat satu baris Action Delete per node yang terhapus (dua baris Delete)

### TC-FA-GRP-1021: Dua group bernama sama di parent berbeda

48. Ganti isi kotak search dengan `Floor 2`, tekan Enter
49. Verifikasi kolom Group Name menampilkan `Head Office > Floor 2` dan `Branch Office > Floor 2` sebagai dua nilai berbeda
50. Klik `(←)` pada kotak Search
51. Klik icon Filter
52. Buka dropdown Group Name
53. Verifikasi dropdown Group Name memuat opsi `Head Office > Floor 2` dan `Branch Office > Floor 2`
54. Pilih opsi `Head Office > Floor 2`
55. Klik [Apply]
56. Verifikasi sedikitnya satu baris tampil pada tabel
57. Verifikasi baris Group Name `Head Office > Floor 2` tampil
58. Verifikasi baris Group Name `Branch Office > Floor 2` tidak tampil
59. Klik icon Filter
60. Klik [Clear Field]
61. Klik [Apply]
62. Klik icon close (X) pada header Modal Changelog

## Notes

- Sumber TC: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`.
- Urutan TC di spec berbeda dari urutan sumber: seluruh aksi pada TC-FA-GRP-1018, 1019, 1020, dan 1022 dijalankan lebih dulu (aksi Delete TC-FA-GRP-1022 paling akhir, S-10), lalu Modal Changelog dibuka sekali untuk membaca hasilnya, dan TC-FA-GRP-1021 (hanya baca) di akhir. Tiap Expected tetap diasersi terhadap entri aksinya sendiri.
- Langkah penghubung (tanpa awalan `Verifikasi`): "Tunggu aksi selesai" setelah [Submit]/[Save]/[Delete] yang hasilnya tidak diasersi langsung, membuka node di sidebar, membuka dan menutup Modal Changelog, mengganti isi kotak search untuk menemukan baris target, kembali ke `All Groups` di sidebar, dan `(←)` serta [Clear Field] + [Apply] (S-03, bagian 8b butir 8, R-16).
- Client punya lebih dari 10 node level 1 dan ukuran halaman 10, sehingga baris level 1 target tidak dijamin ada di halaman 1 All Groups: tiap aksi pada baris level 1 (`Path Anchor`, `Snap Anc`, `Snap Anc Renamed`, `Del Parent`) didahului `Ketik Search` nama bersufiks + Enter, dan Search dikosongkan dengan `(←)` sesudahnya (S-03, R-16). Group Tree dikembalikan ke root (`All Groups`) sebelum menarget `Snap Anc`, karena langkah 9 membuka konteks `Ren Parent`.
- Entri Create `Snap Desc` yang lama berasal dari seeding (S-04: precondition TC-FA-GRP-1020 "sudah punya entri Create").
- Pemisah path pada Group Name Changelog adalah ` > ` sesuai Expected TC (`Parent > Child`).
- Spec 62 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Password akun aktor memakai env baru `FA_TC_PASSWORD` (nama `<APP>_<ROLE>_PASSWORD`); perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
  - TC-FA-GRP-1018 hingga 1022 memakai fixture Pre-setup tambahan literal (Warehouse A, Ren Parent, Snap Anc, Del Parent); spec memakai fixture milik spec bersuffix (S-06, S-12).
  - TC-FA-GRP-1018 langkah 1 menyebut "Lakukan aksi" tanpa rincian form; spec memakai row action Add Subgroup dan `[+] Group` dengan nilai bawaan form untuk field wajib lain.
