---
id: TC-GS-ROLE-E2E-072-resilience-tulis-edit-crud-dan-remove-baris
title: "Resilience Tulis: Edit CRUD, Auto-Revert, dan Remove Baris Role Gagal 5xx"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-108
  - TC-GS-ROLE-109
  - TC-GS-ROLE-117
  - TC-GS-ROLE-118
coverage:
  web: automated
---

# Resilience Tulis: Edit CRUD, Auto-Revert, dan Remove Baris Role Gagal 5xx

## Prerequisites

- Mode: FE+BE dengan intercept parsial di atas backend nyata (bagian 6 konvensi; kelas harness fault injection, prinsip 13b).
- Akun aktor: Total Control, Ahmad Fauzi (`Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission > System > Detail "Manage TAG".
- Seeding precondition TC (Given; lewat API oleh akun Ahmad Fauzi di hook `before`; kemampuan dari `openapi.yaml`: POST/DELETE `/v2/iam/products/{product}/roles/access-level` dan POST/DELETE `/v2/iam/products/{product}/roles/capabilities/users`):
  - Wawan Setiawan (Pre-setup #11): di-assign baris Manage TAG (Read checked, Update unchecked) dan baris Manage files (Tabel Data Uji Dinamis #5), sebagai target TC-GS-ROLE-108 dan TC-GS-ROLE-117.
  - Rudi Hartono (Pre-setup #11, Pending Activation): di-assign Total Control (Tabel Data Uji Dinamis #2), sebagai target TC-GS-ROLE-109.
  - Siti Nurhaliza (Pre-setup #4, Read Only): di-assign Total Control (upgrade; Tabel Data Uji Dinamis #3), sebagai target TC-GS-ROLE-118.
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah, tanpa berasumsi seeding berhasil penuh), lewat API: Wawan Setiawan dan Rudi Hartono dikembalikan ke kondisi kandidat Pre-setup #11 (tanpa access level, tanpa baris role); Siti Nurhaliza dikembalikan ke Read Only (Pre-setup #4) dengan Remove Total Control lalu Assign Read Only. Efek pada Modified By dan Last Updated Siti Nurhaliza di Tab Read Only tidak diasersi.
- Kebutuhan intercept (`Spectra.intercept()`), semuanya pada request tulis, dilepas segera setelah dipakai, respons dipaksa HTTP 500 tanpa meneruskan request ke server:
  - Edit CRUD: `PATCH /v2/iam/products/{product}/roles/capabilities/users/{user_id}` (`openapi.yaml`, `low-level-design.md`) (TC-GS-ROLE-108 dan TC-GS-ROLE-109; TC-GS-ROLE-109 memakai pesan gagal yang sama dengan Edit CRUD sesuai judulnya);
  - Remove baris role: `DELETE /v2/iam/products/{product}/roles/capabilities/users` (TC-GS-ROLE-117 dan TC-GS-ROLE-118).
- Kemampuan teknis: membaca state checkbox sel CRUD; menekan F5.
- Pemulihan lain di hook `after`: semua intercept dilepas; dialog Remove ditutup.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-108: Edit CRUD gagal 5xx pada target biasa

1. Ketik Search `Wawan Setiawan`, tekan Enter
2. Pasang intercept pada respons Edit CRUD: jawab 500
3. Centang Update pada baris Wawan Setiawan
4. Verifikasi toast error `Error, failed to update permissions.`
5. Verifikasi checkbox Update baris Wawan Setiawan kembali ke nilai tersimpan (unchecked)
6. Lepas intercept 500
7. Tekan F5
8. Ketik Search `Wawan Setiawan`, tekan Enter
9. Verifikasi checkbox Update baris Wawan Setiawan tetap unchecked
10. Klik `(←)` pada kotak Search

### TC-GS-ROLE-109: Auto-revert gagal 5xx memakai pesan gagal Edit CRUD

11. Ketik Search `Rudi Hartono`, tekan Enter
12. Hapus centang Update pada baris Rudi Hartono
13. Verifikasi checkbox Update baris Rudi Hartono menampilkan nilai baru (unchecked) selama dialog `Remove Access` terbuka sebelum submit
14. Pasang intercept pada respons Edit CRUD: jawab 500
15. Klik `[Remove]` pada dialog `Remove Access`
16. Verifikasi toast error `Error, failed to update permissions.`
17. Verifikasi dialog `Remove Access` tetap terbuka
18. Verifikasi `[Remove]` aktif kembali untuk retry
19. Verifikasi checkbox Update baris Rudi Hartono tetap menampilkan nilai baru (unchecked) setelah gagal
20. Lepas intercept 500
21. Klik `[Cancel]` pada dialog `Remove Access`
22. Verifikasi checkbox Update baris Rudi Hartono kembali checked
23. Klik `(←)` pada kotak Search
24. Klik menu sidebar `Role & Permission`
25. Klik Tab `Total Control`
26. Ketik Search `Rudi Hartono`, tekan Enter
27. Verifikasi Rudi Hartono tetap tampil di Tab Total Control
28. Klik `(←)` pada kotak Search

### TC-GS-ROLE-117: Remove baris role gagal 5xx

29. Klik Tab `System`
30. Klik Role Name `Manage files`
31. Ketik Search `Wawan Setiawan`, tekan Enter
32. Klik `(⋯)` pada baris Wawan Setiawan
33. Klik `Remove`
34. Pasang intercept pada respons Remove baris role: jawab 500
35. Klik `[Remove]` pada dialog Remove
36. Verifikasi toast error `Error, failed to remove user.`
37. Verifikasi dialog Remove tetap terbuka
38. Verifikasi `[Remove]` aktif kembali untuk retry
39. Lepas intercept 500
40. Klik `[Cancel]` pada dialog Remove
41. Verifikasi baris Wawan Setiawan tetap tampil

### TC-GS-ROLE-118: Remove baris role target Total Control gagal 5xx

42. Ganti isi kotak search dengan `Siti Nurhaliza`, tekan Enter
43. Klik `(⋯)` pada baris Siti Nurhaliza
44. Klik `Remove`
45. Pasang intercept pada respons Remove baris role: jawab 500
46. Klik `[Remove]` pada dialog Remove
47. Verifikasi toast error `Error, failed to remove user.`
48. Verifikasi dialog Remove tetap terbuka
49. Verifikasi `[Remove]` aktif kembali untuk retry
50. Lepas intercept 500
51. Klik `[Cancel]` pada dialog Remove
52. Verifikasi baris Siti Nurhaliza tetap tampil
53. Klik `(←)` pada kotak Search
54. Klik menu sidebar `Role & Permission`
55. Klik Tab `Total Control`
56. Ketik Search `Siti Nurhaliza`, tekan Enter
57. Verifikasi Siti Nurhaliza tetap tampil di Tab Total Control
58. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE dengan intercept parsial (prinsip 13b); kegagalan dipicu dengan `Spectra.intercept()` pada request browser, sehingga bukan `Mode: mock`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (108, 109, 117, 118) dipertahankan; tidak ada aksi yang menghapus data karena semua submit digagalkan.
- Expected b dan c TC-GS-ROLE-117 dan TC-GS-ROLE-118 (baris tetap ada) diasersi sesudah dialog ditutup lewat `[Cancel]` (langkah 41 dan 52), karena tabel tertutup dialog selama dialog terbuka; Expected c (dialog tetap terbuka dan `[Remove]` aktif) diasersi lebih dulu (langkah 37, 38, 48, dan 49) sesuai urutan state. Dialog `Remove Access` TC-GS-ROLE-118 untuk target Total Control dan dialog TC-GS-ROLE-117 untuk target biasa tidak diverifikasi isinya karena bukan Expected TC ini.
- Expected a sampai c TC-GS-ROLE-109 diurutkan menurut state: nilai checkbox saat dialog terbuka sebelum submit (langkah 13) dan setelah gagal (langkah 19) dibaca saat dialog masih terbuka, `[Cancel]` baru sesudahnya (langkah 21), lalu nilai tersimpan (langkah 22) dan Tab Total Control (langkah 27).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 8, 10, 11, 23, 26, 28, 31, 42, 53, 56, dan 58 (Search dan penutupan Search untuk menemukan baris); langkah 6, 20, 39, dan 50 (melepas intercept segera setelah pemicu, S-09; intercept dipasang pada langkah 2, 14, 34, dan 45); langkah 21, 40, dan 51 (menutup dialog); langkah 7 (muat ulang halaman); langkah 24, 25, 29, 30, 54, dan 55 (pindah tab, sidebar, dan Detail).
- Spec melewati sekitar 35 langkah (58 langkah) karena memuat empat TC kelas fault injection dengan intercept parsial, satu akun, dan data milik spec yang disiapkan sekali di hook, dan tiap klausa Expected dipecah menjadi satu `Verifikasi` (S-01). Satu kelas harness; tiap blok (Edit CRUD, Auto-Revert, Remove baris biasa, Remove baris target Total Control) memakai targetnya sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-ROLE-108 Expected c ("retry dilakukan dengan mencentang ulang") tidak menyebut hasil retry; spec hanya mengasersi bahwa sesudah muat ulang Update tetap unchecked dan tidak menjalankan retry.
  - TC-GS-ROLE-117 tidak menyebut baris Manage files milik Wawan Setiawan sebagai Given (Tabel Data Uji Dinamis #5 hanya mencatat baris Manage TAG untuk Wawan Setiawan); spec men-seed baris Manage files untuk Wawan Setiawan.
  - TC-GS-ROLE-108, 109, 117, dan 118 tidak menyebut apakah respons 5xx dipaksa dengan atau tanpa meneruskan request ke server; spec memaksa respons tanpa meneruskan request.
  - TC-GS-ROLE-109 Langkah Uji 3 ("Amati dialog dan checkbox") dan Expected c menyebut nilai checkbox "sebelum dan sesudah gagal"; spec membaca keduanya (langkah 13 dan 19).
  - TC-GS-ROLE-118 Dependensi TC-GS-ROLE-60 (Siti Nurhaliza menjadi Total Control lewat Assign); spec men-seed upgrade itu lewat API dan memulihkan Siti Nurhaliza ke Read Only.
