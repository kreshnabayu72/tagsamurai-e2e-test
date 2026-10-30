---
id: TC-GS-UCF-E2E-024-form-user-numeric-input-dan-validasi-digit-desimal
title: "Form User: Input Numeric (Karakter Diizinkan, Batas 15 Digit, Decimal Places) dan Simpan 15 Digit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UCF-177
  - TC-GS-UCF-545
  - TC-GS-UCF-546
  - TC-GS-UCF-476
  - TC-GS-UCF-179
  - TC-GS-UCF-389
  - TC-GS-UCF-350
  - TC-GS-UCF-178
coverage:
  web: automated
---

# Form User: Input Numeric (Karakter Diizinkan, Batas 15 Digit, Decimal Places) dan Simpan 15 Digit

## Prerequisites

- Mode: FE+BE (backend nyata). Cakupan lintas modul: field Custom Field Numeric pada form Create User (modul User) dan Detail User.
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`; environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_<page_key>` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Layar awal: Global Settings > User > User List sub-tab Login User, dibuka di hook `beforeEach`.
- Data Pre-setup (di-seed lewat API di hook `before`, idempotent, fixture `Fixture.customFieldUser.preset14` (fixture baru, belum ada; lihat coverage); hanya dibaca): 14 Custom Field aktif Client A (D-01): 6 Pre-setup (`Cost Center` Dropdown `Finance`, `Operations`, `Marketing`, Required Yes; `Employee Grade`; `Job Description`; `Bonus` Numeric Decimal Places 2; `Office Phone` Phone Required Yes; `Joining Date` [Inactive]) dan 8 Population (`Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID` Text Required Yes, `Work Notes`, `Annual Target`, `badge number`). Hanya `Bonus` yang diasersi; `Cost Center`, `Office Phone`, dan `Tax ID` diisi sebagai Custom Field Required; field lain dipakai sebagai precondition TC (14 field aktif), tidak diasersi.
- Data dinamis (di-seed lewat API di hook `before` sebagai precondition): `Dec Form` (D-133, Numeric Decimal Places 2, belum pernah bernilai; diedit spec ini menjadi Decimal Places 0) dan `Dec One` (D-203, Numeric Decimal Places 1, belum pernah bernilai). Nama literal karena pesan error (`Dec form must ...`, `Dec one must ...`) diturunkan dari Field Name (pengecualian S-12 butir (ii)); seeding idempotent (dilewati bila sudah ada), hook `before` menghapus sisa field bernama sama dari run lain, hook `after` menghapus yang dibuat spec ini.
- Data dinamis dibuat lewat UI: User `Probe Custom` (D-78 `User Num15`) dengan Email `probeCustom178_automated_qaTeam1+{runId}-024@qwertysystem.net` dan Bonus `-1234567890123.45` (TC-GS-UCF-178; `{runId}` terdiri atas digit). Hook `after` menghapus user ini lewat API.
- Kondisi D-158 (precondition TC): Custom Field Required Yes yang Active di Client A hanya `Cost Center`, `Office Phone`, dan `Tax ID`; dijamin oleh hook `before` suite (butir D-158 di `suite.md`: Custom Field Required Yes Active selain yang disebut dinonaktifkan atau dihapus lewat API sebelum spec berjalan dan dipulihkan di hook `after` suite; mekanisme disediakan tim FE/BE); spec ini tidak mengubah status field.
- Field wajib Create User (fixture form, tabel Data Uji Pre-setup TC): First Name `Probe`, Last Name `Custom`, Email `probeCustom<n>_automated_qaTeam1+{runId}-024@qwertysystem.net` (n = nomor TC), Division = Division Client A mana pun (fixture modul Division, disediakan tim FE), Access = opsi pertama yang tersedia untuk Client A; field User opsional dikosongkan. Custom Field Required: Cost Center `Finance`, Office Phone Country Code `🇮🇩 +62` dengan Number `81234567890`, Tax ID `TX-001`.
- Nilai yang hanya diketik: `abc`, `12-5`, `-12.5`, `1,5`, `1e5`, `1.2`, `1.2.3`, `--5`, `12.34`, `12.3`, `1234567890123456`, `12.345`, `-`, `0000000000000001`, `12.5`, `12.`, `.`.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API user `Probe Custom` (Email memuat `{runId}-024`), `Dec Form`, dan `Dec One`.
- Kemampuan teknis: mengetik karakter satu per ketukan pada input Numeric; membaca nilai input; membuka Detail User (section Custom Fields) dari modul User; menutup popup Create User dirty lewat `[✕]` dan `[Leave]`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### Sesi form 1 (tanpa membuat user)

1. Klik [+ User] pada tab User List sub-tab Login User

#### TC-GS-UCF-177: Field Numeric hanya menerima angka, tanda minus awal, dan titik desimal

2. Ketik `abc` di Bonus
3. Verifikasi `abc` tidak masuk ke field Bonus
4. Ketik `12-5` di Bonus
5. Verifikasi tanda minus tidak dapat diketik di tengah angka
6. Kosongkan Bonus, lalu ketik `-12.5`
7. Verifikasi `-12.5` diterima persis
8. Kosongkan Bonus, lalu ketik `1,5`
9. Verifikasi koma tidak masuk ke field Bonus
10. Kosongkan Bonus, lalu ketik `1e5`
11. Verifikasi `e` tidak masuk ke field Bonus

#### TC-GS-UCF-545: Field Numeric tidak menerima titik desimal kedua saat diketik

12. Kosongkan Bonus, ketik `1.2`, lalu ketik `.`
13. Verifikasi nilai Bonus tetap `1.2`
14. Verifikasi tidak ada pesan error pada Bonus
15. Kosongkan Bonus, lalu ketik `1.2.3` satu karakter per ketukan
16. Verifikasi nilai Bonus menjadi `1.23` (titik kedua diblok, digit `3` diterima)
17. Verifikasi tidak ada pesan error pada Bonus

#### TC-GS-UCF-546: Field Numeric tidak menerima tanda minus selain di posisi awal saat diketik

18. Kosongkan Bonus, lalu ketik `--5` satu karakter per ketukan
19. Verifikasi nilai Bonus menjadi `-5` (tanda minus kedua diblok tanpa pesan)
20. Verifikasi tidak ada pesan error inline pada Bonus karena `-5` adalah angka valid

#### TC-GS-UCF-476: Numeric Decimal Places 1: satu digit desimal diterima dan dua digit ditolak

21. Ketik `12.34` di Dec One
22. Verifikasi error inline `Dec one must have at most 1 decimal place(s)` muncul real-time
23. Ganti isi Dec One dengan `12.3`
24. Verifikasi tidak ada error pada Dec One

#### TC-GS-UCF-179: Numeric melebihi 15 digit atau melebihi Decimal Places menampilkan error inline

25. Kosongkan Bonus dan Dec One, lalu isi Field wajib Create User (Email `probeCustom179_automated_qaTeam1+{runId}-024@qwertysystem.net`) dan Custom Field Required
26. Ketik `1234567890123456` (16 digit) di Bonus
27. Verifikasi error inline `Max. 15 characters` muncul real-time
28. Klik [Submit]
29. Verifikasi popup Create User tetap terbuka
30. Verifikasi error inline `Max. 15 characters` tetap tampil
31. Verifikasi tidak ada toast sukses
32. Ganti isi Bonus dengan `12.345`
33. Verifikasi error inline `Bonus must have at most 2 decimal place(s)`
34. Ganti isi Bonus dengan `-`
35. Verifikasi error inline `Bonus must be a number`

#### TC-GS-UCF-389: Batas 15 digit Numeric dihitung pada teks yang diketik sebelum normalisasi

36. Ganti isi Bonus dengan `0000000000000001` (16 digit)
37. Verifikasi error inline `Max. 15 characters`
38. Klik [Submit]
39. Verifikasi popup Create User tetap terbuka
40. Verifikasi error inline `Max. 15 characters` tetap tampil
41. Verifikasi tidak ada toast sukses
42. Hapus satu angka `0` di depan sehingga tersisa 15 digit
43. Verifikasi tidak ada error pada Bonus
44. Klik `[✕]`
45. Verifikasi dialog `Unsaved Changes` tampil
46. Klik [Leave]

### TC-GS-UCF-350: Decimal Places yang diubah sebelum field punya nilai berlaku pada validasi form User berikutnya

47. Buka Global Settings > User > tab Custom Field
48. Ketik Search `Dec Form`, tekan Enter
49. Klik `⋯` pada baris `Dec Form` > Edit
50. Ubah Decimal Places menjadi `0`
51. Klik [Save]
52. Verifikasi toast sukses: "Success, custom field has been updated."
53. Buka Global Settings > User > User List sub-tab Login User, klik [+ User]
54. Isi Field wajib Create User (Email `probeCustom350_automated_qaTeam1+{runId}-024@qwertysystem.net`) dan Custom Field Required
55. Ketik `12.5` di Dec Form
56. Klik [Submit]
57. Verifikasi error inline `Dec form must have at most 0 decimal place(s)`
58. Verifikasi popup Create User tetap terbuka
59. Verifikasi tidak ada toast sukses
60. Kosongkan Dec Form, lalu ketik `12.`
61. Verifikasi tidak ada error pada Dec Form (titik dapat diketik pada Decimal Places 0)
62. Kosongkan Dec Form, lalu ketik `.`
63. Verifikasi error inline `Dec form must be a number`
64. Klik `[✕]`
65. Verifikasi dialog `Unsaved Changes` tampil
66. Klik [Leave]

### TC-GS-UCF-178: Numeric menerima tepat 15 digit termasuk digit desimal dan minus serta titik tidak dihitung

67. Klik [+ User] pada tab User List sub-tab Login User
68. Ketik `-1234567890123.45` di Bonus
69. Verifikasi tidak ada error pada Bonus
70. Isi Field wajib Create User (First Name `Probe`, Last Name `Custom`, Email `probeCustom178_automated_qaTeam1+{runId}-024@qwertysystem.net`) dan Custom Field Required
71. Klik [Submit]
72. Buka Global Settings > User > Detail User dengan Email `probeCustom178_automated_qaTeam1+{runId}-024@qwertysystem.net`, section Custom Fields
73. Verifikasi Detail User `Probe Custom` menampilkan Bonus `-1234567890123.45`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Spec melewati sekitar 35 langkah (smell, bagian 3 prinsip 13 konvensi): 8 TC satu topik (input dan validasi Numeric pada form User) dengan satu akun; setiap Expected bermajemuk dipecah satu `Verifikasi` per klausa (S-01) dan blok per TC tetap bermakna bila blok sebelumnya gagal.
- Subjudul memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 177, 545, 546, 476, 179, 389 (sesi form 1: mengetik dan Submit diblokir, tanpa data), lalu 350 (mengubah Decimal Places `Dec Form`), lalu 178 (membuat user, paling akhir). Urutan sumber (177, 545, 546, 178, 179, 350, 476, 389) berubah demi satu sesi form (bagian 3 prinsip 3, 6, 7, dan 13 "halaman yang sama dipakai berulang"). Pembukaan form: 3 (langkah 1, 53, 67); kejadian menutup form: 3 (langkah 44 sampai 46, 64 sampai 66, dan Submit user pada langkah 71).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6, 8, 10, 12, 15, 18 (mengosongkan lalu mengetik sebagai bagian langkah TC), langkah 25 (menyiapkan field wajib agar Submit TC-GS-UCF-179 dan 389 hanya diblokir oleh error Bonus; precondition TC), langkah 47 dan 53 (pindah tab), langkah 48 (Search), langkah 44 sampai 46 dan 64 sampai 66 (menutup form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08).
- Langkah 70 mengisi field wajib setelah Bonus diketik (urutan langkah TC-GS-UCF-178 Langkah 2 dan 3).
- Asersi "tidak ada toast sukses" (langkah 31, 41, 59) memakai popup yang tetap terbuka sebagai bukti Submit diblokir.
- Temuan untuk QA:
  - TC-GS-UCF-178 Expected hanya "Tidak ada error" dan Detail User tanpa toast; teks toast Create User tidak tertulis di TC (modul User) sehingga tidak diasersi.
  - TC-GS-UCF-179 Expected c dan d memakai pesan `[Field name] must have at most [N] decimal place(s)` dan `[Field name] must be a number`; spec mengikuti TC (NC-05) dan hanya mengasersi pesan itu untuk `12.345` dan `-`.
  - TC-GS-UCF-177 Langkah 2 sampai 5 tidak menyebut pengosongan Bonus di antara kasus `abc`, `12-5`, dan `1,5`/`1e5`, padahal nilai sisa kasus sebelumnya memengaruhi hasil; spec mengosongkan Bonus sebelum tiap kasus.
  - Nama `Dec Form` dan `Dec One` literal (pengecualian S-12 butir (ii), nama penentu pesan error).
