---
id: TC-GS-ROLE-E2E-070-resilience-tulis-assign-total-control-read-only-dan-role
title: "Resilience Tulis: Assign Total Control, Read Only, dan Role Gagal 5xx atau Timeout"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-64
  - TC-GS-ROLE-81
  - TC-GS-ROLE-97
  - TC-GS-ROLE-306
coverage:
  web: automated
---

# Resilience Tulis: Assign Total Control, Read Only, dan Role Gagal 5xx atau Timeout

## Prerequisites

- Mode: FE+BE dengan intercept parsial di atas backend nyata (bagian 6 konvensi; kelas harness fault injection, prinsip 13b).
- Akun aktor: Total Control, Ahmad Fauzi (`Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission > Total Control.
- Data Pre-setup (tetap di environment, hanya dibaca): Wawan Setiawan (Pre-setup #11) dalam kondisi kandidat: Active, Access Global Settings dicentang, tanpa access level, dan tanpa baris Manage hardware. Semua submit pada spec ini digagalkan oleh intercept tanpa meneruskan request ke server, sehingga state Wawan Setiawan tidak berubah dan tidak ada pemulihan data (S-06).
- Kebutuhan intercept (`Spectra.intercept()`), semuanya pada request tulis dan dilepas segera setelah dipakai; respons dipaksa tanpa meneruskan request ke server:
  - Assign Total Control dan Assign Read Only: `POST /v2/iam/products/{product}/roles/access-level` (`openapi.yaml`, `low-level-design.md`) dipaksa HTTP 500 (TC-GS-ROLE-64, 81);
  - Assign Total Control: request yang sama dipaksa timeout klien (respons ditahan melewati batas klien) (TC-GS-ROLE-306);
  - Assign Role: `POST /v2/iam/products/{product}/roles/capabilities/users` dipaksa HTTP 500 (TC-GS-ROLE-97).
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah): semua intercept dilepas; popup Assign ditutup. Spec tidak mengubah data Role.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-64: Assign Total Control gagal 5xx

1. Klik `[+ Assign]`
2. Ketik Search `Wawan Setiawan`, tekan Enter pada popup
3. Centang Wawan Setiawan
4. Pasang intercept pada respons Assign access level: jawab 500
5. Klik `[Assign]`
6. Verifikasi toast error `Error, failed to assign Total Control.`
7. Verifikasi popup tetap terbuka
8. Verifikasi Wawan Setiawan tetap tercentang
9. Verifikasi `[Assign]` enabled untuk retry

### TC-GS-ROLE-306: Assign Total Control gagal jaringan atau timeout

10. Lepas intercept 500
11. Pasang intercept pada respons Assign access level: timeout
12. Klik `[Assign]`
13. Verifikasi toast `Connection problem. Please try again.`
14. Verifikasi toast memuat tombol `[Try Again]`
15. Verifikasi popup tetap terbuka
16. Verifikasi Wawan Setiawan tetap tercentang
17. Verifikasi `[Assign]` enabled untuk retry
18. Lepas intercept timeout
19. Klik `[Cancel]`
20. Ketik Search `Wawan Setiawan`, tekan Enter pada tabel Tab Total Control
21. Verifikasi "No results found"
22. Klik `(←)` pada kotak Search

### TC-GS-ROLE-81: Assign Read Only gagal 5xx

23. Klik Tab `Read Only`
24. Klik `[+ Assign]`
25. Ketik Search `Wawan Setiawan`, tekan Enter pada popup
26. Centang Wawan Setiawan
27. Pasang intercept pada respons Assign access level: jawab 500
28. Klik `[Assign]`
29. Verifikasi toast error `Error, failed to assign Read Only.`
30. Verifikasi popup tetap terbuka
31. Verifikasi seleksi dipertahankan: Wawan Setiawan tetap tercentang
32. Lepas intercept 500
33. Klik `[Cancel]`
34. Ketik Search `Wawan Setiawan`, tekan Enter pada tabel Tab Read Only
35. Verifikasi "No results found"
36. Klik `(←)` pada kotak Search

### TC-GS-ROLE-97: Assign Role gagal 5xx

37. Klik Tab `System`
38. Klik Role Name `Manage hardware`
39. Klik `[+ Assign]`
40. Ketik Search `Wawan Setiawan`, tekan Enter pada popup
41. Centang Wawan Setiawan
42. Pasang intercept pada respons Assign Role: jawab 500
43. Klik `[Assign]`
44. Verifikasi toast error `Error, failed to assign role.`
45. Verifikasi popup tetap terbuka
46. Verifikasi seleksi dipertahankan: Wawan Setiawan tetap tercentang
47. Lepas intercept 500
48. Klik `[Cancel]`
49. Ketik Search `Wawan Setiawan`, tekan Enter pada tabel Detail "Manage hardware"
50. Verifikasi "No results found" (tidak ada baris baru)
51. Klik `(←)` pada kotak Search

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE dengan intercept parsial (prinsip 13b); kegagalan dipicu dengan `Spectra.intercept()` pada request browser, sehingga bukan `Mode: mock`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC diubah dari TC sumber (64, 81, 97, 306) menjadi 64, 306, 81, 97: popup Assign Total Control dari TC-GS-ROLE-64 dipakai ulang oleh TC-GS-ROLE-306 dengan seleksi Wawan Setiawan yang masih tercentang (prinsip 6 dan 8, hemat buka popup); Langkah Uji 1 sampai 3 TC-GS-ROLE-306 tidak ditulis ulang. TC-GS-ROLE-306 hanya mengganti intercept lalu klik ulang `[Assign]`.
- Expected c TC-GS-ROLE-64 dan TC-GS-ROLE-306 (Wawan Setiawan tidak muncul di Tab Total Control) diasersi satu kali sesudah kedua percobaan gagal (langkah 20 dan 21), karena popup yang sama dipakai ulang dan tabel tertutup popup selama popup terbuka; asersi ini berlaku untuk kedua TC.
- Langkah 2, 25, dan 40 (Search Wawan Setiawan di popup) menemukan baris yang dicentang karena kandidat dapat berada di halaman selain halaman 1 picker; TC hanya menulis "Centang Wawan Setiawan".
- Asersi absence (langkah 21, 35, dan 50) memakai empty state "No results found" hasil Search sebagai anchor positif yang sah (bagian 8b butir 2).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 10, 18, 32, dan 47 (melepas intercept segera setelah pemicu, S-09; intercept dipasang pada langkah 4, 11, 27, dan 42); langkah 19, 33, dan 48 (menutup popup lewat `[Cancel]` tanpa dialog `Unsaved Changes`, sesuai PRD role.md bagian Tutup Popup); langkah 20, 22, 34, 36, 49, dan 51 (Search dan penutupan Search pada tabel); langkah 23, 37, dan 38 (pindah tab dan membuka Detail "Manage hardware").
- Spec melewati sekitar 35 langkah (51 langkah) karena memuat empat TC kelas fault injection dengan intercept parsial yang berbagi satu akun dan satu data (Wawan Setiawan), dan tiap klausa Expected dipecah menjadi satu `Verifikasi` (S-01). Satu kelas harness; tiap blok (Total Control, Read Only, Role) berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-ROLE-64, 81, 97, dan 306 tidak menyebut apakah respons 5xx atau timeout dipaksa dengan atau tanpa meneruskan request ke server; spec memaksa respons tanpa meneruskan request.
  - TC-GS-ROLE-81 dan 97 mengisi Data Uji dengan "-" padahal Langkah Uji menyebut Wawan Setiawan; spec memakai Wawan Setiawan seperti pada Langkah Uji.
  - TC-GS-ROLE-81 Expected b dan TC-GS-ROLE-97 Expected b ("seleksi dipertahankan") tidak menyebut baris yang dimaksud; spec mengasersi Wawan Setiawan tetap tercentang.
  - TC-GS-ROLE-97 Expected c ("Tidak ada baris baru") tidak menyebut cara mengamatinya; spec memakai Search nama Wawan Setiawan pada tabel Detail "Manage hardware".
  - TC-GS-ROLE-64 dan 306 tidak menyebut pesan dan tombol dismiss toast 5xx saat toast timeout diverifikasi berikutnya; spec memverifikasi toast sesuai teks masing-masing.
