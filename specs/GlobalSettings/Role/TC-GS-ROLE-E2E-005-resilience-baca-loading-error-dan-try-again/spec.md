---
id: TC-GS-ROLE-E2E-005-resilience-baca-loading-error-dan-try-again
title: "Resilience Baca: Loading State per Surface, Error Load 5xx, dan Pulih lewat Try Again"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-15
  - TC-GS-ROLE-16
  - TC-GS-ROLE-17
coverage:
  web: automated
---

# Resilience Baca: Loading State per Surface, Error Load 5xx, dan Pulih lewat Try Again

## Prerequisites

- Mode: mock.
- Seluruh API di-mock (spec dijalankan tim FE sebagai integration test, tanpa backend nyata). Spec tidak memakai hook suite Guided Tooltip; flag `guided_tooltip_seen_gs-role` diatur lewat respons mock yang disediakan tim FE (seen = true).
- Aktor: Ahmad Fauzi (Total Control, Pre-setup #1) sebagai identitas mock dengan akses Global Settings. Karena API di-mock, tidak ada login nyata dan tidak ada password. API pendukung di luar sumber modul (identitas pengguna, menu sidebar, flag Guided Tooltip) disediakan tim FE.
- Layar awal: hook `beforeEach` hanya menyiapkan sesi mock dan membuka Portal; hook tidak membuka Role & Permission karena membuka tiap surface adalah objek uji (langkah buka ada di Test Steps).
- Endpoint yang dipanggil halaman pada kondisi uji (`global-settings/role/API/openapi.yaml`, awalan `/v2/iam/products/{product}/roles`, semuanya `POST`):
  - `/access-level/list` (Tab Total Control dan Tab Read Only; dibedakan oleh body `accessLevel`: `total_control` atau `read_only`)
  - `/access-level/options` (opsi Filter Tab Total Control dan Tab Read Only; dipanggil bila halaman memuatnya)
  - `/capabilities/list` (Tab System)
  - `/capabilities/users/list` (Detail role)
  - `/capabilities/users/options` (opsi Filter Detail; dipanggil bila halaman memuatnya)
  - `/assignable-users/list` dan `/assignable-users/options` (Table User Picker Popup Assign)
  - Data Modal Changelog: endpoint tidak tercantum di `openapi.yaml` maupun `low-level-design.md` modul ini; endpoint dan bentuk responsnya disediakan tim FE.
  - Aliran SSE `user.role_assigned` yang disebut `low-level-design.md` (bila halaman berlangganan) disediakan tim FE sebagai aliran tanpa event; endpoint aliran tidak disebut di sumber.
- Respons mock default tiap endpoint adalah 200 dengan data minimal sehingga tabel terisi: Tab Total Control (Ahmad Fauzi, Budi Santoso, Dewi Lestari), Tab Read Only (Siti Nurhaliza, Rina Putri), Tab System (enam role tetap), Detail "Manage TAG" (beberapa baris), Table User Picker (beberapa kandidat), dan Modal Changelog (beberapa entri).
- Kebutuhan mock per blok:
  - TC-GS-ROLE-15: semua respons list ditunda cukup lama untuk diamati (tim FE menetapkan durasi; dianjurkan ≥3 detik) tanpa mengubah isi respons. Penundaan dipasang di hook `before`, dilepas pada langkah 22, dan dilepas juga di hook `after` sebagai cadangan.
  - TC-GS-ROLE-16: `/access-level/list` untuk `accessLevel` `total_control` dijawab 500 sebanyak satu kali (body `message: Unable to load this data.`, `ReadError` di `openapi.yaml`), lalu kembali 200.
  - TC-GS-ROLE-17: respons 500 (body sama) dipasang per surface sesuai langkah "Atur mock ..." dan dipulihkan ke 200 pada langkah pemulihan.
- Pemicu kegagalan (langkah "Atur mock ...") adalah aksi pemasangan mock sebelum surface dibuka, bukan objek asersi; pemulihan dilakukan di langkah pemulihan dan di hook `after`.

## Test Steps

### TC-GS-ROLE-15: Loading state per surface

1. Buka Global Settings > Role & Permission (Tab Total Control)
2. Verifikasi loading component tampil sebelum tabel Tab Total Control terisi
3. Klik Tab Read Only
4. Verifikasi loading component tampil di Tab Read Only
5. Klik Tab System
6. Verifikasi loading component tampil di Tab System
7. Tunggu tabel Tab System termuat
8. Klik Role Name `Manage TAG`
9. Verifikasi loading component tampil di Detail
10. Tunggu tabel Detail termuat
11. Klik segmen "System" pada breadcrumb
12. Klik Tab Total Control
13. Tunggu tabel Tab Total Control termuat
14. Klik `[+ Assign]`
15. Verifikasi loading component tampil di tabel picker Popup Assign Total Control
16. Tunggu tabel picker termuat
17. Klik `✕` pada header Popup Assign Total Control
18. Klik Changelog
19. Verifikasi loading component tampil di Modal Changelog
20. Tunggu Modal Changelog termuat
21. Tutup Modal Changelog dengan `✕`

### TC-GS-ROLE-16: Error load Tab Total Control dan pulih via Try Again

22. Lepas penundaan respons mock, lalu atur mock `/access-level/list` untuk `accessLevel` `total_control` gagal 500 satu kali
23. Klik menu sidebar Role & Permission (Tab Total Control)
24. Verifikasi area tabel menampilkan "Unable to load this data."
25. Verifikasi area tabel menampilkan `[Try Again]`
26. Verifikasi area tabel bukan empty state
27. Klik `[Try Again]`
28. Verifikasi tabel Tab Total Control termuat normal

### TC-GS-ROLE-17: Error load pada Tab Read Only, Tab System, Detail, Table User Picker, dan Modal Changelog

29. Atur mock `/access-level/list` untuk `accessLevel` `read_only` gagal 500
30. Klik Tab Read Only
31. Verifikasi Tab Read Only menampilkan "Unable to load this data."
32. Verifikasi Tab Read Only menampilkan `[Try Again]`
33. Atur mock `/capabilities/list` gagal 500
34. Klik Tab System
35. Verifikasi Tab System menampilkan "Unable to load this data."
36. Verifikasi Tab System menampilkan `[Try Again]`
37. Pulihkan mock `/capabilities/list` dan `/access-level/list` ke 200, lalu atur mock `/capabilities/users/list` gagal 500
38. Klik `[Try Again]` pada Tab System
39. Klik Role Name `Manage TAG`
40. Verifikasi Detail menampilkan "Unable to load this data."
41. Verifikasi Detail menampilkan `[Try Again]`
42. Klik segmen "System" pada breadcrumb
43. Klik Tab Total Control
44. Tunggu tabel Tab Total Control termuat
45. Atur mock `/assignable-users/list` gagal 500
46. Klik `[+ Assign]`
47. Verifikasi area tabel picker Popup Assign Total Control menampilkan "Unable to load this data."
48. Verifikasi area tabel picker Popup Assign Total Control menampilkan `[Try Again]`
49. Klik `✕` pada header Popup Assign Total Control
50. Atur mock data Modal Changelog gagal 500
51. Klik Changelog
52. Verifikasi Modal Changelog menampilkan "Unable to load this data."
53. Verifikasi Modal Changelog menampilkan `[Try Again]`
54. Tutup Modal Changelog dengan `✕`

## Notes

- Mode: mock. Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Kelas harness: fault injection / resilience (kelas b) dengan seluruh API di-mock. TC-GS-ROLE-15 menahan respons hanya untuk mengamati state UI dan tidak memaksa kegagalan; ia berada di spec ini karena surface dan pemicunya sama dengan TC-GS-ROLE-16 dan TC-GS-ROLE-17 (satu spec per kelas per modul).
- Langkah penghubung (bukan dari TC sumber, tanpa `Verifikasi`): menunggu tabel termuat (langkah 7, 10, 13, 16, 20, 44) karena langkah berikutnya memakai baris atau tombol yang baru tersedia setelah termuat; berpindah surface lewat breadcrumb dan tab (langkah 11, 12, 42, 43); menutup popup dan modal (langkah 17, 21, 49, 54); memasang dan memulihkan mock (langkah 22, 29, 33, 37, 45, 50); `[Try Again]` pada Tab System (langkah 38) untuk memuat ulang sebelum membuka Detail.
- TC-GS-ROLE-17 memakai "idem" untuk Tab System, Detail, Popup Assign, dan Modal Changelog; spec mengasersi pesan "Unable to load this data." dan `[Try Again]` pada tiap surface sesuai butir a Expected. Klausa "bukan empty state" hanya disebut pada TC-GS-ROLE-16 (langkah 26) dan tidak diasersi pada TC-GS-ROLE-17.
- Respons mock sukses tidak dibaca ulang kecuali Expected TC memintanya (langkah 28 memverifikasi tabel termuat normal sesuai Expected TC-GS-ROLE-16 butir b).
- Spec melewati sekitar 35 langkah (54 langkah). Alasan: seluruh blok satu kelas harness (resilience baca, seluruh API di-mock) dan satu aktor; jumlah langkah berasal dari lima surface TC-GS-ROLE-17 dan enam surface TC-GS-ROLE-15, masing-masing dengan satu sampai tiga `Verifikasi` (S-01) dan langkah navigasi serta menunggu. Blok TC-GS-ROLE-15, TC-GS-ROLE-16, dan TC-GS-ROLE-17 masing-masing dimulai dari mock dan navigasinya sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - Endpoint data Modal Changelog tidak ada di `openapi.yaml` dan `low-level-design.md` modul; spec tidak mengarang endpoint dan menyebutnya "disediakan tim FE" (S-13).
  - TC-GS-ROLE-15 tidak menyebut durasi penundaan respons; spec menyerahkannya ke tim FE.
  - TC-GS-ROLE-17 butir a sampai e memakai "idem" tanpa menyebut apakah empty state juga harus tidak tampil; spec hanya mengasersi pesan dan `[Try Again]`.
