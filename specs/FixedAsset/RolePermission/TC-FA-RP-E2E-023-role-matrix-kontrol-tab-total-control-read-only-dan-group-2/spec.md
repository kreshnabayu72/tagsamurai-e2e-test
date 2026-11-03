---
id: TC-FA-RP-E2E-023-role-matrix-kontrol-tab-total-control-read-only-dan-group-2
title: "Role Matrix: kontrol Tab Total Control, Read Only, dan Group Manager per peran (2/3)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-87
  - TC-FA-RP-88
  - TC-FA-RP-89
coverage:
  web: automated
---

# Role Matrix: kontrol Tab Total Control, Read Only, dan Group Manager per peran (2/3)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage global user & role (Update) (Pre-setup #6, role pertama pada tabel); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Role yang diuji (Role Matrix, bagian 3a); urutan baris = urutan pemakaian; spec ditulis per blok role karena hasil per role berbeda dan ganti akun menuntut Step eksplisit:

| Role | Pre-setup | TC | Email | Env var password |
|---|---|---|---|---|
| Manage global user & role (Update) (Hendra Wijaya) | #6 | TC-FA-RP-87 | `murGlobal_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.murGlobal.email`) | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |
| Manage user & role (Group, Update, `IT Infrastructure`) (Gita Maharani) | #7 | TC-FA-RP-88 | `murGroup_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.murGroup.email`) | `Spectra.env.FA_MUR_GROUP_PASSWORD` |
| Manage global user & role tanpa Update (Bayu Prakoso) | #8 | TC-FA-RP-89 | `murReadOnlyGate_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.murGlobalReadOnly.email`) | `Spectra.env.FA_MUR_GLOBAL_RO_PASSWORD` |

- Tabel A "Tab yang diuji" (urutan baris = urutan iterasi; dipakai blok Manage global user & role (Update) dan blok Manage global user & role tanpa Update):

| Tab | Cakupan baris (hanya blok Manage global user & role (Update)) |
|---|---|
| `Total Control` | seluruh user tampil (tanpa batasan cakupan group) |
| `Read Only` | seluruh user tampil (tanpa batasan cakupan group) |
| `Group Manager` | seluruh group dan seluruh penugasan Group Manager tampil (tanpa batasan cakupan group) |

- Tabel B "Tab dengan batas cakupan Home Group" (blok Manage user & role (Group, Update)): `Total Control` dan `Read Only`; cakupan: hanya user ber-Home Group dalam cakupan `IT Infrastructure` beserta descendant.
- Data Pre-setup (Company Alpha): #12 (Maya Anggraeni, Read Only), #15 (pool pengguna), #17 (variasi Home Group), #43 (seed Group Manager). Spec membaca Pre-setup; satu-satunya perubahan data adalah seed di bullet berikut.
- Data Dinamis dan pemulihan (seed hook `before` lewat sesi API, pola spec 035 sampai 037): Gunawan Halim (Pre-setup #17, Home Group `Data Center`, dalam cakupan `IT Infrastructure`) ditetapkan Total Control, dan satu user Read Only bersuffix `Uji Read Only {runId}-023` (S-12) ber-Home Group `Data Center` di-seed. Seed ini menjamin Tab `Total Control` dan Tab `Read Only` memuat sedikitnya satu baris bagi aktor ber-cakupan `IT Infrastructure`. Hook `after` mengembalikan Gunawan Halim ke kondisi Pre-setup #17 (tanpa tingkat akses) dan menghapus user Read Only itu.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun dan tabel di atas ditambahkan tim FE.
- Kemampuan teknis: penangkapan overlay Download tanpa menyimpan berkas. State global yang diubah hanya data seed milik spec di atas (dipulihkan atau dihapus hook `after`).

## Test Steps

### TC-FA-RP-87: Manage global user & role (Update)

1. Untuk setiap baris Tabel A (langkah 1 sampai 9): klik Tab pada baris tabel
2. Verifikasi data tab dapat dibaca (sedikitnya satu baris tampil)
3. Verifikasi `[+ Assign]` Hidden pada tab itu
4. Verifikasi aksi `Remove` Hidden pada baris tab itu
5. Verifikasi cakupan baris sesuai kolom "Cakupan baris" Tabel A
6. Verifikasi ikon Download dan Changelog tampil pada tab itu
7. Klik ikon Download
8. Verifikasi menu Download dapat dibuka dengan opsi `Download as CSV` dan `Download as XLSX`
9. Tutup overlay Download dengan Esc

### TC-FA-RP-88: Manage user & role (Group, Update, `IT Infrastructure`)

10. Logout dari akun Manage global user & role (Update), lalu login sebagai Manage user & role (Group, Update) dengan `Spectra.env.FA_MUR_GROUP_PASSWORD`
11. Untuk setiap baris Tabel B (langkah 11 sampai 19): klik Tab pada baris tabel
12. Verifikasi data tab dapat dibaca (sedikitnya satu baris tampil)
13. Verifikasi `[+ Assign]` Hidden pada tab itu
14. Verifikasi aksi `Remove` Hidden pada baris tab itu
15. Verifikasi tab hanya memuat user ber-Home Group dalam cakupan `IT Infrastructure` beserta descendant
16. Verifikasi ikon Download dan Changelog tampil pada tab itu
17. Klik ikon Download
18. Verifikasi menu Download dapat dibuka dengan opsi `Download as CSV` dan `Download as XLSX`
19. Tutup overlay Download dengan Esc
20. Klik Tab `Group Manager`
21. Verifikasi data Tab `Group Manager` dapat dibaca (sedikitnya satu baris tampil)
22. Verifikasi `[+ Assign]` Hidden pada Tab `Group Manager`
23. Verifikasi aksi `Remove` Hidden pada baris Tab `Group Manager`
24. Verifikasi ikon Download dan Changelog tampil pada Tab `Group Manager`
25. Klik ikon Download
26. Verifikasi menu Download dapat dibuka dengan opsi `Download as CSV` dan `Download as XLSX`
27. Tutup overlay Download dengan Esc

### TC-FA-RP-89: Manage global user & role tanpa Update

28. Logout dari akun Manage user & role (Group, Update), lalu login sebagai Manage global user & role tanpa Update dengan `Spectra.env.FA_MUR_GLOBAL_RO_PASSWORD`
29. Untuk setiap baris Tabel A, kolom "Tab" saja (langkah 29 sampai 36): klik Tab pada baris tabel
30. Verifikasi data tab dapat dibaca (sedikitnya satu baris tampil)
31. Verifikasi `[+ Assign]` Hidden pada tab itu
32. Verifikasi aksi `Remove` Hidden pada baris tab itu
33. Verifikasi ikon Download dan Changelog tampil pada tab itu
34. Klik ikon Download
35. Verifikasi menu Download dapat dibuka dengan opsi `Download as CSV` dan `Download as XLSX`
36. Tutup overlay Download dengan Esc

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-87, 88, 89). TC-FA-RP-84 sampai 86 ada di spec `TC-FA-RP-E2E-022-role-matrix-kontrol-tab-total-control-read-only-dan-group-1`; TC-FA-RP-90 ada di spec `TC-FA-RP-E2E-024-role-matrix-kontrol-tab-total-control-read-only-dan-group-3`.
- Spec Role Matrix ditulis per blok role (bagian 3a, keputusan 2026-10-30): hasil per role berbeda dan akun pertama login di hook `before`; ganti akun pada langkah 10 dan 28. Spec memuat tampil dan Hidden dalam satu matriks visibilitas sehingga title tanpa kata Positif atau Negatif; `caseType` Negative mengikuti ketiga TC sumber (semua `Negative`).
- Pengulangan (bagian 8b butir 7): langkah 1 sampai 9 diulang untuk 3 baris Tabel A; langkah 11 sampai 19 untuk 2 baris Tabel B; langkah 29 sampai 36 untuk 3 baris Tabel A. Blok Manage user & role (Group, Update) memeriksa Tab `Group Manager` tanpa langkah cakupan karena TC-FA-RP-88 hanya menyatakan batas cakupan untuk Tab Total Control dan Read Only.
- Alasan di atas sekitar 35 langkah setelah ekspansi (36 langkah nominal; iterasi 9, 9, dan 8 langkah dikali 3, 2, dan 3 tab ditambah langkah Tab Group Manager menjadi 79 langkah): seluruh blok satu topik (kontrol tiga tab per role) dan satu kelas fungsional; tiap blok role berdiri sendiri sehingga kegagalan satu role tidak membuat role lain kehilangan makna.
- Langkah penghubung (tanpa awalan `Verifikasi`): ganti akun, klik tab, membuka dan menutup overlay Download tanpa memilih format.
- Anchor Hidden (8b butir 2): `Verifikasi` data tab dapat dibaca mendahului asersi Hidden dan asersi cakupan pada tab yang sama.
- Temuan untuk QA:
  - TC-FA-RP-87 expected c ("seluruh group dan seluruh user tampil") tidak menyebut tab mana; spec memetakan Tab Total Control dan Read Only ke "seluruh user" dan Tab Group Manager ke "seluruh group dan penugasan".
  - TC-FA-RP-87, 88, dan 89 menyatakan aksi `Remove` Hidden tanpa menyebut apakah menu `[⋯]` baris masih ada; spec tidak membuka menu `[⋯]` dan hanya memverifikasi `Remove` Hidden pada baris.
  - TC-FA-RP-88 expected c dan TC-FA-RP-86 expected c mengharapkan hanya user ber-Home Group dalam cakupan, sedangkan TC-FA-RP-47 mengharapkan Tab Total Control kosong untuk Group Manager yang sama bila tidak ada user ber-Home Group dalam cakupan; spec men-seed user ber-Home Group dalam cakupan di hook `before` sehingga asersi cakupan punya data jaminan.
  - Post Condition TC-FA-RP-87, 88, dan 89 tidak memberi langkah observasi tambahan; tidak diasersi.
