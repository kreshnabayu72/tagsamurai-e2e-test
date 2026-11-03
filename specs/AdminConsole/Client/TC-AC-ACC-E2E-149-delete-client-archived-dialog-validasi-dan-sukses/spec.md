---
id: TC-AC-ACC-E2E-149-delete-client-archived-dialog-validasi-dan-sukses
title: "Delete Client Archived: Dialog Konfirmasi D-05 dan Warning D-04, Tombol Delete Disabled Sampai Nama dan Checkbox Valid, Cancel, serta Delete Sukses"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-651
  - TC-AC-ACC-220
  - TC-AC-ACC-221
  - TC-AC-ACC-218
  - TC-AC-ACC-219
coverage:
  web: automated
---

# Delete Client Archived: Dialog Konfirmasi D-05 dan Warning D-04, Tombol Delete Disabled Sampai Nama dan Checkbox Valid, Cancel, serta Delete Sukses

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Archived-Delete-Only A-10 `archivedDeleteJakarta_automated_qaTeam1@qwertysystem.net`, password dari `AC_CLIENT_ARCHIVED_DELETE_PASSWORD` (Manage archived client: Delete + Read, exact-match Area Jakarta). Login di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Data Pre-setup (Tabel A2, kelas Dikonsumsi pada blok Delete sukses): C-05 `PT Lama Tak Berbayar` (Archived; FAMS Purge, SAMS Deleted; tanpa user ber-App Access; dipakai TC-AC-ACC-651, 220, dan 218) dan C-04 `PT Karya Abadi` (Archived; FAMS, SAMS, SIEM Archive; 2 user dengan App Access di bawah Client ini; dipakai TC-AC-ACC-219). Partner CV Mitra Sejati (pengelola kedua Client) memiliki user A-14 (user Partner tidak dihitung pada kalimat jumlah user). Fixture BE (disediakan tim FE/BE, idempotent) men-seed ulang C-05 dan C-04 di hook `before` dan `after` (TC-AC-ACC-218 dan 219 menghapusnya; C-04 juga dipakai sebagai target baca atau tolak pada spec lain di suite, sehingga seed ulang dijamin sebelum spec itu berjalan; suite serial).
- Efek Delete: Client soft-delete; relasi Client–Partner `transferred`; relasi Group dilepas; riwayat subscription dan log tetap tersimpan; baris Changelog `Delete` ditulis.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### TC-AC-ACC-651: Delete Client Archived tanpa user App Access sendiri yang dikelola Partner ber-user: dialog konfirmasi D-05, bukan D-04

1. Klik sub-tab Archived
2. Ketik Search `PT Lama Tak Berbayar`, tekan Enter
3. Klik `[⋯]` pada baris `PT Lama Tak Berbayar` → klik `Delete`
4. Verifikasi header dialog berjudul "Delete Client"
5. Verifikasi body dialog memuat bullet `• PT Lama Tak Berbayar`
6. Verifikasi body dialog memuat "This client will be removed and can no longer be accessed. This action cannot be undone. Are you sure you want to delete it?"
7. Verifikasi dialog memuat input "Type the client name to confirm" dan checkbox "I understand this action cannot be undone"
8. Verifikasi footer memuat `[Cancel]` dan `[Delete]` yang disabled sampai nama cocok dan checkbox dicentang
9. Verifikasi lebar dialog 480px
10. Verifikasi kalimat "This client has [N] user(s) with product access." tidak tampil
11. Klik `[Cancel]`
12. Verifikasi dialog tertutup
13. Verifikasi baris `PT Lama Tak Berbayar` tetap tampil di sub-tab Archived

### TC-AC-ACC-220: Tombol Delete disabled sampai nama cocok persis (case-sensitive) dan checkbox dicentang

14. Klik `[⋯]` pada baris `PT Lama Tak Berbayar` dan pilih `Delete`
15. Centang checkbox "I understand this action cannot be undone" tanpa mengetik nama
16. Verifikasi `[Delete]` tampil dan disabled
17. Ketik `pt lama tak berbayar` pada input "Type the client name to confirm"
18. Verifikasi `[Delete]` tampil dan disabled
19. Ganti isi input dengan `PT Lama Tak Berbaya` (nama terpotong)
20. Verifikasi `[Delete]` tampil dan disabled
21. Ganti isi input dengan `PT Lama Tak Berbayar` (nama persis)
22. Verifikasi `[Delete]` enabled
23. Hapus karakter terakhir nama
24. Verifikasi `[Delete]` kembali disabled
25. Ketik ulang `PT Lama Tak Berbayar`, lalu hilangkan centang checkbox
26. Verifikasi `[Delete]` kembali disabled
27. Centang checkbox kembali
28. Verifikasi `[Delete]` enabled kembali
29. Klik `[Cancel]`
30. Verifikasi dialog tertutup
31. Verifikasi Client `PT Lama Tak Berbayar` tetap ada

### TC-AC-ACC-221: Cancel pada dialog Delete

32. Klik `[⋯]` pada baris `PT Lama Tak Berbayar` dan pilih `Delete`
33. Klik `[Cancel]`
34. Verifikasi dialog tertutup
35. Verifikasi Client `PT Lama Tak Berbayar` tetap ada

### TC-AC-ACC-218: Delete Client Archived tanpa user App Access: dialog konfirmasi D-05 dan Delete sukses

36. Klik `[⋯]` pada baris `PT Lama Tak Berbayar` dan pilih `Delete`
37. Verifikasi dialog Title "Delete Client" dengan bullet `• PT Lama Tak Berbayar`
38. Verifikasi dialog memuat input "Type the client name to confirm" (placeholder = Company Name) dan checkbox "I understand this action cannot be undone"
39. Verifikasi `[Delete]` (danger) disabled sebelum nama cocok dan checkbox dicentang
40. Ketik nama persis `PT Lama Tak Berbayar`, centang checkbox, klik `[Delete]`
41. Verifikasi toast sukses "Success, client has been deleted."
42. Verifikasi baris `PT Lama Tak Berbayar` hilang dari list

### TC-AC-ACC-219: Delete Client Archived dengan user App Access: dialog warning D-04 menghitung hanya user Client itu sendiri

43. Ketik Search `PT Karya Abadi`, tekan Enter
44. Klik `[⋯]` pada baris `PT Karya Abadi` → klik `Delete`
45. Verifikasi dialog warning Title "Delete Client" dengan bullet `• PT Karya Abadi`
46. Verifikasi body dialog memuat "This client has 2 user(s) with product access. This client will be removed and can no longer be accessed. This action cannot be undone. Are you sure you want to delete it?"
47. Verifikasi angka 2 hanya menghitung user di bawah "PT Karya Abadi" (user CV Mitra Sejati tidak dihitung)
48. Verifikasi dialog memuat input "Type the client name to confirm" dan checkbox "I understand this action cannot be undone"
49. Verifikasi footer memuat `[Cancel]` dan `[Delete]` dengan lebar dialog 480px
50. Ketik nama persis `PT Karya Abadi`, centang checkbox, klik `[Delete]`
51. Verifikasi toast sukses "Success, client has been deleted."

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC menyimpang dari urutan nomor: TC-AC-ACC-651, 220, dan 221 (dialog dan Cancel, tanpa mengubah data) mendahului TC-AC-ACC-218 dan 219 (Delete yang menghabisi data) karena aksi yang menghabisi data ditaruh paling akhir dan Client `PT Lama Tak Berbayar` harus masih ada untuk blok sebelumnya (prinsip 5; S-05).
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas lima TC satu topik (dialog Delete Client Archived), satu akun, satu kelas harness; blok dialog dan Cancel tetap bermakna walau blok Delete yang mengikutinya gagal, dan Delete di akhir.
- Asersi tambahan yang dicatat (S-03): langkah 10 sampai 11 dan 21 sampai 28 mengikuti Expected TC-AC-ACC-651 dan 220; langkah 36 sampai 39 mengamati dialog TC-AC-ACC-218 (Expected a) yang sama dengan blok sebelumnya karena TC-AC-ACC-218 menyatakannya sendiri. Langkah penghubung (tanpa awalan Verifikasi): Search yang menemukan baris target (R-16) dan `[Cancel]` penutup.
- Post Condition TC-AC-ACC-218 butir a sampai c (soft-delete, riwayat tersimpan, Changelog `Delete` Field `Company Name`) dan TC-AC-ACC-219 tanpa langkah observasi di TC tidak diasersi selain Expected; seed ulang C-05 dan C-04 dilakukan di hook.
- Temuan untuk QA:
  - TC-AC-ACC-219 Precondition d menyebut Partner CV Mitra Sejati memiliki user (A-14) tanpa Expected terpisah tentang user Partner; spec mengasersi bahwa angka 2 tidak mencakup user Partner (Expected a).
  - TC-AC-ACC-219 menghapus C-04 `PT Karya Abadi` yang dipakai TC lain sebagai target baca atau tolak (TC-AC-ACC-226, 227, 232, 455); seed ulang diperlukan sebelum spec itu berjalan (suite serial).
  - TC-AC-ACC-218 Post Condition butir c dan d tidak punya langkah observasi; Changelog `Delete` hanya diasersi pada TC lain yang menyebutnya di Expected.
