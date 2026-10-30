---
id: TC-GS-ROLE-E2E-073-resilience-tulis-bulk-remove-dan-sukses-parsial
title: "Resilience Tulis: Bulk Remove Gagal 5xx, Timeout, dan Sukses Parsial"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-133
  - TC-GS-ROLE-261
  - TC-GS-ROLE-309
coverage:
  web: automated
---

# Resilience Tulis: Bulk Remove Gagal 5xx, Timeout, dan Sukses Parsial

## Prerequisites

- Mode: FE+BE dengan intercept parsial di atas backend nyata (bagian 6 konvensi; kelas harness fault injection, prinsip 13b).
- Akun aktor: Total Control, Ahmad Fauzi (`Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission > System > Detail "Manage hardware".
- Data Dinamis milik spec (suffix per run dan nomor spec, bagian 5 konvensi), dua baris eligible di Detail "Manage hardware" (Active, Access Global Settings dicentang, tanpa access level), dibuat di hook `before`: user `Bulk Remove Satu {runId}-073` dan `Bulk Remove Dua {runId}-073` dibuat lewat kemampuan seeding user (modul User, disediakan tim FE; endpoint tidak tercantum di sumber modul Role), lalu masing-masing di-assign Role Manage hardware lewat API `POST /v2/iam/products/{product}/roles/capabilities/users` oleh akun Ahmad Fauzi (`openapi.yaml`). Search `{runId}-073` hanya mencocokkan kedua baris ini.
- Kebutuhan intercept (`Spectra.intercept()`) pada request Bulk Remove `DELETE /v2/iam/products/{product}/roles/capabilities/users` (`openapi.yaml`, `low-level-design.md`), dipasang dan dilepas lewat langkah eksplisit:
  - respons dipaksa HTTP 500 tanpa meneruskan request ke server (TC-GS-ROLE-133);
  - respons dipaksa timeout klien (respons ditahan melewati batas klien) tanpa meneruskan request ke server (TC-GS-ROLE-309);
  - sukses parsial (TC-GS-ROLE-261): request diteruskan ke server hanya dengan id user `Bulk Remove Satu {runId}-073`, sedangkan respons yang diterima browser diganti HTTP 200 dengan `failedUserIds` berisi id user `Bulk Remove Dua {runId}-073` (bentuk respons parsial pada `openapi.yaml`), sehingga baris pertama benar-benar terhapus di backend dan baris kedua tetap ada.
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah, tanpa berasumsi seeding berhasil penuh): semua intercept dilepas; dialog Bulk Remove ditutup; kedua user milik spec dihapus lewat kemampuan seeding user (disediakan tim FE). Entri Changelog tidak bisa dihapus.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-133: Bulk Remove gagal 5xx

1. Ketik Search `{runId}-073`, tekan Enter
2. Verifikasi baris `Bulk Remove Satu {runId}-073` tampil
3. Verifikasi baris `Bulk Remove Dua {runId}-073` tampil
4. Centang baris `Bulk Remove Satu {runId}-073`
5. Centang baris `Bulk Remove Dua {runId}-073`
6. Klik Bulk Action
7. Klik `Remove`
8. Pasang intercept pada respons Bulk Remove: jawab 500
9. Klik `[Remove]` pada dialog Bulk Remove
10. Verifikasi toast error `Error, failed to remove user.`
11. Verifikasi dialog Bulk Remove tetap terbuka
12. Verifikasi `[Remove]` aktif kembali untuk retry
13. Lepas intercept 500
14. Klik `[Cancel]` pada dialog Bulk Remove
15. Verifikasi kedua baris tetap tampil
16. Verifikasi kedua baris tetap tercentang
17. Verifikasi Bulk Action Bar tetap tampil

### TC-GS-ROLE-309: Bulk Remove gagal jaringan atau timeout

18. Klik Bulk Action
19. Klik `Remove`
20. Pasang intercept pada respons Bulk Remove: timeout
21. Klik `[Remove]` pada dialog Bulk Remove
22. Verifikasi toast `Connection problem. Please try again.`
23. Verifikasi toast memuat tombol `[Try Again]`
24. Verifikasi tidak ada toast `Error, failed to remove user.`
25. Verifikasi dialog Bulk Remove tetap terbuka
26. Verifikasi `[Remove]` aktif kembali untuk retry
27. Lepas intercept timeout
28. Klik `[Cancel]` pada dialog Bulk Remove
29. Verifikasi kedua baris tetap tampil
30. Verifikasi kedua baris tetap tercentang
31. Verifikasi Bulk Action Bar tetap tampil

### TC-GS-ROLE-261: Sukses parsial Bulk Remove menampilkan toast sukses parsial

32. Klik Bulk Action
33. Klik `Remove`
34. Pasang intercept sukses parsial pada respons Bulk Remove: hanya baris `Bulk Remove Satu {runId}-073` diteruskan ke server, baris `Bulk Remove Dua {runId}-073` dilaporkan gagal
35. Klik `[Remove]` pada dialog Bulk Remove
36. Verifikasi toast sukses `Success, user has been removed. Some items were skipped.`
37. Verifikasi baris `Bulk Remove Satu {runId}-073` hilang dari tabel
38. Verifikasi baris `Bulk Remove Dua {runId}-073` tetap tampil
39. Verifikasi Bulk Action Bar tertutup
40. Verifikasi seleksi di-reset ke 0 sehingga baris `Bulk Remove Dua {runId}-073` tidak tercentang
41. Lepas intercept sukses parsial
42. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE dengan intercept parsial (prinsip 13b); kegagalan dan sukses parsial dipicu dengan `Spectra.intercept()` pada request browser di atas backend nyata, sehingga bukan `Mode: mock`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC diubah dari TC sumber (133, 261, 309) menjadi 133, 309, 261: TC-GS-ROLE-261 menghapus satu baris di backend sehingga ditaruh paling akhir (bagian 3 prinsip 5), dan TC-GS-ROLE-133 serta TC-GS-ROLE-309 memakai kembali dua baris yang sama.
- Spec melewati sekitar 35 langkah (42 langkah) karena memuat tiga TC kelas fault injection dengan intercept parsial yang berbagi satu akun, satu Detail, dan dua baris data milik spec, dan tiap klausa Expected dipecah menjadi satu `Verifikasi` (S-01). Satu kelas harness; blok 5xx, timeout, dan sukses parsial masing-masing memasang intercept sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah Uji 1 TC-GS-ROLE-309 dan Langkah Uji 1 TC-GS-ROLE-261 ("centang 2 baris") dipenuhi oleh seleksi yang dipertahankan dari TC-GS-ROLE-133 (langkah 16 dan 30); keduanya tidak ditulis ulang. Langkah 1 sampai 3 memastikan kedua baris tampil sebelum dicentang (anchor positif).
- Expected b dan c TC-GS-ROLE-133 dan TC-GS-ROLE-309 (baris tetap ada dan tercentang, Bulk Action Bar tampil) diasersi sesudah dialog ditutup lewat `[Cancel]` (langkah 14 dan 28), karena tabel tertutup dialog selama dialog terbuka; Expected dialog tetap terbuka dan `[Remove]` aktif diasersi lebih dulu (langkah 11, 12, 25, dan 26) sesuai urutan state. Asersi "bukan toast `Error, failed to remove user.`" (langkah 24) diletakkan segera sesudah toast timeout muncul, yang menjadi anchor positifnya (langkah 22 dan 23; bagian 8b butir 11).
- Langkah 37 (baris hilang) didahului toast sukses langkah 36 sebagai anchor (bagian 8b butir 2).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 dan 42 (Search dan penutupan Search untuk menemukan baris), langkah 13, 27, dan 41 (melepas intercept segera setelah pemicu, S-09; intercept dipasang pada langkah 8, 20, dan 34), langkah 14 dan 28 (menutup dialog).
- Tidak ada TC yang terbelah lintas spec. Bulk Remove saat semua baris ditolak per baris (TC-GS-ROLE-299) dan Bulk Remove berhasil ada di spec lain.
- Temuan untuk QA:
  - TC-GS-ROLE-133, 261, dan 309 menyebut "2 baris eligible" tanpa menyebut user; spec memakai dua user milik spec bersuffix `{runId}-073` (S-06).
  - TC-GS-ROLE-261 menyebut "satu dari dua baris ditolak per baris" lewat intercept respons jaringan tanpa menyebut cara membuat satu baris benar-benar terhapus dan satu baris tetap ada; spec meneruskan request dengan satu id ke server dan mengganti respons dengan `failedUserIds` berisi id lain.
  - TC-GS-ROLE-133, 261, dan 309 tidak menyebut apakah respons 5xx atau timeout dipaksa dengan atau tanpa meneruskan request ke server; spec memaksa respons 5xx dan timeout tanpa meneruskan request.
  - TC-GS-ROLE-261 Expected a menyebut toast sukses parsial "Success, user has been removed. Some items were skipped.", sedangkan `openapi.yaml` memberi contoh pesan parsial `2 removed, 1 failed.`; spec mengikuti teks TC (NC-03 di `tc-role.md` berstatus Dikonfirmasi).
  - Endpoint pembuatan dan penghapusan user untuk seeding berada di modul User dan tidak tercantum di sumber modul Role; kemampuannya disediakan tim FE (S-13).
