---
id: TC-FA-RP-E2E-024-role-matrix-kontrol-tab-total-control-read-only-dan-group-3
title: "Role Matrix: kontrol Tab Total Control, Read Only, dan Group Manager per peran (3/3)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-90
coverage:
  web: automated
---

# Role Matrix: kontrol Tab Total Control, Read Only, dan Group Manager per peran (3/3)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage user & role (Group) tanpa Update (Pre-setup #9); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Role yang diuji (Role Matrix negatif, satu role):

| Role | Pre-setup | TC | Email | Env var password |
|---|---|---|---|---|
| Manage user & role (Group) tanpa Update (`IT Infrastructure`) (Wulan Sari) | #9 | TC-FA-RP-90 | `murGroupReadOnly_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.murGroupReadOnly.email`) | `Spectra.env.FA_MUR_GROUP_RO_PASSWORD` |

- Tabel "Tab dengan batas cakupan Home Group" (urutan baris = urutan iterasi): `Total Control` dan `Read Only`; cakupan: hanya user ber-Home Group dalam cakupan `IT Infrastructure` beserta descendant.
- Data Pre-setup (Company Alpha): #12 (Maya Anggraeni, Read Only), #15 (pool pengguna), #17 (variasi Home Group), #43 (seed Group Manager). Spec membaca Pre-setup; satu-satunya perubahan data adalah seed di bullet berikut.
- Data Dinamis dan pemulihan (seed hook `before` lewat sesi API, pola spec 035 sampai 037): Gunawan Halim (Pre-setup #17, Home Group `Data Center`, dalam cakupan `IT Infrastructure`) ditetapkan Total Control, dan satu user Read Only bersuffix `Uji Read Only {runId}-024` (S-12) ber-Home Group `Data Center` di-seed. Seed ini menjamin Tab `Total Control` dan Tab `Read Only` memuat sedikitnya satu baris bagi aktor ber-cakupan `IT Infrastructure`. Hook `after` mengembalikan Gunawan Halim ke kondisi Pre-setup #17 (tanpa tingkat akses) dan menghapus user Read Only itu.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun ditambahkan tim FE.
- Kemampuan teknis: penangkapan overlay Download tanpa menyimpan berkas. State global yang diubah hanya data seed milik spec di atas (dipulihkan atau dihapus hook `after`).

## Test Steps

### TC-FA-RP-90: Manage user & role tanpa Update (Group, `IT Infrastructure`)

1. Untuk setiap baris tabel "Tab dengan batas cakupan Home Group" (langkah 1 sampai 9): klik Tab pada baris tabel
2. Verifikasi data tab dapat dibaca (sedikitnya satu baris tampil)
3. Verifikasi `[+ Assign]` Hidden pada tab itu
4. Verifikasi aksi `Remove` Hidden pada baris tab itu
5. Verifikasi tab hanya memuat user ber-Home Group dalam cakupan `IT Infrastructure` beserta descendant
6. Verifikasi ikon Download dan Changelog tampil pada tab itu
7. Klik ikon Download
8. Verifikasi menu Download dapat dibuka dengan opsi `Download as CSV` dan `Download as XLSX`
9. Tutup overlay Download dengan Esc
10. Klik Tab `Group Manager`
11. Verifikasi data Tab `Group Manager` dapat dibaca (sedikitnya satu baris tampil)
12. Verifikasi `[+ Assign]` Hidden pada Tab `Group Manager`
13. Verifikasi aksi `Remove` Hidden pada baris Tab `Group Manager`
14. Verifikasi ikon Download dan Changelog tampil pada Tab `Group Manager`
15. Klik ikon Download
16. Verifikasi menu Download dapat dibuka dengan opsi `Download as CSV` dan `Download as XLSX`
17. Tutup overlay Download dengan Esc

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-90). TC-FA-RP-84 sampai 89 ada di spec `TC-FA-RP-E2E-022-role-matrix-kontrol-tab-total-control-read-only-dan-group-1` dan `TC-FA-RP-E2E-023-role-matrix-kontrol-tab-total-control-read-only-dan-group-2`.
- Spec Role Matrix negatif satu role (bagian 3a); title tanpa kata Negatif karena mengikuti seri matriks visibilitas per role.
- Pengulangan (bagian 8b butir 7): langkah 1 sampai 9 diulang untuk 2 baris tabel (Tab `Total Control` dan `Read Only`); Tab `Group Manager` ditulis eksplisit tanpa langkah cakupan karena TC-FA-RP-90 hanya menyatakan batas cakupan untuk Tab Total Control dan Read Only.
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab dan membuka dan menutup overlay Download tanpa memilih format.
- Anchor Hidden (8b butir 2): `Verifikasi` data tab dapat dibaca mendahului asersi Hidden dan asersi cakupan pada tab yang sama.
- Temuan untuk QA:
  - TC-FA-RP-90 menyatakan aksi `Remove` Hidden tanpa menyebut apakah menu `[⋯]` baris masih ada; spec tidak membuka menu `[⋯]` dan hanya memverifikasi `Remove` Hidden pada baris.
  - TC-FA-RP-90 expected c mengharapkan hanya user ber-Home Group dalam cakupan, sedangkan TC-FA-RP-47 mengharapkan Tab Total Control kosong bagi Group Manager bila tidak ada user ber-Home Group dalam cakupan; spec men-seed user ber-Home Group dalam cakupan di hook `before` sehingga asersi cakupan punya data jaminan.
  - Post Condition TC-FA-RP-90 tidak memberi langkah observasi tambahan; tidak diasersi.
