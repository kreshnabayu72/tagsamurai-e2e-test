---
id: TC-FA-RP-E2E-022-role-matrix-kontrol-tab-total-control-read-only-dan-group-1
title: "Role Matrix: kontrol Tab Total Control, Read Only, dan Group Manager per peran (1/3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-84
  - TC-FA-RP-85
  - TC-FA-RP-86
coverage:
  web: automated
---

# Role Matrix: kontrol Tab Total Control, Read Only, dan Group Manager per peran (1/3)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2, role pertama pada tabel); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Role yang diuji (Role Matrix, bagian 3a); urutan baris = urutan pemakaian; spec ditulis per blok role karena hasil per role berbeda dan ganti akun menuntut Step eksplisit:

| Role | Pre-setup | TC | Email | Env var password |
|---|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | TC-FA-RP-84 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |
| Read Only (Dewi Anggraini) | #4 | TC-FA-RP-85 | `readOnly_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.readOnly.email`) | `Spectra.env.FA_RO_PASSWORD` |
| Group Manager (Fajar Nugroho, `IT Infrastructure`) | #5 | TC-FA-RP-86 | `groupManager_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.groupManager.email`) | `Spectra.env.FA_GM_PASSWORD` |

- Tabel "Tab yang diuji" (urutan baris = urutan iterasi):

| Tab | Baris target untuk menu `[⋯]` (blok Total Control; target selain Default User dan diri sendiri) | Cakupan baris yang diverifikasi (blok Group Manager) |
|---|---|---|
| `Total Control` | Rina Wulandari (Pre-setup #3) | hanya user ber-Home Group dalam cakupan `IT Infrastructure` beserta descendant |
| `Read Only` | Maya Anggraeni (Pre-setup #12) | hanya user ber-Home Group dalam cakupan `IT Infrastructure` beserta descendant |
| `Group Manager` | Kevin Susanto (Pre-setup #43) | penugasan Group Manager dalam cakupan `IT Infrastructure` beserta descendant |

- Data Pre-setup (Company Alpha): #12 (Maya Anggraeni, Read Only), #15 (pool pengguna), #17 (variasi Home Group), #43 (seed Group Manager). Spec membaca Pre-setup; menu `[⋯]` dibuka tanpa memilih `Remove`; satu-satunya perubahan data adalah seed di bullet berikut.
- Data Dinamis dan pemulihan (seed hook `before` lewat sesi API, pola spec 035 sampai 037): Gunawan Halim (Pre-setup #17, Home Group `Data Center`, dalam cakupan `IT Infrastructure`) ditetapkan Total Control, dan satu user Read Only bersuffix `Uji Read Only {runId}-022` (S-12) ber-Home Group `Data Center` di-seed. Seed ini menjamin Tab `Total Control` dan Tab `Read Only` memuat sedikitnya satu baris bagi aktor ber-cakupan `IT Infrastructure`. Hook `after` mengembalikan Gunawan Halim ke kondisi Pre-setup #17 (tanpa tingkat akses) dan menghapus user Read Only itu.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun dan tabel di atas ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): penangkapan overlay Download tanpa menyimpan berkas. State global yang diubah hanya data seed milik spec di atas (dipulihkan atau dihapus hook `after`).

## Test Steps

### TC-FA-RP-84: Total Control

1. Untuk setiap baris tabel "Tab yang diuji" (langkah 1 sampai 10): klik Tab pada baris tabel
2. Verifikasi `[+ Assign]` tampil (Show) pada tab itu
3. Klik `[⋯]` pada baris target di kolom "Baris target" tabel
4. Verifikasi menu `[⋯]` baris memuat `Remove` dengan status Enabled
5. Tutup menu `[⋯]` dengan Esc
6. Verifikasi ikon Download dan Changelog tampil pada tab itu
7. Klik ikon Download
8. Verifikasi menu Download dapat dibuka dengan opsi `Download as CSV` dan `Download as XLSX`
9. Tutup overlay Download dengan Esc
10. Verifikasi data tab dapat dibaca (sedikitnya satu baris tampil)

### TC-FA-RP-85: Read Only

11. Logout dari akun Total Control, lalu login sebagai Read Only dengan `Spectra.env.FA_RO_PASSWORD`
12. Untuk setiap baris tabel "Tab yang diuji" (langkah 12 sampai 19): klik Tab pada baris tabel
13. Verifikasi `[+ Assign]` Hidden pada tab itu
14. Verifikasi aksi `Remove` Hidden pada baris tab itu
15. Verifikasi ikon Download dan Changelog tampil pada tab itu
16. Klik ikon Download
17. Verifikasi menu Download dapat dibuka dengan opsi `Download as CSV` dan `Download as XLSX`
18. Tutup overlay Download dengan Esc
19. Verifikasi data tab dapat dibaca (sedikitnya satu baris tampil)

### TC-FA-RP-86: Group Manager (Fajar Nugroho, `IT Infrastructure`)

20. Logout dari akun Read Only, lalu login sebagai Group Manager dengan `Spectra.env.FA_GM_PASSWORD`
21. Untuk setiap baris tabel "Tab yang diuji" (langkah 21 sampai 29): klik Tab pada baris tabel
22. Verifikasi data tab dapat dibaca (sedikitnya satu baris tampil)
23. Verifikasi `[+ Assign]` Hidden pada tab itu
24. Verifikasi aksi `Remove` Hidden pada baris tab itu
25. Verifikasi baris tab sesuai kolom "Cakupan baris yang diverifikasi" tabel
26. Verifikasi ikon Download dan Changelog tampil pada tab itu
27. Klik ikon Download
28. Verifikasi menu Download dapat dibuka dengan opsi `Download as CSV` dan `Download as XLSX`
29. Tutup overlay Download dengan Esc

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-84, 85, 86). TC-FA-RP-87 sampai 89 ada di spec `TC-FA-RP-E2E-023-role-matrix-kontrol-tab-total-control-read-only-dan-group-2`; TC-FA-RP-90 ada di spec `TC-FA-RP-E2E-024-role-matrix-kontrol-tab-total-control-read-only-dan-group-3`.
- Spec Role Matrix ditulis per blok role (bagian 3a, keputusan 2026-10-30): hasil per role berbeda dan akun pertama login di hook `before`; ganti akun pada langkah 11 dan 20. Susunan tampil dan Hidden dalam satu spec (matriks visibilitas, bagian 3a) sehingga title tanpa kata Positif atau Negatif.
- Pengulangan (bagian 8b butir 7): langkah 1 sampai 10, 12 sampai 19, dan 21 sampai 29 diulang untuk 3 baris tabel "Tab yang diuji" pada tiap blok. Parameter tiap iterasi ada di tabel Prerequisites.
- Alasan di atas sekitar 35 langkah setelah ekspansi (29 langkah nominal; tiga blok role dengan iterasi 10, 8, dan 9 langkah dikali 3 tab menjadi 83 langkah): seluruh blok satu topik (kontrol tiga tab per role) dan satu kelas fungsional; tiap blok role berdiri sendiri sehingga kegagalan satu role tidak membuat role lain kehilangan makna.
- Langkah penghubung (tanpa awalan `Verifikasi`): ganti akun, klik tab, membuka dan menutup menu `[⋯]` dan overlay Download. Overlay Download dibuka untuk membuktikan "Menu Download dapat dibaca" dan ditutup tanpa memilih format.
- Anchor Hidden (8b butir 2): Table Tools dan halaman yang sudah termuat menjadi anchor permukaan untuk Hidden `[+ Assign]` dan `Remove`; ikon Download dan Changelog yang tampil pada tab yang sama memperkuatnya.
- Temuan untuk QA:
  - TC-FA-RP-84 expected b menyebut target "selain Default User dan diri sendiri" tanpa nama baris; spec memakai Rina Wulandari (Tab Total Control), Maya Anggraeni (Tab Read Only), dan Kevin Susanto (Tab Group Manager).
  - TC-FA-RP-85 dan 86 menyatakan aksi `Remove` Hidden tanpa menyebut apakah menu `[⋯]` baris masih ada untuk role tanpa aksi lain; spec tidak membuka menu `[⋯]` pada blok Read Only dan Group Manager dan hanya memverifikasi `Remove` Hidden pada baris.
  - TC-FA-RP-86 expected c bahwa Tab Total Control dan Read Only "hanya memuat user ber-Home Group dalam cakupan" tidak sejalan dengan TC-FA-RP-47 (Tab Total Control kosong bagi Group Manager yang sama bila tidak ada user ber-Home Group dalam cakupan); spec memverifikasi sesuai Pre-setup #17 ditambah seed hook `before` (Gunawan Halim Total Control dan satu user Read Only ber-Home Group `Data Center`) dan tidak menyebut baris pembanding spesifik.
  - TC-FA-RP-84 expected d "Menu Download dan data tab dapat dibaca" tidak menyebut format; spec hanya membuka overlay Download tanpa mengunduh.
  - Post Condition TC-FA-RP-84, 85, dan 86 tidak memberi langkah observasi tambahan; tidak diasersi.
